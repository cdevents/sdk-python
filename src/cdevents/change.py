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
"""Events under dev.cdevents.change."""
from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Optional, Union

from cdevents.cdevent import SPEC_VERSION, CDEvent
from cdevents.context import Context
from cdevents.subject import Subject


@dataclass
class ChangeSubjectContent:
    """Content for change subjects."""

    repository: Dict[str, str]
    """A reference to the repository where the change event happened."""


@dataclass
class ChangeSubject(Subject):
    """Subject for change-related events."""

    content: ChangeSubjectContent
    """Content for change subjects."""

    type: str = field(default="change", init=False)


# region ChangeAbandonedEvent


@dataclass
class ChangeAbandonedEvent(CDEvent):
    """Change abandoned event."""

    CDEVENT_TYPE = "dev.cdevents.change.abandoned." + SPEC_VERSION

    subject: ChangeSubject
    """Change subject."""


def new_change_abandoned_event(
    context_id: str,
    context_source: str,
    context_timestamp: datetime,
    subject_id: str,
    subject_source: str,
    repository: Dict[str, str],
    custom_data: Union[str, Dict, None],
    custom_data_content_type: str,
) -> ChangeAbandonedEvent:
    """Creates a new change abandoned CDEvent."""
    context = Context(
        type=ChangeAbandonedEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=context_id,
        source=context_source,
        timestamp=context_timestamp,
    )

    content = ChangeSubjectContent(repository=repository)
    subject = ChangeSubject(id=subject_id, source=subject_source, content=content)

    event = ChangeAbandonedEvent(
        context=context,
        subject=subject,
        custom_data=custom_data,
        custom_data_content_type=custom_data_content_type,
    )

    return event


# endregion ChangeAbandonedEvent


# region ChangeCreatedEvent


@dataclass
class ChangeCreatedEvent(CDEvent):
    """Change created event."""

    CDEVENT_TYPE = "dev.cdevents.change.created." + SPEC_VERSION

    subject: ChangeSubject
    """Change subject."""


def new_change_created_event(
    context_id: str,
    context_source: str,
    context_timestamp: datetime,
    subject_id: str,
    subject_source: str,
    repository: Dict[str, str],
    custom_data: Union[str, Dict, None],
    custom_data_content_type: str,
) -> ChangeCreatedEvent:
    """Creates a new change created CDEvent."""
    context = Context(
        type=ChangeCreatedEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=context_id,
        source=context_source,
        timestamp=context_timestamp,
    )

    content = ChangeSubjectContent(repository=repository)
    subject = ChangeSubject(id=subject_id, source=subject_source, content=content)

    event = ChangeCreatedEvent(
        context=context,
        subject=subject,
        custom_data=custom_data,
        custom_data_content_type=custom_data_content_type,
    )

    return event


# endregion ChangeCreatedEvent


# region ChangeMergedEvent


@dataclass
class ChangeMergedEvent(CDEvent):
    """Change merged event."""

    CDEVENT_TYPE = "dev.cdevents.change.merged." + SPEC_VERSION

    subject: ChangeSubject
    """Change subject."""


def new_change_merged_event(
    context_id: str,
    context_source: str,
    context_timestamp: datetime,
    subject_id: str,
    subject_source: str,
    repository: Dict[str, str],
    custom_data: Union[str, Dict, None],
    custom_data_content_type: str,
) -> ChangeMergedEvent:
    """Creates a new change merged CDEvent."""
    context = Context(
        type=ChangeMergedEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=context_id,
        source=context_source,
        timestamp=context_timestamp,
    )

    content = ChangeSubjectContent(repository=repository)
    subject = ChangeSubject(id=subject_id, source=subject_source, content=content)

    event = ChangeMergedEvent(
        context=context,
        subject=subject,
        custom_data=custom_data,
        custom_data_content_type=custom_data_content_type,
    )

    return event


# endregion ChangeMergedEvent


# region ChangeReviewedEvent


@dataclass
class ChangeReviewedEvent(CDEvent):
    """Change reviewed event."""

    CDEVENT_TYPE = "dev.cdevents.change.reviewed." + SPEC_VERSION

    subject: ChangeSubject
    """Change subject."""


def new_change_reviewed_event(
    context_id: str,
    context_source: str,
    context_timestamp: datetime,
    subject_id: str,
    subject_source: str,
    repository: Dict[str, str],
    custom_data: Union[str, Dict, None],
    custom_data_content_type: str,
) -> ChangeReviewedEvent:
    """Creates a new change reviewed CDEvent."""
    context = Context(
        type=ChangeReviewedEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=context_id,
        source=context_source,
        timestamp=context_timestamp,
    )

    content = ChangeSubjectContent(repository=repository)
    subject = ChangeSubject(id=subject_id, source=subject_source, content=content)

    event = ChangeReviewedEvent(
        context=context,
        subject=subject,
        custom_data=custom_data,
        custom_data_content_type=custom_data_content_type,
    )

    return event


# endregion ChangeReviewedEvent


# region ChangeUpdatedEvent


@dataclass
class ChangeUpdatedEvent(CDEvent):
    """Change updated event."""

    CDEVENT_TYPE = "dev.cdevents.change.updated." + SPEC_VERSION

    subject: ChangeSubject
    """Change subject."""


def new_change_updated_event(
    context_id: str,
    context_source: str,
    context_timestamp: datetime,
    subject_id: str,
    subject_source: str,
    repository: Dict[str, str],
    custom_data: Union[str, Dict, None],
    custom_data_content_type: str,
) -> ChangeUpdatedEvent:
    """Creates a new change updated CDEvent."""
    context = Context(
        type=ChangeUpdatedEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=context_id,
        source=context_source,
        timestamp=context_timestamp,
    )

    content = ChangeSubjectContent(repository=repository)
    subject = ChangeSubject(id=subject_id, source=subject_source, content=content)

    event = ChangeUpdatedEvent(
        context=context,
        subject=subject,
        custom_data=custom_data,
        custom_data_content_type=custom_data_content_type,
    )

    return event


# endregion ChangeUpdatedEvent
