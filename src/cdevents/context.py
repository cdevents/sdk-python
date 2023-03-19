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
"""Shared context between all events."""
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Context:
    """Shared context for all CDEvents."""

    id: str
    """Identifier for an event.
    Subsequent delivery attempts of the MAY share the same id. This attribute matches the syntax and
    semantics of the id attribute of CloudEvents:
    https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md#id
    """

    type: str
    """Defines the type of event, as combination of a subject and predicate.
    Valid event types are defined in the vocabulary. All event types should be prefixed with dev.cdevents.
    One occurrence may have multiple events associated, as long as they have different event types
    """

    version: str
    """Version of the event."""

    source: str
    """Defines the context in which an event happened.
    The main purpose of the source is to provide global uniqueness for source + id.
    The source MAY identify a single producer or a group of producer that belong to the same application.
    """

    timestamp: datetime
    """Defines the time of the occurrence.
    When the time of the occurrence is not available, the time when the event was produced MAY be used.
    In case the transport layer should require a re-transmission of the event,
    the timestamp SHOULD NOT be updated, i.e. it should be the same for the same source + id combination.
    """
