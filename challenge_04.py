import collections
import os

import challenge_00


def decrypt_message(passkey):
    infile_ = os.path.abspath('./Challenges/Challenge 4/solution.txt.enc')
    outfile_ = os.path.abspath('./Challenges/Challenge 4/generated_content/solution.txt')

    challenge_00.decrypt_openssl(infile=infile_, outfile=outfile_, passphrase=passkey)


with open('./Challenges/challenge 4/key', 'rt') as handle:
    key = handle.read()

with open('./Challenges/challenge 4/pass', 'rt') as handle:
    pass_ = handle.read()

print(len(pass_), pass_)
print(len(key), key)
for item in ['MQ', 'IM', '52', 'E', 'EIML', 'IML', '52/IML', 'AL', 'IMLEXQ', 'ML', 'KAL', 'ZMI', 'EIQILSLKI','MQE',
             '3KI5', '/43II4L/PQPC/']:
    print('{}: {}'.format(item, key.count('{}'.format('/' + item + '/'))))

items = key.split('/')
print(len(items))
print([itm for itm in items if '5' in itm])
count = collections.Counter(key)
print(len(count))
print(count.most_common(10))

# etaoinshrdlcumwfg
mappings = {'/': ' ',
            'L': 'e',
            'I': 't',
            'Q': 'a',
            '5': 'o',
            '3': 'i',
            'K': 'n',
            'M': 'h',
            '1': 'c',
            'O': 'k',
            '2': 'f',
            '7': 'u',
            'E': 's',
            'S': 'm',
            '4': 'l',
            'A': 'd',
            '6': 'r',
            'Z': 'g',
            'X': 'p',
            'J': 'w',
            'C': 'y',
            'P': 'b',
            'D': 'v'
}

results = list()
for index in range(0, len(pass_)):
    result = pass_[index:index + 1]
    results.append(mappings.get(result, result))

passkey = ''.join(results)
print('passkey: ', passkey)
decrypt_message(passkey)

# for index in range(len(key)):
#     result = key[index:index + 1]
#     print(mappings.get(result, result), end='')