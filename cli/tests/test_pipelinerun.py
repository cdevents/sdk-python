"""Unit tests for pipelinerun."""
from unittest.mock import patch

import pytest
from cdevents.cli.cdevents_command import CDeventsCommand
from cdevents.cli.pipelinerun import finished, queued, started
from click.testing import CliRunner


# pylint: disable=missing-function-docstring, protected-access, missing-class-docstring
@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()


ID_ARG = "id"
NAME_ARG = "name"
STATUS_ARG = "status"
URL_ARG = "url"
ERRORS_ARG = "errors"
DATA_ARG = "data"


@pytest.mark.unit
def test_started(runner: CliRunner):
    """Test started of an env."""

    expected_id = "task1"
    expected_name = "My Task Run"
    expected_status = "success"
    expected_url = "https://my-url.com"
    expected_errors = "my-errors"
    expected_data = ["key1", "value1"]

    with patch.object(CDeventsCommand, "run", spec=CDeventsCommand):
        result = runner.invoke(
            started,
            [
                f"--{ID_ARG}",
                expected_id,
                f"--{NAME_ARG}",
                expected_name,
                f"--{STATUS_ARG}",
                expected_status,
                f"--{URL_ARG}",
                expected_url,
                f"--{ERRORS_ARG}",
                expected_errors,
                f"--{DATA_ARG}",
                *expected_data,
            ],
        )
    assert result.exit_code == 0
    assert f"{ID_ARG}={expected_id}" in result.stdout
    assert f"{NAME_ARG}={expected_name}" in result.stdout
    assert f"{STATUS_ARG}={expected_status}" in result.stdout
    assert f"{URL_ARG}={expected_url}" in result.stdout
    assert f"{ERRORS_ARG}={expected_errors}" in result.stdout
    assert f"{DATA_ARG}=({tuple(expected_data)},)" in result.stdout


@pytest.mark.unit
def test_finished(runner: CliRunner):
    """Test finished of an env."""

    expected_id = "task1"
    expected_name = "My Task Run"
    expected_status = "success"
    expected_url = "https://my-url.com"
    expected_errors = "my-errors"
    expected_data = ["key1", "value1"]

    with patch.object(CDeventsCommand, "run", spec=CDeventsCommand):
        result = runner.invoke(
            finished,
            [
                f"--{ID_ARG}",
                expected_id,
                f"--{NAME_ARG}",
                expected_name,
                f"--{STATUS_ARG}",
                expected_status,
                f"--{URL_ARG}",
                expected_url,
                f"--{ERRORS_ARG}",
                expected_errors,
                f"--{DATA_ARG}",
                *expected_data,
            ],
        )
    assert result.exit_code == 0
    assert f"{ID_ARG}={expected_id}" in result.stdout
    assert f"{NAME_ARG}={expected_name}" in result.stdout
    assert f"{STATUS_ARG}={expected_status}" in result.stdout
    assert f"{URL_ARG}={expected_url}" in result.stdout
    assert f"{ERRORS_ARG}={expected_errors}" in result.stdout
    assert f"{DATA_ARG}=({tuple(expected_data)},)" in result.stdout


@pytest.mark.unit
def test_queued(runner: CliRunner):
    """Test queued of an env."""

    expected_id = "task1"
    expected_name = "My Task Run"
    expected_status = "success"
    expected_url = "https://my-url.com"
    expected_errors = "my-errors"
    expected_data = ["key1", "value1"]

    with patch.object(CDeventsCommand, "run", spec=CDeventsCommand):
        result = runner.invoke(
            queued,
            [
                f"--{ID_ARG}",
                expected_id,
                f"--{NAME_ARG}",
                expected_name,
                f"--{STATUS_ARG}",
                expected_status,
                f"--{URL_ARG}",
                expected_url,
                f"--{ERRORS_ARG}",
                expected_errors,
                f"--{DATA_ARG}",
                *expected_data,
            ],
        )
    assert result.exit_code == 0
    assert f"{ID_ARG}={expected_id}" in result.stdout
    assert f"{NAME_ARG}={expected_name}" in result.stdout
    assert f"{STATUS_ARG}={expected_status}" in result.stdout
    assert f"{URL_ARG}={expected_url}" in result.stdout
    assert f"{ERRORS_ARG}={expected_errors}" in result.stdout
    assert f"{DATA_ARG}=({tuple(expected_data)},)" in result.stdout
