#!/usr/bin/env python3
from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
files = ["README.md","ROOT.md","CHARTER.md","CONSTITUTION.md","GOVERNANCE.md",
         "repository.yaml","manifest.yaml","SKAC-2026-0001.md","RELEASE_NOTES.md","CHANGELOG.md"]
dirs = ["docs","archive","releases","templates","scripts","validation"]
missing = [f"file:{x}" for x in files if not (root/x).is_file()]
missing += [f"dir:{x}" for x in dirs if not (root/x).is_dir()]
checks = [
    ('id: "KOP-00_0"', root/"repository.yaml"),
    ('starter_kit: "STK-00_0-v1.0"', root/"manifest.yaml"),
    ("One Starter Kit, One Commit", root/"GOVERNANCE.md"),
]
failed = [needle for needle,path in checks if needle not in path.read_text(encoding="utf-8")]
if missing or failed:
    print("VALIDATION FAILED")
    for x in missing: print("MISSING", x)
    for x in failed: print("FAILED", x)
    sys.exit(1)
print("VALIDATION PASSED")
print("Checked 10 required files and 6 required directories.")
