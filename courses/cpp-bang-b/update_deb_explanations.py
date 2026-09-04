#!/usr/bin/env python3
"""
Update De_Bai.md with pedagogical explanations for Volume 2 problems.
"""
import os, re, json, sys
from pathlib import Path

# Add script directory to sys.path
sys.path.insert(0, str(Path(__file__).parent))
from stage3_explanations_data import EXPLANATIONS

def run():
    base_dir = Path(__file__).parent
    json_path = base_dir / "q2_problems_full.json"
    with open(json_path, "r", encoding="utf-8") as f:
        probs = json.load(f)

    updated_count = 0
    for p in probs:
        code = p["code"]
        exp = EXPLANATIONS.get(code)
        if not exp:
            continue
        
        deb_path = Path(p["dir"]) / "De_Bai.md"
        with open(deb_path, "r", encoding="utf-8") as f:
            content = f.read()

        if "### Giải thích" in content:
            continue

        # Regex to locate the Output code block of Sample 1
        pattern = re.compile(r"(###\s*Output\s*\n```(?:text)?\s*[\s\S]*?```)", re.MULTILINE)
        m = pattern.search(content)
        if m:
            matched_output = m.group(1)
            replacement = matched_output + "\n\n### Giải thích\n" + exp
            new_content = content[:m.start()] + replacement + content[m.end():]
            with open(deb_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            updated_count += 1

    print(f"Updated {updated_count} / {len(probs)} De_Bai.md files with pedagogical explanations.")

if __name__ == "__main__":
    run()
