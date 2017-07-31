import unittest
from sample import DbConnector
from moc import moctrigger


class DbConnectorTest(unittest.TestCase):

    def setUp(self):
        """Initialize MySQLdb."""
        moctrigger.reload_for_test(DbConnector)
        moctrigger.prepare_sql_result(
            {'test_fetchRecord': 'hogehoge',
             'fetchRecords2': 'fogafuga'})
        self.dbconn = DbConnector()

    def test_fetchRecord(self):
        rec = self.dbconn.fetchRecords(
            'SELECT * FROM sample;')
        print rec

if __name__ == '__main__':
    unittest.main()
