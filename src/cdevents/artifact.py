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
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Union

from cdevents.cdevent import SPEC_VERSION, CDEvent
from cdevents.context import Context
from cdevents.subject import Subject


@dataclass
class ArtifactSubject(Subject):
    """Subject for artifact-related events."""

    id: str
    """PURL format identifier for the artifact."""

    source: str
    """Source in which the artifact can be found."""


# region ArtifactPackagedEvent


@dataclass
class ArtifactPackagedEvent(CDEvent):
    CDEVENT_TYPE = "dev.cdevents.artifact.packaged." + SPEC_VERSION

    subject: ArtifactSubject
    """Artifact subject."""


def new_artifact_packaged_event(
    context_id: str,
    context_source: str,
    context_timestamp: datetime,
    subject_id: str,
    subject_source: str,
    custom_data: Union[str, Dict, None],
    custom_data_type: str,
) -> ArtifactPackagedEvent:
    """Creates a new artifact packaged CDEvent."""

    context = Context(
        type=ArtifactPackagedEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=context_id,
        source=context_source,
        timestamp=context_timestamp,
    )

    subject = ArtifactSubject(id=subject_id, source=subject_source)

    event = ArtifactPackagedEvent(
        context=context, subject=subject, custom_data=custom_data, custom_data_type=custom_data_type
    )

    return event


# endregion ArtifactPackagedEvent

# region ArtifactPublishedEvent


@dataclass
class ArtifactPublishedEvent(CDEvent):
    CDEVENT_TYPE = "dev.cdevents.artifact.published." + SPEC_VERSION

    subject: ArtifactSubject
    """Artifact subject."""


def new_artifact_published_event(
    context_id: str,
    context_source: str,
    context_timestamp: datetime,
    subject_id: str,
    subject_source: str,
    custom_data: Union[str, Dict, None],
    custom_data_type: str,
) -> ArtifactPublishedEvent:
    """Creates a new artifact published CDEvent."""

    context = Context(
        type=ArtifactPublishedEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=context_id,
        source=context_source,
        timestamp=context_timestamp,
    )

    subject = ArtifactSubject(id=subject_id, source=subject_source)

    event = ArtifactPublishedEvent(
        context=context, subject=subject, custom_data=custom_data, custom_data_type=custom_data_type
    )

    return event


# endregion ArtifactPublishedEvent
