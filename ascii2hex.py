# Author: JohnsonCL Chen and ChatGPT

# Convert UTF-8 encode .hex file to raw format .bin file
source_file = open('pwr-200-wvd-5412-of-pm-New_Firmware.hex', 'r')
output_file = open('output.bin', 'wb')

# declare ASCII(UTF-8) character element
ascii_key = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
# declare binary value in decimal, int format
byte_value = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 58]
old_bin = 0
char_ctr = 0
hex_value = 0

while (1):
    # read one character of file
    char = source_file.read(1)
    char_ctr += 1
    print("char=", char)

    if not char:
        break

    # if start symbol : detected
    if char == ':':
        # write 0x3A into file
        bin = byte_value[16]
        old_bin = 0
        char_ctr = 2

    # abandon LF, CR symbol
    elif char == '/n' or char == '/r':
        old_bin = 0
        bin = 0
        char_ctr = 0

    # check if 0-9 A-F character match
    for i in range(16):
        if char == ascii_key[i]:
            bin = byte_value[i]
            break

    # Assemble two byte into one hex value
    if char_ctr == 2:
        hex_value = old_bin * 16 + bin
        output_file.write(hex_value.to_bytes(1, byteorder='big'))
        print("hex=", hex_value)
        bin = 0
        old_bin = 0
        char_ctr = 0
        # output_file.close()
        # break;
    else:
        old_bin = bin


source_file.close()
output_file.close()
