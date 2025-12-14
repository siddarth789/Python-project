# File Organizer (Python Automation)

A Python command-line tool that automatically organizes files in a folder
into category-based subfolders such as Images, Documents, Audio, and Archives.

## Features
- Automatic file categorization by extension
- Safe file moving with overwrite protection
- Dry-run mode to preview changes
- Command-line interface (CLI)
- Action logging for traceability

## Categories
- Images: jpg, jpeg, png
- Documents: pdf, docx, txt
- Audio: mp3, wav
- Archives: zip, rar
- Others: uncategorized files

## Usage

### Dry Run (Preview only)
```bash
python organizer.py <folder_path> --dry-run
