# pylint: disable=logging-fstring-interpolation,pointless-statement
import os

import click
import plumbum
from click.exceptions import Exit
from plumbum import CommandNotFound, FG, ProcessExecutionError
from plumbum.machines import LocalCommand

from dbcli import logger


def command(command_name: str, fail_message: str = None) -> LocalCommand:
    try:
        return plumbum.local[command_name]
    except CommandNotFound as exception:
        complete_fail_message = f" - {fail_message}" if fail_message is not None else ""
        raise click.ClickException(f"unknow command {command_name}{complete_fail_message}") from exception


def run(local_command: LocalCommand, args: [str], exit_on_error=True) -> None:
    """
    if the excecution process is finishing with an exit code of 0

    There is one or two exception as the execution of migration by alembic through honcho.
    exit_on_error allow to manage them

    :param exit_on_error: break the flow if the exit code is different of 0
    """
    try:
        complete_command = local_command[args]
        working_directory = os.getcwd()
        logger().debug(f'{complete_command} - wd: {working_directory}')
        complete_command & FG
    except ProcessExecutionError as exception:
        if exit_on_error:
            raise Exit(code=exception.retcode) from exception
