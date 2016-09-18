# Kill

There is a broken `pcap` file, which we need to fix. Looks like the file was obtained using tool `dumpcap` on Mac OS X:

```
$ hexdump -C kill.pcapng | head
00000000  aa dd dd aa 8c 00 00 00  4d 3c 2b 1a 01 00 00 00  |........M<+.....|
00000010  ff ff ff ff ff ff ff ff  03 00 2f 00 4d 61 63 20  |........../.Mac |
00000020  4f 53 20 58 20 31 30 2e  31 31 2e 36 2c 20 62 75  |OS X 10.11.6, bu|
00000030  69 6c 64 20 31 35 47 31  30 30 34 20 28 44 61 72  |ild 15G1004 (Dar|
00000040  77 69 6e 20 31 35 2e 36  2e 30 29 00 04 00 34 00  |win 15.6.0)...4.|
00000050  44 75 6d 70 63 61 70 20  31 2e 31 32 2e 34 20 28  |Dumpcap 1.12.4 (|
00000060  76 31 2e 31 32 2e 34 2d  30 2d 67 62 34 38 36 31  |v1.12.4-0-gb4861|
00000070  64 61 20 66 72 6f 6d 20  6d 61 73 74 65 72 2d 31  |da from master-1|
00000080  2e 31 32 29 00 00 00 00  8c 00 00 00 01 00 00 00  |.12)............|
00000090  60 00 00 00 01 00 00 00  00 00 04 00 02 00 06 00  |`...............|
```

If we sniff some of our traffic, we can check if the header matches, but instead of `aa dd dd aa` the file starts with `0a 0d 0d 0a`.

```
$ dumpcap
Capturing on 'eth0'
File: /tmp/wireshark_eth0_20160914212455_WgZFXm.pcapng
Packets captured: 4
Packets received/dropped on interface 'eth0': 4/2 (pcap:1/dumpcap:0/flushed:1/ps_ifdrop:0) (66.7%)
```

```
$ hexdump -C /tmp/wireshark_eth0_20160914212440_jsZWs2.pcapng | head -1
00000000  0a 0d 0d 0a 7c 00 00 00  4d 3c 2b 1a 01 00 00 00  |....|...M<+.....|
```

After we edit the first four bytes and open the file with Wireshark, we read the flag in one of the streams (3).

Easier solution is to read the flag directly on these addresses:

```
006c7d0: ff e0 ba e0 4a 46 49 46 00 01 01 01 00 01 00 01  ....JFIF........
006c7e0: 00 00 ff fe 00 3d 66 6c 61 67 7b 72 6f 73 65 73  .....=flag{roses
006c7f0: 5f 72 5f 62 6c 75 65 5f 76 69 6f 6c 65 74 73 5f  _r_blue_violets_
006c800: 72 5f 72 33 64 5f 6d 61 79 62 33 5f 68 61 72 61  r_r3d_mayb3_hara
006c810: 6d 62 61 65 5f 69 73 5f 6e 6f 74 5f 6b 69 6c 6c  mbae_is_not_kill
006c820: 7d ff ed 00 9c 50 68 6f 74 6f 73 68 6f 70 20 33  }....Photoshop 3
```
