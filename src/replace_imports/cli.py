import argparse
from .scanner import scan_for_pattern
from .replacer import batch_replace
from .config import load_config


def main():
    parser = argparse.ArgumentParser(description="Replace Imports Tool V2")

    parser.add_argument("--config", default="replace-imports.yml")
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--preview", action="store_true")

    args = parser.parse_args()

    config = load_config(args.config)

    print("=== REPLACE-IMPORTS V2 ===")
    print(f"Root: {config.root}")
    print(f"Dry run: {not args.apply}")

    for rule in config.rules:
        old = rule["from"]
        new = rule["to"]

        print(f"\n[RULE] {old} -> {new}")

        files = scan_for_pattern(config.root, old)

        print(f"Found {len(files)} files")

        results = batch_replace(files, old, new, apply=args.apply)

        if args.preview or not args.apply:
            for r in results:
                if r:
                    print(r)
