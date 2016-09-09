Analysis of the image with `volatility`:

```
$ volatility imageinfo -f Station
Volatility Foundation Volatility Framework 2.4
Determining profile based on KDBG search...

          Suggested Profile(s) : Win7SP0x64, Win7SP1x64, Win2008R2SP0x64, Win2008R2SP1x64
                     AS Layer1 : AMD64PagedMemory (Kernel AS)
                     AS Layer2 : VMWareAddressSpace (Unnamed AS)
                     AS Layer3 : FileAddressSpace (/mnt/hgfs/Shared-Folders/Station)
                      PAE type : No PAE
                           DTB : 0x187000L
                          KDBG : 0xf800027f30a0L
          Number of Processors : 1
     Image Type (Service Pack) : 1
                KPCR for CPU 0 : 0xfffff800027f4d00L
             KUSER_SHARED_DATA : 0xfffff78000000000L
           Image date and time : 2016-09-08 08:05:14 UTC+0000
     Image local date and time : 2016-09-08 10:05:14 +0200
```

Process list:

```
$ volatility pslist --profile=Win7SP0x64 -f Station
Volatility Foundation Volatility Framework 2.4
Offset(V)          Name                    PID   PPID   Thds     Hnds   Sess  Wow64 Start                          Exit
------------------ -------------------- ------ ------ ------ -------- ------ ------ ------------------------------ ------------------------------
0xfffffa8000ca4ae0 System                    4      0     85      494 ------      0 2016-09-08 08:00:59 UTC+0000
0xfffffa8001d1f690 smss.exe                256      4      2       32 ------      0 2016-09-08 08:00:59 UTC+0000
0xfffffa8002843b30 csrss.exe               344    336      8      381      0      0 2016-09-08 08:01:02 UTC+0000
0xfffffa8000ca99e0 csrss.exe               380    372      7       76      1      0 2016-09-08 08:01:03 UTC+0000
0xfffffa8001726420 wininit.exe             388    336      3       75      0      0 2016-09-08 08:01:03 UTC+0000
0xfffffa800178cb30 winlogon.exe            416    372      4       95      1      0 2016-09-08 08:01:03 UTC+0000
0xfffffa8000cadb30 services.exe            476    388      8      188      0      0 2016-09-08 08:01:03 UTC+0000
0xfffffa80021a1b30 lsass.exe               484    388      7      716      0      0 2016-09-08 08:01:03 UTC+0000
0xfffffa800288b7b0 lsm.exe                 492    388     10      223      0      0 2016-09-08 08:01:03 UTC+0000
0xfffffa80028f69f0 svchost.exe             600    476     10      354      0      0 2016-09-08 08:01:04 UTC+0000
0xfffffa800291f1d0 svchost.exe             664    476      7      267      0      0 2016-09-08 08:01:04 UTC+0000
0xfffffa8002892b30 LogonUI.exe             748    416      6      177      1      0 2016-09-08 08:01:05 UTC+0000
0xfffffa800296db30 svchost.exe             764    476     18      435      0      0 2016-09-08 08:01:05 UTC+0000
0xfffffa8000d24620 svchost.exe             820    476     19      442      0      0 2016-09-08 08:01:05 UTC+0000
0xfffffa8002989060 svchost.exe             848    476     39     1034      0      0 2016-09-08 08:01:05 UTC+0000
0xfffffa80029a6b30 svchost.exe             964    476     14      271      0      0 2016-09-08 08:01:06 UTC+0000
0xfffffa8002a335f0 svchost.exe             348    476     21      541      0      0 2016-09-08 08:01:07 UTC+0000
0xfffffa8002a8d7b0 spoolsv.exe             984    476     13      438      0      0 2016-09-08 08:01:08 UTC+0000
0xfffffa8002ac7370 svchost.exe            1036    476     18      302      0      0 2016-09-08 08:01:08 UTC+0000
0xfffffa8001e71b30 csrss.exe              1648   1640      9      247      2      0 2016-09-08 08:01:19 UTC+0000
0xfffffa8001eb0060 winlogon.exe           1672   1640      3      110      2      0 2016-09-08 08:01:19 UTC+0000
0xfffffa8002e58630 taskhost.exe           1980    476      8      201      2      0 2016-09-08 08:01:21 UTC+0000
0xfffffa80016e1b30 rdpclip.exe            2020    348      7      179      2      0 2016-09-08 08:01:21 UTC+0000
0xfffffa80016eab30 dwm.exe                2044    820      3       67      2      0 2016-09-08 08:01:21 UTC+0000
0xfffffa80017efb30 explorer.exe           1248   2036     25      805      2      0 2016-09-08 08:01:21 UTC+0000
0xfffffa8002ddeb30 audiodg.exe            1652    764      4      124      0      0 2016-09-08 08:01:24 UTC+0000
0xfffffa8001a4d180 SearchIndexer.         1512    476     14      699      0      0 2016-09-08 08:01:29 UTC+0000
0xfffffa8001af0620 cmd.exe                1748   1248      1       21      2      0 2016-09-08 08:01:32 UTC+0000
0xfffffa8001b06790 conhost.exe            1712   1648      2       52      2      0 2016-09-08 08:01:32 UTC+0000
0xfffffa8001abeb30 SearchProtocol         1796   1512      8      387      0      0 2016-09-08 08:01:33 UTC+0000
0xfffffa8001b78b30 iexplore.exe           2136   1248     14      454      2      1 2016-09-08 08:02:26 UTC+0000
0xfffffa8000dd03e0 iexplore.exe           2252   2136      8      271      2      1 2016-09-08 08:02:30 UTC+0000
0xfffffa8000df3570 notepad.exe            2444   1248      1       59      2      0 2016-09-08 08:02:34 UTC+0000
0xfffffa8000d4f910 calc.exe               2664   1248      3       74      2      0 2016-09-08 08:03:06 UTC+0000
0xfffffa8000e54060 mscorsvw.exe           2680    476      6       85      0      1 2016-09-08 08:03:10 UTC+0000
0xfffffa8000eca930 mscorsvw.exe           2704    476      6       78      0      0 2016-09-08 08:03:11 UTC+0000
0xfffffa8000eb56e0 svchost.exe            2752    476      5       70      0      0 2016-09-08 08:03:13 UTC+0000
0xfffffa8000f0cb30 cmd.exe                2780   1248      1       21      2      0 2016-09-08 08:03:13 UTC+0000
0xfffffa8000ef2b30 sppsvc.exe             2788    476      5      147      0      0 2016-09-08 08:03:13 UTC+0000
0xfffffa8000e90340 conhost.exe            2796   1648      2       52      2      0 2016-09-08 08:03:13 UTC+0000
0xfffffa8000e91950 svchost.exe            2840    476     13      325      0      0 2016-09-08 08:03:14 UTC+0000
0xfffffa8000e04a70 powershell.exe          808   1248     12      474      2      0 2016-09-08 08:03:49 UTC+0000
0xfffffa8000fedb30 conhost.exe             788   1648      2       54      2      0 2016-09-08 08:03:51 UTC+0000
0xfffffa8000ff1060 WmiPrvSE.exe           1684    600      6      166      0      0 2016-09-08 08:04:02 UTC+0000
0xfffffa8000ff6060 SearchProtocol         2380   1512      7      276      2      0 2016-09-08 08:04:34 UTC+0000
0xfffffa8000ff9b30 SearchFilterHo         1020   1512      6      143      0      0 2016-09-08 08:04:34 UTC+0000
0xfffffa8001068b30 WMIADAP.exe            2584    848      6       90      0      0 2016-09-08 08:05:09 UTC+0000
0xfffffa8000fbc920 WmiPrvSE.exe           2736    600      8      125      0      0 2016-09-08 08:05:09 UTC+0000
```

