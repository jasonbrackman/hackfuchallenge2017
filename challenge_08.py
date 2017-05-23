# looked at the wav file with the spectrogram -- found a qr code:
import base64
import os

import subprocess

import collections
from PIL import Image

import hashlib

# Using the crackstation wordlist revealed the following MD5 hashes:
import binascii

import challenge_00

zip_file = 'password\n'
wav_file = 'hellomoto\n'  # moto in English means 'the origin; the cause; the foundation; the basis.'
qr_code = 'domoarigatomrroboto\n'

wav = '047b704a141707ec15a8171ab1d37dbd'
zip = '286755fad04869ca523320acce0dc6a4' # == hashlib.md5((zip + '\n').encode().hexdigest())
key = 'c409227ae91cee2dba2cacae31dc1588'  # hashlib.md5('domoarigatomrroboto\n'.encode()).hexdigest()


def unzip(input_01, password, hash=False, b64=False, salt=None):
    if salt and not isinstance(salt, bytes):
        salt = salt.encode()
    if not isinstance(password, bytes):
        password = password.encode()

    password = password.decode()
    # password = password.lower()
    # password = password.replace(" ", '').replace("'", '').replace('-', '').replace(',', '').replace('.', '').replace('!', '')
    password = password.encode()

    if b64:
        password = base64.b64encode(password)

    if hash:
        t = hashlib.md5()
        if salt:
            t.update(salt)
        t.update(password)
        password = t.hexdigest()
    password = password.strip()
    cmd = [r'/Users/jasonbrackman/Downloads/unar1.10.1/unar',
           '-f',
           '-p', password,
           input_01]

    if os.name == 'nt':
        cmd = [r'C:\Program Files\7-Zip\7z.exe',    # program
               'x',                                 # extract
               '-p{}'.format(password),             # password
               '-y',                                # auto-yes to everything
               input_01]                            # zipped file

    proc = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    stderr, stdout = proc.communicate()
    # print(stderr.decode())
    # print(stdout.decode())
    return stdout + stderr, password


def brute_force_7z(zip_file, items):
    for index, password in enumerate(items):
        result, mangled = unzip(zip_file, password, hash=False, b64=False, salt=None)
        response = 'FAIL' if b'fail' in result or b'Wrong password?' in result else 'PASS'
        if index % 500 == 0:
            print('Completed so far: {}, and crunching on {}'.format(index, password))
        if 'PASS' in response:
            print('[{}] attempt with: {}'.format(response, mangled))
            return mangled
    return


def get_pixel_data(path):
    img = Image.open(path)
    width, height = img.size
    pixels = []
    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            print(pixel, col, row)
            pixels.append(pixel)

    return pixels


def get_pixel_block(path, block=(0, 0)):
    img = Image.open(path)
    width = block[0] * 8
    height = block[1] * 8

    pixels = []
    for row in range(height, height+8):
        for col in range(width, width+8):
            pixel = img.getpixel((col, row))
            #print(pixel, end='')
            pixels.append(pixel)
        #print()

    return pixels


