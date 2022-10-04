"""Unit tests for taskrun."""
from unittest.mock import patch

import pytest
from cdevents.cli.cdevents_command import CDeventsCommand
from cdevents.cli.taskrun import finished, started
from click.testing import CliRunner


# pylint: disable=missing-function-docstring, protected-access, missing-class-docstring
@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()


ID_ARG = "id"
NAME_ARG = "name"
PIPLINEID_ARG = "pipelineid"
DATA_ARG = "data"


@pytest.mark.unit
def test_started(runner: CliRunner):
    """Test started of an taskrun."""

    expected_id = "task1"
    expected_name = "My Task Run"
    expected_pipelineid = "pipeline1"
    expected_data = ["key1", "value1"]

    with patch.object(CDeventsCommand, "run", spec=CDeventsCommand):
        result = runner.invoke(
            started,
            [
                f"--{ID_ARG}",
                expected_id,
                f"--{NAME_ARG}",
                expected_name,
                f"--{PIPLINEID_ARG}",
                expected_pipelineid,
                f"--{DATA_ARG}",
                *expected_data,
            ],
        )
    assert result.exit_code == 0
    assert f"{ID_ARG}={expected_id}" in result.stdout
    assert f"{NAME_ARG}={expected_name}" in result.stdout
    assert f"{PIPLINEID_ARG}={expected_pipelineid}" in result.stdout
    assert f"{DATA_ARG}=({tuple(expected_data)},)" in result.stdout


@pytest.mark.unit
def test_finished(runner: CliRunner):
    """Test finished of an taskrun."""

    expected_id = "task1"
    expected_name = "My Task Run"
    expected_pipelineid = "pipeline1"
    expected_data = ["key1", "value1"]

    with patch.object(CDeventsCommand, "run", spec=CDeventsCommand):
        result = runner.invoke(
            finished,
            [
                f"--{ID_ARG}",
                expected_id,
                f"--{NAME_ARG}",
                expected_name,
                f"--{PIPLINEID_ARG}",
                expected_pipelineid,
                f"--{DATA_ARG}",
                *expected_data,
            ],
        )
    assert result.exit_code == 0
    assert f"{ID_ARG}={expected_id}" in result.stdout
    assert f"{NAME_ARG}={expected_name}" in result.stdout
    assert f"{PIPLINEID_ARG}={expected_pipelineid}" in result.stdout
    assert f"{DATA_ARG}=({tuple(expected_data)},)" in result.stdout
