"""pipelinerun"""

from cdevents.core.event import Event
from cdevents.core.event_type import EventType

class PipelinerunEvent(Event):
    """Pipelinerun Event."""

    def __init__(self, **kwargs):
        """Initializes class.
        """
        self._event_type : EventType = kwargs['pipelinerun_type']
        if 'data' in kwargs:
            self._data :dict = kwargs['data']
        
        if 'id' in kwargs and 'name' in kwargs and 'status' in kwargs and 'url' in kwargs and 'errors' in kwargs:
            self._id :str = kwargs['id']
            self._name :str = kwargs['name']
            self._status :str = kwargs['status']
            self._url :str = kwargs['url']
            self._errors :str = kwargs['errors']
            super().__init__(event_type=self._event_type.value, extensions=self.create_extensions(), data=self._data)
        
        elif 'extensions' in kwargs:
            self._id = kwargs['extensions'].get('pipelinerunid')
            self._name = kwargs['extensions'].get('pipelinerunname')
            self._status = kwargs['extensions'].get('pipelinerunstatus')
            self._url = kwargs['extensions'].get('pipelinerunurl')
            self._errors = kwargs['extensions'].get('pipelinerunerrors')
            super().__init__(event_type=self._event_type.value,  extensions=self.create_extensions(), data=self._data)
        
    def create_extensions(self) -> dict:
        """Create extensions.
        """
        extensions = {
            "pipelinerunid": self._id,
            "pipelinerunname": self._name,
            "pipelinerunstatus": self._status,
            "pipelinerunurl": self._url,
            "pipelinerunerrors": self._errors,
        }
        return extensions
    
class PipelinerunStartedEvent(PipelinerunEvent):
    
    def __init__(self, **kwargs):
        """Initializes class.
        """
        self._event_type: str = EventType.PipelineRunStartedEventV1

        super().__init__(pipelinerun_type=self._event_type, **kwargs)
    
class PipelinerunFinishedEvent(PipelinerunEvent):
    
    def __init__(self, **kwargs):
        """Initializes class.
        """
        self._event_type: str = EventType.PipelineRunFinishedEventV1

        super().__init__(pipelinerun_type=self._event_type, **kwargs)
    
class PipelinerunQueuedEvent(PipelinerunEvent):
    
    def __init__(self, **kwargs):
        """Initializes class.
        """
        self._event_type: str = EventType.PipelineRunQueuedEventV1

        super().__init__(pipelinerun_type=self._event_type, **kwargs)
