"""Module for tests related to configuration_handler."""
import os
from pathlib import Path

import pytest

from cdevents.cli.configuration_handler import ConfigurationHandler

# pylint: disable=missing-function-docstring, protected-access, missing-class-docstring
THIS_DIR: Path = Path(__file__).parent
TEST_CONFIG_FILE: str = Path(THIS_DIR, "configuration_test.yaml").as_posix()


@pytest.mark.unit
def test_create_config_handler():

    handler = ConfigurationHandler.create_new(TEST_CONFIG_FILE)
    assert isinstance(handler, ConfigurationHandler)

    assert handler.source.name == "cde-cli"
    assert handler.client.host == "http://localhost:8080"


@pytest.mark.unit
def test_create_config_handler_with_override():

    expected_source_name = "MySourceName"
    expected_client_host = "http://myhost:5000"
    override_config = {
        "source": {
            "name": expected_source_name,
        },
        "client": {
            "host": expected_client_host,
        },
    }
    handler = ConfigurationHandler.create_new(TEST_CONFIG_FILE, override_config=override_config)
    assert isinstance(handler, ConfigurationHandler)

    assert handler.source.name == expected_source_name
    assert handler.client.host == expected_client_host


@pytest.mark.unit
def test_create_empty_override_dict():

    expected = {}
    actual = ConfigurationHandler.create_override_config()
    assert expected == actual
