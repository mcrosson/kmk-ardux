import board
import os

from kmk.utils import Debug
debug = Debug(__name__)

#####
# Main keyboard object
ardux_board = os.getenv('ARDUX_BOARD')
ardux_keyboard = None

# Get remix info
ARDUX_REMIX = os.getenv('ARDUX_REMIX')
if debug.enabled:
    debug('Ardux remix: ', ARDUX_REMIX)

# override defaults with remix data (if available)
# given how trim the circuit python libs are... we are going to use exec
# yes, this is not ideal
ardux_board_custom = False
if ARDUX_REMIX:
    try:
        exec('from remixes.%s.hardware.%s import %s' % (ARDUX_REMIX, ardux_board, os.getenv('ARDUX_REMIX_KB_CLASS')))
        exec('ardux_keyboard = %s()' % (os.getenv('ARDUX_REMIX_KB_CLASS')))
        ardux_board_custom = True
        if debug.enabled:
            debug('Using remixed keyboard class %s' % os.getenv('ARDUX_REMIX_KB_CLASS'))
    except:
        pass

# standard keyboard classes if not remixed
if not ardux_board_custom:
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
