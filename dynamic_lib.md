# How to obtain libcolors.so

On your computer, make sure you have `git`, `make` and `gcc` installed. 
This library has only been tested with GNU-gcc, but clang and others should work. 
(Should also work on macos, not tested with Windows)

In the terminal, run:

```shell
git clone https://github.com/Ulincsys/C-colors-header

cd C-colors-header

make build

cp build/libcolors.so ../

cd ..
```

Then you can run this example using: `python dynamic_lib.py`