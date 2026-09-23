# Quick Start

The recommended path is **Guided Setup**.

```bash
git clone https://github.com/rtzi-hub/cursor-project-master.git
cd cursor-project-master
```

Inspect a repository:

```bash
python scripts/project_master.py doctor --repo /path/to/project
```

Create a new project engineering pack:

```bash
python scripts/project_master.py init --type web-app --name my-project --target ../my-project
```

After approving `cpm.project.json`:

```bash
python scripts/project_master.py scaffold --manifest ../my-project/cpm.project.json
```

The CLI does not auto-install privileged tools or perform destructive operations.
