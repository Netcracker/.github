# Qubership GitHub Workflow Templates

In this repository in folder [workflow-templates](./workflow-templates/) you can find GitHub Actions workflow templates for common CI/CD, release, and automation tasks across Qubership and Netcracker repositories. These templates help standardize and accelerate automation for various languages and use cases.

## Available Workflow Templates

| Workflow Name                | Description                                                                                 | Typical Use Case / Trigger                | Workflow File |
|------------------------------|---------------------------------------------------------------------------------------------|-------------------------------------------|---------------|
| **Automatic PR Labeler**     | Automatically label PRs based on conventional commit messages. <br>Requires a [auto-labeler-config.yaml](./config/examples/auto-labeler-config.yaml) config file in the `.github` folder | On PR events                              | [automatic-pr-labeler.yaml](./workflow-templates/automatic-pr-labeler.yaml) |
| **CDXGen**                   | Generate SBOM (Software Bill of Materials) and vulnerability scan report                    | On push to main, manual trigger           | [cdxgen.yaml](./workflow-templates/cdxgen.yaml) |
| **Check Go Modules Licenses** | Check the licenses of Go modules in the repository using a configurable allowlist. <br>Fails if any module has a disallowed or missing license. <br>Requires a [.wwhrd.yml](./config/examples/.wwhrd.yml) config file in the repository root. | On push | [check-license.yaml](./workflow-templates/check-license.yaml) |
| **CLA Assistant**            | Check if PR authors have signed the Contributor License Agreement                           | On PR events                              | [cla.yaml](./workflow-templates/cla.yaml) |
| **Cleanup Old Docker**       | Clean up old Docker container versions in GitHub Packages                                   | Scheduled (cron), manual trigger          | [cleanup-old-docker-container.yaml](./workflow-templates/cleanup-old-docker-container.yaml) |
| **Dependency Review**        | Analyze new and updated dependencies for vulnerabilities, license issues, and OpenSSF Scorecard results on PRs and manual runs. | On pull request, manual trigger           | [dependency-review.yaml](./workflow-templates/dependency-review.yaml) |
| **Dev Docker Build**         | Build and publish Docker images for development, supports dry-run and custom tags. <br>Can be configured by [.github/docker-build-config.json](./config/examples/docker-build-config.json) file. [More info](https://github.com/Netcracker/qubership-workflow-hub/tree/main/actions/docker-action#example-configuration) | Manual trigger (workflow_dispatch)        | [dev-docker-build.yml](./workflow-templates/dev-docker-build.yml) |
| **Dev Maven Docker Build**   | Development build for Maven projects, with Docker image build and artifact publishing       | Manual trigger (workflow_dispatch)        | [dev-mvn-docker-build.yml](./workflow-templates/dev-mvn-docker-build.yml) |
| **Docker Release**           | Build and publish Docker images to GitHub Container Registry, create GitHub release         | On push to main, manual trigger           | [docker-release.yaml](./workflow-templates/docker-release.yaml) |
| **Go Build**                 | Build and test Go projects, upload coverage to SonarCloud                                   | On push to main, on pull request          | [go-build.yaml](./workflow-templates/go-build.yaml) |
| **Helm Charts Release**      | Release Helm charts and Docker images, create GitHub release. <br>Requires a lot of configuration. Please read workflow file comments.<br>Configuration examples:<br>[.github/helm-charts-release-config.yaml](./config/examples/helm-charts-release-config.yaml)<br>[.github/docker-build-config.json](./config/examples/docker-build-config.json)<br>[.github/release-drafter-config.yml](./config/examples/release-drafter-config.yml) | Manual trigger (workflow_dispatch)        | [helm-charts-release.yaml](./workflow-templates/helm-charts-release.yaml) |
| **Link Checker**             | Check Markdown files for broken links using lychee                                          | On push, manual trigger                   | [link-checker.yaml](./workflow-templates/link-checker.yaml) |
| **Lint Codebase**           | Lint codebase using GitHub Super-Linter. Runs multiple linters on changed files for supported languages. <br>See [.github/super-linter.env](.github/super-linter.env) and [.github/linters/](.github/linters/) for configuration. | On push, pull request, manual trigger     | [super-linter.yaml](./workflow-templates/super-linter.yaml) |
| **Maven Release v2**         | Enhanced Maven release with dry-run, Docker build, and GitHub release support. <br>Requires `pom.xml` [configuration](https://github.com/Netcracker/qubership-workflow-hub/blob/main/docs/maven-publish-pom-preparation_doc.md) and [.github/release-drafter-config.yml](./config/examples/release-drafter-config.yml) config file. | Manual trigger (workflow_dispatch)        | [maven-release-v2.yaml](./workflow-templates/maven-release-v2.yaml) |
| **Maven Release**            | Release and upload Java artifacts to Maven Central or GitHub Packages, create GitHub release | Manual trigger (workflow_dispatch)        | [maven-release.yaml](./workflow-templates/maven-release.yaml) |
| **Maven Snapshot Deploy**    | Deploy Maven snapshot artifacts to GitHub Packages or Maven Central                         | On push to non-main/non-release branches  | [maven-snapshot-deploy.yaml](./workflow-templates/maven-snapshot-deploy.yaml) |
| **PR Assigner**              | Automatically assign reviewers to PRs based on config or CODEOWNERS                        | On PR events                              | [pr-assigner.yml](./workflow-templates/pr-assigner.yml) |
| **PR Conventional Commits**  | Check if PR commits follow conventional commit messages                                     | On PR events                              | [pr-conventional-commits.yaml](./workflow-templates/pr-conventional-commits.yaml) |
| **PR Lint Title**            | Lint PR titles to ensure they follow conventional commit strategy                           | On PR events                              | [pr-lint-title.yaml](./workflow-templates/pr-lint-title.yaml) |
| **Profanity Filter**         | Check PRs, issues, and comments for profanity                                               | On PR/issue/comment events                | [profanity-filter.yaml](./workflow-templates/profanity-filter.yaml) |
| **NPM Publish**              | Publish npm packages to GitHub Packages or npm registry, supports Lerna monorepos            | Manual trigger (workflow_dispatch)        | [npm-publish.yaml](./workflow-templates/npm-publish.yaml) |
| **Python Release**           | Publish Python packages to PyPI and create GitHub release                                   | Manual trigger (workflow_dispatch)        | [python-release.yaml](./workflow-templates/python-release.yaml) |
| **Scorecard supply-chain security** | Generates and optionaly publishes OSSF scorecard of the repository | On push to `main` and weekly schedule | [ossf-scorecard.yaml](./workflow-templates/ossf-scorecard.yaml) |
| **SBOM to Release**          | Generate SBOM and upload it as a GitHub Release asset                                       | On release, manual trigger                | [sbom-to-release.yaml](./workflow-templates/sbom-to-release.yaml) |

## How to Use

1. **Copy the desired workflow YAML file** from this folder into your repository's `.github/workflows/` directory.
2. **Review and update required secrets and configuration files** as described in the comments at the top of each workflow file. Example config files are available in `config/examples/`.
3. **Customize input parameters** (such as version, tags, or build options) as needed for your project.
4. **Commit and push** the workflow to your repository.

## Configuration Examples
- Example configuration files for release drafter, Docker build, assets, and auto-labeler are available in `config/examples/`.
- Some workflows require secrets (e.g., `PYPI_API_TOKEN`, `MAVEN_USER`, `GITHUB_TOKEN`) to be set in your repository or organization.

## References
- [Qubership Workflow Hub Documentation](https://github.com/netcracker/qubership-workflow-hub)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

---
For questions or improvements, please open an issue or PR in this repository.
