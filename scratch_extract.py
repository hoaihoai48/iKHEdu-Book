import re, glob, os

lesson_files = sorted(glob.glob('/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b-level2/lessons/**/Lesson*.md'))
all_declared = []

for lf in lesson_files:
    content = open(lf, 'r', encoding='utf-8').read()
    matches = re.findall(r'\|\s*\d+\s*\|\s*`(CPPB2-L\d+-\d+)`\s*\|\s*\*\*([^*]+)\*\*\s*\|\s*`([^`]+)`\s*\|\s*([^|]+)\|\s*([^|]+)\|', content)
    for m in matches:
        code, title, level, constraints, goal = m
        all_declared.append({
            'code': code.strip(),
            'title': title.strip(),
            'level': level.strip(),
            'constraints': constraints.strip(),
            'goal': goal.strip(),
            'lesson': os.path.basename(os.path.dirname(lf))
        })

print(f"Total extracted: {len(all_declared)}")
for x in all_declared[:5]:
    print(x)
