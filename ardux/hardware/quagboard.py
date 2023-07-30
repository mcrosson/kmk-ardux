from ardux.kb import _ArduxKeyboard
from kmk.scanners import DiodeOrientation

# Quagboard Implementation
class QuagboardArduxKeyboard(_ArduxKeyboard):
    def setup_physical_config(self):
        self.diode_orientation = DiodeOrientation.COL2ROW
        self.row_pins = (board.GP0,)
        #right hand pins
        #self.col_pins = (board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8 , board.GP10 , board.GP9)
        #left hand pins
        self.col_pins = (board.GP4, board.GP3, board.GP2, board.GP1, board.GP8, board.GP7, board.GP6, board.GP5 , board.GP9 , board.GP10)
