import binascii
from subprocess import Popen, PIPE

message = b"""U2FsdGVkX18FUHPUzSqob7oVy4r6Pv8O04HICtRY4niPtIzTMWZ6gF726eMb2hTZ
ePA5RruIbsNbvQo060+F374+pRiNsm7qWSV3KxV3+ctC+z41n5DsB8zkHHLCTWs3
k2wqxD786phWwrprxQBfyNoRxmcXzOZoFMWB774/JlVmp9xVTOZ9VjpNNDvRVQcf
cOjwfS2+clzU4O8561ahNrmBpCKJcijKa6k/PeQzHION9wiPDIKLa6faVmloXkYk
TYMO3vGClKqMQHYagDPqPbgoxknsiy82xTZJbnNnbSBePZPoHmw1O/rOSb0kXPcV
7sFkIy9Lv9hlJb826uZdOHi5178R5nACi4Zkxp9X1Ph+GRd0jB31vYWPuGaBuhdw
/Gbe+Pm7BMhp0BuhYkrZstfEOY7n0VJ8NkFAY0l+A3+lBglF1ZG135V6Vw32SWJl
2ecobUth1MNWc/rh2vo+pkfRqPItiKM6feVzk+eYbF9wCfHYd+Jy+EzLuRFloIUq
sA4B7PFyIVOGIL5VLmuDEsN8M+JoImlwdS4nAPgWe1Fj7FDFf8hc+rGFO+uThhZl
a2hwjX9UlHf2OlNtNx7VjhE50MBr9X8u2+0BoJl/W1ftR0kelTmjUJRGOKCoRzZ8
HzL7i6Aut6rjzsPC3Dm6pKl6ekTAHu7Z9NiQzZmwW+n/hmMrWdp7mSdEZ5UvqwNR
rTFXsTv2PcfVck4XKxXtFhcAxhoJYUzlVc2HORaahoa/5P9/VfErQ1KkAPviF41w
ipFh08xer2XB0iLFaVQmhgLsmZF94+UbqYhiQHyEyJKMLHSeydIDrAI7fgypo4kw
cNAyIlrQKW7ksc4ZRFtpetdUAfutj7x/c1sEx1TDoTKR9dtj1s1BHGKsa4z7jH2H
edlgI+FPYqSg0Gc4BbTItKR8x/7C+5Yv2xKWTGMDVBcIW8Ycz/u0H15RnG+e05L8
Xjm0rXdD0LstusCN2nv6kBiYJz5zirwK/7Kyu6H95jX9JsYMtcxBKLBmuTXiaV6N
GPZmcaad4FkKPqCdInM46glU4x8DjoySs/3BluAL+sNkHphEJ9SPy1OwZ0LOWUFH
mxbEh5bdIidLw2HSQLLgWWhLYsfDEL5tRcjtS/Y63efglNwRiolQP4sFEgmPO1PU
TkjEj1WtdqcmwZQIo9InkNAR+lTbdZ/ty4poxckbtqKaIbeXNjdHvLs6H+Yeh02p
QIj3aqlZr/SNAA+5O9cknzzRUfKgdrM7a3IHuR6NaE7RLgzPCcLwuSErhEZKFrta
4FxGJNFVcqQD4Y/Se+QfqtsYhScFVCwyIMiFwEC35vSmsCkKw19AmWiazdzB7a50
jq4bmKj9F5X4HyRhplWV1SgpaotvCW6Me5OGwq6A0Akce021rB6R0tygH2apEHtm
oSaiWfQVHgHLCaZE4dUDTBtns8HvQYHsAEyQigEeli4="""

message = binascii.a2b_base64(message)


def decrypt_openssl(infile=None, outfile=None, passphrase=None):

    cmd = 'openssl enc -d -base64 -aes-256-cbc -salt'.split()

    if infile:
        cmd += ['-in', infile]

    if outfile:
        cmd += ['-out', outfile]

    cmd += ['-k', passphrase]

    p = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()

    return out, err

if __name__ == "__main__":
    key = 'hackfuchallenge2017'
    filein = 'challenge_00/00.aes'
    result = decrypt_openssl(infile=filein, passphrase=key)
    for line in result[0].decode().split('\n'):
        print(line)

    decrypt_openssl(infile='challenge_00/Challenges.zip.enc', outfile='challenge_00/Challenges.zip', passphrase=key)
    # decoding the contents reveals:
    # Ah, good, at least we know you can decrypt stuff.
    #
    # Now that you've decrypted this, you can decrypt the ZIP file with all the challenges using the same password. To register for the 2017 Hackfu Challenge and get your name up on the leaderboard, please send us an email with the following:
    #
    # Subject: Hackfu Challenge 2017 - Registration
    # Email address: covertcorrespondent2017@mwrinfosecurity.com
    # Body: Tell us who you are and where you are from (country). Also tell us what you are currently doing (Student/Developer/Scientist/Lab Rat/Dictator/Dr Evil etc.) -- if you're a South African university student, you'll be in line to win some awesome prizes. Lastly, make sure provide us with your user handle (name you'd like to be called online) so that we can use it to display your progess on our leaderboard at https://covertcorrespondent2017.mwrinfosecurity.com
    #
    # We will post occasional hints where necessary on the website and/or our Twitter, at our own discretion }:-]
    # https://twitter.com/mwrlabs
    #
    # Good luck paranormal investigator! The truth is out there!
