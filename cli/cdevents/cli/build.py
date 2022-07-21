"""Module for cli build commands."""
from __future__ import annotations

import os
from typing import List

import click

from cdevents.cli.utils import add_disclaimer_text, print_function_args
from cdevents.cli.cdevents_command import CDeventsCommand

from cdevents.core.events import Events
from cdevents.core import event_type

# pylint: disable=unused-argument
def common_build_options(function):
    """Decorator for common cli options for build."""
    function = click.option(
        "--id",
        "-i",
        required=False,
        type=str,
        help="Build Id.",
    )(function)
    function = click.option(
        "--name",
        "-n",
        required=False,
        type=str,
        help="Build Name.",
    )(function)
    function = click.option(
        "--artifact",
        "-a",
        required=False,
        type=str,
        help="Build's Artifact Id.",
    )(function)
    function = click.option(
        "--data",
        "-d",
        required=False,
        # type=click.Tuple([str, str]),
        type=(str, str),
        multiple=True,
        help="Build Data.",
    )(function)

    return function


@click.command(help=add_disclaimer_text("Build Started CloudEvent."))
@common_build_options
def started(
    id: str,
    name: str = None,
    artifact: str = None,
    data: List[str] = None,
):
    print_function_args()
    e = Events()
    new_event = e.create_build_event(event_type.BuildStartedEventV1, id, name, artifact, data)
    cdevents_command = CDeventsCommand()
    cdevents_command.run(new_event)

@click.command(help=add_disclaimer_text("Build Finished CloudEvent."))
@common_build_options
def finished(
    id: str,
    name: str = None,
    artifact: str = None,
    data: List[str] = None,
):
    print_function_args()
    e = Events()
    new_event = e.create_build_event(event_type.BuildFinishedEventV1, id, name, artifact, data)
    cdevents_command = CDeventsCommand()
    cdevents_command.run(new_event)

@click.command(help=add_disclaimer_text("PipelineRun Queued CloudEvent."))
@common_build_options
def queued(
    id: str,
    name: str = None,
    artifact: str = None,
    data: List[str] = None,
):
    print_function_args()
    e = Events()
    new_event = e.create_build_event(event_type.BuildQueuedEventV1, id, name, artifact, data)
    cdevents_command = CDeventsCommand()
    cdevents_command.run(new_event)
