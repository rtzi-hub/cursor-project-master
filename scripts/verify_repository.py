#!/usr/bin/env python3
import json,re,sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
errors=[]

required=[
"README.md","AGENTS.md","SECURITY.md","PUBLIC_RELEASE_SECURITY.md",
"mkdocs.yml","docs/index.md","docs/assets/javascripts/app.js",
"docs/assets/data/project-types.json","docs/assets/data/workflows.json",
"docs/assets/data/prompts.json","scripts/project_master.py"
]
for r in required:
    if not (ROOT/r).exists():
        errors.append("missing "+r)

for n in ["project-types.json","workflows.json","prompts.json","tool-catalog.json"]:
    try:
        json.loads((ROOT/"docs/assets/data"/n).read_text(encoding="utf-8"))
    except Exception as e:
        errors.append(f"invalid {n}: {e}")

try:
    workflows=json.loads((ROOT/"docs/assets/data/workflows.json").read_text(encoding="utf-8"))
    prompts=json.loads((ROOT/"docs/assets/data/prompts.json").read_text(encoding="utf-8"))
    for flow in ["new","existing"]:
        for step in workflows[flow]:
            if step.get("prompt") and step["prompt"] not in prompts:
                errors.append(f"missing prompt {step['prompt']}")
except Exception:
    pass

credential_patterns=[
    r"AKIA[0-9A-Z]{16}",
    r"gh[pousr]_[A-Za-z0-9]{20,}",
    r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
    r"sk-[A-Za-z0-9]{20,}",
]
for f in ROOT.rglob("*"):
    if f.is_file() and f.suffix.lower() in {".md",".js",".json",".py",".yml",".yaml",".mdc",".txt"}:
        text=f.read_text(encoding="utf-8",errors="ignore")
        for pat in credential_patterns:
            if re.search(pat,text):
                errors.append(f"credential-like content in {f.relative_to(ROOT)}")

for wf in (ROOT/".github"/"workflows").glob("*.yml"):
    text=wf.read_text(encoding="utf-8")
    for line in text.splitlines():
        if "uses:" in line and "actions/" in line:
            if not re.search(r"uses:\s*[^@]+@[0-9a-f]{40}\b",line):
                errors.append(f"un-pinned GitHub Action in {wf.relative_to(ROOT)}: {line.strip()}")
    if "actions/checkout@" in text and "persist-credentials: false" not in text:
        errors.append(f"checkout credentials persist in {wf.relative_to(ROOT)}")

if errors:
    print("FAILED")
    for error in errors:
        print("-",error)
    sys.exit(1)

print("Repository verification passed.")
