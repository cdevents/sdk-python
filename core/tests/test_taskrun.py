import pytest

from cdevents.core.taskrun import TaskRun, TaskRunType

@pytest.mark.unit
def test_taskrun_started():
    taskrun_event = TaskRun(taskrun_type=TaskRunType.TaskRunStartedEventV1, id="_id", name="_name", pipelineid="_pipelineid", data={"key1": "value1"})
    assert taskrun_event is not None
    assert taskrun_event._attributes["type"] == TaskRunType.TaskRunStartedEventV1.value
    assert taskrun_event._attributes["extensions"] == {"taskrunid": "_id", "taskrunname": "_name", "taskrunpipelineid": "_pipelineid"}
    assert taskrun_event.data == {"key1": "value1"}


@pytest.mark.unit
def test_taskrun_finished():
    taskrun_event = TaskRun(taskrun_type=TaskRunType.TaskRunFinishedEventV1, id="_id", name="_name", pipelineid="_pipelineid", data={"key1": "value1"})
    assert taskrun_event is not None
    assert taskrun_event._attributes["type"] == TaskRunType.TaskRunFinishedEventV1.value
    assert taskrun_event._attributes["extensions"] == {"taskrunid": "_id", "taskrunname": "_name", "taskrunpipelineid": "_pipelineid"}
    assert taskrun_event.data == {"key1": "value1"}
