"""Core events."""

from abc import abstractmethod
from typing import Dict

from cloudevents.http import CloudEvent


class Event(CloudEvent):
    """Event."""

    def __init__(self, event_type: str, extensions: dict, attrs=None, data={}):
        """Initializes class."""
        if attrs:
            super().__init__(attributes=attrs, data=data)
        else:
            self._event_type = event_type
            self._extensions = extensions
            self._data = data

            self._attributes = {
                "type": self._event_type,
                "source": "cde-cli",
                "extensions": self._extensions,
            }
            super().__init__(self._attributes, dict(self._data))

    @abstractmethod
    def create_extensions(self) -> Dict[str, str]:
        """Create extensions."""
        extensions: Dict[str, str] = {}
        return extensions
