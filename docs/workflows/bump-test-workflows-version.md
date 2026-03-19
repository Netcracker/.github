# Bump qubership-test-pipelines version

## Purpose

This workflow automatically bumps references to `netcracker/qubership-test-pipelines` in all `.github/workflows/*.yaml` workflow files to the latest release commit SHA, and updates `pipeline_branch` to the same SHA value.

It is useful to keep downstream workflow definitions aligned with the latest test-pipeline version and avoid manual PR churn.

## Trigger

- `on: workflow_dispatch` (manual run)

## Required permissions

In `jobs.bump.permissions`:

- `contents: write`
- `pull-requests: write`

The run also requires a PAT in repository secrets with:

- `GH_ACCESS_TOKEN` containing `contents: write` and `workflows: write`.

## Job: `bump`

Runs on:
- `ubuntu-latest`

### Steps

1. **Get latest release tag SHA**
   - `curl` latest release from:
     - `https://api.github.com/repos/netcracker/qubership-test-pipelines/releases/latest`
   - resolves tag name and tag object SHA into:
     - `latest_release_tag`
     - `latest_release_tag_sha`
   - stores in `GITHUB_ENV`

2. **Checkout**
   - `uses: actions/checkout@v6`
   - `ref: main`
   - `persist-credentials: true`
   - `token: ${{ secrets.GH_ACCESS_TOKEN }}`

3. **Update version**
   - env `GH_TOKEN: ${{ github.token }}`
   - config Git user:
     - `github-actions[bot]@qubership.com`
     - `Git Hub Actions [Bot]`
   - For each workflow file under `./.github/workflows` containing `uses: netcracker/qubership-test-pipelines`:
     - update `uses: ... @<sha>` plus comment `# <tag>`
     - update `pipeline_branch: '<sha>'`
   - If `git status` shows changes:
     - branch `feature/bump-test-pipelines-version-<timestamp>`
     - commit message:
       - `chore: bump netcracker/qubership-test-pipelines version to '<sha>' [<tag>]`
     - push branch
     - create PR:
       - via `gh pr create --base main --head <branch> --title ... --body ...`
   - Else:
     - prints `No changes.`

## Notes

- The workflow uses the release tag's Git object SHA, not the tag name, as version pin.
- It ensures both `uses: ...` and `pipeline_branch:` are updated in sync.
- Requires `gh` CLI auth context in runner.
