"""Unit tests for build."""
import pytest
from unittest.mock import patch
from click.testing import CliRunner

from cdevents.cli.build import started, finished, queued
from cdevents.cli.cdevents_command import CDeventsCommand

# pylint: disable=missing-function-docstring, protected-access, missing-class-docstring
@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()


ID_ARG = "id"
NAME_ARG = "name"
ARTIFACT_ARG = "artifact"
DATA_ARG = "data"

@pytest.mark.unit
def test_started(runner: CliRunner):
    """Test started of a build."""

    expected_id = "task1"
    expected_name = "My Task Run"
    expected_artifact = "artifact1"
    expected_data = ["key1", "value1"]

    with patch.object(CDeventsCommand, "run", spec=CDeventsCommand): 
        result = runner.invoke(
            started,
            [
                f"--{ID_ARG}",
                expected_id,
                f"--{NAME_ARG}",
                expected_name,
                f"--{ARTIFACT_ARG}",
                expected_artifact,
                f"--{DATA_ARG}",
                *expected_data,
            ],
        )
    assert result.exit_code == 0
    assert f"{ID_ARG}={expected_id}" in result.stdout
    assert f"{NAME_ARG}={expected_name}" in result.stdout
    assert f"{ARTIFACT_ARG}={expected_artifact}" in result.stdout
    assert f"{DATA_ARG}=({tuple(expected_data)},)" in result.stdout


@pytest.mark.unit
def test_finished(runner: CliRunner):
    """Test finished of a build."""

    expected_id = "task1"
    expected_name = "My Task Run"
    expected_artifact = "artifact1"
    expected_data = ["key1", "value1"]

    with patch.object(CDeventsCommand, "run", spec=CDeventsCommand): 
        result = runner.invoke(
            finished,
            [
                f"--{ID_ARG}",
                expected_id,
                f"--{NAME_ARG}",
                expected_name,
                f"--{ARTIFACT_ARG}",
                expected_artifact,
                f"--{DATA_ARG}",
                *expected_data,
            ],
        )
    assert result.exit_code == 0
    assert f"{ID_ARG}={expected_id}" in result.stdout
    assert f"{NAME_ARG}={expected_name}" in result.stdout
    assert f"{ARTIFACT_ARG}={expected_artifact}" in result.stdout
    assert f"{DATA_ARG}=({tuple(expected_data)},)" in result.stdout


@pytest.mark.unit
def test_queued(runner: CliRunner):
    """Test queued of a build."""

    expected_id = "task1"
    expected_name = "My Task Run"
    expected_artifact = "artifact1"
    expected_data = ["key1", "value1"]

    with patch.object(CDeventsCommand, "run", spec=CDeventsCommand): 
        result = runner.invoke(
            queued,
            [
                f"--{ID_ARG}",
                expected_id,
                f"--{NAME_ARG}",
                expected_name,
                f"--{ARTIFACT_ARG}",
                expected_artifact,
                f"--{DATA_ARG}",
                *expected_data,
            ],
        )
    assert result.exit_code == 0
    assert f"{ID_ARG}={expected_id}" in result.stdout
    assert f"{NAME_ARG}={expected_name}" in result.stdout
    assert f"{ARTIFACT_ARG}={expected_artifact}" in result.stdout
    assert f"{DATA_ARG}=({tuple(expected_data)},)" in result.stdout

