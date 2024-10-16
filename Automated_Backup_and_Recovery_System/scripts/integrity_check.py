import os
import hashlib

def generate_checksum(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

def verify_integrity(source_dir, backup_dir):
    issues_found = False
    for root, _, files in os.walk(source_dir):
        for file in files:
            source_file = os.path.join(root, file)
            backup_file = source_file.replace(source_dir, backup_dir, 1)
            if not os.path.exists(backup_file):
                print(f"Missing backup file: {backup_file}")
                issues_found = True
                continue
            if generate_checksum(source_file) != generate_checksum(backup_file):
                print(f"Integrity issue with file: {source_file}")
                issues_found = True
    return issues_found

source_dir = "/path/to/source"
backup_dir = "/path/to/backup"

if verify_integrity(source_dir, backup_dir):
    print("Integrity issues found.")
else:
    print("All files backed up correctly.")
