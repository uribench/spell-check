# Cipher Composers for Substitution Ciphering Technique

The source code provided here for substitution ciphers that can be used to compose ciphers
for the encryption and decryption are:

1. Caesar cipher
2. Deranged alphabet cipher

## Caesar cipher

The Caesar cipher performs a cyclic rotation on the provided letters and thus creates a shift 
between the keys and values of the mapping lookup-table. In encryption, the letters are the keys 
while the composed cipher is the values in the key-value pairs of the mapping lookup-table. In
decryption the mapping lookup-table is reversed.

The shift size of the cyclic rotation is parametric. In the provided source code, a positive shift
value is creates a 'left shift' while a negative shift value creates a 'right shift'. Shift equals 
to zero of greater than the length of the list of letters will keep the letters unsifted.

Following is the source code from `caesar_cipher.py`:

```python
"""Substitution cipher using Caesar cipher"""
from string import ascii_letters as letters

def make_cipher(salt):
    """Create a Caesar cipher using a given rotation value as salt"""
    cipher = list(letters)
    return cipher[salt:] + cipher[:salt]
```

The size of shift is provided by the `salt` parameter to the `make_chiper()` function.

The last line uses python’s slicing operator which has following parameters:

```python
    [start : stop : steps]  
```

which means that slicing will start from index `start` and will go up to `stop` (excluded), in step 
of `steps`. 

Default values: 
- `start` is 0, 
- `stop` is last index of list, and
- `step` is 1

Therefore, for `salt=5` the statement `cipher[salt:] + cipher[:salt]` will slice the list from 
`start` index (6th item) till end, and will chain it with the slice of the list from starting till 
`stop` index (5 items) with `step` equal to 1.

Following is the original list of letters on top of the composed cipher for a shift of 5:

```
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', ... , 'U', 'V', 'W', 'X', 'Y', 'Z']
    ['f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', ... , 'Z', 'a', 'b', 'c', 'd', 'e']
```

## Deranged alphabet cipher

The deranged alphabet cipher, also known as mixed alphabet cipher, uses a keyword. Any repeating 
letters are removed from the keyword, and the remaining keyword letters are placed at the beginning 
of the cipher, then all the unused letters in the alphabet are appended to it. 

Only the keyword has to be shared between the two parties in order to compose the same cipher for 
the matching encryption and decryption pair.

Following is the original list of letters on top of the composed cipher for the keyword `QWERTY`:

```
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', ... , 'U', 'V', 'W', 'X', 'Y', 'Z']
    ['Q', 'W', 'E', 'R', 'T', 'Y', a', 'b', 'c', 'd', ... 'P', 'S', 'U', 'V', 'X', 'Z']
```

Following is the source code from `deranged_alphabet_cipher.py`:

```python
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
```

The keyword string is provided by the `salt` parameter to the `make_chiper()` function.

The statement `sorted(set(salt), key=salt.index)` removes duplicates from the provided keyword. This
is done by creating a set from the keyword letters and then sort them based on the original order of 
letters in the keyword, thus preserving the original order. 

The type of returned value from the above statement is a list. It is converted back to string using
the `join` method.

The rest of the code uses regular expressions to remove all the letters used in the keyword from the 
alphabet and append it to the processed keyword.
