from ._skinode import *
from ._skinode import _ATOMS
from ._exceptions import *

from typing import Tuple


class Rule:
    def __init__(self, lhs: str, rhs: str):
        self.rule_str = (lhs, rhs)
        self.lhs, self.rhs = SKInode.from_str(lhs), SKInode.from_str(rhs)

    def __str__(self):
        return "%s => %s" % (self.lhs, self.rhs)

    def __repr__(self):
        return str(self)

    @staticmethod
    def _check(
        lhs: SKInode_T, expr: SKInode_T, mapping: dict, _lctx: dict, _ectx: dict
    ) -> Tuple[bool, dict]:

        # TODO: Make this only for NodeType.CALL

        if isinstance(lhs, str):
            if lhs in _lctx:
                if expr not in _ectx:
                    return False, {}
                return _lctx[lhs] == _ectx[expr], mapping
            if lhs in _ATOMS:
                return lhs == expr, mapping
            if lhs in mapping:
                return mapping[lhs] == expr, mapping
            mapping[lhs] = expr
            return True, mapping

        if isinstance(expr, str):
            return False, {}

        lhs_t = lhs.node_type
        exp_t = expr.node_type
        if lhs_t != exp_t:
            return False, {}

        l1, l2 = lhs.childs
        e1, e2 = expr.childs

        if lhs_t == NodeType.DECL:
            (_lctx := _lctx.copy())[l1] = max(_lctx.values()) + 1
            (_ectx := _ectx.copy())[e1] = max(_ectx.values()) + 1
            return Rule._check(l2, e2, mapping, _lctx, _ectx)

        elif lhs_t == NodeType.CALL:
            succ, mapping = Rule._check(l1, e1, mapping, _lctx, _ectx)
            if not succ:
                return False, {}
            succ, mapping = Rule._check(l2, e2, mapping, _lctx, _ectx)
            if not succ:
                return False, {}
            return True, mapping

        raise SKIioInternalException("Unexpected NodeType!")

    @staticmethod
    def _transform(rhs: SKInode_T, mapping: dict, _rctx: set = set()) -> SKInode_T:

        if isinstance(rhs, str):
            if rhs in _rctx or rhs in _ATOMS:
                return rhs
            if rhs not in mapping:
                raise SKIioInternalException(
                    "Mapping invalid! Doesn't have key %s" % rhs
                )
            return mapping[rhs]

        r1, r2 = rhs.childs
        if rhs.node_type == NodeType.DECL:
            (_rctx := _rctx.copy()).add(r1)
            childs = r1, Rule._transform(r2, mapping, _rctx)
        elif rhs.node_type == NodeType.CALL:
            childs = Rule._transform(r1, mapping, _rctx), Rule._transform(
                r2, mapping, _rctx
            )
        else:
            raise SKIioInternalException("Unexpected NodeType!")

        return SKInode(rhs.node_type, childs)

    def check(self, expr: SKInode_T) -> Tuple[bool, dict]:
        succ, mapping = self._check(self.lhs, expr, {}, {0: 0}, {0: 0})
        if not succ:
            mapping = {}
        frees = get_all_free(self.rhs)
        for name in list(mapping.keys()):
            if name not in frees:
                mapping.pop(name)
        return succ, mapping

    def transform(self, mapping: dict) -> SKInode_T:
        return self._transform(self.rhs, mapping)

    def apply(self, expr: SKInode_T) -> Tuple[bool, SKInode_T]:
        success, mapping = self.check(expr)
        if not success:
            return success, expr
        return True, self.transform(mapping)

    def verify(self) -> bool:
        # If returns False, not guaranteed to be false
        B = beta_eta_reduce
        return B(self.rhs) == B(self.lhs)
