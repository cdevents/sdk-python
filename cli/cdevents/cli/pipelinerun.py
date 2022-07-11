"""Module for cli pipelinerun commands."""
from __future__ import annotations

import os
from typing import List

import click
import requests
from cloudevents.http import CloudEvent, to_structured

from cdevents.cli.utils import add_disclaimer_text, print_function_args


# pylint: disable=unused-argument
def common_pipelinerun_options(function):
    """Decorator for common cli options for pipelinerun."""
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
    cde_sink: str,
    id: str,
    name: str = None,
    status: str = None,
    url: str = None,
    errors: str = None,
    data: List[str] = None,
):
    print_function_args()
    attributes = {
        "type": "cd.pipelinerun.started.v1",
        "source": "cde-cli",
        "extensions": {
            "pipelinerunid": id,
            "pipelinerunname": name,
            "pipelinerunstatus": status,
            "pipelinerunurl": url,
            "pipelinerunerrors": errors,
        },
    }
    event = CloudEvent(attributes, dict(data))
    headers, body = to_structured(event)

    # send and print event
    requests.post(cde_sink, headers=headers, data=body)


@click.command(help=add_disclaimer_text("PipelineRun Finished CloudEvent."))
@common_pipelinerun_options
def finished(
    cde_sink: str,
    id: str,
    name: str = None,
    status: str = None,
    url: str = None,
    errors: str = None,
    data: List[str] = None,
):
    print_function_args()
    attributes = {
        "type": "cd.pipelinerun.finished.v1",
        "source": "cde-cli",
        "extensions": {
            "pipelinerunid": id,
            "pipelinerunname": name,
            "pipelinerunstatus": status,
            "pipelinerunurl": url,
            "pipelinerunerrors": errors,
        },
    }
    event = CloudEvent(attributes, dict(data))
    headers, body = to_structured(event)

    # send and print event
    requests.post(cde_sink, headers=headers, data=body)


@click.command(help=add_disclaimer_text("PipelineRun Queued CloudEvent."))
@common_pipelinerun_options
def queued(
    cde_sink: str,
    id: str,
    name: str = None,
    status: str = None,
    url: str = None,
    errors: str = None,
    data: List[str] = None,
):
    print_function_args()
    attributes = {
        "type": "cd.pipelinerun.queued.v1",
        "source": "cde-cli",
        "extensions": {
            "pipelinerunid": id,
            "pipelinerunname": name,
            "pipelinerunstatus": status,
            "pipelinerunurl": url,
            "pipelinerunerrors": errors,
        },
    }
    event = CloudEvent(attributes, dict(data))
    headers, body = to_structured(event)

    # send and print event
    requests.post(cde_sink, headers=headers, data=body)
