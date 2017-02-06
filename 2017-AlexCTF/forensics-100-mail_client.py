#!/usr/bin/env python

from pwn import *
from sys import argv

context.log_level = 'debug'

r = remote('195.154.53.62', 2222)
r.recvuntil('Email: ')
r.sendline('alexctf@example.com')
r.recvuntil('Password: ')
r.sendline("dksgkpdjg;kdj;gkje;gj;dkgv a enpginewognvln owkge  noejne")

output = r.recv(4096)
time.sleep(0.2)

