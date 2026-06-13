# safe_path.py
from pathlib import Path

BLOCKED = ["site-packages", "venv", ".git", "__pycache__"]

def is_safe(path: Path) -> bool:
    return not any(part in BLOCKED for part in path.parts)
