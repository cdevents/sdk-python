"""Module for cli build commands."""
from __future__ import annotations

from typing import List

import click
from cdevents.cli.cdevents_command import CDeventsCommand
from cdevents.cli.utils import add_disclaimer_text, print_function_args
from cdevents.core.build import BuildFinishedEvent, BuildQueuedEvent, BuildStartedEvent


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
    build_event = BuildStartedEvent(id=id, name=name, artifact=artifact, data=data)
    cdevents_command = CDeventsCommand()
    cdevents_command.run(build_event)


@click.command(help=add_disclaimer_text("Build Finished CloudEvent."))
@common_build_options
def finished(
    id: str,
    name: str = None,
    artifact: str = None,
    data: List[str] = None,
):
    print_function_args()
    build_event = BuildQueuedEvent(id=id, name=name, artifact=artifact, data=data)
    cdevents_command = CDeventsCommand()
    cdevents_command.run(build_event)


@click.command(help=add_disclaimer_text("PipelineRun Queued CloudEvent."))
@common_build_options
def queued(
    id: str,
    name: str = None,
    artifact: str = None,
    data: List[str] = None,
):
    print_function_args()
    build_event = BuildFinishedEvent(id=id, name=name, artifact=artifact, data=data)
    cdevents_command = CDeventsCommand()
    cdevents_command.run(build_event)
