"""service"""

from enum import Enum
from cdevents.core.event import Event

class ServiceType(Enum):
    ServiceDeployedEventV1   :str = "cd.service.deployed.v1"
    ServiceUpgradedEventV1   :str = "cd.service.upgraded.v1"
    ServiceRolledbackEventV1 :str = "cd.service.rolledback.v1"
    ServiceRemovedEventV1    :str = "cd.service.removed.v1"


class ServiceEvent(Event):
    """Service Event."""

    def __init__(self, service_type: ServiceType, envid: str, name: str, version: str, data: dict = {}):
        """Initializes class.
        """
        self._event_type = service_type
        self._envid = envid
        self._name = name
        self._version = version
        super().__init__(event_type=self._event_type.value, extensions=self.create_extensions(), data=data)
        
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
    
    def __init__(self, envid: str, name: str, version: str, data: dict = {}):
        """Initializes class.
        """
        self._event_type: str = ServiceType.ServiceDeployedEventV1

        super().__init__(service_type=self._event_type, envid=envid, name=name, version=version, data=data)

class ServiceUpgradedEvent(ServiceEvent):
    
    def __init__(self, envid: str, name: str, version: str, data: dict = {}):
        """Initializes class.
        """
        self._event_type: str = ServiceType.ServiceUpgradedEventV1

        super().__init__(service_type=self._event_type, envid=envid, name=name, version=version, data=data)

class ServiceRolledbackEvent(ServiceEvent):
    
    def __init__(self, envid: str, name: str, version: str, data: dict = {}):
        """Initializes class.
        """
        self._event_type: str = ServiceType.ServiceRolledbackEventV1

        super().__init__(service_type=self._event_type, envid=envid, name=name, version=version, data=data)

class ServiceRemovedEvent(ServiceEvent):
    
    def __init__(self, envid: str, name: str, version: str, data: dict = {}):
        """Initializes class.
        """
        self._event_type: str = ServiceType.ServiceRemovedEventV1

        super().__init__(service_type=self._event_type, envid=envid, name=name, version=version, data=data)

