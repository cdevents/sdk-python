from cdevents.core import event_type
import pytest

from cdevents.core.events import Events

@pytest.mark.unit
def test_repository_created():
    event = Events().create_repository_event(event_type.RepositoryCreatedEventV1, id="_id", name="_name", url="_url", data={"repository": "_repository"})
    assert event is not None
    assert event._attributes["type"] == event_type.RepositoryCreatedEventV1
    assert event._attributes["extensions"] ==  {"repositoryid": "_id", "repositoryname": "_name", "repositoryurl": "_url"}
    assert event.data == {"repository": "_repository"}

@pytest.mark.unit
def test_repository_modified():
    event = Events().create_repository_event(event_type.RepositoryModifiedEventV1, id="_id", name="_name", url="_url", data={"repository": "_repository"})
    assert event is not None
    assert event._attributes["type"] == event_type.RepositoryModifiedEventV1
    assert event._attributes["extensions"] ==  {"repositoryid": "_id", "repositoryname": "_name", "repositoryurl": "_url"}
    assert event.data == {"repository": "_repository"}

@pytest.mark.unit
def test_repository_deleted():
    event = Events().create_repository_event(event_type.RepositoryDeletedEventV1, id="_id", name="_name", url="_url", data={"repository": "_repository"})
    assert event is not None
    assert event._attributes["type"] == event_type.RepositoryDeletedEventV1
    assert event._attributes["extensions"] ==  {"repositoryid": "_id", "repositoryname": "_name", "repositoryurl": "_url"}
    assert event.data == {"repository": "_repository"}
