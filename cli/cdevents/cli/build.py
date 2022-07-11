"""Module for cli build commands."""
from __future__ import annotations

import os
from typing import List

import click
import requests
from cloudevents.http import CloudEvent, to_structured

from cdevents.cli.utils import add_disclaimer_text, print_function_args


# pylint: disable=unused-argument
def common_build_options(function):
    """Decorator for common cli options for build."""
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
    cde_sink: str,
    id: str,
    name: str = None,
    artifact: str = None,
    data: List[str] = None,
):
    print_function_args()
    attributes = {
        "type": "cd.build.started.v1",
        "source": "cde-cli",
        "extensions": {
            "buildid": id,
            "buildname": name,
            "buildartifactid": artifact,
        },
    }
    event = CloudEvent(attributes, dict(data))
    headers, body = to_structured(event)

    # send and print event
    requests.post(cde_sink, headers=headers, data=body)


@click.command(help=add_disclaimer_text("Build Finished CloudEvent."))
@common_build_options
def finished(
    cde_sink: str,
    id: str,
    name: str = None,
    artifact: str = None,
    data: List[str] = None,
):
    print_function_args()
    attributes = {
        "type": "cd.build.finished.v1",
        "source": "cde-cli",
        "extensions": {
            "buildid": id,
            "buildname": name,
            "buildartifactid": artifact,
        },
    }
    event = CloudEvent(attributes, dict(data))
    headers, body = to_structured(event)

    # send and print event
    requests.post(cde_sink, headers=headers, data=body)


@click.command(help=add_disclaimer_text("PipelineRun Queued CloudEvent."))
@common_build_options
def queued(
    cde_sink: str,
    id: str,
    name: str = None,
    artifact: str = None,
    data: List[str] = None,
):
    print_function_args()
    attributes = {
        "type": "cd.build.queued.v1",
        "source": "cde-cli",
        "extensions": {
            "buildid": id,
            "buildname": name,
            "buildartifactid": artifact,
        },
    }
    event = CloudEvent(attributes, dict(data))
    headers, body = to_structured(event)

    # send and print event
    requests.post(cde_sink, headers=headers, data=body)
