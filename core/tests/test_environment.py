import pytest

from cdevents.core.env import EnvEvent, EnvType, EnvEventCreatedEvent, EnvEventModifiedEvent, EnvEventDeletedEvent

@pytest.mark.unit
def test_environment_created():
    env_event = EnvEvent(env_type=EnvType.EnvironmentCreatedEventV1, id="_id", name="_name", repo="_repo", data={"key1": "value1"})
    assert env_event is not None
    assert env_event._attributes["type"] == EnvType.EnvironmentCreatedEventV1.value
    assert env_event._attributes["extensions"] == {"envId": "_id", "envname": "_name", "envrepourl": "_repo"}
    assert env_event.data == {"key1": "value1"}


@pytest.mark.unit
def test_environment_type_created_v1():
    env_event = EnvEventCreatedEvent(id="_id", name="_name", repo="_repo", data={"key1": "value1"})
    assert env_event is not None
    assert env_event._attributes["type"] == EnvType.EnvironmentCreatedEventV1.value
    assert env_event._attributes["extensions"] == {"envId": "_id", "envname": "_name", "envrepourl": "_repo"}
    assert env_event.data == {"key1": "value1"}


@pytest.mark.unit
def test_environment_type_modified_v1():
    env_event = EnvEventModifiedEvent(id="_id", name="_name", repo="_repo", data={"key1": "value1"})
    assert env_event is not None
    assert env_event._attributes["type"] == EnvType.EnvironmentModifiedEventV1.value
    assert env_event._attributes["extensions"] == {"envId": "_id", "envname": "_name", "envrepourl": "_repo"}
    assert env_event.data == {"key1": "value1"}

@pytest.mark.unit
def test_environment_type_deleted_v1():
    env_event = EnvEventDeletedEvent(id="_id", name="_name", repo="_repo", data={"key1": "value1"})
    assert env_event is not None
    assert env_event._attributes["type"] == EnvType.EnvironmentDeletedEventV1.value
    assert env_event._attributes["extensions"] == {"envId": "_id", "envname": "_name", "envrepourl": "_repo"}
    assert env_event.data == {"key1": "value1"}