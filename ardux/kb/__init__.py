import os
from ardux import debug
from kmk.modules.combos import Chord

class ArduxChord(Chord):
    def __init__(
        self,
        match: Tuple[Union[Key, int], ...],
        result: Key,
        fast_reset=None,
        per_key_timeout=None,
        timeout=None,
        match_coord=None,
    ):
        super().__init__(match, result, fast_reset, per_key_timeout, timeout, match_coord)
        if timeout is None:
            if os.getenv('ARDUX_COMBO_TIMEOUT'):
                self.timeout = os.getenv('ARDUX_COMBO_TIMEOUT')
            else:
                self.timeout = 175
        if debug.enabled:
            debug('Ardux timeout set to %d' % self.timeout)