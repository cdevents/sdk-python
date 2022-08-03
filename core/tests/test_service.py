from cdevents.core import event_type
import pytest

from cdevents.core.service import Service, ServiceType

@pytest.mark.unit
def test_service_deployed():
    service = Service(service_type=ServiceType.ServiceDeployedEventV1, envid="_envid", name="_name", version="_version")
    service_event = service.create_event(data={"key1": "value1"})
    assert service_event is not None
    assert service_event._attributes["type"] == ServiceType.ServiceDeployedEventV1.value
    assert service_event._attributes["extensions"] == {"serviceenvid": "_envid", "servicename": "_name", "serviceversion": "_version"}
    assert service_event.data == {"key1": "value1"}


@pytest.mark.unit
def test_service_upgraded():
    service = Service(service_type=ServiceType.ServiceUpgradedEventV1, envid="_envid", name="_name", version="_version")
    service_event = service.create_event(data={"key1": "value1"})
    assert service_event is not None
    assert service_event._attributes["type"] == ServiceType.ServiceUpgradedEventV1.value
    assert service_event._attributes["extensions"] == {"serviceenvid": "_envid", "servicename": "_name", "serviceversion": "_version"}
    assert service_event.data == {"key1": "value1"}


@pytest.mark.unit
def test_service_rolledback():
    service = Service(service_type=ServiceType.ServiceRolledbackEventV1, envid="_envid", name="_name", version="_version")
    service_event = service.create_event(data={"key1": "value1"})
    assert service_event is not None
    assert service_event._attributes["type"] == ServiceType.ServiceRolledbackEventV1.value
    assert service_event._attributes["extensions"] == {"serviceenvid": "_envid", "servicename": "_name", "serviceversion": "_version"}
    assert service_event.data == {"key1": "value1"}


@pytest.mark.unit
def test_service_removed():
    service = Service(service_type=ServiceType.ServiceRemovedEventV1, envid="_envid", name="_name", version="_version")
    service_event = service.create_event(data={"key1": "value1"})
    assert service_event is not None
    assert service_event._attributes["type"] == ServiceType.ServiceRemovedEventV1.value
    assert service_event._attributes["extensions"] == {"serviceenvid": "_envid", "servicename": "_name", "serviceversion": "_version"}
    assert service_event.data == {"key1": "value1"}

