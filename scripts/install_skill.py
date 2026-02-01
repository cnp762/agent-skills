#!/usr/bin/env python3
"""
Skill Installer - Installs a skill from this repository into a target project.

Usage:
    python3 scripts/install_skill.py <skill-name> --target <target-path>

Example:
    python3 scripts/install_skill.py react-patterns --target ../my-agent/.agent/skills
"""

import sys
import shutil
import argparse
from pathlib import Path

def install_skill(skill_name, target_path):
    # Locate the skill in the current repository
    repo_root = Path(__file__).resolve().parent.parent
    source_skill_path = repo_root / 'skills' / skill_name

    if not source_skill_path.exists():
        print(f"❌ Error: Skill '{skill_name}' not found in {repo_root}/skills")
        return False

    # Define target destination
    target_dir = Path(target_path).resolve()
    destination_path = target_dir / skill_name

    # Check if destination already exists
    if destination_path.exists():
        print(f"⚠️  Warning: Skill '{skill_name}' already exists at {destination_path}")
        response = input("Do you want to overwrite it? (y/N): ").strip().lower()
        if response != 'y':
            print("Installation cancelled.")
            return False
        shutil.rmtree(destination_path)

    try:
        # Copy the skill directory
        shutil.copytree(source_skill_path, destination_path)
        print(f"✅ Successfully installed '{skill_name}' to {destination_path}")
        
        # Verify structure
        if not (destination_path / 'SKILL.md').exists():
            print("⚠️  Warning: SKILL.md missing in installed skill (source might be corrupt)")
        
        return True
    except Exception as e:
        print(f"❌ Error installing skill: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Install a skill from the agent-skills repository.")
    parser.add_argument("skill_name", help="Name of the skill to install")
    parser.add_argument("--target", required=True, help="Target directory to install the skill into")
    
    args = parser.parse_args()
    
    print(f"📦 Installing skill: {args.skill_name}")
    success = install_skill(args.skill_name, args.target)
    
    if success:
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
