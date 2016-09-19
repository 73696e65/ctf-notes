# evidence.zip

The flag is hidden in CRC values:

```
$ zipinfo -v evidence.zip | grep CRC
  32-bit CRC value (hex):                         666c6167
  32-bit CRC value (hex):                         7b746833
  32-bit CRC value (hex):                         5f766931
  32-bit CRC value (hex):                         3169346e
  32-bit CRC value (hex):                         5f77335f
  32-bit CRC value (hex):                         6e333364
  32-bit CRC value (hex):                         5f236672
  32-bit CRC value (hex):                         65656c65
  32-bit CRC value (hex):                         6666656e
  32-bit CRC value (hex):                         7daaaaaa
  32-bit CRC value (hex):                         aaaaaaaa
  32-bit CRC value (hex):                         aaaaaaaa
  32-bit CRC value (hex):                         aaaaaaaa
```

```
$ for x in $(zipinfo -v evidence.zip | grep CRC | cut -d: -f 2 | sed 's# +#0x#g'); do export x; python -c 'import os; from struct import pack; from sys import stdout; stdout.write( pack(">I", int(os.environ["x"], 16)) )'; done
flag{th3_vi11i4n_w3_n33d_#freeleffen}
```



