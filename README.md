This code is experimental.

## Updating

- use bootloader mode to update circuit python
- `kmk` folder in main kmk firmware repo is what needs to be copied to mcu to update kmk
    - replace folder fully to ensure update is properly applied
- files in lib folder need updates too (see the rest of this readme on where to find the upstream files)

## NeoPixel

Put [this](https://raw.githubusercontent.com/adafruit/Adafruit_CircuitPython_NeoPixel/main/neopixel.py) in `lib` folder of CircuitPython disk (compile to `mpy` for nice!nano.

## Compile mpy files for nice!nano kmk

Note: nice!nano must be runing CircuitPython first. See [here](https://circuitpython.org/board/nice_nano/) for more information

``` bash
cd /tmp
git clone https://github.com/KMKfw/kmk_firmware.git
cd kmk_firmware
docker run -v .:/opt/kmk_firmware --rm -it ubuntu:24.04
cd /opt
apt update && apt install -y wget python3 python-is-python3 build-essential
wget https://adafruit-circuit-python.s3.amazonaws.com/bin/mpy-cross/linux-amd64/mpy-cross-linux-amd64-9.2.5.static
chmod a+x mpy-cross-linux-amd64-9.2.5.static
./mpy-cross-linux-amd64-9.2.5.static --help
mv mpy-cross-linux-amd64-9.2.5.static /usr/bin/mpy-cross
mpy-cross --help
cd /opt/kmk_firmware
make compile
cp `.compiled/kmk` folder -> mcu
```

## Misc

- hold boot button (left when usb @ top and chip side up), press reset button (right) to enter bootloader mode
- files in main storage in std boot are for kmk, libs, etc
- Format storage via `REPL`: https://docs.circuitpython.org/en/latest/docs/troubleshooting.html
- [MicroPython Docs](https://docs.micropython.org/en/latest/index.html)
- [CircuitPython Docs](https://docs.circuitpython.org/en/latest/docs/environment.html#environment-variables)
- Adafruit kb2040 circuit python updates are at: https://circuitpython.org/board/adafruit_kb2040/
