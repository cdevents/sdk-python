"""pipelinerun"""

from cdevents.core.event import Event
from cdevents.core.event_type import EventType


class PipelinerunEvent(Event):
    """Pipelinerun Event."""

    def __init__(
        self,
        pipelinerun_type: EventType,
        id: str,
        name: str,
        status: str,
        url: str,
        errors: str,
        attrs=None,
        data: dict = {},
    ):
        """Initializes class."""
        self._event_type = pipelinerun_type
        self._id = id
        self._name = name
        self._status = status
        self._url = url
        self._errors = errors
        super().__init__(
            event_type=self._event_type.value,
            extensions=self.create_extensions(),
            attrs=attrs,
            data=data,
        )

    def create_extensions(self) -> dict:
        """Create extensions."""
        extensions = {
            "pipelinerunid": self._id,
            "pipelinerunname": self._name,
            "pipelinerunstatus": self._status,
            "pipelinerunurl": self._url,
            "pipelinerunerrors": self._errors,
        }
        return extensions


class PipelinerunStartedEvent(PipelinerunEvent):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        status: str = None,
        url: str = None,
        errors: str = None,
        attrs=None,
        data: dict = {},
    ):
        """Initializes class."""
        self._event_type: str = EventType.PipelineRunStartedEventV1

        super().__init__(
            pipelinerun_type=self._event_type,
            id=id,
            name=name,
            status=status,
            url=url,
            errors=errors,
            attrs=attrs,
            data=data,
        )


class PipelinerunFinishedEvent(PipelinerunEvent):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        status: str = None,
        url: str = None,
        errors: str = None,
        attrs=None,
        data: dict = {},
    ):
        """Initializes class."""
        self._event_type: str = EventType.PipelineRunFinishedEventV1

        super().__init__(
            pipelinerun_type=self._event_type,
            id=id,
            name=name,
            status=status,
            url=url,
            errors=errors,
            attrs=attrs,
            data=data,
        )


class PipelinerunQueuedEvent(PipelinerunEvent):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        status: str = None,
        url: str = None,
        errors: str = None,
        attrs=None,
        data: dict = {},
    ):
        """Initializes class."""
        self._event_type: str = EventType.PipelineRunQueuedEventV1

        super().__init__(
            pipelinerun_type=self._event_type,
            id=id,
            name=name,
            status=status,
            url=url,
            errors=errors,
            attrs=attrs,
            data=data,
        )
