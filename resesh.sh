#!/bin/bash

PROGRAM_DIR=~/Programing
BACKUP_DIR=~/.vim/bk

UNDO_DIR_NAME=undo
UNDO_PATTERN='*~'

TILDA_DIR_NAME=tilda


SWAP_DIR_NAME=swap


#mkdir -p $BACKUP_DIR/$UNDO_DIR_NAME
#mkdir -p $BACKUP_DIR/$TILDA_DIR_NAME
#mkdir -p $BACKUP_DIR/$SWAP_DIR_NAME

FILES=$(find $PROGRAM_DIR/ -type f -name "$UNDO_PATTERN")

for f in $FILES
do
    FILE_PATH=`$f | sed -e "s/\/\// /g" | cut -d" " -f2`
done
