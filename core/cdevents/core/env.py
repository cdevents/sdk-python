"""env"""

from enum import Enum
from cdevents.core.events import Events

class EnvType(Enum):
    EnvironmentCreatedEventV1  :str = "cd.environment.created.v1"
    EnvironmentModifiedEventV1 :str = "cd.environment.modified.v1"
    EnvironmentDeletedEventV1  :str = "cd.environment.deleted.v1"


class Env(Events):
    """Env."""

    def __init__(self, env_type: EnvType, id: str, name: str, repo: str,data: dict = {}):
        """Initializes class.
        """
        self._event_type = env_type
        self._id = id
        self._name = name
        self._repo = repo
        super().__init__(event_type=self._event_type.value, extensions=self.create_extensions(), data=data)
    
    def create_extensions(self) -> dict:
        """Create extensions.
        """
        extensions = {
            "envId": self._id,
            "envname": self._name,
            "envrepourl": self._repo,
        }
        return extensions
