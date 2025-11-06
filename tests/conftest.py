import pytest
from typer.testing import CliRunner
from src.main import app

@pytest.fixture
def runner():
    """Fixture that provides a Typer test runner"""
    return CliRunner()
