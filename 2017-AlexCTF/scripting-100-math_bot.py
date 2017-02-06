#!/usr/bin/env python

from pwn import *
from numpy import mean
import re

def process(command):
    try:
        num1, num2 = map(int, re.findall(r'\d+', command))
    except:
        pass

    if '*' in command:
        return str(num1 * num2)
    if '-' in command:
        return str(num1 - num2)
    if '+' in command:
        return str(num1 + num2)
    if '/' in command:
        return str(num1 / num2)
    if '%' in command:
        return str(num1 % num2)


r = remote('195.154.53.62', 1337)
t = Timeout()
t.timeout = 0.05

while True:
    try:
        r.recvuntil(':\n')
        command = r.recvline()
        sleep(0.05)
        answer = process(command)
        r.sendline(answer)
    except:
        print r.recv(4096)

# ALEXCTF{1_4M_l33t_b0t}