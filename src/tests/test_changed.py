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
    to_cloudevent,
)


def test_change_abandoned(schema_validation_error):
    event = new_change_abandoned_event(
        context_id="CONTEXT_ID",
        context_source="CONTEXT_SOURCE",
        context_timestamp=datetime.datetime.now(),
        subject_id="SUBJECT_ID",
        subject_source="SUBJECT_SOURCE",
        custom_data={"hello_message": "hi!"},
        custom_data_content_type="application/json",
        repository={"id": "REPOSITORY_ID"},
    )

    cloudevent = to_cloudevent(event)

    assert cloudevent.get("type") == ChangeAbandonedEvent.CDEVENT_TYPE
    assert not schema_validation_error("changeabandoned.json", cloudevent)


def test_change_created(schema_validation_error):
    event = new_change_created_event(
        context_id="CONTEXT_ID",
        context_source="CONTEXT_SOURCE",
        context_timestamp=datetime.datetime.now(),
        subject_id="SUBJECT_ID",
        subject_source="SUBJECT_SOURCE",
        custom_data={"hello_message": "hi!"},
        custom_data_content_type="application/json",
        repository={"id": "REPOSITORY_ID"},
    )

    cloudevent = to_cloudevent(event)

    assert cloudevent.get("type") == ChangeCreatedEvent.CDEVENT_TYPE
    assert not schema_validation_error("changecreated.json", cloudevent)


def test_change_merged(schema_validation_error):
    event = new_change_merged_event(
        context_id="CONTEXT_ID",
        context_source="CONTEXT_SOURCE",
        context_timestamp=datetime.datetime.now(),
        subject_id="SUBJECT_ID",
        subject_source="SUBJECT_SOURCE",
        custom_data={"hello_message": "hi!"},
        custom_data_content_type="application/json",
        repository={"id": "REPOSITORY_ID"},
    )

    cloudevent = to_cloudevent(event)

    assert cloudevent.get("type") == ChangeMergedEvent.CDEVENT_TYPE
    assert not schema_validation_error("changemerged.json", cloudevent)


def test_change_reviewed(schema_validation_error):
    event = new_change_reviewed_event(
        context_id="CONTEXT_ID",
        context_source="CONTEXT_SOURCE",
        context_timestamp=datetime.datetime.now(),
        subject_id="SUBJECT_ID",
        subject_source="SUBJECT_SOURCE",
        custom_data={"hello_message": "hi!"},
        custom_data_content_type="application/json",
        repository={"id": "REPOSITORY_ID"},
    )

    cloudevent = to_cloudevent(event)

    assert cloudevent.get("type") == ChangeReviewedEvent.CDEVENT_TYPE
    assert not schema_validation_error("changereviewed.json", cloudevent)


def test_change_updated(schema_validation_error):
    event = new_change_updated_event(
        context_id="CONTEXT_ID",
        context_source="CONTEXT_SOURCE",
        context_timestamp=datetime.datetime.now(),
        subject_id="SUBJECT_ID",
        subject_source="SUBJECT_SOURCE",
        custom_data={"hello_message": "hi!"},
        custom_data_content_type="application/json",
        repository={"id": "REPOSITORY_ID"},
    )

    cloudevent = to_cloudevent(event)

    assert cloudevent.get("type") == ChangeUpdatedEvent.CDEVENT_TYPE
    assert not schema_validation_error("changeupdated.json", cloudevent)
