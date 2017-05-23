
"""
def convert_hex(hex_values):
    if not len(hex_values) % 2 == 0:
        raise(ValueError, "must be a valid hex number.")

    for index in range(0, len(hex_values), 2):
        print(hex_values[index:index+2])
        high = int(hex_values[index], 16)
        low = int(hex_values[index+1], 16)

        print(high, low, hex(high+low))



# x = '0000040001070008' # 00401708
# y = '112233445566778899001122112233445566778899001122444444E8174000'
# z = '223322332233223322332266227722adde0000efbe0000efbe'
# last input originals.
# b = '1d1940001d1940001d194000227722adde0000efbe0000031a4000E8174000031a4000'
# p = 'bbbbbbbbcccccccc33333333999999adde0000efbe00001d194000E8174000031a4000'


# first two inputs
# - important part here for input #1: E8174000
a = '000000000000000000000000000000000000000000000000000000E8174000'

b = '000000000000000000000000000000adde0000efbe0000031a4000E81740001d194000'

a = '000000000000000000000000000000adde0000efbe0000031a4000E81740001d194000'

# last input used:
# - important to have:  031a4000 - 00401a03
#                       0df0edfe - feedf00d
#                      
q = '1111111111111111111111111111110df0edfeefbe00001d194000E8174000031a4000'
     



"""
import base64
import itertools

import binascii

test = '6>#"26 Z7;ol`h☺{n↔sfj|lk∟xtmfshs-:-/V):03;ulwerwi↔ph↨txl'
print(test)
# key = itertools.cycle([94, 95, 64, 73, 84, 67])
# line = ''.join([chr(k ^ ord(item)) for item, k in zip(test, key)])
# print(line)
#
original = """06 0E 17 12 03 01 10 18 07 0B 5B 5C 51 5F 44 43 5E 2D 47 56 5B 45 5D 5B 2C 4C 44 5C 51 43 45 58
43 19 0A 1C 18 13 11 0A 00 07 0B 44 55 46 55 42 43 59 2C 47 58 55 44 48 58 30 59 42 55"""

counter = 110
for item in original.split():
    i = int(item, 16)
    print(item, '--> ', i, '--> ', chr(i ^ counter))
    counter += 1


i = int('06', 16)
for index in range(256):
    new = chr(i ^ index)
    if new in 'hH':
        print(i, index, hex(index), new)


i = int('0E', 16)
for index in range(256):
    new = chr(i ^ index)
    if new in 'aA':
        print(i, index, hex(index), new)


i = int('17', 16)
for index in range(256):
    new = chr(i ^ index)
    if new in 'cC':
        print(i, index, hex(index), new)

i = int('12', 16)
for index in range(256):
    new = chr(i ^ index)
    if new in 'kK':
        print(i, index, hex(index), new)

print(int('00000030', 16) ^ int('00000006', 16))

'6E6F74796574646f6e6528'
' n o t y e t d o n e '

for item in 'notyetdone(':
    print(hex(ord(item)), end=' ')