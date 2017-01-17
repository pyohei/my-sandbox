#!/bin/sh

# Logging tool.

# Load config file.
. config.sh


LOG_FILE_PATH=

# Init logging
#   $1 ... Log dir name
createLogging() {
    if [ ! -e $1 ]; then
        mkdir -p $1
    fi
    local log_name=`date +"%Y%m%d"`
    LOG_FILE_PATH=$1/${log_name}.log
    if [ ! -e ${LOG_FILE_PATH} ]; then
        touch ${LOG_FILE_PATH}
    fi
}


# Logging process.
#   $1 ... Message for logging.
logging() {
    if [ ! -e ${LOG_FILE_PATH} ]; then
        echo "Log file is not found. You should call 'createLogging')"
        exit 1
    fi
    LOGGING_DATETIME=`date "+%F %T"`
    echo "$LOGGING_DATETIME $1" >> ${LOG_FILE_PATH}
}
