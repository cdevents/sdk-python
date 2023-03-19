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
import datetime

from cdevents import (
    PipelineRunFinishedEvent,
    PipelineRunQueuedEvent,
    PipelineRunStartedEvent,
    new_pipelinerun_finished_event,
    new_pipelinerun_queued_event,
    new_pipelinerun_started_event,
    to_cloudevent,
)


def test_pipelinerun_queued(schema_validation_error):
    event = new_pipelinerun_queued_event(
        context_id="CONTEXT_ID",
        context_source="CONTEXT_SOURCE",
        context_timestamp=datetime.datetime.now(),
        subject_id="SUBJECT_ID",
        subject_source="SUBJECT_SOURCE",
        custom_data={"hello_message": "hi!"},
        custom_data_content_type="application/json",
        pipeline_name="PIPELINE_NAME",
        url="https://pipeline.run",
    )

    cloudevent = to_cloudevent(event)

    assert cloudevent.get("type") == PipelineRunQueuedEvent.CDEVENT_TYPE
    assert not schema_validation_error("pipelinerunqueued.json", cloudevent)


def test_pipelinerun_started(schema_validation_error):
    event = new_pipelinerun_started_event(
        context_id="CONTEXT_ID",
        context_source="CONTEXT_SOURCE",
        context_timestamp=datetime.datetime.now(),
        subject_id="SUBJECT_ID",
        subject_source="SUBJECT_SOURCE",
        custom_data={"hello_message": "hi!"},
        custom_data_content_type="application/json",
        pipeline_name="PIPELINE_NAME",
        url="https://pipeline.run",
    )

    cloudevent = to_cloudevent(event)

    assert cloudevent.get("type") == PipelineRunStartedEvent.CDEVENT_TYPE
    assert not schema_validation_error("pipelinerunstarted.json", cloudevent)


def test_pipelinerun_finished(schema_validation_error):
    event = new_pipelinerun_finished_event(
        context_id="CONTEXT_ID",
        context_source="CONTEXT_SOURCE",
        context_timestamp=datetime.datetime.now(),
        subject_id="SUBJECT_ID",
        subject_source="SUBJECT_SOURCE",
        custom_data={"hello_message": "hi!"},
        custom_data_content_type="application/json",
        pipeline_name="PIPELINE_NAME",
        url="https://pipeline.run",
        outcome="success",
        errors="ERRORS",
    )

    cloudevent = to_cloudevent(event)

    assert cloudevent.get("type") == PipelineRunFinishedEvent.CDEVENT_TYPE
    assert not schema_validation_error("pipelinerunfinished.json", cloudevent)
