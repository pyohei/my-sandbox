#!/usr/bin/env bash
#

if [ $# -lt 5 ]; then
  echo 'argument must be 5, but ' $#
  echo "usage : ${0} [u|t] <file> <target> <# of processes> <snd_buf_size>"
  exit 1
fi

# 最初の引数が't'ならTCP、'u'ならUDPで送信する
if [ $1 == 't' ]; then
  TYPE='t'
  CMD='./tcp_multi_sender.rb'
elif [ $1 == 'u' ]; then
  TYPE='u'
  CMD='./udp_multi_sender.rb'
else
  echo "invalid parameter"
  echo "usage : ${0} [u|t] <file> <target> <# of processes>"
  exit 1
fi

shift # 引数を一つずらす
FILE=$1 # 2nd argument is the file name

shift
TARGET="-h ${1}" # 3rd argument is the target host

shift
NUMPROC=$1 # 4th argument is the number of processes

shift
SNDBUF="-b ${1}" # 5th argument is the send buffer size

# 入力ファイルを分割する
S_SIZE=`(ls -l ${FILE} | awk  "{print int(\\$5 / ${NUMPROC})}"  )`
#echo $S_SIZE

if [ `ls x?? | wc -l` -ne 0 ]; then
  echo 'temporary files already exist' 
  ls x??
  echo 'cleanup em!'
  exit 2
fi

echo "splitting ${FILE}"
split -b ${S_SIZE} ${FILE}

echo "Start !"

# ポート番号
p=3000

# yeilds NUMPROC processes
#while [ $NUMPROC -gt 0 ]
for i in x??
do
  # UDPの場合、ポート番号を指定する
  if [ $TYPE == 'u' ]; then
    PORT="-p ${p}"
  fi
  # 処理をバックグラウンドで実行
  echo "ruby ${CMD} ${PORT} ${SNDBUF} ${TARGET} ${i}"
  ruby ${CMD} ${PORT} ${SNDBUF} ${TARGET} ${i} &

  # ポート番号をずらす
  p=`expr $p \+ 1`

  #NUMPROC=`expr $NUMPROC - 1`

done

# バックグラウンド処理が全て終了するまで待機する
wait

echo "End !"

echo "cleanup temporary files"
rm x??

