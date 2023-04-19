import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.quickpin.pro_micro.kb2040 import pinout as pins
from kmk.scanners.keypad import KeysScanner

# Direct wire config
_KEY_CFG = [
    pins[16],
    pins[17],
    pins[18],
    pins[19],
    pins[12],
    pins[13],
    pins[14],
    pins[15]
]

class KMKKeyboard(_KMKKeyboard):
    def __init__(self):
        # create and register the scanner for direct wire
        self.matrix = KeysScanner(_KEY_CFG)

    coord_mapping = [
        0,  1,  2,  3,
        4,  5,  6,  7,
    ]
