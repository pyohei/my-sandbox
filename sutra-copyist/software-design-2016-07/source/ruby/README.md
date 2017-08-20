# Echoサーバ サンプルを動作させるには

1. サーバを起動します(使用したバージョンは2.2.3p173)
```
ruby echo_server.js
```
1.  ターミナルで以下のコマンドを実行します
```
telnet localhost 3000
```
1. 'exit'を入力するとサーバとの接続が解除されます

以上です

# データ送受信(TCP)サンプルを動作させるには

1. サーバを起動します(使用したバージョンは2.2.3p173)
```
ruby tdp_receive_server.rb --host=0.0.0.0 --port=3000
[option]
--host: 受信に使用するホスト名またはIPアドレス
--port: 受信に使用するポート番号
```

1. クライアント(シングルタスク)を起動します
```
ruby tcp_single_sender.rb --host=127.0.0.1 --port=3000 --split=8 hoge.txt
--host: 送信先ホスト名またはIPアドレス
--port: 送信先ポート番号
--split: ファイルの分割数
hoge.txt: 送信するファイル名
```

1. クライアント(マルチタスク)を起動します
```
ruby tcp_multi_sender.rb --host=127.0.0.1 --port=3000 --thread=8 hoge.txt
--host: 送信先ホスト名またはIPアドレス
--port: 送信先ポート番号
--thread: スレッド数(分割数)
hoge.txt: 送信するファイル名
```

# データ送受信(UDP)サンプルを動作させるには

1. サーバを起動します(使用したバージョンは2.2.3p173)
```
ruby udp_receive_server.rb --host=0.0.0.0 --port=3000 -s
[option]
--host: 受信に使用するホスト名またはIPアドレス
--port: 受信に使用するポート番号
-s: シーケンス制御をする
```

1. クライアント(シングルタスク)を起動します
```
ruby udp_single_sender.rb --host=127.0.0.1 --port=3000 --split=8 hoge.txt
--host: 送信先ホスト名またはIPアドレス
--port: 送信先ポート番号
--split: ファイルの分割数
hoge.txt: 送信するファイル名
```

1. クライアント(マルチタスク)を起動します
```
ruby udp_multi_sender.rb --host=127.0.0.1 --port=3000 --thread=8 hoge.txt
--host: 送信先ホスト名またはIPアドレス
--port: 送信先ポート番号
--thread: スレッド数
hoge.txt: 送信するファイル名
```

# 実装メモ

## UDP送信(udp_multi_sender.rb)で起こったこと

### 1. sendtoで 'message too long' が発生

原因：大きなファイルを特定の数に分割して送信するロジックを実装したがsendtoへ一度に渡すデータサイズが大きすぎてエラーが発生していた

対策：getsockopt関数で送信バッファサイズを取得し、そのサイズ内に収まるよう加筆修正をおこなった

### 2. sendtoで 'message too long' が発生

原因：上記対策をおこなったが、対策が不十分でUDPパケットの最大送信長（65535byte）を超えてしまっていたためエラーが発生していた

対策：送信データサイズを最大送信長を超えないよう加筆修正をおこなった

### 3. sendtoで 'too many open files' が発生

原因：上記対策をおこなった結果、スレッドが作成される量が増えたためファイルディスクリプタ数が制限を超えてしまったためエラーが発生していた

対策：スレッド数を無制限に増やすのではなく対向サーバのスレッド数に合わせられるように修正し、分割したメッセージをキューとみなして動作するよう加筆修正をおこなった

### 4. sendtoで 'message too long' が発生

原因：上記対策をおこなったが、送信バッファサイズ(UDPのパケットサイズではない)以上の送信要求をしてしまっていたためエラーが発生していた

対策：マルチスレッドでも一度に送信できる個数を制限できるよう加筆修正をおこなった