Command scan:

```
$ volatility cmdscan --profile=Win7SP0x64 -f Station
Volatility Foundation Volatility Framework 2.4
**************************************************
CommandProcess: conhost.exe Pid: 788
CommandHistory: 0x2133260 Application: powershell.exe Flags: Allocated, Reset
CommandCount: 7 LastAdded: 6 LastDisplayed: 6
FirstCommand: 0 CommandCountMax: 50
ProcessHandle: 0x60
Cmd #0 @ 0x289f30: Set-ExecutionPolicy Unrestricted
Cmd #1 @ 0x2133470: yes
Cmd #2 @ 0x361470: clear
Cmd #3 @ 0x361490: cd ..
Cmd #4 @ 0x289ee0: cd .\Users\ThePlague\Desktop
Cmd #5 @ 0x2133480: cls
Cmd #6 @ 0x361450: .\Game.ps1
```

Because the file `Game.ps1` looks suspicious, we extract it to check if there is any clue.

```
$ volatility filescan --profile=Win7SP0x64 -f Station  | grep Game.ps1
Volatility Foundation Volatility Framework 2.4
Offset(P)            #Ptr   #Hnd Access Name
------------------ ------ ------ ------ ----
0x000000003fdc8a20     16      0 R--r-- \Device\HarddiskVolume2\Users\ThePlague\Desktop\Game.ps1
```

