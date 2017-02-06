# Fore4: Unknown format

- Extract the package captures using `Wireshark`:

```
root@kali64:~/usb-challenge$ ls -l
total 184
-rw-r--r-- 1 root root  4096 Jan 18 17:16 109.data
-rw-r--r-- 1 root root  4096 Jan 18 17:50 109.pgn
-rw-r--r-- 1 root root  4096 Jan 18 17:16 115.data
-rw-r--r-- 1 root root  4096 Jan 18 17:16 121.data
-rw-r--r-- 1 root root 61440 Jan 18 17:11 19.data
-rw-r--r-- 1 root root 61440 Jan 18 17:16 25.data
-rw-r--r-- 1 root root 28672 Jan 18 17:16 31.data
-rw-r--r-- 1 root root  4096 Jan 18 17:16 37.data
-rw-r--r-- 1 root root  4096 Jan 18 17:17 4160.data
-rw-r--r-- 1 root root  4096 Jan 18 17:16 55.data
-rw-r--r-- 1 root root  8192 Jan 18 17:16 8256.data
```

```
root@kali64:~/usb-challenge$ cat 19.data 25.data 31.data > kindle.bin
```

- Install [KindleTool](https://github.com/yifanlu/KindleTool) to identify and extract the firmware.

```
root@kali64:~/usb-challenge$ ../KindleTool/KindleTool/Release/kindletool convert -i kindle.bin
Checking update package 'kindle.bin'.
Bundle         SP01 (Signing Envelope)
Cert number    0
Cert file      pubdevkey01.pem (Developer)
Bundle         FC04 (OTA [ota])
Bundle Type    OTA V2
Minimum OTA    0
Target OTA     18446744073709551615
Devices        2
Device         Silver Kindle 4 Non-Touch (2011)
Device         Black Kindle 4 Non-Touch (2012)
Critical       0
Padding Byte   0 (0x00)
MD5 Hash       6d365ea5d3b953706488d36b5fa867bd
Metadata       0
```

```
root@kali64:~/usb-challenge$ ../KindleTool/KindleTool/Release/kindletool convert -s kindle.bin
Converting update package 'kindle.bin' to 'kindle_converted.tar.gz' (with sig, delete input).
Bundle         SP01 (Signing Envelope)
Cert number    0
Cert file      pubdevkey01.pem (Developer)
Bundle         FC04 (OTA [ota])
Bundle Type    OTA V2
Minimum OTA    0
Target OTA     18446744073709551615
Devices        2
Device         Silver Kindle 4 Non-Touch (2011)
Device         Black Kindle 4 Non-Touch (2012)
Critical       0
Padding Byte   0 (0x00)
MD5 Hash       6d365ea5d3b953706488d36b5fa867bd
Metadata       0
```

```
root@kali64:~/usb-challenge$ tar xvzf kindle_converted.tar.gz
kindle_out/
kindle_out/rootfs_md5_list.tar.gz
kindle_out/2540270001-2692310002.ffs
kindle_out/flag.txt
kindle_out/update-patches.tar.gz

gzip: stdin: invalid compressed data--format violated
tar: Unexpected EOF in archive
tar: Unexpected EOF in archive
tar: Error is not recoverable: exiting now
```

```
root@kali64:~/usb-challenge$ ls kindle_out/
2540270001-2692310002.ffs  flag.txt  rootfs_md5_list.tar.gz  update-patches.tar.gz

root@kali64:~/usb-challenge$ cat kindle_out/flag.txt
ALEXCTF{Wh0_N33d5_K1nDl3_t0_3X7R4Ct_K1ND13_F1rMw4R3}
```