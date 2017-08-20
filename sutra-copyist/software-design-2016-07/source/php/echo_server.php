<?php
# ホストアドレス
$host = "127.0.0.1"
# ポート番号
$port = 3000;

# ソケット(TCP)を作成する
$socket = socket_create(AF_INET,
            SOCK_STREAM, SOL_TCP)
if (false == ($socket)) {
  $errno = socket_last_error();
  $msg = socket_strerror($errno);
  echo "Create Error: " . $msg . "\n";
  exit(-1);
}

# 待受アドレスとポートを指定する
$err = socket_bind($socket, $host, $port)
if (false == $err) {
  $errno = socket_last_error();
  $msg = socket_strerror($errno);
  echo "Bind Error: " . $msg . "\n";
  exit(-1);
}

# 接続待ちソケットを指定する
if (false == socket_listen($socket)) {
  $errno = socket_last_error();
  $msg = socket_strerror($errno);
  echo "Listen Error: " . $msg . "\n";
  exit(-1);
}

echo "ServerStart:127.0.0.1:".$port."\n";

# 接続待ちをする
while($connection = socket_accept($socket)) {
  echo "Connecttion Start\n";
  # データを受信する
  while(($input = socket_read($connection, 1024))) {
    # 受信したデータが"exit"なら処理を終了する
    if (trim($input) == "exit") {
      break;
    }
    echo "Data: ".$input;
    # データを返送する
    socket_write($connection, "RET: ".$input);
  }
  echo "Connecttion Closed\n";
  # 接続を終了する
  socket_close($connection);
}
?>
