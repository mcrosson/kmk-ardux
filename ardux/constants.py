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
