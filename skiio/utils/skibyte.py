from .._skinode import SKInode, SKInode_T

from typing import Dict

SKI_byte: Dict[int, SKInode_T] = {
    0: SKInode.from_str("K(I)"),
    1: SKInode.from_str("I"),
    2: SKInode.from_str("S(S(K(S))(K))(I)"),
    3: SKInode.from_str("S(S(K(S))(K))(S(S(K(S))(K))(I))"),
    4: SKInode.from_str("S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I)))"),
    5: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))"
    ),
    6: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))"
    ),
    7: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(S(K(S))(K))(I)))"
    ),
    8: SKInode.from_str(
        "S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(I))(S(S(K(S))(K))(I))"
    ),
    9: SKInode.from_str(
        "S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)"
    ),
    10: SKInode.from_str(
        "S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I))"
    ),
    11: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))"
    ),
    12: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I))))"
    ),
    13: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))))"
    ),
    14: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I))))))"
    ),
    15: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))))))"
    ),
    16: SKInode.from_str(
        "S(S(K(S(S(S(K(S))(K)))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(I))"
    ),
    17: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S(S(S(K(S))(K)))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(I)))"
    ),
    18: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S(S(S(K(S))(K)))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(I))))"
    ),
    19: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S(S(S(K(S))(K)))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(I)))))"
    ),
    20: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S(S(S(K(S))(K)))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(I))))))"
    ),
    21: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))"
    ),
    22: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I))))"
    ),
    23: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I))))"
    ),
    24: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(I))(S(S(K(S))(K))(I)))(S(S(K(S(S(S(K(S))(K)))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(I)))"
    ),
    25: SKInode.from_str(
        "S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))(I)"
    ),
    26: SKInode.from_str(
        "S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))(I))"
    ),
    27: SKInode.from_str(
        "S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(I))"
    ),
    28: SKInode.from_str(
        "S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(I)))"
    ),
    29: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(I))))"
    ),
    30: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(I)))))"
    ),
    31: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(I))))))"
    ),
    32: SKInode.from_str(
        "S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(I))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))"
    ),
    33: SKInode.from_str(
        "S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(I))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))"
    ),
    34: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(I))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))"
    ),
    35: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(S(K(S(S(S(K(S))(K)))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(I))))"
    ),
    36: SKInode.from_str(
        "S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))(I)"
    ),
    37: SKInode.from_str(
        "S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))(I))"
    ),
    38: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))(I)))"
    ),
    39: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))(I))))"
    ),
    40: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))(I)))))"
    ),
    41: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))(I))))))"
    ),
    42: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))(I)))))))"
    ),
    43: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(S(K(S(S(S(K(S))(K)))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(I)))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(I)))"
    ),
    44: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(S(K(S(S(S(K(S))(K)))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(I))))"
    ),
    45: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))(I))"
    ),
    46: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))(I)))"
    ),
    47: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))(I)))"
    ),
    48: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(S(K(S(S(S(K(S))(K)))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(I)))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(I))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))"
    ),
    49: SKInode.from_str(
        "S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(S(K(S))(K))(I))))(I)"
    ),
    50: SKInode.from_str(
        "S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(S(K(S))(K))(I))))(I))"
    ),
    51: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))(I))"
    ),
    52: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))(I)))"
    ),
    53: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))(I))))"
    ),
    54: SKInode.from_str(
        "S(S(K(S(S)(K(K(K(I))))))(S(K(S(I)))(S(K(K))(S(K(S(S)(K(K))))(S(K(K))(S(K(S(S(S(I)(K(S(S(K(S))(K))))))))(K)))))))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I))))(S(S(K(S))(K))(I))"
    ),
    55: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(I)))"
    ),
    56: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(I))))"
    ),
    57: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(I))))"
    ),
    58: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(I)))))"
    ),
    59: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(I)))))"
    ),
    60: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(I))))))"
    ),
    61: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(I))))))"
    ),
    62: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(I)))))))"
    ),
    63: SKInode.from_str(
        "S(K(S(K(S(K(S(S)(K(K))))(S(K(K))(S(S)(K(K(I)))))))))(S(K(S(S)(K(S(K(S(K(S(K(S(I)))(K)))))(S(K(S(I)))(K))))))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))(S(S(K(S))(K))(I)))"
    ),
    64: SKInode.from_str(
        "S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))(S(S(K(S))(K))(I))"
    ),
    65: SKInode.from_str(
        "S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))(S(S(K(S))(K))(I)))"
    ),
    66: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))(S(S(K(S))(K))(I))))"
    ),
    67: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))(S(S(K(S))(K))(I)))))"
    ),
    68: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))(S(S(K(S))(K))(I))))))"
    ),
    69: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))(S(S(K(S))(K))(I)))))))"
    ),
    70: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))(S(S(K(S))(K))(I))))))))"
    ),
    71: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))(S(S(K(S))(K))(I)))))))))"
    ),
    72: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(I))(S(S(K(S))(K))(I)))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))(S(S(K(S))(K))(I)))"
    ),
    73: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))(I))"
    ),
    74: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))(I)))"
    ),
    75: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))(I)))"
    ),
    76: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K))))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))(I))"
    ),
    77: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))(I))))"
    ),
    78: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))(I)))))"
    ),
    79: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))(I)))))"
    ),
    80: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(S(K(S(S(S(K(S))(K)))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(I)))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))(S(S(K(S))(K))(I)))"
    ),
    81: SKInode.from_str(
        "S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(S(S(K(S))(K))(I)))"
    ),
    82: SKInode.from_str(
        "S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(S(S(K(S))(K))(I))))"
    ),
    83: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))"
    ),
    84: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I))))(S(S(K(S))(K))(S(S(K(S))(K))(I)))"
    ),
    85: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I))))(S(S(K(S))(K))(S(S(K(S))(K))(I))))"
    ),
    86: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I))))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))"
    ),
    87: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))))(S(S(K(S))(K))(S(S(K(S))(K))(I)))"
    ),
    88: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))))(S(S(K(S))(K))(S(S(K(S))(K))(I))))"
    ),
    89: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(I))(S(S(K(S))(K))(I)))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(S(S(K(S))(K))(I))))"
    ),
    90: SKInode.from_str(
        "S(S(K(S(S)(K(K(K(I))))))(S(K(S(I)))(S(K(K))(S(K(S(S)(K(K))))(S(K(K))(S(K(S(S(S(I)(K(S(S(K(S))(K))))))))(K)))))))(S(S(K(S))(K)))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I))"
    ),
    91: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))"
    ),
    92: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))"
    ),
    93: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I))))(S(S(K(S))(K))(S(S(K(S))(K))(I))))"
    ),
    94: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I))))(S(S(K(S))(K))(S(S(K(S))(K))(I))))"
    ),
    95: SKInode.from_str(
        "S(S(K(S))(K))(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I))))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))"
    ),
    96: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(I))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))(S(S(K(S))(K))(I)))"
    ),
    97: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(S(K(S(S(S(K(S))(K)))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(I)))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(S(S(K(S))(K))(I))))"
    ),
    98: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(S(K(S(S(S(K(S))(K)))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))"
    ),
    99: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(S(K(S))(K))(I))))(I))"
    ),
    100: SKInode.from_str(
        "S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))(I)"
    ),
    101: SKInode.from_str(
        "S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))(I))"
    ),
    102: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))(I)))"
    ),
    103: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))(I))))"
    ),
    104: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))(I)))))"
    ),
    105: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))(I))))))"
    ),
    106: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))(I)))))))"
    ),
    107: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))(I))))))))"
    ),
    108: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(I)))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(S(S(K(S))(K))(I))))"
    ),
    109: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K))))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))(I))"
    ),
    110: SKInode.from_str(
        "S(S(K(S(S)(K(K(K(I))))))(S(K(S(I)))(S(K(K))(S(K(S(S)(K(K))))(S(K(K))(S(K(S(S(S(I)(K(S(S(K(S))(K))))))))(K)))))))(S(S(K(S))(K)))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))"
    ),
    111: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(I))))"
    ),
    112: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(I)))))"
    ),
    113: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(I))))))"
    ),
    114: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(I)))))))"
    ),
    115: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(I)))))"
    ),
    116: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(S(K(S(S(S(K(S))(K)))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(I)))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))(I))"
    ),
    117: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(S(K(S))(K))(S(S(K(S(S(S(K(S))(K)))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(I))))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))(I))"
    ),
    118: SKInode.from_str(
        "S(S(K(S))(K))(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(S(K(S))(K))(S(S(K(S(S(S(K(S))(K)))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(I))))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))(I)))"
    ),
    119: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(I))))))"
    ),
    120: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(I)))))))"
    ),
    121: SKInode.from_str(
        "S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I))))(I)"
    ),
    122: SKInode.from_str(
        "S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I))))(I))"
    ),
    123: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I))))(I)))"
    ),
    124: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I))))(I))))"
    ),
    125: SKInode.from_str(
        "S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))(S(S(K(S))(K))(I))"
    ),
    126: SKInode.from_str(
        "S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))(S(S(K(S))(K))(I)))"
    ),
    127: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))(S(S(K(S))(K))(I))))"
    ),
    128: SKInode.from_str(
        "S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(I))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))"
    ),
    129: SKInode.from_str(
        "S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(I))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))))"
    ),
    130: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(I))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))))"
    ),
    131: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))(S(S(K(S))(K))(I))))"
    ),
    132: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))(S(S(K(S))(K))(I)))))"
    ),
    133: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))(S(S(K(S))(K))(I)))))"
    ),
    134: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(I)))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))"
    ),
    135: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(I)))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))))"
    ),
    136: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(I)))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))))"
    ),
    137: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(I)))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))))))"
    ),
    138: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(I)))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))))))"
    ),
    139: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))(S(S(K(S))(K))(I))))))))"
    ),
    140: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(I))))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))"
    ),
    141: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(S(K(S(S(S(K(S))(K)))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(I)))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))(S(S(K(S))(K))(I)))"
    ),
    142: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(S(K(S(S(S(K(S))(K)))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))(S(S(K(S))(K))(I))))"
    ),
    143: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(S(K(S))(K))(S(S(K(S(S(S(K(S))(K)))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(I))))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))(S(S(K(S))(K))(I))))"
    ),
    144: SKInode.from_str(
        "S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))))(I)"
    ),
    145: SKInode.from_str(
        "S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))))(I))"
    ),
    146: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))))(I)))"
    ),
    147: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))))(I))))"
    ),
    148: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))))(I)))))"
    ),
    149: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))))(I))))))"
    ),
    150: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))))(I)))))))"
    ),
    151: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))))(I))))))))"
    ),
    152: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(I)))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))(S(S(K(S))(K))(I)))"
    ),
    153: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))(S(S(K(S))(K))(I))))"
    ),
    154: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(I))))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))(S(S(K(S))(K))(I))))"
    ),
    155: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(I)))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(I))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))))"
    ),
    156: SKInode.from_str(
        "S(S(K(S(S)(K(K(K(I))))))(S(K(S(I)))(S(K(K))(S(K(S(S)(K(K))))(S(K(K))(S(K(S(S(S(I)(K(S(S(K(S))(K))))))))(K)))))))(S(S(K(S))(K)))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))))"
    ),
    157: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(I))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))(S(S(K(S))(K))(I)))"
    ),
    158: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(I))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))(S(S(K(S))(K))(I))))"
    ),
    159: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(I))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))(S(S(K(S))(K))(I))))"
    ),
    160: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(S(K(S(S(S(K(S))(K)))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(I)))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))))(I))"
    ),
    161: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))(I))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))(S(S(K(S))(K))(I)))"
    ),
    162: SKInode.from_str(
        "S(K(S(S)(K(K(K(I))))))(S(K(S(I)))(S(K(K))(S(K(S(S)(K(K))))(S(K(K))(S(K(S(S(S(I)(K(S(S(K(S))(K))))))))(K))))))(S(S(K(S))(K))(I))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(S(S(K(S))(K))(I))))"
    ),
    163: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(S(S(K(S))(K))(I))))"
    ),
    164: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))"
    ),
    165: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))"
    ),
    166: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))"
    ),
    167: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))))"
    ),
    168: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))))"
    ),
    169: SKInode.from_str(
        "S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I))))))(I)"
    ),
    170: SKInode.from_str(
        "S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I))))))(I))"
    ),
    171: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I))))))(I)))"
    ),
    172: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I))))))(I))))"
    ),
    173: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I))))))(I)))))"
    ),
    174: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I))))))(I))))))"
    ),
    175: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))))(S(S(K(S))(K))(S(S(K(S))(K))(I))))"
    ),
    176: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))"
    ),
    177: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(I))(S(S(K(S))(K))(I)))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I))))))(I))"
    ),
    178: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(S(K(S(S(S(K(S))(K)))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(I))))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(S(S(K(S))(K))(I))))"
    ),
    179: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(S(K(S(S(S(K(S))(K)))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(I))))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))"
    ),
    180: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(S(K(S(S(S(K(S))(K)))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(I))))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))"
    ),
    181: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(S(S(K(S))(K))(I))))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))(I))"
    ),
    182: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))(I))"
    ),
    183: SKInode.from_str(
        "S(S(K(S))(K))(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))(I)))"
    ),
    184: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I))))(S(S(K(S))(K))(S(S(K(S))(K))(I))))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))(I))"
    ),
    185: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))(S(S(K(S))(K))(I)))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I))))(I))"
    ),
    186: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))(S(S(K(S))(K))(I))))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I))))(I))"
    ),
    187: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))(I)))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(S(S(K(S))(K))(I))))"
    ),
    188: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))(I)))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))"
    ),
    189: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))(S(S(K(S))(K))(I)))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))(S(S(K(S))(K))(I)))"
    ),
    190: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))(S(S(K(S))(K))(I))))"
    ),
    191: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(I))))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))"
    ),
    192: SKInode.from_str(
        "S(K(S(S)(K(K(K(I))))))(S(K(S(I)))(S(K(K))(S(K(S(S)(K(K))))(S(K(K))(S(K(S(S(S(I)(K(S(S(K(S))(K))))))))(K))))))(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))(S(S(K(S))(K))(I)))"
    ),
    193: SKInode.from_str(
        "S(S(K(S))(K))(S(K(S(S)(K(K(K(I))))))(S(K(S(I)))(S(K(K))(S(K(S(S)(K(K))))(S(K(K))(S(K(S(S(S(I)(K(S(S(K(S))(K))))))))(K))))))(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))(S(S(K(S))(K))(I))))"
    ),
    194: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(I))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(S(S(K(S))(K))(I))))"
    ),
    195: SKInode.from_str(
        "S(K(S(S)(K(K(K(I))))))(S(K(S(I)))(S(K(K))(S(K(S(S)(K(K))))(S(K(K))(S(K(S(S(S(I)(K(S(S(K(S))(K))))))))(K))))))(S(S(K(S))(K))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))(S(S(K(S))(K))(I))))"
    ),
    196: SKInode.from_str(
        "S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))))))(I)"
    ),
    197: SKInode.from_str(
        "S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))))))(I))"
    ),
    198: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))))))(I)))"
    ),
    199: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))))))(I))))"
    ),
    200: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))))))(I)))))"
    ),
    201: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))(I))"
    ),
    202: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))(I)))"
    ),
    203: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))(I)))"
    ),
    204: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))(I))))"
    ),
    205: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))(I))))"
    ),
    206: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))(I)))))"
    ),
    207: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))(I)))))"
    ),
    208: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))(I))))))"
    ),
    209: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))(I))))))"
    ),
    210: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))(I)))))))"
    ),
    211: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))(I)))))))"
    ),
    212: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))(I))))))))"
    ),
    213: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))(I))))))))"
    ),
    214: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I)))(I)))))))))"
    ),
    215: SKInode.from_str(
        "S(K(S(K(S(K(S(S)(K(K))))(S(K(K))(S(S)(K(K(I)))))))))(S(K(S(S)(K(S(K(S(K(S(K(S(I)))(K)))))(S(K(S(I)))(K))))))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))(S(S(K(S))(K))(I)))"
    ),
    216: SKInode.from_str(
        "S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))(S(S(K(S))(K))(I))"
    ),
    217: SKInode.from_str(
        "S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))(S(S(K(S))(K))(I)))"
    ),
    218: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))(S(S(K(S))(K))(I))))"
    ),
    219: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))(S(S(K(S))(K))(I)))))"
    ),
    220: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))(S(S(K(S))(K))(I))))))"
    ),
    221: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))(S(S(K(S))(K))(I)))))))"
    ),
    222: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))(S(S(K(S))(K))(I))))))))"
    ),
    223: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))(S(S(K(S))(K))(I)))))))))"
    ),
    224: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(I))(S(S(K(S))(K))(I)))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))(S(S(K(S))(K))(I)))"
    ),
    225: SKInode.from_str(
        "S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I))))))))(I)"
    ),
    226: SKInode.from_str(
        "S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I))))))))(I))"
    ),
    227: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I))))))))(I)))"
    ),
    228: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I))))))))(I))))"
    ),
    229: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I))))))))(I)))))"
    ),
    230: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I))))))))(I))))))"
    ),
    231: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I))))))))(I)))))))"
    ),
    232: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(S(K(S(S(S(K(S))(K)))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(I)))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))(S(S(K(S))(K))(I)))"
    ),
    233: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(S(K(S(S(S(K(S))(K)))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(I)))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))(S(S(K(S))(K))(I))))"
    ),
    234: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(S(K(S))(K))(S(S(K(S(S(S(K(S))(K)))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(I))))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))(S(S(K(S))(K))(I))))"
    ),
    235: SKInode.from_str(
        "S(S(K(S))(K))(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(S(K(S))(K))(S(S(K(S(S(S(K(S))(K)))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(I))))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))(S(S(K(S))(K))(I)))))"
    ),
    236: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S(S(S(K(S))(K)))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(I)))))(S(S(K(S))(K))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))(S(S(K(S))(K))(I)))))"
    ),
    237: SKInode.from_str(
        "S(K(S(S(I)(K(S(K(S(K(S(K(S(S)(K(K))))(S(K(K))(S(S)(K(K(I)))))))))(S(K(S(S)(K(S(K(S(K(S(K(S(I)))(K)))))(S(K(S(I)))(K))))))(K)))))))(K)(S(S(K(S(S(S(K(S))(K)))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(S(K(S))(K))(I))))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))))"
    ),
    238: SKInode.from_str(
        "S(K(S(S(I)(K(S(K(S(K(S(K(S(S)(K(K))))(S(K(K))(S(S)(K(K(I)))))))))(S(K(S(S)(K(S(K(S(K(S(K(S(I)))(K)))))(S(K(S(I)))(K))))))(K)))))))(K)(S(S(K(S(S(S(K(S))(K)))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(S(K(S))(K))(I))))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))"
    ),
    239: SKInode.from_str(
        "S(K(S(S(I)(K(S(K(S(K(S(K(S(S)(K(K))))(S(K(K))(S(S)(K(K(I)))))))))(S(K(S(S)(K(S(K(S(K(S(K(S(I)))(K)))))(S(K(S(I)))(K))))))(K)))))))(K)(S(S(K(S(S(S(K(S))(K)))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(S(K(S))(K))(I))))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I))))"
    ),
    240: SKInode.from_str(
        "S(K(S(S(I)(K(S(K(S(K(S(K(S(S)(K(K))))(S(K(K))(S(S)(K(K(I)))))))))(S(K(S(S)(K(S(K(S(K(S(K(S(I)))(K)))))(S(K(S(I)))(K))))))(K)))))))(K)(S(S(K(S(S(S(K(S))(K)))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(S(K(S))(K))(I))))(S(S(K(S))(K))(S(S(K(S))(K))(I)))"
    ),
    241: SKInode.from_str(
        "S(K(S(S(I)(K(S(K(S(K(S(K(S(S)(K(K))))(S(K(K))(S(S)(K(K(I)))))))))(S(K(S(S)(K(S(K(S(K(S(K(S(I)))(K)))))(S(K(S(I)))(K))))))(K)))))))(K)(S(S(K(S(S(S(K(S))(K)))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(S(K(S))(K))(I))))(S(S(K(S))(K))(I))"
    ),
    242: SKInode.from_str(
        "S(K(S(K(S(K(S(S)(K(K))))(S(K(K))(S(S)(K(K(I)))))))))(S(K(S(S)(K(S(K(S(K(S(K(S(I)))(K)))))(S(K(S(I)))(K))))))(K))(S(S(K(S(S(S(K(S))(K)))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(S(K(S))(K))(I))))"
    ),
    243: SKInode.from_str(
        "S(S(K(S(S(S(K(S))(K)))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(S(K(S))(K))(I)))"
    ),
    244: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S(S(S(K(S))(K)))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(S(K(S))(K))(I))))"
    ),
    245: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S(S(S(K(S))(K)))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))"
    ),
    246: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S(S(S(K(S))(K)))))(K))(S(S(K(S))(K))))(S(S(K(S))(K))(S(S(K(S))(K))(I)))"
    ),
    247: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S(S(S(K(S))(K)))))(K))(S(S(K(S))(K))))(S(S(K(S))(K))(S(S(K(S))(K))(I))))"
    ),
    248: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S(S(S(K(S))(K)))))(K))(S(S(K(S))(K))))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))"
    ),
    249: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S(S(S(K(S))(K)))))(K))(S(S(K(S))(K)))))(S(S(K(S))(K))(S(S(K(S))(K))(I)))"
    ),
    250: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S(S(S(K(S))(K)))))(K))(S(S(K(S))(K)))))(S(S(K(S))(K))(S(S(K(S))(K))(I))))"
    ),
    251: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))(S(S(K(S))(K))(I)))"
    ),
    252: SKInode.from_str(
        "S(K(S(S(I)(K(S(S(K(S))(K)))))))(K)(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(I)))(I))(S(S(K(S(S(S(K(S))(K)))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(S(K(S))(K))(I))))"
    ),
    253: SKInode.from_str(
        "S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))(S(S(K(S))(K))(I))))"
    ),
    254: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))(S(S(K(S))(K))(I)))))"
    ),
    255: SKInode.from_str(
        "S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S(S(I)(K(S(S(K(S))(K)))))))(K))(S(S(K(S))(K)))(S(S(K(S))(K))(S(K(S(S(S(K(S))(K)))))(K)(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(S(S(K(S))(K))(I)))))(S(S(K(S))(K))(I))))))"
    ),
}
