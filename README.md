# Agent Skills Collection

A centralized library of **Agent Skills** designed to enhance AI capabilities. This repository follows the [Anthropic Skills Standard](https://github.com/anthropics/skills) and allows you to easily create, validate, and share skills.

## 📂 Structure

The repository is organized into a comprehensive [SKILLS_CATALOG.md](SKILLS_CATALOG.md), covering:
- **Standard Skills**: Core technical and workflow skills (e.g., `react-patterns`, `api-design`).
- **Growth & Marketing**: Skills for CRO, SEO, copywriting, and psychology.
- **Anthropic Official**: Verified skills from Anthropic (e.g., `docx`, `pdf`, `skill-creator`).

All skills are located in the `skills/` directory.

## 🛠️ Creating New Skills

We provide standardized scripts to synthesize new skills quickly.

### 1. Initialize a New Skill
Use the initialization script to create a template following best practices:
```bash
python3 scripts/init_skill.py <skill-name> --path skills/
```
Example:
```bash
python3 scripts/init_skill.py data-analysis --path skills/
```
This creates:
- `skills/data-analysis/SKILL.md` (Template)
- `skills/data-analysis/scripts/` (For executable code)
- `skills/data-analysis/references/` (For docs/schemas)
- `skills/data-analysis/assets/` (For templates/files)

### 2. Validate Your Skill
Ensure your skill meets the structural requirements:
```bash
python3 scripts/quick_validate.py skills/<skill-name>
```

### 3. Package Your Skill
Create a distributable `.skill` file (zip archive):
```bash
python3 scripts/package_skill.py skills/<skill-name> [output-dir]
```

## 📦 Installation Workflow (For New Projects)

If you are starting a new project and want to use these skills:

1.  **Clone this repository** (e.g., as a submodule or tool library):
    ```bash
    git clone https://github.com/cnp762/agent-skills libs/agent-skills
    ```

2.  **Install Required Skills**:
    Use the `install_skill.py` script to copy specific skills into your project's active skill directory.
    ```bash
    # Syntax: python3 scripts/install_skill.py <skill-name> --target <your-project-skill-dir>
    
    python3 libs/agent-skills/scripts/install_skill.py react-patterns --target .agent/skills
    python3 libs/agent-skills/scripts/install_skill.py anthropic-frontend-design --target .agent/skills
    ```

    **What this does:**
    -   Copies the full skill folder (e.g., `react-patterns/`) to your target.
    -   Preserves the standard structure (`SKILL.md`, `scripts/`, `assets/`).
    -   Ensures you have a clean, standalone copy of the skill ready for your agent.

## 🚀 Usage

To equip an agent with a skill:

1.  **Copy**: Move the `skills/<skill-name>` folder to your agent's skill directory (e.g., `.agent/skills`).
2.  ** instruct**: Tell your agent to read `SKILLS_CATALOG.md` or the specific `SKILL.md` to understand its capabilities.

## 🔄 Synchronizing
Run `git pull origin main` to fetch the latest skills and updates.