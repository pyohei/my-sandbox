# -*- Coding: utf-8 -*-

a = {"A": {"B": [1,2,3,4,5,6], "C": {"D": [1,2,3,4,5], "E": "X", "F": {"G": [1,2,3,4,5], "H": [1,2,3,4,5]}},"I": "XY"}}


def hoge(a):
    def _hoge(a):
        value = ""
        for k, v in a.items():
            if isinstance(v, list):
                for vv in v:
                    value += str(vv)
                    _hoge(a)
        if not isinstance(v, dict):
            print v
        else:
            _hoge(v)
    _hoge(a)


def catch_list(a):
    my_list = {}
    def _search_list(a, ml):
        for k, v in a.items():
            if isinstance(v, list):
                ml[k] = v
            if isinstance(v, dict):
                ml[k] = {}
                #print ml, v
                _search_list(v, ml[k])
        return ml
    return _search_list(a, my_list)

selections = catch_list(a)
print selections

def print_all(a):
    def _re_print(a):
        next_dict = {}
        cur_lists = []
        for k, v in a.items():
            if isinstance(v, list):
                cur_lists.append(v)
