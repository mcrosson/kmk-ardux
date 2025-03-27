from ardux.kb.big import _ArduxKeyboardBig

class _ArduxKeyboard40p(_ArduxKeyboardBig):
    coord_mapping = [
    ]

    keymap = []

    # Init / constructor / setup
    def __init__(self):
        super().__init__()
    
    def setup_layer_toggles(self):
        super().setup_layer_toggles()
    
    def setup_keymap(self):
        self.keymap = []

    # Define combos for ardux
    def setup_combos(self):
        super().setup_combos()
