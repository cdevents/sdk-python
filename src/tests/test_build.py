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
    BuildFinishedEvent,
    BuildQueuedEvent,
    BuildStartedEvent,
    new_build_finished_event,
    new_build_queued_event,
    new_build_started_event,
    to_cloudevent,
)


def test_build_queued(schema_validation_error):
    event = new_build_queued_event(
        context_id="CONTEXT_ID",
        context_source="CONTEXT_SOURCE",
        context_timestamp=datetime.datetime.now(),
        subject_id="SUBJECT_ID",
        subject_source="SUBJECT_SOURCE",
        custom_data={"hello_message": "hi!"},
        custom_data_content_type="application/json",
    )

    cloudevent = to_cloudevent(event)

    assert cloudevent.get("type") == BuildQueuedEvent.CDEVENT_TYPE
    assert not schema_validation_error("buildqueued.json", cloudevent)


def test_build_started(schema_validation_error):
    event = new_build_started_event(
        context_id="CONTEXT_ID",
        context_source="CONTEXT_SOURCE",
        context_timestamp=datetime.datetime.now(),
        subject_id="SUBJECT_ID",
        subject_source="SUBJECT_SOURCE",
        custom_data={"hello_message": "hi!"},
        custom_data_content_type="application/json",
    )

    cloudevent = to_cloudevent(event)

    assert cloudevent.get("type") == BuildStartedEvent.CDEVENT_TYPE
    assert not schema_validation_error("buildstarted.json", cloudevent)


def test_build_finished(schema_validation_error):
    event = new_build_finished_event(
        context_id="CONTEXT_ID",
        context_source="CONTEXT_SOURCE",
        context_timestamp=datetime.datetime.now(),
        subject_id="SUBJECT_ID",
        subject_source="SUBJECT_SOURCE",
        custom_data={"hello_message": "hi!"},
        custom_data_content_type="application/json",
        artifact_id="ARTIFACT_ID",
    )

    cloudevent = to_cloudevent(event)

    assert cloudevent.get("type") == BuildFinishedEvent.CDEVENT_TYPE
    assert not schema_validation_error("buildfinished.json", cloudevent)
