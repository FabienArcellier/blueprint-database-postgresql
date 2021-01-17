"""create internet usage table

Revision ID: 5ca0a8c0b78c
Revises:
Create Date: 2021-01-17 21:19:08.096583

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ca0a8c0b78c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()  # type: Connection

    conn.execute("""CREATE TABLE internet_usage(
      internet_usage_id SERIAL PRIMARY KEY,
      client_id INTEGER,
      date TIMESTAMP,
      data_mb DOUBLE PRECISION
    );""")


def downgrade():
    raise NotImplementedError
