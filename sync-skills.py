import os
import shutil
import json
import filecmp

REPO_DIR = "/Users/bb/code/pr-purgatory/Skills"
CONFIG_PLUGIN_DIR = "/Users/bb/.gemini/config/plugins/pr-purgatory-skills"
ANTIGRAVITY_SKILLS_DIR = "/Users/bb/.gemini/antigravity/skills"
GEMINI_SKILLS_DIR = "/Users/bb/.gemini/skills"

ACTIVE_SKILLS = [
    "archie",
    "deep-research-firecrawl",
    "lfm",
    "redteam",
    "revert-forge",
    "rust-forge",
    "sandbox-forge",
    "selina",
    "ui-forge",
    "provenance",
]

PRUNED_SKILLS = [
    "babel-smith",
    "bridge-builder",
    "context-janitor",
    "dependency-janitor",
    "deploy-forge",
    "doc-forge",
    "forge-master",
    "noise-filter",
    "perf-profiler",
    "refactor-forge",
    "schema-audit",
    "schema-smith",
    "smoke-tester",
    "success-forge",
    "telemetry-eye",
    "test-sentry",
    "vibe-check",
]

def sync_dir(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    # ignore .DS_Store and __pycache__
    def ignore_patterns(dir, files):
        return [f for f in files if f == ".DS_Store" or f == "__pycache__"]
    shutil.copytree(src, dst, ignore=ignore_patterns)

def run_sync():
    print("--- 1. Validating Active Skills in Repo ---")
    for skill in ACTIVE_SKILLS:
        skill_path = os.path.join(REPO_DIR, skill)
        skill_md = os.path.join(skill_path, "SKILL.md")
        agent_md = os.path.join(skill_path, "AGENT.md")
        assert os.path.isdir(skill_path), f"Missing {skill_path}"
        assert os.path.isfile(skill_md), f"Missing {skill_md}"
        assert os.path.isfile(agent_md), f"Missing {agent_md}"
        print(f"  OK: {skill} has SKILL.md and AGENT.md")

    print("\n--- 2. Syncing Config Plugin (pr-purgatory-skills) ---")
    plugin_skills_dir = os.path.join(CONFIG_PLUGIN_DIR, "skills")
    plugin_agents_dir = os.path.join(CONFIG_PLUGIN_DIR, "agents")
    os.makedirs(plugin_skills_dir, exist_ok=True)
    os.makedirs(plugin_agents_dir, exist_ok=True)

    # Sync skills
    for skill in ACTIVE_SKILLS:
        src = os.path.join(REPO_DIR, skill)
        dst = os.path.join(plugin_skills_dir, skill)
        sync_dir(src, dst)
        print(f"  Synced skill -> {dst}")

    # Remove pruned/inactive skills from plugin_skills_dir
    for item in os.listdir(plugin_skills_dir):
        if item not in ACTIVE_SKILLS and (item in PRUNED_SKILLS or item.startswith(".")):
            path = os.path.join(plugin_skills_dir, item)
            if os.path.isdir(path):
                shutil.rmtree(path)
                print(f"  Removed pruned skill from plugin: {item}")
            elif os.path.isfile(path) and item.startswith("."):
                os.remove(path)

    # Sync agents
    for skill in ACTIVE_SKILLS:
        src = os.path.join(REPO_DIR, skill)
        dst = os.path.join(plugin_agents_dir, skill)
        sync_dir(src, dst)
        print(f"  Synced agent -> {dst}")

    # Remove pruned/inactive agents from plugin_agents_dir
    for item in os.listdir(plugin_agents_dir):
        if item not in ACTIVE_SKILLS and (item in PRUNED_SKILLS or item.startswith(".")):
            path = os.path.join(plugin_agents_dir, item)
            if os.path.isdir(path):
                shutil.rmtree(path)
                print(f"  Removed pruned agent from plugin: {item}")
            elif os.path.isfile(path) and item.startswith("."):
                os.remove(path)

    # Update plugin manifest & version
    plugin_json_path = os.path.join(CONFIG_PLUGIN_DIR, "plugin.json")
    with open(plugin_json_path, "w") as f:
        json.dump({
            "name": "pr-purgatory-skills",
            "version": "1.1.0",
            "description": "Custom skills and subagents for PR Purgatory workspace",
            "author": {
                "name": "Antigravity Agent"
            },
            "license": "MIT"
        }, f, indent=2)
    print("  Updated plugin.json to v1.1.0")

    installed_ver_path = os.path.join(CONFIG_PLUGIN_DIR, "installed_version.json")
    with open(installed_ver_path, "w") as f:
        json.dump({"version": "1.1.0"}, f, indent=2)
    print("  Updated installed_version.json to v1.1.0")

    print("\n--- 3. Syncing ~/.gemini/antigravity/skills ---")
    if os.path.exists(ANTIGRAVITY_SKILLS_DIR):
        for skill in ACTIVE_SKILLS:
            src = os.path.join(REPO_DIR, skill)
            dst = os.path.join(ANTIGRAVITY_SKILLS_DIR, skill)
            sync_dir(src, dst)
            print(f"  Synced -> {dst}")
        for item in os.listdir(ANTIGRAVITY_SKILLS_DIR):
            if item in PRUNED_SKILLS:
                path = os.path.join(ANTIGRAVITY_SKILLS_DIR, item)
                if os.path.isdir(path):
                    shutil.rmtree(path)
                    print(f"  Removed pruned skill from antigravity: {item}")

    print("\n--- 4. Syncing ~/.gemini/skills ---")
    if os.path.exists(GEMINI_SKILLS_DIR):
        for skill in ACTIVE_SKILLS:
            src = os.path.join(REPO_DIR, skill)
            dst = os.path.join(GEMINI_SKILLS_DIR, skill)
            sync_dir(src, dst)
            print(f"  Synced -> {dst}")
        for item in os.listdir(GEMINI_SKILLS_DIR):
            if item in PRUNED_SKILLS:
                path = os.path.join(GEMINI_SKILLS_DIR, item)
                if os.path.isdir(path):
                    shutil.rmtree(path)
                    print(f"  Removed pruned skill from gemini: {item}")

    print("\n--- Sync Complete ---")

if __name__ == "__main__":
    run_sync()

