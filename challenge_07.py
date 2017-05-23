# coding=utf-8
#
# --------------------------------------------------------------------------------------

from PIL import Image
import os
import challenge_00


def get_image_data(path):
    im = Image.open(path)
    data = im.getdata()
    for item in data:
        print(item)
    return data


def print_lowest_bits(path):
    data = get_image_data(path)
    #stuff = [format(item, '#010b')[-1] for item in data]  # get LSB
    stuff = [str(item & 0b00000001) for item in data]
    collector = []

    for index in range(0, len(stuff), 8):
        num = ''.join(stuff[index:index + 8])
        collector.append(chr(int(num, 2)))
    print(''.join(collector))
    print(len(collector))


def create_white_map_template(input_01, output_01, input_02):
    im01 = Image.open(input_01)
    im02 = Image.open(output_01)
    im03 = Image.open(input_02)

    data01 = im01.getdata()
    data02 = im02.getdata()
    data03 = im03.getdata()
    for d in data03:
        print(d)
    count = 0
    for x, y in zip(data01, data02):
        print('[{}]'.format('w' if y == (255, 255, 255, 255) else 'b'), end='')
        # print(count, '[{}]'.format('white' if y == (255, 255, 255, 255) else 'black'), x, end='')
        if count != 0 and count % 112 == 0:
            print()
        count += 1
    print(count)

    whites = [col01 for col01, col02 in zip(data01, data02) if col02 == (255, 255, 255, 255)]
    blacks = [col01 for col01, col02 in zip(data01, data02) if col02 == (0, 0, 0, 255)]

    im = Image.new(im03.mode, im03.size)
    pixels = []
    for index, pixel in enumerate(data03):
        if pixel in whites:
            pixels.append((255, 255, 255, 255))
        elif pixel in blacks:
            pixels.append((0, 0, 0, 255))
        else:
            pixels.append((127, 127, 127, 255))

    im.putdata(pixels)
    im.save('./challenges/challenge 7/generated_content/test.png')
    # im.show()

def decrypt_message(passkey):
    infile_ = os.path.abspath('./Challenges/Challenge 7/solution.txt.enc')
    outfile_ = os.path.abspath('./Challenges/Challenge 7/generated_content/solution.txt')

    challenge_00.decrypt_openssl(infile=infile_, outfile=outfile_, passphrase=passkey)

if __name__ == "__main__":
    input_01 = './challenges/challenge 7/input1.png'
    output_01 = './challenges/challenge 7/output1.png'
    a = './challenges/challenge 7/input2.png'
    # create_white_map_template(input_01, output_01, a)
    passkey = 'hackfuwearehonouredtohavewithusarevolutionaryofadifferentcalibre'
    decrypt_message(passkey)
