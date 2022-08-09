"""pipelinerun"""

from enum import Enum
from cdevents.core.event import Event

class PipelinerunType(Enum):
    PipelineRunStartedEventV1  :str = "cd.pipelinerun.started.v1"
    PipelineRunFinishedEventV1 :str = "cd.pipelinerun.finished.v1"
    PipelineRunQueuedEventV1   :str = "cd.pipelinerun.queued.v1"


class PipelinerunEvent(Event):
    """Pipelinerun Event."""

    def __init__(self, pipelinerun_type: PipelinerunType, id: str, name: str, status: str, url: str, errors: str, data: dict = {}):
        """Initializes class.
        """
        self._event_type = pipelinerun_type
        self._id = id
        self._name = name
        self._status = status
        self._url = url
        self._errors = errors
        super().__init__(event_type=self._event_type.value, extensions=self.create_extensions(), data=data)
        
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
    
