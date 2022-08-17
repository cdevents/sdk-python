"""taskrun"""

from cdevents.core.event import Event
from cdevents.core.event_type import EventType

class TaskRunEvent(Event):
    """Taskrun Event."""

    def __init__(self, **kwargs):
        """Initializes class.
        """
        self._event_type :EventType = kwargs['taskrun_type']
        if 'data' in kwargs:
            self._data :dict = kwargs['data']
        
        if 'id' in kwargs and 'name' in kwargs and 'pipelineid' in kwargs:
            self._id :str = kwargs['id']
            self._name :str = kwargs['name']
            self._pipelineid :str = kwargs['pipelineid']
        
        elif 'extensions' in kwargs:
            self._id = kwargs['extensions']['taskrunid']
            self._name = kwargs['extensions']['taskrunname']
            self._pipelineid = kwargs['extensions']['taskrunpipelineid']
        
        super().__init__(event_type=self._event_type.value, extensions=self.create_extensions(), data=self._data)
        
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
    
    def __init__(self, **kwargs):
        """Initializes class.
        """
        self._event_type: str = EventType.TaskRunStartedEventV1

        super().__init__(taskrun_type=self._event_type, **kwargs)

class TaskRunFinishedEvent(TaskRunEvent):
    
    def __init__(self, **kwargs):
        """Initializes class.
        """
        self._event_type: str = EventType.TaskRunFinishedEventV1

        super().__init__(taskrun_type=self._event_type, **kwargs)
