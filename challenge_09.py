#"sans-serif    key MessageActivity Time remaining: Decryption key &&hackfu.mwr.com.masterclass." \
#       "preferences GGYou need to grant permission for this app to write to external storage. ``Write Externa" \
#       "l Storage Permission has not been granted. You will not be able to export the file. bbWrite " \
#       "External Storage Permission has been granted. You can now export the file. Tap export again. ##" \
#       "Could not create file or directory. !!External storage is not writable. Decrypted message: tt" \
#       "[54, 99, 54, 98, 54, 122, 54, 114, 54, 116, 54, 101, 54, 110, 54, 97, 268, 54, 103, 262, 54, 102, 55, 263, 113, 276" \
#       "] Submit The file already exists. Export successful! 		" \
#       "soup.chef" \
#       " Key is required This key is an invalid length $$This key contains invalid characters This field is required " \
#       "UTF-8 Could not retrieve Key. Could not retrieve Cipher Text. Could not retrieve IV. No time remaining! " \
#       "Time remaining AES/CBC/PKCS5PADDING AES """

# This feels like I need to run the apk file.  Maybe the images that are part of this glob of files are used to generate
# pixels from those locations above to create a new image with info?
import os

import challenge_00

nums = "54, 99, 54, 98, 54, 122, 54, 114, 54, 116, 54, 101, 54, 110, 54, 97, 268, 54, 103, 262, 54, 102, 55, 263, 113, 276".split(',')
numbers = [num.rstrip() for num in nums]
print(' '.join(numbers))
byte_numbers = (87 ^ int(num) for num in numbers)
for item in byte_numbers:
    print(item, end='')
print()
print(''.join(chr(int(num)) for num in numbers))
# print(''.join())
# print(''.join(hex(int(num)) for num in numbers).replace('0x', ''))
def decrypt_message(passkey):
    infile_ = os.path.abspath('./Challenges/Challenge 9/solution.txt.enc')
    outfile_ = os.path.abspath('./Challenges/Challenge 9/generated_content/solution.txt')

    challenge_00.decrypt_openssl(infile=infile_, outfile=outfile_, passphrase=passkey)

if __name__ == "__main__":
    passkey = 'hackfuwhereitlandswesetourscene'
    decrypt_message(passkey)