#!/bin/bash
# Recovery Script

# Define directories
BACKUP_DIR="/path/to/backup"
RECOVERY_DIR="/path/to/recovery" # Replace with original location

# Copy files back
rsync -av "$BACKUP_DIR" "$RECOVERY_DIR"

echo "Recovery completed on $(date)"
