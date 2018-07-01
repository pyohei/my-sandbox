#!/bin/bash

# This is tool like twitter.
# Usage: "sh writeMyThink.sh xxxxx"
# "xxx" is your thinking to save.
# Automatically, your comments are recorded in the file each day.

# directory making file
DIR=~/99.diary/thinking
#DIR=xxxxxxxxxxxxx
TODAY_FILE=`date '+%Y%m%d'`.log
WRITE_TIME=`date '+%Y%m%d%H%M%S'`
COMMENT=

# make directory
if [ ! -d $DIR ]
then
    mkdir -p $DIR
    echo "made directory"
fi

# move directory
cd $DIR

# connect multi input.
for comment in $@
do
    COMMENT+=$comment" "
done
COMMENT=`echo $COMMENT | sed -e "s/.¥[1¥]$//"`

# save comment
echo [$WRITE_TIME]" "$COMMENT >> $TODAY_FILE
