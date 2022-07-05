"""Module for cli build commands."""
from __future__ import annotations

from ast import literal_eval
from pathlib import Path
from typing import List, Tuple, Union

import click
# from click_option_group import MutuallyExclusiveOptionGroup, optgroup

# from hostlog.cli.cached_settings import CachedSettingsHandler
# from hostlog.cli.configuration_handler import new_configuration_handler_with_override
# from hostlog.cli.configuration_reader import ConfigurationReader
# from cdevents.cli.online_commands import (
#     FetchTdfCommand,
#     MaxLogData,
#     StartLoggingCommand,
#     Topic,
# )
from cdevents.cli.utils import (
    add_disclaimer_text,
    print_function_args,
    yaml_files_in_directory,
)


# pylint: disable=unused-argument
def common_build_options(function):
    """Decorator for common cli options for host connection."""
    function = click.option(
        "--output",
        "-o",
        # FIXME: set to true during integration
        required=False,
        type=str,
        help="Path to output directory. Overrides configuration.",
    )(function)
    function = function = click.option(
        "--port",
        "-p",
        required=False,
        type=int,
        help="The host's port. Overrides configuration.",
    )(function)
    function = click.option(
        "--host",
        "-h",
        required=False,
        type=str,
        help="IP address of host. Overrides configuration.",
    )(function)
    function = click.option(
        "--to-binary",
        "-b",
        type=bool,
        is_flag=True,
        default=False,
        help="If set, all received data will be stored in binary format.",
    )(function)
    function = click.option(
        "--no-decode",
        type=bool,
        is_flag=True,
        default=False,
        help="If set, no decoding of received data will be done.",
    )(function)
    function = click.option(
        "--dcf-version",
        type=int,
        required=False,
        help="Version of the DCF protocol to use. Overrides configuration.",
    )(function)
    return function


@click.command(help=add_disclaimer_text("Fetch Topic Definition Files from target."))
@common_build_options
def fetch_tdf(
    output: str,
    host: str = None,
    port: int = None,
    dcf_version: int = None,
    to_binary: bool = False,
    no_decode: bool = False,
):
    """Start client, fetch and save TDF files. \
         Storage location is read from configuration file or optional argument."""
    print_function_args()

    # config_handler = new_configuration_handler_with_override(output, host, port, dcf_version)

    # fetch_tdf_command = FetchTdfCommand(
    #     config_handler=config_handler, to_binary=to_binary, no_decode=no_decode
    # )
    # fetch_tdf_command.run()
    # # Save tdf output directory to settings file.
    # settings_handler = CachedSettingsHandler()
    # settings_handler.latest_tdf_directory = fetch_tdf_command.destination_directory


@click.command(
    help=add_disclaimer_text(
        "Subscribe to one or more hostlog/DCF topics and start receiving and decoding messages."
    )
)
@common_build_options
@click.option(
    "--topics",
    "-t",
    type=str,
    required=False,
    default="",
    help=(
        "Topic subscriptions as a comma separated string '<chId>:<topicId>'."
        + " E.g. '1:0,1:2,2:0,2:1'"
        + " (Selected topics must be described in TDFs)."
        + " Optional. If not provided, all topics in given TDFs will be subscribed to."
    ),
)
# @click.option(
#     "--visualize",
#     type=bool,
#     is_flag=True,
#     default=False,
#     help="If set, then visualization will start at the same time as logging",
# )
# FIXME: Add more help text regarding configuration of dissector.
# @click.option(
#     "--create-dissector",
#     type=str,
#     help="If set, a Wireshark dissector is created based on configuration TBD.",
# )
@click.option(
    "--to-hdf5",
    type=bool,
    is_flag=True,
    default=False,
    help="If set, decoded data will be saved to HDF5 file in the output directory.",
)
@click.option(
    "--to-text",
    type=bool,
    is_flag=True,
    default=False,
    help="If set, decoded data will be saved to text file in the output directory.",
)
@click.option(
    "--definitions",
    "-d",
    type=str,
    required=False,
    help=(
        "Path to Topic Definition File(s) describing all topics that can be subscribed to."
        + " If path is a directory then all its *.yaml files will be loaded."
        + " Optional: If no argument is given,"
        + " the most recently fetched TDF directory will be used."
    ),
)
@click.option(
    "--config",
    "-c",
    type=str,
    required=False,
    default="",
    help=(
        "Path to configuration file generated by frontend UI."
        + " N.B. This configuration will override arguments '--config' and '--topics'"
    ),
)
@click.option(
    "--max-messages",
    type=int,
    required=False,
    help=("Maximum number of messages to log."),
)
# @optgroup.group(
#     "Maximum logging time.",
#     cls=MutuallyExclusiveOptionGroup,
#     help="Mutually exclusive parameters for maximum logging time.",
# )
# @optgroup.option(
#     "--max-time-s",
#     type=int,
#     help=("Maximum logging time in seconds."),
# )
# @optgroup.option(
#     "--max-time-m",
#     type=float,
#     help=("Maximum logging time in minutes."),
# )
# @optgroup.option(
#     "--max-time-h",
#     type=float,
#     help=("Maximum logging time in hours."),
# )
# @optgroup.group(
#     "Maximum amount of logged data.",
#     cls=MutuallyExclusiveOptionGroup,
#     help="Mutually exclusive parameters group for maximum amount of logged data.",
# )
# @optgroup.option(
#     "--max-kbytes",
#     type=float,
#     help=("Maximum number of kilobytes to log."),
# )
# @optgroup.option(
#     "--max-mbytes",
#     type=float,
#     help=("Maximum number of megabytes to log."),
# )
# @optgroup.option(
#     "--max-gbytes",
#     type=float,
#     help=("Maximum number of gigabytes to log."),
# )
# TODO: keep or not to keep "--enable-multiprocessing"
# @click.option(
#     "--enable-multiprocessing",
#     type=bool,
#     is_flag=True,
#     default=False,
#     help="If set, multiprocessing decoding will be disabled.",
# )
def start_logging(
    output: str,
    definitions: Union[str, Path],
    topics: str = "",
    visualize: bool = False,
    create_dissector: str = None,
    host: str = None,
    port: int = None,
    dcf_version: int = None,
    to_hdf5: bool = False,
    to_binary: bool = False,
    no_decode: bool = False,
    to_text: bool = False,
    config: str = "",
    max_messages: int = None,
    max_time_s: int = None,
    max_time_m: int = None,
    max_time_h: int = None,
    max_kbytes: int = None,
    max_mbytes: int = None,
    max_gbytes: int = None,
    enable_multiprocessing: bool = None,
):
    """Method for cli command to start streaming host logging."""
    print_function_args()

    # config_handler = new_configuration_handler_with_override(
    #     output,
    #     host,
    #     port,
    #     dcf_version,
    #     enable_multiprocessing,
    # )

    # ###### frontend configuration file
    # _topics = []
    # if config:
    #     # override '--topics' and '--definitions'
    #     frontend_config_handler = FrontendConfigHandler(config)
    #     definitions = frontend_config_handler.topic_collection
    #     if not Path(definitions).is_absolute():
    #         definitions = Path(config_handler.output.directory).joinpath("tdf", definitions)
    #     _topics = frontend_config_handler.selected_topics
    # elif topics != "":
    #     # Only true if topics are used and no UI config file.
    #     _topics = TopicsArgParser.topic_arg_to_topics(topics)
    # # If no-decode true then configuration files are not necessary.
    # if no_decode:
    #     hostlog_configuration_files = []
    # else:
    #     ######## If '--config' and '--contend_config' are not set, use latest fetched tdfs ####
    #     if not (definitions or config):
    #         definitions = CachedSettingsHandler.get_cached_configuration_path()

    #     ####### Fetch all tdf configuration files. ##########
    #     hostlog_configuration_files = yaml_files_in_directory(Path(definitions))

    # ####### Max data to log. #######
    # max_log_data = MaxLogData.new_instance(
    #     max_time_s=max_time_s,
    #     max_time_m=max_time_m,
    #     max_time_h=max_time_h,
    #     max_messages=max_messages,
    #     max_kbytes=max_kbytes,
    #     max_mbytes=max_mbytes,
    #     max_gbytes=max_gbytes,
    # )

    # start_logging_command = StartLoggingCommand(
    #     config_handler=config_handler,
    #     hostlog_config_files=hostlog_configuration_files,
    #     topics=_topics,
    #     to_binary=to_binary,
    #     no_decode=no_decode,
    #     to_hdf5=to_hdf5,
    #     to_text=to_text,
    #     max_log_data=max_log_data,
    # )
    # start_logging_command.run()


