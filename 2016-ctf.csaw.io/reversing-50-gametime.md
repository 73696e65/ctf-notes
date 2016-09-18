# Gametime

There were a several things which we manually patched (keypresses, time delay), this part of the program was 
called often and we negated the condition on `0x00401554` to `je` to pass the check:

```
.text:00401549 8B CF                             mov     ecx, edi
.text:0040154B E8 10 FD FF FF                    call    sub_401260
.text:00401550 5F                                pop     edi
.text:00401551 5E                                pop     esi
.text:00401552 84 C0                             test    al, al
.text:00401554 75 21                             jnz     short loc_401577
.text:00401556 FF 75 0C                          push    [ebp+arg_4]
.text:00401559 FF 75 10                          push    [ebp+arg_8]
.text:0040155C 68 50 7A 41 00                    push    offset aKeyIsSS_0 ; "key is %s (%s)\r"
.text:00401561 E8 F5 04 00 00                    call    print_something
.text:00401566 68 B0 7A 41 00                    push    offset aUdderFailure_0 ; "UDDER FAILURE! http://imgur.com/4Ajx21P"...
.text:0040156B E8 EB 04 00 00                    call    print_something
.text:00401570 83 C4 10                          add     esp, 10h
.text:00401573 32 C0                             xor     al, al
.text:00401575 5D                                pop     ebp
.text:00401576 C3                                retn
```

The goal was to reach this part to print the flag:

```
.text:00401973 0F B6 06                          movzx   eax, byte ptr [esi]
.text:00401976 50                                push    eax
.text:00401977 68 DC 7A 41 00                    push    offset a02x     ; "%02x"
.text:0040197C E8 DA 00 00 00                    call    print_something
.text:00401981 59                                pop     ecx
.text:00401982 46                                inc     esi
.text:00401983 59                                pop     ecx
.text:00401984 83 EB 01                          sub     ebx, 1
.text:00401987 75 EA                             jnz     short loc_401973
.text:00401989 68 E4 7A 41 00                    push    offset asc_417AE4 ; ")\n\n"
.text:0040198E E8 C8 00 00 00                    call    print_something
.text:00401993 8B 1D 20 21 41 00                 mov     ebx, ds:Sleep
.text:00401999 59                                pop     ecx
```

Finally the whole output:
```
        ZOMGZOMGOZMGZOMGZOMGOZMGZOMGZOMGOZMGZOMGZOMGOZMG
        ZOMGZOMG                                ZOMGZOMG
        ZOMGZOMG     TAP TAP REVOLUTION!!!!!!!  ZOMGZOMG
        ZOMGZOMG                                ZOMGZOMG
        ZOMGZOMGOZMGZOMGZOMGOZMGZOMGZOMGOZMGZOMGZOMGOZMG


                      R U READDY?!


The game is starting in...
Get ready to play
Get ready to play
Get ready to play
Get ready to play
Get ready to play
Get ready to play
Get ready to play
Get ready to play
Get ready to play
Get ready to play
ZOMGZOMGOZMGZOMGZOMGOZMGZOMGZOMGOZMGZOMGZOMGOZMG

When you see an 's', press the space bar

ZOMGZOMGOZMGZOMGZOMGOZMGZOMGZOMGOZMGZOMGZOMGOZMG
Get ready to play
Get ready to play
Get ready to play
Get ready to play
Get ready to play
Get ready to play
Get ready to play
Get ready to play
Get ready to play
Get ready to play
..........s
ZOMGZOMGOZMGZOMGZOMGOZMGZOMGZOMGOZMGZOMGZOMGOZMG

When you see an 'x', press the 'x' key

ZOMGZOMGOZMGZOMGZOMGOZMGZOMGZOMGOZMGZOMGZOMGOZMG
Get ready to play
Get ready to play
Get ready to play
Get ready to play
Get ready to play
Get ready to play
Get ready to play
Get ready to play
Get ready to play
Get ready to play
........x
ZOMGZOMGOZMGZOMGZOMGOZMGZOMGZOMGOZMGZOMGZOMGOZMG

When you see an 'm', press the 'm' key

ZOMGZOMGOZMGZOMGZOMGOZMGZOMGZOMGOZMGZOMGZOMGOZMG
Get ready to play
Get ready to play
Get ready to play
Get ready to play
Get ready to play
Get ready to play
Get ready to play
Get ready to play
Get ready to play
Get ready to play
.....m
TRAINING COMPLETE!




















Now you know everything you need to know....


for the rest of your life!




















LETS PLAY !




















Get ready to play
Get ready to play
Get ready to play
Get ready to play
Get ready to play
Get ready to play
Get ready to play
Get ready to play
Get ready to play
Get ready to play
.....s
..x
.m
ooooh, you fancy!!!
.....m
..x
.s
key is not (NIIICE JOB)!!!!




















TURBO TIME!

key is  (no5c30416d6cf52638460377995c6a8cf5)
```
