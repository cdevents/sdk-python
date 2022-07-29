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

    def create_artifact_event(self, event_type: str , id: str, name: str, version: str, data = {}) -> CloudEvent:
        """Create artifact event.
        """
        
        extensions = {
            "artifactid": id,
            "artifactname": name,
            "artifactversion": version,
        }
        event = self.create_event(event_type, extensions, data)

        return event

    def create_branch_event(self, event_type: str , id: str, name: str, repoid: str, data = {}) -> CloudEvent:
        """Create branch event.
        """
        
        extensions = {
            "branchid": id,
            "branchname": name,
            "branchrepositoryid": repoid,
        }
        event = self.create_event(event_type, extensions, data)

        return event


    def create_build_event(self, event_type: str , id: str, name: str, artifact: str, data = {}) -> CloudEvent:
        """Create build event.
        """
        
        extensions = {
            "buildid": id,
            "buildname": name,
            "buildartifactid": artifact,
        }
        event = self.create_event(event_type, extensions, data)

        return event

    def create_environment_event(self, event_type: str , id: str, name: str, repo: str, data = {}) -> CloudEvent:
        """Create environment event.
        """
            
        extensions = {
            "envId": id,
            "envname": name,
            "envrepourl": repo,
        }
        event = self.create_event(event_type, extensions, data)

        return event

    def create_pipelinerun_event(self, event_type: str , id: str, name: str, status: str, url: str, errors: str, data = {}) -> CloudEvent:
        """Create pipelinerun event.
        """
            
        extensions = {
            "pipelinerunid": id,
            "pipelinerunname": name,
            "pipelinerunstatus": status,
            "pipelinerunurl": url,
            "pipelinerunerrors": errors,
        }
        event = self.create_event(event_type, extensions, data)

        return event

    def create_repository_event(self, event_type: str , id: str, name: str, url: str, data = {}) -> CloudEvent:
        """Create repository event.
        """
            
        extensions = {
            "repositoryid": id,
            "repositoryname": name,
            "repositoryurl": url,
        }

        event = self.create_event(event_type, extensions, data)

        return event


    def create_service_event(self, event_type: str , envid: str, name: str, version: str, data = {}) -> CloudEvent:
        """Create service event.
        """
            
        extensions = {
            "serviceenvid": envid,
            "servicename": name,
            "serviceversion": version,
        }

        event = self.create_event(event_type, extensions, data)

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

