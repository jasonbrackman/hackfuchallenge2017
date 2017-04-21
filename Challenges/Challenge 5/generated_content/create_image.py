# coding=utf-8
#
# Creation Date: 4/20/2017
#
# --------------------------------------------------------------------------------------

from PIL import Image

def get_pixels():
    # pixels = list()

    with open('arr.txt.enc.dec', 'r') as handle:
        r = handle.read().strip().split(' ')
        print(len(r))
        # return [int(item) for item in r]

    with open('bee.txt.enc.dec', 'r') as handle:
        b = handle.read().strip().split(' ')
        print(len(b))

    with open('gee.txt.enc.dec', 'r') as handle:
        g = handle.read().strip().split(' ')
        print(len(g))

    for c1, c2, c3 in zip(r,g,b):
        pixels.append((int(c1), int(c2), int(c1)))

    return pixels


def create_image(pixels, width, height):
    temp_im = Image.new('L', (width, height))
    temp_im.putdata(pixels)
    temp_im.save('b_image.jpg')

if __name__ == "__main__":
    pixels = get_pixels()

    # for
    d1 = 35
    d2 = 99
    create_image(pixels, d1, d2)

    # for pixel in pixels:
    #     print(len(pixel))