"""Module for cli common command code."""
import logging
from abc import ABC
import requests

from cdevents.cli.configuration_handler import ConfigurationHandler
from cloudevents.http import CloudEvent, to_structured
from cdevents.cli.configuration_handler import new_default_configuration_handler

class CDeventsCommand(ABC):
    """Abstract base class for all Hostlog commands."""

    def __init__(self, config_handler: ConfigurationHandler = None):
        """Initializes base class.

        Args:
            config_handler (ConfigurationHandler): the configuration handler.
        """
        self._log = logging.getLogger(__name__)
        self._config_handler = config_handler
        if config_handler is None:
            self._config_handler = new_default_configuration_handler()

    def run(self, type, extensions, data):
        """run command.
        """
        attributes = {
            "type": type,
            "source": self.config_handler.source.name,
            "extensions": extensions,
        }
        event = CloudEvent(attributes, dict(data))
        headers, body = to_structured(event)
        cde_link = self.config_handler.client.host

        # send and print event
        result = requests.post(cde_link, headers=headers, data=body)
        self._log.info(f"Response with state code {result.status_code}")


    @property
    def config_handler(self) -> ConfigurationHandler:
        """Property for configuration handler."""
        return self._config_handler
