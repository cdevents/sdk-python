"""Repository-related events."""

from typing import Optional

from cdevents.core.event import Event
from cdevents.core.event_type import EventType


class RepositoryEvent(Event):
    """Repository Event."""

    def __init__(
        self,
        repository_type: EventType,
        id: Optional[str],
        name: Optional[str],
        url: Optional[str],
        attrs=None,
        data: dict = {},
    ):
        """Initializes class."""
        self._event_type = repository_type
        self._id = id
        self._name = name
        self._url = url
        super().__init__(
            event_type=self._event_type.value,
            extensions=self.create_extensions(),
            attrs=attrs,
            data=data,
        )

    def create_extensions(self) -> dict:
        """Create extensions."""
        extensions = {
            "repositoryid": self._id,
            "repositoryname": self._name,
            "repositoryurl": self._url,
        }
        return extensions


class RepositoryCreatedEvent(RepositoryEvent):
    """Repository Created CDEvent."""

    def __init__(
        self, id: str = None, name: str = None, url: str = None, attrs=None, data: dict = {}
    ):
        """Initializes class."""
        self._event_type: str = EventType.RepositoryCreatedEventV1

        super().__init__(
            repository_type=self._event_type, id=id, name=name, url=url, attrs=attrs, data=data
        )


class RepositoryModifiedEvent(RepositoryEvent):
    """Repository Modified CDEvent."""

    def __init__(
        self, id: str = None, name: str = None, url: str = None, attrs=None, data: dict = {}
    ):
        """Initializes class."""
        self._event_type: str = EventType.RepositoryModifiedEventV1

        super().__init__(
            repository_type=self._event_type, id=id, name=name, url=url, attrs=attrs, data=data
        )


class RepositoryDeletedEvent(RepositoryEvent):
    """Repository Deleted CDEvent."""

    def __init__(
        self, id: str = None, name: str = None, url: str = None, attrs=None, data: dict = {}
    ):
        """Initializes class."""
        self._event_type: str = EventType.RepositoryDeletedEventV1

        super().__init__(
            repository_type=self._event_type, id=id, name=name, url=url, attrs=attrs, data=data
        )
