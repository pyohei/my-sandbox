#!/bin/bash

# Input your base directory.
BASE_DIR=~/Programing/dev/ 
CACHE_DIR=`pwd`/.cache
CACHE_FILE=`pwd`/.cache/projects.txt

# Backup cache.
if [ ! -e $CACHE_DIR ]; then
    mkdir -p $CACHE_DIR
else
    if [ -e $CACHE_FILE ]; then
        mv $CACHE_FILE $CACHE_DIR/project-`date "+%Y%m%d%H%M%S"`.txt
    fi
fi

# Find project directoiesl.
for n in `find $BASE_DIR -type d -name '.git'`
do  
    PROJECT_DIR=`echo $n | sed -e "s/\/\//!!!!!/g" | sed -E "s/^.*!!!!!//g" | sed -e "s/\/.git//g"`
    PROJECT_NAME=`echo $PROJECT_DIR | awk -F / '{print $NF }'`
    echo $PROJECT_NAME >> $CACHE_FILE
done
