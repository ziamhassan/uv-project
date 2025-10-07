import typer
import json
from pathlib import Path

app = typer.Typer()

TASKS_FILE = Path("tasks.json")


def load_tasks():
    if TASKS_FILE.exists():
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


@app.command()
def add(description: str):
    """Add a new task"""
    tasks = load_tasks()
    task = {"id": len(tasks) + 1, "description": description, "done": False}
    tasks.append(task)
    save_tasks(tasks)
    typer.echo(f"✅ Task added: {description}")


@app.command()
def list():
    """List all tasks"""
    tasks = load_tasks()
    if not tasks:
        typer.echo("📭 No tasks found.")
        return
    for task in tasks:
        status = "✅" if task["done"] else "❌"
        typer.echo(f"{task['id']}. {task['description']} [{status}]")


@app.command()
def done(task_id: int):
    """Mark a task as done"""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks)
            typer.echo(f"🎉 Task {task_id} marked as done!")
            return
    typer.echo(f"⚠️ Task {task_id} not found.")


if __name__ == "__main__":
    app()
