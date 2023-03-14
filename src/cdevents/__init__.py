#  Copyright 2022 The CDEvents Authors
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
#  SPDX-License-Identifier: Apache-2.0
"""Python SDK to emit CDEvents.

Example usage:
```py

```
"""

from cdevents._cloudevents import to_cloudevent
from cdevents.artifact import (
    ArtifactPackagedEvent,
    ArtifactPublishedEvent,
    new_artifact_packaged_event,
    new_artifact_published_event,
)
from cdevents.branch import (
    BranchCreatedEvent,
    BranchDeletedEvent,
    new_branch_created_event,
    new_branch_deleted_event,
)
from cdevents.build import (
    BuildFinishedEvent,
    BuildQueuedEvent,
    BuildStartedEvent,
    new_build_finished_event,
    new_build_queued_event,
    new_build_started_event,
)
from cdevents.change import (
    ChangeAbandonedEvent,
    ChangeCreatedEvent,
    ChangeMergedEvent,
    ChangeReviewedEvent,
    ChangeUpdatedEvent,
    new_change_abandoned_event,
    new_change_created_event,
    new_change_merged_event,
    new_change_reviewed_event,
    new_change_updated_event,
)
from cdevents.environment import (
    EnvironmentCreatedEvent,
    EnvironmentDeletedEvent,
    EnvironmentModifiedEvent,
    new_environment_created_event,
    new_environment_deleted_event,
    new_environment_modified_event,
)
from cdevents.pipeline_run import (
    PipelineRunFinishedEvent,
    PipelineRunQueuedEvent,
    PipelineRunStartedEvent,
    new_pipelinerun_finished_event,
    new_pipelinerun_queued_event,
    new_pipelinerun_started_event,
)
from cdevents.repository import (
    RepositoryCreatedEvent,
    RepositoryDeletedEvent,
    RepositoryModifiedEvent,
    new_repository_created_event,
    new_repository_deleted_event,
    new_repository_modified_event,
)
from cdevents.service import (
    ServiceDeployedEvent,
    ServicePublishedEvent,
    ServiceRemovedEvent,
    ServiceRolledbackEvent,
    ServiceUpgradedEvent,
    new_service_deployed_event,
    new_service_published_event,
    new_service_removed_event,
    new_service_rolledback_event,
    new_service_upgraded_event,
)
from cdevents.task_run import (
    TaskRunFinishedEvent,
    TaskRunStartedEvent,
    new_taskrun_finished_event,
    new_taskrun_started_event,
)
from cdevents.test_case import (
    TestCaseFinishedEvent,
    TestCaseQueuedEvent,
    TestCaseStartedEvent,
    new_testcase_finished_event,
    new_testcase_queued_event,
    new_testcase_started_event,
)
from cdevents.test_suite import (
    TestSuiteFinishedEvent,
    TestSuiteStartedEvent,
    new_testsuite_finished_event,
    new_testsuite_started_event,
)

__version__ = "0.0.1"
