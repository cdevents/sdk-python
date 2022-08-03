"""Constants Event types."""

# pylint: TODO: 

# Change Events
ChangeCreatedEventV1   :str = "cd.repository.change.created.v1"
ChangeUpdatedEventV1   :str = "cd.repository.change.updated.v1"
ChangeReviewedEventV1  :str = "cd.repository.change.reviewed.v1"
ChangeMergedEventV1    :str = "cd.repository.change.merged.v1"
ChangeAbandonedEventV1 :str = "cd.repository.change.abandoned.v1"

# PipelineRun events
PipelineRunStartedEventV1  :str = "cd.pipelinerun.started.v1"
PipelineRunFinishedEventV1 :str = "cd.pipelinerun.finished.v1"
PipelineRunQueuedEventV1   :str = "cd.pipelinerun.queued.v1"

# Repository events
RepositoryCreatedEventV1  :str = "cd.repository.created.v1"
RepositoryModifiedEventV1 :str = "cd.repository.modified.v1"
RepositoryDeletedEventV1  :str = "cd.repository.deleted.v1"

# Service Events
ServiceDeployedEventV1   :str = "cd.service.deployed.v1"
ServiceUpgradedEventV1   :str = "cd.service.upgraded.v1"
ServiceRolledbackEventV1 :str = "cd.service.rolledback.v1"
ServiceRemovedEventV1    :str = "cd.service.removed.v1"

# TaskRun events
TaskRunStartedEventV1  :str = "cd.taskrun.started.v1"
TaskRunFinishedEventV1 :str = "cd.taskrun.finished.v1"

# Test Events
TestCaseStartedEventV1  :str = "cd.test.case.started.v1"
TestCaseQueuedEventV1   :str = "cd.test.case.queued.v1"
TestCaseFinishedEventV1 :str = "cd.test.case.finished.v1"

TestSuiteStartedEventV1  :str = "cd.test.suite.started.v1"
TestSuiteQueuedEventV1   :str = "cd.test.suite.queued.v1"
TestSuiteFinishedEventV1 :str = "cd.test.suite.finished.v1"
