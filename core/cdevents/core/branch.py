"""Branch-related events."""

from cdevents.core.event import Event
from cdevents.core.event_type import EventType


class BranchEvent(Event):
    """Branch Event."""

    def __init__(
        self,
        branch_type: EventType,
        id: str = None,
        name: str = None,
        repoid: str = None,
        attrs=None,
        data: dict = {},
    ):
        """Initializes class."""
        self._event_type = branch_type
        self._id = id
        self._name = name
        self._repoid = repoid
        super().__init__(
            event_type=self._event_type.value,
            extensions=self.create_extensions(),
            attrs=attrs,
            data=data,
        )

    def create_extensions(self) -> dict:
        """Create extensions."""
        extensions = {
            "branchid": self._id,
            "branchname": self._name,
            "branchrepositoryid": self._repoid,
        }
        return extensions


class BranchCreatedEvent(BranchEvent):
    """Branch created event."""

    def __init__(
        self, id: str = None, name: str = None, repoid: str = None, attrs=None, data: dict = {}
    ):
        """Initializes class."""
        self._event_type: str = EventType.BranchCreatedEventV1

        super().__init__(
            branch_type=self._event_type, id=id, name=name, repoid=repoid, attrs=attrs, data=data
        )


class BranchDeletedEvent(BranchEvent):
    """Branch deleted event."""

    def __init__(
        self, id: str = None, name: str = None, repoid: str = None, attrs=None, data: dict = {}
    ):
        """Initializes class."""
        self._event_type: str = EventType.BranchDeletedEventV1

        super().__init__(
            branch_type=self._event_type, id=id, name=name, repoid=repoid, attrs=attrs, data=data
        )
