#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
This module is test code for excel.py
Separate with test unit to test simply.
"""

from excel import *

def test_reader():
    w = Reader("/Users/mukaishohei/programing/Python/lib/excel/test.xls")
    print w.load_sheet_names()
    print w.calc_sheet_number()
    h = w.extract_header()
    for hh in h:
        print hh
    cs = w.get_all_cell()
    for css in cs:
        for csss in css:
            print csss
    print w.get_cell_value(1,1)
    g = w.generate_cell()
    print g.next()
    print g.next()

def test_writer():
    t = Writer("./tests.xls")
    t.make_sheet("test_sheet")
    t.write_a_rows(0, [["test",u"てすと"],["test1", u"てすた"]])
    t.make_sheet("test_sheet2")
    t.write_a_rows(0, [["test",u"てすと"],["test1", u"てすた"]])
    t.save()
    print ("MRO:", [x.__name__ for x in Editor.__mro__])

def test_editor():
    e = Editor('./test.xls')
    e.select_sheet('test')
    e.modify_cell_value(0, 0, u"変更")
    e.modify_cell_values(1, [u"変更","test"])
    e.save()

if __name__ == "__main__":
    test_editor()
