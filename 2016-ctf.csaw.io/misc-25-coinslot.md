# Coinslot

```python
#!/usr/bin/env python

from pwn import *

r = remote('misc.chal.csaw.io', '8000')

def process():
    value = float(r.recvline()[1:])

    bills = [10000, 5000, 1000, 500, 100, 50, 20, 10, 5, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
    counter = dict.fromkeys(bills, 0)

    print('input: ' + str(value))
    for bill in bills:
        # the second condition is because we are using float
        while value - bill > 0 or abs(value - bill) < 0.005:
            counter[bill] += 1
            value -= bill

        r.recvuntil(': ')
        r.sendline(str(counter[bill]))

    return r.recvline()

while True:
  print process()
```

```
$ python ./coinbase.py DEBUG
[ .. SNIP .. ]

[DEBUG] Sent 0x2 bytes:
    '1\n'
[DEBUG] Received 0xe bytes:
    'nickels (5c): '
[DEBUG] Sent 0x2 bytes:
    '0\n'
[DEBUG] Received 0xe bytes:
    'pennies (1c): '
[DEBUG] Sent 0x2 bytes:
    '2\n'
[DEBUG] Received 0x47 bytes:
    'correct!\n'
    'flag{started-from-the-bottom-now-my-whole-team-fucking-here}\n'
    '\n'
correct!

Traceback (most recent call last):
  File "./coinbase.py", line 26, in <module>
    print process()
  File "./coinbase.py", line 8, in process
    value = float(r.recvline()[1:])
ValueError: could not convert string to float: lag{started-from-the-bottom-now-my-whole-team-fucking-here}

[*] Closed connection to misc.chal.csaw.io port 8000
```

