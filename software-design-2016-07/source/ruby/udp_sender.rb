#!/usr/bin/env ruby

require "socket"

host = "127.0.0.1"
port = 3000

# ファイルの読み込み(５文字づつ分割をする)
texts = File.read("hoge.txt",
  :encoding => Encoding::UTF_8).scan(/.{1,5}/)

# 送信用ソケットアドレスを設定
sockaddr = Socket.pack_sockaddr_in(port, host)
sender = UDPSocket.open()
puts 'SenderStart:'+host+":"+port.to_s

# ファイル転送（シーケンス番号を使った独自プロトコル）
# 送信個数を送る(シーケンス番号は０番)
n = 0
sender.send(n.to_s+":"+texts.count.to_s,
            0, sockaddr)
# 分割メッセージを送る(シーケンス番号は１番から)
texts.each{|text|
  n += 1
  sender.send(n.to_s + ":" + text,
              0, sockaddr)
}
# 送信完了
sender.close
