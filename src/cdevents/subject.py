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
"""Common subject for all CDEvents."""
from dataclasses import dataclass


@dataclass
class Subject:
    """Common subject for all CDEvents."""

    id: str
    """Identifier for a subject."""

    source: str
    """Defines the context in which the subject originated.
    In most cases the source of the subject matches the source of the event.
    This field should be used only in cases where the source of the subject is different from the source of the event.
    """
