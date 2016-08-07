#!/usr/local/bin/python
#-*- coding: utf-8 -*-

"""
Create : 2014/02/02
print を使用したときにかかる時間を計るモジュール
1から、指定した数字までを1ずつprintする場合と、
最後の数字だけを表示する場合の時間を出力する。
「python2.7 print_calc xxxx（計りたい数字)」
で使用する事
"""

import sys
import datetime
import time
import os

class Print_calcuer:

    def main(self):
        if len(sys.argv) < 2:
            print "引数がありません。"
            raise
        if not sys.argv[1].isdigit():
            print "数値を入力してください。"
            raise
        last = int(sys.argv[1])
        if not os.path.exists("print_result"):
            os.mkdir("print_result")
        curDir = os.getcwd()
        curDay = datetime.datetime.now().strftime("%Y%m%d")
        fileName = curDir + "/print_result/" + curDay + ".txt"
        # print run
        start = time.time()
        for num in range(1, last+1):
            a = 1
            print num
        end = time.time()
        wasPrintTime = end - start
        # not print run
        start = time.time()
        for num in range(1, int(last+1)):
            a = 2
            pass
        end = time.time()
        wsaTime = end - start
        with open(fileName, "a") as resultFile:
            result = ("culculate time! [%s]\n"
                "number----%s\n"
                "time(print)----%s\n"
                "time(not_print)----%s\n"
                "difference---%s\n\n")%(
                str(curDay),
                str(last),
                str(wasPrintTime),
                str(wsaTime),
                wasPrintTime - wsaTime)
            resultFile.write(result)

# start in console
if __name__ == '__main__':
    p = Print_calcuer()
    p.main()


