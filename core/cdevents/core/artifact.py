"""artifact"""

from cdevents.core.event import Event
from cdevents.core.event_type import EventType

class ArtifactEvent(Event):
    """Artifact Event."""

    def __init__(self, **kwargs):
        """Initializes class.
        """
        self._event_type : EventType = kwargs['artifact_type']
        if 'data' in kwargs:
            self._data :dict = kwargs['data']
        
        if 'id' in kwargs and 'name' in kwargs and 'version' in kwargs:
            self._id :str = kwargs['id']
            self._name :str = kwargs['name']
            self._version :str = kwargs['version']
            super().__init__(event_type=self._event_type.value, extensions=self.create_extensions(), data=self._data)
        
        elif 'extensions' in kwargs:
            self._id = kwargs['extensions'].get('artifactid')
            self._name = kwargs['extensions'].get('artifactname')
            self._version = kwargs['extensions'].get('artifactversion')
            super().__init__(event_type=self._event_type.value,  extensions=self.create_extensions(), data=self._data)

    def create_extensions(self) -> dict:
        """Create extensions.
        """
        extensions = {
            "artifactid": self._id,
            "artifactname": self._name,
            "artifactversion": self._version,
        }
        return extensions

class ArtifactPackagedEvent(ArtifactEvent):
    
    def __init__(self, **kwargs):
        """Initializes class.
        """
        self._event_type: str = EventType.ArtifactPackagedEventV1

        super().__init__(artifact_type=self._event_type, **kwargs)

class ArtifactPublishedEvent(ArtifactEvent):
    
    def __init__(self, **kwargs):
        """Initializes class.
        """
        self._event_type: str = EventType.ArtifactPublishedEventV1

        super().__init__(artifact_type=self._event_type, **kwargs)
