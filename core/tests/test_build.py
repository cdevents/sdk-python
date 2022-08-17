import pytest

from cdevents.core.event_type import EventType
from cdevents.core.build import BuildEvent, BuildStartedEvent, BuildQueuedEvent, BuildFinishedEvent

@pytest.mark.unit
def test_build_created():
    build_event = BuildEvent(build_type=EventType.BuildStartedEventV1, id="_id", name="_name", artifact="_artifact", data={"key1": "value1"})
    assert build_event is not None
    assert build_event._attributes["type"] == EventType.BuildStartedEventV1.value
    assert build_event._attributes["extensions"] == {"buildid": "_id", "buildname": "_name", "buildartifactid": "_artifact"}
    assert build_event.data == {"key1": "value1"}

@pytest.mark.unit
def test_build_type_started_v1():
    build_event = BuildStartedEvent(id="_id", name="_name", artifact="_artifact", data={"key1": "value1"})
    assert build_event is not None
    assert build_event._attributes["type"] == EventType.BuildStartedEventV1.value
    assert build_event._attributes["extensions"] == {"buildid": "_id", "buildname": "_name", "buildartifactid": "_artifact"}
    assert build_event.data == {"key1": "value1"}

@pytest.mark.unit
def test_build_type_queued_v1():
    build_event = BuildQueuedEvent(id="_id", name="_name", artifact="_artifact", data={"key1": "value1"})
    assert build_event is not None
    assert build_event._attributes["type"] == EventType.BuildQueuedEventV1.value
    assert build_event._attributes["extensions"] == {"buildid": "_id", "buildname": "_name", "buildartifactid": "_artifact"}
    assert build_event.data == {"key1": "value1"}

@pytest.mark.unit
def test_build_type_finished_v1():
    build_event = BuildFinishedEvent(id="_id", name="_name", artifact="_artifact", data={"key1": "value1"})
    assert build_event is not None
    assert build_event._attributes["type"] == EventType.BuildFinishedEventV1.value
    assert build_event._attributes["extensions"] == {"buildid": "_id", "buildname": "_name", "buildartifactid": "_artifact"}
    assert build_event.data == {"key1": "value1"}
