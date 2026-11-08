#!/usr/bin/env python3
"""Lightweight static checks for common API route definitions in a project."""

import argparse
import re
from pathlib import Path

ROUTE_PATTERNS = [
    re.compile(r"""\b(?:app|router|server)\.(get|post|put|patch|delete|options|head)\s*\(\s*['"`]([^'"`]+)""", re.I),
    re.compile(r"""@(?:Get|Post|Put|Patch|Delete|Request)Mapping\s*\(\s*['"`]([^'"`]+)"""),
    re.compile(r"""\bpath\s*\(\s*['"`]([^'"`]+)"""),
]
EXTENSIONS = {".js", ".jsx", ".ts", ".tsx", ".py", ".java", ".go", ".php", ".rb"}


def scan(root: Path):
    findings = []
    for file in root.rglob("*"):
        if not file.is_file() or file.suffix.lower() not in EXTENSIONS:
            continue
        if any(part in {"node_modules", ".git", "vendor", "dist", "build"} for part in file.parts):
            continue
        try:
            source = file.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for number, line in enumerate(source.splitlines(), 1):
            for pattern in ROUTE_PATTERNS:
                for match in pattern.finditer(line):
                    groups = match.groups()
                    if len(groups) == 2:
                        method, path = groups
                    else:
                        method, path = "route", groups[0]
                    findings.append((file.relative_to(root), number, method.upper(), path))
    return findings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_path", type=Path)
    args = parser.parse_args()
    root = args.project_path.resolve()
    if not root.is_dir():
        parser.error(f"not a directory: {root}")
    findings = scan(root)
    if not findings:
        print("No supported route declarations found. This is not proof that the project has no API routes.")
        return 0
    print(f"Found {len(findings)} route declaration(s):")
    for file, line, method, path in findings:
        print(f"{file}:{line}: {method} {path}")
    print("\nStatic inventory only: verify middleware, authentication, authorization, and runtime behavior separately.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
