import pytest

from cdevents.core.pipelinerun import PipelinerunEvent, PipelinerunStartedEvent, PipelinerunFinishedEvent, PipelinerunQueuedEvent
from cdevents.core.event_type import EventType

@pytest.mark.unit
def test_pipelinerun_created():
    pipelinerun_event = PipelinerunEvent(pipelinerun_type=EventType.PipelineRunStartedEventV1, id="_id", name="_name", status="_status", url="_url", errors="_errors", data={"key1": "value1"})
    assert pipelinerun_event is not None
    assert pipelinerun_event._attributes["type"] == EventType.PipelineRunStartedEventV1.value
    assert pipelinerun_event._attributes["extensions"] == {"pipelinerunid": "_id", "pipelinerunname": "_name", "pipelinerunstatus": "_status", "pipelinerunurl": "_url", "pipelinerunerrors": "_errors"}
    assert pipelinerun_event.data == {"key1": "value1"}

@pytest.mark.unit
def test_pipelinerun_type_started_v1():
    pipelinerun_event = PipelinerunStartedEvent(id="_id", name="_name", status="_status", url="_url", errors="_errors", data={"key1": "value1"})
    assert pipelinerun_event is not None
    assert pipelinerun_event._attributes["type"] == EventType.PipelineRunStartedEventV1.value
    assert pipelinerun_event._attributes["extensions"] == {"pipelinerunid": "_id", "pipelinerunname": "_name", "pipelinerunstatus": "_status", "pipelinerunurl": "_url", "pipelinerunerrors": "_errors"}
    assert pipelinerun_event.data == {"key1": "value1"}

@pytest.mark.unit
def test_pipelinerun_type_finished_v1():
    pipelinerun_event = PipelinerunFinishedEvent( id="_id", name="_name", status="_status", url="_url", errors="_errors", data={"key1": "value1"})
    assert pipelinerun_event is not None
    assert pipelinerun_event._attributes["type"] == EventType.PipelineRunFinishedEventV1.value
    assert pipelinerun_event._attributes["extensions"] == {"pipelinerunid": "_id", "pipelinerunname": "_name", "pipelinerunstatus": "_status", "pipelinerunurl": "_url", "pipelinerunerrors": "_errors"}
    assert pipelinerun_event.data == {"key1": "value1"}

@pytest.mark.unit
def test_pipelinerun_type_queued_v1():
    pipelinerun_event = PipelinerunQueuedEvent(id="_id", name="_name", status="_status", url="_url", errors="_errors", data={"key1": "value1"})
    assert pipelinerun_event is not None
    assert pipelinerun_event._attributes["type"] == EventType.PipelineRunQueuedEventV1.value
    assert pipelinerun_event._attributes["extensions"] == {"pipelinerunid": "_id", "pipelinerunname": "_name", "pipelinerunstatus": "_status", "pipelinerunurl": "_url", "pipelinerunerrors": "_errors"}
    assert pipelinerun_event.data == {"key1": "value1"}
