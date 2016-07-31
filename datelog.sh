#!/bin/bash

echoLog () {
    echo `date +'[%Y-%m-%d %H:%M:%S]'` $*
}

LOG_NAME=test_log.log

touch $LOG_NAME
echoLog "test" >> $LOG_NAME
echoLog "test2" "test3" >> $LOG_NAME
