# RE4: unVM me

```
root@kali64:~$ pycdc/pycdc unvm_me.pyc
# Source Generated with Decompyle++
# File: unvm_me.pyc (Python 2.7)

import md5
md5s = [
    0x831DAA3C843BA8B087C895F0ED305CE7L,
    0x6722F7A07246C6AF20662B855846C2C8L,
    0x5F04850FEC81A27AB5FC98BEFA4EB40CL,
    0xECF8DCAC7503E63A6A3667C5FB94F610L,
    0xC0FD15AE2C3931BC1E140523AE934722L,
    0x569F606FD6DA5D612F10CFB95C0BDE6DL,
    0x68CB5A1CF54C078BF0E7E89584C1A4EL,
    0xC11E2CD82D1F9FBD7E4D6EE9581FF3BDL,
    0x1DF4C637D625313720F45706A48FF20FL,
    0x3122EF3A001AAECDB8DD9D843C029E06L,
    0xADB778A0F729293E7E0B19B96A4C5A61L,
    0x938C747C6A051B3E163EB802A325148EL,
    0x38543C5E820DD9403B57BEFF6020596DL]
print 'Can you turn me back to python ? ...'
flag = raw_input('well as you wish.. what is the flag: ')
if len(flag) > 69:
    print 'nice try'
    exit()
if len(flag) % 5 != 0:
    print 'nice try'
    exit()
for i in range(0, len(flag), 5):
    s = flag[i:i + 5]
    if int('0x' + md5.new(s).hexdigest(), 16) != md5s[i / 5]:
        print 'nice try'
        exit()
        continue
print 'Congratz now you have the flag'
```

```
$ grep custom /usr/share/rainbowcrack/charset.txt
custom = [0123456789CTF{}abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ]

$ crunch 5 5 -f  /usr/share/rainbowcrack/charset.txt custom -o use.me
$ john --wordlist=./use.me --format=raw-md5 crackme
```

```
831daa3c843ba8b087c895f0ed305ce7 : ALEXC
6722f7a07246c6af20662b855846c2c8 : CT{dv
5f04850fec81a27ab5fc98befa4eb40c : 5d4s2
ecf8dcac7503e63a6a3667c5fb94f610 : vj8nk
c0fd15ae2c3931bc1e140523ae934722 : 43s8d
569f606fd6da5d612f10cfb95c0bde6d : 8l6m1
068cb5a1cf54c078bf0e7e89584c1a4e : n5l67
c11e2cd82d1f9fbd7e4d6ee9581ff3bd : ds9v4
1df4c637d625313720f45706a48ff20f : 1n52n
3122ef3a001aaecdb8dd9d843c029e06 : v37j4
adb778a0f729293e7e0b19b96a4c5a61 : 81h3d
938c747c6a051b3e163eb802a325148e : 28n4b
38543c5e820dd9403b57beff6020596d : 6v3k}
```

```
ALEXCTF{dv5d4s2vj8nk43s8d8l6m1n5l67ds9v41n52nv37j481h3d28n4b6v3k}
```

