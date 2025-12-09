# npm Release

## Overview

The npm Release workflow is designed to be triggered manually via `workflow_dispatch` with configurable input parameters. It performs a comprehensive npm package release process including tag validation, testing, git tag creation, package publishing to npm registry, and GitHub release creation.

## Trigger

This workflow is triggered manually via `workflow_dispatch` with configurable input parameters.

## Workflow Details

### Jobs

#### `check-tag`
- **Runner**: `ubuntu-latest`
- **Purpose**: Validates that the release tag does not already exist to prevent duplicate releases
- **Condition**: Only runs if not in dry-run mode (`!inputs.dry-run`)
- **Uses**: `netcracker/qubership-workflow-hub/actions/tag-checker@v1.0.7`

#### `npm-test`
- **Runner**: `ubuntu-latest` (via reusable workflow)
- **Purpose**: Performs a dry-run test of the npm package publishing process
- **Dependencies**: Requires `check-tag` job completion
- **Uses**: `Netcracker/qubership-workflow-hub/.github/workflows/re-npm-publish.yml@v2.0.5`
- **Condition**: Always runs regardless of previous job status

#### `npm-publish`
- **Runner**: `ubuntu-latest` (via reusable workflow)
- **Purpose**: Publishes the npm package to the registry
- **Dependencies**: Requires `npm-test` job completion
- **Condition**: Only runs if not in dry-run mode (`!inputs.dry-run`)
- **Uses**: `Netcracker/qubership-workflow-hub/.github/workflows/re-npm-publish.yml@v2.0.5`

#### `tag`
- **Runner**: `ubuntu-latest` (via reusable workflow)
- **Purpose**: Creates a git tag for the release
- **Dependencies**: Requires `npm-publish` job completion
- **Condition**: Only runs if not in dry-run mode (`!inputs.dry-run`)
- **Uses**: `netcracker/qubership-workflow-hub/.github/workflows/tag-creator.yml@v1.0.7`

#### `github-release`
- **Runner**: `ubuntu-latest` (via reusable workflow)
- **Purpose**: Creates a GitHub release from the git tag
- **Dependencies**: Requires `tag` job completion
- **Condition**: Only runs if not in dry-run mode (`!inputs.dry-run`)
- **Uses**: `netcracker/qubership-workflow-hub/.github/workflows/release-drafter.yml@v2.0.5`

### Workflow Sequence

1. **Tag Validation** → **Package Test** → **Publishing** → **Tag Creation** → **Release Creation**

In dry-run mode:
- Only tag validation and package test are executed
- No publishing, tagging, or release creation occurs

## Delegated Tasks

The workflow delegates the actual npm publishing process to the `re-npm-publish.yml` workflow from the `qubership-workflow-hub` repository, which performs:

1. Repository checkout
2. Node.js environment setup
3. Dependency installation
4. Lerna monorepo detection (if applicable)
5. Dependency updates (if required)
6. Package version updates in package.json or lerna.json
7. Project build
8. Test execution
9. Changes commit and push
10. Package publishing to npm registry

## Configuration

### Required Input Parameters
- `version` (string, required): Release version for npm (e.g., 1.0.0)

### Optional Input Parameters
- `scope` (string, optional): npm scope for the package (default: "@netcracker")
- `node-version` (string, optional): Node.js version to use (default: "22.x")
- `registry-url` (string, optional): npm registry URL (default: "https://npm.pkg.github.com")
- `update-nc-dependency` (boolean, optional): Update @netcracker dependencies (default: false)
- `dry-run` (boolean, optional): Run in dry-run mode without actual publishing (default: false)
- `npm-dist-tag` (string, optional): npm distribution tag (default: "latest")

### Permissions
- `contents: write` - For creating git tags and GitHub releases
- `packages: write` - For publishing npm packages to the registry

### Environment Variables
- `GITHUB_TOKEN` - Used for GitHub API operations and npm authentication

## Prerequisites

Before using this workflow, you need to:

1. **Adjust package.json**
   - Ensure proper project configuration
   - Set up scopes and registry information if using scoped packages

2. **Create GitHub release configuration**
   - Add or configure release drafter configuration file
   - This is used by the release creation step

3. **Review qubership-workflow-hub documentation**
   - See: https://github.com/netcracker/qubership-workflow-hub?tab=readme-ov-file#npm-project-release-workflow
   - Contains detailed npm project release workflow instructions

## Usage

### Production Release

1. Trigger the workflow manually from GitHub Actions
2. Provide the release version (e.g., 1.0.0)
3. Configure optional parameters as needed
4. Leave `dry-run` as `false` (default)
5. Workflow will:
   - Validate the tag doesn't exist
   - Run tests in dry-run mode
   - Publish the package to npm
   - Create a git tag
   - Create a GitHub release

### Dry-Run Testing

1. Trigger the workflow manually from GitHub Actions
2. Set `dry-run` to `true`
3. Provide any desired parameters
4. Workflow will:
   - Validate the tag (if specified)
   - Run tests without publishing
   - Report results without creating tags or releases
   - Useful for validating the release process

### Monorepo Projects

For Lerna monorepos:

1. Ensure the project is properly configured as a Lerna monorepo
2. Set `update-nc-dependency` to `true` if needed to update @netcracker dependencies
3. The workflow will automatically detect and handle Lerna configuration

## Features

- **Tag validation**: Prevents duplicate releases by checking for existing tags
- **Dry-run support**: Test the entire release process without publishing
- **Comprehensive testing**: Runs tests before publishing to ensure quality
- **Monorepo support**: Automatically detects and handles Lerna monorepos
- **Scoped packages**: Supports @netcracker scoped packages
- **Distribution tags**: Allows setting custom npm distribution tags
- **GitHub integration**: Creates releases automatically after publishing
- **Manual control**: Manually triggered for precise release management
- **Dependency management**: Can update @netcracker dependencies during release

## Important Notes

- This workflow is designed for **production releases** and should be triggered manually when ready to publish
- Version parameter is required for production releases
- In dry-run mode, no actual publishing, tagging, or release creation occurs
- Duplicate release prevention is handled by tag validation
- All operations are logged in the GitHub Actions workflow summary

## Categories
- Node.js
- npm
- Automation
- Release Management

## Labels
- npm
- release
- node
- publishing
- automation
