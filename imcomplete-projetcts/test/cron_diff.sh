#!/bin/sh

crontab -l > /tmp/crontab_now.txt
# diff argment is `old` `new`
diff -u /tmp/crontab_now.txt /tmp/crontab_org.txt > /tmp/cron_diff.txt
