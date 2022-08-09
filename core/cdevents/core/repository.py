"""repository"""

from enum import Enum
from cdevents.core.event import Event

class RepositoryType(Enum):
    RepositoryCreatedEventV1  :str = "cd.repository.created.v1"
    RepositoryModifiedEventV1 :str = "cd.repository.modified.v1"
    RepositoryDeletedEventV1  :str = "cd.repository.deleted.v1"


class RepositoryEvent(Event):
    """Repository Event."""

    def __init__(self, repository_type: RepositoryType, id: str, name: str, url: str, data: dict = {}):
        """Initializes class.
        """
        self._event_type = repository_type
        self._id = id
        self._name = name
        self._url = url
        super().__init__(event_type=self._event_type.value, extensions=self.create_extensions(), data=data)
        
    def create_extensions(self) -> dict:
        """Create extensions.
        """
        extensions = {
            "repositoryid": self._id,
            "repositoryname": self._name,
            "repositoryurl": self._url,
        }
        return extensions
