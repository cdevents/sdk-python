"""Build-related events."""

from cdevents.core.event import Event
from cdevents.core.event_type import EventType


class BuildEvent(Event):
    """Build Event."""

    def __init__(
        self,
        build_type: EventType,
        id: str = None,
        name: str = None,
        artifact: str = None,
        attrs=None,
        data: dict = {},
    ):
        """Initializes class."""
        self._event_type = build_type
        self._id = id
        self._name = name
        self._artifact = artifact
        super().__init__(
            event_type=self._event_type.value,
            extensions=self.create_extensions(),
            attrs=attrs,
            data=data,
        )

    def create_extensions(self) -> dict:
        """Create extensions."""
        extensions = {
            "buildid": self._id,
            "buildname": self._name,
            "buildartifactid": self._artifact,
        }
        return extensions


class BuildStartedEvent(BuildEvent):
    """Build Started Event."""

    def __init__(
        self, id: str = None, name: str = None, artifact: str = None, attrs=None, data: dict = {}
    ):
        """Initializes class."""
        self._event_type: str = EventType.BuildStartedEventV1

        super().__init__(
            build_type=self._event_type, id=id, name=name, artifact=artifact, attrs=attrs, data=data
        )


class BuildQueuedEvent(BuildEvent):
    """Build Queued Event."""

    def __init__(
        self, id: str = None, name: str = None, artifact: str = None, attrs=None, data: dict = {}
    ):
        """Initializes class."""
        self._event_type: str = EventType.BuildQueuedEventV1

        super().__init__(
            build_type=self._event_type, id=id, name=name, artifact=artifact, attrs=attrs, data=data
        )


class BuildFinishedEvent(BuildEvent):
    """Build Finished Event."""

    def __init__(
        self, id: str = None, name: str = None, artifact: str = None, attrs=None, data: dict = {}
    ):
        """Initializes class."""
        self._event_type: str = EventType.BuildFinishedEventV1

        super().__init__(
            build_type=self._event_type, id=id, name=name, artifact=artifact, attrs=attrs, data=data
        )
