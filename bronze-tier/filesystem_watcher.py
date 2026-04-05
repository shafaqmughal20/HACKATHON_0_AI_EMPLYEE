#!/usr/bin/env python3
"""
Filesystem Watcher for Bronze-tier AI Employee
==============================================

Monitors the Inbox folder for new files and creates action tasks for the AI
employee to process. Handles any file type dropped into the inbox.

Features:
- Monitors Inbox/ folder for new files
- Copies files to Needs_Action/ for processing
- Creates rich metadata action files
- Tracks processed files to avoid duplicates
- Robust error handling

Usage:
    python filesystem_watcher.py [vault_path] [--interval SECONDS]

Author: AI Employee System
Version: 1.0.0 (Bronze Tier)
Created: 2026-04-05
"""

import argparse
import hashlib
import logging
import shutil
from datetime import datetime
from pathlib import Path
from typing import Optional, Set

from base_watcher import BaseWatcher


class FilesystemWatcher(BaseWatcher):
    """
    Watches the Inbox folder for new files and creates processing tasks.

    Monitors for any file type (documents, images, data files, etc.) and
    automatically creates action files for the AI employee to handle them.

    Attributes:
        processed_files (Set[str]): Set of file hashes already processed
        inbox_folder (Path): Path to the Inbox folder being monitored
        needs_action_folder (Path): Path to Needs_Action folder for tasks
    """

    def __init__(
        self,
        vault_path: str | Path,
        check_interval: int = 30,
        log_level: int = logging.INFO
    ):
        """
        Initialize the filesystem watcher.

        Args:
            vault_path: Path to the AI Employee Vault root directory
            check_interval: Seconds between folder checks (default: 30)
            log_level: Logging level (default: INFO)
        """
        super().__init__(vault_path, check_interval, log_level)

        # Setup folder paths
        self.inbox_folder = self.ensure_folder_exists("Inbox")
        self.needs_action_folder = self.ensure_folder_exists("Needs_Action")

        # Track processed files to avoid duplicates
        self.processed_files: Set[str] = set()

        self.logger.info("FilesystemWatcher initialized")
        self.logger.info(f"Monitoring: {self.inbox_folder}")

    def _get_file_hash(self, file_path: Path) -> str:
        """
        Calculate SHA256 hash of a file for duplicate detection.

        Args:
            file_path: Path to the file

        Returns:
            str: Hexadecimal hash string
        """
        sha256_hash = hashlib.sha256()

        try:
            with open(file_path, "rb") as f:
                # Read in chunks for memory efficiency
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)

            return sha256_hash.hexdigest()

        except Exception as e:
            self.logger.error(f"Failed to hash file {file_path}: {e}")
            # Fallback to filename + size + mtime
            stat = file_path.stat()
            return f"{file_path.name}_{stat.st_size}_{stat.st_mtime}"

    def _get_file_size_human(self, size_bytes: int) -> str:
        """
        Convert file size to human-readable format.

        Args:
            size_bytes: File size in bytes

        Returns:
            str: Human-readable size (e.g., "1.5 MB")
        """
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.1f} PB"

    def _should_process_file(self, file_path: Path) -> bool:
        """
        Determine if a file should be processed.

        Args:
            file_path: Path to the file

        Returns:
            bool: True if file should be processed, False otherwise
        """
        # Skip directories
        if file_path.is_dir():
            return False

        # Skip README files
        if file_path.name.upper() == "README.MD":
            return False

        # Skip hidden files (starting with .)
        if file_path.name.startswith('.'):
            return False

        # Skip temporary files
        if file_path.name.endswith(('.tmp', '.temp', '~')):
            return False

        # Check if already processed
        file_hash = self._get_file_hash(file_path)
        if file_hash in self.processed_files:
            self.logger.debug(f"File already processed: {file_path.name}")
            return False

        return True

    def check_for_updates(self) -> bool:
        """
        Check Inbox folder for new files.

        Scans the Inbox folder for any new files that haven't been processed yet.

        Returns:
            bool: True if new files found, False otherwise
        """
        try:
            # Get all files in inbox
            all_files = [f for f in self.inbox_folder.iterdir() if f.is_file()]

            # Filter to processable files
            new_files = [f for f in all_files if self._should_process_file(f)]

            if new_files:
                self.logger.info(f"Found {len(new_files)} new file(s) in Inbox")
                for file in new_files:
                    self.logger.info(f"  - {file.name}")
                return True

            return False

        except Exception as e:
            self.logger.error(f"Error checking for updates: {e}", exc_info=True)
            return False

    def create_action_file(self) -> Optional[Path]:
        """
        Create action files for all new files in Inbox.

        For each new file:
        1. Copy file to Needs_Action folder
        2. Create rich metadata action file
        3. Mark file as processed

        Returns:
            Optional[Path]: Path to last created action file, or None if failed
        """
        try:
            # Get all processable files
            all_files = [f for f in self.inbox_folder.iterdir() if f.is_file()]
            new_files = [f for f in all_files if self._should_process_file(f)]

            if not new_files:
                self.logger.warning("create_action_file called but no new files found")
                return None

            last_action_file = None

            # Process each file
            for file_path in new_files:
                try:
                    action_file = self._process_single_file(file_path)
                    if action_file:
                        last_action_file = action_file

                except Exception as e:
                    self.logger.error(f"Failed to process {file_path.name}: {e}")
                    continue

            return last_action_file

        except Exception as e:
            self.logger.error(f"Error creating action files: {e}", exc_info=True)
            return None

    def _process_single_file(self, file_path: Path) -> Optional[Path]:
        """
        Process a single file from Inbox.

        Args:
            file_path: Path to the file to process

        Returns:
            Optional[Path]: Path to created action file, or None if failed
        """
        self.logger.info(f"Processing file: {file_path.name}")

        # Get file metadata
        stat = file_path.stat()
        file_size = stat.st_size
        file_size_human = self._get_file_size_human(file_size)
        file_hash = self._get_file_hash(file_path)
        file_extension = file_path.suffix.lower()

        # Determine file type category
        file_type = self._categorize_file(file_extension)

        # Copy file to Needs_Action folder
        destination = self.needs_action_folder / file_path.name

        # Handle name conflicts
        counter = 1
        while destination.exists():
            stem = file_path.stem
            destination = self.needs_action_folder / f"{stem}_{counter}{file_path.suffix}"
            counter += 1

        try:
            shutil.copy2(file_path, destination)
            self.logger.info(f"Copied to: {destination.name}")

        except Exception as e:
            self.logger.error(f"Failed to copy file: {e}")
            return None

        # Create action file with rich metadata
        action_filename = f"{self.get_date_prefix()}_FileDropped_{file_path.stem}.md"
        action_file = self.needs_action_folder / action_filename

        # Handle action file name conflicts
        counter = 1
        while action_file.exists():
            action_filename = f"{self.get_date_prefix()}_FileDropped_{file_path.stem}_{counter}.md"
            action_file = self.needs_action_folder / action_filename
            counter += 1

        # Create action file content
        content = self._create_action_content(
            file_path=file_path,
            destination=destination,
            file_size=file_size,
            file_size_human=file_size_human,
            file_hash=file_hash,
            file_type=file_type,
            file_extension=file_extension
        )

        try:
            action_file.write_text(content, encoding='utf-8')
            self.logger.info(f"Created action file: {action_file.name}")

        except Exception as e:
            self.logger.error(f"Failed to create action file: {e}")
            return None

        # Mark file as processed
        self.processed_files.add(file_hash)
        self.logger.info(f"Successfully processed: {file_path.name}")

        return action_file

    def _categorize_file(self, extension: str) -> str:
        """
        Categorize file by extension.

        Args:
            extension: File extension (e.g., '.pdf', '.jpg')

        Returns:
            str: File category
        """
        categories = {
            'document': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt'],
            'spreadsheet': ['.xls', '.xlsx', '.csv', '.ods'],
            'presentation': ['.ppt', '.pptx', '.odp'],
            'image': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'],
            'video': ['.mp4', '.avi', '.mov', '.mkv', '.webm'],
            'audio': ['.mp3', '.wav', '.flac', '.m4a', '.ogg'],
            'archive': ['.zip', '.rar', '.7z', '.tar', '.gz'],
            'code': ['.py', '.js', '.java', '.cpp', '.c', '.html', '.css', '.json', '.xml'],
            'data': ['.json', '.xml', '.yaml', '.yml', '.sql', '.db'],
        }

        for category, extensions in categories.items():
            if extension in extensions:
                return category

        return 'other'

    def _create_action_content(
        self,
        file_path: Path,
        destination: Path,
        file_size: int,
        file_size_human: str,
        file_hash: str,
        file_type: str,
        file_extension: str
    ) -> str:
        """
        Create rich action file content with metadata.

        Args:
            file_path: Original file path
            destination: Copied file path
            file_size: File size in bytes
            file_size_human: Human-readable file size
            file_hash: SHA256 hash of file
            file_type: File category
            file_extension: File extension

        Returns:
            str: Formatted action file content
        """
        timestamp = self.get_timestamp()
        date_prefix = self.get_date_prefix()

        content = f"""---
type: file_drop
created: {date_prefix}
timestamp: {timestamp}
priority: medium
status: pending
assigned_to: ai
---

# File Dropped: {file_path.name}

## Description
A new file has been dropped into the Inbox and requires processing.

## File Metadata

### Basic Information
- **Original Name**: {file_path.name}
- **File Type**: {file_type}
- **Extension**: {file_extension}
- **Size**: {file_size_human} ({file_size:,} bytes)

### Location
- **Original Path**: `Inbox/{file_path.name}`
- **Current Path**: `Needs_Action/{destination.name}`

### Technical Details
- **SHA256 Hash**: `{file_hash}`
- **Detected**: {timestamp}
- **Modified**: {datetime.fromtimestamp(file_path.stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S')}

## Suggested Actions

Based on file type `{file_type}`, consider:

"""

        # Add type-specific suggestions
        suggestions = self._get_type_suggestions(file_type)
        for suggestion in suggestions:
            content += f"- {suggestion}\n"

        content += f"""

## Success Criteria
- [ ] File reviewed and categorized
- [ ] Appropriate action taken based on file type
- [ ] File moved to appropriate folder or archived
- [ ] Log entry created
- [ ] Dashboard updated

## Notes
- File automatically copied from Inbox to Needs_Action
- Original file remains in Inbox (can be deleted after processing)
- Hash recorded to prevent duplicate processing

## Next Steps
1. Review file contents
2. Determine appropriate action
3. Execute or create plan if complex
4. Update status and log

---
**Auto-generated by FilesystemWatcher**
**Detection Time**: {timestamp}
"""

        return content

    def _get_type_suggestions(self, file_type: str) -> list[str]:
        """
        Get suggested actions based on file type.

        Args:
            file_type: File category

        Returns:
            list[str]: List of suggested actions
        """
        suggestions = {
            'document': [
                'Review document contents',
                'Extract key information',
                'File in appropriate project folder',
                'Add to document index'
            ],
            'spreadsheet': [
                'Review data structure',
                'Validate data integrity',
                'Import into database if needed',
                'Generate summary report'
            ],
            'image': [
                'Review image content',
                'Optimize if needed',
                'Add to media library',
                'Extract text if contains information (OCR)'
            ],
            'code': [
                'Review code quality',
                'Check for security issues',
                'Add to code repository',
                'Document purpose and usage'
            ],
            'archive': [
                'Extract contents safely',
                'Review extracted files',
                'Process individual files',
                'Clean up after extraction'
            ],
            'data': [
                'Validate data format',
                'Parse and analyze contents',
                'Import into appropriate system',
                'Create backup'
            ],
        }

        return suggestions.get(file_type, [
            'Review file contents',
            'Determine appropriate action',
            'File in correct location',
            'Update documentation'
        ])


