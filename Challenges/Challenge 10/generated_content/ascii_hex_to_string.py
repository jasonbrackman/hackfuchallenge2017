# coding=utf-8
# Creation Date: 5/2/2017
# --------------------------------------------------------------------------------------
import hashlib

# var_c = -0x0c
# arg_0 = 8
# arg_4 = 0x0c
#
# # 40 bytes to play with
# ebp = "pointer_to_caller"
# esp = "pointer_to_stack_length_40"
# eax = ebp + 8 # < pointer moves forward 8 bytes and puts that into the register.
# esp = eax # esp is now a character string of whatever was found an pointer ebp+8
# # the stringlength is found
# # this is populated to the ds: global memory space
x = 'domoarigatomrroboto'
for item in x:
    print(ord(item) )
num = '0415131501180907012015131891815021515\n'
totals = str('0415131501180907012015131891815021515')
counter = 0
for index in range(0, len(str(totals)), 2):
    counter += int(totals[index:index+2])
print(counter)
print(hashlib.md5(str(counter).encode()).hexdigest())

if __name__ == "__main__":
    pass