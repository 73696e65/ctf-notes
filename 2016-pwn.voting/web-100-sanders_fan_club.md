# Sanders Fan Club

Because the application loads `css` from the `flag2.jpg` file, we tried to fetch the resource with different content-type:

```
$ curl -I http://sandersfanclub.pwn.democrat
HTTP/1.1 200 OK
Server: nginx/1.10.0 (Ubuntu)
Date: Sat, 05 Nov 2016 08:34:58 GMT
Content-Type: text/html
Content-Length: 1951
Last-Modified: Thu, 03 Nov 2016 00:04:55 GMT
Connection: keep-alive
ETag: "581a7f27-79f"
Link: <flag2.jpg>;rel=stylesheet
Accept-Ranges: bytes
```

```
$ curl http://sandersfanclub.pwn.democrat/flag2.jpg -H "Accept: text/css"
/* Space out content a bit */
body {
  padding-top: 40px;
  padding-bottom: 40px;
  background-color: #eee;
}

/* Everything but the jumbotron gets side spacing for mobile first views */
.header,
.marketing,
.footer {
  padding-right: 15px;
  padding-left: 15px;
}

/* Custom page header */
.header {
  padding-bottom: 20px;
  border-bottom: 1px solid #e5e5e5;
}
/* Make the masthead heading the same height as the navigation */
.header h3 {
  margin-top: 0;
  margin-bottom: 0;
  line-height: 40px;
}

/* Custom page footer */
.footer {
  padding-top: 19px;
  color: #777;
  border-top: 1px solid #e5e5e5;
}

/* Customize container */
@media (min-width: 768px) {
  .container {
    max-width: 730px;
  }
}
.container-narrow > hr {
  margin: 30px 0;
}

/* Main marketing message and sign up button */
.jumbotron {
  text-align: center;
  border-bottom: 1px solid #e5e5e5;
}
.jumbotron .btn {
  padding: 14px 24px;
  font-size: 21px;
}

/* Supporting marketing content */
.marketing {
  margin: 40px 0;
}
.marketing p + h4 {
  margin-top: 28px;
}

/* Responsive: Portrait tablets and up */
@media screen and (min-width: 768px) {
  /* Remove the padding we set earlier */
  .header,
  .marketing,
  .footer {
    padding-right: 0;
    padding-left: 0;
  }
  /* Space out the masthead */
  .header {
    margin-bottom: 30px;
  }
  /* Remove the bottom border on the jumbotron for visual effect */
  .jumbotron {
    border-bottom: 0;
  }
}

.form-signin {
  max-width: 330px;
  padding: 15px;
  margin: 0 auto;
}
.form-signin .form-signin-heading,
.form-signin .checkbox {
  margin-bottom: 10px;
}
.form-signin .checkbox {
  font-weight: normal;
}
.form-signin .form-control {
  position: relative;
  height: auto;
  -webkit-box-sizing: border-box;
     -moz-box-sizing: border-box;
          box-sizing: border-box;
  padding: 10px;
  font-size: 16px;
}
.form-signin .form-control:focus {
  z-index: 2;
}
.form-signin input[type="email"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.form-signin input[type="password"] {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}

/*
 * How did I... Nevermind. I'm pretty sure my creds are in a text file
 */
 ```

```
$ curl http://sandersfanclub.pwn.democrat/flag2.jpg -H "Accept: text/plain"
Password reminder: flag{I_am_very_bad_with_computers}
(Go tell chrome devs to support RFC 5988
Firefox masterrace)
```

