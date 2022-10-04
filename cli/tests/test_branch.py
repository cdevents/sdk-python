"""Unit tests for branch."""
from unittest.mock import patch

import pytest
from cdevents.cli.branch import created, deleted
from cdevents.cli.cdevents_command import CDeventsCommand
from click.testing import CliRunner

# pylint: disable=missing-function-docstring, protected-access, missing-class-docstring


@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()


ID_ARG = "id"
NAME_ARG = "name"
REPOID_ARG = "repoid"
DATA_ARG = "data"


@pytest.mark.unit
def test_created(runner: CliRunner):
    """Test created of a branch."""

    expected_id = "task1"
    expected_name = "My Task Run"
    expected_repoid = "repo1"
    expected_data = ["key1", "value1"]

    with patch.object(CDeventsCommand, "run", spec=CDeventsCommand):
        result = runner.invoke(
            created,
            [
                f"--{ID_ARG}",
                expected_id,
                f"--{NAME_ARG}",
                expected_name,
                f"--{REPOID_ARG}",
                expected_repoid,
                f"--{DATA_ARG}",
                *expected_data,
            ],
        )
    assert result.exit_code == 0
    assert f"{ID_ARG}={expected_id}" in result.stdout
    assert f"{NAME_ARG}={expected_name}" in result.stdout
    assert f"{REPOID_ARG}={expected_repoid}" in result.stdout
    assert f"{DATA_ARG}=({tuple(expected_data)},)" in result.stdout


@pytest.mark.unit
def test_deleted(runner: CliRunner):
    """Test deleted of a branch."""

    expected_id = "task1"
    expected_name = "My Task Run"
    expected_repoid = "repo1"
    expected_data = ["key1", "value1"]

    with patch.object(CDeventsCommand, "run", spec=CDeventsCommand):
        result = runner.invoke(
            deleted,
            [
                f"--{ID_ARG}",
                expected_id,
                f"--{NAME_ARG}",
                expected_name,
                f"--{REPOID_ARG}",
                expected_repoid,
                f"--{DATA_ARG}",
                *expected_data,
            ],
        )
    assert result.exit_code == 0
    assert f"{ID_ARG}={expected_id}" in result.stdout
    assert f"{NAME_ARG}={expected_name}" in result.stdout
    assert f"{REPOID_ARG}={expected_repoid}" in result.stdout
    assert f"{DATA_ARG}=({tuple(expected_data)},)" in result.stdout
