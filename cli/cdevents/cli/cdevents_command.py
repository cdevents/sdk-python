"""Module for cli common command code."""
import logging
from abc import ABC

from cdevents.cli.configuration_handler import (
    ConfigurationHandler,
    new_default_configuration_handler,
)
from cdevents.core.event_sender import EventSender
from cloudevents.http import CloudEvent


class CDeventsCommand(ABC):
    """Abstract base class for all CDevents commands."""

    def __init__(self, config_handler: ConfigurationHandler = None):
        """Initializes base class.

        Args:
            config_handler (ConfigurationHandler): the configuration handler.
        """
        self._log = logging.getLogger(__name__)
        self._config_handler = config_handler
        if config_handler is None:
            self._config_handler = new_default_configuration_handler()

    def run(self, event: CloudEvent):
        """run command."""
        e = EventSender(cde_link=self.config_handler.client.host)
        e.send(event)

    @property
    def config_handler(self) -> ConfigurationHandler:
        """Property for configuration handler."""
        return self._config_handler
