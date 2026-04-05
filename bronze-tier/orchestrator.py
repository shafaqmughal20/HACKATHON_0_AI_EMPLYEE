#!/usr/bin/env python3
"""
Simple Orchestrator for Bronze-tier AI Employee
===============================================

A basic orchestrator that reads tasks from Needs_Action/, presents them to
Claude Code for execution, and moves completed tasks to Done/.

This is a MANUAL orchestrator - you run it when you want the AI to work on tasks.
It's intentionally simple for Bronze tier.

Usage:
    python orchestrator.py [vault_path]

Author: AI Employee System
Version: 1.0.0 (Bronze Tier)
Created: 2026-04-05
"""

import argparse
import sys
from datetime import datetime
from pathlib import Path
from typing import List, Optional


class BronzeOrchestrator:
    """
    Simple orchestrator for Bronze-tier AI Employee.

    Reads tasks from Needs_Action/, presents them to the user (Claude Code),
    and helps manage the workflow.
    """

    def __init__(self, vault_path: str | Path):
        """
        Initialize the orchestrator.

        Args:
            vault_path: Path to the AI Employee Vault
        """
        self.vault_path = Path(vault_path)

        # Validate vault exists
        if not self.vault_path.exists():
            raise FileNotFoundError(f"Vault not found: {vault_path}")

        # Setup folder paths
        self.needs_action = self.vault_path / "Needs_Action"
        self.done = self.vault_path / "Done"
        self.logs = self.vault_path / "Logs"
        self.dashboard = self.vault_path / "Dashboard.md"

        # Ensure folders exist
        self.needs_action.mkdir(exist_ok=True)
        self.done.mkdir(exist_ok=True)
        self.logs.mkdir(exist_ok=True)

    def get_pending_tasks(self) -> List[Path]:
        """
        Get all task files from Needs_Action folder.

        Returns:
            List of task file paths, sorted by priority and date
        """
        # Get all .md files except README
        tasks = [
            f for f in self.needs_action.glob("*.md")
            if f.name.upper() != "README.MD"
        ]

        # Sort by filename (date prefix ensures chronological order)
        tasks.sort()

        return tasks

    def read_task(self, task_path: Path) -> dict:
        """
        Read a task file and extract key information.

        Args:
            task_path: Path to the task file

        Returns:
            Dictionary with task information
        """
        try:
            content = task_path.read_text(encoding='utf-8')

            # Extract frontmatter
            frontmatter = {}
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    fm_lines = parts[1].strip().split('\n')
                    for line in fm_lines:
                        if ':' in line:
                            key, value = line.split(':', 1)
                            frontmatter[key.strip()] = value.strip()

            # Extract title (first # heading)
            title = "Untitled Task"
            for line in content.split('\n'):
                if line.startswith('# '):
                    title = line[2:].strip()
                    break

            return {
                'path': task_path,
                'filename': task_path.name,
                'title': title,
                'priority': frontmatter.get('priority', 'medium'),
                'status': frontmatter.get('status', 'pending'),
                'type': frontmatter.get('type', 'task'),
                'content': content,
                'frontmatter': frontmatter
            }

        except Exception as e:
            return {
                'path': task_path,
                'filename': task_path.name,
                'title': f"Error reading: {task_path.name}",
                'priority': 'unknown',
                'status': 'error',
                'error': str(e)
            }

    def display_task(self, task: dict, index: int, total: int) -> None:
        """
        Display a task in a readable format.

        Args:
            task: Task dictionary
            index: Current task number
            total: Total number of tasks
        """
        print(f"\n{'='*70}")
        print(f"📋 TASK {index}/{total}")
        print(f"{'='*70}")
        print(f"📄 File: {task['filename']}")
        print(f"📌 Title: {task['title']}")
        print(f"⚡ Priority: {task['priority'].upper()}")
        print(f"📊 Status: {task['status']}")
        print(f"🏷️  Type: {task['type']}")
        print(f"{'='*70}\n")

        # Display content preview (first 500 chars)
        if 'content' in task:
            preview = task['content'][:500]
            if len(task['content']) > 500:
                preview += "\n\n... (content truncated, see full file) ..."
            print(preview)
            print(f"\n{'='*70}")

    def present_next_task(self) -> Optional[dict]:
        """
        Present the next task to work on.

        Returns:
            Task dictionary or None if no tasks
        """
        tasks = self.get_pending_tasks()

        if not tasks:
            print("\n✅ No tasks in Needs_Action/ folder!")
            print("   All caught up! 🎉\n")
            return None

        # Get first task (highest priority, oldest first)
        task = self.read_task(tasks[0])

        # Display it
        self.display_task(task, 1, len(tasks))

        return task

    def mark_task_done(self, task_path: Path) -> bool:
        """
        Move a task from Needs_Action/ to Done/.

        Args:
            task_path: Path to the task file

        Returns:
            True if successful, False otherwise
        """
        try:
            # Read current content
            content = task_path.read_text(encoding='utf-8')

            # Update status in frontmatter
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    frontmatter = parts[1]

                    # Update or add status
                    if 'status:' in frontmatter:
                        frontmatter = frontmatter.replace(
                            'status: pending',
                            'status: done'
                        ).replace(
                            'status: in_progress',
                            'status: done'
                        )
                    else:
                        frontmatter += f"\nstatus: done"

                    # Add completion timestamp
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    if 'completed:' not in frontmatter:
                        frontmatter += f"\ncompleted: {timestamp}"

                    # Reconstruct content
                    content = f"---{frontmatter}---{parts[2]}"

            # Move to Done folder
            destination = self.done / task_path.name

            # Handle name conflicts
            counter = 1
            while destination.exists():
                stem = task_path.stem
                destination = self.done / f"{stem}_{counter}{task_path.suffix}"
                counter += 1

            # Write updated content to Done folder
            destination.write_text(content, encoding='utf-8')

            # Remove from Needs_Action
            task_path.unlink()

            print(f"\n✅ Task moved to Done/: {destination.name}")
            return True

        except Exception as e:
            print(f"\n❌ Error moving task: {e}")
            return False

    def log_activity(self, message: str) -> None:
        """
        Log activity to today's log file.

        Args:
            message: Message to log
        """
        try:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            date_str = datetime.now().strftime('%Y-%m-%d')
            log_file = self.logs / f"{date_str}_daily.md"

            # Append to log
            with open(log_file, 'a', encoding='utf-8') as f:
                f.write(f"- {timestamp} - {message}\n")

        except Exception as e:
            print(f"⚠️  Warning: Could not write to log: {e}")

    def show_summary(self) -> None:
        """
        Show a summary of the current state.
        """
        tasks = self.get_pending_tasks()
        done_files = list(self.done.glob("*.md"))
        done_count = len([f for f in done_files if f.name.upper() != "README.MD"])

        print("\n" + "="*70)
        print("📊 CURRENT STATUS SUMMARY")
        print("="*70)
        print(f"📋 Tasks in Needs_Action/: {len(tasks)}")
        print(f"✅ Tasks in Done/: {done_count}")

        if tasks:
            print(f"\n📌 Next task: {tasks[0].name}")

        print("="*70 + "\n")

    def run_interactive(self) -> None:
        """
        Run the orchestrator in interactive mode.

        Presents tasks one at a time and waits for user to complete them.
        """
        print("\n" + "="*70)
        print("🤖 Bronze-tier AI Employee Orchestrator")
        print("="*70)
        print("\nThis orchestrator helps you work through tasks in Needs_Action/")
        print("It will show you each task, and you can mark it done when complete.\n")

        while True:
            # Show summary
            self.show_summary()

            # Get next task
            task = self.present_next_task()

            if not task:
                break

            # Wait for user action
            print("\n" + "="*70)
            print("🎯 WHAT TO DO:")
            print("="*70)
            print("1. Read the task above")
            print("2. Execute the task (use Claude Code to help)")
            print("3. When done, come back here")
            print("="*70)

            print("\nOptions:")
            print("  [d] Mark as Done and move to Done/")
            print("  [s] Skip this task for now")
            print("  [v] View full task file")
            print("  [q] Quit orchestrator")

            choice = input("\nYour choice: ").strip().lower()

            if choice == 'd':
                if self.mark_task_done(task['path']):
                    self.log_activity(f"Completed task: {task['filename']}")
                    print("\n✅ Task marked as done!")
                    input("\nPress Enter to continue to next task...")

            elif choice == 's':
                print("\n⏭️  Skipping task for now...")
                input("\nPress Enter to continue...")

            elif choice == 'v':
                print("\n" + "="*70)
                print("📄 FULL TASK CONTENT")
                print("="*70)
                print(task.get('content', 'No content available'))
                print("="*70)
                input("\nPress Enter to continue...")

            elif choice == 'q':
                print("\n👋 Exiting orchestrator...")
                break

            else:
                print("\n❌ Invalid choice. Please try again.")
                input("\nPress Enter to continue...")

        print("\n✅ Orchestrator session complete!")
        self.show_summary()


def main():
    """
    Main entry point for the orchestrator.
    """
    parser = argparse.ArgumentParser(
        description='Simple orchestrator for Bronze-tier AI Employee'
    )
    parser.add_argument(
        'vault_path',
        nargs='?',
        default='AI_Employee_Vault',
        help='Path to AI Employee Vault (default: AI_Employee_Vault)'
    )

    args = parser.parse_args()

    try:
        # Create orchestrator
        orchestrator = BronzeOrchestrator(args.vault_path)

        # Run interactive mode
        orchestrator.run_interactive()

    except FileNotFoundError as e:
        print(f"\n❌ Error: {e}")
        print(f"Please ensure the vault exists at: {args.vault_path}")
        return 1

    except KeyboardInterrupt:
        print("\n\n👋 Orchestrator interrupted by user")
        return 0

    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
