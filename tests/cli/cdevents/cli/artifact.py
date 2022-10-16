"""Module for cli artifact commands."""
from __future__ import annotations

from typing import List

import click
from cdevents.cli.cdevents_command import CDeventsCommand
from cdevents.cli.utils import add_disclaimer_text, print_function_args
from cdevents.core.artifact import ArtifactPackagedEvent, ArtifactPublishedEvent


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
    """Creates an ArtifactPackaged CDEvent."""
    print_function_args()
    artifact_event = ArtifactPackagedEvent(id=id, name=name, version=version, data=data)
    cdevents_command = CDeventsCommand()
    cdevents_command.run(artifact_event)


@click.command(help=add_disclaimer_text("Artifact Published CloudEvent."))
@common_artifact_options
def published(
    id: str,
    name: str = None,
    version: str = None,
    data: List[str] = None,
):
    """Creates an ArtifactPublished CDEvent."""
    print_function_args()
    artifact_event = ArtifactPublishedEvent(id=id, name=name, version=version, data=data)
    cdevents_command = CDeventsCommand()
    cdevents_command.run(artifact_event)
