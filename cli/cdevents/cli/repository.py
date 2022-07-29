"""Module for cli repository commands."""
from __future__ import annotations

import os
from typing import List

import click

from cdevents.cli.utils import add_disclaimer_text, print_function_args
from cdevents.cli.cdevents_command import CDeventsCommand

from cdevents.core.events import Events
from cdevents.core import event_type

# pylint: disable=unused-argument
def common_repository_options(function):
    """Decorator for common cli options for repository."""
    function = click.option(
        "--id",
        "-i",
        required=False,
        type=str,
        help="Repository Id.",
    )(function)
    function = click.option(
        "--name",
        "-n",
        required=False,
        type=str,
        help="Repository's Name.",
    )(function)
    function = click.option(
        "--url",
        "-u",
        required=False,
        type=str,
        help="Repository's URL.",
    )(function)
    function = click.option(
        "--data",
        "-d",
        required=False,
        type=(str, str),
        multiple=True,
        help="Repository's Data.",
    )(function)

    return function


@click.command(help=add_disclaimer_text("Repository Created CloudEvent."))
@common_repository_options
def created(
    id: str,
    name: str = None,
    url: str = None,
    data: List[str] = None,
):
    print_function_args()
    e = Events()
    new_event = e.create_repository_event(event_type.RepositoryCreatedEventV1, id, name, url, data)
    cdevents_command = CDeventsCommand()
    cdevents_command.run(new_event)


@click.command(help=add_disclaimer_text("Repository Modified CloudEvent."))
@common_repository_options
def modified(
    id: str,
    name: str = None,
    url: str = None,
    data: List[str] = None,
):
    print_function_args()
    e = Events()
    new_event = e.create_repository_event(event_type.RepositoryModifiedEventV1, id, name, url, data)
    cdevents_command = CDeventsCommand()
    cdevents_command.run(new_event)


@click.command(help=add_disclaimer_text("Repository Deleted CloudEvent."))
@common_repository_options
def deleted(
    id: str,
    name: str = None,
    url: str = None,
    data: List[str] = None,
):
    print_function_args()
    e = Events()
    new_event = e.create_repository_event(event_type.RepositoryModifiedEventV1, id, name, url, data)
    cdevents_command = CDeventsCommand()
    cdevents_command.run(new_event)

