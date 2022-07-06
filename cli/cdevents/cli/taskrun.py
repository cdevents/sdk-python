"""Module for cli taskrun commands."""
from __future__ import annotations
import os

from typing import List

import click
import requests

from cloudevents.http import CloudEvent, to_structured

from cdevents.cli.utils import (
    add_disclaimer_text,
    print_function_args,
)


# pylint: disable=unused-argument
def common_taskrun_options(function):
    """Decorator for common cli options for taskrun."""
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
        type=(str,str),
        multiple=True,
        help="Task Run's Data.",
    )(function)

    return function


@click.command(help=add_disclaimer_text("TaskRun Started CloudEvent."))
@common_taskrun_options
def started(
    cde_sink: str,
    id: str,
    name: str = None,
    pipelineid: str = None,
    data :List[str] = None,
):
    print_function_args()
    attributes = {
        "type": "cd.taskrun.started.v1",
        "source": "cde-cli",
        "extensions": {
            "taskrunid": id,
            "taskrunname": name,
            "taskrunpipelineid": pipelineid,
        },
    }
    event = CloudEvent(attributes, dict(data))
    headers, body = to_structured(event)

    # send and print event
    requests.post(cde_sink, headers=headers, data=body)

@click.command(help=add_disclaimer_text("TaskRun Finished CloudEvent."))
@common_taskrun_options
def finished(
    cde_sink: str,
    id: str,
    name: str = None,
    pipelineid: str = None,
    data :List[str] = None,
):
    print_function_args()
    attributes = {
        "type": "cd.taskrun.finished.v1",
        "source": "cde-cli",
        "extensions": {
            "taskrunid": id,
            "taskrunname": name,
            "taskrunpipelineid": pipelineid,
        },
    }
    event = CloudEvent(attributes, dict(data))
    headers, body = to_structured(event)

    # send and print event
    requests.post(cde_sink, headers=headers, data=body)
