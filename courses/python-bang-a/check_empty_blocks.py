import glob, re, os

empty_inputs = []
empty_outputs = []

for f in sorted(glob.glob('courses/python-bang-a/problems/*/De_Bai.md')):
    content = open(f, encoding='utf-8').read()
    if '### Input' in content and '### Output' in content:
        m = re.search(r'### Input\s*```[a-z]*\s*(.*?)\s*```\s*### Output\s*```[a-z]*\s*(.*?)\s*```', content, re.DOTALL)
        if m:
            inp = m.group(1)
            out = m.group(2)
            if not inp.strip() and not ('Không có' in content or 'Không cần' in content):
                empty_inputs.append(f)
            if not out.strip():
                empty_outputs.append(f)

print(f"Empty inputs without 'Không có': {len(empty_inputs)}")
for e in empty_inputs[:10]:
    print(" ", e)
print(f"Empty outputs: {len(empty_outputs)}")
for e in empty_outputs[:10]:
    print(" ", e)
