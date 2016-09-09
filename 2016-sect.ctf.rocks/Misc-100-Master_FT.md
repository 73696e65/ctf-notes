```
$ date -d @1247501656
Mon Jul 13 18:14:16 CEST 2009
```

```
$ grep "SUSP ENTRY" issue > issue.suspicious
$ grep "07/13/2009" issue.suspicious > issue.suspicious.1247501656
```

We sort the entries by the date and it looks like the flag has always 6 seconds + some multiple of tens. 
```
$ cat issue.suspicious.1247501656 | sed 's#\([0-9][0-9]\)/\([0-9][0-9]\)/\([0-9][0-9][0-9][0-9]\)#\3-\1-\2#' | sort -n | grep 6,
2009-07-13,18:14:16,CEST,.ACB,FILE,NTFS $MFT,$SI [.ACB] time,-,SECT2016-PC,/Windows/System32/se,/Windows/System32/se,2,/Windows/System32/se,41705,{SUSP ENTRY - second prec. $SI [MACB] FN rec AFTER SI rec} ,Log2t::input::mft,-
2009-07-13,18:57:36,CEST,M.CB,FILE,NTFS $MFT,$SI [M.CB] time,-,SECT2016-PC,/Program Files/ct{,/Program Files/ct{,2,/Program Files/ct{,15824,{SUSP ENTRY - second prec. $SI [MACB] FN rec AFTER SI rec} ,Log2t::input::mft,-
2009-07-13,19:40:56,CEST,M.CB,FILE,NTFS $MFT,$SI [M.CB] time,-,SECT2016-PC,/Windows/System32/drivers/etc/H4,/Windows/System32/drivers/etc/H4,2,/Windows/System32/drivers/etc/H4,41713,{SUSP ENTRY - second prec. $SI [MACB] FN rec AFTER SI rec} ,Log2t::input::mft,-
2009-07-13,20:24:16,CEST,M.CB,FILE,NTFS $MFT,$SI [M.CB] time,-,SECT2016-PC,/Windows/ck,/Windows/ck,2,/Windows/ck,41715,{SUSP ENTRY - second prec. $SI [MACB] FN rec AFTER SI rec} ,Log2t::input::mft,-
2009-07-13,21:07:36,CEST,MAC.,FILE,NTFS $MFT,$SI [MAC.] time,-,SECT2016-PC,/Windows/System32/_th,/Windows/System32/_th,2,/Windows/System32/_th,41699,{SUSP ENTRY - second prec. $SI [MACB] FN rec AFTER SI rec} ,Log2t::input::mft,-
2009-07-13,21:50:56,CEST,M.CB,FILE,NTFS $MFT,$SI [M.CB] time,-,SECT2016-PC,/Program Files/Internet Explorer/3_G,/Program Files/Internet Explorer/3_G,2,/Program Files/Internet Explorer/3_G,41719,{SUSP ENTRY - second prec. $SI [MACB] FN rec AFTER SI rec} ,Log2t::input::mft,-
2009-07-13,21:55:16,CEST,MACB,FILE,NTFS $MFT,$SI [MACB] time,-,SECT2016-PC,/Windows/System32/t_t,/Windows/System32/t_t,2,/Windows/System32/t_t,41707,{SUSP ENTRY - second prec. $SI [MACB] FN rec AFTER SI rec} ,Log2t::input::mft,-
2009-07-13,22:34:16,CEST,M.CB,FILE,NTFS $MFT,$SI [M.CB] time,-,SECT2016-PC,/Users/Administrator/1b,/Users/Administrator/1b,2,/Users/Administrator/1b,388,{SUSP ENTRY - second prec. $SI [MACB] FN rec AFTER SI rec} ,Log2t::input::mft,-
2009-07-13,22:39:04,CEST,M...,FILE,NTFS $MFT,$SI [M...] time,-,SECT2016-PC,/Windows/servicing/Packages/MIAB1E~1.MM,/Windows/servicing/Packages/MIAB1E~1.MM,2,/Windows/servicing/Packages/MIAB1E~1.MM,41086,{SUSP ENTRY - second prec. $SI [M...]} ,Log2t::input::mft,-
2009-07-13,22:39:06,CEST,M...,FILE,NTFS $MFT,$SI [M...] time,-,SECT2016-PC,/Windows/servicing/Packages/MI5376~1.MM,/Windows/servicing/Packages/MI5376~1.MM,2,/Windows/servicing/Packages/MI5376~1.MM,41094,{SUSP ENTRY - second prec. $SI [M...]} ,Log2t::input::mft,-
2009-07-13,23:17:36,CEST,MAC.,FILE,NTFS $MFT,$SI [MAC.] time,-,SECT2016-PC,/Windows/System32/s0n},/Windows/System32/s0n},2,/Windows/System32/s0n},41706,{SUSP ENTRY - second prec. $SI [MACB] FN rec AFTER SI rec} ,Log2t::input::mft,-
```

Here we can read the solution, ignoring `t_t`:

```
sect{H4ck_th3_G1bs0n}
```
