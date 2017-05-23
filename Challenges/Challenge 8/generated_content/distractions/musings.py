# coding=utf-8
# Copyright 2017 SEGA Corporation, Developed by Relic Entertainment
#
# Name:     
# Purpose:  
# 
# Creation Date: 5/3/2017
#
# --------------------------------------------------------------------------------------
import base64
import os

# import binwalk
#
# def binwalk_test():
#     items = os.listdir('..')
#     for item in items:
#         print(item)
#         for module in binwalk.scan('..\{}'.format(item), signature=True):
#             print('{} Results:'.format(module))
#             for result in module.results:
#                 print(result.file.name, result.offset, result.description)
import string

def carve_binary():
    stuff = []
    with open('../047b704a141707ec15a8171ab1d37dbd.wav', 'rb') as handle:
        for line in handle:
            for letter in line:
                if 60 < letter < 123:
                    stuff.append(chr(letter))

    all = ''.join([item for index, item in enumerate(stuff) if index % 2])
    all = all.replace("==", '==\n')
    #all = all.split("\n")
    for index in range(0, len(all), 80):
        print(all[index:index+80])


    # for item in all:
    #     try:
    #         print(base64.b64decode(item))
    #     except Exception as e:
    #         pass

def carve_binary2():
    stuff = []
    with open('../047b704a141707ec15a8171ab1d37dbd.wav', 'rb') as handle:
        for line in handle:
            for letter in line:
                stuff.append(letter)

    mask = 0b1111111
    bits = 7
    for index in range(44, len(stuff), bits):
        goods = [i for i in stuff[index:index+bits]]
        new_word = [bin(mask & i)[-1] for i in goods]
        new_letter = int(''.join(new_word), 2)
        print(chr(new_letter), end='')

    # for item in stuff:
    #     print(bin(mask & item))
    # # all = ''.join(stuff)


def carve_binary3(stuff, start_byte=0, bits=7, mask=0b1111111):
    # clipped = [item[-1] for item in stuff[39004:]]
    end_byte = len(stuff)

    end_byte = start_byte + 500
    collection = []
    for index in range(start_byte, end_byte, bits):
        new_word = [bin(mask & int(i, 2))[-1] for i in stuff[index:index+bits]]
        new_letter = int(''.join(new_word), 2)
        test_character = chr(new_letter)
        if test_character in string.printable:
            collection.append(test_character)

    if len(collection) >= 30:
        # print("Could Be The One at start_byte: {} bit:{}".format(start_byte, bits))
        print(start_byte, len(collection), ''.join(collection[0:80]))


    # print(len(collection), start_byte,  ''.join(collection[0:80]))


def get_binary_representation():
    stuff = []
    with open('../047b704a141707ec15a8171ab1d37dbd.wav', 'rb') as handle:
        for line in handle:
            for letter in line:
                stuff.append(bin(letter))

    return stuff


def domo_t():
    x = "domoarigatomrroboto"
    y = {'d': 4,
         'o': 15,
         'm': 13,
         'a': 1,
         'r': 18,
         'i': 9,
         'g': 7,
         't': 20,
         'b': 2}
    for item in x:
            print(y[item], end='')

if __name__ == "__main__":
    # binwalk_test()
    stuff = get_binary_representation()
    for index in range(32000, 42320):
        #print("STARTING NEW ROUND: {}".format(index))
        carve_binary3(stuff, start_byte=index)



