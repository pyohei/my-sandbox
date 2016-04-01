#!/bin/bash

for n in `find ~/Programing/dev/ -type d -name '.git'`
do  
    PROJECT_DIR=`echo $n | sed -e "s/\/\//!!!!!/g" | sed -E "s/^.*!!!!!//g" | sed -e "s/\/.git//g"`
    PROJECT_NAME=`echo $PROJECT_DIR | awk -F / '{print $NF }'`
    echo $PROJECT_NAME
done
