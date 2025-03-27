import os

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC

from kmk.modules.combos import Combos, Chord
from kmk.modules.holdtap import HoldTap
from kmk.modules.sticky_keys import StickyKeys
from kmk.modules.mouse_keys import MouseKeys
from kmk.extensions.media_keys import MediaKeys

from ardux.constants import *
from ardux.layers import ArduxLayers

if os.getenv('ARDUX_DISPLAY_DRIVER'):
    from ardux.oled import *

from ardux.rgb import *

class _ArduxKeyboardStandard(KMKKeyboard):
    coord_mapping = [
        0,  1,  2,  3,
        4,  5,  6,  7,
    ]

    keymap = []

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
        self.combo_module.timeout=250
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

        # Setup kemap as last step
        self.setup_keymap()

        # Setup combos
        self.setup_combos()

        # RGB, if enabled
        if ardux_rgb_active:
            self.extensions.append(rgb_ext)

        # Display, if enabled
        if os.getenv('ARDUX_DISPLAY_DRIVER'):
            self.extensions.append(display)

    # Define keymap
    def setup_keymap(self):
        self.base_s_numbers = KC.LT(LAYER_ID_NUMBERS, KC.S)
        self.base_a_parens = KC.LT(LAYER_ID_PARENS, KC.A)
        self.base_o_custom = KC.LT(LAYER_ID_CUSTOM, KC.O)
        self.base_e_symbols = KC.LT(LAYER_ID_SYMBOLS, KC.E)
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
        self.combo_module.combos.append(Chord((KC.R, KC.I, self.base_e_symbols), KC.TO(LAYER_ID_NAVIGATION), timeout=150))
        self.combo_module.combos.append(Chord((KC.T, KC.Y, self.base_a_parens), KC.TO(LAYER_ID_MOUSE), timeout=150))
        # mods
        self.combo_module.combos.append(Chord((self.base_s_numbers, self.base_e_symbols), KC.SK(KC.LCTRL), timeout=100))
        self.combo_module.combos.append(Chord((KC.Y, self.base_s_numbers), KC.SK(KC.LGUI), timeout=100))
        self.combo_module.combos.append(Chord((KC.I, self.base_s_numbers), KC.SK(KC.LALT), timeout=100))
        self.combo_module.combos.append(Chord((self.base_s_numbers, KC.R, KC.T, self.base_e_symbols), KC.SK(KC.LSHIFT), timeout=200))
        # control sequences
        self.combo_module.combos.append(Chord((self.base_o_custom, KC.I, KC.Y, self.base_e_symbols), KC.SPACE, timeout=200))
        self.combo_module.combos.append(Chord((self.base_a_parens,  KC.R, self.base_o_custom), KC.ESCAPE, timeout=150))
        self.combo_module.combos.append(Chord((self.base_e_symbols,  KC.R), KC.BSPACE, timeout=100))
        self.combo_module.combos.append(Chord((KC.R,  KC.I), KC.DELETE, timeout=100))
        self.combo_module.combos.append(Chord((self.base_a_parens,  KC.R,  KC.T,  self.base_o_custom), KC.TAB, timeout=200))
        self.combo_module.combos.append(Chord((self.base_a_parens, self.base_e_symbols), KC.ENTER, timeout=100))
        self.combo_module.combos.append(Chord((self.base_a_parens, KC.Y, KC.I, self.base_o_custom), KC.CAPSLOCK, timeout=200))
        # symbols
        self.combo_module.combos.append(Chord((self.base_a_parens, KC.Y), KC.DOT, timeout=100))
        self.combo_module.combos.append(Chord((self.base_a_parens, KC.I), KC.COMMA, timeout=100))
        self.combo_module.combos.append(Chord((self.base_a_parens, self.base_o_custom), KC.SLASH, timeout=100))
        self.combo_module.combos.append(Chord((self.base_a_parens, KC.Y, KC.I), KC.QUOTE, timeout=150))
        # ansi
        self.combo_module.combos.append(Chord((self.base_o_custom, self.base_e_symbols), KC.B, timeout=100))
        self.combo_module.combos.append(Chord((self.base_e_symbols,  KC.Y), KC.C, timeout=100))
        self.combo_module.combos.append(Chord((KC.I,  self.base_o_custom), KC.N, timeout=100))
        self.combo_module.combos.append(Chord((self.base_a_parens,  KC.R), KC.F, timeout=100))
        self.combo_module.combos.append(Chord((KC.R, KC.T), KC.G, timeout=100))
        self.combo_module.combos.append(Chord((KC.Y, KC.I), KC.U, timeout=100))
        self.combo_module.combos.append(Chord((self.base_e_symbols, KC.I), KC.H, timeout=100))
        self.combo_module.combos.append(Chord((KC.R, self.base_s_numbers), KC.V, timeout=100))
        self.combo_module.combos.append(Chord((KC.T, self.base_s_numbers), KC.J, timeout=100))
        self.combo_module.combos.append(Chord((self.base_a_parens, self.base_s_numbers), KC.W, timeout=100))
        self.combo_module.combos.append(Chord((KC.Y, self.base_o_custom), KC.K, timeout=100))
        self.combo_module.combos.append(Chord((KC.Y, KC.I, self.base_o_custom), KC.M, timeout=150))
        self.combo_module.combos.append(Chord((self.base_a_parens, KC.R, KC.T), KC.D, timeout=150))
        self.combo_module.combos.append(Chord((self.base_o_custom, KC.I, self.base_e_symbols), KC.P, timeout=150))
        self.combo_module.combos.append(Chord((self.base_a_parens, KC.T,  self.base_s_numbers), KC.Q, timeout=150))
        self.combo_module.combos.append(Chord((KC.R, KC.T, self.base_s_numbers), KC.X, timeout=150))
        self.combo_module.combos.append(Chord((KC.I, KC.Y, self.base_e_symbols), KC.L, timeout=150))
        self.combo_module.combos.append(Chord((self.base_a_parens, KC.R, KC.T, self.base_s_numbers), KC.Z, timeout=200))
        
        #####
        # std - nav
        self.combo_module.combos.append(Chord((KC.UP, KC.LEFT, KC.RIGHT), KC.TO(LAYER_ID_BASE), timeout=150))
        self.combo_module.combos.append(Chord((KC.END, KC.RIGHT), KC.ENTER, timeout=100))
        self.combo_module.combos.append(Chord((KC.END, KC.UP, KC.PGDOWN), KC.ESCAPE, timeout=150))
        self.combo_module.combos.append(Chord((KC.RIGHT, KC.UP), KC.BSPACE, timeout=100))
        self.combo_module.combos.append(Chord((KC.UP, KC.LEFT), KC.DELETE, timeout=100))
        self.combo_module.combos.append(Chord((KC.END, KC.UP, KC.HOME, KC.PGDOWN), KC.TAB, timeout=2000))
        self.combo_module.combos.append(Chord((KC.RIGHT, KC.DOWN, KC.LEFT, KC.PGDOWN), KC.SPACE, timeout=200))
        self.combo_module.combos.append(Chord((KC.RIGHT, KC.PGUP), KC.SK(KC.LCTRL), timeout=100))
        self.combo_module.combos.append(Chord((KC.DOWN, KC.PGUP), KC.SK(KC.LGUI), timeout=100))
        self.combo_module.combos.append(Chord((KC.LEFT, KC.PGUP), KC.SK(KC.LALT), timeout=100))
        self.combo_module.combos.append(Chord((KC.RIGHT, KC.UP, KC.HOME, KC.PGUP), KC.SK(KC.LSHIFT), timeout=200))
        
        #####
        # std - number
        self.combo_module.combos.append(Chord((KC.N1, KC.N2), KC.N7, timeout=100))
        self.combo_module.combos.append(Chord((KC.N2, KC.N3), KC.N8, timeout=100))
        self.combo_module.combos.append(Chord((KC.N4, KC.N5), KC.N9, timeout=100))
        self.combo_module.combos.append(Chord((KC.N5, KC.N6), KC.N0, timeout=100))
        self.combo_module.combos.append(Chord((KC.N1, KC.N5), KC.DOT, timeout=100))
        self.combo_module.combos.append(Chord((KC.N1, KC.N6), KC.COMMA, timeout=100))
        self.combo_module.combos.append(Chord((KC.N1, KC.N4), KC.ENTER, timeout=100))
        self.combo_module.combos.append(Chord((KC.N2, KC.N6), KC.DELETE, timeout=100))
        self.combo_module.combos.append(Chord((KC.N4, KC.N2), KC.BSPACE, timeout=100))
        
        #####
        # std - mouse
        self.combo_module.combos.append(Chord((KC.MB_RMB, KC.MS_DN, KC.MB_LMB), KC.TO(LAYER_ID_BASE), timeout=150))

        # work around a bug with combo handling and layer selections in kmk
        #    these combos should be removed if/when kmk stops 'going hayware' or 'getting stuck' when these key combos are pressed when the below are not in the code
        self.combo_module.combos.append(Chord((self.base_o_custom, KC.Y, self.base_e_symbols), KC.NO, timeout=150))
        self.combo_module.combos.append(Chord((self.base_a_parens, KC.R,  self.base_s_numbers), KC.NO, timeout=150))
        self.combo_module.combos.append(Chord((self.base_a_parens, KC.T), KC.NO, timeout=100))
        self.combo_module.combos.append(Chord((self.base_o_custom, KC.T), KC.NO, timeout=100))
        self.combo_module.combos.append(Chord((self.base_o_custom, self.base_s_numbers), KC.NO, timeout=100))
        self.combo_module.combos.append(Chord((self.base_s_numbers, KC.Y), KC.NO, timeout=100))
