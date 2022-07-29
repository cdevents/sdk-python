from pickle import NONE
from cdevents.core import event_type
import pytest

from cdevents.core.events import Events

@pytest.mark.unit
def test_pipelinerun_started():
    event = Events().create_pipelinerun_event(event_type.PipelineRunStartedEventV1, id="_id", name="_name", status="_status", url="_url", errors="_errors", data={"pipelinerun": "_pipelinerun"})
    assert event is not None
    assert event._attributes["type"] == event_type.PipelineRunStartedEventV1
    assert event._attributes["extensions"] ==  {"pipelinerunid": "_id", "pipelinerunname": "_name", "pipelinerunstatus": "_status", "pipelinerunurl": "_url", "pipelinerunerrors": "_errors"}
    assert event.data == {"pipelinerun": "_pipelinerun"}

@pytest.mark.unit
def test_pipelinerun_finished():
    event = Events().create_pipelinerun_event(event_type.PipelineRunFinishedEventV1, id="_id", name="_name", status="_status", url="_url", errors="_errors", data={"pipelinerun": "_pipelinerun"})
    assert event is not None
    assert event._attributes["type"] == event_type.PipelineRunFinishedEventV1
    assert event._attributes["extensions"] ==  {"pipelinerunid": "_id", "pipelinerunname": "_name", "pipelinerunstatus": "_status", "pipelinerunurl": "_url", "pipelinerunerrors": "_errors"}
    assert event.data == {"pipelinerun": "_pipelinerun"}

@pytest.mark.unit
def test_pipelinerun_queued():
    event = Events().create_pipelinerun_event(event_type.PipelineRunQueuedEventV1, id="_id", name="_name", status="_status", url="_url", errors="_errors", data={"pipelinerun": "_pipelinerun"})
    assert event is not None
    assert event._attributes["type"] == event_type.PipelineRunQueuedEventV1
    assert event._attributes["extensions"] ==  {"pipelinerunid": "_id", "pipelinerunname": "_name", "pipelinerunstatus": "_status", "pipelinerunurl": "_url", "pipelinerunerrors": "_errors"}
    assert event.data == {"pipelinerun": "_pipelinerun"}
