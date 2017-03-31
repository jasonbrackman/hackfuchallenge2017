# coding=utf-8
#
# Name:     
# Tried:
# 1. Seperated out the original image from a downloaded equivalent to reveal:
#       DidTheMoonLandingReallyHappen?!?
# 2. Ran the image through a hex editor -- pass3/password is listed.
# 
# Creation Date: 3/31/2017
#
# --------------------------------------------------------------------------------------
import os
from PIL import Image
import challenge_00

def decrypt_message():
    passkey = '{}'.format('DidTheMoonLandingReallyHappen?!?'.lower())
    passkey = '{}'.format('DidTheMoonLandingReallyHappen'.lower())
    infile_ = os.path.abspath('./Challenges/Challenge 1/solution.txt.enc')
    outfile_ = os.path.abspath('./Challenges/Challenge 1/generated_content/solution.txt')

    challenge_00.decrypt_openssl(infile=infile_, outfile=outfile_, passphrase=passkey)


def get_new_data(im, value):
    width, height = im.size

    new_data = []
    for w in range(width):
        for h in range(height):

            pixel = im.getpixel((h, w))
            if value == pixel:
                pixel = 255
            else:
                pixel = 0
            new_data.append(pixel)

    return new_data


def explore_pixel_values(path_01, path_02):

    im_01 = Image.open(path_01)
    im_02 = Image.open(path_02)

    width, height = im_02.size

    pixels = []
    for w in range(width):
        for h in range(height):
            pixel_01 = im_01.getpixel((h, w))
            pixel_02 = im_02.getpixel((h, w))

            if pixel_01 == pixel_02:
                pixels.append((0, 0, 0))
            else:
                pixels.append((250, 250, 250))

    temp_im = Image.new(im_01.mode, im_01.size)
    temp_im.putdata(pixels)
    temp_im.save('./Challenges/Challenge 1/generated_content/output.jpg')

def convert_to_grayscale(path):
    im = Image.open(path)
    im = im.convert('1')
    im.save('grayscale_test.bmp')

if __name__ == "__main__":
    path = './Challenges/Challenge 1/AldrinApollo11'
    path02 = './Challenges/Challenge 1/generated_content/downloaded_from_internet.jpg'
    # explore_pixel_values(path, path02)

    decrypt_message()
