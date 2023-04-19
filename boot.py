print('START boot.py')

# Used http://kmkfw.ioy/docs/boot/ as starting point

import os

# Enable use w/ BIOS
if os.getenv('ARDUX_KMK_DEBUGGING'):
    print('START bios hid enable')
import usb_hid
from usb_hid import Device
usb_hid.enable((Device.KEYBOARD, Device.MOUSE), boot_device=1)
if os.getenv('ARDUX_KMK_DEBUGGING'):
    print('END bios hid enable')

# Print env vars if debugging enabled
if os.getenv('ARDUX_KMK_DEBUGGING'):
    print('debugging enabled')
    print('START env')
    print('CIRCUITPY_BLE_NAME:', os.getenv('CIRCUITPY_BLE_NAME'))
    print('ARDUX_KMK_DEBUGGING:', os.getenv('ARDUX_KMK_DEBUGGING'))
    print('ARDUX_KMK_USB_DISK_ALWAYS:', os.getenv('ARDUX_KMK_USB_DISK_ALWAYS'))
    print('ARDUX_SIZE:', os.getenv('ARDUX_SIZE'))
    print('ARDUX_HAND:', os.getenv('ARDUX_HAND'))
    print('ARDUX_BOARD:', os.getenv('ARDUX_BOARD'))
    print('END env')
else:
    print('debugging disabled')

# If this key is held during boot, don't run the code which hides the storage and disables serial
# bottom row, index finger key / bottom row pinky key
import digitalio
from kmk.quickpin.pro_micro.kb2040 import pinout as pins
key_1 = digitalio.DigitalInOut(pins[12])
key_2 = digitalio.DigitalInOut(pins[15])

# Configure gpio for boot
key_1.switch_to_input(pull=digitalio.Pull.UP)
key_2.switch_to_input(pull=digitalio.Pull.UP)

# Pull up means 'active low' so invert pin values for positive logic below
key_1_val = not (key_1.value)
key_2_val = not (key_2.value)

# Check for key hold and disable any dangerous features
if not (key_1_val or key_2_val) and not os.getenv('ARDUX_KMK_DEBUGGING'):
    if not os.getenv('ARDUX_KMK_USB_DISK_ALWAYS'):
        import storage
        storage.disable_usb_drive()
    import usb_cdc
    usb_cdc.disable() # Equivalent to usb_cdc.enable(console=False, data=False)

# Deinit pins so they can be setup per the kmk keymap post-boot
key_1.deinit()
key_2.deinit()

print('END boot.py')
