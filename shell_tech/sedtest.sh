#!/bin/bash

find ./sample -type f -print0 | xargs -0 sed -e -i "s|./hoge.html|./foo_hoge.html|g"
