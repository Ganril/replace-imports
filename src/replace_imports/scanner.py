from pathlib import Path
from .safe_path import is_safe


def find_py_files(root: str):
    root_path = Path(root)

    for file in root_path.rglob("*.py"):
        if not is_safe(file):
            continue
        yield file


def scan_for_pattern(root: str, pattern: str):
    matches = []

    for file in find_py_files(root):
        try:
            content = file.read_text(encoding="utf-8")
        except Exception:
            continue

        if pattern in content:
            matches.append(file)

    return matches
