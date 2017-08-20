#!/usr/local/bin/python
#-*- coding: utf-8 -*-

# Created: 2014/03/05
import imp
def adapter_for(protocol):
    adapter_name = "%sAdapter"%(protocol.capitalize(),)
    module_name  = "%s_adapter"%(protocol.lower(),)

    file, filename, description = imp.find_module(module_name, ["./"])
    module = imp.load_module(module_name, file, filename, description)
    print adapter_name
    adapter_class = getattr(module, adapter_name)
    print adapter_class
    # return adapter_class()

if __name__ == '__main__':
    a = "test"
    adapter_for(a)
    # print d
