# Fore2: Mail client

```
gdb-peda$ info proc mappings
Mapped address spaces:

          Start Addr           End Addr       Size     Offset objfile
            0x6df000           0x6e0000     0x1000    0xdf000 /usr/bin/mutt-org
            0x6e0000           0x6e5000     0x5000    0xe0000 /usr/bin/mutt-org
      0x7fc64e225000     0x7fc64e226000     0x1000     0x5000 /lib/x86_64-linux-gnu/libnss_dns-2.23.so
      0x7fc64e226000     0x7fc64e227000     0x1000     0x6000 /lib/x86_64-linux-gnu/libnss_dns-2.23.so
      0x7fc64e431000     0x7fc64e432000     0x1000     0xa000 /lib/x86_64-linux-gnu/libnss_files-2.23.so
      0x7fc64e432000     0x7fc64e433000     0x1000     0xb000 /lib/x86_64-linux-gnu/libnss_files-2.23.so
      0x7fc64e643000     0x7fc64e644000     0x1000     0xa000 /lib/x86_64-linux-gnu/libnss_nis-2.23.so
      0x7fc64e644000     0x7fc64e645000     0x1000     0xb000 /lib/x86_64-linux-gnu/libnss_nis-2.23.so
      0x7fc64e85a000     0x7fc64e85b000     0x1000    0x15000 /lib/x86_64-linux-gnu/libnsl-2.23.so
      0x7fc64e85b000     0x7fc64e85c000     0x1000    0x16000 /lib/x86_64-linux-gnu/libnsl-2.23.so
      0x7fc64ea65000     0x7fc64ea66000     0x1000     0x7000 /lib/x86_64-linux-gnu/libnss_compat-2.23.so
      0x7fc64ea66000     0x7fc64ea67000     0x1000     0x8000 /lib/x86_64-linux-gnu/libnss_compat-2.23.so
      0x7fc64ec6d000     0x7fc64ec6e000     0x1000     0x6000 /usr/lib/x86_64-linux-gnu/libffi.so.6.0.4
      0x7fc64ec6e000     0x7fc64ec6f000     0x1000     0x7000 /usr/lib/x86_64-linux-gnu/libffi.so.6.0.4
      0x7fc64ee86000     0x7fc64ee87000     0x1000    0x17000 /lib/x86_64-linux-gnu/libresolv-2.23.so
      0x7fc64ee87000     0x7fc64ee88000     0x1000    0x18000 /lib/x86_64-linux-gnu/libresolv-2.23.so
      0x7fc64f08c000     0x7fc64f08d000     0x1000     0x2000 /lib/x86_64-linux-gnu/libkeyutils.so.1.5
      0x7fc64f08d000     0x7fc64f08e000     0x1000     0x3000 /lib/x86_64-linux-gnu/libkeyutils.so.1.5
      0x7fc64f2a0000     0x7fc64f2a1000     0x1000    0x12000 /lib/x86_64-linux-gnu/libgpg-error.so.0.17.0
      0x7fc64f2a1000     0x7fc64f2a2000     0x1000    0x13000 /lib/x86_64-linux-gnu/libgpg-error.so.0.17.0
      0x7fc64f4b3000     0x7fc64f4b4000     0x1000    0x11000 /usr/lib/x86_64-linux-gnu/libassuan.so.0.7.2
      0x7fc64f4b4000     0x7fc64f4b5000     0x1000    0x12000 /usr/lib/x86_64-linux-gnu/libassuan.so.0.7.2
      0x7fc64f7bc000     0x7fc64f7bd000     0x1000   0x107000 /lib/x86_64-linux-gnu/libm-2.23.so
      0x7fc64f7bd000     0x7fc64f7be000     0x1000   0x108000 /lib/x86_64-linux-gnu/libm-2.23.so
      0x7fc64f9d5000     0x7fc64f9d6000     0x1000    0x17000 /lib/x86_64-linux-gnu/libpthread-2.23.so
      0x7fc64f9d6000     0x7fc64f9d7000     0x1000    0x18000 /lib/x86_64-linux-gnu/libpthread-2.23.so
      0x7fc64fbe9000     0x7fc64fbea000     0x1000     0xe000 /lib/x86_64-linux-gnu/libbz2.so.1.0.4
      0x7fc64fbea000     0x7fc64fbeb000     0x1000     0xf000 /lib/x86_64-linux-gnu/libbz2.so.1.0.4
      0x7fc64fe69000     0x7fc64fe6a000     0x1000    0x7e000 /usr/lib/x86_64-linux-gnu/libgmp.so.10.3.0
      0x7fc64fe6a000     0x7fc64fe6b000     0x1000    0x7f000 /usr/lib/x86_64-linux-gnu/libgmp.so.10.3.0
      0x7fc65009c000     0x7fc65009d000     0x1000    0x31000 /usr/lib/x86_64-linux-gnu/libhogweed.so.4.2
      0x7fc65009d000     0x7fc65009e000     0x1000    0x32000 /usr/lib/x86_64-linux-gnu/libhogweed.so.4.2
      0x7fc6502d1000     0x7fc6502d3000     0x2000    0x33000 /usr/lib/x86_64-linux-gnu/libnettle.so.6.2
      0x7fc6502d3000     0x7fc6502d4000     0x1000    0x35000 /usr/lib/x86_64-linux-gnu/libnettle.so.6.2
      0x7fc6504e5000     0x7fc6504e6000     0x1000    0x11000 /usr/lib/x86_64-linux-gnu/libtasn1.so.6.5.1
      0x7fc6504e6000     0x7fc6504e7000     0x1000    0x12000 /usr/lib/x86_64-linux-gnu/libtasn1.so.6.5.1
      0x7fc65073f000     0x7fc650749000     0xa000    0x58000 /usr/lib/x86_64-linux-gnu/libp11-kit.so.0.1.0
      0x7fc650749000     0x7fc65074b000     0x2000    0x62000 /usr/lib/x86_64-linux-gnu/libp11-kit.so.0.1.0
      0x7fc650963000     0x7fc650964000     0x1000    0x18000 /lib/x86_64-linux-gnu/libz.so.1.2.8
      0x7fc650964000     0x7fc650965000     0x1000    0x19000 /lib/x86_64-linux-gnu/libz.so.1.2.8
      0x7fc650b6e000     0x7fc650b6f000     0x1000     0x9000 /usr/lib/x86_64-linux-gnu/libkrb5support.so.0.1
      0x7fc650b6f000     0x7fc650b70000     0x1000     0xa000 /usr/lib/x86_64-linux-gnu/libkrb5support.so.0.1
      0x7fc650d72000     0x7fc650d73000     0x1000     0x2000 /lib/x86_64-linux-gnu/libcom_err.so.2.1
      0x7fc650d73000     0x7fc650d74000     0x1000     0x3000 /lib/x86_64-linux-gnu/libcom_err.so.2.1
      0x7fc650f9f000     0x7fc650fa1000     0x2000    0x2b000 /usr/lib/x86_64-linux-gnu/libk5crypto.so.3.1
      0x7fc650fa1000     0x7fc650fa2000     0x1000    0x2d000 /usr/lib/x86_64-linux-gnu/libk5crypto.so.3.1
      0x7fc651266000     0x7fc651273000     0xd000    0xc3000 /usr/lib/x86_64-linux-gnu/libkrb5.so.3.3
      0x7fc651273000     0x7fc651275000     0x2000    0xd0000 /usr/lib/x86_64-linux-gnu/libkrb5.so.3.3
      0x7fc651477000     0x7fc651478000     0x1000     0x2000 /lib/x86_64-linux-gnu/libdl-2.23.so
      0x7fc651478000     0x7fc651479000     0x1000     0x3000 /lib/x86_64-linux-gnu/libdl-2.23.so
      0x7fc651838000     0x7fc65183c000     0x4000   0x1bf000 /lib/x86_64-linux-gnu/libc-2.23.so
      0x7fc65183c000     0x7fc65183e000     0x2000   0x1c3000 /lib/x86_64-linux-gnu/libc-2.23.so
      0x7fc651a7b000     0x7fc651a7c000     0x1000    0x39000 /usr/lib/x86_64-linux-gnu/libgpgme.so.11.14.0
      0x7fc651a7c000     0x7fc651a7e000     0x2000    0x3a000 /usr/lib/x86_64-linux-gnu/libgpgme.so.11.14.0
      0x7fc651caf000     0x7fc651cb0000     0x1000    0x31000 /usr/lib/x86_64-linux-gnu/libidn.so.11.6.15
      0x7fc651cb0000     0x7fc651cb1000     0x1000    0x32000 /usr/lib/x86_64-linux-gnu/libidn.so.11.6.15
      0x7fc651fb6000     0x7fc651fb7000     0x1000   0x105000 /usr/lib/x86_64-linux-gnu/libtokyocabinet.so.9.11.0
      0x7fc651fb7000     0x7fc651fb8000     0x1000   0x106000 /usr/lib/x86_64-linux-gnu/libtokyocabinet.so.9.11.0
      0x7fc6521d1000     0x7fc6521d2000     0x1000    0x19000 /usr/lib/x86_64-linux-gnu/libsasl2.so.2.0.25
      0x7fc6521d2000     0x7fc6521d3000     0x1000    0x1a000 /usr/lib/x86_64-linux-gnu/libsasl2.so.2.0.25
      0x7fc6524f5000     0x7fc652500000     0xb000   0x122000 /usr/lib/x86_64-linux-gnu/libgnutls.so.30.6.2
      0x7fc652500000     0x7fc652502000     0x2000   0x12d000 /usr/lib/x86_64-linux-gnu/libgnutls.so.30.6.2
      0x7fc652749000     0x7fc65274b000     0x2000    0x46000 /usr/lib/x86_64-linux-gnu/libgssapi_krb5.so.2.2
      0x7fc65274b000     0x7fc65274d000     0x2000    0x48000 /usr/lib/x86_64-linux-gnu/libgssapi_krb5.so.2.2
      0x7fc652971000     0x7fc652975000     0x4000    0x24000 /lib/x86_64-linux-gnu/libtinfo.so.5.9
      0x7fc652975000     0x7fc652976000     0x1000    0x28000 /lib/x86_64-linux-gnu/libtinfo.so.5.9
      0x7fc652ba3000     0x7fc652ba4000     0x1000    0x2d000 /lib/x86_64-linux-gnu/libncursesw.so.5.9
      0x7fc652ba4000     0x7fc652ba5000     0x1000    0x2e000 /lib/x86_64-linux-gnu/libncursesw.so.5.9
      0x7fc652dca000     0x7fc652dcb000     0x1000    0x25000 /lib/x86_64-linux-gnu/ld-2.23.so
```

```
root@kali64:~$ readelf -n core.1719
root@kali64:~$ objdump -s core.1719
```

The only suspicious string which we found in the binary was something which looked as `smtp_pass`: 

```
tp_pass = "e. en kv,dvlejhgouehg;oueh fenjhqeouhfouehejbge ef"
```

We found another instance of this file together with:

```
dksgkpdjg;kdj;gkje;gj;dkgv a enpginewognvln owkge  noejne
```

Solution:

```
$ ./forensics-100-mail_client.py
[+] Opening connection to 195.154.53.62 on port 2222: Done
[DEBUG] Received 0x7 bytes:
    'Email: '
[DEBUG] Sent 0x14 bytes:
    'alexctf@example.com\n'
[DEBUG] Received 0xa bytes:
    'Password: '
[DEBUG] Sent 0x3a bytes:
    'dksgkpdjg;kdj;gkje;gj;dkgv a enpginewognvln owkge  noejne\n'
[DEBUG] Received 0x29 bytes:
    '1 new unread flag\n'
    'ALEXCTF{Mu77_Th3_CoRe}\n'
[*] Closed connection to 195.154.53.62 port 2222
```