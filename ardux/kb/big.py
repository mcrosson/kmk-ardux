from ardux.kb.standard import _ArduxKeyboardStandard
from kmk.keys import KC

class _ArduxKeyboardBig(_ArduxKeyboardStandard):
    coord_mapping = [
    ]

    keymap = []

    # Init / constructor / setup
    def __init__(self):
        super().__init__()
    
    def setup_layer_toggles(self):
        super().setup_layer_toggles()
    
    def setup_keymap(self):
        self.keymap = [
            # std - left - base
            [self.base_s_numbers, KC.T,    KC.R,   self.base_a_parens,  KC.MINUS,
             self.base_o_custom,  KC.I,    KC.Y,   self.base_e_symbols, KC.SK(KC.LSHIFT),
             KC.SK(KC.LCTRL),     KC.AMPR, KC.DEL, KC.EQUAL,            KC.TAB,
             KC.NO, KC.ENTER, KC.SPACE
            ],
            # std - left - parenthesis
            [KC.RIGHT_CURLY_BRACE, KC.LEFT_PAREN, KC.RIGHT_PAREN, KC.TRANSPARENT, KC.NO,
             KC.LEFT_CURLY_BRACE,  KC.LBRACKET,   KC.RBRACKET,    KC.NO,          KC.NO,
             KC.NO, KC.NO, KC.NO
            ],
            # std - left - number
            [KC.TRANSPARENT, KC.N3, KC.N2, KC.N1, KC.NO,
             KC.NO,          KC.N6, KC.N5, KC.N4, KC.NO,
             KC.NO,          KC.NO, KC.NO
            ],
            # std - left - navigation
            [KC.PGUP,   KC.HOME, KC.UP,   KC.END, KC.NO,
             KC.PGDOWN, KC.LEFT, KC.DOWN, KC.RIGHT, KC.NO,
             KC.NO, KC.NO, KC.NO
            ],
            # std - left - symbols
            [KC.GRAVE, KC.SCOLON, KC.BSLASH,   KC.EXCLAIM,     KC.NO,
             KC.EQUAL, KC.MINUS,  KC.QUESTION, KC.TRANSPARENT, KC.NO,
             KC.NO, KC.NO, KC.NO
            ],
            # std - left - custom
            [KC.NO,          KC.AUDIO_VOL_UP,   KC.INSERT,  KC.AUDIO_MUTE, KC.NO,
             KC.TRANSPARENT, KC.AUDIO_VOL_DOWN, KC.PSCREEN, KC.RSHIFT,     KC.NO,
             KC.NO, KC.NO, KC.NO
            ],
            # std - left - mouse
            [KC.MW_UP,   KC.MB_RMB,  KC.MS_UP, KC.MB_LMB,   KC.NO,
             KC.MW_DOWN, KC.MS_LEFT, KC.MS_DN, KC.MS_RIGHT, KC.NO,
             KC.NO, KC.NO, KC.NO
            ]
        ]

    # Define combos for ardux
    def setup_combos(self):
        super().setup_combos()
