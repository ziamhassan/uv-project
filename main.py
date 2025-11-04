import argparse
from main import add_task, list_tasks, mark_done

def main():
    parser = argparse.ArgumentParser(
        description="Task Manager CLI - Manage your tasks easily"
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add Task
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("description", type=str, help="Task description")

    # List Tasks
    subparsers.add_parser("list", help="List all tasks")

    # Mark Done
    parser_done = subparsers.add_parser("done", help="Mark a task as done")
    parser_done.add_argument("id", type=int, help="Task ID")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description)
    elif args.command == "list":
        list_tasks()
    elif args.command == "done":
        mark_done(args.id)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
