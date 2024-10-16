#!/bin/bash
# Automated Backup Script

# Define directories
SOURCE_DIR="/path/to/source"
BACKUP_DIR="/path/to/backup"

# Create the backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Rsync command with options
rsync -av --delete "$SOURCE_DIR" "$BACKUP_DIR"

# Output message
echo "Backup completed on $(date)"
