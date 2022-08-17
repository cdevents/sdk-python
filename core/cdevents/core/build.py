"""build"""

from cdevents.core.event import Event 
from cdevents.core.event_type import EventType

class BuildEvent(Event):
    """Build Event."""

    def __init__(self, **kwargs):
        """Initializes class.
        """
        self._event_type : EventType = kwargs['build_type']
        if 'data' in kwargs:
            self._data :dict = kwargs['data']

        if 'id' in kwargs and 'name' in kwargs and 'artifact' in kwargs:
            self._id :str = kwargs['id']
            self._name :str = kwargs['name']
            self._artifact :str = kwargs['artifact']
            super().__init__(event_type=self._event_type.value, extensions=self.create_extensions(), data=self._data)

        elif 'extensions' in kwargs:
            self._id = kwargs['extensions'].get('buildid'),
            self._name = kwargs['extensions'].get('buildname')
            self._artifact = kwargs['extensions'].get('buildartifactid')
            super().__init__(event_type=self._event_type.value,  extensions=self.create_extensions(), attrs=kwargs['attrs'], data=self._data)

    def create_extensions(self) -> dict:
        """Create extensions.
        """
        extensions = {
            "buildid": self._id,
            "buildname": self._name,
            "buildartifactid": self._artifact,
        }
        return extensions

class BuildStartedEvent(BuildEvent):
    """Build Started Event."""
    def __init__(self, **kwargs):
        """Initializes class.
        """
        self._event_type: str = EventType.BuildStartedEventV1

        super().__init__(build_type=self._event_type, **kwargs)
    
class BuildQueuedEvent(BuildEvent):
    """Build Queued Event."""
    def __init__(self, **kwargs):
        """Initializes class.
        """
        self._event_type: str = EventType.BuildQueuedEventV1

        super().__init__(build_type=self._event_type, **kwargs)

class BuildFinishedEvent(BuildEvent):
    """Build Finished Event."""
    def __init__(self, **kwargs):
        """Initializes class.
        """
        self._event_type: str = EventType.BuildFinishedEventV1

        super().__init__(build_type=self._event_type, **kwargs)
