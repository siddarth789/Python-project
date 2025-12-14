from pathlib import Path
from collections import Counter, defaultdict

CATEGORY_MAP = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"],
    "Others": []
}

def get_category(ext: str):
    ext = ext.lower()
    for category, exts in CATEGORY_MAP.items():
        if ext in exts:
            return category
    return "Others"

def analyze_folder(folder: Path):
    files = []
    for item in folder.iterdir():
        if item.is_dir():
            continue
        ext = item.suffix
        category = get_category(ext)
        size = item.stat().st_size
        files.append((item.name, category, size))
    return files

def print_report(files):
    print("\n=== FILE ANALYSIS REPORT ===\n")
    for name, category, size in files:
        print(f"{name}  ->  {category}")

if __name__ == "__main__":
    folder = Path("test_files")
    files = analyze_folder(folder)
    print_report(files)
