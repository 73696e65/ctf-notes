# RE5: packed movement

First we unpack the binary using `upx`:

```
$ upx -d move
                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2013
UPX 3.91        Markus Oberhumer, Laszlo Molnar & John Reiser   Sep 30th 2013

        File size         Ratio      Format      Name
   --------------------   ------   -----------   -----------
  10308504 <-   2619128   25.41%  netbsd/elf386  move

Unpacked 1 file.
```


To deobfuscate the movfuscated binary:

```
$ git clone https://github.com/kirschju/demovfuscator
$ ./demov -o move-deobfuscated move
```

We set the breakpoint after the `read()` (using `dispatch` method) is called and observe that the flag is compared by one character, correct value is in `edx`:

```
gdb-peda$ context
[----------------------------------registers-----------------------------------]
EAX: 0x58 ('X')
EBX: 0xf7ffd000 --> 0x23f3c
ECX: 0x88049b2b
EDX: 0x41 ('A')
ESI: 0xffffd480 --> 0xffffd5ec ("LC_ALL=en_US.UTF-8")
EDI: 0x804829c (<_start>:       mov    DWORD PTR ds:0x840b150,esp)
EBP: 0x0
ESP: 0x860b128 --> 0x0
EIP: 0x80493f5 (<main+3121>:    mov    DWORD PTR ds:0x820b110,ecx)
EFLAGS: 0x207 (CARRY PARITY adjust zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x80493e5 <main+3105>:       mov    eax,ds:0x806206c
   0x80493ea <main+3110>:       mov    edx,DWORD PTR ds:0x8062068
   0x80493f0 <main+3116>:       mov    ecx,0x88049b2b
=> 0x80493f5 <main+3121>:       mov    DWORD PTR ds:0x820b110,ecx
   0x80493fb <main+3127>:       mov    ds:0x820b000,eax
   0x8049400 <main+3132>:       mov    DWORD PTR ds:0x820b004,edx
   0x8049406 <main+3138>:       mov    DWORD PTR ds:0x820b0a0,edx
   0x804940c <main+3144>:       mov    eax,0x0
[------------------------------------stack-------------------------------------]
0000| 0x860b128 --> 0x0
0004| 0x860b12c --> 0x860b134 ("XXXXXXXXXX\n")
0008| 0x860b130 --> 0x32 ('2')
0012| 0x860b134 ("XXXXXXXXXX\n")
0016| 0x860b138 ("XXXXXX\n")
0020| 0x860b13c --> 0xa5858 ('XX\n')
0024| 0x860b140 --> 0x0
0028| 0x860b144 --> 0x0
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
```

Setting breakpoint on `edx` and updating the `eax` with the correct value after a few minutes gave as the solution:

```
ALEXCTF{M0Vfusc4t0r_w0rk5_l1ke_m4g1c}
```