"""Module for cli service commands."""
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
def common_service_options(function):
    """Decorator for common cli options for service."""
    function = click.option(
        "--cde_sink",
        "-c",
        required=False,
        type=str,
        default=lambda: os.environ.get("CDE_SINK", "http://localhost:8080"),
        help="CDE_SINK",
    )(function)
    function = click.option(
        "--envid",
        "-e",
        required=False,
        type=str,
        help="Environment Id where the Service is running.",
    )(function)
    function = click.option(
        "--name",
        "-n",
        required=False,
        type=str,
        help="Service's Name.",
    )(function)
    function = click.option(
        "--version",
        "-v",
        required=False,
        type=str,
        help="Service's Version.",
    )(function)
    function = click.option(
        "--data",
        "-d",
        required=False,
        type=(str, str),
        multiple=True,
        help="Service's Data.",
    )(function)

    return function


@click.command(help=add_disclaimer_text("Service Deployed CloudEvent."))
@common_service_options
def deployed(
    cde_sink: str,
    envid: str,
    name: str = None,
    version: str = None,
    data: List[str] = None,
):
    print_function_args()
    attributes = {
        "type": "cd.service.deployed.v1",
        "source": "cde-cli",
        "extensions": {
            "serviceenvid": envid,
            "servicename": name,
            "serviceversion": version,
        },
    }
    event = CloudEvent(attributes, dict(data))
    headers, body = to_structured(event)

    # send and print event
    result = requests.post(cde_sink, headers=headers, data=body)
    _log.debug(f"Response with state code {result.status_code}")


@click.command(help=add_disclaimer_text("Service Upgraded CloudEvent."))
@common_service_options
def upgraded(
    cde_sink: str,
    envid: str,
    name: str = None,
    version: str = None,
    data: List[str] = None,
):
    print_function_args()
    attributes = {
        "type": "cd.service.upgraded.v1",
        "source": "cde-cli",
        "extensions": {
            "serviceenvid": envid,
            "servicename": name,
            "serviceversion": version,
        },
    }
    event = CloudEvent(attributes, dict(data))
    headers, body = to_structured(event)

    # send and print event
    result = requests.post(cde_sink, headers=headers, data=body)
    _log.debug(f"Response with state code {result.status_code}")


@click.command(help=add_disclaimer_text("Service Removed CloudEvent."))
@common_service_options
def removed(
    cde_sink: str,
    envid: str,
    name: str = None,
    version: str = None,
    data: List[str] = None,
):
    print_function_args()
    attributes = {
        "type": "cd.service.removed.v1",
        "source": "cde-cli",
        "extensions": {
            "serviceenvid": envid,
            "servicename": name,
            "serviceversion": version,
        },
    }
    event = CloudEvent(attributes, dict(data))
    headers, body = to_structured(event)

    # send and print event
    result = requests.post(cde_sink, headers=headers, data=body)
    _log.debug(f"Response with state code {result.status_code}")


@click.command(help=add_disclaimer_text("Service Rolledback CloudEvent."))
@common_service_options
def rolledback(
    cde_sink: str,
    envid: str,
    name: str = None,
    version: str = None,
    data: List[str] = None,
):
    print_function_args()
    attributes = {
        "type": "cd.service.rolledback.v1",
        "source": "cde-cli",
        "extensions": {
            "serviceenvid": envid,
            "servicename": name,
            "serviceversion": version,
        },
    }
    event = CloudEvent(attributes, dict(data))
    headers, body = to_structured(event)

    # send and print event
    result = requests.post(cde_sink, headers=headers, data=body)
    _log.debug(f"Response with state code {result.status_code}")
