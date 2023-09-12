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
"""Events under dev.cdevents.branch."""
from dataclasses import dataclass, field
from datetime import datetime
import datetime
from typing import Dict, Optional, Union

from cdevents.cdevent import SPEC_VERSION, CDEvent
from cdevents.context import Context
from cdevents.subject import Subject
from pydanticEvent import parsedEvent


@dataclass
class BranchSubjectContent:
    """Content for branch subjects."""

    repository: Dict[str, str]
    """A reference to the repository where the branch event happened."""


@dataclass
class BranchSubject(Subject):
    """Subject for branch-related events."""

    content: BranchSubjectContent
    """Content for branch subjects."""

    type: str = field(default="branch", init=False)


# region BranchCreatedEvent


@dataclass
class BranchCreatedEvent(CDEvent):
    """Branch created event."""

    CDEVENT_TYPE = "dev.cdevents.branch.created." + SPEC_VERSION

    subject: BranchSubject
    """Branch subject."""


def new_branch_created_event(
    context_id: str,
    context_source: str,
    context_timestamp: datetime,
    subject_id: str,
    subject_source: str,
    repository: Dict[str, str],
    custom_data: Union[str, Dict, None],
    custom_data_content_type: str,
) -> BranchCreatedEvent:
    input_data = parsedEvent(context_id= context_id, context_source = context_source, context_timestamp = context_timestamp, subject_id = subject_id, subject_source = subject_source,
    repository=repository, custom_data = custom_data, custom_data_content_type = custom_data_content_type)
    """Creates a new branch created CDEvent."""
    context = Context(
        type=BranchCreatedEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=input_data.context_id,
        source=input_data.context_source,
        timestamp=input_data.context_timestamp,
    )

    content = BranchSubjectContent(repository=input_data.repository)
    subject = BranchSubject(id=input_data.subject_id, source=input_data.subject_source, content=content)

    event = BranchCreatedEvent(
        context=context,
        subject=subject,
        custom_data=input_data.custom_data,
        custom_data_content_type=input_data.custom_data_content_type,
    )

    return event

# endregion BranchCreatedEvent


# region BranchDeletedEvent


@dataclass
class BranchDeletedEvent(CDEvent):
    """Branch deleted event."""

    CDEVENT_TYPE = "dev.cdevents.branch.deleted." + SPEC_VERSION

    subject: BranchSubject
    """Branch subject."""


def new_branch_deleted_event(
    context_id: str,
    context_source: str,
    context_timestamp: datetime,
    subject_id: str,
    subject_source: str,
    repository: Dict[str, str],
    custom_data: Union[str, Dict, None],
    custom_data_content_type: str,
) -> BranchDeletedEvent:
    input_data = parsedEvent(context_id= context_id, context_source = context_source, context_timestamp = context_timestamp, subject_id = subject_id, subject_source = subject_source,
    repository=repository, custom_data = custom_data, custom_data_content_type = custom_data_content_type)
    """Creates a new branch deleted CDEvent."""
    context = Context(
        type=BranchDeletedEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=input_data.context_id,
        source=input_data.context_source,
        timestamp=input_data.context_timestamp,
    )

    content = BranchSubjectContent(repository=input_data.repository)
    subject = BranchSubject(id=input_data.subject_id, source=input_data.subject_source, content=content)

    event = BranchDeletedEvent(
        context=context,
        subject=subject,
        custom_data=input_data.custom_data,
        custom_data_content_type=input_data.custom_data_content_type,
    )

    return event

# endregion BranchDeletedEvent