import board
import os

from kb import KMKKeyboard
from kmk.keys import KC

keyboard = KMKKeyboard()

#####
# Enable debugging
if os.getenv('ARDUX_KMK_DEBUGGING'):
    keyboard.debug_enabled = True

#####
# NeoPixel on kb2040 (tune accordingly / remove if different mcu)
from kmk.extensions.RGB import RGB, AnimationModes
rgb_ext = RGB(
    pixel_pin=board.NEOPIXEL,
    num_pixels=1,
    val_limit=100,
    val_default=25,
    animation_mode=AnimationModes.RAINBOW
)
keyboard.extensions.append(rgb_ext)

#####
# Layers
from kmk.modules.layers import Layers
keyboard.modules.append(Layers())

#####
# Combos
from kmk.modules.combos import Combos, Chord
combos = Combos()
keyboard.modules.append(combos)

class KmNChord(Chord):
    def __init__(
        self,
        match: Tuple[Union[Key, int], ...],
        result: Key,
        fast_reset=None,
        per_key_timeout=None,
        timeout=None,
        match_coord=None,
        keyboard=None,
        layers=[],
    ):
        super().__init__(match, result, fast_reset, per_key_timeout, match_coord)
        self.keyboard = keyboard
        self.layers = layers
        
    def matches(self, key: Key, int_coord: int):
        if keyboard is None or len(self.layers) == 0 or any(i in self.keyboard.active_layers for i in self.layers):
            return super().matches(key, int_coord)
        
        return False

combos.combos = []

combo_enter = KmNChord((KC.A, KC.E), KC.ENTER, keyboard=keyboard, layers=[0])
combos.combos.append(combo_enter)

combo_space = KmNChord((KC.O, KC.I, KC.Y, KC.E), KC.SPACE, keyboard=keyboard, layers=[1])
combos.combos.append(combo_space)

#####
# Keymap
keyboard.keymap = [
    [KC.S, KC.T, KC.R, KC.A,
     KC.O, KC.I, KC.Y, KC.E]
]

#####
# Main
if __name__ == '__main__':
    print('begin main.py')
    keyboard.go()
    print('end main.py')

