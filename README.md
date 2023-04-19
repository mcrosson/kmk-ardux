This code is experimental.

## NeoPixel

Put [this](https://raw.githubusercontent.com/adafruit/Adafruit_CircuitPython_NeoPixel/main/neopixel.py) in `lib` folder of CircuitPython disk (compile to `mpy` for nice!nano.

## Compile mpy files for nice!nano kmk

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

- Press reset button when NeoPixel starts to blink yellow during early boot.
- Format storage via `REPL`: https://docs.circuitpython.org/en/latest/docs/troubleshooting.html
- [MicroPython Docs](https://docs.micropython.org/en/latest/index.html)
- [CircuitPython Docs](https://docs.circuitpython.org/en/latest/docs/environment.html#environment-variables)

