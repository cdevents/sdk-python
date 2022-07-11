"""Module for main entry point for cdevents.cli."""
import logging
import logging.config
from pathlib import Path

import click
import yaml

from cdevents.cli.artifact import packaged, published
from cdevents.cli.branch import created as branch_created
from cdevents.cli.branch import deleted as branch_deleted
from cdevents.cli.build import finished, queued, started
from cdevents.cli.constants import LOGGING_CONFIGURATION_FILE
from cdevents.cli.env import created as env_created
from cdevents.cli.env import deleted as env_deleted
from cdevents.cli.env import modified as env_modified
from cdevents.cli.pipelinerun import finished as pipe_finished
from cdevents.cli.pipelinerun import queued as pipe_queued
from cdevents.cli.pipelinerun import started as pipe_started
from cdevents.cli.service import deployed as service_deployed
from cdevents.cli.service import removed as service_removed
from cdevents.cli.service import rolledback as service_rolledback
from cdevents.cli.service import upgraded as service_upgraded
from cdevents.cli.taskrun import finished as taskrun_finished
from cdevents.cli.taskrun import started as taskrun_started
from cdevents.cli.utils import add_disclaimer_text


def configure_logging():
    """Configures logging from file."""
    config_file = Path(LOGGING_CONFIGURATION_FILE)
    logging_config = yaml.safe_load(config_file.read_text(encoding="utf8"))
    logging.config.dictConfig(logging_config)


@click.group(help=add_disclaimer_text("""Commands Build related CloudEvent."""))
def build():
    """Click group for command 'build'."""


build.add_command(finished)
build.add_command(queued)
build.add_command(started)


@click.group(help=add_disclaimer_text("""Commands Artifact related CloudEvent."""))
def artifact():
    """Click group for command 'artifact'."""


artifact.add_command(packaged)
artifact.add_command(published)


@click.group(help=add_disclaimer_text("""Commands Branch related CloudEvent."""))
def branch():
    """Click group for command 'branch'."""


branch.add_command(branch_created)
branch.add_command(branch_deleted)


@click.group(help=add_disclaimer_text("""Commands Environment related CloudEvent."""))
def env():
    """Click group for command 'environment'."""


env.add_command(env_created)
env.add_command(env_deleted)
env.add_command(env_modified)


@click.group(help=add_disclaimer_text("""Commands PipelineRun related CloudEvent."""))
def pipelinerun():
    """Click group for command 'environment'."""


pipelinerun.add_command(pipe_started)
pipelinerun.add_command(pipe_finished)
pipelinerun.add_command(pipe_queued)


@click.group(help=add_disclaimer_text("""Commands Service related CloudEvent."""))
def service():
    """Click group for command 'service'."""


service.add_command(service_deployed)
service.add_command(service_upgraded)
service.add_command(service_removed)
service.add_command(service_rolledback)


@click.group(help=add_disclaimer_text("""Commands TaskRun related CloudEvent."""))
def taskrun():
    """Click group for command 'taskrun'."""


taskrun.add_command(taskrun_started)
taskrun.add_command(taskrun_finished)


@click.group(
    help=add_disclaimer_text(
        """Main entry point for cdevents client cli.
    Select command group from Commands.
    Add '--help' to see more information about each subcommand, option and argument."""
    )
)
def cli():
    """Main method for cli."""
    configure_logging()


cli.add_command(build)
cli.add_command(artifact)
cli.add_command(branch)
cli.add_command(env)
cli.add_command(pipelinerun)
cli.add_command(service)
cli.add_command(taskrun)

if __name__ == "__main__":
    cli()
