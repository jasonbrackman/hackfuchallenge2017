# !/usr/bin/python

'''
This file requires: python-crypto, python-dev

'''

try:
    from Crypto.Cipher import AES
    from Crypto import Random
except ImportError:
    from Cryptodome.Cipher import AES
    from Cryptodome import Random
import base64
import argparse
import sys


def encrypt(filename, key):
    with open(filename, 'r') as f:
        clear_text = f.read().rstrip()
    clear_text += (AES.block_size - len(clear_text) % AES.block_size) * chr(
        AES.block_size - len(clear_text) % AES.block_size)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    with open(filename + '.enc', 'w') as f:
        f.write(base64.b64encode(iv + cipher.encrypt(clear_text)))
    print('Encryption complete. Check {}.enc for output.'.format(filename))


def decrypt(filename, key):
    with open(filename, 'r') as f:
        cipher_text = f.read().rstrip()
        # cipher_text = cipher_text[0:-2]
    cipher_text = base64.b64decode(cipher_text)
    iv = cipher_text[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    cipher_text = cipher.decrypt(cipher_text[AES.block_size:])
    cipher_text = cipher_text[:-ord(cipher_text[len(cipher_text) - 1:])]
    print(cipher_text)
    with open(filename + '.dec', 'wb') as f:
        f.write(cipher_text)
    print('Decryption complete. Check {}.dec for output.'.format(filename))


def check_key_length(key):
    if sys.getsizeof(key) - 37 == (16 or 24 or 32):
        return key
    elif sys.getsizeof(key) - 37 > 32:
        return key[:32]
    elif sys.getsizeof(key) - 37 > 24:
        return key[:24]
    elif sys.getsizeof(key) - 37 > 16:
        return key[:16]
    else:
        return None


if __name__ == '__main__':
    test = 'wejustfireinside'
    sys.argv = ['', '-f', '08.txt.enc', '-k', test, '-d']
    desc = '''
    Encrypt or decrypt files.
    '''
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('-d', dest='decrypt', action='store_true', required=False)
    parser.add_argument('-e', dest='encrypt', action='store_true', required=False)
    parser.add_argument('-f', dest='filename', type=str, required=True)
    parser.add_argument('-k', dest='key', required=True, type=str)

    args = parser.parse_args()
    print(args)
    if args.decrypt:
        key = check_key_length(args.key)
        if key is not None:
            key = key.encode()
            decrypt(args.filename, key)
        else:
            print("Error. Incompatible key length.")
    elif args.encrypt:
        key = check_key_length(args.key)
        if key is not None:
            encrypt(args.filename, key)
        else:
            print("Error. Incompatible key length.")
    else:
        print('Error. You need to specify whether to encrypt or decrpyt the file.')
