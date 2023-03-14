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
    TestCaseFinishedEvent,
    TestCaseQueuedEvent,
    TestCaseStartedEvent,
    new_testcase_finished_event,
    new_testcase_queued_event,
    new_testcase_started_event,
    to_cloudevent,
)


def test_testcase_queued(schema_validation_error):
    event = new_testcase_queued_event(
        context_id="CONTEXT_ID",
        context_source="CONTEXT_SOURCE",
        context_timestamp=datetime.datetime.now(),
        subject_id="SUBJECT_ID",
        subject_source="SUBJECT_SOURCE",
        custom_data={"hello_message": "hi!"},
        custom_data_content_type="application/json",
    )

    cloudevent = to_cloudevent(event)

    assert cloudevent.get("type") == TestCaseQueuedEvent.CDEVENT_TYPE
    assert not schema_validation_error("testcasequeued.json", cloudevent)


def test_testcase_started(schema_validation_error):
    event = new_testcase_started_event(
        context_id="CONTEXT_ID",
        context_source="CONTEXT_SOURCE",
        context_timestamp=datetime.datetime.now(),
        subject_id="SUBJECT_ID",
        subject_source="SUBJECT_SOURCE",
        custom_data={"hello_message": "hi!"},
        custom_data_content_type="application/json",
    )

    cloudevent = to_cloudevent(event)

    assert cloudevent.get("type") == TestCaseStartedEvent.CDEVENT_TYPE
    assert not schema_validation_error("testcasestarted.json", cloudevent)


def test_testcase_finished(schema_validation_error):
    event = new_testcase_finished_event(
        context_id="CONTEXT_ID",
        context_source="CONTEXT_SOURCE",
        context_timestamp=datetime.datetime.now(),
        subject_id="SUBJECT_ID",
        subject_source="SUBJECT_SOURCE",
        custom_data={"hello_message": "hi!"},
        custom_data_content_type="application/json",
    )

    cloudevent = to_cloudevent(event)

    assert cloudevent.get("type") == TestCaseFinishedEvent.CDEVENT_TYPE
    assert not schema_validation_error("testcasefinished.json", cloudevent)
