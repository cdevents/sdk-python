"""env"""

from cdevents.core.event import Event
from cdevents.core.event_type import EventType

class EnvEvent(Event):
    """Env Event."""

    def __init__(self, env_type: EventType, id: str, name: str, repo: str, attrs=None, data: dict = {}):
        """Initializes class.
        """
        self._event_type = env_type
        self._id = id
        self._name = name
        self._repo = repo
        super().__init__(event_type=self._event_type.value, extensions=self.create_extensions(), attrs=attrs, data=data)
    
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
    
    def __init__(self, id: str=None, name: str=None, repo: str=None, attrs=None, data: dict = {}):
        """Initializes class.
        """
        self._event_type: str = EventType.EnvironmentCreatedEventV1

        super().__init__(env_type=self._event_type, id=id, name=name, repo=repo, attrs=attrs, data=data)

class EnvEventModifiedEvent(EnvEvent):
    
    def __init__(self, id: str=None, name: str=None, repo: str=None, attrs=None, data: dict = {}):
        """Initializes class.
        """
        self._event_type: str = EventType.EnvironmentModifiedEventV1

        super().__init__(env_type=self._event_type, id=id, name=name, repo=repo, attrs=attrs, data=data)

class EnvEventDeletedEvent(EnvEvent):
    
    def __init__(self, id: str=None, name: str=None, repo: str=None, attrs=None, data: dict = {}):
        """Initializes class.
        """
        self._event_type: str = EventType.EnvironmentDeletedEventV1

        super().__init__(env_type=self._event_type, id=id, name=name, repo=repo, attrs=attrs, data=data)

