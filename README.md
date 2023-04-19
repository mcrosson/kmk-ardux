This code is experimental.

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
