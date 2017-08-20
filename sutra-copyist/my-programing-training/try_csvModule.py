#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# Created: 2014/04/22
# test csv module to make csv wrapper.


import csv

class csvInit:
    delimiter = "p"

class csvHandler(csv.Dialect):
    def __init__(self):
        self.delimiter = " "

def main():
    csv.register_dialect("p_test", delimiter='|')
    print csv.list_dialects()
    w = csv.writer(open("csv_test.csv", "wb"), dialect="p_test")
    w.writerows(["aobdca","adfevasb","sssssvac"])

    #これでなんとか動いている。
    #しかし、もう少し工夫したコードが書けるような。。。

if __name__ == '__main__':
    print csv.list_dialects()
   # c = csvHandler()
   # c.main()
    main()
