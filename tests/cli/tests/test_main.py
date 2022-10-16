import pytest
from cdevents.cli.__main__ import cli
from click.testing import CliRunner


@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()


@pytest.mark.unit
def test_cli_main(runner: CliRunner):

    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