# class TopicsArgParser:
#     """Class handling parsing selected topics argument string."""

#     @staticmethod
#     def topic_arg_to_topics(topics_str: str) -> List[Topic]:
#         """Parse arg string to list of Topics.

#         Expected arg string format: '<chId:topicId>,1:2,2:3,.....'

#         Returns:
#             List[Topic]:  A sorted list of topics.
#         """
#         return TopicsArgParser._to_topics(TopicsArgParser._parse_topics_arg(topics_str))

#     @staticmethod
#     def _parse_topics_arg(topics_str: str) -> List[Tuple]:
#         topics = []
#         parse_erro_msg = "Error parsing topics argument:"
#         for tuple_str in topics_str.split(","):
#             topic_tuple = literal_eval(tuple_str.strip().replace(":", ","))
#             if not isinstance(topic_tuple, tuple):
#                 raise ValueError(f"{parse_erro_msg} Expected 'int:int' but found {tuple_str!r}")
#             if not len(topic_tuple) == 2:
#                 raise ValueError(
#                     (
#                         f"{parse_erro_msg} Expected 2 elements but found {len(topic_tuple)!r}"
#                         + f" when parsing {tuple_str!r}."
#                     )
#                 )
#             if not all(isinstance(element, int) for element in topic_tuple):
#                 raise ValueError(f"{parse_erro_msg} Expected int but found {topic_tuple!r}")
#             topics.append(topic_tuple)
#         # Remove duplicates
#         return sorted(list(set(topics)))

#     @staticmethod
#     def _to_topics(topics: List[Tuple]) -> List[Topic]:
#         return [Topic(*i) for i in topics]


# class FrontendConfigHandler:
#     """Class providing configuration from file generated by the frontend."""

#     def __init__(self, config_file: str):
#         """Initialize object.

#         Args:
#             config_file (str): Path to configuration file generated by the selected topics UI.
#         """
#         self._config: dict = self._read(Path(config_file))

#     @staticmethod
#     def _read(config_file: Path) -> dict:
#         config_reader = ConfigurationReader()
#         config_reader.read_configuration(config_file)
#         return config_reader.configuration

#     @property
#     def selected_topics(self) -> List[Topic]:
#         """Return selected topics from configuration file."""
#         result = []
#         _selected_topics = self._config["selected_topics"]
#         for channel_topic in _selected_topics:
#             channel_id = channel_topic["channel"]
#             for _topic in channel_topic["topics"]:
#                 result.append(Topic(channel_id=int(channel_id), topic_id=int(_topic)))
#         return result

#     @property
#     def topic_collection(self) -> Path:
#         """Return topic collection."""
#         return Path(self._config["topic_collection"])
