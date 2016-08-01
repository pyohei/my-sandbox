#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
created 2014/05/11

This module is wrapper of xml.
To use, you must write method named 'parse'.

"""


import xml.etree.ElementTree as tree

class Parser(object):

    def __init__(self, file):
        self.file = file

    def parse(self):
        self.tree = tree.ElementTree()
        self.tree.parse(self.file)

    def find_tag(self,tag):
        return self.tree.find(tag)

    #usually this method don't use
    def fetch_tree(self):
        return self.tree

    def dug_root(self):
        return self.tree.getroot()

    # developing...
    def generate_branch(self):
        for r in self.root:
            yield r.text

    # this module probubly unneccesary
    def find_branch(self, tag):
        for r in self.root:
            print r.tag
            print r.find(tag).text

    def yeild_branch(self):
        return self.tree.iter()

    def yeild_tag_values(self, tag_name):
        for e in self.tree.getroot():
            yield e.find(tag_name).text

    # return object that can use as dictionary
    def load_keys(self, tag_name, value):
        for r in self.tree.getroot():
            if r.get(tag_name) == value:
                return r

    def extract_trees_by_attr(self, element, attr, value):
        l = []
        for r in element:
            if r.get(attr) == value:
                l.append(r)
        return l

    def extract_trees_by_tag(self, element, tag_name):
        l = []
        for e in element:
            if e.tag == tag_name:
                l.append(e)
        return l

    def extract_texts(self, element):
        l = {}
        for e in element:
            l[e.tag] = e.text
        return l

    def modify_attrib(self, element, attr, content):
        element.attrib[attr] = content

    def modify_text(self, element, content):
        element.text = content

    def modify_tag(self, element, content):
        element.tag = content

    def write_new(self, file_name=""):
        if file_name== "":
            file_name = self.file
        self.tree.write(file_name)

    def delete_element(self, element):
        element.clear()

    # not only tag, can use pass
    def extract_mach_tag(self, tag_name):
        return self.tree.findall(tag_name)

    def extract_text_by_tag(self, tag_name):
        return self.tree.findtext(tag_name)

    def generate_all_text(self):
        return self.tree.itertext()

if __name__ == '__main__' :
    p = Parser('test/xmlsample.xml')
    p.parse()
    #t = p.extract_mach_tag('book/title')
    #print t
    #u = p.extract_text_by_tag('book/title')
    #print u
    r = p.dug_root()
    l = p.extract_trees_by_attr(r, 'id', 'bk112')
    e = p.extract_trees_by_tag(l[0], 'genre')
    ee = p.extract_trees_by_tag(l[0], 'author')
    p.delete_element(ee[0])
    p.modify_attrib(e[0], 'mukai', 'mukai')
    p.modify_tag(e[0], 'testt')
    p.modify_text(e[0], 'yes')
    p.write_new('test/test.xml')
