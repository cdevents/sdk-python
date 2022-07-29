from cdevents.core import event_type
import pytest

from cdevents.core.events import Events

@pytest.mark.unit
def test_repository_branch_created():
    event = Events().create_branch_event(event_type.BranchCreatedEventV1, id="_id", name="_name", repoid="_repoid", data={"branch": "_branch"})
    assert event is not None
    assert event._attributes["type"] == event_type.BranchCreatedEventV1
    assert event._attributes["extensions"] == {"branchid": "_id", "branchname": "_name", "branchrepositoryid": "_repoid"}
    assert event.data == {"branch": "_branch"}

@pytest.mark.unit
def test_repository_branch_deleted():
    event = Events().create_branch_event(event_type.BranchDeletedEventV1, id="_id", name="_name", repoid="_repoid", data={"branch": "_branch"})
    assert event is not None
    assert event._attributes["type"] == event_type.BranchDeletedEventV1
    assert event._attributes["extensions"] == {"branchid": "_id", "branchname": "_name", "branchrepositoryid": "_repoid"}
    assert event.data == {"branch": "_branch"}
