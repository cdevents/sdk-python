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
import dataclasses

import humps
from cloudevents.http import CloudEvent

from cdevents.cdevent import CDEvent


def to_cloudevent(event: CDEvent) -> CloudEvent:
    """Creates a new CloudEvent from a CDEvent."""
    attributes = {
        "type": event.context.type,
        "source": event.context.source,
        "subject": event.subject.id,
        "datacontenttype": "application/json",
    }
    data = dataclasses.asdict(event)

    # Convert the context timestamp to a string
    data["context"]["timestamp"] = str(data["context"]["timestamp"])

    # Don't camelize custom data content
    custom_data = None
    if "custom_data" in data:
        custom_data = data["custom_data"]
        data.pop("custom_data")

    # Camelize keys
    camelized_data = humps.camelize(data)

    # Put the custom_data content back if it exists
    if custom_data:
        camelized_data["customData"] = custom_data

    return CloudEvent(attributes=attributes, data=camelized_data)
