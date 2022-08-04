"""build"""

from enum import Enum
from cdevents.core.events import Events

class BuildType(Enum):
    BuildStartedEventV1  :str = "cd.build.started.v1"
    BuildQueuedEventV1   :str = "cd.build.queued.v1"
    BuildFinishedEventV1 :str = "cd.build.finished.v1"


class Build(Events):
    """build."""

    def __init__(self, build_type: BuildType, id: str, name: str, artifact: str, data: dict = {}): 
        """Initializes class.
        """
        self._event_type = build_type
        self._id = id
        self._name = name
        self._artifact = artifact
        super().__init__(event_type=self._event_type.value, extensions=self.create_extensions(), data=data)
    
    def create_extensions(self) -> dict:
        """Create extensions.
        """
        extensions = {
            "buildid": self._id,
            "buildname": self._name,
            "buildartifactid": self._artifact,
        }
        return extensions
