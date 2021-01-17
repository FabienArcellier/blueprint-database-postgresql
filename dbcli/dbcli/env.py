import os

from dotenv import load_dotenv, find_dotenv

from dbcli import ROOT_DIR

load_dotenv(find_dotenv())


def database_connection_string() -> str:
    connection_string = os.getenv('DATABASE_URL', 'postgresql://postgres:1234@localhost:5432/simple')
    return connection_string


def database_alembic_path() -> str:
    """
    The overload of the alembic path allows the management of several databases through the same dbcli utility.
    You must instantiate a new alembic folder with the migrations from this other database.

    """
    path = os.getenv('DATABASE_ALEMBIC_PATH', os.path.join(ROOT_DIR, 'alembic'))
    return path
