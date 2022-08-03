import pytest

from cdevents.core.artifact import Artifact, ArtifactType

@pytest.mark.unit
def test_artifact_packaged_v1():
    artifact = Artifact(artifact_type=ArtifactType.ArtifactPackagedEventV1, id="_id", name="_name", version="_version")
    artifact_event = artifact.create_event(data={"key1": "value1"})
    assert artifact_event is not None
    assert artifact_event._attributes["type"] == ArtifactType.ArtifactPackagedEventV1.value
    assert artifact_event._attributes["extensions"] == {"artifactid": "_id", "artifactname": "_name", "artifactversion": "_version"}
    assert artifact_event.data == {"key1": "value1"}

@pytest.mark.unit
def test_artifact_published_v1():
    artifact = Artifact(artifact_type=ArtifactType.ArtifactPublishedEventV1, id="_id", name="_name", version="_version")
    artifact_event = artifact.create_event(data={"key1": "value1"})
    assert artifact_event is not None
    assert artifact_event._attributes["type"] ==ArtifactType.ArtifactPublishedEventV1.value
    assert artifact_event._attributes["extensions"] == {"artifactid": "_id", "artifactname": "_name", "artifactversion": "_version"}
    assert artifact_event.data == {"key1": "value1"}

