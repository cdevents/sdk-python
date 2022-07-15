"""Module for cli environment commands."""
from __future__ import annotations

import os
from typing import List

import click

from cdevents.cli.utils import add_disclaimer_text, print_function_args
from cdevents.cli.cdevents_command import CDeventsCommand

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
    environment_created_event_v1 = "cd.environment.created.v1"
    extensions = {
        "envId": id,
        "envname": name,
        "envrepourl": repo,
    }

    cdevents_command = CDeventsCommand()
    cdevents_command.run(environment_created_event_v1, extensions, data)


@click.command(help=add_disclaimer_text("Environment Deleted CloudEvent."))
@common_env_options
def deleted(
    id: str,
    name: str = None,
    repo: str = None,
    data: List[str] = None,
):
    print_function_args()
    environment_deleted_event_v1 = "cd.environment.deleted.v1"
    extensions = {
        "envId": id,
        "envname": name,
        "envrepourl": repo,
    }

    cdevents_command = CDeventsCommand()
    cdevents_command.run(environment_deleted_event_v1, extensions, data)


@click.command(help=add_disclaimer_text("Environment Modified CloudEvent."))
@common_env_options
def modified(
    id: str,
    name: str = None,
    repo: str = None,
    data: List[str] = None,
):
    print_function_args()
    environment_modified_event_v1 = "cd.environment.modified.v1"
    extensions = {
        "envId": id,
        "envname": name,
        "envrepourl": repo,
    }

    cdevents_command = CDeventsCommand()
    cdevents_command.run(environment_modified_event_v1, extensions, data)
