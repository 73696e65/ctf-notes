# Fore3: USB probing

```
$ binwalk fore2.pcap

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
62299         0xF35B          PNG image, 460 x 130, 8-bit/color RGBA, interlaced
```

```
$ binwalk -D 'png image:png' fore2.pcap
```

Solution:

```
ALEXCTF{SN1FF_TH3_FL4G_0V3R_U58}
```