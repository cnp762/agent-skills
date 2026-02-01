# Agent Skills Collection

This repository serves as a centralized collection of "Agent Skills".
The goal is to have a library of skills that can be easily imported or copied into various projects to enhance AI agent capabilities.

## Structure
Each skill should be contained in its own directory with a `SKILL.md` file describing how to use it.
Potential structure:
```
skills/
  ├── python-analysis/
  │   ├── SKILL.md
  │   └── ...
  ├── web-scraping/
  │   ├── SKILL.md
  │   └── ...
```

## Usage
To use a skill in your project:
1.  Navigate to the specific skill folder in this repository.
2.  Copy the `SKILL.md` and any associated scripts/resources to your project's `.agent/skills` (or equivalent) directory.
3.  Instruct your agent to read the `SKILL.md`.

## Synchronizing
Run `git pull origin main` to get the latest skills.