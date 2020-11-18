var express = require('express');
var app = express();

var mysql      = require('mysql');
var connection = mysql.createConnection({
  host     : '127.0.0.1',
  user     : 'test',
  password : '',
  database : 'mask'
});

app.get('/', function (req, res) {
  connection.query('SELECT * FROM `mask`', function (error, results, fields) {//SQLの構文入力
    if (error) throw error;
     res.send(results);
    });
});
app.listen(3000, function () {
  console.log('Example app listening on port 3000!');
});