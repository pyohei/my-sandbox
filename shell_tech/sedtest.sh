#!/bin/bash

find ./sample -type f | xargs sed -i.org -e "s|./hoge.html|./foo_hoge.html|g"
