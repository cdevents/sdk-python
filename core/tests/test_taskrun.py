import pytest
from cdevents.core.event_type import EventType
from cdevents.core.taskrun import (
    TaskRunEvent,
    TaskRunFinishedEvent,
    TaskRunStartedEvent,
)


@pytest.mark.unit
def test_taskrun_created():
    taskrun_event = TaskRunEvent(
        taskrun_type=EventType.TaskRunStartedEventV1,
        id="_id",
        name="_name",
        pipelineid="_pipelineid",
        data={"key1": "value1"},
    )
    assert taskrun_event is not None
    assert taskrun_event._attributes["type"] == EventType.TaskRunStartedEventV1.value
    assert taskrun_event._attributes["extensions"] == {
        "taskrunid": "_id",
        "taskrunname": "_name",
        "taskrunpipelineid": "_pipelineid",
    }
    assert taskrun_event.data == {"key1": "value1"}


@pytest.mark.unit
def test_taskrun_type_started_v1():
    taskrun_event = TaskRunStartedEvent(
        id="_id", name="_name", pipelineid="_pipelineid", data={"key1": "value1"}
    )
    assert taskrun_event is not None
    assert taskrun_event._attributes["type"] == EventType.TaskRunStartedEventV1.value
    assert taskrun_event._attributes["extensions"] == {
        "taskrunid": "_id",
        "taskrunname": "_name",
        "taskrunpipelineid": "_pipelineid",
    }
    assert taskrun_event.data == {"key1": "value1"}


@pytest.mark.unit
def test_taskrun_type_finished_v1():
    taskrun_event = TaskRunFinishedEvent(
        id="_id", name="_name", pipelineid="_pipelineid", data={"key1": "value1"}
    )
    assert taskrun_event is not None
    assert taskrun_event._attributes["type"] == EventType.TaskRunFinishedEventV1.value
    assert taskrun_event._attributes["extensions"] == {
        "taskrunid": "_id",
        "taskrunname": "_name",
        "taskrunpipelineid": "_pipelineid",
    }
    assert taskrun_event.data == {"key1": "value1"}
