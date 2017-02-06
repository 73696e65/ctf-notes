# RE2: C++ is awesome

```
gdb-peda$ b *0x400c75
Breakpoint 1 at 0x400c75

gdb-peda$ r _________________________________________________________________

gdb-peda$ commands
Type commands for breakpoint(s) 1, one per line.
End with a line saying just "end".
>printf "%c", $al
>p $dl = $al
>continue
>end
```

```
gdb-peda$ r
Starting program: /root/re2 _________________________________________________________________
A$1 = 0x41

Breakpoint 1, 0x0000000000400c75 in ?? ()
L$2 = 0x4c

Breakpoint 1, 0x0000000000400c75 in ?? ()
E$3 = 0x45

Breakpoint 1, 0x0000000000400c75 in ?? ()
X$4 = 0x58

Breakpoint 1, 0x0000000000400c75 in ?? ()
C$5 = 0x43

Breakpoint 1, 0x0000000000400c75 in ?? ()
T$6 = 0x54

Breakpoint 1, 0x0000000000400c75 in ?? ()
F$7 = 0x46

Breakpoint 1, 0x0000000000400c75 in ?? ()
{$8 = 0x7b

Breakpoint 1, 0x0000000000400c75 in ?? ()
W$9 = 0x57

Breakpoint 1, 0x0000000000400c75 in ?? ()
3$10 = 0x33

Breakpoint 1, 0x0000000000400c75 in ?? ()
_$11 = 0x5f

Breakpoint 1, 0x0000000000400c75 in ?? ()
L$12 = 0x4c

Breakpoint 1, 0x0000000000400c75 in ?? ()
0$13 = 0x30

Breakpoint 1, 0x0000000000400c75 in ?? ()
v$14 = 0x76

Breakpoint 1, 0x0000000000400c75 in ?? ()
3$15 = 0x33

Breakpoint 1, 0x0000000000400c75 in ?? ()
_$16 = 0x5f

Breakpoint 1, 0x0000000000400c75 in ?? ()
C$17 = 0x43

Breakpoint 1, 0x0000000000400c75 in ?? ()
_$18 = 0x5f

Breakpoint 1, 0x0000000000400c75 in ?? ()
W$19 = 0x57

Breakpoint 1, 0x0000000000400c75 in ?? ()
1$20 = 0x31

Breakpoint 1, 0x0000000000400c75 in ?? ()
t$21 = 0x74

Breakpoint 1, 0x0000000000400c75 in ?? ()
h$22 = 0x68

Breakpoint 1, 0x0000000000400c75 in ?? ()
_$23 = 0x5f

Breakpoint 1, 0x0000000000400c75 in ?? ()
C$24 = 0x43

Breakpoint 1, 0x0000000000400c75 in ?? ()
L$25 = 0x4c

Breakpoint 1, 0x0000000000400c75 in ?? ()
4$26 = 0x34

Breakpoint 1, 0x0000000000400c75 in ?? ()
5$27 = 0x35

Breakpoint 1, 0x0000000000400c75 in ?? ()
5$28 = 0x35

Breakpoint 1, 0x0000000000400c75 in ?? ()
3$29 = 0x33

Breakpoint 1, 0x0000000000400c75 in ?? ()
5$30 = 0x35

Breakpoint 1, 0x0000000000400c75 in ?? ()
}$31 = 0x7d

Breakpoint 1, 0x0000000000400c75 in ?? ()
L$32 = 0x4c

Program received signal SIGSEGV, Segmentation fault.
0x0000000000400c72 in ?? ()
```

Solution:

```
ALEXCTF{W3_L0v3_C_W1th_CL45535}
```