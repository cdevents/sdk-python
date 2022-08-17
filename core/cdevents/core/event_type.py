"""Constants Event types."""

from enum import Enum

# pylint: TODO: 

# # Change Events
# ChangeCreatedEventV1   :str = "cd.repository.change.created.v1"
# ChangeUpdatedEventV1   :str = "cd.repository.change.updated.v1"
# ChangeReviewedEventV1  :str = "cd.repository.change.reviewed.v1"
# ChangeMergedEventV1    :str = "cd.repository.change.merged.v1"
# ChangeAbandonedEventV1 :str = "cd.repository.change.abandoned.v1"

# # TestCase Events
# TestCaseStartedEventV1  :str = "cd.test.case.started.v1"
# TestCaseQueuedEventV1   :str = "cd.test.case.queued.v1"
# TestCaseFinishedEventV1 :str = "cd.test.case.finished.v1"

# # TestSuite Events
# TestSuiteStartedEventV1  :str = "cd.test.suite.started.v1"
# TestSuiteQueuedEventV1   :str = "cd.test.suite.queued.v1"
# TestSuiteFinishedEventV1 :str = "cd.test.suite.finished.v1"

class EventType(Enum):
    """Constants Event types."""

    # Artifact Events
    ArtifactPackagedEventV1: str = "cd.artifact.packaged.v1"
    ArtifactPublishedEventV1: str = "cd.artifact.published.v1"

    # Branch Events
    BranchCreatedEventV1: str = "cd.repository.branch.created.v1"
    BranchDeletedEventV1: str = "cd.repository.branch.deleted.v1"

    # Build Events
    BuildStartedEventV1  :str = "cd.build.started.v1"
    BuildQueuedEventV1   :str = "cd.build.queued.v1"
    BuildFinishedEventV1 :str = "cd.build.finished.v1"

    # Environment Events
    EnvironmentCreatedEventV1  :str = "cd.environment.created.v1"
    EnvironmentModifiedEventV1 :str = "cd.environment.modified.v1"
    EnvironmentDeletedEventV1  :str = "cd.environment.deleted.v1"

    # PipelineRun Events
    PipelineRunStartedEventV1  :str = "cd.pipelinerun.started.v1"
    PipelineRunFinishedEventV1 :str = "cd.pipelinerun.finished.v1"
    PipelineRunQueuedEventV1   :str = "cd.pipelinerun.queued.v1"

    # Repository Events
    RepositoryCreatedEventV1  :str = "cd.repository.created.v1"
    RepositoryModifiedEventV1 :str = "cd.repository.modified.v1"
    RepositoryDeletedEventV1  :str = "cd.repository.deleted.v1"

    # Service Events
    ServiceDeployedEventV1   :str = "cd.service.deployed.v1"
    ServiceUpgradedEventV1   :str = "cd.service.upgraded.v1"
    ServiceRolledbackEventV1 :str = "cd.service.rolledback.v1"
    ServiceRemovedEventV1    :str = "cd.service.removed.v1"

    # TaskRun Events
    TaskRunStartedEventV1  :str = "cd.taskrun.started.v1"
    TaskRunFinishedEventV1 :str = "cd.taskrun.finished.v1"
