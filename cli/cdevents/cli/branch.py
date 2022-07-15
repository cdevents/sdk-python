"""Module for cli branch commands."""
from __future__ import annotations

import logging
import os
from typing import List

import click
import requests
from cloudevents.http import CloudEvent, to_structured

from cdevents.cli.utils import add_disclaimer_text, print_function_args

_log = logging.getLogger(__name__)

# pylint: disable=unused-argument
def common_branch_options(function):
    """Decorator for common cli options for branch."""
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
        help="Branch Id.",
    )(function)
    function = click.option(
        "--name",
        "-n",
        required=False,
        type=str,
        help="Branch Name.",
    )(function)
    function = click.option(
        "--repoid",
        "-v",
        required=False,
        type=str,
        help="Branch Repository Id.",
    )(function)
    function = click.option(
        "--data",
        "-d",
        required=False,
        type=(str, str),
        multiple=True,
        help="Branch Data.",
    )(function)

    return function


@click.command(help=add_disclaimer_text("Branch Created CloudEvent."))
@common_branch_options
def created(
    cde_sink: str,
    id: str,
    name: str = None,
    repoid: str = None,
    data: List[str] = None,
):
    print_function_args()
    attributes = {
        "type": "cd.repository.branch.created.v1",
        "source": "cde-cli",
        "extensions": {
            "branchid": id,
            "branchname": name,
            "branchrepositoryid": repoid,
        },
    }
    event = CloudEvent(attributes, dict(data))
    headers, body = to_structured(event)

    # send and print event
    result = requests.post(cde_sink, headers=headers, data=body)
    _log.debug(f"Response with state code {result.status_code}")

@click.command(help=add_disclaimer_text("Branch Deleted CloudEvent."))
@common_branch_options
def deleted(
    cde_sink: str,
    id: str,
    name: str = None,
    repoid: str = None,
    data: List[str] = None,
):
    print_function_args()
    attributes = {
        "type": "cd.repository.branch.deleted.v1",
        "source": "cde-cli",
        "extensions": {
            "branchid": id,
            "branchname": name,
            "branchrepositoryid": repoid,
        },
    }
    event = CloudEvent(attributes, dict(data))
    headers, body = to_structured(event)

    # send and print event
    result = requests.post(cde_sink, headers=headers, data=body)
    _log.debug(f"Response with state code {result.status_code}")