import pytest

from cdevents.core.branch import BranchEvent, BranchType, BranchCreatedEvent, BranchDeletedEvent

@pytest.mark.unit
def test_branch_created():
    branch_event = BranchEvent(branch_type=BranchType.BranchCreatedEventV1, id="_id", name="_name", repoid="_repoid", data={"key1": "value1"})
    assert branch_event is not None
    assert branch_event._attributes["type"] == BranchType.BranchCreatedEventV1.value
    assert branch_event._attributes["extensions"] == {"branchid": "_id", "branchname": "_name", "branchrepositoryid": "_repoid"}
    assert branch_event.data == {"key1": "value1"}

@pytest.mark.unit
def test_branch_type_created_v1():
    branch_event = BranchCreatedEvent(id="_id", name="_name", repoid="_repoid", data={"key1": "value1"})
    assert branch_event is not None
    assert branch_event._attributes["type"] == BranchType.BranchCreatedEventV1.value
    assert branch_event._attributes["extensions"] == {"branchid": "_id", "branchname": "_name", "branchrepositoryid": "_repoid"}
    assert branch_event.data == {"key1": "value1"}

@pytest.mark.unit
def test_branch_type_deleted_v1():
    branch_event = BranchDeletedEvent(id="_id", name="_name", repoid="_repoid", data={"key1": "value1"})
    assert branch_event is not None
    assert branch_event._attributes["type"] == BranchType.BranchDeletedEventV1.value
    assert branch_event._attributes["extensions"] == {"branchid": "_id", "branchname": "_name", "branchrepositoryid": "_repoid"}
    assert branch_event.data == {"key1": "value1"}