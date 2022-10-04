"""Module for configuration provider."""
from __future__ import annotations

import copy
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Union

from cdevents.cli.configuration_reader import ConfigurationReader
from cdevents.cli.constants import DEFAULT_CONFIGURATION_FILE
from cdevents.cli.utils import DictUtils


def get_default_configuration_file() -> str:
    """Returns the default configuration file path."""
    return DEFAULT_CONFIGURATION_FILE


def new_default_configuration_handler() -> ConfigurationHandler:
    """Returnes a configuration handler with the default configuration file"""
    config_handler: ConfigurationHandler = ConfigurationHandler.create_new(
        get_default_configuration_file()
    )

    return config_handler


def new_configuration_handler_with_override(client_host, source_name) -> ConfigurationHandler:
    """Returnes a configuration handler where args override configuration file."""
    args_as_config = ConfigurationHandler.create_override_config(
        client_host=client_host, source_name=source_name
    )

    config_handler: ConfigurationHandler = ConfigurationHandler.create_new(
        get_default_configuration_file(), args_as_config
    )

    return config_handler


class ConfigurationHandler:
    """Class for providing configuration."""

    def __init__(self, configuration: dict):
        """Initializes the configuration.

        Args:
            configuration (dict): The configuration.
        """
        self.client = _ClientConfig(**configuration["client"])
        self.source = _SourceConfig(**configuration["source"])

    @staticmethod
    def create_override_config(
        client_host: str = None,
        source_name: str = None,
    ) -> dict:
        """Create a dict that can be used for overriding the default configuration.

        Args:
            host (str, optional): client host address. Defaults to None.
            name (str, optional): source name. Defaults to None.

        Returns:
            dict: the dict to ovverride configuration with.
        """
        override_dict: dict = {}
        if client_host:
            DictUtils.merge_dicts({"client": {"host": client_host}}, override_dict)
        if source_name:
            DictUtils.merge_dicts({"source": {"name": source_name}}, override_dict)

        return override_dict

    @staticmethod
    def create_new(
        configuration_files: Union[list[str], str] = None, override_config: dict = None
    ) -> ConfigurationHandler:
        """Reads default configurationfile plus any additional configuration files provided.

        Additional configuration files will be merged with the default configfuration file.
        Ovveride configuration will ovverid any configuration from files.
        A configuration provider is returned.

        Args:
            configuration_files (Union[list[str], str], optional): yaml or json configration file. \
                Defaults to None.
            override_config (dict):override configuration from cli args. Defaults to None.

        Returns:
            ConfigurationHandler: the handler.
        """
        file_list = []
        if isinstance(configuration_files, str) or isinstance(configuration_files, Path):
            file_list.append(configuration_files)
        elif isinstance(configuration_files, list):
            file_list.extend(configuration_files)

        reader = ConfigurationReader()
        for _file in file_list:
            reader.read_configuration(_file)

        # merge dicts
        if override_config:
            _config = copy.deepcopy(override_config)
            DictUtils.merge_dicts(reader.configuration["configuration"], _config)
        else:
            _config = reader.configuration["configuration"]

        return ConfigurationHandler(_config)


@dataclass
class _ClientConfig:
    host: str


@dataclass
class _SourceConfig:
    name: str
