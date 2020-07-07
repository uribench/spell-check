"""Substitution cipher using Caesar cipher"""
from string import ascii_letters as letters

def make_cipher(salt):
    """Create a Caesar cipher using a given rotation value as salt"""
    cipher = list(letters)
    return cipher[salt:] + cipher[:salt]
