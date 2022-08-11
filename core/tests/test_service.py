import pytest

from cdevents.core.service import ServiceEvent, ServiceType, ServiceDeployedEvent, ServiceUpgradedEvent, ServiceRolledbackEvent, ServiceRemovedEvent

@pytest.mark.unit
def test_service_created():
    service_event = ServiceEvent(service_type=ServiceType.ServiceDeployedEventV1, envid="_envid", name="_name", version="_version", data={"key1": "value1"})
    assert service_event is not None
    assert service_event._attributes["type"] == ServiceType.ServiceDeployedEventV1.value
    assert service_event._attributes["extensions"] == {"serviceenvid": "_envid", "servicename": "_name", "serviceversion": "_version"}
    assert service_event.data == {"key1": "value1"}


@pytest.mark.unit
def test_service_type_deployed_v1():
    service_event = ServiceDeployedEvent(envid="_envid", name="_name", version="_version", data={"key1": "value1"})
    assert service_event is not None
    assert service_event._attributes["type"] == ServiceType.ServiceDeployedEventV1.value
    assert service_event._attributes["extensions"] == {"serviceenvid": "_envid", "servicename": "_name", "serviceversion": "_version"}
    assert service_event.data == {"key1": "value1"}


@pytest.mark.unit
def test_service_type_upgraded_v1():
    service_event = ServiceUpgradedEvent(envid="_envid", name="_name", version="_version", data={"key1": "value1"})
    assert service_event is not None
    assert service_event._attributes["type"] == ServiceType.ServiceUpgradedEventV1.value
    assert service_event._attributes["extensions"] == {"serviceenvid": "_envid", "servicename": "_name", "serviceversion": "_version"}
    assert service_event.data == {"key1": "value1"}


@pytest.mark.unit
def test_service_type_rolledback_v1():
    service_event = ServiceRolledbackEvent(envid="_envid", name="_name", version="_version", data={"key1": "value1"})
    assert service_event is not None
    assert service_event._attributes["type"] == ServiceType.ServiceRolledbackEventV1.value
    assert service_event._attributes["extensions"] == {"serviceenvid": "_envid", "servicename": "_name", "serviceversion": "_version"}
    assert service_event.data == {"key1": "value1"}


@pytest.mark.unit
def test_service_type_removed_v1():
    service_event = ServiceRemovedEvent(envid="_envid", name="_name", version="_version", data={"key1": "value1"})
    assert service_event is not None
    assert service_event._attributes["type"] == ServiceType.ServiceRemovedEventV1.value
    assert service_event._attributes["extensions"] == {"serviceenvid": "_envid", "servicename": "_name", "serviceversion": "_version"}
    assert service_event.data == {"key1": "value1"}

