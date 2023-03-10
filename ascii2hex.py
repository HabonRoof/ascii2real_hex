#Author: JohnsonCL Chen and ChatGPT
# Convert UTF-8 encode .hex file to raw format .bin file
source_file = open('pwr-200-wvd-5412-of-pm.hex','r')
output_file = open('output.bin','wb')

# declare ASCII(UTF-8) character element
ascii_key = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
# declare binary value in decimal, int format
byte_value = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 58]

# transformat the decimal value into binary value using bytearray()
# real binary data [0x00, 0x01, 0x02... 0x0F, 0xA8]
binary_data = bytearray(byte_value)
print(binary_data)
output_file.write(binary_data)
# binary indicator
bin = binary_data[0]
hex_value = 0x00
char_ctr = 0

while(1):
    # read one character of file
    char = source_file.read(1)

    if not char:
        break;
    # if start symbol : detected
    elif char == ':':
        # write 0x3A into file
        bin = byte_value[16]
    # abandon LF, CR symbol
    elif char == '\n' or char == '\r':
        pass
    # check if 0-9 A-F character match
    for i in range(15):
        if char == ascii_key[i]:
            bin = byte_value[i]

    # Assemble two byte into one hex value
    if char_ctr % 2 != 0:
        hex_value = (bin & 0xFF) << 8 + hex_value
        output_file.write(hex_value)
    else:
        hex_value = bin & 0xFF

    char_ctr += 1
    print("char=",char,"bin=",bin)

source_file.close()
output_file.close()
