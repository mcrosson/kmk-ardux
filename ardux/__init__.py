# setup debugging -- use this global to keep ram use down
import os
from kmk.utils import Debug
debug = Debug('ardux')
debug.enabled = bool(os.getenv('ARDUX_KMK_DEBUGGING'))
if not debug.enabled:
    debug('********** debug disabled **********')
