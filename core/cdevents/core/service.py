"""service"""

from cdevents.core.event import Event
from cdevents.core.event_type import EventType


class ServiceEvent(Event):
    """Service Event."""

    def __init__(
        self,
        service_type: EventType,
        envid: str,
        name: str,
        version: str,
        attrs=None,
        data: dict = {},
    ):
        """Initializes class."""
        self._event_type = service_type
        self._envid = envid
        self._name = name
        self._version = version
        super().__init__(
            event_type=self._event_type.value,
            extensions=self.create_extensions(),
            attrs=attrs,
            data=data,
        )

    def create_extensions(self) -> dict:
        """Create extensions."""
        extensions = {
            "serviceenvid": self._envid,
            "servicename": self._name,
            "serviceversion": self._version,
        }
        return extensions


class ServiceDeployedEvent(ServiceEvent):
    def __init__(
        self, envid: str = None, name: str = None, version: str = None, attrs=None, data: dict = {}
    ):
        """Initializes class."""
        self._event_type: str = EventType.ServiceDeployedEventV1

        super().__init__(
            service_type=self._event_type,
            envid=envid,
            name=name,
            version=version,
            attrs=attrs,
            data=data,
        )


class ServiceUpgradedEvent(ServiceEvent):
    def __init__(
        self, envid: str = None, name: str = None, version: str = None, attrs=None, data: dict = {}
    ):
        """Initializes class."""
        self._event_type: str = EventType.ServiceUpgradedEventV1

        super().__init__(
            service_type=self._event_type,
            envid=envid,
            name=name,
            version=version,
            attrs=attrs,
            data=data,
        )


class ServiceRolledbackEvent(ServiceEvent):
    def __init__(
        self, envid: str = None, name: str = None, version: str = None, attrs=None, data: dict = {}
    ):
        """Initializes class."""
        self._event_type: str = EventType.ServiceRolledbackEventV1

        super().__init__(
            service_type=self._event_type,
            envid=envid,
            name=name,
            version=version,
            attrs=attrs,
            data=data,
        )


class ServiceRemovedEvent(ServiceEvent):
    def __init__(
        self, envid: str = None, name: str = None, version: str = None, attrs=None, data: dict = {}
    ):
        """Initializes class."""
        self._event_type: str = EventType.ServiceRemovedEventV1

        super().__init__(
            service_type=self._event_type,
            envid=envid,
            name=name,
            version=version,
            attrs=attrs,
            data=data,
        )
