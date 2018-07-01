#!/bin/bash

DIR=$(cd $(dirname $0); pwd)
echo $DIR

python $DIR/test_exe.py
