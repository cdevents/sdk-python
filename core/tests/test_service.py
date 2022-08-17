import pytest

from cdevents.core.service import ServiceEvent, ServiceDeployedEvent, ServiceUpgradedEvent, ServiceRolledbackEvent, ServiceRemovedEvent
from cdevents.core.event_type import EventType

@pytest.mark.unit
def test_service_created():
    service_event = ServiceEvent(service_type=EventType.ServiceDeployedEventV1, envid="_envid", name="_name", version="_version", data={"key1": "value1"})
    assert service_event is not None
    assert service_event._attributes["type"] == EventType.ServiceDeployedEventV1.value
    assert service_event._attributes["extensions"] == {"serviceenvid": "_envid", "servicename": "_name", "serviceversion": "_version"}
    assert service_event.data == {"key1": "value1"}


@pytest.mark.unit
def test_service_type_deployed_v1():
    service_event = ServiceDeployedEvent(envid="_envid", name="_name", version="_version", data={"key1": "value1"})
    assert service_event is not None
    assert service_event._attributes["type"] == EventType.ServiceDeployedEventV1.value
    assert service_event._attributes["extensions"] == {"serviceenvid": "_envid", "servicename": "_name", "serviceversion": "_version"}
    assert service_event.data == {"key1": "value1"}


@pytest.mark.unit
def test_service_type_upgraded_v1():
    service_event = ServiceUpgradedEvent(envid="_envid", name="_name", version="_version", data={"key1": "value1"})
    assert service_event is not None
    assert service_event._attributes["type"] == EventType.ServiceUpgradedEventV1.value
    assert service_event._attributes["extensions"] == {"serviceenvid": "_envid", "servicename": "_name", "serviceversion": "_version"}
    assert service_event.data == {"key1": "value1"}


@pytest.mark.unit
def test_service_type_rolledback_v1():
    service_event = ServiceRolledbackEvent(envid="_envid", name="_name", version="_version", data={"key1": "value1"})
    assert service_event is not None
    assert service_event._attributes["type"] == EventType.ServiceRolledbackEventV1.value
    assert service_event._attributes["extensions"] == {"serviceenvid": "_envid", "servicename": "_name", "serviceversion": "_version"}
    assert service_event.data == {"key1": "value1"}


@pytest.mark.unit
def test_service_type_removed_v1():
    service_event = ServiceRemovedEvent(envid="_envid", name="_name", version="_version", data={"key1": "value1"})
    assert service_event is not None
    assert service_event._attributes["type"] == EventType.ServiceRemovedEventV1.value
    assert service_event._attributes["extensions"] == {"serviceenvid": "_envid", "servicename": "_name", "serviceversion": "_version"}
    assert service_event.data == {"key1": "value1"}

