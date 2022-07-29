from cdevents.core import event_type
import pytest

from cdevents.core.events import Events

@pytest.mark.unit
def test_taskrun_started():
    event = Events().create_taskrun_event(event_type.TaskRunStartedEventV1, id="_id", name="_name", pipelineid="_pipelineid", data={"taskrun": "_taskrun"})
    assert event is not None
    assert event._attributes["type"] == event_type.TaskRunStartedEventV1
    assert event._attributes["extensions"] == {"taskrunid": "_id", "taskrunname": "_name", "taskrunpipelineid": "_pipelineid"}
    assert event.data == {"taskrun": "_taskrun"}

@pytest.mark.unit
def test_taskrun_finished():
    event = Events().create_taskrun_event(event_type.TaskRunFinishedEventV1, id="_id", name="_name", pipelineid="_pipelineid", data={"taskrun": "_taskrun"})
    assert event is not None
    assert event._attributes["type"] == event_type.TaskRunFinishedEventV1
    assert event._attributes["extensions"] == {"taskrunid": "_id", "taskrunname": "_name", "taskrunpipelineid": "_pipelineid"}
    assert event.data == {"taskrun": "_taskrun"}
