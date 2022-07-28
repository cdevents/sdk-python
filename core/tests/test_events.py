

from pickle import NONE
from cdevents.core import event_type
import pytest

from cdevents.core.events import Events


@pytest.mark.unit
def test_create_event():
    event = Events().create_event(event_type="event_type", extensions={"test": "test"})
    assert event is not None
    assert event._attributes["type"] == "event_type"
    assert event._attributes["extensions"] == {"test": "test"}

@pytest.mark.unit
def test_create_artifact_event():
    event = Events().create_artifact_event(event_type.ArtifactPackagedEventV1, id="_id", name="_name", version="_version", data={"artifact": "_artifact"})
    assert event is not None
    assert event._attributes["type"] == event_type.ArtifactPackagedEventV1
    assert event._attributes["extensions"] == {"artifactid": "_id", "artifactname": "_name", "artifactversion": "_version"}
    assert event.data == {"artifact": "_artifact"}

@pytest.mark.unit
def test_create_branch_event():
    event = Events().create_branch_event(event_type.BranchCreatedEventV1, id="_id", name="_name", repoid="_repoid", data={"branch": "_branch"})
    assert event is not None
    assert event._attributes["type"] == event_type.BranchCreatedEventV1
    assert event._attributes["extensions"] == {"branchid": "_id", "branchname": "_name", "branchrepositoryid": "_repoid"}
    assert event.data == {"branch": "_branch"}

@pytest.mark.unit
def test_create_build_event():
    event = Events().create_build_event(event_type.BuildFinishedEventV1, id="_id", name="_name", artifact="_artifact", data={"build": "_build"})
    assert event is not None
    assert event._attributes["type"] == event_type.BuildFinishedEventV1
    assert event._attributes["extensions"] == {"buildid": "_id", "buildname": "_name", "buildartifactid": "_artifact"}
    assert event.data == {"build": "_build"}

@pytest.mark.unit
def test_create_environment_event():
    event = Events().create_environment_event(event_type.EnvironmentCreatedEventV1, id="_id", name="_name", repo="_repo", data={"environment": "_environment"})
    assert event is not None
    assert event._attributes["type"] == event_type.EnvironmentCreatedEventV1
    assert event._attributes["extensions"] == {"envId": "_id", "envname": "_name", "envrepourl": "_repo"}
    assert event.data == {"environment": "_environment"} 

@pytest.mark.unit
def test_create_pipelinerun_event():
    event = Events().create_pipelinerun_event(event_type.PipelineRunFinishedEventV1, id="_id", name="_name", status="_status", url="_url", errors="_errors", data={"pipelinerun": "_pipelinerun"})
    assert event is not None
    assert event._attributes["type"] == event_type.PipelineRunFinishedEventV1
    assert event._attributes["extensions"] ==  {"pipelinerunid": "_id", "pipelinerunname": "_name", "pipelinerunstatus": "_status", "pipelinerunurl": "_url", "pipelinerunerrors": "_errors"}
    assert event.data == {"pipelinerun": "_pipelinerun"}

@pytest.mark.unit
def test_create_service_event():
    event = Events().create_service_event(event_type.ServiceDeployedEventV1, envid="_envid", name="_name", version="_version", data={"service": "_service"})
    assert event is not None
    assert event._attributes["type"] == event_type.ServiceDeployedEventV1
    assert event._attributes["extensions"] == {"serviceenvid": "_envid", "servicename": "_name", "serviceversion": "_version"}
    assert event.data == {"service": "_service"}


@pytest.mark.unit
def test_create_taskrun_event():
    event = Events().create_taskrun_event(event_type.TaskRunFinishedEventV1, id="_id", name="_name", pipelineid="_pipelineid", data={"taskrun": "_taskrun"})
    assert event is not None
    assert event._attributes["type"] == event_type.TaskRunFinishedEventV1
    assert event._attributes["extensions"] == {"taskrunid": "_id", "taskrunname": "_name", "taskrunpipelineid": "_pipelineid"}
    assert event.data == {"taskrun": "_taskrun"}
