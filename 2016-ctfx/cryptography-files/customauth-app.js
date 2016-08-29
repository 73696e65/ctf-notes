var http = require('http');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');
var crypto = require('crypto');

var secrets = require('./secrets');

var app = express();

app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());

console.log("Starting server...");

var encrypt = function(data) {
  var cipher = crypto.createCipher('aes-128-ecb', secrets.key);
  cipher.setAutoPadding(true);
  var ctxt = cipher.update(data, 'ascii', 'hex');
  ctxt += cipher.final('hex');
  return ctxt;
};

var decrypt = function(data) {
  var decipher = crypto.createDecipher('aes-128-ecb', secrets.key);
  decipher.setAutoPadding(true);
  var ptxt = decipher.update(data, 'hex', 'ascii');
  ptxt += decipher.final('ascii');
  return ptxt;
};

app.get('/', function(req, res) {
  if(req.cookies.auth) {
    var auth = decrypt(req.cookies.auth);
    auth = JSON.parse(auth);
    res.render('index', {auth: auth, flag: secrets.flag});
  }
  else {
    res.render('index', {auth: false});
  }
});

app.post('/logout', function(req, res) {
  res.append('Set-Cookie', 'auth=; Path=/; HttpOnly');
  res.redirect('/');
});

app.post('/login', function(req, res) {
  if(req.body.username && req.body.password && !req.body.admin) {
    if(req.body.username===secrets.username && req.body.password===secrets.password) {
      req.body.admin = true;
    }
    auth = JSON.stringify(req.body);
    auth = encrypt(auth);
    res.append('Set-Cookie', 'auth='+auth+'; Path=/; HttpOnly');
  }
  res.redirect('/');
});

// catch 404
app.use(function(req, res, next) {
  var err = new Error('Not Found');
  err.status = 404;
  next(err);
});

// error handler
app.use(function(err, req, res, next) {
  console.log(err);
  res.status(err.status || 500);
  res.render('error', {
    status: err.status
  });
});

var server = http.createServer(app).listen(3000, function(){
  console.log("HTTP server listening on port 3000!");
});
