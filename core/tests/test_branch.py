import pytest

from cdevents.core.branch import Branch, BranchType

@pytest.mark.unit
def test_repository_branch_created():
    branch = Branch(branch_type=BranchType.BranchCreatedEventV1, id="_id", name="_name", repoid="_repoid")
    branch_event = branch.create_event(data={"key1": "value1"})
    assert branch_event is not None
    assert branch_event._attributes["type"] == "cd.repository.branch.created.v1"
    assert branch_event._attributes["extensions"] == {"branchid": "_id", "branchname": "_name", "branchrepositoryid": "_repoid"}
    assert branch_event.data == {"key1": "value1"}

@pytest.mark.unit
def test_repository_branch_deleted():
    branch = Branch(branch_type=BranchType.BranchDeletedEventV1, id="_id", name="_name", repoid="_repoid")
    branch_event = branch.create_event(data={"key1": "value1"})
    assert branch_event is not None
    assert branch_event._attributes["type"] == "cd.repository.branch.deleted.v1"
    assert branch_event._attributes["extensions"] == {"branchid": "_id", "branchname": "_name", "branchrepositoryid": "_repoid"}
    assert branch_event.data == {"key1": "value1"}