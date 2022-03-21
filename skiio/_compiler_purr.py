from typing import Set, List, Dict, Optional, Tuple, cast
from dataclasses import dataclass
from enum import Enum, unique
import re
import string
import warnings

from ._skinode import SKInode, NodeType, SKInode_T, sub
from .utils import skibyte
from ._exceptions import *
from ._compiler_ski import compile_node_to_ski

warnings.formatwarning = lambda msg, *args, **kwargs: f"[-] PurrWarning: {msg}"

_VALID_NAME_REGEX: re.Pattern = re.compile(r"[a-zA-Z0-9_]+")
_VALID_CHURCH_INT: re.Pattern = re.compile(r"([a-zA-Z0-9]|[0-9]{2})(?:[^a-zA-Z0-9]|$)")

_RESERVED_NAMES: Dict[str, str] = {
    "ATOM_OUT": "o",
    "ATOM_IN": "i",
    "ATOM_S": "S",
    "ATOM_K": "K",
    "ATOM_I": "I",
}
_CHUCH_LETTERS: str = string.digits + string.ascii_letters


@unique
class TokenType(Enum):

    NONE = 0

    NAME = 1
    RESERVED_NAME = 2

    DECL_START = 3
    DECL_MID = 4
    DECL_END = 5

    CALL_START = 6
    CALL_MID = 7
    CALL_END = 8

    MACRO_START = 9
    MACRO_END = 10

    CHURCH_ENC = 11

    MAIN_START = 12


@dataclass
class Token:

    line: int
    col: int
    type: TokenType
    tok: str

    def __hash__(self):
        return (hash(self.line) << 16) ^ (hash(self.col) << 16)

    def __str__(self):
        return self.tok


def _tokenize(code: str) -> List[Token]:

    codelines = code.split("\n")
    tokens = []

    for lno, line in enumerate(codelines):

        lno += 1
        cno = 0
        while cno < len(line):

            char = line[cno]

            # End of line
            if char == ";":
                break

            elif char in string.whitespace:
                pass

            elif char == "#":
                tokens.append(Token(lno, cno, TokenType.MACRO_START, char))

            elif char == "~":
                tokens.append(Token(lno, cno, TokenType.MACRO_END, char))

            elif char == "[":
                tokens.append(Token(lno, cno, TokenType.DECL_START, char))

            elif char == ":":
                tokens.append(Token(lno, cno, TokenType.DECL_MID, char))

            elif char == "]":
                tokens.append(Token(lno, cno, TokenType.DECL_END, char))

            elif char == "(":
                tokens.append(Token(lno, cno, TokenType.CALL_START, char))

            elif char == ")":
                tokens.append(Token(lno, cno, TokenType.CALL_END, char))

            elif char == "!":
                tokens.append(Token(lno, cno, TokenType.MAIN_START, char))

            elif char == ".":

                match = _VALID_CHURCH_INT.match(line[cno + 1 :])
                if not match:
                    raise PurrCompileSyntaxException(
                        f"Invalid church token! `{line[cno:]}...`", lno, cno
                    )
                tok = "." + match.group(1)
                tokens.append(Token(lno, cno, TokenType.CHURCH_ENC, tok))

                cno += len(tok)
                continue

            elif match := _VALID_NAME_REGEX.match(line[cno:]):

                tok = match.group()
                tokens.append(
                    Token(
                        lno,
                        cno,
                        TokenType.RESERVED_NAME
                        if tok in _RESERVED_NAMES
                        else TokenType.NAME,
                        tok,
                    )
                )

                cno += len(tok)
                continue

            else:
                raise PurrCompileSyntaxException(
                    f"Unknown token! `{line[cno:]}...`", lno, cno
                )

            cno += 1

    return tokens


