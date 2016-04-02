#!/bin/bash

# Input your base directory.
BASE_DIR=~/Programing/dev/ 
CACHE_DIR=`pwd`/.cache
CACHE_FILE=`pwd`/.cache/projects.txt

# Echo help
echo_help() {
    echo "Usage: command [-p ProjectNo] [-l]" 2>&1
    exit 1
}

echo_projects() {
    LINE_NO=1
    cat $CACHE_FILE | while read LINE; do
        PROJECT_NAME=`echo $LINE| awk -F / '{print $NF }'`
        echo $LINE_NO: $PROJECT_NAME
        LINE_NO=`expr $LINE_NO + 1`
    done
}

go_project() {
    PROJECT_NO=$1
    expr $PROJECT_NO + 1 > /dev/null 2>&1
    if [ \( $? -ge 2 \) -o $PROJECT_NO -eq 0 ]; then
        echo "You must indicate project no as integer."
        echo_help
        exit 1
    fi
    LINE_NO=1
    GO_DIR=
    while read TMP_PROJECT_DIR; do
        if [ $LINE_NO -eq $PROJECT_NO ]; then
            GO_DIR=$TMP_PROJECT_DIR
        fi
        LINE_NO=`expr $LINE_NO + 1`
    done < $CACHE_FILE
    if [ -z $GO_DIR ]; then
        echo "Your project no is out of all."
        echo_help
        exit 1
    else
        cd $BASE_DIR$GO_DIR
    fi
}

# Parse Options.
# You need to ":" when argments is needed.
OPT=
while getopts "p:hl" OPT
do
    case $OPT in
        l) echo_projects
            ;;
        p) go_project $OPTARG
            ;;
        h) echo_help
            ;;
        \?) echo_help
            ;;
    esac
done
