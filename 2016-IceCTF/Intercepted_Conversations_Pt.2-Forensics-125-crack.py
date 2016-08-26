#!/usr/bin/env python

import random
import base64
import sys

P = [
    27, 35, 50, 11, 8, 20, 44, 30, 6, 1, 5, 2, 33, 16, 36, 64, 3, 61, 54, 25, 12, 21, 26, 10,
    57, 53, 38, 56, 58, 37, 43, 17, 42, 47, 4, 14, 7, 46, 34, 19, 23, 40, 63, 18, 45, 60, 13,
    15, 22, 9, 62, 51, 32, 55, 29, 24, 41, 39, 49, 52, 48, 28, 31, 59]

S = [
    68, 172, 225, 210, 148, 172, 72, 38, 208, 227, 0, 240, 193, 67, 122, 108, 252, 57, 174, 197,
    83, 236, 16, 226, 133, 94, 104, 228, 135, 251, 150, 52, 85, 56, 174, 105, 215, 251, 111, 77,
    44, 116, 128, 196, 43, 210, 214, 203, 109, 65, 157, 222, 93, 74, 209, 50, 11, 172, 247, 111,
    80, 143, 70, 89]

secret = "Wmkvw680HDzDqMK6UBXChDXCtC7CosKmw7R9w7JLwr/CoT44UcKNwp7DllpPwo3DtsOID8OPTcOWwrzDpi3CtMOKw4PColrCpXUYRhXChMK9w6PDhxfDicOdwoAgwpgNw5/Cvw=="
secret = base64.b64decode(secret)
secret = secret.decode('utf-8')
secret = [ord(x) for x in secret]

for i in range(64):
  sys.stdout.write( chr( (secret[P[i]-1] - S[i]) & 0xff ) )
