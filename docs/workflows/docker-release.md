# Docker Images Release

## Purpose

Releases Docker images and creates a GitHub release tag using configuration in `.qubership/docker-build-config.cfg`.

The workflow validates a `release` tag, builds/publishes images via `qubership-workflow-hub` actions, and runs Release Drafter.

## Trigger

- `workflow_dispatch` with input:
  - `release` (string, required)

## Permissions

- `contents: read` (top-level)

Job-specific permissions:
- `create-tag` job: `contents: write`
- `docker-build` job: `contents: read`, `packages: write`
- `github-release` job: `contents: write`, `packages: write`

## Concurrency

- group: `${{ github.workflow }}-${{ github.ref }}`
- cancel-in-progress: `true`

## Jobs

### `check-tag`

- `netcracker/qubership-workflow-hub/actions/tag-action@...` to ensure `v${{ inputs.release }}` does not already exist

### `load-docker-build-components`

- Checkout code
- Read `.qubership/docker-build-config.cfg`
- Validate format: `components` array and `platforms` string
- Output `components` and `platforms` for matrix build

### `create-tag`

- Create git tag `v${{ inputs.release }}` (write permission)

### `docker-build`

- Matrix over components from config
- For each component:
  - set `IMAGE_VERSION=${{ inputs.release }}`
  - use `netcracker/qubership-workflow-hub/actions/docker-action@...` to build and publish

### `github-release`

- Checkout tag `v${{ inputs.release }}`
- Run `netcracker/release-drafter@...` with:
  - `config-name: release-drafter-config.yml`
  - `publish: true`
  - `name/tag/version: ${{ inputs.release }}`

## Configuration files

- `.qubership/docker-build-config.cfg` (example: `config/examples/docker.cfg`)
- `.github/release-drafter-config.yml` (example: `config/examples/release-drafter-config.yml`)
