"""Substitution ciphers based encoder"""
from string import ascii_letters as letters

def encode(message, cipher):
    """Encode a plain text message using a given substitution cipher"""
    return message.translate(str.maketrans(letters, ''.join(cipher)))
