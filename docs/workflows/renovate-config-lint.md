# Renovate configuration and health check

## Overview

This workflow validates `renovate.json`, resolves shared presets, checks dependency lookups, and reports Renovate health
failures as a GitHub issue.

## Requirements

- Add `renovate.json` to the repository root.
- For repositories that run Renovate, enable the Mend Renovate Community app and the Dependency Dashboard with its
  default `Dependency Dashboard` title.
- Enable GitHub Issues and allow GitHub Actions to create issues with the repository `GITHUB_TOKEN` for Dashboard and
  incident reporting. The workflow provides limited reporting in its run summary when Issues are disabled.

If a repository intentionally does not run Renovate, set the Actions variable `RENOVATE_HEALTH_CHECK` to `false`.
Dependency lookup and health monitoring stop, while configuration validation continues on changes and on the weekly
schedule. Close any existing `Renovate health check failed` issue manually after setting the variable.

## Triggers

- Changes to `renovate.json` or `.github/workflows/renovate-config-lint.yaml` validate the configuration.
- A weekly schedule validates the configuration, looks up dependencies, and checks the Dependency Dashboard.
- `workflow_dispatch` runs the same complete health check on demand.

## Jobs

### Validate Renovate configuration

The validation job runs the strict Renovate configuration validator and resolves shared presets. It reports invalid
configuration, unavailable presets, GitHub API rate limits, and nonzero Renovate exit codes.

### Look up dependencies

The lookup job runs `renovate --platform=local --dry-run=lookup`. It retries lookup-only failures once with a fresh
cache and reports persistent lookup failures, rate limits, error records, and command failures.

### Monitor Renovate health

The monitor checks the hosted Dependency Dashboard for repository problems, errored updates, and dependency lookup
failures. It creates one `Renovate health check failed` issue with links to the failed health-check run and the
Dependency Dashboard.

If GitHub Issues are disabled, the workflow skips Dashboard and incident-issue operations. Validation and dependency
lookup still run, and their failures remain visible in the workflow run.

Repeated failures add a comment with the latest run instead of creating another issue. A successful check adds a
recovery comment and closes the managed issue automatically.

## Schedule

Replace the example cron value with one stable Monday slot between 06:00 and 10:59 UTC. To derive the slot, hash
`owner/repository` with SHA-256, convert the first eight hexadecimal characters to an integer, and take the result
modulo 300. The quotient divided by 60 selects the hour after 06:00, and the remainder selects the minute.

When assigning schedules to multiple repositories, move a colliding result to the next free minute in the window.

The schedule runs from the default branch. GitHub Actions can delay scheduled workflows during periods of high load.

## Permissions

- Validation and dependency lookup jobs use `contents: read`.
- The monitor job uses `contents: read` and `issues: write`.
- Pull request workflows do not run the issue-writing monitor.

## Verification

1. Change `renovate.json` in a pull request and confirm that `Validate renovate.json` succeeds.
1. Run `Validate Renovate Config` manually from the Actions tab on the default branch.
1. Confirm that validation, dependency lookup, and health monitoring succeed.
1. Open the Dependency Dashboard and confirm that it has no repository problems or lookup failures.
