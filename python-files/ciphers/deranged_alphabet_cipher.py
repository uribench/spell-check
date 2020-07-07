"""Substitution cipher using deranged alphabet"""
from string import ascii_letters as letters
import re
import sys

def make_cipher(salt):
    """Create a deranged alphabet cipher using a keyword as salt"""
    if not salt.isalpha():
        print('salt must include only letters {}'.format(salt))
        sys.exit(1)

    salt = ''.join(sorted(set(salt), key=salt.index))
    pattern = '[{}]'.format(salt)
    return salt + re.sub(pattern, '', ''.join(list(letters)))
