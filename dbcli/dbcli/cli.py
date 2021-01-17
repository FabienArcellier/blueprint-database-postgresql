import os

import click
from dbcli.database import Database


@click.group()
def cli():
    pass


@click.command('ping', help="check the host is ready to execute sql query")
def ping():
    connection_string = os.getenv('DATABASE_URL', 'postgresql://postgres:1234@localhost:5432/postgres')
    database = Database(connection_string)
    try:
        database.ping()
        click.echo(f"host is ready")
    except Exception as exception:
        click.echo(exception)


@click.command('init', help="ensure the initial database exists")
def init():
    connection_string = os.getenv('DATABASE_URL', 'postgresql://postgres:1234@localhost:5432/postgres')
    database = Database(connection_string)
    try:
        database.init()
        click.echo(f"{database.database_name} is ready")
    except Exception as exception:
        click.echo(exception)


cli.add_command(ping)
cli.add_command(init)

if __name__ == '__main__':
     cli()
