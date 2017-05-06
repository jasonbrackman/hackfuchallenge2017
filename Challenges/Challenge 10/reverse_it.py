
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
