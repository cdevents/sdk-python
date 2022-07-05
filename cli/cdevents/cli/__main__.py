"""Module for main entry point for cdevents.cli."""
import logging
import logging.config
from pathlib import Path

import click
import yaml

from cdevents.cli.constants import LOGGING_CONFIGURATION_FILE
from cdevents.cli.build import finished, queued, started
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


# @click.group(help=add_disclaimer_text("""Commands with no interaction with hostlog."""))
# def offline():
#     """Function for command group offline."""


# offline.add_command(pcap_to_hdf5)
# TODO: activate line when command is implemented
# offline.add_command(visualize)
# offline.add_command(create_dissector)
# offline.add_command(convert_to_xviz)
# offline.add_command(topic_configuration)


# @click.group(help=add_disclaimer_text("Commands for local web UI."))
# def web():
#     """Click group for command 'web'."""


# web.add_command(web_start)


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
# cli.add_command(offline)
# cli.add_command(web)

if __name__ == "__main__":
    cli()
