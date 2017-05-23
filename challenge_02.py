# http://epublications.regis.edu/cgi/viewcontent.cgi?article=1511&context=theses
# 1. pulled out all the middle pieces
# 2. realized the cube likely has to be solved?
# 3. https://rubiks-cube-solver.com
# 4. Sort of stuck - maybe the center cubie is not the colour of the square -- it can be any of them?
#    -
# 5. Info says the document was created by: Roger Tavares
#
#
import itertools
import collections
import os

import challenge_00

colours = {'r': {('1', '1'): 'G',
                 ('1', '2'): 'M',
                 ('1', '3'): 'a',
                 ('2', '1'): 'm',
                 ('2', '2'): 'N',
                 ('2', '3'): 'h',
                 ('3', '1'): 'y',
                 ('3', '2'): 'f',
                 ('3', '3'): 'r'},
           'b': {('1', '1'): 'L',
                 ('1', '2'): 'X',
                 ('1', '3'): 'U',
                 ('2', '1'): 'z',
                 ('2', '2'): 'n',
                 ('2', '3'): 'F',
                 ('3', '1'): 'c',
                 ('3', '2'): 'H',
                 ('3', '3'): 'i'},
           'y': {('1', '1'): 'P',
                 ('1', '2'): 'B',
                 ('1', '3'): 'S',
                 ('2', '1'): 'v',
                 ('2', '2'): 'W',
                 ('2', '3'): 'O',
                 ('3', '1'): 'J',
                 ('3', '2'): 'B',
                 ('3', '3'): 'j'},
           'g': {('1', '1'): 'R',
                 ('1', '2'): 'g',
                 ('1', '3'): 'u',
                 ('2', '1'): 'k',
                 ('2', '2'): 'w',
                 ('2', '3'): 'D',
                 ('3', '1'): 'I',
                 ('3', '2'): 'x',
                 ('3', '3'): '_'},
           'w': {('1', '1'): 'p',
                 ('1', '2'): 't',
                 ('1', '3'): 's',
                 ('2', '1'): 'K',
                 ('2', '2'): 'E',
                 ('2', '3'): 'Q',
                 ('3', '1'): 'g',
                 ('3', '2'): 'b',
                 ('3', '3'): 'g'},
           'o': {('1', '1'): 'l',
                 ('1', '2'): 'Z',
                 ('1', '3'): 'A',
                 ('2', '1'): 'V',
                 ('2', '2'): 'e',
                 ('2', '3'): 'o',
                 ('3', '1'): 'u',
                 ('3', '2'): 'T',
                 ('3', '3'): 'Y'}
           }

custom = {'b': {('3', '2'): 'h',
                ('3', '1'): 'c',
                ('2', '3'): 'f'},
          'r': {('1', '3'): 'a'},
          'g': {('2', '1'): 'k'},
          'o': {('3', '1'): 'u'}}


colours_01 = {'r': {('1', '1'): 'J',
                    ('1', '2'): 'K',
                    ('1', '3'): 'L',
                    ('2', '1'): 'M',
                    ('2', '2'): 'N',
                    ('2', '3'): 'O',
                    ('3', '1'): 'P',
                    ('3', '2'): 'Q',
                    ('3', '3'): 'R'},
              'b': {('1', '1'): 'j',
                    ('1', '2'): 'k',
                    ('1', '3'): 'l',
                    ('2', '1'): 'm',
                    ('2', '2'): 'n',
                    ('2', '3'): 'o',
                    ('3', '1'): 'p',
                    ('3', '2'): 'q',
                    ('3', '3'): 'r'},
              'y': {('1', '1'): 'P',
                 ('1', '2'): 'O',
                 ('1', '3'): 'S',
                 ('2', '1'): 'B',
                 ('2', '2'): 'W',
                 ('2', '3'): 'd',
                 ('3', '1'): 'J',
                 ('3', '2'): 'v',
                 ('3', '3'): 'j'},
              'g': {('1', '1'): 'U',
                 ('1', '2'): 'D',
                 ('1', '3'): '_',
                 ('2', '1'): 'q',
                 ('2', '2'): 'w',
                 ('2', '3'): 'x',
                 ('3', '1'): 'I',
                 ('3', '2'): 'k',
                 ('3', '3'): 'R'},
              'w': {('1', '1'): 's',
                 ('1', '2'): 'b',
                 ('1', '3'): 'g',
                 ('2', '1'): 't',
                 ('2', '2'): 'E',
                 ('2', '3'): 'Q',
                 ('3', '1'): 'p',
                 ('3', '2'): 'k',
                 ('3', '3'): '.'},
              'o': {('1', '1'): 'A',
                 ('1', '2'): 'o',
                 ('1', '3'): 'Y',
                 ('2', '1'): 'N',
                 ('2', '2'): 'e',
                 ('2', '3'): 'T',
                 ('3', '1'): 'l',
                 ('3', '2'): 'V',
                 ('3', '3'): 'u'}
           }


def cube_decryptor(text):
    # hardcoded split - should be based off of the colours passed in...
    clr = text[0:75]
    row = text[75:150]
    col = text[150:]

    decrypted = ''.join(collect_letters(clr, col, row, colours))

    # debug
    # print(''.join(clr))
    # print(''.join(row))
    # print(''.join(col))
    # print(decrypted)

    return decrypted


def xor_text(line, xor):
    results = [chr(ord(letter) ^ xor) for letter in line]
    print(''.join(results))


def substitute_text(line_01):
    for x in range(54):
        new_line = [get_next_character(letter, x) for letter in line_01]
        line_03 = ''.join(new_line)
        print(line_03)


def get_next_character(pattern, distance):
    text = 'abcdefghijklmnopqrstuvwyxz.ABCDEFGHIJKLMNOPQRSTUVWXYZ_'
    val = text.index(pattern)
    text = itertools.cycle(text)
    for index, letter in enumerate(text):
        if index == val + distance:
            return letter


def frequency_analysis(text):
    count = collections.Counter(text)
    print(count)


def _compare_row_col_swap_similarities(line_01, line_02):
    for a, b in zip(line_01, line_02):
        if a == b:
            print(a, end='')
        else:
            print(' ', end='')
    print()


def _line_break_attempt(line, at=1):

    results = [line[index:index+at] for index in range(0, len(line), at)]
    for index in range(len(results)):
        if index % 10 == 0:
            print()

        print(' {}'.format(results[index]), end='')

    print('\n', "-" * 10)

    # for index in range(255):
    #     for letter in line_02:
    #         print('{}'.format(chr(ord(letter) ^ index)), end='')
    #     print()


def collect_letters(clr, col, row, colours):
    collection = []
    for item in zip(clr, row, col):
        colour, id = item[0], (item[1], item[2])
        if colour in colours:
            if id in colours[colour]:
                collection.append(colours[colour][id])
    return collection


def decrypt_message(passkey):
    infile_ = os.path.abspath('./Challenges/Challenge 2/solution.txt.enc')
    outfile_ = os.path.abspath('./Challenges/Challenge 2/generated_content/solution.txt')

    challenge_00.decrypt_openssl(infile=infile_, outfile=outfile_, passphrase=passkey)

if __name__ == '__main__':
    encrypted = "brbgboorrooyoobgwrorwrgbwrwoworogoorwrrorwbobgorrooobrowyborobworyrrbwogoor3132233232231232122312133" \
                "2111322222211323222323232233221223221313231232222323113123322213113233231333232232333133123123112332" \
                "2231233223233113332323333"

    passkey = cube_decryptor(encrypted)
    decrypt_message(passkey.lower())
