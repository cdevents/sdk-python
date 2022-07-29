from cdevents.core import event_type
import pytest

from cdevents.core.events import Events

@pytest.mark.unit
def test_artifact_packaged_v1():
    event = Events().create_artifact_event(event_type.ArtifactPackagedEventV1, id="_id", name="_name", version="_version", data={"artifact": "_artifact"})
    assert event is not None
    assert event._attributes["type"] == event_type.ArtifactPackagedEventV1
    assert event._attributes["extensions"] == {"artifactid": "_id", "artifactname": "_name", "artifactversion": "_version"}
    assert event.data == {"artifact": "_artifact"}

@pytest.mark.unit
def test_artifact_published_v1():
    event = Events().create_artifact_event(event_type.ArtifactPublishedEventV1, id="_id", name="_name", version="_version", data={"artifact": "_artifact"})
    assert event is not None
    assert event._attributes["type"] == event_type.ArtifactPublishedEventV1
    assert event._attributes["extensions"] == {"artifactid": "_id", "artifactname": "_name", "artifactversion": "_version"}
    assert event.data == {"artifact": "_artifact"}
