import typer
from src.main import add_task, list_tasks, mark_done

app = typer.Typer(help="Task Manager CLI - Manage your tasks easily")

@app.command()
def add(description: str):
    """Add a new task"""
    add_task(description)
    typer.echo(f"✅ Task added: {description}")

@app.command()
def list():
    """List all tasks"""
    list_tasks()

@app.command()
def done(id: int):
    """Mark a task as done"""
    mark_done(id)
    typer.echo(f"🎯 Task #{id} marked as done!")

if __name__ == "__main__":
    app()
@app.command()
def healthcheck():
    """Simple command to check if the CLI works"""
    typer.echo("✅ CLI is healthy and ready!")

if __name__ == "__main__":
    app()