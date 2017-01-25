# bender_safe - Reverse - 50 pts - created by grimmlin

Keygen:

```python
#!/usr/bin/env python

from sys import argv

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

OTP = argv[1]
reply = ""

reply += OTP[0]   
reply += OTP[15]  

if ord(OTP[7]) >= 0x41: 
    reply += chr(ord(OTP[7]) ^ 0x20)
else:                   
    reply += chr(ord(OTP[7]) ^ 0x40)

if ord(OTP[3]) >= 0x41:
    reply += alphabet[(alphabet.index(OTP[3]) + 0xa) % len(alphabet)]
else:
    reply += alphabet[(alphabet.index(OTP[3]) - 0xa) % len(alphabet)]

if ord(OTP[4]) >= 0x41:
    reply += alphabet[(alphabet.index(OTP[4]) + 0xa) % len(alphabet)]
else:
    reply += alphabet[(alphabet.index(OTP[4]) - 0xa) % len(alphabet)]

reply += alphabet[abs(ord(OTP[2])-ord(OTP[1])) % len(alphabet)]
reply += alphabet[abs(ord(OTP[6])-ord(OTP[5])) % len(alphabet)]

if ord(OTP[8]) >= 0x41:
    reply += chr(ord(OTP[8]) ^ 0x20)
else:
    reply += chr(ord(OTP[8]) ^ 0x40)

print reply
```

```
root@kali64:~$ nc bender_safe.teaser.insomnihack.ch 31337
Welcome to Bender's passwords storage service
Here's your OTP challenge :
AQWB922NEU6B2EQA
AAnLZGAe
      _
     ( )
      H
      H
     _H_
  .-'-.-'-.
 /         \
|           |
|   .-------'._
|  / /  '.' '. \
|  \ \ @   @ / /
|   '---------'
|    _______|
|  .'-+-+-+|
|  '.-+-+-+|      INS{Angr_is_great!_Oh_angr_is_great!_Angr_angr_angr}
|    """""" |
'-.__   __.-'
     """

This is Bender's password vault storage
I have 54043195528445952 bytes of memory for storage!
Although 54043195528444928 of which is used to store my fembots videos...HiHiHi!
Your passwords are safe with me meatbag!
-------------------------------
|                             |
|  1. View passwords          |
|  2. Enter new passwords     |
|  3. View admin password     |
|  4. Exit                    |
|                             |
-------------------------------
```

## References:
[MinGW static build](https://github.com/nihilus/snowman/releases/tag/v1.0)
