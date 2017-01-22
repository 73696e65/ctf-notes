# cryptoquizz - Misc/Crypto - 50 pts - realized by cryptopathe

```
$ for i in {1..1000}; do echo | nc quizz.teaser.insomnihack.ch 1031 | grep "What is the birth year of" | cut -c 30-; done | sort -n | uniq  | wc -l
64
```

Solution:

```python
#!/usr/bin/env python

from pwn import *

def process(name):
    d = {}
    d['Alan Turing'] = 1912
    d['Horst Feistel'] = 1915
    d['Claude Shannon'] = 1916
    d['Donald Davies'] = 1924
    d['Michael O. Rabin'] = 1931
    d['Claus-Peter Schnorr'] = 1943
    d['Whitfield Diffie'] = 1944
    d['Jean-Jacques Quisquater'] = 1945
    d['Martin Hellman'] = 1945
    d['Scott Vanstone'] = 1947
    d['Victor S. Miller'] = 1947
    d['Neal Koblitz'] = 1948
    d['Kaisa Nyberg'] = 1948
    d['Jacques Stern'] = 1949
    d['Don Coppersmith'] = 1950
    d['Ueli Maurer'] = 1950
    d['Adi Shamir'] = 1952
    d['Ralph Merkle'] = 1952
    d['Silvio Micali'] = 1954
    d['Xuejia Lai'] = 1954
    d['Gilles Brassard'] = 1955
    d['Taher Elgamal'] = 1955
    d['David Chaum'] = 1955
    d['Ivan Damgard'] = 1956
    d['Arjen K. Lenstra'] = 1956
    d['Ross Anderson'] = 1956
    d['Yvo Desmedt'] = 1956
    d['Amos Fiat'] = 1956
    d['Douglas Stinson'] = 1956
    d['Shafi Goldwasser'] = 1958
    d['Eli Biham'] = 1960
    d['Mitsuru Matsui'] = 1961
    d['Moni Naor'] = 1961
    d['Lars Knudsen'] = 1962
    d['Phil Rogaway'] = 1962
    d['Paul van Oorschot'] = 1962
    d['Mihir Bellare'] = 1962
    d['Rafail Ostrovsky'] = 1963
    d['Bruce Schneier'] = 1963
    d['Bart Preneel'] = 1963
    d['Daniel Bleichenbacher'] = 1964
    d['Jacques Patarin'] = 1965
    d['Joan Daemen'] = 1965
    d['Niels Ferguson'] = 1965
    d['Paulo Barreto'] = 1965
    d['Shai Halevi'] = 1966
    d['Antoine Joux'] = 1967
    d['David Naccache'] = 1967
    d['Nigel P. Smart'] = 1967
    d['Markus Jakobsson'] = 1968
    d['Ronald Cramer'] = 1968
    d['Serge Vaudenay'] = 1968
    d['Alex Biryukov'] = 1969
    d['Dan Boneh'] = 1969
    d['Vincent Rijmen'] = 1970
    d['Daniel J. Bernstein'] = 1971
    d['Yehuda Lindell'] = 1971
    d['Paul Kocher'] = 1973
    d['Amit Sahai'] = 1974

    return d[name]

r = remote('quizz.teaser.insomnihack.ch', 1031)
t = Timeout()
t.timeout = 0.05

i = 0
while True:
    r.recvuntil('What is the birth year of ')
    name = r.recvuntil(' ?')[:-2]
    print 'Processing[' + str(i) + "]: " + repr(name)
    answer = process(name)
    r.sendline(str(answer))
    i += 1
```


```
# Output from ./script.py DEBUG
[ .. SNIP ..]

[DEBUG] Received 0x11b bytes:
    '\n'
    '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
    '~~ OK, young hacker. You are now considered to be a                ~~\n'
    '~~ INS{GENUINE_CRYPTOGRAPHER_BUT_NOT_YET_A_PROVEN_SKILLED_ONE}     ~~\n'
    '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
    '\n'
    '\n'
Traceback (most recent call last):
```

