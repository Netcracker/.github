# Netcracker/.github Repository - GitHub Copilot Instructions

This is the Netcracker organization's GitHub repository that provides workflow templates and configurations for Qubership and Netcracker projects. It contains over 30 reusable GitHub Actions workflow templates for CI/CD, release automation, and repository management.

**ALWAYS follow these instructions first and only fall back to additional search or bash commands when the information here is incomplete or found to be in error.**

## Working Effectively

### Repository Structure and Purpose
- `workflow-templates/`: 30+ GitHub Actions workflow templates with accompanying `.properties.json` files
- `.github/workflows/`: Actual workflows running on this repository (linting, link checking, etc.)
- `config/examples/`: Configuration file examples for various workflows  
- `docs/workflows/`: Documentation for each workflow template
- `.github/linters/`: Linter configuration files (markdownlint, yamllint, actionlint)

### Primary Validation and Testing Commands

**NEVER CANCEL builds or validation commands. Set timeouts to 120+ seconds minimum.**

#### YAML Linting (Required for all YAML changes)
```bash
# Test individual YAML file - takes 0.1-0.3 seconds
yamllint -c .github/linters/.yaml-lint.yml path/to/file.yaml

# Test all workflow templates - takes 0.3-0.5 seconds, NEVER CANCEL
yamllint -c .github/linters/.yaml-lint.yml workflow-templates/*.yaml

# Test actual workflows - takes 0.1-0.2 seconds  
yamllint -c .github/linters/.yaml-lint.yml .github/workflows/*.yaml

# Comprehensive YAML validation - takes 4-5 seconds, NEVER CANCEL, set timeout to 120+ seconds
find . -name "*.yaml" -o -name "*.yml" | xargs -I {} yamllint -c .github/linters/.yaml-lint.yml {}
```

#### Markdown Linting (Required for documentation changes)
```bash
# Install markdownlint-cli if not available
npm install -g markdownlint-cli

# Test README.md - takes 0.3 seconds
markdownlint -c .github/linters/.markdownlint.json README.md

# Test all documentation - takes 0.5 seconds, reports style issues but workflow continues
markdownlint -c .github/linters/.markdownlint.json docs/workflows/*.md
```

#### GitHub Actions Workflow Linting (Required for workflow changes)
```bash
# Download and install actionlint (if not available)
curl -sSLO https://github.com/rhysd/actionlint/releases/download/v1.7.1/actionlint_1.7.1_linux_amd64.tar.gz
tar xf actionlint_1.7.1_linux_amd64.tar.gz actionlint
chmod +x actionlint

# Test workflow templates - takes 0.1 seconds, may report shellcheck issues
./actionlint -config-file .github/linters/actionlint.yml workflow-templates/*.yaml

# Test actual workflows - takes 0.1 seconds
./actionlint -config-file .github/linters/actionlint.yml .github/workflows/*.yaml
```

#### Link Checking (Required when modifying documentation)
```bash
# Download and install lychee (if not available)
curl -sSL https://github.com/lycheeverse/lychee/releases/download/v0.15.1/lychee-v0.15.1-x86_64-unknown-linux-gnu.tar.gz | tar xz
chmod +x lychee

# Check all markdown files - takes 1-2 seconds, NEVER CANCEL, set timeout to 180+ seconds
# External links may fail due to network restrictions - this is expected
./lychee --base . --verbose --no-progress './**/*.md' --accept 100..=103,200..=299,429
```

#### JSON Validation (Required for workflow template properties)
```bash
# Validate all .properties.json files - takes 0.1 seconds
find workflow-templates/ -name "*.properties.json" | xargs -I {} python3 -m json.tool {} > /dev/null

# Validate specific JSON file
python3 -m json.tool workflow-templates/example.properties.json > /dev/null
```

### Complete Validation Workflow (Run before any commit)

**NEVER CANCEL these validation steps. Set timeout to 300+ seconds for the complete process.**

