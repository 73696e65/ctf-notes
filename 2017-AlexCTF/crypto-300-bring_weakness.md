# CR5: Bring weakness

We fetch the first 32768 numbers, then the PRNG starts to repeat: 

```python
#!/usr/bin/env python

from pwn import *

x = remote('195.154.53.62', 7412)

f = open('nums.txt', 'w')

for _ in range(0, 32768):
    print _
    x.recvuntil('2: Give me the next number\n')
    x.sendline('2')
    num = x.recvline()
    f.write(num)
f.close()

x.interactive()
```

```
root@kali64:~$ head nums.txt
3521574185
1150688941
220272533
1347899797
2903473250
2192475601
1891835768
3653416117
2088442820
2732428441
```

```
$ python fetch.py 
...
32763
32764
32765
32766
32767
[*] Switching to interactive mode
Guessed 0/10
1: Guess the next number
2: Give me the next number
$ 1
Next number (in decimal) is
$ 3521574185
Guessed 1/10
1: Guess the next number
2: Give me the next number
$ 1
Next number (in decimal) is
$ 1150688941
Guessed 2/10
Guessed 2/10
1: Guess the next number
2: Give me the next number
$ 1
Next number (in decimal) is
$ 220272533
Guessed 3/10
1: Guess the next number
2: Give me the next number
$ 1
Next number (in decimal) is
$ 1347899797
Guessed 4/10
1: Guess the next number
2: Give me the next number
$ 1
Next number (in decimal) is
$ 2903473250
Guessed 5/10
1: Guess the next number
2: Give me the next number
$ 1
Next number (in decimal) is
$ 2192475601
Guessed 6/10
1: Guess the next number
2: Give me the next number
$ 1
Next number (in decimal) is
$ 1891835768
Guessed 7/10
1: Guess the next number
2: Give me the next number
$ 1
Next number (in decimal) is
$ 3653416117
Guessed 8/10
1: Guess the next number
2: Give me the next number
$ 1
Next number (in decimal) is
$ 2088442820
Guessed 9/10
1: Guess the next number
2: Give me the next number
$ 1
Next number (in decimal) is
$ 2732428441
flag is ALEXCTF{f0cfad89693ec6787a75fa4e53d8bdb5}
```