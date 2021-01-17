import unittest

from dbcli.database import Database


class TestDatabase(unittest.TestCase):

    def test_init_should_calculate_dsn_from_connection_string(self):
        # Acts
        database = Database('postgresql://postgres:1234@localhost:5432/postgres')

        # Assert
        self.assertEqual("dbname='postgres' user='postgres' host='localhost' port='5432' password='1234'", database.postgres_dsn)

    def test_init_should_calculate_dsn_for_postgresql_from_connection_string(self):
        # Acts
        database = Database('postgresql://postgres:1234@localhost:5432/database')

        # Assert
        self.assertEqual("dbname='postgres' user='postgres' host='localhost' port='5432' password='1234'", database.postgres_dsn)


    def test_init_should_calculate_database_name_from_connection_string(self):
        # Acts
        database = Database('postgresql://postgres:1234@localhost:5432/database')

        # Assert
        self.assertEqual("database", database.database_name)


if __name__ == '__main__':
    unittest.main()