```bash
# Step 1: YAML validation (4-5 seconds)
find . -name "*.yaml" -o -name "*.yml" | xargs -I {} yamllint -c .github/linters/.yaml-lint.yml {}

# Step 2: Markdown validation (0.5 seconds) 
markdownlint -c .github/linters/.markdownlint.json README.md docs/workflows/*.md

# Step 3: Workflow validation (0.2 seconds)
./actionlint -config-file .github/linters/actionlint.yml workflow-templates/*.yaml .github/workflows/*.yaml

# Step 4: Link checking (1-2 seconds) - may show network errors for external links
./lychee --base . --verbose --no-progress './**/*.md' --accept 100..=103,200..=299,429

# Step 5: JSON validation (0.1 seconds)
find workflow-templates/ -name "*.properties.json" | xargs -I {} python3 -m json.tool {} > /dev/null
```

## Manual Validation Requirements

### After Making Changes to Workflow Templates
1. **Syntax Validation**: Run yamllint and actionlint on modified templates
2. **JSON Structure Check**: Verify `.properties.json` file exists and is valid JSON using `python3 -m json.tool`
3. **Documentation Update**: Update corresponding file in `docs/workflows/` if template behavior changes
4. **Cross-Reference Validation**: Check that examples in `config/examples/` match template requirements

### After Making Documentation Changes  
1. **Link Validation**: Run lychee to check for broken internal references
2. **Markdown Linting**: Run markdownlint to ensure consistent formatting
3. **Content Accuracy**: Manually verify that documented commands and configurations are accurate

### Repository-Wide Validation
1. Run complete validation workflow (all 5 steps above)
2. Check that all workflow templates have corresponding documentation
3. Verify configuration examples are up-to-date with template changes

## Key Constraints and Limitations

### What Works
- YAML, Markdown, and GitHub Actions workflow validation
- Link checking for internal repository references  
- Template syntax and structure validation
- Documentation formatting checks

### What Has Known Issues
- **External link checking**: Network restrictions cause some external URLs to fail - this is expected
- **YAML indentation warnings**: Some workflow templates have indentation warnings that are acceptable
- **Shellcheck warnings**: actionlint reports shellcheck issues that are often acceptable in GitHub Actions context

### Expected Timing and Timeouts
- **Individual file validation**: 0.1-0.5 seconds
- **Complete repository validation**: 4-6 seconds total
- **Link checking**: 1-2 seconds
- **ALWAYS set timeout to minimum 120 seconds** for any validation command
- **NEVER CANCEL** validation processes even if they seem slow

## Common Validation Scenarios

### Adding a New Workflow Template
1. Create `.yaml` file in `workflow-templates/`
2. Create corresponding `.properties.json` file and validate with `python3 -m json.tool`
3. Add documentation in `docs/workflows/`
4. Run complete validation workflow (all 5 steps)
5. Verify template follows organization patterns

### Modifying Existing Templates
1. Edit template file
2. Update documentation if behavior changes  
3. Run yamllint and actionlint on specific file
4. Test any referenced configuration examples
5. Run complete validation before commit

### Documentation Updates
1. Edit markdown files
2. Run markdownlint on modified files
3. Run lychee link checker  
4. Verify code examples and commands are accurate

## File Structure Reference

### Root Directory
```
.
├── README.md                 # Main repository documentation
├── workflow-templates/       # 30+ workflow templates with .properties.json
├── .github/workflows/        # Repository's own workflows  
├── config/examples/          # Configuration file examples
├── docs/workflows/           # Template documentation
├── .github/linters/          # Linter configurations
├── CODEOWNERS               # Code ownership rules
└── LICENSE                  # Apache 2.0 license
```

### Critical Configuration Files
- `.github/linters/.markdownlint.json`: Markdown style rules
- `.github/linters/.yaml-lint.yml`: YAML formatting rules  
- `.github/linters/actionlint.yml`: GitHub Actions workflow rules
- `.github/super-linter.env`: Super-linter environment configuration

**CRITICAL REMINDER**: This repository contains templates and documentation, not application code. The "build" process is validation and linting. Focus on template syntax correctness and documentation accuracy rather than traditional compilation or runtime testing.