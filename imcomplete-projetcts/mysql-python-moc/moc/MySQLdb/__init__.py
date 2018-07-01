"""MySQLdb execution moc."""
import inspect
import mocbase


def connect(*args, **kwargs):
    return MocConnection()


class MocConnection(object):

    def cursor(self, cursor):
        return MocCursor()


class MocCursor(object):
    def execute(self, sql):
        msg = 'Execute yourSQL\n  {}'.format(sql)
        print msg

    def fetchall(self):
        current_frame = inspect.currentframe()
        frames = inspect.getouterframes(current_frame)
        for func_name, result in mocbase.MYSQL_RECORD.items():
            for f in frames:
                if func_name == f[3]:
                    return result