def main():
    """
    Main entry point for the filesystem watcher.

    Parses command-line arguments and starts the watcher.
    """
    parser = argparse.ArgumentParser(
        description='Monitor Inbox folder for new files (Bronze-tier AI Employee)'
    )
    parser.add_argument(
        'vault_path',
        nargs='?',
        default='AI_Employee_Vault',
        help='Path to AI Employee Vault (default: AI_Employee_Vault)'
    )
    parser.add_argument(
        '--interval',
        type=int,
        default=30,
        help='Check interval in seconds (default: 30)'
    )
    parser.add_argument(
        '--log-level',
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
        default='INFO',
        help='Logging level (default: INFO)'
    )

    args = parser.parse_args()

    # Convert log level string to constant
    log_level = getattr(logging, args.log_level)

    # Setup basic logging
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    print("=" * 60)
    print("Bronze-tier AI Employee - Filesystem Watcher")
    print("=" * 60)
    print(f"Vault Path: {args.vault_path}")
    print(f"Check Interval: {args.interval} seconds")
    print(f"Log Level: {args.log_level}")
    print("\nMonitoring Inbox folder for new files...")
    print("Drop any file into Inbox/ to trigger processing")
    print("\nPress Ctrl+C to stop\n")
    print("=" * 60)

    try:
        # Create and run the watcher
        watcher = FilesystemWatcher(
            vault_path=args.vault_path,
            check_interval=args.interval,
            log_level=log_level
        )
        watcher.run()

    except FileNotFoundError as e:
        print(f"\n❌ Error: {e}")
        print(f"Please ensure the vault exists at: {args.vault_path}")
        return 1

    except KeyboardInterrupt:
        print("\n\n✅ Watcher stopped by user")
        return 0

    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        logging.exception("Fatal error")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
