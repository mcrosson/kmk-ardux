import os
import board

from ardux.kb import _ArduxKeyboardStandard
from kmk.scanners.keypad import KeysScanner
from kmk.scanners import DiodeOrientation

mcu = os.getenv('ARDUX_MCU')
if 'kb2040' == mcu:
    from kmk.quickpin.pro_micro.kb2040 import pinout as pins
elif 'sparkfun_promicro_rp2040' == mcu:
    from kmk.quickpin.pro_micro.sparkfun_promicro_rp2040 import pinout as pins
elif 'nice_nano' == mcu:
    from kmk.quickpin.pro_micro.nice_nano import pinout as pins
else:
    print('Unsupported mcu: ', os.getenv('ARDUX_MCU'))
    raise NotImplementedError('Unsupported mcu:'+ os.getenv('ARDUX_MCU'))

# crkbd Implementationa
class CrkbdArduxKeyboard(_ArduxKeyboardStandard):
    def setup_physical_config(self):
        # General board config & setup
        self.col_pins = (
            pins[19],
            pins[18],
            pins[17],
            pins[16],
            pins[15],
            pins[14],
        )
        self.row_pins = (
            pins[6],
            pins[7],
            pins[8],
            pins[9],
        )
        self.diode_orientation = DiodeOrientation.COLUMNS

        self.coord_mapping = [
             0,  1,  2,  3,  4,  5,  29, 28, 27, 26, 25, 24,
             6,  7,  8,  9, 10, 11,  35, 34, 33, 32, 31, 30,
            12, 13, 14, 15, 16, 17,  41, 40, 39, 38, 37, 36,
                        21, 22, 23,  47, 46, 45,
        ]
