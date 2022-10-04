"""Unit tests for service."""
from unittest.mock import patch

import pytest
from cdevents.cli.cdevents_command import CDeventsCommand
from cdevents.cli.service import deployed, removed, rolledback, upgraded
from click.testing import CliRunner


# pylint: disable=missing-function-docstring, protected-access, missing-class-docstring
@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()


ENVID_ARG = "envid"
NAME_ARG = "name"
VERSION_ARG = "version"
DATA_ARG = "data"


@pytest.mark.unit
def test_deployed(runner: CliRunner):
    """Test deployed of an service."""

    expected_id = "task1"
    expected_name = "My Task Run"
    expected_version = "1.0.0"
    expected_data = ["key1", "value1"]

    with patch.object(CDeventsCommand, "run", spec=CDeventsCommand):
        result = runner.invoke(
            deployed,
            [
                f"--{ENVID_ARG}",
                expected_id,
                f"--{NAME_ARG}",
                expected_name,
                f"--{VERSION_ARG}",
                expected_version,
                f"--{DATA_ARG}",
                *expected_data,
            ],
        )
    assert result.exit_code == 0
    assert f"{ENVID_ARG}={expected_id}" in result.stdout
    assert f"{NAME_ARG}={expected_name}" in result.stdout
    assert f"{VERSION_ARG}={expected_version}" in result.stdout
    assert f"{DATA_ARG}=({tuple(expected_data)},)" in result.stdout


@pytest.mark.unit
def test_upgraded(runner: CliRunner):
    """Test upgraded of an service."""

    expected_id = "task1"
    expected_name = "My Task Run"
    expected_version = "1.0.0"
    expected_data = ["key1", "value1"]

    with patch.object(CDeventsCommand, "run", spec=CDeventsCommand):
        result = runner.invoke(
            upgraded,
            [
                f"--{ENVID_ARG}",
                expected_id,
                f"--{NAME_ARG}",
                expected_name,
                f"--{VERSION_ARG}",
                expected_version,
                f"--{DATA_ARG}",
                *expected_data,
            ],
        )
    assert result.exit_code == 0
    assert f"{ENVID_ARG}={expected_id}" in result.stdout
    assert f"{NAME_ARG}={expected_name}" in result.stdout
    assert f"{VERSION_ARG}={expected_version}" in result.stdout
    assert f"{DATA_ARG}=({tuple(expected_data)},)" in result.stdout


@pytest.mark.unit
def test_removed(runner: CliRunner):
    """Test removed of an service."""

    expected_id = "task1"
    expected_name = "My Task Run"
    expected_version = "1.0.0"
    expected_data = ["key1", "value1"]

    with patch.object(CDeventsCommand, "run", spec=CDeventsCommand):
        result = runner.invoke(
            removed,
            [
                f"--{ENVID_ARG}",
                expected_id,
                f"--{NAME_ARG}",
                expected_name,
                f"--{VERSION_ARG}",
                expected_version,
                f"--{DATA_ARG}",
                *expected_data,
            ],
        )
    assert result.exit_code == 0
    assert f"{ENVID_ARG}={expected_id}" in result.stdout
    assert f"{NAME_ARG}={expected_name}" in result.stdout
    assert f"{VERSION_ARG}={expected_version}" in result.stdout
    assert f"{DATA_ARG}=({tuple(expected_data)},)" in result.stdout


@pytest.mark.unit
def test_rolledback(runner: CliRunner):
    """Test rolledback of an service."""

    expected_id = "task1"
    expected_name = "My Task Run"
    expected_version = "1.0.0"
    expected_data = ["key1", "value1"]

    with patch.object(CDeventsCommand, "run", spec=CDeventsCommand):
        result = runner.invoke(
            rolledback,
            [
                f"--{ENVID_ARG}",
                expected_id,
                f"--{NAME_ARG}",
                expected_name,
                f"--{VERSION_ARG}",
                expected_version,
                f"--{DATA_ARG}",
                *expected_data,
            ],
        )
    assert result.exit_code == 0
    assert f"{ENVID_ARG}={expected_id}" in result.stdout
    assert f"{NAME_ARG}={expected_name}" in result.stdout
    assert f"{VERSION_ARG}={expected_version}" in result.stdout
    assert f"{DATA_ARG}=({tuple(expected_data)},)" in result.stdout