def _build_globals_dict(tokens: List[Token]) -> Dict[Token, List[Token]]:

    ret: Dict[Token, List[Token]] = {}
    acc: Optional[List[Token]] = None
    macro_name = None

    has_main = False

    ptr = 0
    while ptr < len(tokens):

        tok = tokens[ptr]

        if tok.type == TokenType.MACRO_START:
            acc = []
            macro_name = tokens[ptr + 1]

            if macro_name.type != TokenType.NAME:
                if macro_name.type == TokenType.RESERVED_NAME:
                    raise PurrCompileSyntaxException(
                        f"Cannot use reserved name `{macro_name}` as variable name!",
                        macro_name.line,
                        macro_name.col,
                    )
                raise PurrCompileSyntaxException(
                    f"Unexpected token: `{macro_name}`, expected a variable name!",
                    macro_name.line,
                    macro_name.col,
                )

            ptr += 2
            continue

        if tok.type == TokenType.MAIN_START:

            if has_main:
                raise PurrCompileASTException(
                    "Entry point redefinition!", tok.line, tok.col
                )

            acc = []
            macro_name = tok
            ptr += 1
            has_main = True
            continue

        elif tok.type == TokenType.MACRO_END:

            if acc is None:
                raise PurrCompileSyntaxException(
                    "Unexpected token! `~` encountered before start of macro",
                    tok.line,
                    tok.col,
                )

            ret[cast(Token, macro_name)] = acc
            acc = None
            ptr += 1
            continue

        if acc is not None:
            acc.append(tok)

        ptr += 1

    if ret is None:
        raise PurrCompileASTException("Empty program!", -1, -1)

    if not has_main:
        raise PurrCompileASTException("Program has no entry point!", -1, -1)

    return ret


def _get_balancing_bracket(
    tokens: List[Token], start: TokenType, end: TokenType
) -> int:

    t = tokens[0]
    if t.type != start:
        raise PurrCompileInternalException(
            f"Invalid call to `_get_balancing_bracket`! `{t}..`"
            + "`tokens` must start with a token of type `start`",
            t.line,
            t.col,
        )

    depth = 0
    for idx, tok in enumerate(tokens):

        if tok.type == start:
            depth += 1
        elif tok.type == end:
            depth -= 1

        if depth == 0:
            return idx

    raise PurrCompileSyntaxException(
        f"No closing bracket found for `{t}`", t.line, t.col
    )


def _build_macro(
    tokens: List[Token], namespace: Optional[Dict[str, Token]] = None
) -> Tuple[SKInode_T, Dict[str, List[Token]]]:

    if namespace is None:
        namespace = {}

    if len(tokens) == 0:
        raise PurrCompileInternalException("Macro is empty!", -1, -1)

    tok = tokens[0]
    if tok.type == TokenType.DECL_START:

        if len(tokens) < 5:
            raise PurrCompileSyntaxException(
                "Incomplete declaration!", tok.line, tok.col
            )

        t1, t2 = tokens[1], tokens[2]

        # [x:y] at x
        if t1.type != TokenType.NAME:
            if t1.type == TokenType.RESERVED_NAME:
                raise PurrCompileSyntaxException(
                    f"Cannot use reserved name `{t1}` as variable name!",
                    t1.line,
                    t1.col,
                )
            raise PurrCompileSyntaxException(
                f"Unexpected token: `{t1}`, expected a variable name!", t1.line, t1.col
            )

        namespace = namespace.copy()
        namespace[t1.tok] = t1

        # [x:y] at :
        if t2.type != TokenType.DECL_MID:
            raise PurrCompileSyntaxException(
                f"Unexpected token: `{t2}`, expected `:`", t2.line, t2.col
            )

        # [x:y] at y
        defi = _get_balancing_bracket(tokens, TokenType.DECL_START, TokenType.DECL_END)
        definode, free = _build_macro(tokens[3:defi], namespace)
        node: SKInode_T = SKInode(NodeType.DECL, (t1.tok, definode))
        idx = defi + 1  # Points to after the function

    elif tok.type == TokenType.CALL_START:

        argi = _get_balancing_bracket(tokens, TokenType.CALL_START, TokenType.CALL_END)
        node, free = _build_macro(tokens[1:argi], namespace)
        idx = argi + 1  # Points to after function

    elif tok.type == TokenType.NAME or tok.type == TokenType.RESERVED_NAME:

        if tok.tok in namespace.keys():
            node = tok.tok
            free = {}
        else:
            node = tok.tok
            free = {tok.tok: [tok]}
        idx = 1

    elif tok.type == TokenType.CHURCH_ENC:

        if len(tok.tok) == 2:  # Of the form .<char>
            val = ord(tok.tok[1:])
        elif len(tok.tok) == 3:  # Of the form .<hex-byte>
            val = int(tok.tok[1:], 16)
        else:
            raise PurrCompileSyntaxException(
                f"Token `{tok}` is an invalid church encoding! "
                + "Expected the form .<char> (e.g. .H) or .<hex-byte> (e.g. .0f)",
                tok.line,
                tok.col,
            )

        if val >= 0x100:
            raise PurrCompileASTException(
                f"Token `{tok}` represents a church encoding more than 0x100! "
                + "Only support chuch encodings 0 <= n < 0x100",
                tok.line,
                tok.col,
            )

        node = f".{format(val, '02x')}"
        tok.tok = node
        free = {tok.tok: [tok]}
        idx = 1

    else:
        raise PurrCompileSyntaxException(
            f"Unexpected token: `{tok}`, expected a "
            + "name, church encoding, or function",
            tok.line,
            tok.col,
        )

    while idx < len(tokens):

        tok = tokens[idx]
        if tok.type != TokenType.CALL_START:
            raise PurrCompileSyntaxException(
                f"Unexpected token: `{tok}`, expected `(`", tok.line, tok.col
            )

        argi = (
            _get_balancing_bracket(
                tokens[idx:], TokenType.CALL_START, TokenType.CALL_END
            )
            + idx
        )

        ntokens = tokens[idx + 1 : argi]
        nnode, nfree = _build_macro(ntokens, namespace)

        # Combine
        node = SKInode(NodeType.CALL, (node, nnode))
        _free: Dict[str, List[Token]] = {}
        for k, v in free.items():
            if k not in _free:
                _free[k] = []
            _free[k].extend(v)
        for k, v in nfree.items():
            if k not in _free:
                _free[k] = []
            _free[k].extend(v)
        free = _free

        idx = argi + 1

    return node, free


