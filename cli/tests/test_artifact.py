"""Unit tests for artifact."""
from unittest.mock import patch

import pytest
from cdevents.cli.artifact import packaged, published
from cdevents.cli.cdevents_command import CDeventsCommand
from click.testing import CliRunner

# pylint: disable=missing-function-docstring, protected-access, missing-class-docstring


@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()


ID_ARG = "id"
NAME_ARG = "name"
VERSION_ARG = "version"
DATA_ARG = "data"


@pytest.mark.unit
def test_packaged(runner: CliRunner):
    """Test packaging of an artifact."""

    expected_id = "task1"
    expected_name = "My Task Run"
    expected_version = "MyArtifact"
    expected_data = ["key1", "value1"]

    with patch.object(CDeventsCommand, "run", spec=CDeventsCommand):
        result = runner.invoke(
            packaged,
            [
                f"--{ID_ARG}",
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
    assert f"{ID_ARG}={expected_id}" in result.stdout
    assert f"{NAME_ARG}={expected_name}" in result.stdout
    assert f"{VERSION_ARG}={expected_version}" in result.stdout
    assert f"{DATA_ARG}=({tuple(expected_data)},)" in result.stdout


@pytest.mark.unit
def test_published(runner: CliRunner):
    """Test published of an artifact."""

    expected_id = "task1"
    expected_name = "My Task Run"
    expected_version = "MyArtifact"
    expected_data = ["key1", "value1"]

    with patch.object(CDeventsCommand, "run", spec=CDeventsCommand):
        result = runner.invoke(
            published,
            [
                f"--{ID_ARG}",
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
    assert f"{ID_ARG}={expected_id}" in result.stdout
    assert f"{NAME_ARG}={expected_name}" in result.stdout
    assert f"{VERSION_ARG}={expected_version}" in result.stdout
    assert f"{DATA_ARG}=({tuple(expected_data)},)" in result.stdout
