# Dev Docker Build (Multiple Images) – Workflow Template

**Repository**: `https://github.com/Netcracker/.github`  
**Path**: `workflow-templates/dev-docker-build-multiple-images.yml`

## Purpose

GitHub Actions workflow template that builds and publishes **multiple Docker images** from a single repository according to configuration defined in `.qubership/docker.cfg`.

Main features:

- Builds several Docker images in parallel (matrix strategy)
- Supports multi-platform builds (when specified in config)
- Publishes images to GitHub Container Registry (ghcr.io) or other registry configured via secrets
- Automatic tagging based on branch/tag name
- Manual override tags via workflow_dispatch
- Dry-run mode (build without push)
- Uses centralized custom actions from `netcracker/qubership-workflow-hub`

## How to Use This Template

Copy the whole template into your repository and customize it if needed.

## Required Files in Your Repository

| File                       | Mandatory | Purpose                                                                              |
| -------------------------- | --------- | ------------------------------------------------------------------------------------ |
| `.qubership/docker.cfg`    | Yes       | Main configuration – defines which images to build, contexts, Dockerfiles, platforms |
| `Dockerfile` (or multiple) | Yes       | Standard Dockerfiles referenced from the config                                      |

Example location of config:  
[docker-config-resolver action documentation](https://github.com/Netcracker/qubership-workflow-hub/tree/main/actions/docker-config-resolver#configuration-file-format)

## Configuration File Reference

See detailed documentation:  
→ [docker-config-resolver action documentation](https://github.com/Netcracker/qubership-workflow-hub/tree/main/actions/docker-config-resolver)

## Triggers

- `push` to any branch (except paths in `.github/**`, `docs/**`, etc.)
- `pull_request` to any branch
- `workflow_dispatch` (manual trigger)

## Inputs (workflow_dispatch)

| Name             | Type    | Default | Description                                  |
| ---------------- | ------- | ------- | -------------------------------------------- |
| `tags`           | string  | `""`    | Extra tags (comma separated)                 |
| `dry-run`        | boolean | `false` | Build images but do **not** push them        |
| `replace-symbol` | string  | `"_"`   | Symbol used to replace invalid chars in tags |

## Generated Image Tags

Default pattern:

- Branch build → `ghcr.io/<owner>/<repo>:feature_new-login`
- PR build     → `ghcr.io/<owner>/<repo>:pr-123`
- Tag build    → `ghcr.io/<owner>/<repo>:v1.2.3`, `ghcr.io/<owner>/<repo>:1.2.3`
- Manual extra tags are appended

Invalid characters (e.g. `/`) are replaced with `_` (configurable via `replace-symbol` input).

## Permissions Used

```yaml
permissions:
  contents: read
  packages: write   # required to push to ghcr.io
```

## Jobs Overview

1. `load-config`  
   Reads `.qubership/docker.cfg` → produces matrix of components

2. `docker-build` (matrix job)  
   One instance per component defined in config  
   - Checks out code  
   - Generates tags  
   - Builds & pushes (or dry-runs) using centralized `docker-action`

## Dependencies (Custom Actions)

All actions come from the same version:

- `netcracker/qubership-workflow-hub/actions/docker-config-resolver@v2.0.7`
- `netcracker/qubership-workflow-hub/actions/metadata-action@v2.0.7`
- `netcracker/qubership-workflow-hub/actions/docker-action@v2.0.7`

Pinned to commit `c1a5c8c2d9c2a79f548134db1d095f36ee0f28e7`

## Recommendations

- Use **GitHub Packages** (`ghcr.io`) – no extra secrets needed (token is automatic)
- For Docker Hub → add `DOCKER_USERNAME` + `DOCKER_PASSWORD` secrets and adjust config
- Consider adding `pull_request_target` if you want PRs from forks to build images (careful with permissions)

## See Also

- [Qubership Workflow Hub – docker-config-resolver docs](https://github.com/Netcracker/qubership-workflow-hub/tree/main/actions/docker-config-resolver)
- [Netcracker organization shared workflows](https://github.com/Netcracker/.github/tree/refactor/docker-images-build/workflow-templates)

Happy building! 🐳
