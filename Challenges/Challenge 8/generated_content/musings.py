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


def carve_binary3(start_byte=44, bits=7, mask=0b1111111):
    stuff = []
    with open('../047b704a141707ec15a8171ab1d37dbd.wav', 'rb') as handle:
        for line in handle:
            for letter in line:
                stuff.append(letter)

    for index in range(start_byte, len(stuff), bits):
        # print(chr(stuff[index]), end='')

        goods = [i for i in stuff[index:index+bits]]
        new_word = [bin(mask & i)[-1] for i in goods]
        new_letter = int(''.join(new_word), 2)
        print(chr(new_letter), end='')


def domo_test():
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
    carve_binary3()



