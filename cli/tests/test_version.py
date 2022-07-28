import re

import pytest

from cdevents.cli import __version__

# From https://semver.org/#is-there-a-suggested-regular-expression-regex-to-check-a-semver-string
VALID_SEMVER_REGEX = (
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)"
    r"(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$"
)


@pytest.mark.unit
def test_version_is_semantic():
    assert re.fullmatch(VALID_SEMVER_REGEX, __version__)
