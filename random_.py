# https://www.reddit.com/r/codes/comments/62rl1a/good_luck/
import hashlib
import collections
from itertools import permutations
import math
import os
import base64
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
                 'Fake', 'FAKE', 'fake', 'u4j'
                 ]

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

def test_hashes():
    files = ['words.txt', 'words2.txt', 'words3.txt', 'crackstation.txt']
    for f in files:
        filepath = os.path.abspath(r'./challenges/challenge 8/generated_content/{}'.format(f))
        with open(filepath, 'rb') as handle:

            for word in handle:

                result = hashlib.md5(word).hexdigest()

                unknown_01 = '286755fad04869ca523320acce0dc6a4'  # password
                if result == unknown_01:
                    print("[MATCH] {} = {}".format(word.strip(), unknown_01))

                unknown_02 = '047b704a141707ec15a8171ab1d37dbd'  # hellomoto
                if result == unknown_02:
                    print("[MATCH] {} = {}".format(word.strip(), unknown_02))

                unknown_03 = 'e85150c59040bbfe9b14ee0f5fa9e2cf'  #
                if result == unknown_03:
                    print("[MATCH] {} = {}".format(word.strip(), unknown_03))

    print(hashlib.md5('domoarigatomrroboto\n'.encode()).hexdigest())


def get_items(files):
    for f in files:
        fullpath = os.path.abspath(r'./challenges/challenge 8/generated_content/{}'.format(f))

        with open(fullpath, 'rt') as handle:
            for item in handle:
                yield item.strip()


if __name__ == "__main__":
    # reddit_thing()
    # #get_standard_deviation()

    items = [# '1983', #'cypher', 'decipher', 'question',
             # 'domoarigatomrroboto', 'hellomoto', 'password',
             # 'kilroy', 'kilroywashere', 'roboto', 'escape', 'clue',
             # 'himitsuwoshiritai', 'mataahoohimade', 'thankyouverymuchmrroboto',
             # 'imkilroykilroykilroykilroy', 'android', 'mrroboto', 'modren',
             # "Domo arigato misuta Robotto",
             # "Mata au hi made",
             # "Domo arigato misuta Robotto",
             # "Himitsu wo shiritai",
             # "Domoarigatomisuta RobottoMata au hi madeDomo arigato misuta RobottoHimitsuwoshiritai",
             # "You're wondering who I am-machine or mannequin",
             # "With parts made in Japan, I am the modren man",
             # "I've got a secret I've been hiding under my skin",
             # "My heart is human, my blood is boiling, my brain I.B.M.",
             # "So if you see me acting strangely, don't be surprised",
             # "I'm just a man who needed someone, and somewhere to hide",
             # "To keep me alive, just keep me alive",
             # "Somewhere to hide to keep me alive",
             # "I'm not a robot without emotions, I'm not what you see",
             # "I've come to help you with your problems, so we can be free",
             # "I'm not a hero, I'm not a savior, forget what you know",
             # "I'm just a man whose circumstances went beyond his control",
             # "Beyond my control, we all need control",
             # "I need control, we all need control",
             #
             # "I am the modren man, who hides behind a mask",
             # "So no one else can see my true identity",
             #
             # "Domo arigato, Mr. Roboto, domo, domo",
             # "Domo arigato, Mr. Roboto",
             #
             # "Thank you very much, Mr. Roboto",
             # "For doing the jobs nobody wants to",
             # "And thank you very much, Mr. Roboto",
             # "For helping me escape to where I needed to",
             # "Thank you, thank you, thank you",
             # "I want to thank you, please, thank you, oh yeah",
             #
             # "The problem's plain to see, too much technology",
             # "Machines to save our lives. Machines dehumanize.",
             #
             # "The time has come at last",
             # "To throw away this mask",
             # "Now everyone can see",
             '54e7ab81f64f4c3e398951be124bc27b',
             '2fe5eea0ec270f6dad45fc8d99d0cf90',
             'bd66afb1e9da96723ffecf62cdae6f60',
             'ec1dad85eb391fdaaa3b47e721e7b9f1',
             '426133c4d7ef340fbe0da49c9cadbdc5',
             'bc2ebf462409f54173dc1cdecbabe166',
             '6dbcdf333c16781d634a9dc6a1623370',
             '1d330a738dbc1cd112e023cb58e52460',
             '80eebf28cbc124ff143425ad72941046',
             '92adf58c7edce1f212c74dc51aa7cfd5',
             '4141ee79e08eb2727fd0d779c9f0a376',

             # "My true identity", 'Domo Arigato Moto Roboto',
             # "I'm Kilroy! Kilroy! Kilroy! Kilroy!", 'Robert Orin Charles Kilroy',
             # 'styx', 'Dōitashimashite',
             # '1234', 'paradise theatre', 'paradise theater', 'backmasking', 'snowblind', 'domo',
             # 'rock', 'rockcode', 'nomorerock', 'caughtintheact', 'styxcaughtintheact',
             # 'themajorityformusicalmorality', 'mmm', 'kwh', 'motodomoboto', 'domomoto', 'motodomo',
             # 'rightous', 'paradise', 'damr', 'username', '', 'kilroykilroykilroy', 'yourwelcome',
             # 'Mr.Roboto', 'Kilroyishere', 'Jonathan Chance', 'Lt.Vanish', 'Col.Hyde', 'Dr.Righteous',
             # '646F6D6F6172696761746F6D72726F626F746F',  # domoarigatomrrobot in hex
             # '100111109111971141051039711611110911411411198111116111', #domoarigatomrrobot in ordinals
             # '2058', # domoarigato as ordinal added together.
             # '100000001010', # 2058 in binary
             # '1100100110111111011011101111110000111100101101001110011111000011110100110111111011011110010111001011011111100010110111111101001101111', #domo.. in binary

             'jason'

    ]
    input_01 = os.path.abspath('./challenges/challenge 8/generated_content/password.7z')

    #moto
    #domo
    #boto

    files = ['rockyou.txt'] # 'words.txt', 'words2.txt', 'words3.txt']
    # files = ['crackstation.txt']
    # items = get_items(files)
    #items = (str(x) for x in range(1_000_000_000_000_000_000, 2_000_000_000_000_000_000))

    items = [''.join(p) for p in permutations(['domo', 'arigato'])]
    # items = set(items)
    print(len(items))

    for index, password in enumerate(items):
        result, mangled = unzip(input_01, password, hash=False, b64=False, salt=None)
        response = 'FAIL' if b'fail' in result or b'Wrong password?' in result else 'PASS'
        if index % 500 == 0:
            print('Completed so far: {}, and crunching on {}'.format(index, password))
        if 'PASS' in response:
            print('[{}] attempt with: {}'.format(response, mangled))
            break

    # result = 0
    # x = 'domoarigatomrroboto'
    # for item in x:
    #     result += ord(item)
    # print(result)
    #
    # print('\n'.join(format(ord(s), 'b') for s in x))

