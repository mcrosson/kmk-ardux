import os

from kmk.modules.layers import Layers

from ardux.rgb import *

class ArduxLayers(Layers):
    def activate_layer(self, keyboard, layer, idx=None):
        super().activate_layer(keyboard, layer, idx=None)
        if ardux_rgb_active:
            ardux_update_rgb_indicator(keyboard)
    
    def deactivate_layer(self, keyboard, layer):
        super().deactivate_layer(keyboard, layer)
        if ardux_rgb_active:
            ardux_update_rgb_indicator(keyboard)
