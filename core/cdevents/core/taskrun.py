"""Taskrun-related events."""

from cdevents.core.event import Event
from cdevents.core.event_type import EventType


class TaskRunEvent(Event):
    """Taskrun Event."""

    def __init__(
        self,
        taskrun_type: EventType,
        id: str,
        name: str,
        pipelineid: str,
        attrs=None,
        data: dict = {},
    ):
        """Initializes class."""
        self._event_type = taskrun_type
        self._id = id
        self._name = name
        self._pipelineid = pipelineid
        super().__init__(
            event_type=self._event_type.value,
            extensions=self.create_extensions(),
            attrs=attrs,
            data=data,
        )

    def create_extensions(self) -> dict:
        """Create extensions."""
        extensions = {
            "taskrunid": self._id,
            "taskrunname": self._name,
            "taskrunpipelineid": self._pipelineid,
        }
        return extensions


class TaskRunStartedEvent(TaskRunEvent):
    """TaskRun Started CDEvent."""

    def __init__(
        self, id: str = None, name: str = None, pipelineid: str = None, attrs=None, data: dict = {}
    ):
        """Initializes class."""
        self._event_type: str = EventType.TaskRunStartedEventV1

        super().__init__(
            taskrun_type=self._event_type,
            id=id,
            name=name,
            pipelineid=pipelineid,
            attrs=attrs,
            data=data,
        )


class TaskRunFinishedEvent(TaskRunEvent):
    """TaskRun Finished CDEvent."""

    def __init__(
        self, id: str = None, name: str = None, pipelineid: str = None, attrs=None, data: dict = {}
    ):
        """Initializes class."""
        self._event_type: str = EventType.TaskRunFinishedEventV1

        super().__init__(
            taskrun_type=self._event_type,
            id=id,
            name=name,
            pipelineid=pipelineid,
            attrs=attrs,
            data=data,
        )
