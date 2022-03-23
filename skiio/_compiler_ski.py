from ._skinode import SKInode, NodeType, SKInode_T, is_free
from ._rule import Rule
from ._exceptions import *


from typing import List, cast
from functools import lru_cache


_OPTIMIZATION_RULES: List[Rule] = [
    Rule("M(L)(N(L))", "S(M)(N)(L)"),
    Rule("S(K(S(K(A))))(S(K(S(K(B))))(C))", "S(K(S(K(S(K(A))(B)))))(C)"),
    Rule("S(K(S(K(A))))(S(K(B)))", "S(K(S(K(A))(B)))"),
    Rule("S(K(A))(K(B))", "K(A(B))"),
    Rule("S(K(A))(I)", "A"),
    Rule("S(S(K(A))(B))(K(C))", "S(K(S(A)(K(C))))(B)"),
    Rule("S(S(I(A)))(I)", "S(S(S)(K))(A)"),
]


def _optimise_node(expr: SKInode_T, optimisation: bool = True) -> SKInode_T:

    if isinstance(expr, str):
        return expr

    if not optimisation:
        return expr

    for r in _OPTIMIZATION_RULES:
        succ, mapping = r.check(expr)
        if not succ:
            continue
        return r.transform(mapping)

    return expr


@lru_cache(maxsize=None)
def _optimise(expr: SKInode_T, optimisation: bool = True) -> SKInode_T:

    expr = _optimise_node(expr, optimisation)

    if isinstance(expr, str):
        return expr

    t = expr.node_type
    c1, c2 = expr.childs
    if t == NodeType.CALL:
        c1, c2 = (
            _optimise(c1, optimisation),
            _optimise(c2, optimisation),
        )
    else:
        raise SKIioInternalException("Declarations aren't supported in `optimise`")

    new_expr = SKInode(t, (c1, c2))

    return new_expr


@lru_cache(maxsize=None)
def _compile_node_to_ski(expr: SKInode_T, optimisation: bool = True) -> SKInode_T:

    # T[x] => x
    if isinstance(expr, str):
        return expr

    # Shortforms
    def O(e:SKInode_T):
        return _optimise(e, optimisation)

    def T(e:SKInode_T):
        return O(_compile_node_to_ski(e, optimisation))

    C, D, N = NodeType.CALL, NodeType.DECL, SKInode

    t = expr.node_type
    c1, c2 = expr.childs

    # T[AB] => T[A] T[B]
    if t == C:
        return O(N(C, (T(c1), T(c2))))

    # T[[x:A]] => K T[A]  (x isn't free in A)
    if not is_free(c2, cast(str, c1)):
        return O(N(C, ("K", T(c2))))

    # T[x:x] => I
    if isinstance(c2, str) and c2 == c1:
        return "I"

    c2 = cast(SKInode, c2)

    # T[x:[y:A]] => T[[x:T[y:A]]] (x is free in A)
    if c2.node_type == D:
        _, d2 = c2.childs
        if is_free(d2, cast(str, c1)):
            return T(N(D, (c1, T(c2))))

    # T[x:AB] => S T[[x:A]] T[[x:B]] (x is free in AB)
    d1, d2 = c2.childs
    ta = T(N(D, (c1, d1)))
    tb = T(N(D, (c1, d2)))
    return O(N(C, (N(C, ("S", ta)), tb)))


def compile_node_to_ski(expr: SKInode_T, optimisation: bool = True) -> SKInode_T:
    expr = _compile_node_to_ski(expr, optimisation)
    return expr


def compile_node_to_ski_str(expr_str: str, optimisation: bool = True) -> str:
    expr = SKInode.from_str(expr_str)
    return str(compile_node_to_ski(expr, optimisation))
