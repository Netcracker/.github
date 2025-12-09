# Security Scan Docker Packages

## Overview

The Security Scan workflow performs comprehensive security vulnerability scanning on Docker packages in your repository. It supports both manual triggering via `workflow_dispatch` and automatic scheduled runs. The workflow can scan all Docker images in your GitHub Container Registry (GHCR) or a specific image, using multiple security scanning tools (Trivy and Grype) to identify vulnerabilities.

## Trigger

This workflow can be triggered in two ways:

1. **Manual trigger**: Via `workflow_dispatch` with configurable parameters
   - Allows scanning specific images or all images
   - Customizable severity levels, scanners, and error handling
   - Full control over scan parameters

2. **Scheduled trigger**: Automatically runs every Sunday at 03:00 UTC
   - Uses default parameter values
   - Scans all Docker images in the repository
   - Ideal for regular security checks

## Workflow Details

### Jobs

#### `debug-packages`
- **Runner**: `ubuntu-latest`
- **Purpose**: Discovers and lists all Docker packages in GHCR for the repository
- **Permissions**: `packages: read`
- **Uses**: `Netcracker/qubership-workflow-hub/actions/ghcr-discover-repo-packages@v2.0.5`
- **Outputs**:
  - `packages`: JSON array of discovered packages
  - `has-packages`: Boolean indicating if packages were found

### Steps (debug-packages)

1. **List GHCR packages for this repo**
   - Uses the ghcr-discover-repo-packages action
   - Discovers all Docker images available in GHCR
   - Sets output packages as JSON array

2. **Print packages**
   - Displays discovered packages in JSON format
   - Useful for debugging and visibility

3. **Continue only if repo has GHCR packages**
   - Validates that at least one package was found
   - Proceeds if packages exist

4. **No packages found, fail the job**
   - Fails the workflow if no GHCR packages are discovered
   - Prevents invalid scan attempts

#### `security-scan-matrix`
- **Runner**: `ubuntu-latest` (via reusable workflow)
- **Purpose**: Runs security scans on all discovered Docker packages in parallel
- **Dependencies**: Requires `debug-packages` job
- **Condition**: Only runs if no specific image is provided (`inputs.image == '' || inputs.image == null`)
- **Strategy**: Matrix strategy iterates through all discovered packages
- **Uses**: `netcracker/qubership-workflow-hub/.github/workflows/re-security-scan.yml@v2.0.5`

#### `security-scan-single`
- **Runner**: `ubuntu-latest` (via reusable workflow)
- **Purpose**: Runs security scan on a specific Docker image
- **Dependencies**: Requires `debug-packages` job
- **Condition**: Only runs if a specific image is provided (`inputs.image != '' && inputs.image != null`)
- **Uses**: `netcracker/qubership-workflow-hub/.github/workflows/re-security-scan.yml@v2.0.5`

### Workflow Execution Logic

The workflow uses conditional logic to choose between two scanning modes:

- **Matrix Mode**: Automatically scans all discovered Docker images when no specific image is provided
- **Single Image Mode**: Scans a specific image when the `image` parameter is provided

## Configuration

### Optional Input Parameters

#### Scan Target
- `target` (choice, optional): Target type for the scan
  - Options: `docker`, `source`
  - Default: `docker`

#### Image Configuration
- `image` (string, optional): Docker image to scan
  - Format: `ghcr.io/<owner>/<repo>:tag`
  - Default: Empty (scans all repository images)
- `tag` (string, optional): Tag of the image to scan
  - Default: `latest`

#### Severity and Coverage
- `only-high-critical` (boolean, optional): Scope only HIGH and CRITICAL severity vulnerabilities
  - Default: `true`

#### Scanner Selection
- `trivy-scan` (boolean, optional): Enable Trivy vulnerability scanner
  - Default: `true`
- `grype-scan` (boolean, optional): Enable Grype vulnerability scanner
  - Default: `true`

#### Error Handling
- `continue-on-error` (boolean, optional): Continue workflow execution even if scan detects vulnerabilities
  - Default: `true`

#### Vulnerability Filtering
- `only-fixed` (boolean, optional): Ignore unfixed vulnerabilities in scan results
  - Default: `true`

### Permissions
- `packages: read` - For reading Docker packages from GHCR

