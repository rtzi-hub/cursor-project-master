#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,shutil,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];DATA=ROOT/"docs"/"assets"/"data";TEMPLATES=ROOT/"templates"
def load_json(n): return json.loads((DATA/n).read_text(encoding="utf-8"))
def copytree(src,dst):
    copied=skipped=0
    for p in src.rglob("*"):
        if not p.is_file(): continue
        o=dst/p.relative_to(src)
        if o.exists(): skipped+=1; continue
        o.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,o);copied+=1
    return copied,skipped
def detect(repo):
    return {"git":(repo/".git").exists(),"node":(repo/"package.json").exists(),"python":any((repo/n).exists() for n in ["pyproject.toml","requirements.txt","requirements-dev.txt"]),"terraform":any(repo.rglob("*.tf")),"docker":any((repo/n).exists() for n in ["Dockerfile","docker-compose.yml","compose.yml"]), "github_actions":(repo/".github"/"workflows").exists()}
def init(a):
    types=load_json("project-types.json")
    if a.type not in types: raise SystemExit("Unknown type")
    target=Path(a.target).expanduser().resolve();target.mkdir(parents=True,exist_ok=True)
    c,s=copytree(TEMPLATES/"common",target)
    mf=target/"cpm.project.json";d=json.loads(mf.read_text(encoding="utf-8"));d["name"]=a.name;d["project_type"]=a.type;mf.write_text(json.dumps(d,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(f"Initialized {target}; copied {c}, skipped {s}.")
def existing(a):
    target=Path(a.target).expanduser().resolve()
    c1,s1=copytree(TEMPLATES/"common",target);c2,s2=copytree(TEMPLATES/"existing",target/".project-master")
    print(f"Prepared {target}; copied {c1+c2}, skipped {s1+s2}.")
def doctor(a):
    repo=Path(a.repo).expanduser().resolve();print("Cursor Project Master — Doctor");print(json.dumps({"repository":str(repo),"detected":detect(repo)},indent=2))
    print("\nTools:")
    for x in ["git","python","node","docker","terraform","tflint","trivy","semgrep","pre-commit","trufflehog","gitleaks"]: print(("✓" if shutil.which(x) else "○"),x)
    print("\nRead-only: install only tools relevant to the approved stack.")
def _safe_relative_dir(project_root: Path, rel: str) -> Path:
    if not isinstance(rel, str) or not rel.strip():
        raise ValueError("directory entries must be non-empty strings")

    raw = rel.strip().replace("\\", "/")
    candidate_rel = Path(raw)

    if candidate_rel.is_absolute():
        raise ValueError(f"absolute path is not allowed: {rel}")
    if re.match(r"^[A-Za-z]:/", raw):
        raise ValueError(f"drive-qualified path is not allowed: {rel}")
    if raw.startswith("//"):
        raise ValueError(f"UNC/network path is not allowed: {rel}")
    if any(part == ".." for part in candidate_rel.parts):
        raise ValueError(f"path traversal is not allowed: {rel}")

    project_root = project_root.resolve()
    candidate = (project_root / candidate_rel).resolve()
    try:
        candidate.relative_to(project_root)
    except ValueError as exc:
        raise ValueError(f"path escapes project root: {rel}") from exc
    return candidate

def scaffold(a):
    mf=Path(a.manifest).expanduser().resolve()
    d=json.loads(mf.read_text(encoding="utf-8"))
    types=load_json("project-types.json")
    dirs=d.get("directories") or types.get(d.get("project_type","generic"),types["generic"])["scaffold"]

    if not isinstance(dirs, list):
        raise SystemExit("Manifest 'directories' must be a list.")

    created=0
    for rel in dirs:
        try:
            p=_safe_relative_dir(mf.parent, rel)
        except ValueError as exc:
            raise SystemExit(f"Unsafe scaffold path: {exc}")
        p.mkdir(parents=True,exist_ok=True)
        if not any(p.iterdir()):
            (p/".gitkeep").write_text("",encoding="utf-8")
        created += 1

    print(f"Scaffolded {created} directories; no existing files overwritten.")
def inspect(a):
    repo=Path(a.repo).expanduser().resolve();print(json.dumps({"repository":str(repo),"detected":detect(repo)},indent=2))
def main():
    p=argparse.ArgumentParser();s=p.add_subparsers(dest="cmd",required=True)
    q=s.add_parser("init");q.add_argument("--type",required=True);q.add_argument("--name",required=True);q.add_argument("--target",required=True);q.set_defaults(fn=init)
    q=s.add_parser("existing");q.add_argument("--target",required=True);q.set_defaults(fn=existing)
    q=s.add_parser("doctor");q.add_argument("--repo",required=True);q.set_defaults(fn=doctor)
    q=s.add_parser("scaffold");q.add_argument("--manifest",required=True);q.set_defaults(fn=scaffold)
    q=s.add_parser("inspect");q.add_argument("--repo",required=True);q.set_defaults(fn=inspect)
    a=p.parse_args();a.fn(a)
if __name__=="__main__":main()
