#!/bin/sh

# open sublime text 2
# if file doesn't exsist, make new file

# ==ATTENTION==
# This source is 

FILE_NAME=$1
PROGRAM="sublime Text 2"

if [ ! -e ${FILE_NAME} ]; then
    touch ${FILE_NAME}
fi

echo "opne ${FILE_NAME} -a ${PROGRAM}"

open ${FILE_NAME} -a "${PROGRAM}"