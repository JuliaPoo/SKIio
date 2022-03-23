from ._exceptions import *

from dataclasses import dataclass
from typing import Tuple, Literal, Union, List, Any, Dict, Set, Optional, Type, cast
from enum import Enum, unique
import string
import re

ATOMS: Dict[str, str] = {
    "S": "[x:[y:[z:x(z)(y(z))]]]",
    "K": "[x:[y:x]]",
    "I": "[x:x]",
    "i": "i",
    "o": "o",
}

_VALID_NAME_REGEX: str = r"[a-zA-Z0-9_\.]+"

SKInode_T = Union["SKInode", str]


def gen_new_name(avoid: List[str] = [], prefix: str = "") -> str:
    names = string.ascii_lowercase + string.ascii_uppercase
    for n in names:
        n = prefix + n
        if n in avoid:
            continue
        return n
    raise SKIioInternalException("Ran out of variable names")


@unique
class NodeType(Enum):
    DECL = 0
    CALL = 1


@dataclass
class SKInode:

    node_type: Literal[NodeType.DECL, NodeType.CALL]
    childs: Tuple[SKInode_T, SKInode_T]

    @staticmethod
    def _to_str(node: SKInode_T, minimise: bool = False) -> str:

        if isinstance(node, str):
            return node

        ntype = node.node_type
        if ntype == NodeType.DECL:
            argname, defi = node.childs
            return "[%s:%s]" % (argname, SKInode._to_str(defi, minimise))

        elif ntype == NodeType.CALL:
            a, b = node.childs
            a = SKInode._to_str(a, minimise)
            if minimise:
                return str(a) + (
                    b if isinstance(b, str) else "(%s)" % SKInode._to_str(b, minimise)
                )
            return str(a) + "(%s)" % SKInode._to_str(b, minimise)

        else:
            raise SKIioInternalException("Unexpected NodeType!")

    def __str__(self) -> str:
        return self._to_str(self)

    def __hash__(self) -> int:
        return hash(str(self))

    @staticmethod
    def _eq(node1: SKInode_T, node2: SKInode_T, ctx1: Dict[str, int], ctx2: Dict[str, int]) -> bool:

        if type(node1) is not type(node2):
            return False

        # Both nodes are leafs
        if isinstance(node1, str):

            node2 = cast(str, node2)

            free1, free2 = node1 in ctx1, node2 in ctx2
            if free1 != free2:
                return False

            # Both leafs are free
            if free1 and free2:
                # Check if leafs reference same variable
                return ctx1[node1] == ctx2[node2]

            # Both leafs are not free
            return node1 == node2

        node2 = cast(SKInode, node2)

        # Both nodes are SKInodes
        if node1.node_type != node2.node_type:
            return False

        # Both nodes are declarations
        if node1.node_type == NodeType.DECL:

            arg1, defi1 = node1.childs
            arg2, defi2 = node2.childs

            # Add free variables to context
            ctx1, ctx2 = ctx1.copy(), ctx2.copy()
            ctx1[cast(str, arg1)] = max(ctx1.values()) + 1
            ctx2[cast(str, arg2)] = max(ctx2.values()) + 1

            return SKInode._eq(defi1, defi2, ctx1, ctx2)

        # Both nodes are calls
        if node1.node_type == NodeType.CALL:

            # Check if all children are equal
            for c1, c2 in zip(node1.childs, node2.childs):
                if not SKInode._eq(c1, c2, ctx1, ctx2):
                    return False

            return True

        raise SKIioInternalException("Unexpected NodeType!")

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, SKInode):
            return False
        return self._eq(self, other, {":": 0}, {":": 0})

    def __repr__(self) -> str:
        return str(self)

    @staticmethod
    def _is_valid_name(name: str) -> bool:
        return bool(re.match("^%s$" % _VALID_NAME_REGEX, name))

    @staticmethod
    def _tokenize(code: str) -> List[str]:

        tokens = cast(List[str], [])
        idx = 0
        while True:

            if idx == len(code):
                break
            c = code[idx]

            if c in "[]():":
                tokens.append(c)
            elif match := re.match("^" + _VALID_NAME_REGEX, code[idx:]):
                if not match:
                    code_snippet = code[idx : min(len(code) - 1, idx + 10)]
                    raise SKIioInternalException(
                        "Invalid name `%s...`!" % (code_snippet)
                    )
                obj_str = match.group()
                tokens.append(obj_str)
                idx += len(obj_str)
                continue

            idx += 1

        return tokens

    @staticmethod
    def _get_end_bracket(tokens: List[str], idx: int) -> int:

        start = tokens[idx]
        end = {"(": ")", "[": "]"}[start]
        depth = 0
        while True:
            if idx == len(tokens):
                break
            t = tokens[idx]
            depth += t == start
            depth -= t == end
            if depth == 0:
                return idx
            idx += 1
        raise SKIioInternalException("Unbalanced brackets `%s`" % start)

    @staticmethod
    def _to_node(tokens: List[str]) -> SKInode_T:

        self_T = SKInode

        t = tokens[0]
        if len(tokens) == 1:
            if not self_T._is_valid_name(t):
                raise SKIioInternalException("Invalid name %s" % t)
            return t

        if t == "(":
            idx = self_T._get_end_bracket(tokens, 0)
            node = self_T._to_node(tokens[1:idx])

        elif t == "[":
            if len(tokens) < 5:
                raise SKIioInternalException("Incomplete declaration!")
            t1, t2 = tokens[1], tokens[2]
            if not self_T._is_valid_name(t1):
                raise SKIioInternalException("Invalid argname %s" % t1)
            if t2 != ":":
                raise SKIioInternalException("Expected `:`, not %s" % t2)

            idx = self_T._get_end_bracket(tokens, 0)
            node = SKInode(NodeType.DECL, (t1, self_T._to_node(tokens[3:idx])))

        else:
            if not self_T._is_valid_name(t):
                raise SKIioInternalException("Invalid name %s" % t)
            t1 = tokens[1]
            if t1 != "(":
                raise SKIioInternalException("Expected `(`, not %s" % t1)

            idx = self_T._get_end_bracket(tokens, 1)
            node = SKInode(NodeType.CALL, (t, self_T._to_node(tokens[2:idx])))

        while idx != len(tokens) - 1:
            tmp = idx
            t = tokens[tmp + 1]
            if t != "(":
                raise SKIioInternalException("Expected `(`, not %s" % t)

            idx = self_T._get_end_bracket(tokens, tmp + 1)
            node = SKInode(
                NodeType.CALL, (node, self_T._to_node(tokens[tmp + 2 : idx]))
            )

        return node

    @classmethod
    def from_str(cls: Type["SKInode"], code: str) -> SKInode_T:
        tokens = cls._tokenize(code)
        return cls._to_node(tokens)


