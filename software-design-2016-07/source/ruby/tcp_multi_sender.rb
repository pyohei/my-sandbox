#!/usr/bin/env ruby
#
require "socket"
require 'optparse'

Version="0.0.1"
host = "127.0.0.1"  # ホストアドレス
port = 3000         # ポート番号
divide = 1          # 分割数
max_thread = 1      # 最大スレッド数
packet_size = 1454  # バッファサイズ
send_queue = [0]    # 送信キュー

debug=0             # デバッグレベル

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
    max_thread = 16
  end
end

# キューサイズ
send_queue.clear
send_queue = Array.new(max_thread.to_i, 0)

# バッファサイズを指定されたか
if !params['buffer'].nil?
  packet_size = params['buffer'].to_i
end

# デバッグモード
debug = params['d'].to_i

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

threads = []
mutex = Mutex::new
m = messages.length
begin

  max_thread.times do |i|
    puts "create thread #{i}"   if debug > 0
    # スレッドを作成
    threads << Thread.start { # スレッドを作成
      _queue = -1 # 定義だけしている
      puts "connection open #{i}"   if debug > 0
      socket = TCPSocket.open(host, port)
      loop do
        # messageをひとつ取り出し。競合回避のためにsynchronizeで囲う
        message = mutex.synchronize { messages.pop }
        # messageがなくなればループを終了
        break unless message
        # 送信キューを取得する（取得できるまでトライする）
        loop do
          _queue = mutex.synchronize { send_queue.pop }
          break unless _queue.nil?
          sleep 0.01
        end
        # データを送信
        print "sending... #{i} : #{message.length}byte" if debug > 0
        block = socket.write(message)   # 本来ならblock数を確認すべき
        puts " -> #{block}bolocks sent."    if debug > 0
        sleep 0.01 if debug > 1
        # 送信キューを戻す
        mutex.synchronize { send_queue << _queue }
      end
      # ソケットをクローズする
      puts "connection closed #{i}" if debug > 0
      socket.close
    }
  end

  # スレッドが全て終了するまで待つ
  threads.each {|t| t.join}
rescue => e
  puts e.message
end

exit(0)
