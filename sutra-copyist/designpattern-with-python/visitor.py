#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# Created: 2014-04-19

def visit(visited, visitor):
    cls = visited.__class__.__name__
    meth = 'visit_%s' % cls
    method = getattr(visitor, meth, None)
    if method is not None:
        method(visited)

class vlist(list):
    def accept(self, visitor):
        visitor.visit_list(self)

class vdict(dict):
    def accept(self, visitor):
        visitor.visit_dict(self)

class Printer(object):
    def visit_list(self, ob):
        print 'list content :'
        print str(ob)
    def visit_dict(self, ob):
        print 'dict keys : %s' % ','.join(ob.keys())

if __name__ == "__main__":
    visit([1, 2, 5], Printer())
    visit({'one': 1, 'two': 2, 'three': 3}, Printer())
