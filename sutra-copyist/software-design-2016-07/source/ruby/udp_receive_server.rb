#!/usr/bin/env ruby
#
require 'socket'
require 'optparse'
require 'digest/sha1'

Version="0.0.1"
# デフォルトホストアドレス
host = "127.0.0.1"
# デフォルトポート番号
ports = [*3000..3016]
# 受信バッファサイズ(512M)
maxlen = 1024 * 1024 * 512

# シーケンス制御時用データ保存ワークデータ
seqdata = {}

# 引数チェック
begin
  params = ARGV.getopts('sd','host:', 'port:', 'len:')
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
  ports = []
  params['port'].split(',').each {|port|
    ports.push(port.to_i)
  }
end

# バッファ受信サイズが指定されたか
if !params['len'].nil?
  maxlen = params['len'].to_i
end

# シーケンスモード
seqcntl = params['s']

# デバッグモード
dump = params['d']

if seqcntl
  puts "SequenceMode"
end

puts "Server Start - MaxDataReceiveSize: #{maxlen}"

begin
  ports.each do |port|
    # ソケット（UDP）をオープンする
    _socket = UDPSocket.open()
    # 待受アドレスとポートを指定する
    _socket.bind(host, port)
    puts "bind - #{host}:#{port}"

    # スレッドを起動する
    Thread.start(_socket) do |socket|
      while true
        # ソケットの読み取りが可能になるまで待つ
        IO.select([socket])
        # 処理開始時刻取得
        starttime = Time.now.instance_eval { self.to_i * 1000 + (usec/1000) }
        # データを受信する
        buffer, addr = socket.recvfrom_nonblock(maxlen)
        if seqcntl
          # シーケンス制御あり
          seq, digest, data = buffer.split(':', 3)
          puts "#{addr[2]}:#{addr[1]} >> seq: #{seq} length: #{buffer.length}"
          if seqdata[digest].nil?
            seqdata[digest] = Array.new(data.to_i)
            puts "last sequence no: #{data}"
          else
            seqdata[digest][(seq.to_i) - 1] = data
            if seqdata[digest].all?
              puts "all received - #{addr[2]}:#{addr[1]}"
              seqdata.delete(digest)
            end
          end
        else
          # シーケンス制御なし
          puts "#{addr[2]}:#{addr[1]} >> length: #{buffer.length}"
        end
        # 処理終了時刻取得
        endtime = Time.now.instance_eval { self.to_i * 1000 + (usec/1000) }
        # 処理時間算出(ミリ秒)
        interval = endtime - starttime
        puts "processing #{interval} msec"
      end
    end
  end
  # メインスレッドが処理終了しないよう無限ループに
  while true
    sleep(1000)
  end
rescue Interrupt
  # Ctrl-C で終了する
rescue => e
  p e
end

puts "Server closed"
