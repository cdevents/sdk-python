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
"""Events under dev.cdevents.artifact."""
from dataclasses import dataclass, field
from datetime import datetime
import datetime
from typing import Dict, Union

from cdevents.cdevent import SPEC_VERSION, CDEvent
from cdevents.context import Context
from cdevents.subject import Subject
from pydanticEvent import parsedEvent


@dataclass
class ArtifactPackagedSubjectContent:
    """Content for artifact subjects."""

    change: Dict
    """Change from which the artifact was created."""


@dataclass
class ArtifactPackagedSubject(Subject):
    """Subject for artifact-related events."""

    id: str
    """PURL format identifier for the artifact."""

    source: str
    """Source in which the artifact can be found."""

    type: str = field(default="artifact", init=False)

    content: ArtifactPackagedSubjectContent
    """Content for artifact subject."""


@dataclass
class ArtifactPublishedSubject(Subject):
    """Subject for artifact-related events."""

    id: str
    """PURL format identifier for the artifact."""

    source: str
    """Source in which the artifact can be found."""

    type: str = field(default="artifact", init=False)

    content: Dict = field(default_factory=dict, init=False)


# region ArtifactPackagedEvent


@dataclass
class ArtifactPackagedEvent(CDEvent):
    """Artifact packaged event."""

    CDEVENT_TYPE = "dev.cdevents.artifact.packaged." + SPEC_VERSION

    subject: ArtifactPackagedSubject
    """Artifact subject."""


def new_artifact_packaged_event(
    context_id: str,
    context_source: str,
    context_timestamp: datetime,
    subject_id: str,
    subject_source: str,
    change: Dict[str, str],
    custom_data: Union[str, Dict, None],
    custom_data_content_type: str,
) -> ArtifactPackagedEvent:
    input_data = parsedEvent(context_id= context_id, context_source = context_source, context_timestamp = context_timestamp, subject_id = subject_id, subject_source = subject_source,
    change=change, custom_data = custom_data, custom_data_content_type = custom_data_content_type)
    """Creates a new artifact packaged CDEvent."""
    context = Context(
        type=ArtifactPackagedEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=input_data.context_id,
        source=input_data.context_source,
        timestamp=input_data.context_timestamp,
    )

    content = ArtifactPackagedSubjectContent(change=input_data.change)
    subject = ArtifactPackagedSubject(id=input_data.subject_id, source=input_data.subject_source, content=content)

    event = ArtifactPackagedEvent(
        context=context,
        subject=subject,
        custom_data=input_data.custom_data,
        custom_data_content_type=input_data.custom_data_content_type,
    )

    return event
# endregion ArtifactPackagedEvent

# region ArtifactPublishedEvent


@dataclass
class ArtifactPublishedEvent(CDEvent):
    """Artifact published event."""

    CDEVENT_TYPE = "dev.cdevents.artifact.published." + SPEC_VERSION

    subject: ArtifactPublishedSubject
    """Artifact subject."""


def new_artifact_published_event(
    context_id: str,
    context_source: str,
    context_timestamp: datetime,
    subject_id: str,
    subject_source: str,
    custom_data: Union[str, Dict, None],
    custom_data_content_type: str,
) -> ArtifactPublishedEvent:
    input_data = parsedEvent(context_id= context_id, context_source = context_source, context_timestamp = context_timestamp, subject_id = subject_id, subject_source = subject_source,
    custom_data = custom_data, custom_data_content_type = custom_data_content_type)
    """Creates a new artifact published CDEvent."""
    context = Context(
        type=ArtifactPublishedEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=input_data.context_id,
        source=input_data.context_source,
        timestamp=input_data.context_timestamp,
    )

    subject = ArtifactPublishedSubject(id=input_data.subject_id, source=input_data.subject_source)

    event = ArtifactPublishedEvent(
        context=context,
        subject=subject,
        custom_data=input_data.custom_data,
        custom_data_content_type=input_data.custom_data_content_type,
    )

    return event

# endregion ArtifactPublishedEvent