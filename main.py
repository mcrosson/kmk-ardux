import board
import os

from ardux import debug

#####
# import constants
from ardux.constants import ARDUX_REMIX

#####
# Main keyboard object
ardux_board = os.getenv('ARDUX_BOARD')
ardux_keyboard = None

# override defaults with remix data (if available)
# given how trim the circuit python libs are... we are going to use exec
# yes, this is not ideal
if ARDUX_REMIX:
    try:
        exec('from remixes.%s.boards.%s import %s' % (ARDUX_REMIX, ardux_board, os.getenv('ARDUX_REMIX_KB_CLASS')))
        exec('ardux_keyboard = %s()' % (os.getenv('ARDUX_REMIX_KB_CLASS')))
        if debug.enabled:
            debug('Using remix %s' % ARDUX_REMIX)
            debug('Using remixed keyboard class %s' % os.getenv('ARDUX_REMIX_KB_CLASS'))
    except:
        pass

# standard keyboard classes if not remixed
if not ARDUX_REMIX:
    if ardux_board == 'thepaintbrush':
        from boards.thepaintbrush import ThePaintbrushArduxKeyboard
        ardux_keyboard = ThePaintbrushArduxKeyboard()
    elif ardux_board == 'crkbd': # corne
        from boards.crkbd import CrkbdArduxKeyboard
        ardux_keyboard = CrkbdArduxKeyboard()
    else:
        raise NotImplementedError('Please configure the proper keyboard in "settings.toml"')

#####
# Main
if __name__ == '__main__':
    if os.getenv('CIRCUITPY_BLE_NAME'):
        from kmk.hid import HIDModes
        ardux_keyboard.go(hid_type=HIDModes.BLE, ble_name=os.getenv('CIRCUITPY_BLE_NAME'),
                          secondary_hid_type=HIDModes.USB
                          )
    else:
        ardux_keyboard.go()
