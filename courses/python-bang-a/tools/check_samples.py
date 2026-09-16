import glob, re

missing_sample_pya = []
for f in sorted(glob.glob('courses/python-bang-a/problems/*/De_Bai.md')):
    content = open(f, encoding='utf-8').read()
    sample_match = re.search(r'### Input\s*```[a-z]*\s*(.*?)\s*```\s*### Output\s*```[a-z]*\s*(.*?)\s*```', content, re.DOTALL)
    if not sample_match or not sample_match.group(1).strip() or not sample_match.group(2).strip():
        missing_sample_pya.append(f)

print(f'Total problems missing valid Sample 1: {len(missing_sample_pya)}')
for p in missing_sample_pya:
    print(p)
