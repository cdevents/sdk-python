import pytest

from cdevents.core.build import BuildEvent, BuildType

@pytest.mark.unit
def test_build_started():
    build_event = BuildEvent(build_type=BuildType.BuildStartedEventV1, id="_id", name="_name", artifact="_artifact", data={"key1": "value1"})
    assert build_event is not None
    assert build_event._attributes["type"] == BuildType.BuildStartedEventV1.value
    assert build_event._attributes["extensions"] == {"buildid": "_id", "buildname": "_name", "buildartifactid": "_artifact"}
    assert build_event.data == {"key1": "value1"}

@pytest.mark.unit
def test_build_queued():
    build_event = BuildEvent(build_type=BuildType.BuildQueuedEventV1, id="_id", name="_name", artifact="_artifact", data={"key1": "value1"})
    assert build_event is not None
    assert build_event._attributes["type"] == BuildType.BuildQueuedEventV1.value
    assert build_event._attributes["extensions"] == {"buildid": "_id", "buildname": "_name", "buildartifactid": "_artifact"}
    assert build_event.data == {"key1": "value1"}

@pytest.mark.unit
def test_build_finished():
    build_event = BuildEvent(build_type=BuildType.BuildFinishedEventV1, id="_id", name="_name", artifact="_artifact", data={"key1": "value1"})
    assert build_event is not None
    assert build_event._attributes["type"] == BuildType.BuildFinishedEventV1.value
    assert build_event._attributes["extensions"] == {"buildid": "_id", "buildname": "_name", "buildartifactid": "_artifact"}
    assert build_event.data == {"key1": "value1"}
