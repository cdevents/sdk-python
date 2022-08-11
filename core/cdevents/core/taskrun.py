"""taskrun"""

from enum import Enum
from cdevents.core.event import Event

class TaskRunType(Enum):
    TaskRunStartedEventV1  :str = "cd.taskrun.started.v1"
    TaskRunFinishedEventV1 :str = "cd.taskrun.finished.v1"


class TaskRunEvent(Event):
    """Taskrun Event."""

    def __init__(self, taskrun_type: TaskRunType, id: str, name: str, pipelineid: str, data: dict = {}):
        """Initializes class.
        """
        self._event_type = taskrun_type
        self._id= id
        self._name = name
        self._pipelineid = pipelineid
        super().__init__(event_type=self._event_type.value, extensions=self.create_extensions(), data=data)
 
    def create_extensions(self) -> dict:
        """Create extensions.
        """
        extensions = {
            "taskrunid": self._id,
            "taskrunname": self._name,
            "taskrunpipelineid": self._pipelineid,
        }
        return extensions

class TaskRunStartedEvent(TaskRunEvent):
    
    def __init__(self, id: str, name: str, pipelineid: str, data: dict = {}):
        """Initializes class.
        """
        self._event_type: str = TaskRunType.TaskRunStartedEventV1

        super().__init__(taskrun_type=self._event_type, id=id, name=name, pipelineid=pipelineid, data=data)

class TaskRunFinishedEvent(TaskRunEvent):
    
    def __init__(self, id: str, name: str, pipelineid: str, data: dict = {}):
        """Initializes class.
        """
        self._event_type: str = TaskRunType.TaskRunFinishedEventV1

        super().__init__(taskrun_type=self._event_type, id=id, name=name, pipelineid=pipelineid, data=data)
