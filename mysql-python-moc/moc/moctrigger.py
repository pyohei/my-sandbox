import inspect
import os
import sys
import mocbase


def substitute_builin_module():
    del_modules = {}
    for k, v in sys.modules.items():
        if k and 'MySQL' in k:
            del_modules[k] = v
        elif k and 'mysql' in k:
            del_modules[k] = v
    # Set current direcotry as primary.
    cur_dir = os.path.dirname(__file__)
    sys.path = [cur_dir] + sys.path
    # Below codes which commented out are may be unnecessary.
    # But this module is beta code, and I remain this.
    # for dk in del_key:
    #    del sys.modules[dk]
    for dk, dv in del_modules.items():
        if inspect.isroutine(dv):
            continue
        try:
            reload(dv)
        except (TypeError, ImportError) as err_msg:
            msg = 'Reload Error! ({0}) Message:{1}'.format(
                dk,
                err_msg)
            print msg


def reload_routine(test_moduel):
    """Reload modules which created as application.

    This module is beta version.
    """
    for k, v in sys.modules.items():
        if inspect.isroutine(v):
            reload(sys.modules[k])
    if inspect.ismodule(test_moduel):
        reload(test_moduel)
        return
    if inspect.isclass(test_moduel):
        module_name = inspect.getmodule(test_moduel)
        reload(module_name)
        return


def reload_for_test(test_moduel):
    """Reload all module subbordination unit testing module.

    *Attention!*
    However, this module is on researching.
    And I forbid you use this module!
    """
    substitute_builin_module()
    reload_routine(test_moduel)


def prepare_sql_result(results):
    for rk, rv in results.items():
        mocbase.MYSQL_RECORD[rk] = rv
