## !!! CRITICAL !!!

**This code is experimental. Things ARE BROKEN!**

### We are using the following upstream code:

- **CircuitPython**: `9.2.5`
- **KMK Code Revision**: `74b6a777dccda7d1940a1f303270eff9e60ee6a8`
- **Neopixel Library Code Revision**: `af8ae5e17b69e681978c80eb74bcf46e5b86f4af`

### nice!nano mcu

For those with a `nice!nano` mcu, please see the section below about using this mcu with the repo. There are setup and install/setup requirements that are *required* in order to use this mcu.

### Verifying CircuitPython Version

To check the CircuitPython version on your board, open the `boot_out.txt` and it should have the CircuitPython version that's setup on your mcu. Updates and instructions on how to update CircuitPython are available on the main CircuitPython site [here](https://circuitpython.org/downloads).

### KMK Version

We have vendored the KMK code within this repo. The `kmk` folder has the KMK release that is being developed against. Simply copy this folder to your mcu to install or update KMK. When updating the KMK code, it is recommended to delete the `kmk` folder on the mcu then copy this repos `kmk` folder to the mcu to ensure any renamed or deleted files are cleaned up as part of the update process.

### Required Libraries

Like the KMK code, we have vendored any required libraries used by this project. Simply copy the `lib` folder to the mcu to install or update the libraries. When updating the libraries, it is recommended to delete the `lib` folder on the mcu then copy this repos `lib` folder to the mcu to ensure any renamed or deleted files are cleaned up as part of the update process.

### Ardux

The main ardux code is contained in the `ardux` folder as well as `boot.py` and `main.py`. You'll need to copy these to the mcu to update. When updating, it is recommended to delete the `ardux` folder on the mcu then copy this repos `ardux` folder to the mcu to ensure any renamed or deleted files are cleaned up as part of the update process.

## nice!nano mcu

The `nice!nano` mcu does not have enough storage for KMK and ardux unless you take additional steps. In particular: the KMK *and* ardux code, *except* `boot.py` and `main.py`, should be compiled to `mpy` prior to copying to the mcu.

This repo is setup to automatically compile the code whenever we update the repo. Under `Releases` you'll find specific releases for the `nice!nano` that you'll need to use instead of the generic releases.

## Installation & Setup

To install KMK and ardux on an mcu:

1. Download the most recent release for your specific mcu, if available. Use the `generic` release for any mcu's not explicitly listed.
1. Extract the files to the `CIRCUITPY` disk exposed by the mcu
1. Adjust `settings.toml` as appropriate
1. Reboot the mcu as any changes to `boot.py` will not take effect until the mcu is restarted
1. Start using ardux

## Updating

Prior to updating ardux, it is wise to delete the `ardux`, `kmk` and `lib` folders to ensure any files that were renamed or deleted are cleaned up as part of the update process.

When upding ardux, follow the steps in `Installation & Setup` but do *not* copy `settings.toml` to the controller. Instead compare the `settings.toml` file in the release archive to the one that is already on your mcu and add any missing items to the copy on your mcu.

By not overwriting the `settings.toml` file, you'll retain your config file on update. However, you can overwrite `settings.toml` and re-configure if desired.

## Compiling to `mpy` by hand

Please see our GitHub actions for information on how we compile both KMK and ardux to `mpy` for release. These actions can easily be replicated in a local container environment.

Note: we borrowed the main KMK compilation processes and code and adapted them for use with this repo.

## Misc Information

Some things that may be useful for developers and those that'd like to dig deeper:

- Format storage via `REPL`: https://docs.circuitpython.org/en/latest/docs/troubleshooting.html
- [CircuitPython Docs](https://docs.circuitpython.org/en/latest/docs/environment.html#environment-variables)
- [MicroPython Docs](https://docs.micropython.org/en/latest/index.html)
