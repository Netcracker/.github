# NPM Publish

## Overview

The NPM Publish workflow is designed to be triggered when a release is marked as a full release. It performs a comprehensive NPM package release process including dependency management, version updates, building, testing, and publishing to NPM registries.

## Trigger

This workflow is designed as a reusable workflow that can be called by other workflows with configurable input parameters.

## Workflow Details

### Jobs

#### `npm-build-publish`
- **Runner**: `ubuntu-latest`
- **Purpose**: Builds and publishes NPM packages with comprehensive version management
- **Environment**: Uses `GITHUB_TOKEN` for NPM authentication

### Steps

1. **Checkout repository**
   - Uses `actions/checkout@v4`
   - Checks out the repository code

2. **Show branch**
   - Displays the current branch information

3. **Setup Node.js**
   - Uses `actions/setup-node@v4`
   - Configures Node.js version and registry settings
   - Sets up scope for scoped packages

4. **Install dependencies**
   - Runs `npm ci --legacy-peer-deps`
   - Installs project dependencies

5. **Check if project is a Lerna monorepo**
   - Detects if the project uses Lerna for monorepo management
   - Sets environment variable for subsequent steps

6. **Update dependencies (if required)**
   - Updates @netcracker dependencies when specified
   - Only runs when `update-nc-dependency` is true

7. **Update package version**
   - Updates version in lerna.json (for Lerna projects)
   - Updates version in package.json (for standard NPM projects)

## Configuration

### Required Input Parameters
- `version` (string, required): Release version to publish

### Optional Input Parameters
- `scope` (string, optional): NPM scope (default: "@netcracker")
- `node-version` (string, optional): Node.js version (default: "22.x")
- `registry-url` (string, optional): NPM registry URL (default: "https://npm.pkg.github.com")
- `update-nc-dependency` (boolean, optional): Update @netcracker dependencies (default: false)
- `dist-tag` (string, optional): NPM distribution tag (default: "next")
- `branch_name` (string, optional): Branch name (default: "main")

### Permissions
- `contents: write` - For updating package files and committing changes
- `packages: write` - For publishing to NPM registries

## Usage

This workflow is particularly useful for:
- Publishing NPM packages to GitHub Packages or NPM registry
- Managing Lerna monorepo releases
- Automating version updates and dependency management
- Ensuring package quality through building and testing
- Supporting scoped package publishing

## Features

- **Lerna support**: Handles both standard NPM and Lerna monorepo projects
- **Dependency management**: Updates @netcracker dependencies when needed
- **Version management**: Automatically updates package versions
- **Multiple registries**: Supports GitHub Packages and NPM registry
- **Scoped packages**: Supports scoped package publishing
- **Distribution tags**: Configurable NPM distribution tags
- **Comprehensive testing**: Builds and tests before publishing

## Categories
- JavaScript
- Node.js
- Automation
- NPM

## Labels
- npm
- publish
- javascript
- nodejs
