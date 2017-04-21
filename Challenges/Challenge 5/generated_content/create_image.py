# coding=utf-8
#
# Creation Date: 4/20/2017
#
# --------------------------------------------------------------------------------------

from PIL import Image


def get_pixels(file):
    # pixels = list()

    with open(file, 'r') as handle:
        lines = handle.readlines()
        width = len(lines)
        height = len(lines[5])

        handle.seek(0)

        pixels = handle.read().strip().split(' ')
        pixels = [int(item) for item in pixels]

    print(width)
    print(height)
    return pixels, width, height

    #
    # with open('arr.txt.enc.dec', 'r') as handle:
    #     r = handle.read().strip().split(' ')
    #     print(len(r))
    #     # return [int(item) for item in r]
    #
    # with open('bee.txt.enc.dec', 'r') as handle:
    #     b = handle.read().strip().split(' ')
    #     print(len(b))
    #
    # with open('gee.txt.enc.dec', 'r') as handle:
    #     g = handle.read().strip().split(' ')
    #     print(len(g))
    #
    # for c1, c2, c3 in zip(r,g,b):
    #     pixels.append((int(c1), int(c2), int(c1)))
    #
    # return pixels


def create_image(file, width, height):
    temp_im = Image.new('L', (width, height))

    with open(file, 'r') as handle:
        lines = handle.readlines()

        for row, pixels in enumerate(lines):
            pixels = pixels.strip().split(' ')
            for col, item in enumerate(pixels):
                temp_im.putpixel((row, col), int(item))

    temp_im.save('01_image.jpg')

if __name__ == "__main__":
    #pixels, width, height = get_pixels('gee.txt.enc.dec')
    create_image('01.txt.enc.dec', 150, 100)

    # for pixel in pixels:
    #     print(len(pixel))