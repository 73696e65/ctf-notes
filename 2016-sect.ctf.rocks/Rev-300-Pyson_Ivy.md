We download [pyinstallerextractor](https://sourceforge.net/projects/pyinstallerextractor/) to unpack the python exe file:
```
$ python ~/Downloads/pyinstxtractor.py  PYsonIvy.exe
[*] Processing PYsonIvy.exe
[*] Pyinstaller version: 2.1+
[*] Python version: 27
[*] Length of package: 3132800 bytes
[*] Found 20 files in CArchive
[*] Begining extraction...please standby
[*] Found 197 files in PYZ archive
[*] Successfully extracted pyinstaller archive: PYsonIvy.exe

You can now use a python decompiler on the pyc files within the extracted directory
```

For the `implant.blob` file decryption, in `implant_loader` we add the print statement (line 92, `exec_blob` routine):
```python
 89         def compile_exec_blob(self):
 90                 enc_code = self.load_py_blob()
 91                 code = self.rc4_decrypt_blob(enc_code)
 92                 print code
 93                 print self.info.format("Compiling blob ...")
 ```
 
 The following output is printed out:
 ```python
import os
import sys
import sys
from ctypes import *
import shlex
import subprocess
import time
import re
from base64 import b64decode

#tfw no RC6
class RC4(object):
        def __init__(self):
                pass

        def convert_key(self, key):
                key = [ord(c) for c in key]
                while len(key) < 16:
                        key.append(0)
                return key

        def KSA(self, key):
                keylength = len(key)
                S = range(256)
                j = 0
                for i in range(256):
                        j = (j + S[i] + key[i % keylength]) % 256
                        S[i], S[j] = S[j], S[i]
                return S

        def PRGA(self, S):
                i = 0
                j = 0
                while True:
                        i = (i + 1) % 256
                        j = (j + S[i]) % 256
                        S[i], S[j] = S[j], S[i]

                        K = S[(S[i] + S[j]) % 256]
                        yield K

        def encrypt(self, key, data):
                enc = []
                key = self.convert_key(key)
                S = self.KSA(key)
                K = self.PRGA(S)
                for c in data:
                        enc.append(ord(c) ^ K.next())
                return enc

        def decrypt(self, key, data):
                dec = []
                S = self.KSA(key)
                K = self.PRGA(S)
                for c in data:
                        dec.append(ord(c) ^ K.next())
                return dec


class POINT(Structure):
        _fields_ = [('x', c_long),('y', c_long)]

class SYSTEMTIME(Structure):
        _fields_ = [
                ("wYear", c_short),
                ("wMonth", c_short),
                ("wDayOfWeek", c_short),
                ("wDay", c_short),
                ("wHour", c_short),
                ("wMinute", c_short),
                ("wSecond", c_short),
                ("wMilliseconds", c_short),
        ]

class Implant(object):
        def __init__(self):
                self.fail = "[!] Uh oh contact the admin of the CTF! Reason:{}"
                self.execute()
        
        def exec_cmd(self, cmd, wait=True, use_shell=False):
                try:
                        cmd = shlex.split(cmd)
                        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=use_shell)
                        if wait:
                                out, err = p.communicate()
                                return out, err
                        return
                except Exception as e:
                        self.destruct("subprocess pls :(")
                if len(err) > 0:
                        self.destruct("subprocess pls :(")
        
        def rick_roll(self):
                self.exec_cmd('start "" "http://www.youtube.com/watch?v=dQw4w9WgXcQ"', wait=False, use_shell=True)

        def destruct(self, msg):
                print self.fail.format(msg)
                sys.exit(0)

        def failure(self, msg):
                print "[-] {}".format(msg)
                sys.exit(0)

        def check_virtual(self):
                out, err = self.exec_cmd("wmic bios get serialnumber")
                if "vmware" in out.lower() or "virtual" in out.lower():
                        return True
                return False
        
        def check_human(self):
                pos_orig = POINT()
                pos_new = POINT()
                tests = 0
                windll.user32.GetCursorPos(byref(pos_orig))
                while tests < 10:
                        windll.user32.GetCursorPos(byref(pos_new))
                        if pos_new.x != pos_orig.x or pos_new.y != pos_orig.y:
                                tests += 1
                                pos_orig.x = pos_new.x
                                pos_orig.y = pos_new.y
                        time.sleep(1)

        def check_debugger(self):
                dbgs = ["OLLYDBG", "WinDbgFrameClass", "QWidget"]
                for dbg in dbgs:
                        try:
                                if windll.user32.FindWindowA(c_char_p(dbg), None):
                                        return True
                        except Exception as e:
                                self.destruct(e)
                return False
        
        def defense(self):
                if self.check_debugger():
                        self.rick_roll()
                        self.failure("Debugger detected!")
                if self.check_virtual():
                        self.rick_roll()
                        self.failure("Virtualization detected!")
                self.check_human()
                return False

        def fp_one(self):
                out, err = self.exec_cmd("wmic cpu get NumberOfCores")
                try:
                        res = int(re.search(r'\r\r\n(\d)', out).group(0))
                except Exception as e:
                        self.destruct("fingerprint one failed :( ({})".format(e))
                return res

        def fp_two(self):
                time = SYSTEMTIME()
                windll.kernel32.GetLocalTime(byref(time))
                return int(time.wMonth), int(time.wDayOfWeek), int(time.wHour)

        def fp_three(self):
                out, err = self.exec_cmd("wmic os get Version")
                try:
                        res = re.search(r'\r\r\n(\d+\.\d)', out).group(0)
                        major = int(res.split('.')[0])
                        minor = int(res.split('.')[1])
                        return major, minor
                except Exception as e:
                        self.destruct("fingerprint three failed :( ({})".format(e))
                return res

        def fp_four(self):
                SM_CMONITORS = 80
                SM_MOUSEPRESENT = 19
                mo = windll.user32.GetSystemMetrics(c_int(SM_CMONITORS))
                pr = windll.user32.GetSystemMetrics(c_int(SM_MOUSEPRESENT))
                return int(mo), int(pr)

        def build_fingerprint(self, pwd):
                c =  self.fp_one()
                dbg =  int(self.check_debugger())
                m, d, h = self.fp_two()
                ma, mi = self.fp_three()
                mo, pr = self.fp_four()

                fingerprint = [0] * 16
                fingerprint[0] = ord(pwd[0])
                fingerprint[1] = ord(pwd[1])
                fingerprint[2] = ord(pwd[2])
                fingerprint[3] = ord(pwd[3])
                fingerprint[4] = ord(pwd[4])
                fingerprint[5] = 0x2a + m
                fingerprint[6] = 0x78 + pr
                fingerprint[7] = ord(os.name.lower()[0])
                fingerprint[8] = 0x52 + mo
                fingerprint[9] = 0x64 + c
                fingerprint[10] = 0x17 ^ 0x40
                fingerprint[11] = 0x30 + d
                fingerprint[12] = 0x6e + h
                fingerprint[13] = 0x29 + ma
                fingerprint[14] = 0x53 + mi
                fingerprint[15] = 0x21 + dbg
                return fingerprint

        def decrypt_payload(self, key):
                payload = "iroXqJ6jBkOhtVER3DZsOl8M+i33zyZu2i6WzNtbh5fmhpFD/JRUofF32Ho="
                dec = RC4().decrypt(key, b64decode(payload))
                data = []
                for n in dec:
                        try:
                                data.append(chr(n))
                        except:
                                self.failure("Payload is corrupt / Wrong key :(")

                flag = ''.join(data)
                if flag.startswith("SECT{") and flag.endswith("}"):
                        print "[+] Payload decrypted: {}".format(flag)
                else:
                        self.failure("Payload is corrupt / Wrong key :(")

        def execute(self):
                if not self.defense():
                        print "[>] Implant password:",
                        pwd = raw_input()
                        if pwd == "d4nk_":
                                fingerprint = self.build_fingerprint(pwd)
                                self.decrypt_payload(fingerprint)
                        else:
                                self.failure("Incorrect password!")

Implant()
```

We slightly modify the file to brute force the flag:

```python
#!/usr/bin/env python

import os
import sys
import sys
from ctypes import *
import shlex
import subprocess
import time
import re
from base64 import b64decode

#tfw no RC6
class RC4(object):
    def __init__(self):
        pass

    def convert_key(self, key):
        key = [ord(c) for c in key]
        while len(key) < 16:
            key.append(0)
        return key

    def KSA(self, key):
        keylength = len(key)
        S = range(256)
        j = 0
        for i in range(256):
            j = (j + S[i] + key[i % keylength]) % 256
            S[i], S[j] = S[j], S[i]
        return S

    def PRGA(self, S):
        i = 0
        j = 0
        while True:
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]

            K = S[(S[i] + S[j]) % 256]
            yield K

    def encrypt(self, key, data):
        enc = []
        key = self.convert_key(key)
        S = self.KSA(key)
        K = self.PRGA(S)
        for c in data:
            enc.append(ord(c) ^ K.next())
        return enc

    def decrypt(self, key, data):
        dec = []
        S = self.KSA(key)
        K = self.PRGA(S)
        for c in data:
            dec.append(ord(c) ^ K.next())
        return dec


class POINT(Structure):
    _fields_ = [('x', c_long),('y', c_long)]

class SYSTEMTIME(Structure):
    _fields_ = [
        ("wYear", c_short),
        ("wMonth", c_short),
        ("wDayOfWeek", c_short),
        ("wDay", c_short),
        ("wHour", c_short),
        ("wMinute", c_short),
        ("wSecond", c_short),
        ("wMilliseconds", c_short),
    ]

class Implant(object):
    def __init__(self):
        self.fail = "[!] Uh oh contact the admin of the CTF! Reason:{}"
        self.execute()

    def destruct(self, msg):
        print self.fail.format(msg)
        sys.exit(0)

    def failure(self, msg):
        print "[-] {}".format(msg)
        sys.exit(0)

    def defense(self):
        return False

    def fp_one(self):
        out, err = self.exec_cmd("wmic cpu get NumberOfCores")
        try:
            res = int(re.search(r'\r\r\n(\d)', out).group(0))
        except Exception as e:
            self.destruct("fingerprint one failed :( ({})".format(e))
        return res

    def fp_two(self):
        time = SYSTEMTIME()
        windll.kernel32.GetLocalTime(byref(time))
        return int(time.wMonth), int(time.wDayOfWeek), int(time.wHour) # 1-12, 0-6, 0-23

    def fp_three(self):
        out, err = self.exec_cmd("wmic os get Version")
        try:
            res = re.search(r'\r\r\n(\d+\.\d)', out).group(0)
            major = int(res.split('.')[0])
            minor = int(res.split('.')[1])
            return major, minor
        except Exception as e:
            self.destruct("fingerprint three failed :( ({})".format(e))
        return res

    def fp_four(self):
        SM_CMONITORS = 80
        SM_MOUSEPRESENT = 19
        mo = windll.user32.GetSystemMetrics(c_int(SM_CMONITORS))
        print mo
        pr = windll.user32.GetSystemMetrics(c_int(SM_MOUSEPRESENT))
        print pr
        return int(mo), int(pr)

    def build_fingerprint(self, pwd, c, m, d, h, ma, mi, mo, pr):
        #dbg =  int(self.check_debugger())
        dbg =  int(False)
        #m, d, h = self.fp_two()
        #ma, mi = self.fp_three()
        #mo, pr = self.fp_four()

        fingerprint = [0] * 16
        fingerprint[0] = ord(pwd[0])
        fingerprint[1] = ord(pwd[1])
        fingerprint[2] = ord(pwd[2])
        fingerprint[3] = ord(pwd[3])
        fingerprint[4] = ord(pwd[4])
        fingerprint[5] = 0x2a + m
        fingerprint[6] = 0x78 + pr
        fingerprint[7] = 110 # ord('nt'[0])
        # fingerprint[7] = ord(os.name.lower()[0])
        fingerprint[8] = 0x52 + mo
        fingerprint[9] = 0x64 + c
        fingerprint[10] = 0x17 ^ 0x40
        fingerprint[11] = 0x30 + d
        fingerprint[12] = 0x6e + h
        fingerprint[13] = 0x29 + ma
        fingerprint[14] = 0x53 + mi
        fingerprint[15] = 0x21 + dbg
        return fingerprint

    def decrypt_payload(self, key):
        payload = "iroXqJ6jBkOhtVER3DZsOl8M+i33zyZu2i6WzNtbh5fmhpFD/JRUofF32Ho="
        dec = RC4().decrypt(key, b64decode(payload))
        data = []
        for n in dec:
            try:
                data.append(chr(n))
            except:
                self.failure("Payload is corrupt / Wrong key :(")

        flag = ''.join(data)
        if flag.startswith("SECT{") and flag.endswith("}"):
            print "[+] Payload decrypted: {}".format(flag)

    def execute(self):
        pwd = "d4nk_"
        m, d, h = 0, 0, 0 # self.fp_two() 1-12, 0-6, 0-23
        ma, mi = 0, 0     # self.fp_three() 0-10, 0-3
        mo, pr = 0, 0     # self.fp_four() 0-4, 0-1 
        for c in range(0, 16 + 1):
            print c
            for m in range(1, 12 + 1):
                for d in range(0, 6 + 1):
                    for h in range(0, 23 + 1):
                        for ma in range(0, 10 + 1):
                            for mi in range(0, 3 + 1):
                                for mo in range(0, 4 + 1):
                                    for pr in range(0, 1 + 1):
                                        fingerprint = self.build_fingerprint(pwd, c, m, d, h, ma, mi, mo, pr)
                                        self.decrypt_payload(fingerprint)

Implant()
```

```
$ pypy cracker.py
0
1
2
3
4
[+] Payload decrypted: SECT{g00d_job_n0w_roLL_th3_attr1bution_dic3}
```
