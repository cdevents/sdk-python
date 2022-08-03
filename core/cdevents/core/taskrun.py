"""taskrun"""

from enum import Enum
from cdevents.core.events import Events

class TaskRunType(Enum):
    TaskRunStartedEventV1  :str = "cd.taskrun.started.v1"
    TaskRunFinishedEventV1 :str = "cd.taskrun.finished.v1"


class TaskRun(Events):
    """Taskrun."""

    def __init__(self, taskrun_type: TaskRunType, id: str, name: str, pipelineid: str):
        """Initializes class.
        """
        self._event_type = taskrun_type
        self._id= id
        self._name = name
        self._pipelineid = pipelineid

        
    def create_extensions(self):
        """Create extensions.
        """
        extensions = {
            "taskrunid": self._id,
            "taskrunname": self._name,
            "taskrunpipelineid": self._pipelineid,
        }
        return extensions
    
    def create_event(self, data: dict={}):
        """Create taskrun event.
        """
        extensions = self.create_extensions()
        event = super().create_event(event_type=self._event_type.value, extensions=extensions, data=data)
        return event
