import pytest

from cdevents.core.events import Events

@pytest.mark.unit
def test_create_event():
    event = Events(event_type="event_type", extensions={"test": "test"}, data={"key1": "value1"})
    assert event is not None
    assert event._attributes["type"] == "event_type"
    assert event._attributes["extensions"] == {"test": "test"}
    assert event.data == {"key1": "value1"}
