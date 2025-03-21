This code is experimental.

## Updating

- use bootloader mode to update circuit python
- `kmk` folder in main kmk firmware repo is what needs to be copied to mcu to update kmk
    - replace folder fully to ensure update is properly applied
- files in lib folder need updates too (see the rest of this readme on where to find the upstream files)

## NeoPixel

Put [this](https://raw.githubusercontent.com/adafruit/Adafruit_CircuitPython_NeoPixel/main/neopixel.py) in `lib` folder of CircuitPython disk (compile to `mpy` for nice!nano.

## Compile mpy files for nice!nano kmk

WARNING: This is likely outdated and needs a revisit

``` bash
docker run -v /scratch/kmk_firmware:/opt/kmk_firmware --rm -it --entrypoint=/bin/bash python:latest
cd /opt
wget https://adafruit-circuit-python.s3.amazonaws.com/bin/mpy-cross/mpy-cross.static-amd64-linux-8.0.5
chmod a+x mpy-cross.static-amd64-linux-8.0.5
./mpy-cross.static-amd64-linux-8.0.5 --help
mv mpy-cross.static-amd64-linux-8.0.5 /usr/bin/mpy-cross
mpy-cross --help
cd /opt/kmk_firmware
python util/compile.py
cp ~.compiled/kmk~ folder -> mcu
```

## Misc

- hold boot button (left when usb @ top and chip side up), press reset button (right) to enter bootloader mode
- files in main storage in std boot are for kmk, libs, etc
- Format storage via `REPL`: https://docs.circuitpython.org/en/latest/docs/troubleshooting.html
- [MicroPython Docs](https://docs.micropython.org/en/latest/index.html)
- [CircuitPython Docs](https://docs.circuitpython.org/en/latest/docs/environment.html#environment-variables)
- Adafruit kb2040 circuit python updates are at: https://circuitpython.org/board/adafruit_kb2040/
