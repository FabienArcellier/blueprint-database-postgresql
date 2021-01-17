# pylint: disable=broad-except

import os

import click

from dbcli import DATABASE_ALEMBIC_PATH
from dbcli.database import Database
from dbcli.env import database_connection_string
from dbcli.shell import command, run


@click.group(help='cli to manage a postgresql database')
def cli():
    pass


@click.command('alembic:revision', help="create a new revision")
@click.option('--message', '-m', help='message string to use with revision')
def alembic_revision(message):
    args = ['revision']

    if message is not None:
        args.append("-m")
        args.append(message)

    alembic = command('alembic', "alembic is not initialized in your python environment")
    os.chdir(DATABASE_ALEMBIC_PATH)
    run(alembic, args)


@click.command('alembic:upgrade',
               help="upgrade operations, proceeding from the current database revision to the given target revision")
@click.argument('revision', default="head")
def alembic_upgrade(revision):
    args = ['upgrade', revision]

    alembic = command('alembic', "alembic is not initialized in your python environment")
    os.chdir(DATABASE_ALEMBIC_PATH)
    run(alembic, args)


@click.command('ping', help="check the host is ready to execute sql query")
def ping():
    connection_string = database_connection_string()
    database = Database(connection_string)
    try:
        database.ping()
        click.echo("host is ready")
    except Exception as exception:
        click.echo(exception)


@click.command('init', help="ensure the initial database exists")
def init():
    connection_string = database_connection_string()
    database = Database(connection_string)
    try:
        database.init()
        click.echo(f"{database.database_name} is ready")
    except Exception as exception:
        click.echo(exception)


cli.add_command(alembic_revision)
cli.add_command(alembic_upgrade)
cli.add_command(ping)
cli.add_command(init)

if __name__ == '__main__':
    cli()
