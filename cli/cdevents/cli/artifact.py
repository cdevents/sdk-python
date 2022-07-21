"""Module for cli artifact commands."""
from __future__ import annotations

import os
from typing import List

import click

from cdevents.cli.utils import add_disclaimer_text, print_function_args
from cdevents.cli.cdevents_command import CDeventsCommand

from cdevents.core.events import Events
from cdevents.core import event_type

# pylint: disable=unused-argument
def common_artifact_options(function):
    """Decorator for common cli options for artifact."""
    function = click.option(
        "--id",
        "-i",
        required=False,
        type=str,
        help="Artifact Id.",
    )(function)
    function = click.option(
        "--name",
        "-n",
        required=False,
        type=str,
        help="Artifact Name.",
    )(function)
    function = click.option(
        "--version",
        "-v",
        required=False,
        type=str,
        help="Artifact Version.",
    )(function)
    function = click.option(
        "--data",
        "-d",
        required=False,
        type=(str, str),
        multiple=True,
        help="Artifact Data.",
    )(function)

    return function


@click.command(help=add_disclaimer_text("Artifact Packaged CloudEvent."))
@common_artifact_options
def packaged(
    id: str,
    name: str = None,
    version: str = None,
    data: List[str] = None,
):
    print_function_args()
    e = Events()
    new_event = e.create_artifact_event(event_type.ArtifactPackagedEventV1, id, name, version, data)
    cdevents_command = CDeventsCommand()
    cdevents_command.run(new_event)


@click.command(help=add_disclaimer_text("Artifact Published CloudEvent."))
@common_artifact_options
def published(
    id: str,
    name: str = None,
    version: str = None,
    data: List[str] = None,
):
    print_function_args()

    e = Events()
    new_event = e.create_artifact_event(event_type.ArtifactPublishedEventV1, id, name, version, data)
    cdevents_command = CDeventsCommand()
    cdevents_command.run(new_event)
