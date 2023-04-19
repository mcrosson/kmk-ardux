import os
import board
from kmk.quickpin.pro_micro.kb2040 import pinout as pins
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.modules.layers import Layers
from kmk.modules.combos import Combos, Chord

from kmk.keys import KC
@
# TODO: fix up pass by reference trick (wrapped in array) thats used below
#       likely deserves a global but KmN couldnt figure it out
class ArduxChord(Chord):    
    # Override default constructor to allow passing of required fields
    def __init__(
        self,
        match: Tuple[Union[Key, int], ...],
        result: Key,
        fast_reset=None,
        per_key_timeout=None,
        timeout=None,
        match_coord=None,
        ardux_keyboard=[],
        layers=[],
    ):
        super().__init__(match, result, fast_reset, per_key_timeout, match_coord)
        self.ardux_keyboard = ardux_keyboard
        self.layers = layers
    
    # Override standard kmk match logic to first check active vs allowed layers
    def matches(self, key: Key, int_coord: int):
        if self.ardux_keyboard is None or len(self.ardux_keyboard) == 0 or len(self.layers) == 0 or any(i in self.ardux_keyboard[0].active_layers for i in self.layers):
            return super().matches(key, int_coord)
        
        return False

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
