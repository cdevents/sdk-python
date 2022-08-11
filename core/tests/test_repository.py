import pytest

from cdevents.core.repository import RepositoryEvent, RepositoryType, RepositoryCreatedEvent, RepositoryModifiedEvent, RepositoryDeletedEvent

@pytest.mark.unit
def test_repository_created():
    repository_event = RepositoryEvent(repository_type=RepositoryType.RepositoryCreatedEventV1, id="_id", name="_name", url="_url", data={"key1": "value1"})
    assert repository_event is not None
    assert repository_event._attributes["type"] == RepositoryType.RepositoryCreatedEventV1.value
    assert repository_event._attributes["extensions"] == {"repositoryid": "_id", "repositoryname": "_name", "repositoryurl": "_url"}
    assert repository_event.data == {"key1": "value1"}

@pytest.mark.unit
def test_repository_type_created_v1():
    repository_event = RepositoryCreatedEvent(id="_id", name="_name", url="_url", data={"key1": "value1"})
    assert repository_event is not None
    assert repository_event._attributes["type"] == RepositoryType.RepositoryCreatedEventV1.value
    assert repository_event._attributes["extensions"] == {"repositoryid": "_id", "repositoryname": "_name", "repositoryurl": "_url"}
    assert repository_event.data == {"key1": "value1"}

@pytest.mark.unit
def test_repository_type_modified_v1():
    repository_event = RepositoryModifiedEvent(id="_id", name="_name", url="_url", data={"key1": "value1"})
    assert repository_event is not None
    assert repository_event._attributes["type"] == RepositoryType.RepositoryModifiedEventV1.value
    assert repository_event._attributes["extensions"] == {"repositoryid": "_id", "repositoryname": "_name", "repositoryurl": "_url"}
    assert repository_event.data == {"key1": "value1"}

@pytest.mark.unit
def test_repository_type_deleted_v1():
    repository_event = RepositoryDeletedEvent(id="_id", name="_name", url="_url", data={"key1": "value1"})
    assert repository_event is not None
    assert repository_event._attributes["type"] == RepositoryType.RepositoryDeletedEventV1.value
    assert repository_event._attributes["extensions"] == {"repositoryid": "_id", "repositoryname": "_name", "repositoryurl": "_url"}
    assert repository_event.data == {"key1": "value1"}

