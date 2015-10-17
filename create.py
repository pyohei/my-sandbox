"""Dummy Config Creater.

Make dummy file from config file.
This file must use `ConfigParser` module.
"""

EXTENTION = 'dummy'


def main(confpath):
    __chk_path(confpath)
    __copy(confpath)
    dummypath = confpath + '.' + EXTENTION



def __chk_path(confpath):
    pass





if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--confpath', '-c', required=True,
                        help='config file path', metavar='xxxx/yyy.ini',
                        dest='confpath')
    args = parser.parse_args()
    main(args.confpath)
