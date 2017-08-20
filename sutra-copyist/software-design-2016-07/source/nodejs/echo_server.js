// エコーサーバ(TCP)
//
var net = require('net');

// TCPサーバーを作成する
var server = net.createServer();
// 最大接続数を指定
server.maxConnections = 10;

// 接続イベントを定義する
server.on('connection',
  function(socket) {
    var data = '';
    var newline = /\r\n|\n/;
    // データ受信イベントを定義する
    socket.on('data', function(chunk) {
        string = chunk.toString()
        if ( string == 'exit' + "\r\n"
          || string == 'exit' + "\n") {
            // chunkの中身がexitの場合は接続終了とする
          socket.end();
        }
        data += string;
        var client = socket.remoteAddress + ':' + socket.remotePort;
        // 改行コードが含まれているか？
        if (newline.test(data)) {
          console.log(client + " >> " + data);
          // 受け取ったデータを返送する
          if (socket.writable) {
            socket.write("RET: " + data);
          }
          data = '';
      }
    });
    // 接続断イベントを定義する
    socket.on('end', function() {
      server.getConnections(
        function(err, count) {
          console.log('Connection End()');
        });
    });
  });
// クローズイベントを定義する
server.on('close',
  function() {
    console.log('Server Closed');
  });
// 待受アドレスとポートを指定し、接続待ちをおこなう
server.listen(3000, '127.0.0.1',
  function() {
    var addr = server.address();
    console.log('Start Server - ' + addr.address + ':' + addr.port);
  });
