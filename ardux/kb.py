import os

import board
from kmk.quickpin.pro_micro.kb2040 import pinout as pins

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner

from kmk.keys import KC
from ardux.chord import ArduxChord

from kmk.modules.holdtap import HoldTap
from kmk.modules.layers import Layers
from kmk.modules.combos import Combos, Chord
from kmk.modules.oneshot import OneShot
from kmk.modules.mouse_keys import MouseKeys
from kmk.extensions.media_keys import MediaKeys

# constants
LAYER_ID_BASE = 0
LAYER_ID_PARENS = 1
LAYER_ID_NUMBERS = 2
LAYER_ID_NAVIGATION = 3
LAYER_ID_SYMBOLS = 4
LAYER_ID_CUSTOM = 5
LAYER_ID_MOUSE = 6

class ArduxKeyboard(KMKKeyboard):
    coord_mapping = [
        0,  1,  2,  3,
        4,  5,  6,  7,
    ]

    keymap = []

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

        # HoldTap
        self.holdtap_module = HoldTap()
        self.holdtap_module.tap_time = 175
        self.modules.append(self.holdtap_module)
        
        # Layers
        self.modules.append(Layers())

        # Media Keys
        self.extensions.append(MediaKeys())

        # Mouse Keys
        self.modules.append(MouseKeys())

        # Combos
        self.combo_module = Combos()
        self.modules.append(self.combo_module)

        # One Shot
        self.modules.append(OneShot())
        
        # Setup kemap as last step
        self.setup_keymap()

        # Setup combos
        self.setup_combos()

    # Define keymap
    def setup_keymap(self):
        self.base_s_numbers = KC.LT(LAYER_ID_NUMBERS, KC.S, prefer_hold=False)
        self.base_a_parens = KC.LT(LAYER_ID_PARENS, KC.A, prefer_hold=False)
        self.base_o_custom = KC.LT(LAYER_ID_CUSTOM, KC.O, prefer_hold=False)
        self.base_e_symbols = KC.LT(LAYER_ID_SYMBOLS, KC.E, prefer_hold=False)
        self.keymap = [
            # std - left - base
            [self.base_s_numbers, KC.T, KC.R, self.base_a_parens,
             self.base_o_custom, KC.I, KC.Y, self.base_e_symbols],
            # std - left - parenthesis
            [KC.RIGHT_CURLY_BRACE, KC.LEFT_PAREN, KC.RIGHT_PAREN, KC.TRANSPARENT,
             KC.LEFT_CURLY_BRACE, KC.LBRACKET, KC.RBRACKET, KC.NO],
            # std - left - number
            [KC.TRANSPARENT, KC.N3, KC.N2, KC.N1,
             KC.NO, KC.N6, KC.N5, KC.N4],
            # std - left - navigation
            [KC.PGUP, KC.HOME, KC.UP, KC.END,
             KC.PGDOWN, KC.LEFT, KC.DOWN, KC.RIGHT],
            # std - left - symbols
            [KC.GRAVE, KC.SCOLON, KC.BSLASH, KC.EXCLAIM,
             KC.EQUAL, KC.MINUS, KC.QUESTION, KC.TRANSPARENT],
            # std - left - custom
            [KC.NO, KC.AUDIO_VOL_UP, KC.INSERT, KC.AUDIO_MUTE,
             KC.TRANSPARENT, KC.AUDIO_VOL_DOWN, KC.PSCREEN, KC.RSHIFT],
            # std - left - mouse
            [KC.MW_UP, KC.MB_RMB, KC.MS_UP, KC.MB_LMB,
             KC.MW_DOWN, KC.MS_LEFT, KC.MS_DN, KC.MS_RIGHT]
        ]

    # Define combos for ardux
    def setup_combos(self):
        self.combo_module.combos = []

        #####
        # std - base
        # layers
        self.combo_module.combos.append(ArduxChord((KC.R, KC.I, self.base_e_symbols), KC.TO(LAYER_ID_NAVIGATION), ardux_keyboard=[self], layers=[LAYER_ID_BASE]))
        self.combo_module.combos.append(ArduxChord((KC.T, KC.Y, self.base_a_parens), KC.TO(LAYER_ID_MOUSE), ardux_keyboard=[self], layers=[LAYER_ID_BASE]))
        # mods
        self.combo_module.combos.append(ArduxChord((self.base_s_numbers, self.base_e_symbols), KC.OS(KC.LCTRL), ardux_keyboard=[self], layers=[LAYER_ID_BASE]))
        self.combo_module.combos.append(ArduxChord((KC.Y, self.base_s_numbers), KC.OS(KC.LGUI), ardux_keyboard=[self], layers=[LAYER_ID_BASE]))
        self.combo_module.combos.append(ArduxChord((KC.I, self.base_s_numbers), KC.OS(KC.LALT), ardux_keyboard=[self], layers=[LAYER_ID_BASE]))
        self.combo_module.combos.append(ArduxChord((self.base_s_numbers, KC.R, KC.T, self.base_e_symbols), KC.OS(KC.LSHIFT), ardux_keyboard=[self], layers=[LAYER_ID_BASE]))
        # control sequences
        self.combo_module.combos.append(ArduxChord((self.base_o_custom, KC.I, KC.Y, self.base_e_symbols), KC.SPACE, ardux_keyboard=[self], layers=[LAYER_ID_BASE]))
        self.combo_module.combos.append(ArduxChord((self.base_a_parens,  KC.R, self.base_o_custom), KC.ESCAPE, ardux_keyboard=[self], layers=[LAYER_ID_BASE]))
        self.combo_module.combos.append(ArduxChord((self.base_e_symbols,  KC.R), KC.BSPACE, ardux_keyboard=[self], layers=[LAYER_ID_BASE]))
        self.combo_module.combos.append(ArduxChord((KC.R,  KC.I), KC.DELETE, ardux_keyboard=[self], layers=[LAYER_ID_BASE]))
        self.combo_module.combos.append(ArduxChord((self.base_a_parens,  KC.R,  KC.T,  self.base_o_custom), KC.TAB, ardux_keyboard=[self], layers=[LAYER_ID_BASE]))
        self.combo_module.combos.append(ArduxChord((self.base_a_parens, self.base_e_symbols), KC.ENTER, ardux_keyboard=[self], layers=[LAYER_ID_BASE]))
        self.combo_module.combos.append(ArduxChord((self.base_a_parens, KC.Y, KC.I, self.base_o_custom), KC.CAPSLOCK, ardux_keyboard=[self], layers=[LAYER_ID_BASE]))
        # symbols
        self.combo_module.combos.append(ArduxChord((self.base_a_parens, KC.Y), KC.DOT, ardux_keyboard=[self], layers=[LAYER_ID_BASE]))
        self.combo_module.combos.append(ArduxChord((self.base_a_parens, KC.I), KC.COMMA, ardux_keyboard=[self], layers=[LAYER_ID_BASE]))
        self.combo_module.combos.append(ArduxChord((self.base_a_parens, self.base_o_custom), KC.SLASH, ardux_keyboard=[self], layers=[LAYER_ID_BASE]))
        self.combo_module.combos.append(ArduxChord((self.base_a_parens, KC.Y, KC.I), KC.QUOTE, ardux_keyboard=[self], layers=[LAYER_ID_BASE]))
        # ansi
        self.combo_module.combos.append(ArduxChord((self.base_s_numbers, self.base_o_custom), KC.B, ardux_keyboard=[self], layers=[LAYER_ID_BASE]))
        self.combo_module.combos.append(ArduxChord((self.base_s_numbers,  KC.Y), KC.C, ardux_keyboard=[self], layers=[LAYER_ID_BASE]))
        self.combo_module.combos.append(ArduxChord((KC.I,  self.base_o_custom), KC.N, ardux_keyboard=[self], layers=[LAYER_ID_BASE]))
        self.combo_module.combos.append(ArduxChord((self.base_a_parens,  KC.R), KC.F, ardux_keyboard=[self], layers=[LAYER_ID_BASE]))
        self.combo_module.combos.append(ArduxChord((KC.R, KC.T), KC.G, ardux_keyboard=[self], layers=[LAYER_ID_BASE]))
        self.combo_module.combos.append(ArduxChord((KC.Y, KC.I), KC.U, ardux_keyboard=[self], layers=[LAYER_ID_BASE]))
        self.combo_module.combos.append(ArduxChord((self.base_s_numbers, KC.I), KC.H, ardux_keyboard=[self], layers=[LAYER_ID_BASE]))
        self.combo_module.combos.append(ArduxChord((KC.R, self.base_s_numbers), KC.V, ardux_keyboard=[self], layers=[LAYER_ID_BASE]))
        self.combo_module.combos.append(ArduxChord((KC.T, self.base_s_numbers), KC.J, ardux_keyboard=[self], layers=[LAYER_ID_BASE]))
        self.combo_module.combos.append(ArduxChord((self.base_a_parens, self.base_s_numbers), KC.W, ardux_keyboard=[self], layers=[LAYER_ID_BASE]))
        self.combo_module.combos.append(ArduxChord((KC.Y, self.base_o_custom), KC.K, ardux_keyboard=[self], layers=[LAYER_ID_BASE]))
        self.combo_module.combos.append(ArduxChord((KC.Y, KC.I, self.base_o_custom), KC.M, ardux_keyboard=[self], layers=[LAYER_ID_BASE]))
        self.combo_module.combos.append(ArduxChord((self.base_a_parens, KC.R, KC.T), KC.D, ardux_keyboard=[self], layers=[LAYER_ID_BASE]))
        self.combo_module.combos.append(ArduxChord((self.base_s_numbers, KC.I, self.base_o_custom), KC.P, ardux_keyboard=[self], layers=[LAYER_ID_BASE]))
        self.combo_module.combos.append(ArduxChord((self.base_a_parens, KC.T,  self.base_s_numbers), KC.Q, ardux_keyboard=[self], layers=[LAYER_ID_BASE]))
        self.combo_module.combos.append(ArduxChord((KC.R, KC.T, self.base_s_numbers), KC.X, ardux_keyboard=[self], layers=[LAYER_ID_BASE]))
        self.combo_module.combos.append(ArduxChord((self.base_s_numbers, KC.Y, KC.I), KC.L, ardux_keyboard=[self], layers=[LAYER_ID_BASE]))
        self.combo_module.combos.append(ArduxChord((self.base_a_parens, KC.R, KC.T, self.base_s_numbers), KC.Z, ardux_keyboard=[self], layers=[LAYER_ID_BASE]))
        
        #####
        # std - nav
        self.combo_module.combos.append(ArduxChord((KC.UP, KC.LEFT, KC.RIGHT), KC.TO(LAYER_ID_BASE), ardux_keyboard=[self], layers=[LAYER_ID_NAVIGATION]))
        self.combo_module.combos.append(ArduxChord((KC.END, KC.RIGHT), KC.ENTER, ardux_keyboard=[self], layers=[LAYER_ID_NAVIGATION]))
        self.combo_module.combos.append(ArduxChord((KC.END, KC.UP, KC.PGDOWN), KC.ESCAPE, ardux_keyboard=[self], layers=[LAYER_ID_NAVIGATION]))
        self.combo_module.combos.append(ArduxChord((KC.RIGHT, KC.UP), KC.BSPACE, ardux_keyboard=[self], layers=[LAYER_ID_NAVIGATION]))
        self.combo_module.combos.append(ArduxChord((KC.UP, KC.LEFT), KC.DELETE, ardux_keyboard=[self], layers=[LAYER_ID_NAVIGATION]))
        self.combo_module.combos.append(ArduxChord((KC.END, KC.UP, KC.HOME, KC.PGDOWN), KC.TAB, ardux_keyboard=[self], layers=[LAYER_ID_NAVIGATION]))
        self.combo_module.combos.append(ArduxChord((KC.RIGHT, KC.DOWN, KC.LEFT, KC.PGDOWN), KC.SPACE, ardux_keyboard=[self], layers=[LAYER_ID_NAVIGATION]))
        
        #####
        # std - number
        self.combo_module.combos.append(ArduxChord((KC.N1, KC.N2), KC.N7, ardux_keyboard=[self], layers=[LAYER_ID_NUMBERS]))
        self.combo_module.combos.append(ArduxChord((KC.N2, KC.N3), KC.N8, ardux_keyboard=[self], layers=[LAYER_ID_NUMBERS]))
        self.combo_module.combos.append(ArduxChord((KC.N4, KC.N5), KC.N9, ardux_keyboard=[self], layers=[LAYER_ID_NUMBERS]))
        self.combo_module.combos.append(ArduxChord((KC.N5, KC.N6), KC.N0, ardux_keyboard=[self], layers=[LAYER_ID_NUMBERS]))
        self.combo_module.combos.append(ArduxChord((KC.N1, KC.N5), KC.DOT, ardux_keyboard=[self], layers=[LAYER_ID_NUMBERS]))
        self.combo_module.combos.append(ArduxChord((KC.N1, KC.N6), KC.COMMA, ardux_keyboard=[self], layers=[LAYER_ID_NUMBERS]))
        self.combo_module.combos.append(ArduxChord((KC.N1, KC.N4), KC.ENTER, ardux_keyboard=[self], layers=[LAYER_ID_NUMBERS]))
        self.combo_module.combos.append(ArduxChord((KC.N2, KC.N6), KC.DELETE, ardux_keyboard=[self], layers=[LAYER_ID_NUMBERS]))
        self.combo_module.combos.append(ArduxChord((KC.N4, KC.N2), KC.BSPACE, ardux_keyboard=[self], layers=[LAYER_ID_NUMBERS]))
        
        #####
        # std - mouse
        self.combo_module.combos.append(ArduxChord((KC.MB_RMB, KC.MS_DN, KC.MB_LMB), KC.TO(LAYER_ID_BASE), ardux_keyboard=[self], layers=[LAYER_ID_MOUSE]))


