#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
This module is to operate excel-file simply.
How to use:
 See excel_test.py.

ATTENTION
 the vriable value 'self.book' is used All class.
 Be careful what value in it!
"""

import os
import xlwt
import xlrd
import xlutils
from xlutils.copy import copy as u_copy

class Reader(object):

    def __init__(self, file_path):
        self.r_book = xlrd.open_workbook(file_path)

    # return sheet name ([])
    def load_sheet_names(self):
        return self.r_book.sheet_names()

    # return numbers of sheet (int)
    def calc_sheet_number(self):
        return self.r_book.nsheets

    # extract header ([])
    def extract_header(self, sheet_name=""):
        if not sheet_name:
            sheet = self.r_book.sheet_by_index(0)
        sheet = self.r_book.sheet_by_index(sheet_name)
        header = []
        for col in range(sheet.ncols):
            header.append(sheet.cell(0,col).value)
        return header

    ##---ATTENTION---##
    # if you load much cell, you shouldn't use this method!
    # in future, I want to extinguish this method.
    def get_all_cell(self, sheet=0):
        sheet_index = self.r_book.sheet_by_index(sheet)
        col = sheet_index.ncols
        row = sheet_index.nrows
        cell_values = []
        for r in range(row):
            cell_value = []
            for c in range(col):
                cell_value.append(sheet_index.cell(r, c).value)
            cell_values.append(cell_value)
        return cell_values

    # get specific cell value
    def get_cell_value(self, row, col, sheet=0):
        sheet_index = self.r_book.sheet_by_index(sheet)
        return sheet_index.cell(row, col).value

    # generate cell value by generater.
    # to fetch next, user "@@.next()"
    def generate_cell_values(self, sheet=0):
        sheet_index = self.r_book.sheet_by_index(sheet)
        col = sheet_index.ncols
        row = sheet_index.nrows
        for r in range(row):
            cell_value = []
            for c in range(col):
                cell_value.append(sheet_index.cell(r, c).value)
            yield cell_value

class Writer(object):

    def __init__(self, file_path):
        self.file_path = file_path
        self.w_book = xlwt.Workbook()

    def make_sheet(self, sheet_name="sheet"):
        self.book_writer = self.w_book.add_sheet(sheet_name)

    def write_a_row(self, row, values):
        w_row = self.book_writer.row(row)
        for n, v in enumerate(values):
            w_row.write(n, v)

    def write_a_rows(self, from_row, values):
        for n in range(from_row, len(values)):
            self.__write(self.book_writer, n, values[n])

    def __write(self, writer, row_num, values):
        w = writer.row(row_num)
        for n, v in enumerate(values):
            w.write(n, v)

    def write_header(self, values):
        w_row = self.book_writer.row(0)
        for n, v in enumerate(values):
            w_row.write(n, values[n])

    def write_a_cell(self, row, col, value):
        self.book_writer.write(row, col, value)

    def save(self):
        self.w_book.save(self.file_path)

class Editor(Reader, Writer):

    def __init__(self, file_path):
        if not os.path.exists(file_path):
            raise IOError("%s doesn't exist."%(file_path))
        self.file_path = file_path
        Reader.__init__(self, self.file_path)
        self.w_book = u_copy(self.r_book)

    def select_sheet(self, sheet_name="sheet"):
        b = self.r_book
        i = [s.name for s in b.sheets()].index(sheet_name)
        self.book_writer = self.w_book.get_sheet(i)

    def modify_cell_value(self, row, col, value):
        self.write_a_cell(row, col, value)

    def modify_cell_values(self, from_row, values):
        self.write_a_row(from_row, values)

if __name__ == "__main__":
    pass
