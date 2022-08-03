"""branch"""

from enum import Enum
from cdevents.core.events import Events

class BranchType(Enum):
    BranchCreatedEventV1: str = "cd.repository.branch.created.v1"
    BranchDeletedEventV1: str = "cd.repository.branch.deleted.v1"


class Branch(Events):
    """Brach."""

    def __init__(self, branch_type: BranchType, id: str, name: str, repoid: str):
        """Initializes class.
        """
        self._event_type = branch_type
        self._id = id
        self._name = name
        self._repoid = repoid
    
    def create_extensions(self):
        """Create extensions.
        """
        extensions = {
            "branchid": self._id,
            "branchname": self._name,
            "branchrepositoryid": self._repoid,
        }
        return extensions
    
    def create_event(self, data: dict={}):
        """Create branch event.
        """
        extensions = self.create_extensions()
        event = super().create_event(event_type=self._event_type.value, extensions=extensions, data=data)
        return event
