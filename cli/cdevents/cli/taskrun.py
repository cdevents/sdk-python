"""Module for cli taskrun commands."""
from __future__ import annotations

import os
from typing import List

import click

from cdevents.cli.utils import add_disclaimer_text, print_function_args
from cdevents.cli.cdevents_command import CDeventsCommand

from cdevents.core.events import Events
from cdevents.core import event_type

# pylint: disable=unused-argument
def common_taskrun_options(function):
    """Decorator for common cli options for taskrun."""
    function = click.option(
        "--id",
        "-i",
        required=False,
        type=str,
        help="Task Run Id.",
    )(function)
    function = click.option(
        "--name",
        "-n",
        required=False,
        type=str,
        help="Task Run's Name.",
    )(function)
    function = click.option(
        "--pipelineid",
        "-p",
        required=False,
        type=str,
        help="Task Run's Pipeline Id.",
    )(function)
    function = click.option(
        "--data",
        "-d",
        required=False,
        type=(str, str),
        multiple=True,
        help="Task Run's Data.",
    )(function)

    return function


@click.command(help=add_disclaimer_text("TaskRun Started CloudEvent."))
@common_taskrun_options
def started(
    id: str,
    name: str = None,
    pipelineid: str = None,
    data: List[str] = None,
):
    print_function_args()
    e = Events()
    new_event = e.create_taskrun_event(event_type.TaskRunStartedEventV1, id, name, pipelineid, data)
    cdevents_command = CDeventsCommand()
    cdevents_command.run(new_event)

@click.command(help=add_disclaimer_text("TaskRun Finished CloudEvent."))
@common_taskrun_options
def finished(
    id: str,
    name: str = None,
    pipelineid: str = None,
    data: List[str] = None,
):
    print_function_args()
    e = Events()
    new_event = e.create_taskrun_event(event_type.TaskRunFinishedEventV1, id, name, pipelineid, data)
    cdevents_command = CDeventsCommand()
    cdevents_command.run(new_event)
