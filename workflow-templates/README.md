# Qubership GitHub Workflow Templates

This folder contains reusable GitHub Actions workflow templates for common CI/CD, release, and automation tasks across Qubership and Netcracker repositories. These templates help standardize and accelerate automation for various languages and use cases.

## Available Workflow Templates

| Workflow Name                | Description                                                                                 | Typical Use Case / Trigger                |
|------------------------------|---------------------------------------------------------------------------------------------|-------------------------------------------|
| **Maven Release**            | Release and upload Java artifacts to Maven Central or GitHub Packages, create GitHub release | Manual trigger (workflow_dispatch)        |
| **Maven Release v2**         | Enhanced Maven release with dry-run, Docker build, and GitHub release support               | Manual trigger (workflow_dispatch)        |
| **Maven Snapshot Deploy**    | Deploy Maven snapshot artifacts to GitHub Packages or Maven Central                         | On push to non-main/non-release branches  |
| **Dev Maven Docker Build**   | Development build for Maven projects, with Docker image build and artifact publishing       | Manual trigger (workflow_dispatch)        |
| **Dev Docker Build**         | Build and publish Docker images for development, supports dry-run and custom tags           | Manual trigger (workflow_dispatch)        |
| **Docker Release**           | Build and publish Docker images to GitHub Container Registry, create GitHub release         | On push to main, manual trigger           |
| **Helm Charts Release**      | Release Helm charts and Docker images, create GitHub release                                | Manual trigger (workflow_dispatch)        |
| **Python Release**           | Publish Python packages to PyPI and create GitHub release                                   | Manual trigger (workflow_dispatch)        |
| **Go Build**                 | Build and test Go projects, upload coverage to SonarCloud                                   | On push to main, on pull request          |
| **CDXGen**                   | Generate SBOM (Software Bill of Materials) and vulnerability scan report                    | On push to main, manual trigger           |
| **SBOM to Release**          | Generate SBOM and upload it as a GitHub Release asset                                       | On release, manual trigger                |
| **Link Checker**             | Check Markdown files for broken links using lychee                                          | On push, manual trigger                   |
| **Cleanup Old Docker**       | Clean up old Docker container versions in GitHub Packages                                   | Scheduled (cron), manual trigger          |
| **Automatic PR Labeler**     | Automatically label PRs based on conventional commit messages                               | On PR events                              |
| **PR Assigner**              | Automatically assign reviewers to PRs based on config or CODEOWNERS                        | On PR events                              |
| **PR Lint Title**            | Lint PR titles to ensure they follow conventional commit strategy                           | On PR events                              |
| **PR Conventional Commits**  | Check if PR commits follow conventional commit messages                                     | On PR events                              |
| **Profanity Filter**         | Check PRs, issues, and comments for profanity                                               | On PR/issue/comment events                |
| **CLA Assistant**            | Check if PR authors have signed the Contributor License Agreement                           | On PR events                              |

## How to Use

1. **Copy the desired workflow YAML file** from this folder into your repository's `.github/workflows/` directory.
2. **Review and update required secrets and configuration files** as described in the comments at the top of each workflow file. Example config files are available in `config/examples/`.
3. **Customize input parameters** (such as version, tags, or build options) as needed for your project.
4. **Commit and push** the workflow to your repository.

## Configuration Examples
- Example configuration files for release drafter, Docker build, assets, and auto-labeler are available in `config/examples/`.
- Some workflows require secrets (e.g., `PYPI_API_TOKEN`, `MAVEN_USER`, `GITHUB_TOKEN`) to be set in your repository or organization.

## Template Metadata
Each workflow has an accompanying `.properties.json` file describing its purpose, categories, and labels. Review these files for more details.

## References
- [Qubership Workflow Hub Documentation](https://github.com/netcracker/qubership-workflow-hub)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

---
For questions or improvements, please open an issue or PR in this repository.
