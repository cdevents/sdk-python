"""Module for cli pipelinerun commands."""
from __future__ import annotations

import os
from typing import List

import click

from cdevents.cli.utils import add_disclaimer_text, print_function_args
from cdevents.cli.cdevents_command import CDeventsCommand

from cdevents.core.events import Events
from cdevents.core import event_type

# pylint: disable=unused-argument
def common_pipelinerun_options(function):
    """Decorator for common cli options for pipelinerun."""
    function = click.option(
        "--id",
        "-i",
        required=False,
        type=str,
        help="Pipeline Run Id.",
    )(function)
    function = click.option(
        "--name",
        "-n",
        required=False,
        type=str,
        help="Pipeline Run's Name.",
    )(function)
    function = click.option(
        "--status",
        "-s",
        required=False,
        type=str,
        help="Pipeline Run's Status.",
    )(function)
    function = click.option(
        "--url",
        "-u",
        required=False,
        type=str,
        help="Pipeline Run's URL.",
    )(function)
    function = click.option(
        "--errors",
        "-e",
        required=False,
        type=str,
        help="Pipeline Run's Errors.",
    )(function)
    function = click.option(
        "--data",
        "-d",
        required=False,
        type=(str, str),
        multiple=True,
        help="Pipeline Run's Data.",
    )(function)

    return function


@click.command(help=add_disclaimer_text("PipelineRun Started CloudEvent."))
@common_pipelinerun_options
def started(
    id: str,
    name: str = None,
    status: str = None,
    url: str = None,
    errors: str = None,
    data: List[str] = None,
):
    print_function_args()
    e = Events()
    new_event = e.create_pipelinerun_event(event_type.PipelineRunStartedEventV1, id, name, status, url, errors, data)
    cdevents_command = CDeventsCommand()
    cdevents_command.run(new_event)


@click.command(help=add_disclaimer_text("PipelineRun Finished CloudEvent."))
@common_pipelinerun_options
def finished(
    id: str,
    name: str = None,
    status: str = None,
    url: str = None,
    errors: str = None,
    data: List[str] = None,
):
    print_function_args()
    e = Events()
    new_event = e.create_pipelinerun_event(event_type.PipelineRunFinishedEventV1, id, name, status, url, errors, data)
    cdevents_command = CDeventsCommand()
    cdevents_command.run(new_event)

@click.command(help=add_disclaimer_text("PipelineRun Queued CloudEvent."))
@common_pipelinerun_options
def queued(
    id: str,
    name: str = None,
    status: str = None,
    url: str = None,
    errors: str = None,
    data: List[str] = None,
):
    print_function_args()
    e = Events()
    new_event = e.create_pipelinerun_event(event_type.PipelineRunQueuedEventV1, id, name, status, url, errors, data)
    cdevents_command = CDeventsCommand()
    cdevents_command.run(new_event)

