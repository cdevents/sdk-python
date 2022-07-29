from cdevents.core import event_type
import pytest

from cdevents.core.events import Events

@pytest.mark.unit
def test_environment_created():
    event = Events().create_environment_event(event_type.EnvironmentCreatedEventV1, id="_id", name="_name", repo="_repo", data={"environment": "_environment"})
    assert event is not None
    assert event._attributes["type"] == event_type.EnvironmentCreatedEventV1
    assert event._attributes["extensions"] == {"envId": "_id", "envname": "_name", "envrepourl": "_repo"}
    assert event.data == {"environment": "_environment"} 

@pytest.mark.unit
def test_environment_modified():
    event = Events().create_environment_event(event_type.EnvironmentModifiedEventV1, id="_id", name="_name", repo="_repo", data={"environment": "_environment"})
    assert event is not None
    assert event._attributes["type"] == event_type.EnvironmentModifiedEventV1
    assert event._attributes["extensions"] == {"envId": "_id", "envname": "_name", "envrepourl": "_repo"}
    assert event.data == {"environment": "_environment"} 

@pytest.mark.unit
def test_environment_deleted():
    event = Events().create_environment_event(event_type.EnvironmentDeletedEventV1, id="_id", name="_name", repo="_repo", data={"environment": "_environment"})
    assert event is not None
    assert event._attributes["type"] == event_type.EnvironmentDeletedEventV1
    assert event._attributes["extensions"] == {"envId": "_id", "envname": "_name", "envrepourl": "_repo"}
    assert event.data == {"environment": "_environment"} 
