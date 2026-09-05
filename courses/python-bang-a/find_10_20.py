import glob, re

found = []
for deb in sorted(glob.glob('courses/python-bang-a/problems/*/De_Bai.md')):
    c = open(deb, encoding='utf-8').read()
    if '### Input' in c and '### Output' in c:
        m = re.search(r'### Input\s*\n```[^\n]*\n(.*?)\n```\s*\n### Output\s*\n```[^\n]*\n(.*?)\n```', c, re.DOTALL)
        if m:
            inp = m.group(1).strip()
            out = m.group(2).strip()
            if inp == '10' and out == '20':
                found.append(deb)

print(f"Total De_Bai with 10/20 sample: {len(found)}")
for f in found:
    print(f)
