import libscrc

#        bytes((0xAA, 0x55, 0xC0, 0x7F, 0x01, 0x06, 0x00, 0x02, 0x45)),
#        bytes((0xAA, 0x55, 0xC0, 0x7F, 0x01, 0x02, 0x00, 0x02, 0x41)),
#        bytes((0xF7, 0x03, 0x88, 0xB8, 0x00, 0x21, 0x3A, 0xC1)),


def sum(data: bytes):
    sum = 0
    for i in data:
        sum = sum + i
    return hex(sum)


# crc16 = libscrc.modbus(bytes((0xF7, 0x06, 0xB7, 0x98, 0x00, 0x02)))
crc16 = libscrc.modbus(bytes((0xAA, 0x55, 0xC0, 0x7F, 0x01, 0x02, 0x00)))
# crc16 = libscrc.modbus(bytes((0xF7, 0x03, 0x88, 0xB8, 0x00, 0x21)))
print(hex(crc16))
print(sum(bytes((0xAA, 0x55, 0xC0, 0x7F, 0x01, 0x59, 0x01, 0x00))))
print(sum(bytes((0xAA, 0x55, 0xC0, 0x7F, 0x01, 0x09, 0x00, 0x02, 0x48))))
print(sum(bytes.fromhex("aa557fc003d90106")))
print("{:04x}".format(libscrc.modbus(bytes.fromhex("F70388B80021"))))