#!/usr/bin/env python3
"""
Base Watcher for Bronze-tier AI Employee
=========================================

Abstract base class for file system watchers that monitor folders and trigger
AI actions. Designed for reliability and simplicity.

Usage:
    Inherit from BaseWatcher and implement:
    - check_for_updates(): Detect changes in monitored folders
    - create_action_file(): Generate action files for AI to process

Author: AI Employee System
Version: 1.0.0 (Bronze Tier)
Created: 2026-04-05
"""

import logging
import time
from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path
from typing import Optional


class BaseWatcher(ABC):
    """
    Abstract base class for file system watchers.

    Provides core functionality for monitoring directories and triggering
    AI employee actions through file-based communication.

    Attributes:
        vault_path (Path): Root path to AI Employee Vault
        check_interval (int): Seconds between checks (default: 30)
        logger (logging.Logger): Logger instance for this watcher
        is_running (bool): Flag to control the main loop
    """

    def __init__(
        self,
        vault_path: str | Path,
        check_interval: int = 30,
        log_level: int = logging.INFO
    ):
        """
        Initialize the base watcher.

        Args:
            vault_path: Path to the AI Employee Vault root directory
            check_interval: Seconds between folder checks (default: 30)
            log_level: Logging level (default: INFO)

        Raises:
            FileNotFoundError: If vault_path doesn't exist
            ValueError: If check_interval is less than 1
        """
        # Validate inputs
        self.vault_path = Path(vault_path)
        if not self.vault_path.exists():
            raise FileNotFoundError(f"Vault path does not exist: {vault_path}")

        if check_interval < 1:
            raise ValueError("check_interval must be at least 1 second")

        self.check_interval = check_interval
        self.is_running = False

        # Setup logging
        self.logger = self._setup_logging(log_level)

        # Log initialization
        self.logger.info(f"Initialized {self.__class__.__name__}")
        self.logger.info(f"Vault path: {self.vault_path}")
        self.logger.info(f"Check interval: {self.check_interval}s")

    def _setup_logging(self, log_level: int) -> logging.Logger:
        """
        Configure logging for this watcher.

        Args:
            log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)

        Returns:
            Configured logger instance
        """
        logger = logging.getLogger(self.__class__.__name__)
        logger.setLevel(log_level)

        # Avoid duplicate handlers
        if not logger.handlers:
            # Console handler
            console_handler = logging.StreamHandler()
            console_handler.setLevel(log_level)

            # Format: timestamp - name - level - message
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)

            # File handler (logs to vault)
            log_dir = self.vault_path / "Logs"
            log_dir.mkdir(exist_ok=True)

            log_file = log_dir / f"watcher_{datetime.now().strftime('%Y-%m-%d')}.log"
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(log_level)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger

    @abstractmethod
    def check_for_updates(self) -> bool:
        """
        Check monitored folders for changes that require AI action.

        This method should:
        1. Scan relevant folders (Inbox, Needs_Action, etc.)
        2. Detect new files, changes, or conditions requiring action
        3. Return True if action is needed, False otherwise

        Returns:
            bool: True if updates detected, False otherwise

        Example implementation:
            def check_for_updates(self) -> bool:
                inbox = self.vault_path / "Inbox"
                files = list(inbox.glob("*.md"))
                return len(files) > 0
        """
        pass

    @abstractmethod
    def create_action_file(self) -> Optional[Path]:
        """
        Create an action file for the AI employee to process.

        This method should:
        1. Gather information about what needs to be done
        2. Create a properly formatted task file
        3. Place it in the appropriate folder (usually Needs_Action)
        4. Return the path to the created file

        Returns:
            Optional[Path]: Path to created action file, or None if creation failed

        Example implementation:
            def create_action_file(self) -> Optional[Path]:
                action_file = self.vault_path / "Needs_Action" / "task.md"
                action_file.write_text("# Task\\n\\nProcess inbox items")
                return action_file
        """
        pass

    def run(self) -> None:
        """
        Main execution loop for the watcher.

        Continuously monitors for updates at the specified interval.
        Handles errors gracefully and logs all activity.

        Loop behavior:
        1. Check for updates
        2. If updates found, create action file
        3. Sleep for check_interval seconds
        4. Repeat until stopped

        Can be stopped by setting self.is_running = False or KeyboardInterrupt.
        """
        self.is_running = True
        self.logger.info(f"Starting watcher loop (interval: {self.check_interval}s)")
        self.logger.info("Press Ctrl+C to stop")

        try:
            while self.is_running:
                try:
                    # Check for updates
                    self.logger.debug("Checking for updates...")
                    has_updates = self.check_for_updates()

                    if has_updates:
                        self.logger.info("Updates detected - creating action file")

                        # Create action file
                        action_file = self.create_action_file()

                        if action_file:
                            self.logger.info(f"Action file created: {action_file}")
                        else:
                            self.logger.warning("Failed to create action file")
                    else:
                        self.logger.debug("No updates detected")

                except Exception as e:
                    # Log error but continue running
                    self.logger.error(f"Error in check cycle: {e}", exc_info=True)
                    self.logger.info("Continuing despite error...")

                # Sleep until next check
                self.logger.debug(f"Sleeping for {self.check_interval}s")
                time.sleep(self.check_interval)

        except KeyboardInterrupt:
            self.logger.info("Received stop signal (Ctrl+C)")

        except Exception as e:
            # Fatal error - log and exit
            self.logger.critical(f"Fatal error in main loop: {e}", exc_info=True)
            raise

        finally:
            self.is_running = False
            self.logger.info("Watcher stopped")

    def stop(self) -> None:
        """
        Gracefully stop the watcher loop.

        Sets the is_running flag to False, which will cause the run() loop
        to exit after the current check cycle completes.
        """
        self.logger.info("Stop requested")
        self.is_running = False

    def get_folder_path(self, folder_name: str) -> Path:
        """
        Get the full path to a vault folder.

        Args:
            folder_name: Name of the folder (e.g., "Inbox", "Needs_Action")

        Returns:
            Path: Full path to the folder

        Example:
            inbox_path = self.get_folder_path("Inbox")
        """
        return self.vault_path / folder_name

    def ensure_folder_exists(self, folder_name: str) -> Path:
        """
        Ensure a vault folder exists, creating it if necessary.

        Args:
            folder_name: Name of the folder to check/create

        Returns:
            Path: Full path to the folder
        """
        folder_path = self.get_folder_path(folder_name)
        folder_path.mkdir(parents=True, exist_ok=True)
        return folder_path

    def get_timestamp(self) -> str:
        """
        Get current timestamp in standard format.

        Returns:
            str: Timestamp in YYYY-MM-DD HH:MM:SS format
        """
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_date_prefix(self) -> str:
        """
        Get current date prefix for file naming.

        Returns:
            str: Date in YYYY-MM-DD format
        """
        return datetime.now().strftime("%Y-%m-%d")


