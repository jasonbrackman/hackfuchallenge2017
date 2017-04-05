# coding=utf-8
#
# Name:     
# Tried:
# 1. Seperated out the original image from a downloaded equivalent to reveal:
#       DidTheMoonLandingReallyHappen?!?
# 2. Ran the image through a hex editor -- pass3/password is listed (multiple times).
# 3. Feels like: http://worldcomp-proceedings.com/proc/p2012/IPC4659.pdf
# 4. Image is a bmp (uncompressed) so the bits are likely important. (this is wrong its a JFIF (JPG file))
# 5. Last 256 bytes produce the following:
#
#    1ØýuPK?    [X4J             $       íA    pass3/
#             \ûûrÒ §ì ürÒ\ûûrÒPK?3 c ·U4J    N   =    /        ¤$   pass3/password
#             ÓùrÒÀüûrÒÇÔðûrÒ  AE PK      Ã   ©     
# 6. https://ctfs.github.io/resources/topics/steganography/file-in-image/README.htmla
#    Almost certain this is the thing happening here... I need to extract an attached zip.
# 7. YES.  Have a 7z file (after mistaking it for a zip.)
# 8. ... but now I need the password :(
# -- not any of these:
#   DidTheMoonLandingReallyHappen?!?
#   DidTheMoonLandingReallyHappen
#   Did The Moon Landing Really Happen
#   did the moon landing really happen
#   didthemoonlandingreallyhappen?!?
#   DidTheMoonLandingReallyHappen
#   Yes
#   yes
#   No
#   no
#   AldrinApollo11
#   1969
# 9. Info about the 7z compression:
# Name:                       pass3/password
#  Size:                       61 bytes
#  Compressed size:            78 bytes
#  Is encrypted:               Yes
#  Last modified:              Friday, January 20, 2017 at 10:45:46 AM
#  Unix permissions:           rw-r--r-- (100644)
#  Index in file:              1
#  Start of data:              91
#  Length of data:             78
#  WinZipAESCompressionMethod: 8
#  WinZipAESKeySize:           1
#  WinZipAESVendor:            17729
#  WinZipAESVersion:           2
#  ZipCRC32:                   0x00000000
#  ZipCompressionMethod:       99
#  ZipExtractVersion:          819
#  ZipFileAttributes:          -2119925728
#  ZipFlags:                   1
#  ZipLocalDate:               1244943799
#  ZipOS:                      3
#  ZipOSName:                  Unix
#  Flags  File size   Ratio  Mode  Date       Time   Name
#     =====  ==========  =====  ====  ========== =====  ====
#  0. D----           0  -----  None  2017-01-20 11:02  pass3/
#  1. ---E-          61 -27.9%  ----  2017-01-20 10:45  pass3/password
#
# Creation Date: 3/31/2017
#
# --------------------------------------------------------------------------------------
import os
import subprocess
import gzip
from PIL import Image
import challenge_00
import random


def decrypt_message(passkey):
    infile_ = os.path.abspath('./Challenges/Challenge 1/solution.txt.enc')
    outfile_ = os.path.abspath('./Challenges/Challenge 1/generated_content/solution.txt')

    challenge_00.decrypt_openssl(infile=infile_, outfile=outfile_, passphrase=passkey)


def generate_differences_in_white_pixel_values(path_01, path_02):

    im_01 = Image.open(path_01)
    im_02 = Image.open(path_02)

    width, height = im_02.size

    pixels = []
    for w in range(width):
        for h in range(height):
            pixel_01 = im_01.getpixel((h, w))
            pixel_02 = im_02.getpixel((h, w))

            if pixel_01 == pixel_02:
                pixels.append(pixel_01)
            else:
                dif = abs(sum(pixel_01) - sum(pixel_02))
                if dif > 20:
                    print(pixel_01, pixel_02, dif)
                    pixels.append((250, 250, 250))
                else:
                    pixels.append(pixel_01)

    temp_im = Image.new(im_01.mode, im_01.size)
    temp_im.putdata(pixels)
    temp_im.save('./Challenges/Challenge 1/generated_content/output_narrow.jpg')


# def convert_to_grayscale(path):
#     im = Image.open(path)
#     im = im.convert('1')
#     im.save('grayscale_test.bmp')


# def get_new_data(im, value):
#     width, height = im.size
#
#     new_data = []
#     for w in range(width):
#         for h in range(height):
#
#             pixel = im.getpixel((h, w))
#             if value == pixel:
#                 pixel = 255
#             else:
#                 pixel = 0
#             new_data.append(pixel)
#
#     return new_data

def display_hex_values(path):
    with open(path, 'rb') as handle:
        while True:
            chunk = handle.read(16)
            if not chunk:
                break
            else:

                stuff = ' '.join(hex(item) for item in chunk)
                stuff2 = ''.join(chr(item) for item in chunk)
                print(stuff, stuff.count('0xff 0xd9'))
                #print(stuff2, 'hack' in stuff2)
                # handle.seek(0)


def generate_password(wordlist):
    choice = random.SystemRandom().choice
    number = random.randrange(1, 20)
    return ''.join(choice(wordlist) for ii in range(number))


def crack_zip():
    # passwords = (generate_password(['Did', ' ', 'The', 'Moon', 'Landing', 'Really', 'Happen', '?!?'])
    #              for x in range(100000))

    passwords = ['DidTheMoonLandingReallyHappen?!?',
                 'DidTheMoonLandingReallyHappen?',
                 'didthemoonlandingreallyhappen?!',
                 'didthemoonlandingreallyhappen?',
                 'Did The Moon Landing Really Happen?!?',
                 'Did The Moon Landing Really Happen ? ! ?',
                 'DIDTHEMOONLANDINGREALLYHAPPEN',
                 'DID THE MOON LANDING REALLY HAPPEN',
                 "dtmlrh",
                 'yes', 'YES', 'y', 'Yes', 'Y',
                 'no', 'NO', 'No', 'n', 'N',
                 'AldrinApollo11', 'pass3', 'hackfu', 'moon', 'tunnel', '',
                 'pass3', r'pass3/password', r'pass3\password', 'password', 'buzz',
                 'believe', '2700', '1969',
                 'Fact', 'Fiction', 'fact', 'fiction', 'FACT', 'FICTION', 'lies', 'Lies', 'LIES']
    for index, password in enumerate(passwords):
        cmd = ['/Users/jasonbrackman/Downloads/unar1.10.1/unar',
               '-q',
               '-p',
               password,
               r'./Challenges/Challenge 1/generated_content/pass3.7z']

        # print(' '.join(cmd))
        proc = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

        proc.wait()

        print(index, proc.communicate()[0], '\r', end='')

if __name__ == "__main__":
    path = './Challenges/Challenge 1/AldrinApollo11'
    path02 = './Challenges/Challenge 1/generated_content/downloaded_from_internet.jpg'
    crack_zip()
    # display_hex_values(path)
    # generate_differences_in_white_pixel_values(path, path02)

    # decrypt_message()