def is_free(expr: SKInode_T, varname: str) -> bool:

    if isinstance(expr, str):
        return expr == varname

    t = expr.node_type
    c1, c2 = expr.childs
    if t == NodeType.DECL:
        if c1 == varname:
            return False
        return is_free(c2, varname)
    if t == NodeType.CALL:
        ret = is_free(c1, varname)
        ret |= is_free(c2, varname)
        return ret
    raise SKIioInternalException("Unexpected NodeType!")


def get_all_free(expr: SKInode_T, _ctx: Optional[Set[str]] = None) -> Set[str]:

    if _ctx is None:
        _ctx = cast(Set[str], set())
    
    if isinstance(expr, str):
        if expr in _ctx:
            return cast(Set[str], set())
        return set([expr])

    t = expr.node_type
    c1, c2 = expr.childs
    if t == NodeType.DECL:
        (_ctx := _ctx.copy()).add(cast(str, c1))
        return get_all_free(c2, _ctx)
    if t == NodeType.CALL:
        ret1 = get_all_free(c1, _ctx)
        ret2 = get_all_free(c2, _ctx)
        return ret1 | ret2
    raise SKIioInternalException("Unexpected NodeType!")


def _sub(
    expr: SKInode_T, varname: str, repl: SKInode_T, _repl_free: List[str], _ctx: Optional[Set[str]] = None
) -> SKInode_T:

    if _ctx is None:
        _ctx = cast(Set[str], set())
    
    if isinstance(expr, str):
        if expr == varname:
            return repl
        return expr

    t = expr.node_type
    c1, c2 = expr.childs

    if t == NodeType.DECL:
        c1 = cast(str, c1)
        (_ctx := _ctx.copy()).add(c1)
        if c1 == varname:
            return expr
        if c1 in _repl_free:
            new_c1 = gen_new_name(avoid=_repl_free + list(_ctx))
            (_ctx := _ctx.copy()).add(new_c1)
            c2 = sub(c2, c1, new_c1, _ctx)
            c1 = new_c1
        c2 = _sub(c2, varname, repl, _repl_free, _ctx)
        return SKInode(t, (c1, c2))

    if t == NodeType.CALL:
        c1 = _sub(c1, varname, repl, _repl_free, _ctx)
        c2 = _sub(c2, varname, repl, _repl_free, _ctx)
        return SKInode(t, (c1, c2))

    raise SKIioInternalException("Unexpected NodeType!")


