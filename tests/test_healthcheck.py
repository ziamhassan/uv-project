from src.main import app

def test_healthcheck(runner):
    result = runner.invoke(app, ["healthcheck"])
    assert result.exit_code == 0
    assert "healthy" in result.output
