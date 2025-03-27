import os
import board

ardux_rgb_active = bool(os.getenv('ARDUX_RGB_PIXEL_PIN'))

if ardux_rgb_active:
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

    from kmk.extensions.RGB import RGB, AnimationModes
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
