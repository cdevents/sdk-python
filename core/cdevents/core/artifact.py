"""artifact"""

from cdevents.core.event import Event
from cdevents.core.event_type import EventType


class ArtifactEvent(Event):
    """Artifact Event."""

    def __init__(
        self,
        artifact_type: EventType,
        id: str = None,
        name: str = None,
        version: str = None,
        attrs=None,
        data: dict = {},
    ):
        """Initializes class."""
        self._event_type = artifact_type
        self._id = id
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
            "artifactid": self._id,
            "artifactname": self._name,
            "artifactversion": self._version,
        }
        return extensions


class ArtifactPackagedEvent(ArtifactEvent):
    def __init__(
        self, id: str = None, name: str = None, version: str = None, attrs=None, data: dict = {}
    ):
        """Initializes class."""
        self._event_type: str = EventType.ArtifactPackagedEventV1

        super().__init__(
            artifact_type=self._event_type,
            id=id,
            name=name,
            version=version,
            attrs=attrs,
            data=data,
        )


class ArtifactPublishedEvent(ArtifactEvent):
    def __init__(
        self, id: str = None, name: str = None, version: str = None, attrs=None, data: dict = {}
    ):
        """Initializes class."""
        self._event_type: str = EventType.ArtifactPublishedEventV1

        super().__init__(
            artifact_type=self._event_type,
            id=id,
            name=name,
            version=version,
            attrs=attrs,
            data=data,
        )
