from dataclasses import dataclass
import yaml
from pathlib import Path


@dataclass
class Config:
    root: str = "."
    dry_run: bool = True
    apply: bool = False

    ignore: list = None
    rules: list = None


def load_config(path="replace-imports.yml") -> Config:
    p = Path(path)

    if not p.exists():
        return Config(ignore=["venv", ".git", "__pycache__"], rules=[])

    data = yaml.safe_load(p.read_text())

    return Config(
        root=data.get("root", "."),
        dry_run=data.get("dry_run", True),
        apply=data.get("apply", False),
        ignore=data.get("ignore", []),
        rules=data.get("rules", []),
    )
