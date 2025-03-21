from ardux.kb import _ArduxKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.quickpin.pro_micro.kb2040 import pinout as pins

# ThePaintbrush Implementation
class ThePaintbrushArduxKeyboard(_ArduxKeyboard):
    def setup_physical_config(self):
        # Direct wire & matrix setup
        self.matrix = KeysScanner(
            [pins[16], pins[17], pins[18], pins[19], 
             pins[12], pins[13], pins[14], pins[15]],
             value_when_pressed=False
        )