```
$ volatility dumpfiles --profile=Win7SP0x64 -f Station --physoffset=0x000000003fdc8a20 --dump-dir output/
Volatility Foundation Volatility Framework 2.4
DataSectionObject 0x3fdc8a20   None   \Device\HarddiskVolume2\Users\ThePlague\Desktop\Game.ps1
```

We download the original [snake](http://www.twentysidedblog.com/a-powershell-snake-game/) game and compare the sources. They are almost the same, except the three mutices:

```
$ diff Snake.ps1 file.None.0xfffffa8001060e10.dat

    $mtx1 = New-Object System.Threading.Mutex($false, "I don't play well with others.");$mtx1.WaitOne()
    $mtx2 = New-Object System.Threading.Mutex($false, "Hidden in plain sight.");$mtx2.WaitOne()
    $mtx3 = New-Object System.Threading.Mutex($false, "All you need is a .png");$mtx3.WaitOne()
```

We check which thread is associated with them:

```
$ volatility mutantscan --profile=Win7SP0x64 -f Station
Volatility Foundation Volatility Framework 2.4
Offset(P)              #Ptr     #Hnd Signal Thread                   CID Name
------------------ -------- -------- ------ ------------------ --------- ----
0x000000003fde5f70        2        1      0 0xfffffa8001014b60   808:976 I don't play well with others.
0x000000003fde9200        2        1      0 0xfffffa8001014b60   808:976 All you need is a .png
0x000000003fde92c0        2        1      0 0xfffffa8001014b60   808:976 Hidden in plain sight.
```

```
$ volatility threads --profile=Win7SP0x64 -f Station > threads.all
[ .. SNIP .. ]
ETHREAD: 0xfffffa8001014b60 Pid: 808 Tid: 976
Tags:
Created: 2016-09-08 08:03:54 UTC+0000
Exited: 1970-01-01 00:00:00 UTC+0000
Owning Process: powershell.exe
Attached Process: powershell.exe
State: Waiting:WrLpcReply
BasePriority: 0x8
Priority: 0xb
TEB: 0x7fffffa0000
StartAddress: 0x77b0c500 ntdll.dll
Win32Thread: 0xfffff900c2038c30
CrossThreadFlags: PS_CROSS_THREAD_FLAGS_DEADTHREAD
0x77b0c500 4883ec48         SUB RSP, 0x48
0x77b0c504 4c8bc9           MOV R9, RCX
0x77b0c507 488b0552da1000   MOV RAX, [RIP+0x10da52]
0x77b0c50e 4885c0           TEST RAX, RAX
0x77b0c511 0f84e3840300     JZ 0x77b449fa
0x77b0c517 4c               DB 0x4c
```

Because we have not found any further information in `powershell` process, we took the screenshot, where the solution was finally revealed:

```
$ volatility screenshot --profile=Win7SP0x64 -f Station -D output

$ echo -n c2VjdHs0bmRyMDFkNV9jNG50X2gxZDN9Cg==  | base64 -D
sect{4ndr01d5_c4nt_h1d3}
```
