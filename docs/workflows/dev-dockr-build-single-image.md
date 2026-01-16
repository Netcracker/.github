# Dev Docker Build – Single Image

Reusable GitHub Actions workflow template for building and publishing **one multi-platform Docker image** to GitHub Container Registry (GHCR).

This template is part of the Netcracker / Qubership shared workflow collection.

## Repository

https://github.com/Netcracker/.github  
Path: `workflow-templates/dev-docker-build-single-image.yml` (branch: `refactor/docker-images-build`)

## Purpose

Automatically (or manually) build and push a single Docker image from a repository that contains a **Dockerfile in the root**.

- Builds for **linux/amd64** and **linux/arm64**
- Publishes to `ghcr.io/${{ github.repository }}` (or custom name)
- Supports **dry-run** mode
- Allows overriding image name and adding extra tags
- Skips execution on documentation-only or GitHub config changes

## Trigger Events

```yaml
on:
  workflow_dispatch:           # manual trigger from GitHub UI
    inputs:
      custom-image-name
      tags
      dry-run
  push:
    branches: ['**']
    paths-ignore: [ .github/**, docs/**, CODE-OF-CONDUCT.md, CONTRIBUTING.md, LICENSE, README.md, SECURITY.md ]
  pull_request:
    branches: ['**']
    paths-ignore: [ same as above ]
```

### Optional: Override image name & tags via dispatch

When running manually (Workflow Dispatch):

- **custom-image-name**: `mycompany/backend` → results in `ghcr.io/mycompany/backend:…`
- **tags**        : `v1.2.3-test, debug` → additional tags
- **dry-run**     : `true` → build only, do **not** push

## Generated Image Tags (default behavior)

The workflow uses an internal metadata action that typically produces tags like:

```
ghcr.io/owner/repo:pr-45
ghcr.io/owner/repo:pr-45-abc1234   (short sha)
ghcr.io/owner/repo:branch-name
ghcr.io/owner/repo:20250116-abc1234
ghcr.io/owner/repo:latest          (only on default branch in some configurations)
```

→ Exact tags depend on the `netcracker/qubership-workflow-hub/actions/metadata-action` logic.

You can **append** extra tags using the `tags` input.

## Requirements

- Dockerfile must be in the **root** of the repository
- No custom build context / subfolder supported (use a different template if needed)
- Repository must have permission to write packages (`packages: write`)

## Internals / Used Actions

| Step                        | Action                                                                 | Purpose                              |
|-----------------------------|------------------------------------------------------------------------|--------------------------------------|
| Checkout                    | `actions/checkout@v6`                                                  | Get source code                      |
| Create name / metadata      | `netcracker/qubership-workflow-hub/actions/metadata-action@v2.0.7`     | Generates base tag(s)                |
| Prepare tags                | Custom shell script                                                    | Combines base + manual tags          |
| Build & Publish             | `netcracker/qubership-workflow-hub/actions/docker-action@v2.0.7`       | Main docker buildx build & push      |

## Permissions

```yaml
permissions:
  contents: read
  packages: write    # required to push to GHCR
```

## Limitations / Notes

- Expects **Dockerfile** in repository root (no `docker buildx build --file path/Dockerfile`)
- No advanced `.dockerignore` or multi-stage override options exposed
- No configurable build-args via workflow inputs (may be supported inside `docker-action`)
- Dry-run still performs the build (useful to verify multi-platform compatibility)
- Uses fixed platforms: `linux/amd64,linux/arm64`

## Troubleshooting

- Image not pushed? → Check `packages: write` permission & `GITHUB_TOKEN` scope
- Wrong image name? → Use `custom-image-name` input
- Want different platforms? → Currently hardcoded (fork or ask maintainers)
- Build fails on arm64? → Make sure your Dockerfile is multi-arch friendly

## See also

- Parent repo: https://github.com/Netcracker/.github
- Related template: likely exists for multi-image / Helm / release workflows in the same folder
- Internal action docs: `netcracker/qubership-workflow-hub`

Happy building! 🐳
