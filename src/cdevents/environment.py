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
"""Events under dev.cdevents.environment."""
from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict,Union
import datetime

from cdevents.cdevent import SPEC_VERSION, CDEvent
from cdevents.context import Context
from cdevents.subject import Subject
from pydanticEvent import parsedEvent


@dataclass
class EnvironmentSubjectContent:
    """Content for environment subjects."""

    name: str
    """Name of the environment."""


@dataclass
class EnvironmentSubjectContentWithUrl(EnvironmentSubjectContent):
    """Content for environment subjects that includes a URL."""

    url: str
    """URL to reference where the environment is located."""


@dataclass
class EnvironmentSubject(Subject):
    """Subject for branch-related events."""

    content: EnvironmentSubjectContent
    """Content for change subjects."""

    type: str = field(default="environment", init=False)


@dataclass
class EnvironmentSubjectWithUrl(Subject):
    """Subject for branch-related events."""

    content: EnvironmentSubjectContentWithUrl
    """Content for change subjects."""

    type: str = field(default="environment", init=False)


# region EnvironmentCreatedEvent


@dataclass
class EnvironmentCreatedEvent(CDEvent):
    """Environment created event."""

    CDEVENT_TYPE = "dev.cdevents.environment.created." + SPEC_VERSION

    subject: EnvironmentSubjectWithUrl
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
    custom_data_content_type: str,
) -> EnvironmentCreatedEvent:
    input_data = parsedEvent(context_id= context_id, context_source = context_source, context_timestamp = context_timestamp, subject_id = subject_id, subject_source = subject_source,
    custom_data = custom_data, custom_data_content_type = custom_data_content_type, name = name, url = url)
    """Creates a new environment created CDEvent."""
    context = Context(
        type=EnvironmentCreatedEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=input_data.context_id,
        source=input_data.context_source,
        timestamp=input_data.context_timestamp,
    )

    content = EnvironmentSubjectContentWithUrl(name=input_data.name, url=input_data.url)
    subject = EnvironmentSubjectWithUrl(id=input_data.subject_id, source=input_data.subject_source, content=content)

    event = EnvironmentCreatedEvent(
        context=context,
        subject=subject,
        custom_data=input_data.custom_data,
        custom_data_content_type=input_data.custom_data_content_type,
    )

    return event


# endregion EnvironmentCreatedEvent


# region EnvironmentDeletedEvent


@dataclass
class EnvironmentDeletedEvent(CDEvent):
    """Environment deleted event."""

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
    custom_data: Union[str, Dict, None],
    custom_data_content_type: str,
) -> EnvironmentDeletedEvent:
    input_data = parsedEvent(context_id= context_id, context_source = context_source, context_timestamp = context_timestamp, subject_id = subject_id, subject_source = subject_source,
    custom_data = custom_data, custom_data_content_type = custom_data_content_type, name = name)
    """Creates a new environment deleted CDEvent."""
    context = Context(
        type=EnvironmentDeletedEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=input_data.context_id,
        source=input_data.context_source,
        timestamp=input_data.context_timestamp,
    )

    content = EnvironmentSubjectContent(name=input_data.name)
    subject = EnvironmentSubject(id=input_data.subject_id, source=input_data.subject_source, content=content)

    event = EnvironmentDeletedEvent(
        context=context,
        subject=subject,
        custom_data=input_data.custom_data,
        custom_data_content_type=input_data.custom_data_content_type,
    )

    return event


# endregion EnvironmentDeletedEvent


# region EnvironmentModifiedEvent


@dataclass
class EnvironmentModifiedEvent(CDEvent):
    """Environment modified event."""

    CDEVENT_TYPE = "dev.cdevents.environment.modified." + SPEC_VERSION

    subject: EnvironmentSubjectWithUrl
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
    custom_data_content_type: str,
) -> EnvironmentModifiedEvent:
    input_data = parsedEvent(context_id= context_id, context_source = context_source, context_timestamp = context_timestamp, subject_id = subject_id, subject_source = subject_source,
    custom_data = custom_data, custom_data_content_type = custom_data_content_type, name = name, url = url)
    """Creates a new environment modified CDEvent."""
    context = Context(
        type=EnvironmentModifiedEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=input_data.context_id,
        source=input_data.context_source,
        timestamp=input_data.context_timestamp,
    )

    content = EnvironmentSubjectContentWithUrl(name=input_data.name, url=input_data.url)
    subject = EnvironmentSubjectWithUrl(id=input_data.subject_id, source=input_data.subject_source, content=content)

    event = EnvironmentModifiedEvent(
        context=context,
        subject=subject,
        custom_data=input_data.custom_data,
        custom_data_content_type=input_data.custom_data_content_type,
    )

    return event


# endregion EnvironmentModifiedEvent