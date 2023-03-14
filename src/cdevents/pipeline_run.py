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
"""Events under dev.cdevents.pipelinerun."""
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Union

from cdevents.cdevent import SPEC_VERSION, CDEvent
from cdevents.context import Context
from cdevents.subject import Subject


@dataclass
class PipelineRunSubject(Subject):
    """Subject for pipelinerun-related events."""

    pipeline_name: str
    """The name of the pipeline."""

    url: str
    """URL to the pipeline run."""


@dataclass
class PipelineRunFinishedSubject(PipelineRunSubject):
    """Subject for artifact-related messages."""

    outcome: str
    """Outcome of pipeline run.

    One of 'success', 'error' and 'failure'.
    """

    errors: str
    """In case of error or failed pipeline, provides details about the failure."""


# region PipelineRunQueuedEvent


@dataclass
class PipelineRunQueuedEvent(CDEvent):
    CDEVENT_TYPE = "dev.cdevents.pipelinerun.queued." + SPEC_VERSION

    subject: PipelineRunSubject
    """PipelineRun subject."""


def new_pipelinerun_queued_event(
    context_id: str,
    context_source: str,
    context_timestamp: datetime,
    subject_id: str,
    subject_source: str,
    pipeline_name: str,
    url: str,
    custom_data: Union[str, Dict, None],
    custom_data_type: str,
) -> PipelineRunQueuedEvent:
    """Creates a new pipelinerun queued CDEvent."""

    context = Context(
        type=PipelineRunQueuedEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=context_id,
        source=context_source,
        timestamp=context_timestamp,
    )

    subject = PipelineRunSubject(
        id=subject_id, source=subject_source, pipeline_name=pipeline_name, url=url
    )

    event = PipelineRunQueuedEvent(
        context=context, subject=subject, custom_data=custom_data, custom_data_type=custom_data_type
    )

    return event


# endregion PipelineRunQueuedEvent

# region PipelineRunStartedEvent


@dataclass
class PipelineRunStartedEvent(CDEvent):
    CDEVENT_TYPE = "dev.cdevents.pipelinerun.started." + SPEC_VERSION

    subject: PipelineRunSubject
    """PipelineRun subject."""


def new_pipelinerun_started_event(
    context_id: str,
    context_source: str,
    context_timestamp: datetime,
    subject_id: str,
    subject_source: str,
    pipeline_name: str,
    url: str,
    custom_data: Union[str, Dict, None],
    custom_data_type: str,
) -> PipelineRunStartedEvent:
    """Creates a new pipelinerun started CDEvent."""

    context = Context(
        type=PipelineRunStartedEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=context_id,
        source=context_source,
        timestamp=context_timestamp,
    )

    subject = PipelineRunSubject(
        id=subject_id, source=subject_source, pipeline_name=pipeline_name, url=url
    )

    event = PipelineRunStartedEvent(
        context=context, subject=subject, custom_data=custom_data, custom_data_type=custom_data_type
    )

    return event


# endregion PipelineRunStartedEvent

# region PipelineRunFinishedEvent


@dataclass
class PipelineRunFinishedEvent(CDEvent):
    CDEVENT_TYPE = "dev.cdevents.pipelinerun.finished." + SPEC_VERSION

    subject: PipelineRunSubject
    """PipelineRun subject."""


def new_pipelinerun_finished_event(
    context_id: str,
    context_source: str,
    context_timestamp: datetime,
    subject_id: str,
    subject_source: str,
    pipeline_name: str,
    url: str,
    outcome: str,
    errors: str,
    custom_data: Union[str, Dict, None],
    custom_data_type: str,
) -> PipelineRunFinishedEvent:
    """Creates a new pipelinerun finished CDEvent."""

    context = Context(
        type=PipelineRunFinishedEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=context_id,
        source=context_source,
        timestamp=context_timestamp,
    )

    subject = PipelineRunFinishedSubject(
        id=subject_id,
        source=subject_source,
        pipeline_name=pipeline_name,
        url=url,
        outcome=outcome,
        errors=errors,
    )

    event = PipelineRunFinishedEvent(
        context=context, subject=subject, custom_data=custom_data, custom_data_type=custom_data_type
    )

    return event


# endregion PipelineRunFinishedEvent
