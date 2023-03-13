# Intelhex2binary

## Description
This python script translate UTF-8 encode intel hex format file into real binary encoded binary file.

```
$ python3 Intelhex2binary.py
```

In this example use TI CCS generated file "pwr-200-wvd-5412-of-pm-New-firmware.hex" 
Translate into 
"output.bin"

The script translate start symbol **':'**into **"0xA3"** to match the command of I2C for firmware upgrading
For example, the following ASCII string **"F3"**
will translate into **0xF3** real binary value instead of **'0x46'** and **'0x33'**.

## Enviorement
VSCode python version:  python3.11
TI CCS version: 12.1.0.00007 
C2000 compiler tools version: 22.6.0LTS
