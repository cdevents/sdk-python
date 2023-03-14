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
import datetime

from cdevents import (
    ServiceDeployedEvent,
    ServicePublishedEvent,
    ServiceRemovedEvent,
    ServiceRolledbackEvent,
    ServiceUpgradedEvent,
    new_service_deployed_event,
    new_service_published_event,
    new_service_removed_event,
    new_service_rolledback_event,
    new_service_upgraded_event,
    to_cloudevent,
)


def test_service_deployed(schema_validation_error):
    event = new_service_deployed_event(
        context_id="CONTEXT_ID",
        context_source="CONTEXT_SOURCE",
        context_timestamp=datetime.datetime.now(),
        subject_id="SUBJECT_ID",
        subject_source="SUBJECT_SOURCE",
        custom_data={"hello_message": "hi!"},
        custom_data_content_type="application/json",
        artifact_id="ARTIFACT_ID",
        environment={"id": "ENVIRONMENT_ID"},
    )

    cloudevent = to_cloudevent(event)

    assert cloudevent.get("type") == ServiceDeployedEvent.CDEVENT_TYPE
    assert not schema_validation_error("servicedeployed.json", cloudevent)


def test_service_published(schema_validation_error):
    event = new_service_published_event(
        context_id="CONTEXT_ID",
        context_source="CONTEXT_SOURCE",
        context_timestamp=datetime.datetime.now(),
        subject_id="SUBJECT_ID",
        subject_source="SUBJECT_SOURCE",
        custom_data={"hello_message": "hi!"},
        custom_data_content_type="application/json",
        environment={"id": "ENVIRONMENT_ID"},
    )

    cloudevent = to_cloudevent(event)

    assert cloudevent.get("type") == ServicePublishedEvent.CDEVENT_TYPE
    assert not schema_validation_error("servicepublished.json", cloudevent)


def test_service_removed(schema_validation_error):
    event = new_service_removed_event(
        context_id="CONTEXT_ID",
        context_source="CONTEXT_SOURCE",
        context_timestamp=datetime.datetime.now(),
        subject_id="SUBJECT_ID",
        subject_source="SUBJECT_SOURCE",
        custom_data={"hello_message": "hi!"},
        custom_data_content_type="application/json",
        environment={"id": "ENVIRONMENT_ID"},
    )

    cloudevent = to_cloudevent(event)

    assert cloudevent.get("type") == ServiceRemovedEvent.CDEVENT_TYPE
    assert not schema_validation_error("serviceremoved.json", cloudevent)


def test_service_rolledback(schema_validation_error):
    event = new_service_rolledback_event(
        context_id="CONTEXT_ID",
        context_source="CONTEXT_SOURCE",
        context_timestamp=datetime.datetime.now(),
        subject_id="SUBJECT_ID",
        subject_source="SUBJECT_SOURCE",
        custom_data={"hello_message": "hi!"},
        custom_data_content_type="application/json",
        artifact_id="ARTIFACT_ID",
        environment={"id": "ENVIRONMENT_ID"},
    )

    cloudevent = to_cloudevent(event)

    assert cloudevent.get("type") == ServiceRolledbackEvent.CDEVENT_TYPE
    assert not schema_validation_error("servicerolledback.json", cloudevent)


def test_service_upgraded(schema_validation_error):
    event = new_service_upgraded_event(
        context_id="CONTEXT_ID",
        context_source="CONTEXT_SOURCE",
        context_timestamp=datetime.datetime.now(),
        subject_id="SUBJECT_ID",
        subject_source="SUBJECT_SOURCE",
        custom_data={"hello_message": "hi!"},
        custom_data_content_type="application/json",
        artifact_id="ARTIFACT_ID",
        environment={"id": "ENVIRONMENT_ID"},
    )

    cloudevent = to_cloudevent(event)

    assert cloudevent.get("type") == ServiceUpgradedEvent.CDEVENT_TYPE
    assert not schema_validation_error("serviceupgraded.json", cloudevent)
