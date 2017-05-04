def convert_hex(hex_values):
    if not len(hex_values) % 2 == 0:
        raise(ValueError, "must be a valid hex number.")

    for index in range(0, len(hex_values), 2):
        print(hex_values[index:index+2])
        high = int(hex_values[index], 16)
        low = int(hex_values[index+1], 16)

        print(high, low, hex(high+low))



x = '0000040001070008' # 00401708
# x = '0015061114' # in that year on the 15th day, 6th, month 11:14
convert_hex(x)



