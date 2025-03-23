import os

from kmk.utils import Debug
debug = Debug(__name__)

# Get remix info
ARDUX_REMIX = os.getenv('ARDUX_REMIX')
if debug.enabled:
    debug('Ardux remix: ', ARDUX_REMIX)

# layer constants
LAYER_ID_BASE = 0
LAYER_ID_PARENS = 1
LAYER_ID_NUMBERS = 2
LAYER_ID_NAVIGATION = 3
LAYER_ID_SYMBOLS = 4
LAYER_ID_CUSTOM = 5
LAYER_ID_MOUSE = 6

# color constants
HSV_BLUE = (170, 255, os.getenv('ARDUX_RGB_BRIGHTNESS', 255))
HSV_CYAN = (128, 255, os.getenv('ARDUX_RGB_BRIGHTNESS', 255))
HSV_PURPLE = (191, 255, os.getenv('ARDUX_RGB_BRIGHTNESS', 255))
HSV_ORANGE = (21, 255, os.getenv('ARDUX_RGB_BRIGHTNESS', 255))
HSV_RED = (0, 255, os.getenv('ARDUX_RGB_BRIGHTNESS', 255))
HSV_GREEN = (85, 255, os.getenv('ARDUX_RGB_BRIGHTNESS', 255))

# matching for rgb - this is the qmk logic
# base: blue
# 40p base: cyan
# numbers / symbols / paren / custom / big sym / 40p nav / 40p function: purple
# mouse / nav / big function: red
# latching keys (shift lock/caps): orange
color_map = [
    HSV_BLUE,
    HSV_PURPLE,
    HSV_PURPLE,
    HSV_RED,
    HSV_PURPLE,
    HSV_PURPLE,
    HSV_RED,
    HSV_ORANGE # latching keys @ end so can assume use of -1 for color index elsewhere
]

# override defaults with remix data (if available)
# given how trim the circuit python libs are... we are going to use exec
# yes, this is not ideal
if ARDUX_REMIX:
    try:
        exec('from remixes.%s.constants import *' % ARDUX_REMIX)
        if debug.enabled:
            debug('Using remixed constants.py')
    except:
        pass
