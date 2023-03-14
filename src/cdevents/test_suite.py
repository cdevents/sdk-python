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
"""Events under dev.cdevents.testsuite."""
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Union

from cdevents.cdevent import SPEC_VERSION, CDEvent
from cdevents.context import Context
from cdevents.subject import Subject


@dataclass
class TestSuiteSubject(Subject):
    """Subject for testsuite-related events."""

    pass


# region TestSuiteStartedEvent


@dataclass
class TestSuiteStartedEvent(CDEvent):
    """Test suite started event."""

    CDEVENT_TYPE = "dev.cdevents.testsuite.started." + SPEC_VERSION

    subject: TestSuiteSubject
    """TestSuite subject."""


def new_testsuite_started_event(
    context_id: str,
    context_source: str,
    context_timestamp: datetime,
    subject_id: str,
    subject_source: str,
    custom_data: Union[str, Dict, None],
    custom_data_type: str,
) -> TestSuiteStartedEvent:
    """Creates a new testsuite started CDEvent."""
    context = Context(
        type=TestSuiteStartedEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=context_id,
        source=context_source,
        timestamp=context_timestamp,
    )

    subject = TestSuiteSubject(
        id=subject_id,
        source=subject_source,
    )

    event = TestSuiteStartedEvent(
        context=context, subject=subject, custom_data=custom_data, custom_data_type=custom_data_type
    )

    return event


# endregion TestSuiteStartedEvent

# region TestSuiteFinishedEvent


@dataclass
class TestSuiteFinishedEvent(CDEvent):
    """Test suite finished event."""

    CDEVENT_TYPE = "dev.cdevents.testsuite.finished." + SPEC_VERSION

    subject: TestSuiteSubject
    """TestSuite subject."""


def new_testsuite_finished_event(
    context_id: str,
    context_source: str,
    context_timestamp: datetime,
    subject_id: str,
    subject_source: str,
    custom_data: Union[str, Dict, None],
    custom_data_type: str,
) -> TestSuiteFinishedEvent:
    """Creates a new testsuite finished CDEvent."""
    context = Context(
        type=TestSuiteFinishedEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=context_id,
        source=context_source,
        timestamp=context_timestamp,
    )

    subject = TestSuiteSubject(
        id=subject_id,
        source=subject_source,
    )

    event = TestSuiteFinishedEvent(
        context=context, subject=subject, custom_data=custom_data, custom_data_type=custom_data_type
    )

    return event


# endregion TestSuiteFinishedEvent
