# RE3: Catalyst system

- `sub_400C9A` checks if the username is divisible by 8 or 12

- `sub_400CDD` takes 12B from username and checks if it satisfies the following linear equation:

```
v4 - v3 + v2  = 1550207830
v3 + 3 * (v2 + v4)  = 12465522610
v2 * v3  = 3651346623716053780
```

which we solve as:

```
v4 = 1635017059
v3 = 1953724780
v2 = 1868915551

>>> p32(1635017059) + p32(1953724780) + p32(1868915551)
'catalyst_ceo'
```

- `sub_400977` initializes the seed from username (which we already know) and compare the password with hardcoded values, giving `sLSVpQ4vK3cGWyW86AiZhggwLHBjmx9CRspVGggj`

- finally `sub_400876` decrypts and prints the flag

```
root@kali64:~$ ./catalyst2
 ▄▄▄▄▄▄▄▄▄▄▄  ▄            ▄▄▄▄▄▄▄▄▄▄▄  ▄       ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄
▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌▐░▌     ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌▐░▌          ▐░█▀▀▀▀▀▀▀▀▀  ▐░▌   ▐░▌ ▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀
▐░▌       ▐░▌▐░▌          ▐░▌            ▐░▌ ▐░▌  ▐░▌               ▐░▌     ▐░▌
▐░█▄▄▄▄▄▄▄█░▌▐░▌          ▐░█▄▄▄▄▄▄▄▄▄    ▐░▐░▌   ▐░▌               ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄
▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌    ▐░▌    ▐░▌               ▐░▌     ▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌▐░▌          ▐░█▀▀▀▀▀▀▀▀▀    ▐░▌░▌   ▐░▌               ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀
▐░▌       ▐░▌▐░▌          ▐░▌            ▐░▌ ▐░▌  ▐░▌               ▐░▌     ▐░▌
▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄  ▐░▌   ▐░▌ ▐░█▄▄▄▄▄▄▄▄▄      ▐░▌     ▐░▌
▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌     ▐░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░▌
 ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀       ▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀       ▀
Welcome to Catalyst systems
Loading..............................
Username: catalyst_ceo
Password: sLSVpQ4vK3cGWyW86AiZhggwLHBjmx9CRspVGggj
Logging in..............................
your flag is: ALEXCTF{1_t41d_y0u_y0u_ar3__gr34t__reverser__s33}
```