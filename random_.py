# https://www.reddit.com/r/codes/comments/62rl1a/good_luck/
import hashlib
import collections

import math
import os

import subprocess

code = '1171429351229372322293627322717233535293117293519193315111334393725393312272931193334373229393722243'
letters = [code[index:index+2] for index in range(0, len(code), 2)]
letter_count = collections.Counter(letters)

letter_frequency = {letter: score/len(letters) * 100 for letter, score in letter_count.items()}
letter_frequency = reversed(sorted(letter_frequency.items(), key=lambda x: x[1]))

def reddit_thing():
    test = ' etaoinshrdlcumwfg'
    mapping_auto = {letter[0]: new_letter for letter, new_letter in zip(letter_frequency, test)}

    mapping_test = {'93': ' ', '11': 'a', '72': 't', '22': 'e', '53': 'o',
                    '32': 'h', '52': 'n', '31': 'g', '33': 'i', '51': 'm',
                    '43': 'l', '71': 's', '42': 'k', '62': 'q', '73': 'u',
                    '91': 'y'}

    auto_results = []
    test_results = []
    for index in range(0, len(code), 2):
        result = code[index:index+2]
        auto_results.append(mapping_auto.get(result, result))
        test_results.append(mapping_test.get(result, result))
    print(''.join(auto_results))
    print(''.join(test_results))


def get_average(items):
    return sum(items) / len(items)


def get_standard_deviation():
    orders = [3, 5, 7, 8, 5, 25, 8, 4]
    average_orders = get_average(orders)
    differences = [pow(abs(item - average_orders), 2) for item in orders]

    # this is the variance: a statistics concept
    average_differences = get_average(differences)

    standard_deviation = math.sqrt(average_differences)

    for order in orders:
        print(order - average_orders - standard_deviation > 0)

    return standard_deviation

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
                 'pass3', r'pass3/password', r'pass3\password', 'password', 'buzz',
                 'believe', '2700', '1969', '386',
                 'Fact', 'Fiction', 'fact', 'fiction', 'FACT', 'FICTION',
                 'lies', 'Lies', 'LIES',
                 'Fake', 'FAKE', 'fake', 'u4j']

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
        print(stderr.decode())
        # print(password)
        response = 'FAIL' if b'fail' in stderr else 'PASS'
        if 'PASS' in response:
            print(index, '[{}] attempt with: {}'.format(response, password))
            break

def unzip(input_01, password):
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
    return stdout

def test_hashes():
    files = ['words.txt', 'words2.txt', 'words3.txt']
    for f in files:
        with open(r'.\challenges\challenge 8\generated_content\{}'.format(f), 'rt') as handle:
            words = handle.readlines()
            for word in words:
                result = hashlib.md5(word.encode()).hexdigest()

                unknown_01 = '286755fad04869ca523320acce0dc6a4'
                if result == unknown_01:
                    print("[MATCH] {} = {}".format(word.strip(), unknown_01))

                unknown_02 = '047b704a141707ec15a8171ab1d37dbd'
                if result == unknown_02:
                    print("[MATCH] {} = {}".format(word.strip(), unknown_02))

    print(hashlib.md5('domoarigatomrroboto\n'.encode()).hexdigest())


if __name__ == "__main__":
    # reddit_thing()
    # get_standard_deviation()

    items = ['cypher', 'decipher', 'question', 'password', 'domoarigatomrroboto',
             'kilroy', 'kilroywashere', 'roboto', 'escape', 'clue',
             'himitsuwoshiritai', 'mataahoohimade', 'thankyouverymuchmrroboto',
             'imkilroykilroykilroykilroy', 'hellomoto']

    input_01 = os.path.abspath('./challenges/challenge 8/generated_content/password.7z')

    for f in ['words.txt', 'words2.txt', 'words3.txt']:
        with open(r'.\challenges\challenge 8\generated_content\{}'.format(f), 'rt') as items:

            for password in items:
                password = hashlib.md5(password.encode()).hexdigest()
                result = unzip(input_01, password)
                response = 'FAIL' if b'fail' in result or b'Wrong password?' in result else 'PASS'
                if 'PASS' in response:
                    print('[{}] attempt with: {}'.format(response, password))


