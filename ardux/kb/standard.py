import os

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC

from kmk.modules.combos import Combos
from kmk.modules.holdtap import HoldTap
from kmk.modules.sticky_keys import StickyKeys
from kmk.modules.mouse_keys import MouseKeys
from kmk.extensions.media_keys import MediaKeys

from ardux.constants import *
from ardux.layers import ArduxLayers
from ardux.kb import ArduxChord

from ardux.oled import *
from ardux.rgb import *

class _ArduxKeyboardStandard(KMKKeyboard):
    # Switch to ABC python3 stl abstract class methods
    #     See https://stackoverflow.com/a/4382964 for detail (the accepted answer)
    def setup_physical_config(self):
        raise NotImplementedError('Please define the physical config for your keyboard')

    # Init / constructor / setup
    def __init__(self):
        # Run main KMKKeyboard class init before doing any of our own customizations
        super().__init__()
        
        # setup modules/extensions arrays
        self.modules = []
        self.extensions = []

        # Call setup hook -- matrix/direct wire config
        self.setup_physical_config()

        # Layers
        self.layers_module = ArduxLayers()
        self.layers_module.prefer_hold=False
        self.layers_module.tap_interrupted=True
        self.modules.append(self.layers_module)

        # Combos
        self.combo_module = Combos()
        self.combo_module.prefer_hold = True
        self.combo_module.tap_interrupted = False
        self.modules.append(self.combo_module)

        # HoldTap
        self.holdtap_module = HoldTap()
        self.holdtap_module.tap_time = 50
        self.holdtap_module.prefer_hold = True
        self.modules.append(self.holdtap_module)

        # One Shot
        self.modules.append(StickyKeys())

        # Media Keys
        self.extensions.append(MediaKeys())

        # Mouse Keys
        self.modules.append(MouseKeys())

        # Setup layer toggles
        self.setup_layer_toggles()

        # Setup kemap as last step
        self.setup_keymap()

        # Setup combos
        self.setup_combos()

        # RGB, if enabled
        if ardux_rgb_active:
            self.extensions.append(rgb_ext)

        # Display, if enabled
        if ardux_display:
            self.extensions.append(ardux_display)

    # Define hold/tap layer toggles
    def setup_layer_toggles(self):
        self.base_s_numbers = KC.LT(LAYER_ID_NUMBERS, KC.S)
        self.base_a_parens = KC.LT(LAYER_ID_PARENS, KC.A)
        self.base_o_custom = KC.LT(LAYER_ID_CUSTOM, KC.O)
        self.base_e_symbols = KC.LT(LAYER_ID_SYMBOLS, KC.E)

    # Define keymap
    def setup_keymap(self):
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
        self.combo_module.combos.append(ArduxChord((KC.R, KC.I, self.base_e_symbols), KC.TO(LAYER_ID_NAVIGATION)))
        self.combo_module.combos.append(ArduxChord((KC.T, KC.Y, self.base_a_parens), KC.TO(LAYER_ID_MOUSE)))
        # mods
        self.combo_module.combos.append(ArduxChord((self.base_s_numbers, self.base_e_symbols), KC.SK(KC.LCTRL)))
        self.combo_module.combos.append(ArduxChord((KC.Y, self.base_s_numbers), KC.SK(KC.LGUI)))
        self.combo_module.combos.append(ArduxChord((KC.I, self.base_s_numbers), KC.SK(KC.LALT)))
        self.combo_module.combos.append(ArduxChord((self.base_s_numbers, KC.R, KC.T, self.base_e_symbols), KC.SK(KC.LSHIFT)))
        # control sequences
        self.combo_module.combos.append(ArduxChord((self.base_o_custom, KC.I, KC.Y, self.base_e_symbols), KC.SPACE))
        self.combo_module.combos.append(ArduxChord((self.base_a_parens,  KC.R, self.base_o_custom), KC.ESCAPE,))
        self.combo_module.combos.append(ArduxChord((self.base_e_symbols,  KC.R), KC.BSPACE))
        self.combo_module.combos.append(ArduxChord((KC.R,  KC.I), KC.DELETE))
        self.combo_module.combos.append(ArduxChord((self.base_a_parens,  KC.R,  KC.T,  self.base_o_custom), KC.TAB))
        self.combo_module.combos.append(ArduxChord((self.base_a_parens, self.base_e_symbols), KC.ENTER))
        self.combo_module.combos.append(ArduxChord((self.base_a_parens, KC.Y, KC.I, self.base_o_custom), KC.CAPSLOCK))
        # symbols
        self.combo_module.combos.append(ArduxChord((self.base_a_parens, KC.Y), KC.DOT))
        self.combo_module.combos.append(ArduxChord((self.base_a_parens, KC.I), KC.COMMA))
        self.combo_module.combos.append(ArduxChord((self.base_a_parens, self.base_o_custom), KC.SLASH))
        self.combo_module.combos.append(ArduxChord((self.base_a_parens, KC.Y, KC.I), KC.QUOTE))
        # ansi
        self.combo_module.combos.append(ArduxChord((self.base_o_custom, self.base_e_symbols), KC.B))
        self.combo_module.combos.append(ArduxChord((self.base_e_symbols,  KC.Y), KC.C))
        self.combo_module.combos.append(ArduxChord((KC.I,  self.base_o_custom), KC.N))
        self.combo_module.combos.append(ArduxChord((self.base_a_parens,  KC.R), KC.F))
        self.combo_module.combos.append(ArduxChord((KC.R, KC.T), KC.G))
        self.combo_module.combos.append(ArduxChord((KC.Y, KC.I), KC.U))
        self.combo_module.combos.append(ArduxChord((self.base_e_symbols, KC.I), KC.H))
        self.combo_module.combos.append(ArduxChord((KC.R, self.base_s_numbers), KC.V))
        self.combo_module.combos.append(ArduxChord((KC.T, self.base_s_numbers),KC.J))
        self.combo_module.combos.append(ArduxChord((self.base_a_parens, self.base_s_numbers), KC.W))
        self.combo_module.combos.append(ArduxChord((KC.Y, self.base_o_custom), KC.K))
        self.combo_module.combos.append(ArduxChord((KC.Y, KC.I, self.base_o_custom), KC.M))
        self.combo_module.combos.append(ArduxChord((self.base_a_parens, KC.R, KC.T), KC.D))
        self.combo_module.combos.append(ArduxChord((self.base_o_custom, KC.I, self.base_e_symbols), KC.P))
        self.combo_module.combos.append(ArduxChord((self.base_a_parens, KC.T,  self.base_s_numbers), KC.Q))
        self.combo_module.combos.append(ArduxChord((KC.R, KC.T, self.base_s_numbers), KC.X))
        self.combo_module.combos.append(ArduxChord((KC.I, KC.Y, self.base_e_symbols), KC.L))
        self.combo_module.combos.append(ArduxChord((self.base_a_parens, KC.R, KC.T, self.base_s_numbers), KC.Z))
        
        #####
        # std - nav
        self.combo_module.combos.append(ArduxChord((KC.UP, KC.LEFT, KC.RIGHT), KC.TO(LAYER_ID_BASE)))
        self.combo_module.combos.append(ArduxChord((KC.END, KC.RIGHT), KC.ENTER))
        self.combo_module.combos.append(ArduxChord((KC.END, KC.UP, KC.PGDOWN), KC.ESCAPE))
        self.combo_module.combos.append(ArduxChord((KC.RIGHT, KC.UP), KC.BSPACE))
        self.combo_module.combos.append(ArduxChord((KC.UP, KC.LEFT), KC.DELETE))
        self.combo_module.combos.append(ArduxChord((KC.END, KC.UP, KC.HOME, KC.PGDOWN), KC.TAB))
        self.combo_module.combos.append(ArduxChord((KC.RIGHT, KC.DOWN, KC.LEFT, KC.PGDOWN), KC.SPACE))
        self.combo_module.combos.append(ArduxChord((KC.RIGHT, KC.PGUP), KC.SK(KC.LCTRL)))
        self.combo_module.combos.append(ArduxChord((KC.DOWN, KC.PGUP), KC.SK(KC.LGUI)))
        self.combo_module.combos.append(ArduxChord((KC.LEFT, KC.PGUP), KC.SK(KC.LALT)))
        self.combo_module.combos.append(ArduxChord((KC.RIGHT, KC.UP, KC.HOME, KC.PGUP), KC.SK(KC.LSHIFT)))
        
        #####
        # std - number
        self.combo_module.combos.append(ArduxChord((KC.N1, KC.N2), KC.N7))
        self.combo_module.combos.append(ArduxChord((KC.N2, KC.N3), KC.N8))
        self.combo_module.combos.append(ArduxChord((KC.N4, KC.N5), KC.N9))
        self.combo_module.combos.append(ArduxChord((KC.N5, KC.N6), KC.N0))
        self.combo_module.combos.append(ArduxChord((KC.N1, KC.N5), KC.DOT))
        self.combo_module.combos.append(ArduxChord((KC.N1, KC.N6), KC.COMMA))
        self.combo_module.combos.append(ArduxChord((KC.N1, KC.N4), KC.ENTER))
        self.combo_module.combos.append(ArduxChord((KC.N2, KC.N6), KC.DELETE))
        self.combo_module.combos.append(ArduxChord((KC.N4, KC.N2), KC.BSPACE))
        
        #####
        # std - mouse
        self.combo_module.combos.append(ArduxChord((KC.MB_RMB, KC.MS_DN, KC.MB_LMB), KC.TO(LAYER_ID_BASE)))

        # work around a bug with combo handling and layer selections in kmk
        #    these combos should be removed if/when kmk stops 'going hayware' or 'getting stuck' when these key combos are pressed when the below are not in the code
        self.combo_module.combos.append(ArduxChord((self.base_o_custom, KC.Y, self.base_e_symbols), KC.NO))
        self.combo_module.combos.append(ArduxChord((self.base_a_parens, KC.R,  self.base_s_numbers), KC.NO))
        self.combo_module.combos.append(ArduxChord((self.base_a_parens, KC.T), KC.NO))
        self.combo_module.combos.append(ArduxChord((self.base_o_custom, KC.T), KC.NO))
        self.combo_module.combos.append(ArduxChord((self.base_o_custom, self.base_s_numbers), KC.NO))
        self.combo_module.combos.append(ArduxChord((self.base_s_numbers, KC.Y), KC.NO))
