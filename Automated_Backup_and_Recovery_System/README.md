# Automated Backup and Recovery System

## Overview
This project is a simple automated backup and recovery system that uses Bash scripting, Rsync, and Python to automate data backups, perform integrity checks, and allow for quick recovery.

## Project Structure
- **scripts/backup.sh**: Bash script to automate data backups using Rsync.
- **scripts/integrity_check.py**: Python script to verify backup integrity using checksums.
- **scripts/recovery.sh**: Bash script to recover data from backup.
- **README.md**: Project documentation.

## Setup and Usage
1. Edit the `SOURCE_DIR` and `BACKUP_DIR` variables in `backup.sh` and `integrity_check.py`.
2. Make the scripts executable:
   ```bash
   chmod +x scripts/backup.sh
   chmod +x scripts/recovery.sh
   ```
3. Schedule the `backup.sh` script to run automatically using a Cron job:
   ```bash
   crontab -e
   ```
   Add the following to run daily at midnight:
   ```bash
   0 0 * * * /path/to/backup.sh
   ```
4. (Optional) Run `integrity_check.py` to verify backups.

## Dependencies
- Python 3.x
- Rsync

## Notes
- Update the paths in each script to match your system configuration.
- This setup assumes a Linux/macOS environment with Rsync and Python installed.
