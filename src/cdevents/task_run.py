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
"""Events under dev.cdevents.taskrun."""
from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Union
import datetime

from cdevents.cdevent import SPEC_VERSION, CDEvent
from cdevents.context import Context
from cdevents.pipeline_run import PipelineRunSubject
from cdevents.subject import Subject
from pydanticEvent import parsedEvent


@dataclass
class TaskRunSubjectContent:
    """Content for task run subjects."""

    task_name: str
    """The name of the task."""

    pipeline_run: Dict[str, str]
    """Information about the pipeline that runs this task."""

    url: str
    """URL to the task run."""


@dataclass
class TaskRunSubject(Subject):
    """Subject for taskrun-related events."""

    content: TaskRunSubjectContent
    """Content for change subjects."""

    type: str = field(default="taskRun", init=False)


@dataclass
class TaskRunFinishedSubjectContent(TaskRunSubjectContent):
    """Subject for artifact-related messages."""

    outcome: str
    """Outcome of task run run.

    One of 'success', 'error' and 'failure'.
    """

    errors: str
    """In case of error or failed task run, provides details about the failure."""


@dataclass
class TaskRunFinishedSubject(TaskRunSubject):
    """Subject for taskrun-related events."""

    content: TaskRunFinishedSubjectContent
    """Content for change subjects."""


# region TaskRunStartedEvent


@dataclass
class TaskRunStartedEvent(CDEvent):
    """Task run started event."""

    CDEVENT_TYPE = "dev.cdevents.taskrun.started." + SPEC_VERSION

    subject: TaskRunSubject
    """TaskRun subject."""


def new_taskrun_started_event(
    context_id: str,
    context_source: str,
    context_timestamp: datetime,
    subject_id: str,
    subject_source: str,
    task_name: str,
    pipeline_run: Dict[str, str],
    url: str,
    custom_data: Union[str, Dict, None],
    custom_data_content_type: str,
) -> TaskRunStartedEvent:
    input_data = parsedEvent(context_id = context_id, context_source = context_source, context_timestamp = context_timestamp, subject_id = subject_id, subject_source = subject_source,
    task_name = task_name, pipeline_run = pipeline_run, url = url, custom_data = custom_data, custom_data_content_type = custom_data_content_type)
    """Creates a new taskrun started CDEvent."""
    context = Context(
        type=TaskRunStartedEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=input_data.context_id,
        source=input_data.context_source,
        timestamp=input_data.context_timestamp,
    )

    content = TaskRunSubjectContent(task_name=input_data.task_name, pipeline_run=input_data.pipeline_run, url=input_data.url)

    subject = TaskRunSubject(id=input_data.subject_id, source=input_data.subject_source, content=content)

    event = TaskRunStartedEvent(
        context=context,
        subject=subject,
        custom_data=input_data.custom_data,
        custom_data_content_type=input_data.custom_data_content_type,
    )

    return event

# endregion TaskRunStartedEvent

# region TaskRunFinishedEvent


@dataclass
class TaskRunFinishedEvent(CDEvent):
    """Task run finished event."""

    CDEVENT_TYPE = "dev.cdevents.taskrun.finished." + SPEC_VERSION

    subject: TaskRunFinishedSubject
    """TaskRun subject."""


def new_taskrun_finished_event(
    context_id: str,
    context_source: str,
    context_timestamp: datetime,
    subject_id: str,
    subject_source: str,
    task_name: str,
    pipeline_run: Dict[str, str],
    url: str,
    outcome: str,
    errors: str,
    custom_data: Union[str, Dict, None],
    custom_data_content_type: str,
) -> TaskRunFinishedEvent:
    input_data = parsedEvent(context_id = context_id, context_source = context_source, context_timestamp = context_timestamp, subject_id = subject_id, subject_source = subject_source,
    task_name = task_name,errors = errors, outcome = outcome, pipeline_run = pipeline_run, url = url, custom_data = custom_data, custom_data_content_type = custom_data_content_type)
    """Creates a new taskrun finished CDEvent."""
    context = Context(
        type=TaskRunFinishedEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=input_data.context_id,
        source=input_data.context_source,
        timestamp=input_data.context_timestamp,
    )

    content = TaskRunFinishedSubjectContent(
        task_name=input_data.task_name, pipeline_run=input_data.pipeline_run, url=input_data.url, outcome=input_data.outcome, errors=input_data.errors
    )

    subject = TaskRunFinishedSubject(id=input_data.subject_id, source=input_data.subject_source, content=content)

    event = TaskRunFinishedEvent(
        context=context,
        subject=subject,
        custom_data=input_data.custom_data,
        custom_data_content_type=input_data.custom_data_content_type,
    )

    return event


# endregion TaskRunFinishedEvent