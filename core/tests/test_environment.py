import pytest

from cdevents.core.env import Env, EnvType

@pytest.mark.unit
def test_environment_created():
    env = Env(env_type=EnvType.EnvironmentCreatedEventV1, id="_id", name="_name", repo="_repo")
    env_event = env.create_event(data={"key1": "value1"})
    assert env_event is not None
    assert env_event._attributes["type"] == EnvType.EnvironmentCreatedEventV1.value
    assert env_event._attributes["extensions"] == {"envId": "_id", "envname": "_name", "envrepourl": "_repo"}
    assert env_event.data == {"key1": "value1"}


@pytest.mark.unit
def test_environment_modified():
    env = Env(env_type=EnvType.EnvironmentModifiedEventV1, id="_id", name="_name", repo="_repo")
    env_event = env.create_event(data={"key1": "value1"})
    assert env_event is not None
    assert env_event._attributes["type"] == EnvType.EnvironmentModifiedEventV1.value
    assert env_event._attributes["extensions"] == {"envId": "_id", "envname": "_name", "envrepourl": "_repo"}
    assert env_event.data == {"key1": "value1"}

@pytest.mark.unit
def test_environment_deleted():
    env = Env(env_type=EnvType.EnvironmentDeletedEventV1, id="_id", name="_name", repo="_repo")
    env_event = env.create_event(data={"key1": "value1"})
    assert env_event is not None
    assert env_event._attributes["type"] == EnvType.EnvironmentDeletedEventV1.value
    assert env_event._attributes["extensions"] == {"envId": "_id", "envname": "_name", "envrepourl": "_repo"}
    assert env_event.data == {"key1": "value1"}