import os
import re
from pathlib import Path

problems_dir = Path("courses/scratch-bang-a/problems")
problems = sorted([p for p in problems_dir.iterdir() if p.is_dir()])

py_in_hd = []
py_keywords = ["print(", "map(int", ".split()", "int(câu trả lời)", "Python", "```python"]

for p in problems:
    hd_path = p / "Huong_Dan_Giang_Day.md"
    if hd_path.exists():
        txt = hd_path.read_text(encoding="utf-8")
        found = []
        for kw in py_keywords:
            if kw in txt:
                found.append(kw)
        if re.search(r'\b\w+\s*//\s*\w+', txt):
            found.append("//")
        if re.search(r'\b\w+\s*%\s*\w+', txt):
            found.append("%")
        if found:
            py_in_hd.append((p.name, found))

print(f"Total problems: {len(problems)}")
print(f"Problems with Python keywords or syntax: {len(py_in_hd)} / {len(problems)}")
print("\nSample 15 problems with Python elements:")
for name, found in py_in_hd[:15]:
    print(f"  - {name}: {found}")
