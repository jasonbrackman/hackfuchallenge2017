# https://www.reddit.com/r/codes/comments/62rl1a/good_luck/
import collections

import math

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


if __name__ == "__main__":
    reddit_thing()
    #get_standard_deviation()
