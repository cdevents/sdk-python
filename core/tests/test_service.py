from cdevents.core import event_type
import pytest

from cdevents.core.events import Events

@pytest.mark.unit
def test_service_deployed():
    event = Events().create_service_event(event_type.ServiceDeployedEventV1, envid="_envid", name="_name", version="_version", data={"service": "_service"})
    assert event is not None
    assert event._attributes["type"] == event_type.ServiceDeployedEventV1
    assert event._attributes["extensions"] == {"serviceenvid": "_envid", "servicename": "_name", "serviceversion": "_version"}
    assert event.data == {"service": "_service"}


@pytest.mark.unit
def test_service_upgraded():
    event = Events().create_service_event(event_type.ServiceUpgradedEventV1, envid="_envid", name="_name", version="_version", data={"service": "_service"})
    assert event is not None
    assert event._attributes["type"] == event_type.ServiceUpgradedEventV1
    assert event._attributes["extensions"] == {"serviceenvid": "_envid", "servicename": "_name", "serviceversion": "_version"}
    assert event.data == {"service": "_service"}


@pytest.mark.unit
def test_service_rolledback():
    event = Events().create_service_event(event_type.ServiceRolledbackEventV1, envid="_envid", name="_name", version="_version", data={"service": "_service"})
    assert event is not None
    assert event._attributes["type"] == event_type.ServiceRolledbackEventV1
    assert event._attributes["extensions"] == {"serviceenvid": "_envid", "servicename": "_name", "serviceversion": "_version"}
    assert event.data == {"service": "_service"}


@pytest.mark.unit
def test_service_removed():
    event = Events().create_service_event(event_type.ServiceRemovedEventV1, envid="_envid", name="_name", version="_version", data={"service": "_service"})
    assert event is not None
    assert event._attributes["type"] == event_type.ServiceRemovedEventV1
    assert event._attributes["extensions"] == {"serviceenvid": "_envid", "servicename": "_name", "serviceversion": "_version"}
    assert event.data == {"service": "_service"}

