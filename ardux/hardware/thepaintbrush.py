from ardux.kb import _ArduxKeyboardStandard
from kmk.scanners.keypad import KeysScanner

import os
mcu = os.getenv('ARDUX_MCU')
if 'kb2040' == mcu:
    from kmk.quickpin.pro_micro.kb2040 import pinout as pins
elif 'sparkfun_promicro_rp2040' == mcu:
    from kmk.quickpin.pro_micro.sparkfun_promicro_rp2040 import pinout as pins
else:
    print('Unsupported mcu: ', os.getenv('ARDUX_MCU'))
    raise NotImplementedError('Unsupported mcu:'+ os.getenv('ARDUX_MCU'))


# ThePaintbrush Implementation
class ThePaintbrushArduxKeyboard(_ArduxKeyboardStandard):
    def setup_physical_config(self):
        # Direct wire & matrix setup
        self.matrix = KeysScanner(
            [pins[16], pins[17], pins[18], pins[19], 
             pins[12], pins[13], pins[14], pins[15]],
             value_when_pressed=False
        )

