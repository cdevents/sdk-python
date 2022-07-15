"""Module for cli build commands."""
from __future__ import annotations

import os
from typing import List

import click

from cdevents.cli.utils import add_disclaimer_text, print_function_args
from cdevents.cli.cdevents_command import CDeventsCommand

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
    build_started_event_v1 = "cd.build.started.v1"
    extensions = {
        "buildid": id,
        "buildname": name,
        "buildartifactid": artifact,
    }

    cdevents_command = CDeventsCommand()
    cdevents_command.run(build_started_event_v1, extensions, data)

@click.command(help=add_disclaimer_text("Build Finished CloudEvent."))
@common_build_options
def finished(
    id: str,
    name: str = None,
    artifact: str = None,
    data: List[str] = None,
):
    print_function_args()
    build_finished_event_v1 = "cd.build.finished.v1"
    extensions = {
        "buildid": id,
        "buildname": name,
        "buildartifactid": artifact,
    }

    cdevents_command = CDeventsCommand()
    cdevents_command.run(build_finished_event_v1, extensions, data)


@click.command(help=add_disclaimer_text("PipelineRun Queued CloudEvent."))
@common_build_options
def queued(
    id: str,
    name: str = None,
    artifact: str = None,
    data: List[str] = None,
):
    print_function_args()
    build_queued_event_v1 = "cd.build.queued.v1"
    extensions = {
        "buildid": id,
        "buildname": name,
        "buildartifactid": artifact,
    }

    cdevents_command = CDeventsCommand()
    cdevents_command.run(build_queued_event_v1, extensions, data)
