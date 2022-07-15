# Should support yaml, json file json config string
"""Module for configuration read and provisioning."""
import copy
import json
import logging
from pathlib import Path
from typing import Union

import yaml

from cdevents.cli.utils import DictUtils


class ConfigurationReader:
    """Handle reading of configuration.

    Configuration source can be provided as file paths or JSON string.
    """

    _YAML_FILE_SUFFIXES = [".yml", ".yaml"]
    _JSON_FILE_SUFFIXES = [".json"]

    def __init__(self) -> None:  # noqa: D107
        self._configuration: dict = {}
        self._log = logging.getLogger(__name__)

    @property
    def configuration(self) -> dict:
        """Returns a deep copy of the configuration dict."""
        return copy.deepcopy(self._configuration)

    @configuration.setter
    def configuration(self, configuration: dict):
        """Merge existing configuration with new configuration.

        If the new configuration have the same corresponding keys,
        the new configuration will overwrite the previous.

        Args:
            configuration (dict): _description_
        """
        _config = copy.deepcopy(configuration)
        if not self._configuration:
            self._configuration = _config
        else:
            DictUtils.merge_dicts(
                self._configuration,
                _config,
            )
            self._configuration = _config

    def read_configuration(self, configuration_file: Union[str, Path]):
        """Read configuration from file.

        Args:
            configuration (Union[str, Path]): Path to configuration file.

        Raises:
            FileNotFoundError: Thrown if configuration file does  not exist
            ValueError: Thrown if file suffix is not supported.
        """
        _config_file = Path(configuration_file)
        self._log.debug("Reading configuration file '%s'", _config_file)
        if not _config_file.exists():
            raise FileNotFoundError(f"Configuration file {_config_file} not found.")
        elif self._is_supported_yaml_suffix(_config_file):
            self.configuration = yaml.safe_load(_config_file.read_text(encoding="utf-8"))

        elif self._is_supported_json_suffix(_config_file):
            self.configuration = json.loads(_config_file.read_text("utf-8"))

        else:
            error_msg = (
                f"Unsupported file format {_config_file.suffix!r},"
                + f" Supported formats: {self._YAML_FILE_SUFFIXES+self._JSON_FILE_SUFFIXES!r}"
            )
            self._log.error(error_msg)
            raise ValueError(error_msg)
        self._log.debug("Configuration: '%s'", self.configuration)

    @staticmethod
    def _is_supported_json_suffix(_config_file: Path) -> bool:
        return _config_file.suffix.lower() in ConfigurationReader._JSON_FILE_SUFFIXES

    @staticmethod
    def _is_supported_yaml_suffix(_config_file: Path) -> bool:
        return _config_file.suffix.lower() in ConfigurationReader._YAML_FILE_SUFFIXES
