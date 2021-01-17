from urllib.parse import urlparse

import psycopg2
from retrying import retry

from dbcli import logger


class Database:

    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        self.postgres_dsn = self._get_postgres_dsn(connection_string)
        self.database_name = self._get_database(connection_string)

    @retry(wait_fixed=5000, stop_max_attempt_number=10)
    def init(self):
        conn = psycopg2.connect(self.postgres_dsn)
        conn.autocommit = True
        cursor = conn.cursor()
        self._execute(cursor, f"SELECT 1 AS result FROM pg_database WHERE datname='{self.database_name}'")
        if cursor.rowcount == 0:
            query = f"CREATE DATABASE {self.database_name}"
            self._execute(cursor, query)

    def _execute(self, cursor, query):
        logger().info(f"sql: {query}")
        cursor.execute(query)

    @retry(wait_fixed=5000, stop_max_attempt_number=10)
    def ping(self):
        conn = psycopg2.connect(self.postgres_dsn)
        cursor = conn.cursor()
        cursor.execute("SELECT 1'")

    def _get_postgres_dsn(self, connection_string: str) -> str:
        """
        postgres database is a database that is always present on a cluster postgresql.
        on database init, we are using this database to connect

        :see: https://www.psycopg.org/docs/module.html#psycopg2.connect
        :return:
        """
        o = urlparse(connection_string)
        user = o.username
        password = o.password
        hostname = o.hostname
        port = o.port
        dsn = f"dbname='postgres' user='{user}' host='{hostname}' port='{port}' password='{password}'"
        return dsn

    def _get_database(self, connection_string: str) -> str:
        o = urlparse(connection_string)
        database = o.path[1:]
        return database
