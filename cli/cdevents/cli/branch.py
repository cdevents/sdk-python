"""Module for cli branch commands."""
from __future__ import annotations

import os
from typing import List

import click

from cdevents.cli.utils import add_disclaimer_text, print_function_args
from cdevents.cli.cdevents_command import CDeventsCommand

from cdevents.core.events import Events
from cdevents.core import event_type

# pylint: disable=unused-argument
def common_branch_options(function):
    """Decorator for common cli options for branch."""
    function = click.option(
        "--id",
        "-i",
        required=False,
        type=str,
        help="Branch Id.",
    )(function)
    function = click.option(
        "--name",
        "-n",
        required=False,
        type=str,
        help="Branch Name.",
    )(function)
    function = click.option(
        "--repoid",
        "-v",
        required=False,
        type=str,
        help="Branch Repository Id.",
    )(function)
    function = click.option(
        "--data",
        "-d",
        required=False,
        type=(str, str),
        multiple=True,
        help="Branch Data.",
    )(function)

    return function


@click.command(help=add_disclaimer_text("Branch Created CloudEvent."))
@common_branch_options
def created(
    id: str,
    name: str = None,
    repoid: str = None,
    data: List[str] = None,
):
    print_function_args() 
    e = Events()
    new_event = e.create_branch_event(event_type.BranchCreatedEventV1, id, name, repoid, data)
    cdevents_command = CDeventsCommand()
    cdevents_command.run(new_event)


@click.command(help=add_disclaimer_text("Branch Deleted CloudEvent."))
@common_branch_options
def deleted(
    id: str,
    name: str = None,
    repoid: str = None,
    data: List[str] = None,
):
    print_function_args() 
    e = Events()
    new_event = e.create_branch_event(event_type.BranchDeletedEventV1, id, name, repoid, data)
    cdevents_command = CDeventsCommand()
    cdevents_command.run(new_event)