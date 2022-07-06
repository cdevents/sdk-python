"""Module for cli environment commands."""
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
def common_env_options(function):
    """Decorator for common cli options for environment."""
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
        help="Environment's Id.",
    )(function)
    function = click.option(
        "--name",
        "-n",
        required=False,
        type=str,
        help="Environment's Name.",
    )(function)
    function = click.option(
        "--repo",
        "-r",
        required=False,
        type=str,
        help="Environment's RepoUrl.",
    )(function)
    function = click.option(
        "--data",
        "-d",
        required=False,
        type=(str,str),
        multiple=True,
        help="Environment's Data.",
    )(function)

    return function


@click.command(help=add_disclaimer_text("Environment Created CloudEvent."))
@common_env_options
def created(
    cde_sink: str,
    id: str,
    name: str = None,
    repo: str = None,
    data :List[str] = None,
):
    print_function_args()
    attributes = {
        "type": "cd.environment.created.v1",
        "source": "cde-cli",
        "extensions": {
            "envId": id,
            "envname": name,
            "envrepourl": repo,
        },
    }
    event = CloudEvent(attributes, dict(data))
    headers, body = to_structured(event)

    # send and print event
    requests.post(cde_sink, headers=headers, data=body)

@click.command(help=add_disclaimer_text("Environment Deleted CloudEvent."))
@common_env_options
def deleted(
    cde_sink: str,
    id: str,
    name: str = None,
    repo: str = None,
    data :List[str] = None,
):
    print_function_args()
    attributes = {
        "type": "cd.environment.deleted.v1",
        "source": "cde-cli",
        "extensions": {
            "envId": id,
            "envname": name,
            "envrepourl": repo,
        },
    }
    event = CloudEvent(attributes, dict(data))
    headers, body = to_structured(event)

    # send and print event
    requests.post(cde_sink, headers=headers, data=body)


@click.command(help=add_disclaimer_text("Environment Modified CloudEvent."))
@common_env_options
def modified(
    cde_sink: str,
    id: str,
    name: str = None,
    repo: str = None,
    data :List[str] = None,
):
    print_function_args()
    attributes = {
        "type": "cd.environment.modified.v1",
        "source": "cde-cli",
        "extensions": {
            "envId": id,
            "envname": name,
            "envrepourl": repo,
        },
    }
    event = CloudEvent(attributes, dict(data))
    headers, body = to_structured(event)

    # send and print event
    requests.post(cde_sink, headers=headers, data=body)

