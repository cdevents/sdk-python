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
from typing import Dict, Union

from cdevents.cdevent import SPEC_VERSION, CDEvent
from cdevents.context import Context
from cdevents.subject import Subject


@dataclass
class ServiceSubjectContent:
    """Content for service subjects."""

    environment: Dict[str, str]
    """Environment where the service runs."""


@dataclass
class ServiceArtifactSubjectContent(ServiceSubjectContent):
    """Content for service subjects that include use of an artifact."""

    artifact_id: str
    """ID of the artifact used for the service."""


@dataclass
class ServiceSubject(Subject):
    """Subject for service-related events."""

    content: ServiceSubjectContent
    """Content for service subjects."""

    type: str = field(default="repository", init=False)


@dataclass
class ServiceArtifactSubject(ServiceSubject):
    """Subject for service-related events that use an artifact."""

    content: ServiceArtifactSubjectContent
    """Content for service subjects."""


# region ServiceDeployedEvent


@dataclass
class ServiceDeployedEvent(CDEvent):
    """Service deployed event."""

    CDEVENT_TYPE = "dev.cdevents.service.deployed." + SPEC_VERSION

    subject: ServiceArtifactSubject
    """Service subject."""


def new_service_deployed_event(
    context_id: str,
    context_source: str,
    context_timestamp: datetime,
    subject_id: str,
    subject_source: str,
    environment: Dict[str, str],
    artifact_id: str,
    custom_data: Union[str, Dict, None],
    custom_data_content_type: str,
) -> ServiceDeployedEvent:
    """Creates a new service deployed CDEvent."""
    context = Context(
        type=ServiceDeployedEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=context_id,
        source=context_source,
        timestamp=context_timestamp,
    )

    content = ServiceArtifactSubjectContent(artifact_id=artifact_id, environment=environment)
    subject = ServiceArtifactSubject(id=subject_id, source=subject_source, content=content)

    event = ServiceDeployedEvent(
        context=context,
        subject=subject,
        custom_data=custom_data,
        custom_data_content_type=custom_data_content_type,
    )

    return event


# endregion ServiceDeployedEvent


# region ServicePublishedEvent


@dataclass
class ServicePublishedEvent(CDEvent):
    """Service published event."""

    CDEVENT_TYPE = "dev.cdevents.service.published." + SPEC_VERSION

    subject: ServiceSubject
    """Service subject."""


def new_service_published_event(
    context_id: str,
    context_source: str,
    context_timestamp: datetime,
    subject_id: str,
    subject_source: str,
    environment: Dict[str, str],
    custom_data: Union[str, Dict, None],
    custom_data_content_type: str,
) -> ServicePublishedEvent:
    """Creates a new service published CDEvent."""
    context = Context(
        type=ServicePublishedEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=context_id,
        source=context_source,
        timestamp=context_timestamp,
    )

    content = ServiceSubjectContent(environment=environment)
    subject = ServiceSubject(id=subject_id, source=subject_source, content=content)

    event = ServicePublishedEvent(
        context=context,
        subject=subject,
        custom_data=custom_data,
        custom_data_content_type=custom_data_content_type,
    )

    return event


# endregion ServicePublishedEvent


# region ServiceRemovedEvent


@dataclass
class ServiceRemovedEvent(CDEvent):
    """Service removed event."""

    CDEVENT_TYPE = "dev.cdevents.service.removed." + SPEC_VERSION

    subject: ServiceSubject
    """Service subject."""


def new_service_removed_event(
    context_id: str,
    context_source: str,
    context_timestamp: datetime,
    subject_id: str,
    subject_source: str,
    environment: Dict[str, str],
    custom_data: Union[str, Dict, None],
    custom_data_content_type: str,
) -> ServiceRemovedEvent:
    """Creates a new service removed CDEvent."""
    context = Context(
        type=ServiceRemovedEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=context_id,
        source=context_source,
        timestamp=context_timestamp,
    )

    content = ServiceSubjectContent(environment=environment)
    subject = ServiceSubject(id=subject_id, source=subject_source, content=content)

    event = ServiceRemovedEvent(
        context=context,
        subject=subject,
        custom_data=custom_data,
        custom_data_content_type=custom_data_content_type,
    )

    return event


# endregion ServiceRemovedEvent


# region ServiceRolledbackEvent


@dataclass
class ServiceRolledbackEvent(CDEvent):
    """Service rolledback event."""

    CDEVENT_TYPE = "dev.cdevents.service.rolledback." + SPEC_VERSION

    subject: ServiceArtifactSubject
    """Service subject."""


def new_service_rolledback_event(
    context_id: str,
    context_source: str,
    context_timestamp: datetime,
    subject_id: str,
    subject_source: str,
    environment: Dict[str, str],
    artifact_id: str,
    custom_data: Union[str, Dict, None],
    custom_data_content_type: str,
) -> ServiceRolledbackEvent:
    """Creates a new service rolledback CDEvent."""
    context = Context(
        type=ServiceRolledbackEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=context_id,
        source=context_source,
        timestamp=context_timestamp,
    )

    content = ServiceArtifactSubjectContent(artifact_id=artifact_id, environment=environment)
    subject = ServiceArtifactSubject(id=subject_id, source=subject_source, content=content)

    event = ServiceRolledbackEvent(
        context=context,
        subject=subject,
        custom_data=custom_data,
        custom_data_content_type=custom_data_content_type,
    )

    return event


# endregion ServiceRolledbackEvent


# region ServiceUpgradedEvent


@dataclass
class ServiceUpgradedEvent(CDEvent):
    """Service upgraded event."""

    CDEVENT_TYPE = "dev.cdevents.service.upgraded." + SPEC_VERSION

    subject: ServiceArtifactSubject
    """Service subject."""


def new_service_upgraded_event(
    context_id: str,
    context_source: str,
    context_timestamp: datetime,
    subject_id: str,
    subject_source: str,
    environment: Dict[str, str],
    artifact_id: str,
    custom_data: Union[str, Dict, None],
    custom_data_content_type: str,
) -> ServiceUpgradedEvent:
    """Creates a new service upgraded CDEvent."""
    context = Context(
        type=ServiceUpgradedEvent.CDEVENT_TYPE,
        version=SPEC_VERSION,
        id=context_id,
        source=context_source,
        timestamp=context_timestamp,
    )

    content = ServiceArtifactSubjectContent(artifact_id=artifact_id, environment=environment)
    subject = ServiceArtifactSubject(id=subject_id, source=subject_source, content=content)

    event = ServiceUpgradedEvent(
        context=context,
        subject=subject,
        custom_data=custom_data,
        custom_data_content_type=custom_data_content_type,
    )

    return event


# endregion ServiceUpgradedEvent
