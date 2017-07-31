import MySQLdb
from MySQLdb import cursors
from sample2 import DbConnector as dc2


MYSQL_MAP = {
    'host': '192.168.0.90',
    'database': 'moc_sample',
    'user': 'developer',
    'password': 'developer',
    'encoding': 'utf8'}
SAMPLE_QUERY = 'SELECT * FROM sample;'


class DbConnector:

    def __init__(self):
        d = dc2()
        print d.fetchRecords2("hoge")
        connection = MySQLdb.connect(
            host=MYSQL_MAP['host'],
            db=MYSQL_MAP['database'],
            user=MYSQL_MAP['user'],
            passwd=MYSQL_MAP['password'],
            charset=MYSQL_MAP['encoding'])
        self.conn = connection
        self.cur = self.conn.cursor(cursors.DictCursor)

    def insertRecord(self, sql):
        self.cur.execute(sql)
        self.conn.commit()

    def fetchRecords(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def updateRecords(self, sql):
        self.cur.execute(sql)
        self.conn.commit()

    def deleteRecords(self, sql):
        self.execute(sql)
        self.conn.commit()

if __name__ == '__main__':
    dbconn = DbConnector()
    print dbconn.fetchRecords(SAMPLE_QUERY)
