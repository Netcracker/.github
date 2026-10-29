# Cleanup Old Docker Container Versions

## Retention policy

The shared template runs weekly on Sunday at 00:00 UTC and supports manual runs.
It keeps:

- `latest` indefinitely.
- LTS snapshot aliases matching `lts-*-snapshot` or `lts_*-snapshot` indefinitely.
  For example, branch `lts/25-snapshot` is published as `lts-25-snapshot`
  when `/` is normalized to `-`; legacy builds may use `_` instead.
- All container versions created within the last seven days.

Other tagged versions older than seven days are eligible for deletion, including
Renovate and Dependabot builds, feature branches, commit tags, `main`, and release
versions. If a version has multiple tags, any protected tag preserves the whole
version. The cleanup action also protects manifest children of protected aliases.

Do not use `*.*` as an exclusion: it retains every tag containing a dot, including
Renovate branch tags with dependency versions or registry hostnames. `semver`,
`release*`, and `main` are also intentionally absent from the default exclusions.
Repositories that require additional retained tags must configure them explicitly.

## Configuration

| Manual input | Default | Purpose |
| --- | --- | --- |
| `threshold-days` | `7` | Minimum age in days for deletion |
| `included-tags` | `*` | Tags eligible for deletion |
| `excluded-tags` | `latest,lts-*-snapshot,lts_*-snapshot` | Tags protected from deletion |
| `dry-run` | `true` | Preview candidates without deleting versions |
| `debug` | `false` | Enable detailed logs |

Scheduled runs use the same tag exclusions and age threshold, with `dry-run: false`.
Manual runs default to a preview; choose `dry-run: false` to perform cleanup.
The action automatically protects `latest` even if it is omitted from exclusions.

## Required secret

`GH_RWD_PACKAGE_TOKEN` must be able to read and delete packages associated with the
service repository (`read:packages` and `delete:packages`). The workflow declares
`contents: read`; package access is provided by this secret.

The pinned `container-package-cleanup` action discovers organization packages and
limits processing to packages linked to the repository running the workflow.

## Rollout and existing garbage

Updating this template does not update copies already installed in service
repositories. Copy `workflow-templates/cleanup-old-docker-container.yaml` to each
service repository's `.github/workflows/cleanup-old-docker-container.yaml`, or use
the `container_cleanup_workflow` section of the broadcast configuration to prepare
updates through the existing broadcast workflow.

For each target repository:

1. Run the updated workflow manually with `dry-run: true`.
2. Check that the report retains its actual LTS snapshot aliases and `latest`.
3. Run with `dry-run: false` to remove existing eligible versions, or wait for the
   weekly schedule. The default seven-day grace period still applies.

Do not run this template in `Netcracker/.github` expecting organization-wide
cleanup: package discovery is scoped to the repository executing the action.
