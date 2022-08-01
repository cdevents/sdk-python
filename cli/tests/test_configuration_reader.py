"""Module testing ConfigurationReader"""
import json
import unittest
from pathlib import Path
from unittest.mock import patch

import pytest
import yaml

from cdevents.cli.configuration_reader import ConfigurationReader

# pylint: disable=missing-function-docstring, protected-access, missing-class-docstring
TEST_DIR = Path(__file__).parent
CONFIG_DIR: Path = Path(TEST_DIR, "configurations")

YAML_CONFIG_1 = """---
configuration:
  source:
    name: cde-cli
  client:
    host: http://localhost:8080
"""
DICT_CONFIG_1 = yaml.safe_load(YAML_CONFIG_1)

JSON_CONFIG_1 = json.dumps(DICT_CONFIG_1)
YAML_CONFIG_2 = """---
configuration:
  source:
    name: mysource
  client:
    host: http://myhost:5000
"""
DICT_CONFIG_2 = {
    "configuration": {
        "source": {"name": "mysource"},
        "client": {"host": "http://myhost:5000"},
    },
}

DUMMY_PATH = "my/dummy/path/dummy.yaml"


class TestConfigurationReader(unittest.TestCase):
    # pylint: disable=unused-argument
    def setUp(self) -> None:
        self.reader = ConfigurationReader()

    @pytest.mark.unit
    @patch.object(Path, "exists", return_value=False)
    def test_read_configuration_with_invalid_file_path_then_exception(self, mocked_exists):
        with self.assertRaises(FileNotFoundError):
            self.reader.read_configuration(Path(DUMMY_PATH))

    @pytest.mark.unit
    @patch.object(Path, "read_text", return_value=YAML_CONFIG_1)
    @patch.object(Path, "exists", return_value=True)
    def test_read_configuration_with_valid_yaml_file(self, mocked_exists, mocked_read_text):
        self.reader.read_configuration(Path(DUMMY_PATH))
        actual = self.reader.configuration
        self.assertDictEqual(actual, DICT_CONFIG_1)

    @pytest.mark.unit
    @patch.object(Path, "read_text", return_value=JSON_CONFIG_1)
    @patch.object(Path, "exists", return_value=True)
    def test_read_configuration_with_valid_json_file(self, mocked_exists, mocked_read_text):
        self.reader.read_configuration(Path("path/to/my/config.json"))
        actual = self.reader.configuration
        self.assertDictEqual(actual, DICT_CONFIG_1)

    @pytest.mark.unit
    @patch.object(Path, "exists", return_value=True)
    def test_read_configuration_with_invalid_filetype_then_value_error(
        self,
        mocked_exists,
    ):
        with self.assertRaises(ValueError):
            self.reader.read_configuration(Path("path/to/my/invalid_config.jsonX"))

    @pytest.mark.unit
    @patch.object(Path, "read_text", side_effect=[YAML_CONFIG_1, YAML_CONFIG_2])
    @patch.object(Path, "exists", return_value=True)
    def test_read_configuration_with_2_configs(self, mocked_exists, mocked_read_text):
        """Second configuration overwrites previous."""
        self.reader.read_configuration(Path(DUMMY_PATH))
        actual = self.reader.configuration
        self.assertDictEqual(actual, DICT_CONFIG_1)
        self.reader.read_configuration(Path("dummy_config2.yml"))
        actual_2 = self.reader.configuration
        self.assertDictEqual(actual_2, DICT_CONFIG_2)

    @pytest.mark.unit
    def test_is_supported_suffix_with_valid_suffix(self):
        self.assertTrue(ConfigurationReader._is_supported_json_suffix(Path("valid_suffix.json")))
        self.assertTrue(ConfigurationReader._is_supported_yaml_suffix(Path("valid_suffix.yml")))
        self.assertTrue(ConfigurationReader._is_supported_yaml_suffix(Path("valid_suffix.yAMl")))

    @pytest.mark.unit
    def test_is_supported_suffix_with_invalid_suffix(self):
        self.assertFalse(ConfigurationReader._is_supported_yaml_suffix(Path("valid_suffix.berra")))
