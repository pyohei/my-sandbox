#!/usr/bin/env ruby
require "socket"
require 'optparse'
require 'digest/sha1'

Version="0.0.1"
host = "127.0.0.1"  # ホストアドレス
port = 3000         # ポート番号
divide = 1          # 分割数
max_thread = 1      # 最大スレッド数
send_queue = [0]    # 送信キュー
packet_size = 1454  # バッファサイズ

debug = 0           # デバッグレベル

# UDPシーケンス制御用に追加するサイズ
SOCKETMANAGESIZE=80

retrycount= 0       # 送信リトライ回数
cdntgetq  = 0       # 送信キューが取れなかった回数

# 引数チェック
begin
  params = ARGV.getopts('d:','host:', 'port:', 'thread:', 'buffer:')
rescue OptionParser::ParseError => e
  puts e.message
  exit(-1)
end

if ARGV.length < 1
  puts "ファイルを指定してください"
  exit(-2)
end

filename = ARGV[0]

# ホスト名（IPアドレス）が指定されたか
if !params['host'].nil?
  host = params['host']
end

# ポート番号が指定されたか
if !params['port'].nil?
  port = params['port'].to_i
end

# スレッド数を指定されたか
if !params['thread'].nil?
  max_thread = params['thread'].to_i
  if max_thread > 16
    puts 'max threads adjusted to 16'
    max_thread = 16
  end
end

# キューサイズ
send_queue.clear
send_queue = Array.new(max_thread.to_i, 0)

# デバッグモード
debug = params['d'].to_i

# ソケット(UDP)をオープンする
begin
  _socket = UDPSocket.open()

  if !params['buffer'].nil?  # バッファサイズを指定されたか
    bsize = params['buffer'].to_i
    if bsize > 65535 # UDPパケット最大サイズを超えてないか確認する
      bsize = 65535
      puts 'send buffer size adjusted to 65535'
    end
    packet_size = bsize - SOCKETMANAGESIZE
  else
    packet_size = packet_size - SOCKETMANAGESIZE
  end

  # ソケットの送信バッファサイズを取得する
  sndbsize = _socket.getsockopt(Socket::SOL_SOCKET,Socket::SO_SNDBUF).int
  if sndbsize < 65535 # UDPパケット最大サイズより小さくないか
    _socket.setsockopt(Socket::SOL_SOCKET,Socket::SO_SNDBUF, 65535)
  end

  puts "packet send buffer size: #{packet_size}bytes"
rescue SocketError => e
  puts e.message
  exit(-4)
end

# ファイルの読み込み & ファイル分割
puts "reading file... " + filename
messages=[]
begin
  data = File.read(filename)
  divide = (data.length / packet_size.to_f).ceil
  divide.times do |i|
    messages << data[i*packet_size,packet_size]
  end
rescue => e
  puts e.message
  exit(-3)
end

# シーケンス制御用ダイジェスト
digest = Digest::SHA1.hexdigest(Time.now.to_s);

begin
  n = 0
  # 接続先アドレスとポートを指定しデータを送信(シーケンス制御用ヘッダー情報)
  puts "sending... host:#{host} port:#{port}"
  _socket.send(n.to_s + ":" + digest + ":" + messages.length.to_s, 0, host, port)
  # 必ず最初に到達させたいパケットなのでスリープを入れている
  sleep 0.1
  _socket.close
rescue SocketError => e
  puts e.message
  exit(-4)
end

# 送信メッセージ作成
messages.length.times {|i|
  messages[i] = i.to_s+":" + digest + ":" + messages[i]
}

threads = []

mutex = Mutex::new

m = messages.length

# max_threadで指定した数だけスレッドを開始
max_thread.times do |i|
  _port = port + i
  puts "create thread #{i}" if debug > 0
  threads << Thread.start { # スレッドを作成
    _queue = -1 # 定義だけしている
    puts "connection open #{i}" if debug > 0
    socket = UDPSocket.open()
    loop do
      # messageをひとつ取り出し。競合回避のためにsynchronizeで囲う
      message = mutex.synchronize { messages.pop }
      # messageがなくなればループを終了
      break unless message
      # 送信キューを取得する（取得できるまでトライする）
      loop do
        _queue = mutex.synchronize { send_queue.pop }
        break unless _queue.nil?
        cdntgetq += 1
        sleep 0.01
      end
      # 接続先アドレスとポートを指定しデータを送信
      n,x = message.split(":",2) # 送信シーケンス番号を取得

      while true
        print "sending... #{i}:#{n}/#{m} : #{message.length}byte port:#{_port}" if debug > 0
        begin
          block = socket.send(message, 0, host, _port)   # 本来ならblock数を確認すべき
        rescue Errno::ENOBUFS
          sleep 2
          puts  if debug > 0
          puts "resending... #{i}:#{n}/#{m} : #{message.length}byte port:#{_port}"  if debug > 0
          retrycount += 1
          next
        end
        puts " -> #{block}blocks sent." if debug > 0
        break
      end

      sleep 0.01 if debug > 1
      # 送信キューを戻す
      mutex.synchronize { send_queue << _queue }
    end

    sleep 0.01
    # ソケットをクローズする
    puts "connection closed #{i}"
    socket.close
  }
end

threads.each { |t| t.join }

exit(0)
