#!/usr/bin/env ruby
#
require "socket"
require 'optparse'

Version="0.0.1"
# デフォルトホストアドレス
host = "127.0.0.1"
# デフォルトポート番号
port = 3000
# 受信バッファサイズ(512M)
maxlen = 1024 * 1024 * 512

# 引数チェック
begin
  params = ARGV.getopts('d','host:', 'port:', 'len:')
rescue OptionParser::ParseError => e
  puts e.message
  exit(-1)
end

# ホスト名（IPアドレス）が指定されたか
if !params['host'].nil?
  host = params['host']
end

# ポート番号が指定されたか
if !params['port'].nil?
  port = params['port'].to_i
end

# バッファ受信サイズが指定されたか
if !params['len'].nil?
  maxlen = params['len'].to_i
end

# デバッグモード
dump = params['d']

# ソケット(TCP)をオープンし待受アドレスとポートを指定する（関数内部でsocket/bindを同時に実行している）
socket = TCPServer.open(host, port)
# listenでbacklogの値を設定する
socket.listen(16)

puts "Server Start - #{host}:#{port}"
begin
  while true
    # スレッドを作成し、ソケットへの接続を待つ
    Thread.start(socket.accept) do |connection|
      # ソケットに接続がされたら以下の処理を実行する
      puts "Connecttion Start - #{connection.peeraddr[2]}:#{connection.peeraddr[1]}"
      starttime = Time.now.instance_eval { self.to_i * 1000 + (usec/1000) }
      # コネクションからデータをブロックモードで受信する ソケットが切断されるまで受信を続ける
      while buffer = connection.read(maxlen)
        puts "#{connection.peeraddr[2]}:#{connection.peeraddr[1]} >> length: #{buffer.length}"
        if dump
          puts "data: #{buffer}"
        end
      end
      puts "Connecttion Close - #{connection.peeraddr[2]}:#{connection.peeraddr[1]}"
      # コネクションをクローズする
      connection.close
      endtime = Time.now.instance_eval { self.to_i * 1000 + (usec/1000) }
      interval = endtime - starttime
      puts "processing #{interval} msec"
    end
  end
rescue Interrupt
rescue => e
  p e
end
# ソケットをクローズする
socket.close
puts "Server closed - #{host}:#{port}"
