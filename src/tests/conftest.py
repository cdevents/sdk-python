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
import json
from pathlib import Path
from typing import Callable

import jsonschema
import pytest
from cloudevents.http import CloudEvent


@pytest.fixture()
def schema_validation_error() -> Callable[[str, CloudEvent], None]:
    def validator(schema_file_name: str, cloudevent: CloudEvent) -> str:
        schema = json.loads(
            Path(__file__).parent.joinpath("spec", "schemas", schema_file_name).read_text()
        )

        validation_error = ""
        try:
            data = cloudevent.data
            jsonschema.validate(data, schema)
        except jsonschema.exceptions.ValidationError as err:
            validation_error = err.message

        return validation_error

    return validator
