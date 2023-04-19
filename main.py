import board
import os

#####
# Main keyboard object
from ardux.kb import ArduxKeyboard
ardux_keyboard = ArduxKeyboard()

#####
# NeoPixel on kb2040 (tune accordingly / remove if different mcu)
from kmk.extensions.RGB import RGB, AnimationModes
rgb_ext = RGB(
    pixel_pin=board.NEOPIXEL,
    num_pixels=1,
    val_limit=100,
    val_default=25,
    animation_mode=AnimationModes.BREATHING_RAINBOW
)
ardux_keyboard.extensions.append(rgb_ext)

#####
# Main
if __name__ == '__main__':
    ardux_keyboard.go()

