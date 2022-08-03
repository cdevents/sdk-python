"""Core events."""

from cloudevents.http import CloudEvent

class Events():
    """Events."""

    def __init__(self):
        """Initializes class.
        """

    def create_event(self, event_type: str, extensions:dict, data = {}) -> CloudEvent:
        """Create event.
        """ 
        attributes = {
            "type": event_type,
            "source": "cde-cli",
            "extensions": extensions,
        }

        event = CloudEvent(attributes, dict(data))

        return event


    def create_taskrun_event(self, event_type: str, id: str, name: str, pipelineid: str, data = {}) -> CloudEvent:
        """Create taskrun event.
        """
            
        extensions = {
            "taskrunid": id,
            "taskrunname": name,
            "taskrunpipelineid": pipelineid,
        }

        event = self.create_event(event_type, extensions, data)

        return event

