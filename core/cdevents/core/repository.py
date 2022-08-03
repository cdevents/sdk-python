"""repository"""

from enum import Enum
from cdevents.core.events import Events

class RepositoryType(Enum):
    RepositoryCreatedEventV1  :str = "cd.repository.created.v1"
    RepositoryModifiedEventV1 :str = "cd.repository.modified.v1"
    RepositoryDeletedEventV1  :str = "cd.repository.deleted.v1"


class Repository(Events):
    """Repository."""

    def __init__(self, repository_type: RepositoryType, id: str, name: str, url: str):
        """Initializes class.
        """
        self._event_type = repository_type
        self._id = id
        self._name = name
        self._url = url
        
    def create_extensions(self):
        """Create extensions.
        """
        extensions = {
            "repositoryid": self._id,
            "repositoryname": self._name,
            "repositoryurl": self._url,
        }
        return extensions
    
    def create_event(self, data: dict={}):
        """Create Repository event.
        """
        extensions = self.create_extensions()
        event = super().create_event(event_type=self._event_type.value, extensions=extensions, data=data)
        return event
