import os

problems_dir = "courses/scratch-bang-a/problems"
problems = sorted(os.listdir(problems_dir))

count = 0
for p in problems:
    hd_path = os.path.join(problems_dir, p, "Huong_Dan_Giang_Day.md")
    if os.path.exists(hd_path):
        txt = open(hd_path, encoding="utf-8").read()
        if "```python" in txt:
            count += 1

print(f"Total problems with python code: {count} / {len(problems)}")
