#!/usr/bin/env ruby

require "socket"

# ホストアドレス
host = "127.0.0.1"
# ポート番号
port = 3000

# ソケットをオープンし待受アドレスとポートを指定する
#（関数内部でsocket/bindを同時に実行している）
server = TCPServer.open(host, port)

puts 'ServerStart:'+host+":"+port.to_s

while true
  # スレッドを作成し、ソケットへの接続を待つ(関数内部でlisten/acceptを連続して実行している)
  Thread.start(server.accept) do |socket|
    # 接続がされたら処理を実行する
    puts 'Connecttion Start'
    # ソケットからデータを受信する
    while buffer = socket.gets
      if buffer.strip == "exit"
        # データが"exit"なら処理終了する
        break
      end
      puts socket.peeraddr[2]+":"+socket.peeraddr[1].to_s+">"+buffer.strip
      # 受信したデータを返送する
      socket.puts "RET: " + buffer
    end
    puts 'Connecttion Closed'
    # ソケットをクローズする
    socket.close
  end
end
# メインソケットをクローズする
server.close
