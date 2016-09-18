# Sleeping Guard

```
$ nc crypto.chal.csaw.io 8000 | base64 -D > img-encrypted.png
```

From the source code we can see the key length (12), used to XOR the image:

```python
import base64
from twisted.internet import reactor, protocol
import os

PORT = 9013

import struct
def get_bytes_from_file(filename):
    return open(filename, "rb").read()

KEY = "[CENSORED]"

def length_encryption_key():
    return len(KEY)

def get_magic_png():
    image = get_bytes_from_file("./sleeping.png")
    encoded_string = base64.b64encode(image)
    key_len = length_encryption_key()
    print 'Sending magic....'
    if key_len != 12:
        return ''
    return encoded_string


class MyServer(protocol.Protocol):
    def connectionMade(self):
        resp = get_magic_png()
        self.transport.write(resp)

class MyServerFactory(protocol.Factory):
    protocol = MyServer

factory = MyServerFactory()
reactor.listenTCP(PORT, factory)
reactor.run()
```

The first few bytes of the legitimate `png` file should look like:

```
00000000  89 50 4e 47 0d 0a 1a 0a  00 00 00 0d 49 48 44 52  |.PNG........IHDR|
```

Using this information and [xortool-xor](https://github.com/hellman/xortool), 
we were able to extract the file manually:

```
$ xortool-xor -f img-encrypted.png -s "\x89"  | hexdump -C | head -1
00000000  57 b6 86 a6 db c2 cc c8  ec f0 a8 bb 97 ae 8c b3  |W...............|

$ xortool-xor -f img-encrypted.png -s "\x57"  | hexdump -C | head -1
00000000  89 68 58 78 05 1c 12 16  32 2e 76 65 49 70 52 6d  |.hXx....2.veIpRm|

$ xortool-xor -f img-encrypted.png -s "\x57\x50"  | hexdump -C | head -1
00000000  89 6f 58 7f 05 1b 12 11  32 29 76 62 49 77 52 6a  |.oX.....2)vbIwRj|

$ xortool-xor -f img-encrypted.png -s "\x57\x6f"  | hexdump -C | head -1
00000000  89 50 58 40 05 24 12 2e  32 16 76 5d 49 48 52 55  |.PX@.$..2.v]IHRU|
```

```
$ xortool-xor -f img-encrypted.png -s "\x57\x6f\x41\x68\x5f\x41\x5f\x4b\x65\x79\x21\x3f"  > flag.png
```

Finally, we read the answer from the png file:

```
flag{l4zy_H4CK3rs_d0nt_g3t_MAg1C_FLaG5}
```
