# -*- coding:sjis -*-

from datetime import datetime
import fcntl
import os

FileName = ""


def init(logdir):
    u"""初期化

    グローバル変数にファイル名を格納しているため注意する事.

    :param str logdir:
    """
    if not os.path.exists(logdir):
        os.mkdir(logdir)
    logname = "%s.log" % (datetime.now().strftime("%Y%m%d"))
    global FileName
    FileName = os.path.join(logdir, logname)


def write(msg, caption="Normal"):
    msg = "[%s] [%s] %s\r\n" % (
        datetime.now().strftime("%Y/%m/%d %H:%M:%S"), caption, msg)
    writeDirect(msg)


def writeDirect(msg):
    f = open(FileName, "ab")
    fcntl.flock(f.fileno(), fcntl.LOCK_EX)
    f.write(msg)
    fcntl.flock(f.fileno(), fcntl.LOCK_UN)
    f.close()

if __name__ == "__main__":
    init("/tmp/test")
    for i in range(10):
        write("aaa", "test")
