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
# 6. https://ctfs.github.io/resources/topics/steganography/file-in-image/README.html
#    http://resources.infosecinstitute.com/steganography-what-your-eyes-dont-see/#gref
#    Almost certain this is the thing happening here... I need to extract an attached zip.
# 7. YES.  Have a 7z file (after mistaking it for a zip.) / Now thinking its a zip again(
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
# 9. Info about the 7z/Zip compression:
#  Name:                       pass3/password
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
# 10.  Online EXIF reader produced (why does it list two images?)
# Mimetype:  	 image/jpeg
# Mimetype:  	 image/jpeg
# Image dimensions:  	 2700x2700
# Image dimensions:  	 2700x2700
# Thumbnail:  	 (binary, 34263 bytes)
# Mimetype:  	 image/jpeg
# Unknown:  	 sof-marker=0
# Video dimensions:  	 2700x2700
# Video depth:  	 24
# Pixel aspect ratio:  	 1/1
# Mimetype:  	 application/zip
# Embedded filename:  	 pass3/
# Embedded filename:  	 pass3/password
#
# 11. Can't tell if I'm going down the wrong path -- but the only difference between my images and the original is the
#     - YCbCr4:4:4 vs. YCbCr4:2:0
#     - maybe more data is being hidden the values I'm throwing away?
#     - quick google search shows:
#     Park et al., [3], has proposed an image steganography method uses AC coefficients of the Discrete Cosine
#     Transform (DCT) domain to verify the secret information that is hidden in a spatial domain of the Carrier image
#     had been remove, replaced, forged or changed by attackers. LIU Tong and QIU, Zheng-ding [4], have presented a
#     method that hide the secret data or message into a color image by the quantization based Steganography in which
#     it guarantees the transportation of the secret data which will not attract the attention of eavesdropper. In this
#     method the original RGB image was transformed to YCbCr to use the perceptual masking function of YCbCr components;
#     since the marked strength is matched according to the human visual system. The perceptual quality of the
#     watermaked image is not severely deteriorated. The hidden message could be reliably extracted without degrading
#     original image.
#     https://www.rroij.com/open-access/an-efficient-and-secure-data-hidingtechnique--steganography.php?aid=44664
#
# 12. Tried reducing the bands of the original image to its lowest significant bit(s) -- Y appears to be the only
#     channel actually holding onto the watermark.  Attempting to take the LSB of all pixels in this channel and
#     group them back together again doesn't appear to reveal anything other than gibberish... (I keep going back
#     to #8...)
#
# 13. Randomly came across this online steghide website:
#   https://futureboy.us/stegano/decinput.html
#   entered in the password of: DidTheMoonLandingReallyHappen?!?
#   revealing anohter clue:
#       HereMenFromThePlanetEarthFirstSetFootUponTheMoon,July1969A.D.WeCameinPeaceForAllMankind
# Creation Date: 3/31/2017
#
# --------------------------------------------------------------------------------------
import os
import subprocess
from PIL import Image
import challenge_00
import random
import numpy
import itertools
import string
import base64
import binascii

from stegano import lsb, exifHeader

def identify_header(path):
    """
    - doesn't account for items that branch over two blocks
    - should really allow for headers to be filled and checked afterwards to determine the 'likelihood' of a match.
    :param path: 
    :return: 
    """
    headers = {'JFIF start': b'\xff\xd8',
               'JFIF end': b'\xff\xd9',
               'PKZip start': b'\x50\x4b\x03\x04\x14'}

    markers = list()

    with open(path, 'rb') as blob:
        print("length of file: {}".format(len(blob.read())))
        blob.seek(0)

        count = 0
        while True:
            chunk = blob.read(16)

            if chunk:
                for name, id in headers.items():
                    # attempt to find search pattern id
                    index = chunk.find(id)
                    if index >= 0:
                        # if found -- find out where we are
                        marker = count * 16 + index

                        if 'end' in name:
                            # if an end marker -- add the length of the marker to the total
                            marker += len(id)

                        markers.append(marker)
                        print(name, chunk, marker)
            else:
                break

            count += 1

    return markers


