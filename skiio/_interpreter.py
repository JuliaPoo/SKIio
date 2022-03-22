from ._skinode import *
from ._exceptions import *
from .utils import skibyte

import sys
from typing import Deque, Union, Tuple, Any, Optional
from functools import lru_cache
from collections import deque

_SKIEvalElement_T = Union[str, int]
_SKIEvalNode_T = Union[
    # mypy still doesn't support recursive types
    Tuple[Any, Any],  # Supposed to be _SKIEvalNode_T
    _SKIEvalElement_T,
]
_SKIEvalStack_T = Deque[_SKIEvalNode_T]


@lru_cache(maxsize=None)
def _to_SKIEvalNode(expr: SKInode_T) -> _SKIEvalNode_T:

    if isinstance(expr, str):
        if expr.isdigit():
            return int(expr)
        return expr

    if expr.node_type == NodeType.DECL:
        expr_str = str(expr)
        raise SKIioInterpreterException(
            "Expression "
            + (expr_str[:10] + "... " if len(expr_str) > 10 else " ")
            + "contains a declaration! Compile to SKI first with `compile_to_SKI`"
        )

    c1, c2 = expr.childs
    return (_to_SKIEvalNode(c1), _to_SKIEvalNode(c2))


@lru_cache(maxsize=None)
def _SKIEvalNode_str(expr: Optional[_SKIEvalNode_T]) -> str:

    if not isinstance(expr, tuple):
        return str(expr)

    c1, c2 = expr
    return f"{_SKIEvalNode_str(c1)}({_SKIEvalNode_str(c2)})"


def _SKIEvalStack_str(stack: _SKIEvalStack_T) -> str:

    return ", ".join(map(_SKIEvalNode_str, stack))


def _atom_i(expr: _SKIEvalNode_T) -> _SKIEvalNode_T:

    char = ord(sys.stdin.read(1))
    if char >= 256:
        raise SKIioInterpreterException(
            "Error running `i` combinator! "
            + f"`{chr(char)}` isn't supported! Only ord(char) < 256 is supported"
        )
    return _to_SKIEvalNode(skibyte.SKI_byte[char])


def _atom_p(expr: _SKIEvalNode_T) -> _SKIEvalNode_T:

    if not isinstance(expr, int):
        raise SKIioInterpreterException(
            "Error running `o` combinator! "
            + "Attempted to print "
            + f"`{expr}` which isn't an integer! "
        )

    # print("-->", expr, "<--")
    sys.stdout.write(chr(expr))

    return "I"


def interpret_SKI(expr: SKInode_T, dbg: bool = False) -> str:

    curr: _SKIEvalNode_T = _to_SKIEvalNode(expr)
    hold: _SKIEvalStack_T = deque()
    ret: _SKIEvalStack_T = deque()

    def state() -> str:
        if not dbg:
            return ""
        return (
            _SKIEvalStack_str(ret)
            + " | "
            + _SKIEvalNode_str(curr)
            + " | "
            + _SKIEvalStack_str(hold)
        )

    while True:

        if dbg:
            print(">>", state())
            input()

        # ret, a(b) => [b, ret], a
        if isinstance(curr, tuple):
            c1, c2 = curr
            ret.appendleft(c2)
            curr = c1

        # [., ret], n, [x, hold] => [ret], x(n), [hold]
        elif len(ret) > 0 and ret[0] == ".":
            if len(hold) < 1:
                raise SKIioInterpreterException(
                    "Corrupted program! "
                    + "Check if you are using the `i` and `o` combinators correctly."
                )
            ret.popleft()
            curr = (hold.popleft(), curr)

        # I(a) => a
        # [a,ret], I => [ret], a
        elif curr == "I":
            if len(ret) < 1:
                break
            curr = ret.popleft()

        # K(a)(b) => a
        # [a,b,ret], K => [ret], a
        elif curr == "K":
            if len(ret) < 2:
                break
            curr = ret.popleft()
            ret.popleft()

        # S(a)(b)(c) => a(c)(b(c))
        # [a,b,c,ret], S => [c, b(c), ret], a
        elif curr == "S":
            if len(ret) < 3:
                break
            curr = ret.popleft()
            b = ret.popleft()
            c = ret.popleft()
            ret.extendleft([(b, c), c])

        # i(a) => n
        # [a, ret], i => [ret], n
        elif curr == "i":
            if len(ret) < 1:
                break
            curr = _atom_i(ret.popleft())

        # o(a) => p(a(u)(0))
        # [a, ret], o => [a(u)(0), ret], p
        elif curr == "o":
            if len(ret) < 1:
                break
            ret[0] = ((ret[0], "u"), 0)
            curr = "p"

        # u(n) => n+1
        # [n, ret], u => [ret], n+1 (if n is int)
        # [n, ret], u, [hold] => [., ret], n, [u, hold]
        elif curr == "u":
            if len(ret) < 1:
                break
            n = ret.popleft()
            if isinstance(n, int):
                curr = n + 1
            else:
                hold.appendleft(curr)
                ret.appendleft(".")
                curr = n

        # p(n) => I
        # [n, ret], p => [ret], I (if n is int)
        # [n, ret], p, [hold] => [., ret], n, [p, hold]
        elif curr == "p":
            if len(ret) < 1:
                break
            n = ret.popleft()
            if isinstance(n, int):
                curr = _atom_p(n)
            else:
                hold.appendleft(curr)
                ret.appendleft(".")
                curr = n

        else:
            raise SKIioInterpreterException(
                f"Unexpected state! "
                + f"Check if you are using the `i` and `o` combinators correctly. {state()}"
            )

    if hold:
        raise SKIioInterpreterException(
            f"Failed to fully execute program! "
            + f"Check if you are using the `i` and `o` combinators correctly. {state()}"
        )

    for r in ret:
        curr = (curr, r)

    return _SKIEvalNode_str(curr)


def interpret_SKI_from_str(code: str, dbg: bool = False) -> str:

    ski = ""
    for line in code.split("\n"):
        ski += line.split(";")[0]
    skinode = SKInode.from_str(ski)

    return interpret_SKI(skinode, dbg)
