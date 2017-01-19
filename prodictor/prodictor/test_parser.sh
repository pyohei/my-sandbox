#!/bin/bash

# Black Box test for cron parser.
rm result.csv

python parser.py --start 20170114235959 --end 20170115060000

RESULT=`diff result.csv test/test_result.csv`

if [ -z $RESULT ]; then
    echo "Success!"
else
    echo "Failure! Your diff is below."
    echo ${RESULT}
fi
