"""artifact"""

from enum import Enum
from cdevents.core.event import Event

class ArtifactType(Enum):
    ArtifactPackagedEventV1: str = "cd.artifact.packaged.v1"
    ArtifactPublishedEventV1: str = "cd.artifact.published.v1"


class ArtifactEvent(Event):
    """Artifact Event."""

    def __init__(self, artifact_type: ArtifactType, id: str, name: str, version: str, data: dict = {}):
        """Initializes class.
        """
        self._event_type = artifact_type
        self._id = id
        self._name = name
        self._version = version
        super().__init__(event_type=self._event_type.value, extensions=self.create_extensions(), data=data)
    
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
    
    def __init__(self, id: str, name: str, version: str, data: dict = {}):
        """Initializes class.
        """
        self._event_type: str = ArtifactType.ArtifactPackagedEventV1

        super().__init__(artifact_type=self._event_type, id=id, name=name, version=version, data=data)

class ArtifactPublishedEvent(ArtifactEvent):
    
    def __init__(self, id: str, name: str, version: str, data: dict = {}):
        """Initializes class.
        """
        self._event_type: str = ArtifactType.ArtifactPublishedEventV1

        super().__init__(artifact_type=self._event_type, id=id, name=name, version=version, data=data)