# Example implementation for reference
class ExampleWatcher(BaseWatcher):
    """
    Example implementation of BaseWatcher.

    Monitors the Inbox folder and creates action files when new tasks appear.
    This serves as a reference implementation for Bronze-tier watchers.
    """

    def check_for_updates(self) -> bool:
        """Check if there are any .md files in the Inbox folder."""
        inbox = self.get_folder_path("Inbox")

        # Skip README files
        task_files = [
            f for f in inbox.glob("*.md")
            if f.name.lower() != "readme.md"
        ]

        if task_files:
            self.logger.info(f"Found {len(task_files)} task(s) in Inbox")
            return True

        return False

    def create_action_file(self) -> Optional[Path]:
        """Create an action file to process inbox items."""
        try:
            # Create action file in Needs_Action
            action_file = self.get_folder_path("Needs_Action") / \
                         f"{self.get_date_prefix()}_ProcessInbox.md"

            # Write action content
            content = f"""---
type: task
created: {self.get_date_prefix()}
priority: high
status: pending
assigned_to: ai
---

# Process Inbox Items

## Description
New tasks detected in Inbox folder. Process and route to appropriate folders.

## Success Criteria
- All inbox items reviewed
- Tasks routed to correct folders
- Dashboard updated
- Log entries created

## Timestamp
Created: {self.get_timestamp()}
"""

            action_file.write_text(content)
            return action_file

        except Exception as e:
            self.logger.error(f"Failed to create action file: {e}")
            return None


if __name__ == "__main__":
    """
    Example usage and testing.

    Run this file directly to test the ExampleWatcher implementation.
    """
    import sys

    # Setup basic logging for demo
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Get vault path from command line or use default
    if len(sys.argv) > 1:
        vault_path = sys.argv[1]
    else:
        vault_path = Path(__file__).parent / "AI_Employee_Vault"

    print(f"Starting ExampleWatcher for vault: {vault_path}")
    print("Press Ctrl+C to stop\n")

    try:
        # Create and run the example watcher
        watcher = ExampleWatcher(
            vault_path=vault_path,
            check_interval=30,
            log_level=logging.INFO
        )
        watcher.run()

    except FileNotFoundError as e:
        print(f"Error: {e}")
        print(f"Please ensure the vault exists at: {vault_path}")
        sys.exit(1)

    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)
