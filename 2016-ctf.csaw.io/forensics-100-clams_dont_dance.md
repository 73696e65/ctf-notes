# Clams Don't Dance

We use `The Sleuth Kit` to analyse the image:

```
$ fls out.img
r/r 3:	USB         (Volume Label Entry)
r/r 5:	._.Trashes
d/d 7:	.Trashes
d/d 10:	.Spotlight-V100
d/d 12:	.fseventsd
r/r * 14:	clam.pptx
r/r 16:	dance.mp4
v/v 3270243:	$MBR
v/v 3270244:	$FAT1
v/v 3270245:	$FAT2
d/d 3270246:	$OrphanFiles
```

`clam.pptx` looks suspicious so we extract it:

```
$ icat out.img 14 > clam.pptx
```

When we `unzip` the `pptx`, there is one file (`image0.gif`) which has a different timestamp and moreover it is not linked in the document:

```
$ ls -lt
total 9488
-rw-r--r--  1 sine  staff    6979 Sep  6 11:25 image0.gif
-rw-rw-r--  1 sine  staff   30602 Jan  1  1980 image1.jpg
-rw-rw-r--  1 sine  staff   29515 Jan  1  1980 image10.jpg
-rw-rw-r--  1 sine  staff   23499 Jan  1  1980 image11.png
-rw-rw-r--  1 sine  staff   18897 Jan  1  1980 image12.png
-rw-rw-r--  1 sine  staff   53048 Jan  1  1980 image13.jpg
-rw-rw-r--  1 sine  staff   30865 Jan  1  1980 image14.jpg
-rw-rw-r--  1 sine  staff   34211 Jan  1  1980 image15.jpg
-rw-rw-r--  1 sine  staff   38920 Jan  1  1980 image16.jpg
-rw-rw-r--  1 sine  staff   24656 Jan  1  1980 image17.jpg
-rw-rw-r--  1 sine  staff   20048 Jan  1  1980 image18.gif
-rw-rw-r--  1 sine  staff  118081 Jan  1  1980 image19.png
-rw-rw-r--  1 sine  staff   89395 Jan  1  1980 image2.jpg
-rw-rw-r--  1 sine  staff   80663 Jan  1  1980 image20.jpg
-rw-rw-r--  1 sine  staff   65815 Jan  1  1980 image21.jpg
-rw-rw-r--  1 sine  staff  258672 Jan  1  1980 image22.png
-rw-rw-r--  1 sine  staff    8319 Jan  1  1980 image23.jpg
-rw-rw-r--  1 sine  staff  232546 Jan  1  1980 image24.png
-rw-rw-r--  1 sine  staff    5277 Jan  1  1980 image25.png
-rw-rw-r--  1 sine  staff  124208 Jan  1  1980 image26.jpg
-rw-rw-r--  1 sine  staff  253876 Jan  1  1980 image27.png
-rw-rw-r--  1 sine  staff  329579 Jan  1  1980 image28.png
-rw-rw-r--  1 sine  staff  379591 Jan  1  1980 image29.png
-rw-rw-r--  1 sine  staff   29635 Jan  1  1980 image3.jpg
-rw-rw-r--  1 sine  staff  396789 Jan  1  1980 image30.png
-rw-rw-r--  1 sine  staff  231275 Jan  1  1980 image31.jpg
-rw-rw-r--  1 sine  staff    8176 Jan  1  1980 image32.gif
-rw-rw-r--  1 sine  staff   29956 Jan  1  1980 image33.jpg
-rw-rw-r--  1 sine  staff   32790 Jan  1  1980 image34.jpg
-rw-rw-r--  1 sine  staff   21739 Jan  1  1980 image35.jpg
-rw-rw-r--  1 sine  staff   20837 Jan  1  1980 image36.jpg
-rw-rw-r--  1 sine  staff  359819 Jan  1  1980 image37.png
-rw-rw-r--  1 sine  staff   70181 Jan  1  1980 image38.png
-rw-rw-r--  1 sine  staff   23371 Jan  1  1980 image39.png
-rw-rw-r--  1 sine  staff   11919 Jan  1  1980 image4.png
-rw-rw-r--  1 sine  staff   18374 Jan  1  1980 image40.jpg
-rw-rw-r--  1 sine  staff   60743 Jan  1  1980 image41.jpg
-rw-rw-r--  1 sine  staff  608631 Jan  1  1980 image5.png
-rw-rw-r--  1 sine  staff   32615 Jan  1  1980 image6.png
-rw-rw-r--  1 sine  staff   12219 Jan  1  1980 image7.jpg
-rw-rw-r--  1 sine  staff  467084 Jan  1  1980 image8.jpg
-rw-rw-r--  1 sine  staff   84197 Jan  1  1980 image9.jpg
```

It reminds us the `Maxicode`, using [QR Code (2D Barcode) Reader](http://www.funcode-tech.com/Download_en.html) 
we can read it. We scanned it with this [iPhone App](https://itunes.apple.com/tw/app/logo-qr-barcode-scanner/id1142976425?mt=8).

```
FLAG{TH1NK ABOUT 1T B1LL. 1F U D13D, WOULD ANY1 CARE??}
```
