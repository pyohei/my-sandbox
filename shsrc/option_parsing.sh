#!/bin/bash

SUFFIX=ho

OPTION=$*

while getopts "d:" OPT
do
    case $OPT in
        d) SUFFIX=$OPTARG
            ;;
        \?) ;;
    esac
done > /dev/null 2>&1

echo "Suffix"
echo $SUFFIX

echo "Option"
echo $OPTION
