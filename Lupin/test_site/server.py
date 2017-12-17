"""Test http server managemant.

Manage http server which do testing.
Usage:
    python server.py [start|sopt]

    start: start server
    stop: stop server
"""
import argparse
import os
import sys
import signal
import SimpleHTTPServer
import SocketServer
import time


# HTTP Defines
PORT = 9090
CUR_DIR = os.path.abspath(os.path.dirname(__file__))
PID_FILE = os.path.join(CUR_DIR, 'pid.txt')
LOG_DIR = os.path.join(CUR_DIR, 'log')
if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)
ACCESS_LOG = os.path.join(LOG_DIR, 'access.log')
ERROR_LOG = os.path.join(LOG_DIR, 'error.log')


class SimpleHTTPServerWrapper(SimpleHTTPServer.SimpleHTTPRequestHandler):

    """Wrapping SimpleHTTPServer.

    The aim of this class is to separate log file.
    Because default SimpleHTTPServer is write all log into stderr.
    """

    def log_error(self, format, *args):
        """Logging error.

        Write log into another definition compared with base definition.
        """
        self.log_error_message(format, *args)

    def log_message(self, format, *args):
        access_log = open(ACCESS_LOG, 'a+')
        access_log.write("%s -- - [%s] %s\n" %
                         (self.client_address[0],
                          self.log_date_time_string(),
                          format % args))
        access_log.close()

    def log_error_message(self, format, *args):
        error_log = open(ERROR_LOG, 'a+')
        error_log.write("%s -- - [%s] %s\n" %
                        (self.client_address[0],
                         self.log_date_time_string(),
                         format % args))
        error_log.close()


def start():
    """Start httpd server.

    Server runs child process.
    Process id is written in `pid.txt`.
    Access or error log can be confirmed in `log` directory.
    """
    child = os.fork()
    if child > 0:
        sys.exit(1)
    pid = os.getpid()
    f = open(PID_FILE, 'w')
    f.write(str(pid))
    f.close()
    Handler = SimpleHTTPServerWrapper
    httpd = SocketServer.TCPServer(("", PORT), Handler)
    httpd.serve_forever()


def stop():
    """Stop test httpd server.

    Stop server running.
    When stopping, this delete `pid.txt` file.
    """
    if not os.path.exists(PID_FILE):
        print 'Pid already doest\'t exist.'
        sys.exit(0)
    with open(PID_FILE, 'r') as pidfile:
        pid = int(pidfile.read())
    print '.',
    while True:
        print '.',
        time.sleep(1)
        try:
            os.kill(pid, signal.SIGTERM)
        except OSError:
            break
        continue
    os.remove(PID_FILE)
    print ''
    print 'Stop http server'


if __name__ == '__main__':
    description_help = 'Manage test site.'
    EXEC_DEFS = {
        'start': start,
        'stop': stop,
        }
    parser = argparse.ArgumentParser(description=description_help)
    parser.add_argument('command', metavar='[command(start|stop)]',
                        help='start or stop server.')
    args = parser.parse_args()
    if not EXEC_DEFS.get(args.command, None):
        command_list = '` or `'.join(EXEC_DEFS.keys())
        print 'Command should be `{0}`.'.format(command_list)
        sys.exit(0)
    EXEC_DEFS[args.command]()
