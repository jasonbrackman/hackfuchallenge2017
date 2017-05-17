import binascii
import wave

import struct
import collections

def pprint_negative_positive_as_bits(raw_data):
    collection = []
    for item in raw_data:
        bit_id = '1' if item > 0 else '0'
        collection.append(bit_id)

    _group_and_print(collection, bits=7)


def pprint_7bit_lsb(raw_data):
    collection = []
    for item in raw_data:
        collection.append(bin(item)[-1])
    collection = collection[collection.index('1') - 0: -1]  # remove the leading zeroes

    _group_and_print(collection, bits=7)


def pprint_16bit_lsb(raw_data):
    collection = []
    for item in raw_data:
        collection.append(bin(item)[-1])
    collection = collection[collection.index('1') - 0: -1]  # remove the leading zeroes
    _group_and_print(collection, bits=16)


def _group_and_print(collection, bits):
    for index in range(0, len(collection), bits):
        current = collection[index: index + bits]
        current = ''.join(current)
        current = int(current, 2)
        print(chr(current), end='')


with wave.open('../047b704a141707ec15a8171ab1d37dbd.wav', 'rb') as sound:
    num_channels = sound.getnchannels()
    sample_width = sound.getsampwidth()
    num_frames = sound.getnframes()
    comp_type = sound.getcomptype()
    num_samples = num_frames * num_channels
    fmt = "{}h".format(num_samples)
    # The least possible value for a sample in the sound file
    min_sample = -(1 << 15)

    print('MinSample: ', min_sample)
    print('fmt: ', fmt)
    print('channels: ', num_channels)
    print('sample_width: ', sample_width)
    print('num_frames: ', num_frames)
    print('num_samples: ', num_samples)
    print('comp_type: ', comp_type)

    # Put all the samples from the sound file into a list
    raw_data = list(struct.unpack(fmt, sound.readframes(num_frames)))

    # split the stereo into left and right
    l = [r for index, r in enumerate(raw_data) if index % 2 == 0]
    r = [r for index, r in enumerate(raw_data) if index % 2 == 1]

    # Left & Right channel info should be equal for this challenge
    assert l == r
    # print(collections.Counter(r).most_common(5))

    pprint_7bit_lsb(r)
    # pprint_16bit_lsb(r)
    # pprint_negative_positive_as_bits(r)


    # for item in raw_data:
    #     if item > 0:
    #         print(hex(item), end='')
    # for item in raw_data:
    #     if item > 0:
    #         print(chr(item), end='')
        # print(chr(item), end='')

