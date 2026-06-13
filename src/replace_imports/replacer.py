from pathlib import Path
import difflib


def replace_in_file(file_path: Path, old: str, new: str, apply: bool = False):
    """
    Replaces text in a single file safely.
    Returns diff output.
    """

    try:
        original = file_path.read_text(encoding="utf-8")
    except Exception as e:
        return f"[SKIP] {file_path}: {e}"

    if old not in original:
        return f"[NO MATCH] {file_path}"

    updated = original.replace(old, new)

    diff = difflib.unified_diff(
        original.splitlines(keepends=True),
        updated.splitlines(keepends=True),
        fromfile=str(file_path),
        tofile=str(file_path),
    )

    diff_text = "".join(diff)

    if apply:
        file_path.write_text(updated, encoding="utf-8")

    return diff_text


def batch_replace(files, old: str, new: str, apply: bool = False):
    results = []

    for file in files:
        result = replace_in_file(file, old, new, apply=apply)
        results.append(result)

    return results
