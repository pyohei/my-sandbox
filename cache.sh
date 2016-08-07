#!/bin/bash

# Input your base directory.
BASE_DIR=${HOME}/Programing 
CACHE_DIR=`dirname $0`/.cache
CACHE_FILE=`dirname $0`/.cache/projects.txt

# Backup cache.
if [ ! -e $CACHE_DIR ]; then
    mkdir -p $CACHE_DIR
else
    if [ -e $CACHE_FILE ]; then
        mv $CACHE_FILE $CACHE_DIR/project-`date "+%Y%m%d%H%M%S"`.txt
    fi
fi

# Find project directoiesl.
for n in `find $BASE_DIR -type d -follow -name '.git'`
do  
    PROJECT_DIR=`echo $n | sed -e "s/\/\//!!!!!/g" \
        | sed -E "s/^.*!!!!!//g" | sed -e "s/\/.git//g"`
    echo $PROJECT_DIR >> $CACHE_FILE
done
