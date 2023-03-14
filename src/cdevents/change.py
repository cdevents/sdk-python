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
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Optional, Union

from cdevents.cdevent import SPEC_VERSION, CDEvent
from cdevents.context import Context
from cdevents.subject import Subject


@dataclass
class ChangeSubject(Subject):
    """Subject for change-related events."""

    repository: Optional[Dict]
    """A reference to the repository where the change event happened."""


# region ChangeAbandonedEvent


@dataclass
class ChangeAbandonedEvent(CDEvent):
    CDEVENT_TYPE = "dev.cdevents.change.abandoned." + SPEC_VERSION

    subject: ChangeSubject
    """Change subject."""


def new_change_abandoned_event(
    context_id: str,
    context_source: str,
    context_timestamp: datetime,
    subject_id: str,
    subject_source: str,
    repository: Optional[Dict],
    custom_data: Union[str, Dict, None],
    custom_data_type: str,
) -> ChangeAbandonedEvent:
    """Creates a new change abandoned CDEvent."""

    context = Context(
        type=ChangeAbandonedEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=context_id,
        source=context_source,
        timestamp=context_timestamp,
    )

    subject = ChangeSubject(id=subject_id, source=subject_source, repository=repository)

    event = ChangeAbandonedEvent(
        context=context, subject=subject, custom_data=custom_data, custom_data_type=custom_data_type
    )

    return event


# endregion ChangeAbandonedEvent


# region ChangeCreatedEvent


@dataclass
class ChangeCreatedEvent(CDEvent):
    CDEVENT_TYPE = "dev.cdevents.change.created." + SPEC_VERSION

    subject: ChangeSubject
    """Change subject."""


def new_change_created_event(
    context_id: str,
    context_source: str,
    context_timestamp: datetime,
    subject_id: str,
    subject_source: str,
    repository: Optional[Dict],
    custom_data: Union[str, Dict, None],
    custom_data_type: str,
) -> ChangeCreatedEvent:
    """Creates a new change created CDEvent."""

    context = Context(
        type=ChangeCreatedEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=context_id,
        source=context_source,
        timestamp=context_timestamp,
    )

    subject = ChangeSubject(id=subject_id, source=subject_source, repository=repository)

    event = ChangeCreatedEvent(
        context=context, subject=subject, custom_data=custom_data, custom_data_type=custom_data_type
    )

    return event


# endregion ChangeCreatedEvent


# region ChangeMergedEvent


@dataclass
class ChangeMergedEvent(CDEvent):
    CDEVENT_TYPE = "dev.cdevents.change.merged." + SPEC_VERSION

    subject: ChangeSubject
    """Change subject."""


def new_change_merged_event(
    context_id: str,
    context_source: str,
    context_timestamp: datetime,
    subject_id: str,
    subject_source: str,
    repository: Optional[Dict],
    custom_data: Union[str, Dict, None],
    custom_data_type: str,
) -> ChangeMergedEvent:
    """Creates a new change merged CDEvent."""

    context = Context(
        type=ChangeMergedEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=context_id,
        source=context_source,
        timestamp=context_timestamp,
    )

    subject = ChangeSubject(id=subject_id, source=subject_source, repository=repository)

    event = ChangeMergedEvent(
        context=context, subject=subject, custom_data=custom_data, custom_data_type=custom_data_type
    )

    return event


# endregion ChangeMergedEvent


# region ChangeReviewedEvent


@dataclass
class ChangeReviewedEvent(CDEvent):
    CDEVENT_TYPE = "dev.cdevents.change.reviewed." + SPEC_VERSION

    subject: ChangeSubject
    """Change subject."""


def new_change_reviewed_event(
    context_id: str,
    context_source: str,
    context_timestamp: datetime,
    subject_id: str,
    subject_source: str,
    repository: Optional[Dict],
    custom_data: Union[str, Dict, None],
    custom_data_type: str,
) -> ChangeReviewedEvent:
    """Creates a new change reviewed CDEvent."""

    context = Context(
        type=ChangeReviewedEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=context_id,
        source=context_source,
        timestamp=context_timestamp,
    )

    subject = ChangeSubject(id=subject_id, source=subject_source, repository=repository)

    event = ChangeReviewedEvent(
        context=context, subject=subject, custom_data=custom_data, custom_data_type=custom_data_type
    )

    return event


# endregion ChangeReviewedEvent


# region ChangeUpdatedEvent


@dataclass
class ChangeUpdatedEvent(CDEvent):
    CDEVENT_TYPE = "dev.cdevents.change.updated." + SPEC_VERSION

    subject: ChangeSubject
    """Change subject."""


def new_change_updated_event(
    context_id: str,
    context_source: str,
    context_timestamp: datetime,
    subject_id: str,
    subject_source: str,
    repository: Optional[Dict],
    custom_data: Union[str, Dict, None],
    custom_data_type: str,
) -> ChangeUpdatedEvent:
    """Creates a new change updated CDEvent."""

    context = Context(
        type=ChangeUpdatedEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=context_id,
        source=context_source,
        timestamp=context_timestamp,
    )

    subject = ChangeSubject(id=subject_id, source=subject_source, repository=repository)

    event = ChangeUpdatedEvent(
        context=context, subject=subject, custom_data=custom_data, custom_data_type=custom_data_type
    )

    return event


# endregion ChangeUpdatedEvent
