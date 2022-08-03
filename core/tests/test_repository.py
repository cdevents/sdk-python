from cdevents.core import event_type
import pytest

from cdevents.core.repository import Repository, RepositoryType

@pytest.mark.unit
def test_repository_created():
    repository = Repository(repository_type=RepositoryType.RepositoryCreatedEventV1, id="_id", name="_name", url="_url")
    repository_event = repository.create_event(data={"key1": "value1"})
    assert repository_event is not None
    assert repository_event._attributes["type"] == RepositoryType.RepositoryCreatedEventV1.value
    assert repository_event._attributes["extensions"] == {"repositoryid": "_id", "repositoryname": "_name", "repositoryurl": "_url"}
    assert repository_event.data == {"key1": "value1"}


@pytest.mark.unit
def test_repository_modified():
    repository = Repository(repository_type=RepositoryType.RepositoryModifiedEventV1, id="_id", name="_name", url="_url")
    repository_event = repository.create_event(data={"key1": "value1"})
    assert repository_event is not None
    assert repository_event._attributes["type"] == RepositoryType.RepositoryModifiedEventV1.value
    assert repository_event._attributes["extensions"] == {"repositoryid": "_id", "repositoryname": "_name", "repositoryurl": "_url"}
    assert repository_event.data == {"key1": "value1"}


@pytest.mark.unit
def test_repository_deleted():
    repository = Repository(repository_type=RepositoryType.RepositoryDeletedEventV1, id="_id", name="_name", url="_url")
    repository_event = repository.create_event(data={"key1": "value1"})
    assert repository_event is not None
    assert repository_event._attributes["type"] == RepositoryType.RepositoryDeletedEventV1.value
    assert repository_event._attributes["extensions"] == {"repositoryid": "_id", "repositoryname": "_name", "repositoryurl": "_url"}
    assert repository_event.data == {"key1": "value1"}

