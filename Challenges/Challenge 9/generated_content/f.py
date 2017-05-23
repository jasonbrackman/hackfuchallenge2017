# thanks to some decompile: http://www.javadecompilers.com/apk

import re


# /* renamed from: hackfu.mwr.com.masterclass.f */
class C0722f(object):

    def m5053a(self, key):

        ints = self.m5050a(key)
        new_string = self.m5049a(ints)
        jumble_letters = self.m5051b(new_string)

        # Returns a string
        return self.m5052c(jumble_letters)

    def m5050a(self, str):
        # get_ints_from_key
        values = [int(item.strip()) for item in str.split(",")]

        # Returns a list of ints
        return values


    def m5049a(self, list):

        hashMap = {index: chr(index) for index in range(0, 256)}

        # str = "" + ((char) ((Integer) list.remove(0)).intValue());
        str = chr(int(list.pop(0)))

        stringBuffer = [str]

        i2 = 256
        str2 = str
        for intvalue in list:
            i = int(intvalue)

            if i in hashMap:
                str = hashMap[i]
            elif i == i2:
                str = str2 + str2 # str2.charAt(0)
            else:
                str = ""

            stringBuffer.append(str)

            i3 = i2 + 1
            hashMap[int(i2)] = str2 + str #str.charAt(0));
            str2 = str
            i2 = i3

        return ''.join(stringBuffer)


    def m5051b(self, str):
        stringBuilder = list()
        for c in str:
            c2 = ord(c)
            if c2 >= ord('A') and c2 <= ord('Z'):
                c2 = c2 + 13
                if c2 > ord('Z'):
                    c2 = chr(c2 - 26)

            elif c2 >= ord('a') and c2 <= ord('z'):
                c2 = c2 + 13
                if c2 > ord('z'):
                    c2 = chr(c2 - 26)

            elif c2 >= ord('0') and c2 <= ord('9'):
                c2 = c2 + 5
                if c2 > ord('9'):
                    c2 = chr(c2 - 10)
            if isinstance(c2, int):
                c2 = chr(c2)
            stringBuilder.append(c2)

        return ''.join(stringBuilder)


    def m5052c(self, str):
        print(str)
        stringBuilder = list()
        matcher = re.compile("[0-9]+|[a-zA-Z]").findall(str)
        for match in matcher:

            if match.isdigit() and int(match) == 1:
                pass
            else:
                stringBuilder.append(match)

            # print("asdf: ", match.isdigit())
            # parseInt = 1 if match.isdigit() else ord(match)
            #
            # i = parseInt - 1
            # if parseInt != 0:
            #     stringBuilder.append(match)
            #     # parseInt = i

            # matcher.find();
            # while True:
            #     i = parseInt - 1
            #     if parseInt != 0:
            #         stringBuilder.append(match)
            #         parseInt = i

        return ''.join(stringBuilder)

if __name__ == "__main__":
    decrypt = C0722f()

    new_key = list()
    with open('soup.chef', 'rt') as handle:
        for line in handle:
            test = line[0:3].strip()
            if test.isdigit():
                new_key.append(test)

    keys = ["54, 99, 54, 98, 54, 122, 54, 114, 54, 116, 54, 101, 54, 110, 54, 97, 268, 54, 103, 262, 54, 102, 55, 263, 113, 276"]

    keys.append(', '.join(new_key))
    for key in keys:
        print(key)
        print(decrypt.m5053a(key))
        result = ''.join(chr(int(item.strip())) for item in key.split(','))
        print(''.join(reversed(result)))
