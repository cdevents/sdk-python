import pytest

from cdevents.core.pipelinerun import Pipelinerun, PipelinerunType

@pytest.mark.unit
def test_pipelinerun_started():
    pipelinerun_event = Pipelinerun(pipelinerun_type=PipelinerunType.PipelineRunStartedEventV1, id="_id", name="_name", status="_status", url="_url", errors="_errors", data={"key1": "value1"})
    assert pipelinerun_event is not None
    assert pipelinerun_event._attributes["type"] == PipelinerunType.PipelineRunStartedEventV1.value
    assert pipelinerun_event._attributes["extensions"] == {"pipelinerunid": "_id", "pipelinerunname": "_name", "pipelinerunstatus": "_status", "pipelinerunurl": "_url", "pipelinerunerrors": "_errors"}
    assert pipelinerun_event.data == {"key1": "value1"}

@pytest.mark.unit
def test_pipelinerun_finished():
    pipelinerun_event = Pipelinerun(pipelinerun_type=PipelinerunType.PipelineRunFinishedEventV1, id="_id", name="_name", status="_status", url="_url", errors="_errors", data={"key1": "value1"})
    assert pipelinerun_event is not None
    assert pipelinerun_event._attributes["type"] == PipelinerunType.PipelineRunFinishedEventV1.value
    assert pipelinerun_event._attributes["extensions"] == {"pipelinerunid": "_id", "pipelinerunname": "_name", "pipelinerunstatus": "_status", "pipelinerunurl": "_url", "pipelinerunerrors": "_errors"}
    assert pipelinerun_event.data == {"key1": "value1"}

@pytest.mark.unit
def test_pipelinerun_queued():
    pipelinerun_event = Pipelinerun(pipelinerun_type=PipelinerunType.PipelineRunQueuedEventV1, id="_id", name="_name", status="_status", url="_url", errors="_errors", data={"key1": "value1"})
    assert pipelinerun_event is not None
    assert pipelinerun_event._attributes["type"] == PipelinerunType.PipelineRunQueuedEventV1.value
    assert pipelinerun_event._attributes["extensions"] == {"pipelinerunid": "_id", "pipelinerunname": "_name", "pipelinerunstatus": "_status", "pipelinerunurl": "_url", "pipelinerunerrors": "_errors"}
    assert pipelinerun_event.data == {"key1": "value1"}
