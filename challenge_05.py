# Stuff found inside the .img file:
# lost+found, my-files, my-scripts
# /tmp/backups
#   encrypted.py (Found)

#   audio0.mp3 (Likely)
#   --> Angle Arithmetic (song)
#   --> Acutes (artist)
#   --> Alphabet (Album)
#   file0.ps  (Found)
#   arr.txt.enc (Likely)
#   gee.txt.enc (Likely)
#   bee.txt.enc (Likely)
import os

import challenge_00


def decrypt_message(passkey):
    infile_ = os.path.abspath('./Challenges/Challenge 5/solution.txt.enc')
    outfile_ = os.path.abspath('./Challenges/Challenge 5/generated_content/solution.txt')

    challenge_00.decrypt_openssl(infile=infile_, outfile=outfile_, passphrase=passkey)

if __name__ == '__main__':
    key = 'hackfuihaveseenthenightgauntsintheirhauntsandtheoldonesatthebottomofthesea'
    decrypt_message(key)