# CR4: Poor RSA

```
$ openssl rsa -in key.pub -pubin -text -modulus
Modulus (399 bit):
    52:a9:9e:24:9e:e7:cf:3c:0c:bf:96:3a:00:96:61:
    77:2b:c9:cd:f6:e1:e3:fb:fc:6e:44:a0:7a:5e:0f:
    89:44:57:a9:f8:1c:3a:e1:32:ac:56:83:d3:5b:28:
    ba:5c:32:42:43
Exponent: 65537 (0x10001)
Modulus=52A99E249EE7CF3C0CBF963A009661772BC9CDF6E1E3FBFC6E44A07A5E0F894457A9F81C3AE132AC5683D35B28BA5C324243
writing RSA key
-----BEGIN PUBLIC KEY-----
ME0wDQYJKoZIhvcNAQEBBQADPAAwOQIyUqmeJJ7nzzwMv5Y6AJZhdyvJzfbh4/v8
bkSgel4PiURXqfgcOuEyrFaD01soulwyQkMCAwEAAQ==
-----END PUBLIC KEY-----
```

Sage script (does not gave the correct solution):

```python
# http://www.factordb.com
N = 0x52A99E249EE7CF3C0CBF963A009661772BC9CDF6E1E3FBFC6E44A07A5E0F894457A9F81C3AE132AC5683D35B28BA5C324243
p = 863653476616376575308866344984576466644942572246900013156919
q = 965445304326998194798282228842484732438457170595999523426901

assert(N == p * q)

c = int('Ni45iH4UnXSttNuf0Oy80+G5J7tm8sBJuDNN7qfTIdEKJow4siF2cpSbP/qIWDjSi+w='.decode('base64').encode('hex'), 16)

e = 65537

phi = (p - 1) * (q - 1)
bezout = xgcd(e, phi);

d = Integer(mod(bezout[1], phi))

assert( mod(d * e, phi) == 1 )

decrypted = Mod(c, N) ** d
flag = hex(Integer(decrypted)).decode('hex')
```

Another try with [rsatool](https://github.com/ius/rsatool):

```
root@kali64:~/rsatool on master $ ./rsatool.py -p 863653476616376575308866344984576466644942572246900013156919 -q 965445304326998194798282228842484732438457170595999523426901 -o priv.txt
Using (p, q) to initialise RSA instance

n =
52a99e249ee7cf3c0cbf963a009661772bc9cdf6e1e3fbfc6e44a07a5e0f894457a9f81c3ae132ac
5683d35b28ba5c324243

e = 65537 (0x10001)

d =
33ad09ca06f50f9e90b1acae71f390d6b92f1d6d3b6614ff871181c4df08da4c5f5012457a643094
05eaecd6341e43027931

p =
899683060c76b9c0de581a69e0ea9d91bed1071beb1d924a37

q =
99cde74aedee87adffdd684cbc478e759870b4f20692f65255

Saving PEM as priv.txt
```

```
$ base64 -d flag.b64 > flag
$ openssl rsautl -in flag -inkey priv.txt -decrypt
ALEXCTF{SMALL_PRIMES_ARE_BAD}
```