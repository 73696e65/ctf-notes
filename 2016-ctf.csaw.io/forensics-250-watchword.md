# Watchword

I solved the challenge after they published two hints:

```
Hint: http://domnit.org/stepic/doc/

Hint: It's not base64, but it uses the Python 3 base64 module

password = password
```

There was a comment in `exif` header, `base64` encoded:

```
$ exiftool powpow.mp4 | grep Title | cut -d: -f2 | tr -d ' ' | base64 -d

http://steghide.sourceforge.net/
```

We extracted the `png` image from the `mp4` file:
```
$ binwalk powpow.mp4

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
547541        0x85AD5         PNG image, 720 x 581, 8-bit/color RGB, non-interlaced
547595        0x85B0B         Zlib compressed data, default compression
547904        0x85C40         Zlib compressed data, default compression
```

```
$ dd if=powpow.mp4 bs=1 skip=547541 > image.png
419063+0 records in
419063+0 records out
419063 bytes (419 kB, 409 KiB) copied, 0.363718 s, 1.2 MB/s
```

Using `stepic`, we extracted the another image (`jpg`) from `png`:

```
$ stepic -d -i image.png  > image.jpg
```

There are hidden some data, we can recoved them using `password` passphrase:

```
$ steghide info image.jpg
"image.jpg":
  format: jpeg
  capacity: 1.7 KB
Try to get information about embedded data ? (y/n) n
```

```
$ steghide extract -sf image.jpg -p password
wrote extracted data to "base64.txt"
```

Finally with python3 `base64` module, we use `b85decode` to read the flag:

```
$ python3

>>> f = open("base64.txt", "r")
>>> data = f.read().rstrip()
>>> f.close()

>>> from base64 import b85decode
>>> b85decode(data)
b'flag{We are fsociety, we are finally free, we are finally awake!}'
```


