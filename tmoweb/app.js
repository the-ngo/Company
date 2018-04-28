var http = require('http');
var fs = require('fs');
var path = require('path')
var hostname = '127.0.0.1';
const port = 3000;
var url = require('url');
var querystring = require('querystring')
http.createServer(function(req, res) {
  if (req.url === "/") {
    fs.readFile("./public/index.html", "UTF-8", function(err, html) {
      res.writeHead(200, {
        "Content-Type": "text/html"
      });
      res.end(html);
    });

  } else if (req.url.match("\.css$")) {
    var cssPath = path.join(__dirname, 'public', req.url);
    var fileStream = fs.createReadStream(cssPath, "UTF-8");
    res.writeHead(200, {
      "Content-Type": "text/css"
    });
    fileStream.pipe(res);

  } else if (req.url.match("\.png$")) {
    var imagepath = path.join(__dirname, 'public', req.url);
    var fileStream = fs.createReadStream(imagepath);
    res.writeHead(200, {
      "Content-Type": "image/png"
    });
    fileStream.pipe(res);
  }
  else {
    res.writeHead(404, {
      "Content-Type": "text/html"
    });
    res.end("<h1> Page not found<h1>");
  }
  //
  if(req.method ==="POST"){
    var data = "";
    req.on("data",function(chunk){
      data += chunk;
    });
    req.on("end",function(chunk){
      var formdata = querystring.parse(data);
      console.log()

      console.log(data)
      resa = data.replace(/&/g," ").replace(/=/g," ");
      final = resa.split(" ");
      console.log(resa)
      for ( var i = 0 ; i<final.length; i++){
        console.log(final[i]);
      }
      var username = final[1];
      var oldpass = final[3];
      var newpass = final[5];
      var retype = final[7];
      if (oldpass == newpass){
        res.end("<h1> The new password cannot be same old password<h1>");
      }
    });
  }
}).listen(port);