### Environment Variables
- `GH_TOKEN`: GitHub access token (uses `secrets.GH_ACCESS_TOKEN`)

### Schedule
- Runs automatically every **Sunday at 03:00 UTC**

## Usage

### Scan All Docker Images

1. Trigger the workflow manually from GitHub Actions
2. Leave all parameters at default values
3. Leave `image` parameter empty
4. Workflow will:
   - Discover all Docker images in GHCR
   - Scan each image in parallel using matrix strategy
   - Use Trivy and Grype scanners
   - Report only HIGH and CRITICAL vulnerabilities
   - Ignore unfixed vulnerabilities

### Scan Specific Docker Image

1. Trigger the workflow manually from GitHub Actions
2. Provide the `image` parameter (e.g., `ghcr.io/netcracker/myrepo/myimage`)
3. Optionally customize other parameters:
   - `tag`: Specify image tag (default: `latest`)
   - `trivy-scan`: Enable/disable Trivy
   - `grype-scan`: Enable/disable Grype
4. Workflow will scan only the specified image with your configurations

### Full Vulnerability Scan

1. Trigger the workflow manually
2. Set `only-high-critical` to `false` to include all severity levels
3. Set `only-fixed` to `false` to include unfixed vulnerabilities
4. Workflow will report all detected vulnerabilities

### Fail on Vulnerabilities

1. Trigger the workflow manually
2. Set `continue-on-error` to `false`
3. If vulnerabilities matching the criteria are found, workflow will fail
4. Useful for blocking deployments with security issues

### Scheduled Weekly Scan

- Workflow automatically runs every Sunday at 03:00 UTC
- Scans all Docker images with default parameters
- No manual intervention required
- Results available in GitHub Actions history

## Features

- **Multi-scanner support**: Uses both Trivy and Grype for comprehensive coverage
- **Automatic discovery**: Finds all Docker images in repository GHCR
- **Batch scanning**: Scans multiple images in parallel using matrix strategy
- **Specific image scanning**: Optionally scan individual images
- **Severity filtering**: Filter by HIGH/CRITICAL or view all vulnerabilities
- **Fixed vulnerabilities handling**: Option to ignore or include unfixed vulnerabilities
- **Flexible error handling**: Choose to fail or continue on vulnerability detection
- **Scheduled runs**: Automatic weekly security scans
- **Manual control**: Manually trigger scans with custom parameters
- **Detailed reporting**: JSON output of discovered packages and scan results

## Prerequisites

Before using this workflow, ensure:

1. **Docker images are published to GHCR**
   - Images must be available in GitHub Container Registry
   - Must be in the same repository

2. **GitHub Token with appropriate permissions**
   - `GH_ACCESS_TOKEN` secret must be configured
   - Token needs `packages: read` permission

## Delegated Tasks

The workflow delegates actual vulnerability scanning to the `re-security-scan.yml` reusable workflow from the `qubership-workflow-hub` repository, which:

1. Sets up and configures security scanning tools
2. Pulls the specified Docker image from GHCR
3. Runs Trivy vulnerability scanner (if enabled)
4. Runs Grype vulnerability scanner (if enabled)
5. Filters results by severity and fix status
6. Reports findings

## Important Notes

- **No GHCR packages**: If no Docker images are found in GHCR, the workflow fails during the `debug-packages` job
- **Matrix vs Single**: Only one scanning job runs (either matrix or single image mode)
- **Default parameters**: Matrix mode uses hardcoded defaults when triggered by schedule
- **Token requirements**: Ensure `GH_ACCESS_TOKEN` has sufficient permissions
- **Parallel execution**: Multiple images are scanned in parallel for efficiency
- **Scheduled runs**: Use default parameters during scheduled execution; customize by manually triggering

## Output

The workflow provides:

- **Package discovery**: List of all Docker images found in GHCR
- **Vulnerability reports**: Detailed findings from Trivy and Grype scanners
- **Step summaries**: GitHub Actions step summaries for each scan
- **Matrix job logs**: Individual logs for each scanned image

## Categories
- Security
- Docker
- Automation
- Vulnerability Scanning

## Labels
- security
- docker
- scanning
- vulnerability
- automation
- trivy
- grype
