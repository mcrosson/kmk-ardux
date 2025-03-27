##########
# Print env vars if debugging enabled
import os
if bool(os.getenv('ARDUX_KMK_SHOW_ENV')):
    print('START env')
    print('SIZE:', os.getenv('ARDUX_SIZE'))
    print('HAND:', os.getenv('ARDUX_HAND'))
    print('BOARD:', os.getenv('ARDUX_BOARD'))
    print('MCU:', os.getenv('ARDUX_MCU'))
    print('BLE_NAME:', os.getenv('CIRCUITPY_BLE_NAME'))
    print('RGB_PIXEL_PIN:', os.getenv('ARDUX_RGB_PIXEL_PIN'))
    print('RGB_NUM_LEDS:', os.getenv('ARDUX_RGB_NUM_LEDS'))
    print('RGB_BRIGHTNESS:', os.getenv('ARDUX_RGB_BRIGHTNESS'))
    print('DISPLAY_DRIVER:', os.getenv('ARDUX_DISPLAY_DRIVER'))
    print('DISPLAY_HEIGHT:', os.getenv('ARDUX_DISPLAY_HEIGHT'))
    print('DISPLAY_WIDTH:', os.getenv('ARDUX_DISPLAY_WIDTH'))
    print('REMIX:', os.getenv('ARDUX_REMIX'))
    print('REMIX_KB_CLASS:', os.getenv('ARDUX_REMIX_KB_CLASS'))
    print('DEBUGGING:', os.getenv('ARDUX_KMK_DEBUGGING'))
    print('USB_DISK_ALWAYS:', os.getenv('ARDUX_KMK_USB_DISK_ALWAYS'))
    print('END env')

##########
# various `settings.toml` validations
if not os.getenv('ARDUX_SIZE'):
    print('`ARDUX_SIZE` configuration is required')
    raise NotImplementedError('`ARDUX_SIZE` configuration is required')

if os.getenv('ARDUX_SIZE') not in ('STANDARD', 'BIG', '40%'):
    print('Unsupported `ARDUX_SIZE`:'+ os.getenv('ARDUX_SIZE'))
    raise NotImplementedError('Unsupported `ARDUX_SIZE`:'+ os.getenv('ARDUX_SIZE'))

if not os.getenv('ARDUX_HAND'):
    print('`ARDUX_HAND` configuration is required')
    raise NotImplementedError('`ARDUX_HAND` configuration is required')

if os.getenv('ARDUX_HAND') not in ('LEFT', 'RIGHT'):
    print('Unsupported `ARDUX_HAND`:'+ os.getenv('ARDUX_HAND'))
    raise NotImplementedError('Unsupported `ARDUX_HAND`:'+ os.getenv('ARDUX_HAND'))

if not os.getenv('ARDUX_BOARD'):
    print('`ARDUX_BOARD` configuration is required')
    raise NotImplementedError('`ARDUX_BOARD` configuration is required')

if not os.getenv('ARDUX_MCU'):
    print('`ARDUX_MCU` configuration is required')
    raise NotImplementedError('`ARDUX_MCU` configuration is required')

if os.getenv('ARDUX_MCU') not in ('nice_nano', 'kb2040', 'sparkfun_promicro_rp2040'):
    print('Unsupported `ARDUX_MCU`:'+ os.getenv('ARDUX_MCU'))
    raise NotImplementedError('Unsupported `ARDUX_MCU`:'+ os.getenv('ARDUX_MCU'))

if os.getenv('ARDUX_RGB_PIXEL_PIN') and not os.getenv('ARDUX_RGB_NUM_LEDS'):
    print('`ARDUX_RGB_NUM_LEDS` must be set when `ARDUX_RGB_PIXEL_PIN` is set')
    raise NotImplementedError('`ARDUX_RGB_NUM_LEDS` must be set when `ARDUX_RGB_PIXEL_PIN` is set')

if os.getenv('ARDUX_DISPLAY_DRIVER') and not (os.getenv('ARDUX_DISPLAY_HEIGHT') and os.getenv('ARDUX_DISPLAY_WIDTH')):
    print('`ARDUX_DISPLAY_HEIGHT` and `ARDUX_DISPLAY_WIDTH` must be set when `ARDUX_DISPLAY_DRIVER` is set')
    raise NotImplementedError('`ARDUX_DISPLAY_HEIGHT` and `ARDUX_DISPLAY_WIDTH` must be set when `ARDUX_DISPLAY_DRIVER` is set')

if os.getenv('ARDUX_REMIX') and not os.getenv('ARDUX_REMIX_KB_CLASS'):
    print('`ARDUX_REMIX_KB_CLASS` must be set when `ARDUX_REMIX` is set')
    raise NotImplementedError('`ARDUX_REMIX_KB_CLASS` must be set when `ARDUX_REMIX` is set')

##########
# early boot config
if not bool(os.getenv('ARDUX_KMK_DEBUGGING')):
    # dont expose storage by default
    if not bool(os.getenv('ARDUX_KMK_USB_DISK_ALWAYS')):
        import storage
        storage.disable_usb_drive()
    
    # disable usb cdc stuff thats only useful when debugging
    import usb_cdc
    usb_cdc.disable() # Equivalent to usb_cdc.enable(console=False, data=False)

    # Enable use w/ bios when not debugging (serial device from debug messes things up)
    # this only works if *both* cdc and storage are disabled above
    import usb_hid
    from usb_hid import Device
    if not bool(os.getenv('ARDUX_KMK_USB_DISK_ALWAYS')):
        usb_hid.enable((Device.KEYBOARD,), boot_device=1)
