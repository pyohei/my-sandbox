
import signal
import os
import sys

import test_server

def start():
    wf = open(
        "", "a")
    rf = open(
        "/dev/null", "r")
    os.setsid()
    os.umask(0)
    os.dup2(wf.fileno(), sys.stdout.fileno())
    os.dup2(rf.fileno(), sys.stdin.fileno())
    os.dup2(wf.fileno(), sys.stderr.fileno())
    pid_file = open(
        "", "w")
    pid = os.getpid()
    pid_file.write(str(pid))
    pid_file.close()
    def stop():
        sys.exit(0)
    signal.signal(signal.SIGTERM, stop)
    signal.signal(signal.SIGINT, stop)
    while True:
        test_server.start()

if __name__ == "__main__":
    print "start"
    start()


