import board
import os

#####
# Main keyboard object
ardux_board = os.getenv('ARDUX_BOARD')
if ardux_board == 'thepaintbrush':
    from ardux.hardware.thepaintbrush import ThePaintbrushArduxKeyboard
    ardux_keyboard = ThePaintbrushArduxKeyboard()
else:
    raise NotImplementedError('Please configure the proper keyboard in "settings.toml"')

#####
# NeoPixel on kb2040 (tune accordingly / remove if different mcu)
if os.getenv('ARDUX_RGB_KB2040'):
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

