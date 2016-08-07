# -*- coding: utf-8 -*-
#
from __future__ import print_function
import sys
import socket
from contextlib import closing

def main():
  argv = sys.argv
  argc = len(argv)

  # ホストアドレス
  host = '127.0.0.1'
  # ポート番号
  port = 3000
  # 受信バッファサイズ
  bufsize = 4096

  # 引数をチェック
  if argc == 3:
    port = int(argv[2])
    host = argv[1]
  elif argc == 2:
    host = argv[1]

  # ソケット作成
  sock = socket.socket(socket.AF_INET,
                    socket.SOCK_STREAM)
  # ソケットがクローズされるまでループする
  with closing(sock):
    # サーバに接続する
    sock.connect((host, port))

    while True:
      # キーボードからのタイプ待ち
      sys.stdout.write("input-> ")
      line = sys.stdin.readline()
      # 空行だと終了させる
      if len(line.rstrip()) == 0:
        break
      # キーボードからの入力を送信する
      sock.send(line.encode('utf-8'))
      # 入力文字列が'exit'だと終了させる
      if line.rstrip()=='exit':
        break;
      # サーバからのデータを受信する
      print(sock.recv(bufsize).rstrip())
  return

if __name__ == '__main__':
  main()
