"""build"""

from enum import Enum
from cdevents.core.events import Events

class BuildType(Enum):
    BuildStartedEventV1  :str = "cd.build.started.v1"
    BuildQueuedEventV1   :str = "cd.build.queued.v1"
    BuildFinishedEventV1 :str = "cd.build.finished.v1"


class Build(Events):
    """build."""

    def __init__(self, build_type: BuildType, id: str, name: str, artifact: str):
        """Initializes class.
        """
        self._event_type = build_type
        self._id = id
        self._name = name
        self._artifact = artifact
    
    def create_extensions(self):
        """Create extensions.
        """
        extensions = {
            "buildid": self._id,
            "buildname": self._name,
            "buildartifactid": self._artifact,
        }
        return extensions
    
    def create_event(self, data: dict={}):
        """Create build event.
        """
        extensions = self.create_extensions()
        event = super().create_event(event_type=self._event_type.value, extensions=extensions, data=data)
        return event
