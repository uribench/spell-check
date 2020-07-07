#!/usr/bin/env python3

"""Sample code demonstrating usage of the Caesar cipher"""
from ciphers.caesar_cipher import make_cipher
from encoder import encode
from decoder import decode

def main():
    """ Simple example entry point"""
    message = 'Clean Code'
    cipher = make_cipher(5)
    secret = encode(message, cipher)
    print('secret: {}'.format(secret))
    # secret: Hqjfs Htij
    print(decode(secret, cipher))

if __name__ == '__main__':
    main()
