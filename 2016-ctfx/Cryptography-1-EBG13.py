#!/usr/bin/env python

from string import ascii_lowercase, maketrans

secret = 'pgs(ebg13vffhcrefrpher!)'

def caesar(plaintext, shift):
    alphabet = ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)

for i in range(26):
        print i, caesar(secret, i)

# python ./caesar.py | grep ctf
# ctf(rot13issupersecure!)
