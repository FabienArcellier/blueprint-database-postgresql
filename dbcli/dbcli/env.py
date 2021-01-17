import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def database_connection_string() -> str:
    connection_string = os.getenv('DATABASE_URL', 'postgresql://postgres:1234@localhost:5432/simple')
    return connection_string
