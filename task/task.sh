#!/bin/sh

# Created: 2014-03-29

#タスク管理をするシェルファイル。
# 使用例 -> sh task.sh -*
# -l --list でタスクを一覧する。
# -a --append でタスクを追加する。
# -d --delete でタスクを論理削除する。

# status（番号の次）で判定するようにしよう
# 0 -> 進行中
# 1 -> 達成
# 9 -> 削除（論理）
# 3 -> ストップ

HOME_DIR=`pwd`
CMDNAME=`basename $0`
USAGE="Usage: $CMDNAME [-signal] [taskNo] "
USAGE_EXPLAIN="PREASE CONFIRM OPTION WITH -h "
LIST_DIR=${HOME_DIR}/list
LIST_FILE=taskList.txt
LOG_DIR=${HOME_DIR}/log
LOG_FILE="task2014.log"

# init flag for judging command
DELETE=0
ADD=0
LIST=0
FINISH=0
STOP=0
VIEW=0

writeLog(){
    COMMENT=$1
    WRITE_TIME=`date +"%Y%m%d%H%M%S"`
    echo "${WRITE_TIME}  ${COMMENT}" >> $LOG_DIR/$LOG_FILE
}

if [ $# -eq 0 ] ; then
    echo ${USAGE}
    echo ${USAGE_EXPLAIN}
fi


while getopts dalfsvh OPT
do
    case $OPT in
        d) DELETE=1
            ;;
        a) ADD=1
            ;;
        l) LIST=1
            ;;
        f) FINISH=1
            ;;
        s) STOP=1
            ;;
        v) VIEW=1
            ;;
        h|help) cat ${HOME_DIR}/README.md
            ;;
        \?) echo ${USAGE} 1>&2
            exit
    esac
done

# confirm option code
if [[ ! $1 =~ -* ]] ; then
    echo $USAGE
    exit
fi

# make directory
if [ ! -e $LIST_DIR ]
then
     mkdir $LIST_DIR
fi

# move list file directory
cd $LIST_DIR

# make list file
if [ ! -e $LIST_DIR/$LIST_FILE ]
then
    touch $LIST_DIR/$LIST_FILE
fi

# make log file
if [ ! -e $LOG_DIR ]
then
     mkdir $LOG_DIR
fi

if [ ! -e $LOG_DIR/$LOG_FILE ]
then
    touch $LOG_DIR/$LOG_FILE
fi

# start
writeLog "----START----"

# View all contents
if [ $VIEW -eq 1 ] ; then
    echo "----all task-----"
    echo LOOK FILE $LIST_DIR/$LIST_FILE
    cat $LIST_DIR/$LIST_FILE
    writeLog "Look all contents"
    writeLog "----END----"
    exit
fi

# add task
if [ $ADD -eq 1 ]; then
    if [ $FINISH -eq 1 -o $DELETE -eq 1 -o $STOP -eq 1 ] ; then
        echo "YOUR OPTION IS WRONG"
    fi
    LAST_NO=`wc -l ./taskList.txt | tail -n 1 | sed -e 's/^ *//' | cut -f 1 -d ' '`
    TASK=$2
    if [ -z $2 ] ; then
        echo "NEED TASK NAME!"
    else
        NEW_NO=`expr $LAST_NO + 1`
        echo $NEW_NO,0,$TASK >> $LIST_DIR/$LIST_FILE
    fi
    writeLog "Add task ${TASK}"
fi

# definition of changing flag
chkFlag()
{
    IS_CHK=$1
    CHK_LINE=$2
    VALUE=$3
    if [ $1 -eq 1 ]; then
        if [ -z $2 ] ; then
            echo "need task No"
            exit
        fi
        TASK_NUM=$2
        sed -i -e ${TASK_NUM}s/,0,/,${3},/ ./taskList.txt
    fi
}

# task finish
if [ $FINISH -eq 1 ]; then
    chkFlag 1 $2 1
    writeLog "Finish task no $2"
fi

# task stop
if [ $STOP -eq 1 ]; then
    chkFlag 1 $2 3
    writeLog "Stop task no $2"
fi

#task delete
if [ $DELETE -eq 1 ]; then
    chkFlag 1 $2 9
    writeLog "Delete task no $2"
fi

# display task
if [ $LIST -eq 1 ]; then
    for LINE in $(cat $LIST_DIR/$LIST_FILE)     # これは覚えておこう
    do
        NO=`echo $LINE | cut -d ',' -f 1`
        INVALID=`echo $LINE | cut -d ',' -f 2`
        TASK=`echo $LINE | cut -d ',' -f 3`
        if [ $INVALID -eq 0 ]
        then
            echo $NO, $TASK
        fi
    done
    writeLog "Display task list"
fi

writeLog "-----END----"

