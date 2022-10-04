import pytest
from cdevents.core.event_type import EventType
from cdevents.core.repository import (
    RepositoryCreatedEvent,
    RepositoryDeletedEvent,
    RepositoryEvent,
    RepositoryModifiedEvent,
)


@pytest.mark.unit
def test_repository_created():
    repository_event = RepositoryEvent(
        repository_type=EventType.RepositoryCreatedEventV1,
        id="_id",
        name="_name",
        url="_url",
        data={"key1": "value1"},
    )
    assert repository_event is not None
    assert repository_event._attributes["type"] == EventType.RepositoryCreatedEventV1.value
    assert repository_event._attributes["extensions"] == {
        "repositoryid": "_id",
        "repositoryname": "_name",
        "repositoryurl": "_url",
    }
    assert repository_event.data == {"key1": "value1"}


@pytest.mark.unit
def test_repository_type_created_v1():
    repository_event = RepositoryCreatedEvent(
        id="_id", name="_name", url="_url", data={"key1": "value1"}
    )
    assert repository_event is not None
    assert repository_event._attributes["type"] == EventType.RepositoryCreatedEventV1.value
    assert repository_event._attributes["extensions"] == {
        "repositoryid": "_id",
        "repositoryname": "_name",
        "repositoryurl": "_url",
    }
    assert repository_event.data == {"key1": "value1"}


@pytest.mark.unit
def test_repository_type_modified_v1():
    repository_event = RepositoryModifiedEvent(
        id="_id", name="_name", url="_url", data={"key1": "value1"}
    )
    assert repository_event is not None
    assert repository_event._attributes["type"] == EventType.RepositoryModifiedEventV1.value
    assert repository_event._attributes["extensions"] == {
        "repositoryid": "_id",
        "repositoryname": "_name",
        "repositoryurl": "_url",
    }
    assert repository_event.data == {"key1": "value1"}


@pytest.mark.unit
def test_repository_type_deleted_v1():
    repository_event = RepositoryDeletedEvent(
        id="_id", name="_name", url="_url", data={"key1": "value1"}
    )
    assert repository_event is not None
    assert repository_event._attributes["type"] == EventType.RepositoryDeletedEventV1.value
    assert repository_event._attributes["extensions"] == {
        "repositoryid": "_id",
        "repositoryname": "_name",
        "repositoryurl": "_url",
    }
    assert repository_event.data == {"key1": "value1"}
