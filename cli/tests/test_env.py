"""Unit tests for env."""
import pytest
from unittest.mock import patch
from click.testing import CliRunner

from cdevents.cli.env import created, deleted, modified
from cdevents.cli.cdevents_command import CDeventsCommand

# pylint: disable=missing-function-docstring, protected-access, missing-class-docstring
@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()


ID_ARG = "id"
NAME_ARG = "name"
REPO_ARG = "repo"
DATA_ARG = "data"

@pytest.mark.unit
def test_started(runner: CliRunner):
    """Test started of an env."""

    expected_id = "task1"
    expected_name = "My Task Run"
    expected_repo = "my-repo"
    expected_data = ["key1", "value1"]

    with patch.object(CDeventsCommand, "run", spec=CDeventsCommand): 
        result = runner.invoke(
            created,
            [
                f"--{ID_ARG}",
                expected_id,
                f"--{NAME_ARG}",
                expected_name,
                f"--{REPO_ARG}",
                expected_repo,
                f"--{DATA_ARG}",
                *expected_data,
            ],
        )
    assert result.exit_code == 0
    assert f"{ID_ARG}={expected_id}" in result.stdout
    assert f"{NAME_ARG}={expected_name}" in result.stdout
    assert f"{REPO_ARG}={expected_repo}" in result.stdout
    assert f"{DATA_ARG}=({tuple(expected_data)},)" in result.stdout


@pytest.mark.unit
def test_started(runner: CliRunner):
    """Test started of an env."""

    expected_id = "task1"
    expected_name = "My Task Run"
    expected_repo = "my-repo"
    expected_data = ["key1", "value1"]

    with patch.object(CDeventsCommand, "run", spec=CDeventsCommand): 
        result = runner.invoke(
            deleted,
            [
                f"--{ID_ARG}",
                expected_id,
                f"--{NAME_ARG}",
                expected_name,
                f"--{REPO_ARG}",
                expected_repo,
                f"--{DATA_ARG}",
                *expected_data,
            ],
        )
    assert result.exit_code == 0
    assert f"{ID_ARG}={expected_id}" in result.stdout
    assert f"{NAME_ARG}={expected_name}" in result.stdout
    assert f"{REPO_ARG}={expected_repo}" in result.stdout
    assert f"{DATA_ARG}=({tuple(expected_data)},)" in result.stdout


@pytest.mark.unit
def test_started(runner: CliRunner):
    """Test started of an env."""

    expected_id = "task1"
    expected_name = "My Task Run"
    expected_repo = "my-repo"
    expected_data = ["key1", "value1"]

    with patch.object(CDeventsCommand, "run", spec=CDeventsCommand): 
        result = runner.invoke(
            modified,
            [
                f"--{ID_ARG}",
                expected_id,
                f"--{NAME_ARG}",
                expected_name,
                f"--{REPO_ARG}",
                expected_repo,
                f"--{DATA_ARG}",
                *expected_data,
            ],
        )
    assert result.exit_code == 0
    assert f"{ID_ARG}={expected_id}" in result.stdout
    assert f"{NAME_ARG}={expected_name}" in result.stdout
    assert f"{REPO_ARG}={expected_repo}" in result.stdout
    assert f"{DATA_ARG}=({tuple(expected_data)},)" in result.stdout

