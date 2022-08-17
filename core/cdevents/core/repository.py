"""repository"""

from cdevents.core.event import Event
from cdevents.core.event_type import EventType

class RepositoryEvent(Event):
    """Repository Event."""

    def __init__(self, **kwargs):
        """Initializes class.
        """
        self._event_type :EventType = kwargs['repository_type']
        if 'data' in kwargs:
            self._data :dict = kwargs['data']
        
        if 'id' in kwargs and 'name' in kwargs and 'url' in kwargs:
            self._id :str = kwargs['id']
            self._name :str = kwargs['name']
            self._url :str = kwargs['url']
        
        elif 'extensions' in kwargs:
            self._id = kwargs['extensions']['repositoryid']
            self._name = kwargs['extensions']['repositoryname']
            self._url = kwargs['extensions']['repositoryurl']

        super().__init__(event_type=self._event_type.value, extensions=self.create_extensions(), data=self._data)

    def create_extensions(self) -> dict:
        """Create extensions.
        """
        extensions = {
            "repositoryid": self._id,
            "repositoryname": self._name,
            "repositoryurl": self._url,
        }
        return extensions

class RepositoryCreatedEvent(RepositoryEvent):
    
    def __init__(self, **kwargs):
        """Initializes class.
        """
        self._event_type: str = EventType.RepositoryCreatedEventV1

        super().__init__(repository_type=self._event_type, **kwargs)

class RepositoryModifiedEvent(RepositoryEvent):
    
    def __init__(self, **kwargs):
        """Initializes class.
        """
        self._event_type: str = EventType.RepositoryModifiedEventV1

        super().__init__(repository_type=self._event_type, **kwargs)

class RepositoryDeletedEvent(RepositoryEvent):
    
    def __init__(self, **kwargs):
        """Initializes class.
        """
        self._event_type: str = EventType.RepositoryDeletedEventV1

        super().__init__(repository_type=self._event_type, **kwargs)

