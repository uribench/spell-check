"""Substitution ciphers based decoder"""
from string import ascii_letters as letters

def decode(secret, cipher):
    """Decode an encoded secret using a given substitution cipher"""
    return secret.translate(str.maketrans(''.join(cipher), letters))
