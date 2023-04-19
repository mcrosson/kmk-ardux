from kmk.modules.combos import Chord

# TODO: fix up pass by reference trick (wrapped in array) thats used below
#       likely deserves a global but KmN couldnt figure it out
class ArduxChord(Chord):    
    # Override default constructor to allow passing of required fields
    def __init__(
        self,
        match: Tuple[Union[Key, int], ...],
        result: Key,
        fast_reset=None,
        per_key_timeout=None,
        timeout=None,
        match_coord=None,
        ardux_keyboard=[],
        layers=[],
    ):
        super().__init__(match, result, fast_reset, per_key_timeout, match_coord)
        self.ardux_keyboard = ardux_keyboard
        self.layers = layers
    
    # Override standard kmk match logic to first check active vs allowed layers
    def matches(self, key: Key, int_coord: int):
        if self.ardux_keyboard is None or len(self.ardux_keyboard) == 0 or len(self.layers) == 0 or any(i in self.ardux_keyboard[0].active_layers for i in self.layers):
            return super().matches(key, int_coord)
        
        return False
