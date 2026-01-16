# CI: Dev Docker Build (Selective)

**Workflow template name:** `dev-docker-build-selective.yml`  
**Purpose:** Build and (optionally) publish multiple Docker images **selectively** — only for components whose source files have changed.

This is a **template-style workflow** designed for monorepos that contain multiple independent services / libraries packaged as Docker images.

## Features

- **Selective builds** — builds only images whose declared `changeset` paths were modified (using `tj-actions/changed-files`)
- Skips unchanged components → saves a lot of CI time and resources in large monorepos
- Configuration-driven via single file: `.qubership/docker.cfg`
- Supports **push**, **pull_request**, and **workflow_dispatch** triggers
- Generates semantic tags (branch name → tag, customizable)
- Dry-run mode available (useful for PRs or manual testing)
- Publishes to GitHub Container Registry (`ghcr.io`) when permissions allow
- Concurrency group prevents parallel runs on the same branch / commit

## Configuration File

All logic is driven by this file (must exist in the repository):

```text
.qubership/docker.cfg
```

Example location of full documentation + example:

https://github.com/Netcracker/qubership-workflow-hub/tree/main/actions/docker-config-resolver

## Triggers

```yaml
on:
  push:
    branches: ["**"]
    paths-ignore: [ .github/**, docs/**, *.md (various meta files) ]

  pull_request:
    branches: ["**"]
    paths-ignore: same as above

  workflow_dispatch:
    inputs:
      tags:          { type: string,  default: "" }
      dry-run:       { type: boolean, default: false }
      replace-symbol:{ type: string,  default: "_" }
```

## How Selective Building Works

1. `tj-actions/changed-files` → collects all changed files (push/PR)
2. Filters `.qubership/docker.cfg` components
3. Keeps only those where **any** path from `changeset` matches a changed file
4. Only matching components go to the matrix strategy

→ On big monorepos you usually build 1–3 images instead of 20–50

## Jobs Overview

| Job       | Purpose                                         | Matrix? | Key Action used                                 |
|-----------|--------------------------------------------------|---------|--------------------------------------------------|
| `prepare` | Checkout → detect changes → filter config → generate tags | No      | `docker-config-resolver`, `metadata-action` |
| `build`   | Build & push selected images                     | Yes     | `docker-action` (from Netcracker/qubership-workflow-hub) |

## Important Inputs / Controls (workflow_dispatch)

| Input           | Type    | Default     | Meaning                                                                 |
|-----------------|---------|-------------|-------------------------------------------------------------------------|
| `tags`          | string  | `""`        | Extra tags to add (comma-separated or space-separated)                  |
| `dry-run`       | boolean | `false`     | When `true` → build but **do not push**                                 |
| `replace-symbol`| string  | `"_"`       | In branch names: `-` → `_` (or any other symbol you prefer in tags)     |

## Outputs / Artifacts

Images are pushed directly to:

```
ghcr.io/${{ github.repository_owner }}/<component-name>:<tag>
```

Example tags generated:

- `main` → `main`
- `feature/new-login` → `feature_new_login` (with default replace-symbol)
- `refs/heads/release/1.2.3` → `release_1.2.3`

## Recommended Usage in Your Repository

Copy the whole template into your repository and customize it if needed.

```yaml
name: CI - Docker Images

on: [push, pull_request, workflow_dispatch]

jobs:
  call-docker-build:
    uses: Netcracker/.github/.github/workflow-templates/dev-docker-build-selective.yml@refactor/docker-images-build
    secrets: inherit
```

Or copy the template and adjust paths / organisation name.

## Requirements

- Repository must contain `.qubership/docker.cfg`
- Custom actions from `Netcracker/qubership-workflow-hub` must be available
  - `docker-config-resolver`
  - `metadata-action`
  - `docker-action`
- Write permission to `packages` (for `ghcr.io` push)

## Related Repositories

- https://github.com/Netcracker/qubership-workflow-hub  
  (contains the composite actions used in this workflow)
