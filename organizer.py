from pathlib import Path
import shutil
import argparse
import logging

# ---------------- CONFIG ---------------- #

CATEGORY_MAP = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"],
    "Others": []
}

LOG_FILE = "organizer.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# ---------------- LOGIC ---------------- #

def get_category(ext: str):
    ext = ext.lower()
    for category, exts in CATEGORY_MAP.items():
        if ext in exts:
            return category
    return "Others"

def move_files(folder: Path, dry_run: bool):
    if not folder.exists():
        print("❌ Error: Folder does not exist")
        logging.error(f"Folder does not exist: {folder}")
        return

    for item in folder.iterdir():

        if item.is_dir():
            continue

        # Skip hidden files
        if item.name.startswith("."):
            logging.info(f"Skipped hidden file: {item.name}")
            continue

        ext = item.suffix.lower()
        category = get_category(ext)

        category_folder = folder / category
        destination = category_folder / item.name

        # Avoid overwrite
        if destination.exists():
            destination = category_folder / f"copy_{item.name}"

        if dry_run:
            print(f"[DRY RUN] {item.name} → {category}/")
            logging.info(f"[DRY RUN] {item.name} → {category}/")
        else:
            category_folder.mkdir(exist_ok=True)
            shutil.move(str(item), str(destination))
            print(f"Moved {item.name} → {category}/")
            logging.info(f"Moved {item.name} → {category}/")

# ---------------- ENTRY ---------------- #

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="File Organizer Tool")
    parser.add_argument("path", help="Folder path to organize")
    parser.add_argument("--dry-run", action="store_true", help="Preview without moving files")

    args = parser.parse_args()
    folder_path = Path(args.path)

    move_files(folder_path, args.dry_run)
