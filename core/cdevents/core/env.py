"""env"""

from cdevents.core.event import Event
from cdevents.core.event_type import EventType

class EnvEvent(Event):
    """Env Event."""

    def __init__(self, **kwargs):
        """Initializes class.
        """
        self._event_type : EventType = kwargs['env_type']
        if 'data' in kwargs:
            self._data :dict = kwargs['data']

        if 'id' in kwargs and 'name' in kwargs and 'repo' in kwargs:
            self._id :str = kwargs['id']
            self._name :str = kwargs['name']
            self._repo :str = kwargs['repo']
            super().__init__(event_type=self._event_type.value, extensions=self.create_extensions(), data=self._data)
        
        elif 'extensions' in kwargs:
            self._id = kwargs['extensions'].get('envId')
            self._name = kwargs['extensions'].get('envname')
            self._repo = kwargs['extensions'].get('envrepourl')
            super().__init__(event_type=self._event_type.value,  extensions=self.create_extensions(), data=self._data)
    
    def create_extensions(self) -> dict:
        """Create extensions.
        """
        extensions = {
            "envId": self._id,
            "envname": self._name,
            "envrepourl": self._repo,
        }
        return extensions

class EnvEventCreatedEvent(EnvEvent):
    
    def __init__(self, **kwargs):
        """Initializes class.
        """
        self._event_type: str = EventType.EnvironmentCreatedEventV1

        super().__init__(env_type=self._event_type, **kwargs) 

class EnvEventModifiedEvent(EnvEvent):
    
    def __init__(self, **kwargs):
        """Initializes class.
        """
        self._event_type: str = EventType.EnvironmentModifiedEventV1

        super().__init__(env_type=self._event_type, **kwargs)


class EnvEventDeletedEvent(EnvEvent):
    
    def __init__(self, **kwargs):
        """Initializes class.
        """
        self._event_type: str = EventType.EnvironmentDeletedEventV1

        super().__init__(env_type=self._event_type, **kwargs)

