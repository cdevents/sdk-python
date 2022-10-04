"""Module for cli taskrun commands."""
from __future__ import annotations

from typing import List

import click
from cdevents.cli.cdevents_command import CDeventsCommand
from cdevents.cli.utils import add_disclaimer_text, print_function_args
from cdevents.core.taskrun import TaskRunFinishedEvent, TaskRunStartedEvent


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
    """Creates a TaskRunStarted CDEvent."""
    print_function_args()
    taskrun_event = TaskRunStartedEvent(id=id, name=name, pipelineid=pipelineid, data=data)
    cdevents_command = CDeventsCommand()
    cdevents_command.run(taskrun_event)


@click.command(help=add_disclaimer_text("TaskRun Finished CloudEvent."))
@common_taskrun_options
def finished(
    id: str,
    name: str = None,
    pipelineid: str = None,
    data: List[str] = None,
):
    """Creates a TaskRunFinished CDEvent."""
    print_function_args()
    taskrun_event = TaskRunFinishedEvent(id=id, name=name, pipelineid=pipelineid, data=data)
    cdevents_command = CDeventsCommand()
    cdevents_command.run(taskrun_event)
