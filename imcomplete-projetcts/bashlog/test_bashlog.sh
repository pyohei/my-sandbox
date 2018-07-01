#!/bin/bash

# Test of bashlog.sh

. bashlog.sh

createLogging /tmp/test1
logging hoge
logging foo
logging bar
