"""Gather values by excel sheets, and write the values into new sheet."""
import xlrd

SHEET_GROUPS = (('C', 'B',), ('A',),)
BASE_GROUP = 'A'
COMMON_KEY = 'commonnum'
UNIQ_KEY = 'langnum'


def __debug(v):
    from pprint import pprint
    print 'DEBUG', '-' * 40, '>'
    pprint(v)


def main():
    book = xlrd.open_workbook('sample.xlsx')
    group_objs = []
    for sheet_group in SHEET_GROUPS:
        group_obj = {}
        for sheet_name in sheet_group:
            sheet_obj = book.sheet_by_name(sheet_name)
            col_objs = {}
            for col in range(sheet_obj.ncols):
                _obj = sheet_obj.col(col)
                col_objs[_obj[0].value] = [n.value for n in _obj[1:]]
            group_obj[sheet_name] = col_objs
        group_objs.append(group_obj)
    __debug(group_objs)
    combined_objs = {}
    for objs in group_objs:
        __debug(objs)
        if len(objs.keys()) <= 1:
            combined_objs[objs.keys()[0]] = objs.values()[0]
            continue
        using_candi_keys = ([n.keys() for n in objs.values()])
        using_export_key = list(
            reduce(lambda a, b: a & b,
                   map(lambda n: set(n),
                       using_candi_keys)))
        for k, v in objs.items():
            index_nums = [len(v) for v in v.values()]
        if len(set(index_nums)) != 1:
            raise IndexError('{0} is invalid index.'.format(k))
        _stack = {}
        for v in objs.values():
            for _k, _v in v.items():
                if _k not in using_export_key:
                    continue
                if _k not in _stack:
                    _stack[_k] = _v
                else:
                    _stack[_k] = _stack[_k] + _v
        combined_objs['-'.join(sorted(objs.keys()))] = _stack
    __debug(combined_objs)

main()
