import os
import board

ardux_rgb_active = bool(os.getenv('ARDUX_RGB_PIXEL_PIN'))

if ardux_rgb_active:
    from kmk.extensions.RGB import RGB, AnimationModes
    from ardux.constants import *
    rgb_ext = RGB(
        pixel_pin=eval('board.%s' % (os.getenv('ARDUX_RGB_PIXEL_PIN'))),
        num_pixels=os.getenv('ARDUX_RGB_NUM_LEDS'),
        # use first (default) layer from color map as default color
        # this solves an odd async hiccup on startup
        # kmk assumes `0` for default layer on startup
        hue_default=color_map[0][0],
        sat_default=color_map[0][1],
        val_default=color_map[0][2],
        animation_mode=AnimationModes.STATIC
    )

    def ardux_update_rgb_indicator(keyboard):
        if not ardux_rgb_active or not keyboard or not rgb_ext.pixels:
            return
        
        # shenanigans:
        #     - array makes lookups fast
        #     - the `*` unpacks the stored tuple as arguments to the function call
        #     - max looks for the highest layer active so the 'state' reflects the upper most, active layer
        rgb_ext.set_hsv_fill(*color_map[max(keyboard.active_layers)])
        rgb_ext.show()
