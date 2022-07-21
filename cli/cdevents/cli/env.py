"""Module for cli environment commands."""
from __future__ import annotations

import os
from typing import List

import click

from cdevents.cli.utils import add_disclaimer_text, print_function_args
from cdevents.cli.cdevents_command import CDeventsCommand

from cdevents.core.events import Events
from cdevents.core import event_type

# pylint: disable=unused-argument
def common_env_options(function):
    """Decorator for common cli options for environment."""
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
        type=(str, str),
        multiple=True,
        help="Environment's Data.",
    )(function)

    return function


@click.command(help=add_disclaimer_text("Environment Created CloudEvent."))
@common_env_options
def created(
    id: str,
    name: str = None,
    repo: str = None,
    data: List[str] = None,
):
    print_function_args()
    e = Events()
    new_event = e.create_environment_event(event_type.EnvironmentCreatedEventV1, id, name, repo, data)
    cdevents_command = CDeventsCommand()
    cdevents_command.run(new_event)


@click.command(help=add_disclaimer_text("Environment Deleted CloudEvent."))
@common_env_options
def deleted(
    id: str,
    name: str = None,
    repo: str = None,
    data: List[str] = None,
):
    print_function_args()
    e = Events()
    new_event = e.create_environment_event(event_type.EnvironmentDeletedEventV1, id, name, repo, data)
    cdevents_command = CDeventsCommand()
    cdevents_command.run(new_event)

@click.command(help=add_disclaimer_text("Environment Modified CloudEvent."))
@common_env_options
def modified(
    id: str,
    name: str = None,
    repo: str = None,
    data: List[str] = None,
):
    print_function_args()
    e = Events()
    new_event = e.create_environment_event(event_type.EnvironmentModifiedEventV1, id, name, repo, data)
    cdevents_command = CDeventsCommand()
    cdevents_command.run(new_event)