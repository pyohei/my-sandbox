#!/bin/sh

# Logging tool.

. config.sh

logging() {
    LOGGING_DATETIME=`date "+%F %T"`
    echo "$LOGGING_DATETIME $1" >> $2
}

logging test /tmp/hoge.txt
