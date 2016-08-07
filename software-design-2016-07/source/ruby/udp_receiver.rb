#!/usr/bin/env ruby
require "socket"

host = "127.0.0.1"
port = 3000

receiver = UDPSocket.open()

receiver.bind(host, port)

puts 'ReceiverStart:'+host+":"+port.to_s

# データ宣言兼初期化
n = 0
m = 0
datas = []

loop do
  seq, data = receiver.recv(65535).split(':')
  if seq.to_i == 0 then
    # データ個数取得
    m = data.to_i
  else
    # データ取得
    # (受信データの順番が入れ替わる可能性があるのでその対応)
    datas[seq.to_i]=data
  end
  if m == n then
    break;
  end
  n += 1
end

p datas.join('')

receiver.close
