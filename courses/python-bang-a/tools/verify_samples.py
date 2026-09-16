#!/usr/bin/env python3
"""Verify moi solution.py chay dung Sample 1 trong De_Bai.md."""
from pathlib import Path
import re
import subprocess

BASE = Path(__file__).parent


def parse_sample(debai):
    t = debai.read_text(encoding='utf-8')
    m = re.search(r'## Sample 1\s+### Input\s+```text\n(.*?)```\s+'
                  r'### Output\s+```text\n(.*?)```', t, re.S)
    if not m:
        return None
    return m.group(1).strip('\n'), m.group(2).strip('\n')


ok, fail, nosample = [], [], []
for d in sorted((BASE / 'problems').iterdir()):
    if not d.is_dir():
        continue
    s = parse_sample(d / 'De_Bai.md')
    if s is None:
        nosample.append(d.name)
        continue
    inp, out = s
    try:
        r = subprocess.run(['python3', str(d / 'solution.py')],
                           input=(inp + '\n' if inp else ''),
                           capture_output=True, text=True, timeout=10)

        def norm(s):
            return '\n'.join(l.rstrip() for l in s.split('\n')).strip('\n')

        got = norm(r.stdout)
        want = norm(out)
        if r.returncode == 0 and got == want:
            ok.append(d.name)
        else:
            fail.append((d.name, inp, want, got, r.stderr.strip()[:200]))
    except subprocess.TimeoutExpired:
        fail.append((d.name, inp, out, 'TIMEOUT', ''))

print('PASS: %d | FAIL: %d | NO-SAMPLE: %d' % (len(ok), len(fail), len(nosample)))
for name, inp, out, got, err in fail:
    print('--- FAIL', name)
    print('  in :', repr(inp))
    print('  exp:', repr(out))
    print('  got:', repr(got))
    if err:
        print('  err:', err)
for n in nosample:
    print('NO-SAMPLE:', n)
