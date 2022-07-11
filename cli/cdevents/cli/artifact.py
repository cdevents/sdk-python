"""Module for cli artifact commands."""
from __future__ import annotations

import os
from typing import List

import click
import requests
from cloudevents.http import CloudEvent, to_structured

from cdevents.cli.utils import add_disclaimer_text, print_function_args


# pylint: disable=unused-argument
def common_artifact_options(function):
    """Decorator for common cli options for artifact."""
    function = click.option(
        "--cde_sink",
        "-c",
        required=False,
        type=str,
        default=lambda: os.environ.get("CDE_SINK", "http://localhost:8080"),
        help="CDE_SINK",
    )(function)
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
    cde_sink: str,
    id: str,
    name: str = None,
    version: str = None,
    data: List[str] = None,
):
    print_function_args()
    attributes = {
        "type": "cd.artifact.packaged.v1",
        "source": "cde-cli",
        "extensions": {
            "artifactid": id,
            "artifactname": name,
            "artifactversion": version,
        },
    }
    event = CloudEvent(attributes, dict(data))
    headers, body = to_structured(event)

    # send and print event
    requests.post(cde_sink, headers=headers, data=body)


@click.command(help=add_disclaimer_text("Artifact Published CloudEvent."))
@common_artifact_options
def published(
    cde_sink: str,
    id: str,
    name: str = None,
    version: str = None,
    data: List[str] = None,
):
    print_function_args()
    attributes = {
        "type": "cd.artifact.published.v1",
        "source": "cde-cli",
        "extensions": {
            "artifactid": id,
            "artifactname": name,
            "artifactversion": version,
        },
    }
    event = CloudEvent(attributes, dict(data))
    headers, body = to_structured(event)

    # send and print event
    requests.post(cde_sink, headers=headers, data=body)
