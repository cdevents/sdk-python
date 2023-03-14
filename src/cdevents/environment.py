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
"""Events under dev.cdevents.environment"""
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Optional, Union

from cdevents.cdevent import SPEC_VERSION, CDEvent
from cdevents.context import Context
from cdevents.subject import Subject


@dataclass
class EnvironmentSubject(Subject):
    """Subject for branch-related events."""

    name: str
    """Name of the environment."""

    url: str
    """URL to reference where the environment is located."""


# region EnvironmentCreatedEvent


@dataclass
class EnvironmentCreatedEvent(CDEvent):
    CDEVENT_TYPE = "dev.cdevents.environment.created." + SPEC_VERSION

    subject: EnvironmentSubject
    """Environment subject."""


def new_environment_created_event(
    context_id: str,
    context_source: str,
    context_timestamp: datetime,
    subject_id: str,
    subject_source: str,
    name: str,
    url: str,
    custom_data: Union[str, Dict, None],
    custom_data_type: str,
) -> EnvironmentCreatedEvent:
    """Creates a new environment created CDEvent."""

    context = Context(
        type=EnvironmentCreatedEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=context_id,
        source=context_source,
        timestamp=context_timestamp,
    )

    subject = EnvironmentSubject(id=subject_id, source=subject_source, name=name, url=url)

    event = EnvironmentCreatedEvent(
        context=context, subject=subject, custom_data=custom_data, custom_data_type=custom_data_type
    )

    return event


# endregion EnvironmentCreatedEvent


# region EnvironmentDeletedEvent


@dataclass
class EnvironmentDeletedEvent(CDEvent):
    CDEVENT_TYPE = "dev.cdevents.environment.deleted." + SPEC_VERSION

    subject: EnvironmentSubject
    """Environment subject."""


def new_environment_deleted_event(
    context_id: str,
    context_source: str,
    context_timestamp: datetime,
    subject_id: str,
    subject_source: str,
    name: str,
    url: str,
    custom_data: Union[str, Dict, None],
    custom_data_type: str,
) -> EnvironmentDeletedEvent:
    """Creates a new environment deleted CDEvent."""

    context = Context(
        type=EnvironmentDeletedEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=context_id,
        source=context_source,
        timestamp=context_timestamp,
    )

    subject = EnvironmentSubject(id=subject_id, source=subject_source, name=name, url=url)

    event = EnvironmentDeletedEvent(
        context=context, subject=subject, custom_data=custom_data, custom_data_type=custom_data_type
    )

    return event


# endregion EnvironmentDeletedEvent


# region EnvironmentModifiedEvent


@dataclass
class EnvironmentModifiedEvent(CDEvent):
    CDEVENT_TYPE = "dev.cdevents.environment.modified." + SPEC_VERSION

    subject: EnvironmentSubject
    """Environment subject."""


def new_environment_modified_event(
    context_id: str,
    context_source: str,
    context_timestamp: datetime,
    subject_id: str,
    subject_source: str,
    name: str,
    url: str,
    custom_data: Union[str, Dict, None],
    custom_data_type: str,
) -> EnvironmentModifiedEvent:
    """Creates a new environment modified CDEvent."""

    context = Context(
        type=EnvironmentModifiedEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=context_id,
        source=context_source,
        timestamp=context_timestamp,
    )

    subject = EnvironmentSubject(id=subject_id, source=subject_source, name=name, url=url)

    event = EnvironmentModifiedEvent(
        context=context, subject=subject, custom_data=custom_data, custom_data_type=custom_data_type
    )

    return event


# endregion EnvironmentModifiedEvent