def split_binary(path, start, end=None):
    with open(path, 'rb') as blob:
        blob.seek(start)
        chunk = blob.read()

    with open('./Challenges/Challenge 1/generated_content/test.7z', 'wb') as blob:
        blob.write(chunk)


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
                dif = abs(pixel_01[2] - pixel_02[2])
                if dif >= 5:
                    # print(pixel_01, pixel_02, dif)
                    pixels.append((250, 250, 250))
                else:
                    pixels.append(pixel_01)

    temp_im = Image.new(im_01.mode, im_01.size)
    temp_im.putdata(pixels)
    temp_im.save('./Challenges/Challenge 1/generated_content/output_narrow.jpg')


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

    passwords = ['DidTheMoonLandingReallyHappen?!?',  # this is the correct length for an 256bit key
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
                 'pass', 'pass3', r'pass3/password', r'pass3\password', 'password', 'buzz',
                 'believe', '2700', '1969', '386',
                 'Fact', 'Fiction', 'fact', 'fiction', 'FACT', 'FICTION',
                 'lies', 'Lies', 'LIES',
                 'Fake', 'FAKE', 'fake', 'u4j',
                 'HereMenFromThePlanetEarthFirstSetFootUponTheMoon,July1969A.D.WeCameinPeaceForAllMankind']

    # passwords = [str(nums) for nums in range(99, 1000, 1)] <-- :(
    # passwords = (''.join(i) for i in itertools.product('DidTheMoonLandingReallyHappen?!?', repeat=32))
    # passwords = (''.join(i) for i in itertools.product(['Did', 'The', 'Moon', 'Landing', 'Really', 'Happen', '?!?'],
    #                                                    repeat=7))
    for index, password in enumerate(passwords):
        # password = base64.b64encode(password.encode())
        cmd = [r'/Users/jasonbrackman/Downloads/unar1.10.1/unar',
               '-f', '-p', password,  os.path.abspath(r'./Challenges/Challenge 1/generated_content/aldrinapollo11.zip')]

        # print(' '.join(cmd))
        proc = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        stderr, stdout = proc.communicate()
        print(password, stderr.decode())
        # print(password)
        response = 'FAIL' if b'fail' in stderr else 'PASS'
        if 'PASS' in response:
            print(index, '[{}] attempt with: {}'.format(response, password))
            break

def convertRGB2YCBCR(path):
    im = Image.open(path)
    ycbcr = im.convert("YCbCr")
    y, cb, cr = ycbcr.split()
    # r, g, b = im.split()
    data = y.getdata()
    print_lowest_bits(data)


def convert_rgb_to_bytes(path):
    with open(path, 'rb') as data:
        print_lowest_bits(data.read())


def mask_and_show_lsb(path):
    data = get_image_data(path)
    stuff = [(item & 0b00011111) << 3 for item in data]
    # for item in stuff:
    #     # print(format(item << 7, '#010b'))
    #     # print(format(item, '#010b'))
    #     print(int(item))
    im = Image.new('L', (2700, 2700))
    im.putdata(stuff)
    im.show()


def get_image_data(path):
    im = Image.open(path).convert('YCbCr')
    b1, b2, b3 = im.split()
    data = b1.getdata()
    return data


def get_pixel_data(path):
    img = Image.open(path)
    width, height = img.size
    pixels = []
    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            print(pixel)
            pixels.append(pixel)

    return pixels


def print_lowest_bits(path):
    #data = get_image_data(path)
    data = get_pixel_data(path)
    #stuff = [format(item, '#010b')[-1] for item in data]  # get LSB
    stuff = [str(item & 0b00000001) for item in data]
    collector = []

    for index in range(0, len(stuff), 8):
        num = ''.join(stuff[index:index + 8])
        collector.append(chr(int(num, 2)))
    print(''.join(collector))
    print(len(collector))


def stegano_attempt(path):
    path = os.path.abspath(path)
    # print(exifHeader.reveal(path))
    print(lsb.reveal(path))

if __name__ == "__main__":
    path = './Challenges/Challenge 1/AldrinApollo11'
    path02 = './Challenges/Challenge 1/generated_content/downloaded_from_internet.jpg'

    # identify watermark
    generate_differences_in_white_pixel_values(path, path02)

    # identify the zip file
    markers = identify_header(path)
    _, _, start_of_pkzip = markers

    # pull out the zip from the image
    split_binary(path, start=start_of_pkzip)

    # https://futureboy.us/stegano/decinput.html which is based off of steghide
    # Uploaded the original image and used the watermark as password to reveal:
    # HereMenFromThePlanetEarthFirstSetFootUponTheMoon,July1969A.D.WeCameinPeaceForAllMankind
    # This password was used to open the zip file, which generated:
    passkey = 'HackFuTheresAFalseWallInTheBackOfTheClosetQuiteObviousReally'.lower()

    # which was used to finish the puzzle
    decrypt_message(passkey)

    # investigative attempts:
    # crack_zip()
    # stegano_attempt(path)
    # display_hex_values(path)
    # convertRGB2YCBCR(path) # can delete?
    # print_lowest_bits(path)
    # convert_rgb_to_bytes(path)
    # mask_and_show_lsb(path)

