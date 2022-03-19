from dataclasses import dataclass
from enum import Enum, unique

from ._skinode import SKInode, NodeType, SKInode_T

@unique
class TokenType(Enum):
    ...


@dataclass
class Token:
    line: int
    col: int
    type: TokenType
    tok: str