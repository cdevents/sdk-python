"""Module for cli service commands."""
from __future__ import annotations

import os
from typing import List

import click

from cdevents.cli.utils import add_disclaimer_text, print_function_args
from cdevents.cli.cdevents_command import CDeventsCommand

from cdevents.core.events import Events
from cdevents.core import event_type

# pylint: disable=unused-argument
def common_service_options(function):
    """Decorator for common cli options for service."""
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
    envid: str,
    name: str = None,
    version: str = None,
    data: List[str] = None,
):
    print_function_args()
    e = Events()
    new_event = e.create_service_event(event_type.ServiceDeployedEventV1, envid, name, version, data)
    cdevents_command = CDeventsCommand()
    cdevents_command.run(new_event)


@click.command(help=add_disclaimer_text("Service Upgraded CloudEvent."))
@common_service_options
def upgraded(
    envid: str,
    name: str = None,
    version: str = None,
    data: List[str] = None,
):
    print_function_args()
    e = Events()
    new_event = e.create_service_event(event_type.ServiceUpgradedEventV1, envid, name, version, data)
    cdevents_command = CDeventsCommand()
    cdevents_command.run(new_event)


@click.command(help=add_disclaimer_text("Service Removed CloudEvent."))
@common_service_options
def removed(
    envid: str,
    name: str = None,
    version: str = None,
    data: List[str] = None,
):
    print_function_args()
    e = Events()
    new_event = e.create_service_event(event_type.ServiceRemovedEventV1, envid, name, version, data)
    cdevents_command = CDeventsCommand()
    cdevents_command.run(new_event)


@click.command(help=add_disclaimer_text("Service Rolledback CloudEvent."))
@common_service_options
def rolledback(
    envid: str,
    name: str = None,
    version: str = None,
    data: List[str] = None,
):
    print_function_args()
    e = Events()
    new_event = e.create_service_event(event_type.ServiceRolledbackEventV1, envid, name, version, data)
    cdevents_command = CDeventsCommand()
    cdevents_command.run(new_event)
