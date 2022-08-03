"""artifact"""

from enum import Enum
from cdevents.core.events import Events

class ArtifactType(Enum):
    ArtifactPackagedEventV1: str = "cd.artifact.packaged.v1"
    ArtifactPublishedEventV1: str = "cd.artifact.published.v1"


class Artifact(Events):
    """Artifact."""

    def __init__(self, artifact_type: ArtifactType, id: str, name: str, version: str):
        """Initializes class.
        """
        self._event_type = artifact_type
        self._id = id
        self._name = name
        self._version = version
    
    def create_extensions(self):
        """Create extensions.
        """
        extensions = {
            "artifactid": self._id,
            "artifactname": self._name,
            "artifactversion": self._version,
        }
        return extensions
    
    def create_event(self, data: dict={}):
        """Create artifact event.
        """
        extensions = self.create_extensions()
        event = super().create_event(event_type=self._event_type.value, extensions=extensions, data=data)
        return event
