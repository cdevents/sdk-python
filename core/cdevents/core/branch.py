"""branch"""

from cdevents.core.event import Event
from cdevents.core.event_type import EventType

class BranchEvent(Event):
    """Branch Event."""

    def __init__(self, **kwargs):
        """Initializes class.
        """
        self._event_type : EventType = kwargs['branch_type']
      
        if 'data' in kwargs:
            self._data :dict = kwargs['data']
        
        if 'id' in kwargs and 'name' in kwargs and 'repoid' in kwargs:
            self._id :str = kwargs['id']
            self._name :str = kwargs['name']
            self._repoid :str = kwargs['repoid']
            super().__init__(event_type=self._event_type.value, extensions=self.create_extensions(), data=self._data)
        elif 'extensions' in kwargs:
            self._id = kwargs['extensions'].get('branchid')
            self._name = kwargs['extensions'].get('branchname')
            self._repoid = kwargs['extensions'].get('branchrepositoryid')
            super().__init__(event_type=self._event_type.value,  extensions=self.create_extensions(), data=self._data)

    def create_extensions(self) -> dict:
        """Create extensions.
        """
        extensions = {
            "branchid": self._id,
            "branchname": self._name,
            "branchrepositoryid": self._repoid,
        }
        return extensions

class BranchCreatedEvent(BranchEvent):
    
    def __init__(self, **kwargs):
        """Initializes class.
        """
        self._event_type: str = EventType.BranchCreatedEventV1

        super().__init__(branch_type=self._event_type, **kwargs)

class BranchDeletedEvent(BranchEvent):
    
    def __init__(self, **kwargs):
        """Initializes class.
        """
        self._event_type: str = EventType.BranchDeletedEventV1

        super().__init__(branch_type=self._event_type, **kwargs)
