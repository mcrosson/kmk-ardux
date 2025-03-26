import os

from kmk.utils import Debug
debug = Debug(__name__)

import busio
import board

from kmk.extensions.display import Display, TextEntry, ImageEntry

from ardux.constants import *

if 'SSD1306' == os.getenv('ARDUX_DISPLAY_DRIVER'):
    from kmk.extensions.display.ssd1306 import SSD1306

class ArduxDisplay(Display):
    def render(self, layer):
        # Simple, non-ideal fix for memory alloc error when refreshing oled
        #    - this is issue is mainly seen on the n!n
        #    - this is not an ideal fix
        #    - this causes the display to 'blink'
        self.display.root_group = None
        super().render(layer)

# Init as blank, set these based on which oled is enabled in config
i2c_bus = None
display_driver = None
display = None

if 'SSD1306' == os.getenv('ARDUX_DISPLAY_DRIVER'):
    i2c_bus = busio.I2C(scl=board.SCL, sda=board.SDA)
    display_driver = SSD1306(
        i2c=i2c_bus,
        # Optional device_addres argument. Default is 0x3C.
        # device_address=0x3C,
    )

    display = ArduxDisplay(
        display=display_driver,
        entries=[
            TextEntry(text='Layer: ', x=0, y=4, x_anchor='L', y_anchor='T'),
            TextEntry(text='Base', layer=LAYER_ID_BASE, x=40, y=4, x_anchor='L', y_anchor='T'),
            TextEntry(text='Parens', layer=LAYER_ID_PARENS, x=40, y=4, x_anchor='L', y_anchor='T'),
            TextEntry(text='Numbers', layer=LAYER_ID_NUMBERS, x=40, y=4, x_anchor='L', y_anchor='T'),
            TextEntry(text='Navigation', layer=LAYER_ID_NAVIGATION, x=40, y=4, x_anchor='L', y_anchor='T'),
            TextEntry(text='Symbols', layer=LAYER_ID_SYMBOLS, x=40, y=4, x_anchor='L', y_anchor='T'),
            TextEntry(text='Custom', layer=LAYER_ID_CUSTOM, x=40, y=4, x_anchor='L', y_anchor='T'),
            TextEntry(text='Mouse', layer=LAYER_ID_MOUSE, x=40, y=4, x_anchor='L', y_anchor='T'),
            TextEntry(text='Mods: [n/a]', x=0, y=32, x_anchor='L', y_anchor='B'),
        ],
        width=os.getenv('ARDUX_DISPLAY_WIDTH'),
        height=os.getenv('ARDUX_DISPLAY_HEIGHT')
    )
