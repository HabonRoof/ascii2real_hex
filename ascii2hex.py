source = "pwr-200-wvd-5412-of-pm-New_Firmware.hex"
output = "output2.bin"

with open(output, "wb") as ostream:
    with open(source, "r", encoding="utf-8") as istream:
        for line in istream.readlines():
            ostream.write(bytes.fromhex("3A" + line[1:]))
