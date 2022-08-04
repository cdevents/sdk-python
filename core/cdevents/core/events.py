"""Core events."""

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
