"""service"""

from enum import Enum
from cdevents.core.events import Events

class ServiceType(Enum):
    ServiceDeployedEventV1   :str = "cd.service.deployed.v1"
    ServiceUpgradedEventV1   :str = "cd.service.upgraded.v1"
    ServiceRolledbackEventV1 :str = "cd.service.rolledback.v1"
    ServiceRemovedEventV1    :str = "cd.service.removed.v1"


class Service(Events):
    """Service."""

    def __init__(self, service_type: ServiceType, envid: str, name: str, version: str):
        """Initializes class.
        """
        self._event_type = service_type
        self._envid = envid
        self._name = name
        self._version = version
        
    def create_extensions(self):
        """Create extensions.
        """
        extensions = {
            "serviceenvid": self._envid,
            "servicename": self._name,
            "serviceversion": self._version,
        }
        return extensions
    
    def create_event(self, data: dict={}):
        """Create Service event.
        """
        extensions = self.create_extensions()
        event = super().create_event(event_type=self._event_type.value, extensions=extensions, data=data)
        return event
