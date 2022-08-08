"""Core events."""

from abc import abstractmethod
from cloudevents.http import CloudEvent

class Events(CloudEvent):
    """Events."""

    def __init__(self, event_type: str, extensions: dict, data = {}):
        """Initializes class.
        """
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
    def create_extensions(self) -> dict:
        """Create extensions.
        """
        extensions = {}
        return extensions

    # @abstractmethod
    # def event_from_json(json_obj: dict) -> Events:
    #     """Create event from json.
    #     """
    #     pass