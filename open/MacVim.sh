#!/bin/sh

# open sublime text 2
# if file doesn't exsist, make new file

FILE_NAME=$1
PROGRAM="MacVim"

if [ ! -e ${FILE_NAME} ]; then
    touch ${FILE_NAME}
fi

echo "opne ${FILE_NAME} -a ${PROGRAM}"

open ${FILE_NAME} -a "${PROGRAM}"