"""Testing for module utils."""
from datetime import datetime
from unittest import mock

import pytest
from cdevents.cli.utils import DictUtils, time_stamp


# pylint: disable=missing-function-docstring, protected-access, missing-class-docstring
@pytest.mark.unit
def test_merge_dicts_1():
    source = {"a": 66}
    target = {"b": 77, "c": 88}
    expected = {"a": 66, "b": 77, "c": 88}
    merge_and_test(source, target, expected)


@pytest.mark.unit
def test_merge_dicts_2():
    source = {"a": 66}
    target = {"a": 77}
    expected = {"a": 77}
    merge_and_test(source, target, expected)


@pytest.mark.unit
def test_merge_dicts_3():
    source = {}
    target = {"a": 77}
    expected = {"a": 77}
    merge_and_test(source, target, expected)


@pytest.mark.unit
def test_merge_dicts_3_1():
    target = {}
    source = {"a": 77}
    expected = {"a": 77}
    merge_and_test(source, target, expected)


@pytest.mark.unit
def test_merge_dicts_4():
    source = {"a": {"aa": 11, "aaa": {"aaaa": 111}}}
    target = {"b": {"bb": 22, "bbb": {"bbbb": 222}}}
    expected = {
        "a": {"aa": 11, "aaa": {"aaaa": 111}},
        "b": {"bb": 22, "bbb": {"bbbb": 222}},
    }
    merge_and_test(source, target, expected)


@pytest.mark.unit
def test_merge_dicts_5():
    source = {
        "a": {"aa": 12, "aaa": {"aaaa": 222, "bbb": 333}},
        "b": 4,
        "c": [8, 9],
        "d": [1],
    }
    target = {
        "a": {"aa": 11, "aaa": {"aaaa": 111}},
        "b": 5,
        "c": [1, 2, 3],
        "d": {"v": 1},
    }
    expected = {
        "a": {"aa": 11, "aaa": {"aaaa": 111, "bbb": 333}},
        "b": 5,
        "c": [1, 2, 3, 8, 9],
        "d": {"v": 1},
    }
    merge_and_test(source, target, expected)


def merge_and_test(source, target, expected):
    DictUtils.merge_dicts(source, target)
    assert target == expected


# FIXME: add test for times_tamep
# VALID_TIME_STAMP_REGEX=
EXPECTED_DATETIME = datetime(
    year=2022,
    month=1,
    day=12,
    hour=10,
    minute=44,
    second=23,
)
EXPECTED_TIMESTAMP = "20220112T104423000"


@pytest.mark.unit
@mock.patch("cdevents.cli.utils._utcnow")
def test_time_stamp(mock_utcnow):
    mock_utcnow.return_value = EXPECTED_DATETIME
    actual = time_stamp("T")
    assert actual == EXPECTED_TIMESTAMP
