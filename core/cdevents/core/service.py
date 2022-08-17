"""service"""

from cdevents.core.event import Event
from cdevents.core.event_type import EventType

class ServiceEvent(Event):
    """Service Event."""

    def __init__(self, **kwargs):
        """Initializes class.
        """
        self._event_type :EventType = kwargs['service_type']
        if 'data' in kwargs:
            self._data :dict = kwargs['data']
        
        if 'envid' in kwargs and 'name' in kwargs and 'version' in kwargs:
            self._envid :str = kwargs['envid']
            self._name :str = kwargs['name']
            self._version :str = kwargs['version']
        
        elif 'extensions' in kwargs:
            self._envid = kwargs['extensions']['serviceenvid']
            self._name = kwargs['extensions']['servicename']
            self._version = kwargs['extensions']['serviceversion']
        
        super().__init__(event_type=self._event_type.value, extensions=self.create_extensions(), data=self._data)
        
    def create_extensions(self) -> dict:
        """Create extensions.
        """
        extensions = {
            "serviceenvid": self._envid,
            "servicename": self._name,
            "serviceversion": self._version,
        }
        return extensions

class ServiceDeployedEvent(ServiceEvent):
    
    def __init__(self, **kwargs):
        """Initializes class.
        """
        self._event_type: str = EventType.ServiceDeployedEventV1

        super().__init__(service_type=self._event_type, **kwargs)

class ServiceUpgradedEvent(ServiceEvent):
    
    def __init__(self, **kwargs):
        """Initializes class.
        """
        self._event_type: str = EventType.ServiceUpgradedEventV1

        super().__init__(service_type=self._event_type, **kwargs)

class ServiceRolledbackEvent(ServiceEvent):
    
    def __init__(self, **kwargs):
        """Initializes class.
        """
        self._event_type: str = EventType.ServiceRolledbackEventV1

        super().__init__(service_type=self._event_type, **kwargs)

class ServiceRemovedEvent(ServiceEvent):
    
    def __init__(self, **kwargs):
        """Initializes class.
        """
        self._event_type: str = EventType.ServiceRemovedEventV1

        super().__init__(service_type=self._event_type, **kwargs)

