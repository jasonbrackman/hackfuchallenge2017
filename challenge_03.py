# downloaded Sonic Visualizer - nothing special initially in the spectrum analyzer.
# Its possible that the upper range is actually morse code?
# there is a narrow band where content is repeated...
# small dots of data appear in sequences of blocks of 7.  There are 48 blocks. (maybe 48 letters?)

import os
import wave
import collections
import challenge_00

file = os.path.abspath('./Challenge 3/test.wav')

def print_lowest_bits(file):
    with wave.open(file, 'rb') as handle:
        data = handle.readframes(1024)
        # stuff = [format(item, '#010b')[-1] for item in data]  # get LSB
        stuff = [str(item & 0b00000001) for item in data]
        collector = []

    for index in range(0, len(stuff), 8):
        num = ''.join(stuff[index:index + 8])
        collector.append(chr(int(num, 2)))
    print(''.join(collector))
    print(len(collector))

def wav_example(path):
    with wave.open(path, 'rb') as w:
        amplitudes = list()

        for index in range(w.getnframes()):
            frame = w.readframes(index)
            for item in range(len(frame)):
                amplitudes.append(frame[item])

        print(max(amplitudes))
        print(min(amplitudes))

        count = collections.Counter(amplitudes)
        for item in count.items():
            print(item)

def decrypt_message(passkey):
    infile_ = os.path.abspath('./Challenge 3/solution.txt.enc')
    outfile_ = os.path.abspath('./Challenge 3/generated_content/solution.txt')

    challenge_00.decrypt_openssl(infile=infile_, outfile=outfile_, passphrase=passkey)

if __name__ == '__main__':
    passkey = 'hackfuandallyourtrickshellbearandneverseemtomind'
    decrypt_message(passkey.lower())

    # print_lowest_bits(file)
    # wav_example(file)

    # with wave.open(file) as handle:
    #     for item in dir(handle):
    #         print(item)
    #     print(handle.tell())
    #     print(handle.getcompname())
    #     print(handle.getcomptype())
    #     print(handle.getfp())
    #     print(handle.getframerate())
    #     print(handle.getparams())
    #     print(handle.getsampwidth())
    #     print(handle.getnchannels())
    #     print(handle.getnframes())
    #     print(handle.getmarkers())
    #     print(2534400 / 8)
