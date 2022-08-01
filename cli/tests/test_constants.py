"""Tests for constants."""
from pathlib import Path

import pytest

from cdevents.cli.constants import DEFAULT_CONFIGURATION_FILE, LOGGING_CONFIGURATION_FILE

# pylint: disable=missing-function-docstring, missing-class-docstring

@pytest.mark.unit
def test_default_config_exist():
    assert Path(DEFAULT_CONFIGURATION_FILE).exists()


@pytest.mark.unit
def test_logging_config_file_exist():
    assert Path(LOGGING_CONFIGURATION_FILE).exists()
