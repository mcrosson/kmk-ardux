import os

import board
from kmk.quickpin.pro_micro.kb2040 import pinout as pins

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner

from kmk.modules.layers import Layers
from kmk.modules.combos import Combos, Chord
from ardux.chord import ArduxChord

from kmk.keys import KC

class ArduxKeyboard(KMKKeyboard):
    coord_mapping = [
        0,  1,  2,  3,
        4,  5,  6,  7,
    ]

    keymap = [
        [KC.S, KC.T, KC.R, KC.A,
         KC.O, KC.I, KC.Y, KC.E]
        ]

    # Init / constructor / setup
    def __init__(self):
        # Enable debugging if appropriate
        if os.getenv('ARDUX_KMK_DEBUGGING'):
            self.debug_enabled = True

        # setup modules/extensions arrays
        self.modules = []
        self.extensions = []
        
        # Direct wire & matrix setup
        self.matrix = KeysScanner([pins[16], pins[17], pins[18], pins[19], pins[12], pins[13], pins[14], pins[15]])

        # Layers
        self.modules.append(Layers())

        # Combos
        self.combo_module = Combos()
        self.modules.append(self.combo_module)
        self.setup_combos()

    # Define combos for ardux
    def setup_combos(self):
        self.combo_module.combos = []
        
        combo_enter = ArduxChord((KC.A, KC.E), KC.ENTER, ardux_keyboard=[self], layers=[0])
        self.combo_module.combos.append(combo_enter)
        
        combo_space = ArduxChord((KC.O, KC.I, KC.Y, KC.E), KC.SPACE, ardux_keyboard=[self], layers=[1])
        self.combo_module.combos.append(combo_space)