def investigative_stuff():
    image_file = r'./challenges/Challenge 8/generated_content/0520f85b16f1baa6ca418/mrroboto.png'
    # get_pixel_data(image_file)
    letters = list()
    for row in range(0, 11):
        for col in range(10, -1, -1):
            results = get_pixel_block(image_file, block=(row, col))
            total = sum(results[0]) + sum(results[9]) - sum(results[19])
            result = 'red' if total == 295 else 'white' if total == 765 else chr(total)
            print("Block ({:02}, {:02}):".format(row, col), result, total, results[0], results[9], results[19])
            letters.append(result)
            # print(chr(sum(results[0]) + sum(results[9]) - sum(results[18])), end='')
        print()
    print('\nLength: {}'.format(len(letters)), letters)

    items = collections.Counter(letters)
    print(items)
    guess = 'h a c k f u t h e ' \
            'o d d b a l l ' \
            'c o l o u r a t a l l ' \
            'a n a m e n d m e n t ' \
            'c o l o u r i n s i d e t h e l i n e s'.split()
    items_02 = collections.Counter(guess)
    print(items_02)

    for index, item in enumerate((letters)):
        letter = item.replace('white', '*').replace('red', '@')
        if index != 0 and index % 11 == 0:
            print()
        print(letter, '', end='')

        # 00#  hackfuthe
        # 01# c cbcsooe t
        # 02# hc oddba od
        # 03# san ste mlt
        # 04# elre b aiop
        # 05# olshelbnoue
        # 06# sert a aorl
        # 07# ydy wii lig
        # 08# yc ouldi nb
        # 09# e tondmen o
        # 10# lour at all

        # 00#  ---------
        # 01# - -b----- t    bt                    star, be, ly, sh, hot, so, to
        # 02# -- ----- --                          or, host, white, rgb
        # 03# s-- --- --t    st         b*      pose, bore, pore, test, by,
        # 04# e-re b -i-p    erebip     ee*       but, best, rap, yes, stop, rise, star
        # 05# o-----b-oue    oboue      ooo        yet, stay, sorry, pray, pirate, cats
        # 06# s--- - aor-    saor       r*         beer, rest, be, store, rosy, rose, bore,
        # 07# y-y --- ---    yy         s*
        # 08# y- ----- -b    yb         yy*       rose, yes, boy, o, yore,

        # hackfuthe
        # twilight
        # colourin
        # oddballs
        # chooseto
        # could
        # anamendment
        # insidethelines
        # called
        # colouratall


    # twilight star could be
    # an amendment at twilight could stop

    # hackfu the oddballs choose
    # to colour inside the lines
    # but i pray an amendment at
    # twilight could stop
    # (rose, yes, boy, o)
    # best be
    # called colour at all

    # hackfu the oddballs choose
    # to colour inside the lines


    # ---------
    # hackfu the oddballs choose to colour inside the lines
    # i pray an amendment twilight could best be called colour at all
    # ooo l -t bb
    # --------
    # hackfu the oddballs choose to colour inside the lines
    # i pray an amendment twilight could be called colour at all
    # ooo, l, e, bbb, s, -i
    # --------
    # hackfu the oddballs choose to colour inside the lines
    # pray an amendment could be called colour at all
    # ooo, t, i, r, yy, w, g

    # toy, grit, it, or, got, writ, wort, try, root

    # ----------
    # hackfu these oddballs choose to colour inside the lines
    # pray an amendment
    # could it be called colour at all'
    # ooo, t, bbb, i, r, yy, w, g
    #
    # to, it, bow, go, got, rot, boy, bot, rig, wig, wry, rib, rgb,

    # ----------
    # hackfu these oddballs choose to colour inside the lines
    # i pray
    # an amendment to rgb could it be called colour at all
    #
    # oo, bb, yy, w # i , p, r , a , y
    # boy, it, booty, boot, wit, boo, toy, too, by, bit,
    # wait, write,

    # to get twilight back I would need to get twilight: twi _ _ _ _ _
    # remove rgb -- for the g # twi_ _ g _
    #

    # -------
    # hackfu these oddballs choose to colour inside the lines
    # i pray an amendment to rgb
    # could it be called colour at all
    #
    # w, bb, yy, oo
    # boy, bow, by, yoyo

    # i worry an amendement to

    maybe = 'hackfutheoddballschoosetocolourinsidethelinesbutiprayanamendmentattwilightcouldstopbestbecalledcolouratall'
    maybe = 'hackfutheseoddballschoosetocolourinsidethelinesiprayanamendmenttorgbcoulditbecalledcolouratall'
    actual = ''.join(letters).replace('red', '').replace('white', '')
    print()
    print(maybe[9:])
    print(actual[9:])
    print('M: ', collections.Counter(maybe[9:]))
    print('A: ', collections.Counter(actual[9:]))


def decrypt_message(passkey):
    infile_ = os.path.abspath('./Challenges/Challenge 8/solution.txt.enc')
    outfile_ = os.path.abspath('./Challenges/Challenge 8/generated_content/solution.txt')

    challenge_00.decrypt_openssl(infile=infile_, outfile=outfile_, passphrase=passkey)

if __name__ == "__main__":
    input_01 = os.path.abspath('./challenges/challenge 8/generated_content/password.7z')
    items = ['domo', 'domoarigato', 'domoarigatomr', 'domoarigatomrroboto']
    password = brute_force_7z(input_01, items)

    key = r'hackfu the colour in the oddbands on the meteor was impossible to describe only by analogy could it be ' \
          r'called colour at all'.replace(' ', '')
    print(key)
    decrypt_message(key)

