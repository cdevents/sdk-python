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
"""Events under dev.cdevents.repository."""
from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Optional, Union
import datetime

from cdevents.cdevent import SPEC_VERSION, CDEvent
from cdevents.context import Context
from cdevents.subject import Subject
from pydanticEvent import parsedEvent


@dataclass
class RepositorySubjectContent:
    """Content for repository subjects."""

    name: str
    """Name of the repository."""

    owner: str
    """Owner of the repository."""

    url: str
    """URL to reference where the repository is located."""

    view_url: str
    """URL for humans to view the content of the repository."""


@dataclass
class RepositorySubject(Subject):
    """Subject for branch-related events."""

    content: RepositorySubjectContent
    """Content for change subjects."""

    type: str = field(default="repository", init=False)


# region RepositoryCreatedEvent


@dataclass
class RepositoryCreatedEvent(CDEvent):
    """Repository created event."""

    CDEVENT_TYPE = "dev.cdevents.repository.created." + SPEC_VERSION

    subject: RepositorySubject
    """Repository subject."""


def new_repository_created_event(
    context_id: str,
    context_source: str,
    context_timestamp: datetime,
    subject_id: str,
    subject_source: str,
    name: str,
    owner: str,
    url: str,
    view_url: str,
    custom_data: Union[str, Dict, None],
    custom_data_content_type: str,
) -> RepositoryCreatedEvent:
    """Creates a new repository created CDEvent."""
    input_data = parsedEvent(context_id= context_id, context_source = context_source, context_timestamp = context_timestamp, subject_id = subject_id, subject_source = subject_source,
    url = url, name=name, owner = owner, view_url = view_url,  custom_data = custom_data, custom_data_content_type = custom_data_content_type)
    context = Context(
        type=RepositoryCreatedEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=input_data.context_id,
        source=input_data.context_source,
        timestamp=input_data.context_timestamp,
    )
    content = RepositorySubjectContent(name=input_data.name, owner=input_data.owner, url=input_data.url, view_url=input_data.view_url)
    subject = RepositorySubject(id=input_data.subject_id, source=input_data.subject_source, content=content)

    event = RepositoryCreatedEvent(
        context=context,
        subject=subject,
        custom_data=input_data.custom_data,
        custom_data_content_type=input_data.custom_data_content_type,
    )

    return event


# endregion RepositoryCreatedEvent


# region RepositoryDeletedEvent


@dataclass
class RepositoryDeletedEvent(CDEvent):
    """Repository deleted event."""

    CDEVENT_TYPE = "dev.cdevents.repository.deleted." + SPEC_VERSION

    subject: RepositorySubject
    """Repository subject."""


def new_repository_deleted_event(
    context_id: str,
    context_source: str,
    context_timestamp: datetime,
    subject_id: str,
    subject_source: str,
    name: str,
    owner: str,
    url: str,
    view_url: str,
    custom_data: Union[str, Dict, None],
    custom_data_content_type: str,
) -> RepositoryDeletedEvent:
    input_data = parsedEvent(context_id= context_id, context_source = context_source, context_timestamp = context_timestamp, subject_id = subject_id, subject_source = subject_source,
    url = url, name=name, owner = owner, view_url = view_url,  custom_data = custom_data, custom_data_content_type = custom_data_content_type)
    """Creates a new repository deleted CDEvent."""
    context = Context(
        type=RepositoryDeletedEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=input_data.context_id,
        source=input_data.context_source,
        timestamp=input_data.context_timestamp,
    )

    content = RepositorySubjectContent(name=input_data.name, owner=input_data.owner, url=input_data.url, view_url=input_data.view_url)
    subject = RepositorySubject(id=input_data.subject_id, source=input_data.subject_source, content=content)

    event = RepositoryDeletedEvent(
        context=context,
        subject=subject,
        custom_data=input_data.custom_data,
        custom_data_content_type=input_data.custom_data_content_type,
    )

    return event



# endregion RepositoryDeletedEvent


# region RepositoryModifiedEvent


@dataclass
class RepositoryModifiedEvent(CDEvent):
    """Repository modified event."""

    CDEVENT_TYPE = "dev.cdevents.repository.modified." + SPEC_VERSION

    subject: RepositorySubject
    """Repository subject."""


def new_repository_modified_event(
    context_id: str,
    context_source: str,
    context_timestamp: datetime,
    subject_id: str,
    subject_source: str,
    name: str,
    owner: str,
    url: str,
    view_url: str,
    custom_data: Union[str, Dict, None],
    custom_data_content_type: str,
) -> RepositoryModifiedEvent:
    input_data = parsedEvent(context_id= context_id, context_source = context_source, context_timestamp = context_timestamp, subject_id = subject_id, subject_source = subject_source,
    url = url, name=name, owner = owner, view_url = view_url,  custom_data = custom_data, custom_data_content_type = custom_data_content_type)
    """Creates a new repository modified CDEvent."""
    context = Context(
        type=RepositoryModifiedEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=input_data.context_id,
        source=input_data.context_source,
        timestamp=input_data.context_timestamp,
    )

    content = RepositorySubjectContent(name=input_data.name, owner=input_data.owner, url=input_data.url, view_url=input_data.view_url)
    subject = RepositorySubject(id=input_data.subject_id, source=input_data.subject_source, content=content)

    event = RepositoryModifiedEvent(
        context=context,
        subject=subject,
        custom_data=input_data.custom_data,
        custom_data_content_type=input_data.custom_data_content_type,
    )

    return event


# endregion RepositoryModifiedEvent