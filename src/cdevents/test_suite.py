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
"""Events under dev.cdevents.testcase."""
from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Union
import datetime

from cdevents.cdevent import SPEC_VERSION, CDEvent
from cdevents.context import Context
from cdevents.subject import Subject
from pydanticEvent import parsedEvent


@dataclass
class TestCaseSubject(Subject):
    """Subject for testcase-related events."""

    content: Dict = field(default_factory=dict, init=False)
    """Content for test case subjects."""

    type: str = field(default="testCase", init=False)


# region TestCaseQueuedEvent


@dataclass
class TestCaseQueuedEvent(CDEvent):
    """Test case queued event."""

    CDEVENT_TYPE = "dev.cdevents.testcase.queued." + SPEC_VERSION

    subject: TestCaseSubject
    """TestCase subject."""


def new_testcase_queued_event(
    context_id: str,
    context_source: str,
    context_timestamp: datetime,
    subject_id: str,
    subject_source: str,
    custom_data: Union[str, Dict, None],
    custom_data_content_type: str,
) -> TestCaseQueuedEvent:
    input_data = parsedEvent(context_id= context_id, context_source = context_source, context_timestamp = context_timestamp, subject_id = subject_id, subject_source = subject_source,
    custom_data = custom_data, custom_data_content_type = custom_data_content_type)
    """Creates a new testcase queued CDEvent."""
    context = Context(
        type=TestCaseQueuedEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=input_data.context_id,
        source=input_data.context_source,
        timestamp=input_data.context_timestamp,
    )

    subject = TestCaseSubject(
        id=input_data.subject_id,
        source=input_data.subject_source,
    )

    event = TestCaseQueuedEvent(
        context=context,
        subject=subject,
        custom_data=input_data.custom_data,
        custom_data_content_type=input_data.custom_data_content_type,
    )

    return event


# endregion TestCaseQueuedEvent


# region TestCaseStartedEvent


@dataclass
class TestCaseStartedEvent(CDEvent):
    """Test case started event."""

    CDEVENT_TYPE = "dev.cdevents.testcase.started." + SPEC_VERSION

    subject: TestCaseSubject
    """TestCase subject."""


def new_testcase_started_event(
    context_id: str,
    context_source: str,
    context_timestamp: datetime,
    subject_id: str,
    subject_source: str,
    custom_data: Union[str, Dict, None],
    custom_data_content_type: str,
) -> TestCaseStartedEvent:
    input_data = parsedEvent(context_id= context_id, context_source = context_source, context_timestamp = context_timestamp, subject_id = subject_id, subject_source = subject_source,
    custom_data = custom_data, custom_data_content_type = custom_data_content_type)
    """Creates a new testcase started CDEvent."""
    context = Context(
        type=TestCaseStartedEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=input_data.context_id,
        source=input_data.context_source,
        timestamp=input_data.context_timestamp,
    )

    subject = TestCaseSubject(
        id=input_data.subject_id,
        source=input_data.subject_source,
    )

    event = TestCaseStartedEvent(
        context=context,
        subject=subject,
        custom_data=input_data.custom_data,
        custom_data_content_type=input_data.custom_data_content_type,
    )

    return event


# endregion TestCaseStartedEvent

# region TestCaseFinishedEvent


@dataclass
class TestCaseFinishedEvent(CDEvent):
    """Test case finished event."""

    CDEVENT_TYPE = "dev.cdevents.testcase.finished." + SPEC_VERSION

    subject: TestCaseSubject
    """TestCase subject."""


def new_testcase_finished_event(
    context_id: str,
    context_source: str,
    context_timestamp: datetime,
    subject_id: str,
    subject_source: str,
    custom_data: Union[str, Dict, None],
    custom_data_content_type: str,
) -> TestCaseFinishedEvent:
    input_data = parsedEvent(context_id= context_id, context_source = context_source, context_timestamp = context_timestamp, subject_id = subject_id, subject_source = subject_source,
    custom_data = custom_data, custom_data_content_type = custom_data_content_type)
    """Creates a new testcase finished CDEvent."""
    context = Context(
        type=TestCaseFinishedEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=input_data.context_id,
        source=input_data.context_source,
        timestamp=input_data.context_timestamp,
    )

    subject = TestCaseSubject(
        id=input_data.subject_id,
        source=input_data.subject_source,
    )

    event = TestCaseFinishedEvent(
        context=context,
        subject=subject,
        custom_data=input_data.custom_data,
        custom_data_content_type=input_data.custom_data_content_type,
    )

    return event


# endregion TestCaseFinishedEvent