def _topological_sort_macros(
    adjacency: Dict[Token, List[Token]],
    start: Token,
    _marked: Optional[Dict[Token, bool]] = None,
    _childs: Optional[List[Token]] = None,
    _acc: Optional[Tuple[Token]] = None,
) -> List[Token]:

    if _marked is None:
        _marked = {}
    if _acc is None:
        _acc = []
    if _childs is None:
        _childs = ()

    _childs = (*_childs, start)
    if start in _marked:

        suc = _marked[start]
        if suc:
            return _acc

        loop = _childs[_childs.index(start) :]
        raise PurrCompileASTException(
            f"Recursive macro! `{'->'.join(map(str, loop))}`", start.line, start.col
        )

    _marked[start] = False
    for n in adjacency[start]:
        _acc = _topological_sort_macros(adjacency, n, _marked, _childs, _acc)

    _marked[start] = True
    _acc.append(start)
    return _acc


def compile_purr_to_node(code: str) -> SKInode_T:

    tokens = _tokenize(code)
    macros = _build_globals_dict(tokens)

    macro_nodes = {k: _build_macro(m) for k, m in macros.items()}
    str_token_map = {t.tok: t for t in macro_nodes.keys()}

    adjacency = {}
    church_encodings: Set[str] = set()
    for k, (_, f) in macro_nodes.items():
        adjk = []
        for t in f.keys():

            # A free variable isn't one of the defined macros
            if t not in str_token_map:

                # If free variable is a reserved word, then it's fine
                # since it's predefined.
                if t in _RESERVED_NAMES:
                    continue

                # It could also be a church encoding
                if t[0] == ".":
                    church_encodings.add(t)
                    continue

                tok = f[t][0]  # Just raise error on first instance
                raise PurrCompileASTException(
                    f"Unknown macro reference `{tok}`!", tok.line, tok.col
                )

            adjk.append(str_token_map[t])

        adjacency[k] = adjk

    macro_order_keys = _topological_sort_macros(adjacency, str_token_map["!"])[::-1]
    unused_macros = set(macro_nodes.keys()) - set(macro_order_keys)
    if unused_macros:
        warnings.warn(f"Unused macros: {[*map(str, unused_macros)]}")

    macro_order_nodes = [macro_nodes[m][0] for m in macro_order_keys]
    node = macro_order_nodes[0]
    for k, n in zip(macro_order_keys[1:], macro_order_nodes[1:]):
        # [k:node](n)
        # Effectively letting `node` access `n` via variable name `k`
        node = SKInode(NodeType.CALL, (SKInode(NodeType.DECL, (k.tok, node)), n))

    # Substitute all the Purr's atoms for SKInode's atoms
    for a, b in _RESERVED_NAMES.items():
        node = sub(node, a, b)

    return node, church_encodings


def compile_purr_to_ski_str(code: str) -> str:

    node, church = compile_purr_to_node(code)
    ski = compile_node_to_ski(node)

    # Replace church encodings with SKI equivalent
    for c in church:
        val = int(c[1:], 16)
        ski = sub(ski, c, skibyte.SKI_byte[val])

    header = "\n".join(
        [
            "; +-----------------------------+",
            "; | Compiled from Purr   /\_/\  |",
            "; | Purr Source: -.-    (:o.o<) |",
            "; +----------------------> ^ <--+",
            ";",
        ]
    )
    code = "\n".join(";    |" + l for l in code.split("\n"))
    return f"{header}\n{code}\n\n{ski}"