def sub(expr: SKInode_T, varname: str, repl: SKInode_T, ctx: Optional[Set[str]] = None) -> SKInode_T:

    if ctx is None:
        ctx = cast(Set[str], set())

    repl_free = list(get_all_free(repl))
    return _sub(expr, varname, repl, repl_free, ctx)


def beta_eta_reduce(
    expr: SKInode_T,
    max_depth: int = 500,
    raise_error: bool =True,
    _ctx: Optional[Set[str]] = None,
    _depth: int = 0,
) -> SKInode_T:

    if _ctx is None:
        _ctx = cast(Set[str], set())

    if _depth == max_depth:
        if raise_error:
            raise SKIioInternalException(
                "`beta_eta_reduce` Max depth `%d` reached" % max_depth
            )
        return expr
    _depth += 1

    if isinstance(expr, str):
        if expr in ATOMS and expr not in _ctx:
            return SKInode.from_str(ATOMS[expr])
        return expr

    # Shortforms
    def B(e:SKInode_T, _c:Set[str], _d:int):
        return beta_eta_reduce(e, max_depth, raise_error, _c, _d)

    N, C, D = SKInode, NodeType.CALL, NodeType.DECL

    t = expr.node_type
    c1, c2 = expr.childs

    if t == C:

        c2 = B(c2, _ctx, _depth)
        if isinstance(c1, N) and c1.node_type == D:
            n, fn = c1.childs
            (_ctx := _ctx.copy()).add(cast(str, n))
            return B(sub(fn, cast(str, n), c2, _ctx), _ctx, _depth)

        if isinstance(c1, str):
            if c1 in "SKI" and c1 not in _ctx:
                c1 = SKInode.from_str(ATOMS[c1])
                return B(N(t, (c1, c2)), _ctx, _depth)
            return N(t, (c1, c2))

        c1 = B(c1, _ctx, _depth)
        if isinstance(c1, N) and c1.node_type == D:
            return B(N(t, (c1, c2)), _ctx, _depth)

        return N(t, (c1, c2))

    if t == D:

        c1 = cast(str, c1)

        if isinstance(c2, N) and c2.node_type == C:
            d1, d2 = c2.childs
            if d2 == c1 and not is_free(d1, c1):
                return B(d1, _ctx, _depth)

        (_ctx := _ctx.copy()).add(c1)
        c2 = B(c2, _ctx, _depth)
        return N(t, (c1, c2))

    raise SKIioInternalException("Unexpected NodeType!")
