#!/usr/bin/env python

# To 'reverse' byte order in the binary, we used:
# http://www.bernstein-plus-sons.com/.dowling/CSC080/reverse_c.html

# Then it was necessary to replace the first 4 bytes (FLAG) with \x7fELF

def fixed_xor(bin1, bin2):
  """
  XOR two strings with the same length
  """
  return "".join([ chr(ord(x) ^ ord(y)) for (x, y) in zip(bin1, bin2) ])

# More about this here: https://github.com/73696e65/ctf-notes/issues/2
str1 = "\x33\x2b\x79\x49\x26\x2a\x76\x2f\x2e\x2b\x73\x49\x24\x36\x6a\x2b\x38\x49\x78\x25\x2d\x22\x12\x21\x29\x30\x12\x30\x2e\x2a"
str2 = "\x61\x68\x4a\x64\x14\x1a\x47\x19\x03\x72\x36\x08\x6c\x1b\x2e\x6a\x6c\x1a\x55\x67\x68\x76\x46\x64\x7b\x1d\x50\x7f\x67\x63"

print fixed_xor(str1, str2)
