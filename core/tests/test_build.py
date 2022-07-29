from cdevents.core import event_type
import pytest

from cdevents.core.events import Events

@pytest.mark.unit
def test_build_started():
    event = Events().create_build_event(event_type.BuildStartedEventV1, id="_id", name="_name", artifact="_artifact", data={"build": "_build"})
    assert event is not None
    assert event._attributes["type"] == event_type.BuildStartedEventV1
    assert event._attributes["extensions"] == {"buildid": "_id", "buildname": "_name", "buildartifactid": "_artifact"}
    assert event.data == {"build": "_build"}

@pytest.mark.unit
def test_build_queued():
    event = Events().create_build_event(event_type.BuildQueuedEventV1, id="_id", name="_name", artifact="_artifact", data={"build": "_build"})
    assert event is not None
    assert event._attributes["type"] == event_type.BuildQueuedEventV1
    assert event._attributes["extensions"] == {"buildid": "_id", "buildname": "_name", "buildartifactid": "_artifact"}
    assert event.data == {"build": "_build"}

@pytest.mark.unit
def test_build_finished():
    event = Events().create_build_event(event_type.BuildFinishedEventV1, id="_id", name="_name", artifact="_artifact", data={"build": "_build"})
    assert event is not None
    assert event._attributes["type"] == event_type.BuildFinishedEventV1
    assert event._attributes["extensions"] == {"buildid": "_id", "buildname": "_name", "buildartifactid": "_artifact"}
    assert event.data == {"build": "_build"}
