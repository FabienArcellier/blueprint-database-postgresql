import logging
import os
import sys

ROOT_DIR = os.path.realpath(os.path.join(__file__, "..", ".."))
DATABASE_ALEMBIC_PATH = ROOT_DIR


def logger() -> logging.Logger:
    dbcli_logger = logging.getLogger('dbcli')
    dbcli_logger.setLevel(logging.DEBUG)
    log_stdout = logging.StreamHandler(stream=sys.stdout)
    dbcli_logger.addHandler(log_stdout)

    return dbcli_logger
