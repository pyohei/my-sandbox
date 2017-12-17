#!/bin/bash

PROGRAM_DIR=~/Programing
BACKUP_DIR=./.vim/bk
#BACKUP_DIR=~/.vim/bk

UNDO_PATTERN='*un~'
TILDA_PATTERN='*~'
SWAP_PATTERN='*.sw*'

if [ ! -e $BACKUP_DIR ]
then
    mkdir -p $BACKUP_DIR
fi

# Backup vim file.
backup() {
    FILES=$(find $1/ -type f -name "$2")
    for f in $FILES
    do
        FILE_PATH=`echo "$f" | sed -e "s/\/\// /g" | cut -d" " -f2`
        BK_DIR=${FILE_PATH%/*}
        BK_FILE=${FILE_PATH##*/}

        mkdir -p $3/$BK_DIR

        FROM_PATH=$1/$FILE_PATH
        TO_PATH=$3/$FILE_PATH

        if [ -e $TO_PATH ]
        then
            # Only run in Mac(Darwin).
            UPDATE_TIME=`ls -lUT resesh.sh | \
                sed -e 's/  */ /g' | \
                awk '{printf "%04d%02d%02d%s",$9,$6,$7,$8}' | \
                sed -e 's/://g'`
            mv $TO_PATH $TO_PATH.$UPDATE_TIME
        fi
        mv $FROM_PATH $TO_PATH
    done
}

backup $PROGRAM_DIR "$UNDO_PATTERN" $BACKUP_DIR
backup $PROGRAM_DIR "$TILDA_PATTERN" $BACKUP_DIR
backup $PROGRAM_DIR "$SWAP_PATTERN" $BACKUP_DIR
