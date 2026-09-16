#!/usr/bin/env python3
"""Gan lai P0-P3 theo do kho that (diem tu calibrate_levels), giu nguyen
kich thuoc tang (4/4/4/rest), sort bai tu de den kho trong Bai_Tap."""
from pathlib import Path
import re
import sys

BASE = Path(__file__).parent
sys.path.insert(0, str(BASE))
from calibrate_levels import score_solution

MAPPING = {1: ['l01'], 2: ['l02'], 3: ['l03'], 4: ['l04', 'l05', 'l06'],
           5: ['l07'], 6: ['l08'], 7: ['l09'], 8: ['l10'], 9: ['l11'],
           10: ['l12'], 11: ['l16'], 12: ['l17'], 13: ['l13'],
           14: ['l14', 'l15'], 15: ['l18']}
TITLES = {1: 'Bài 01', 2: 'Bài 02', 3: 'Bài 03',
          4: 'Bài 04: Rẽ nhánh và điều kiện logic',
          5: 'Bài 05: Vòng lặp for và hàm range',
          6: 'Bài 06: Vòng lặp while và biến cờ',
          7: 'Bài 07: Quy luật dãy số và tam giác số',
          8: 'Bài 08: Tách chữ số',
          9: 'Bài 09: Ước số, Bội số và Số nguyên tố',
          10: 'Bài 10: Đếm số theo quy luật và số đặc biệt',
          11: 'Bài 11: Danh sách (List) và thao tác cơ bản',
          12: 'Bài 12: Thống kê danh sách và sắp xếp',
          13: 'Bài 13: Chuỗi ký tự',
          14: 'Bài 14: Duyệt chuỗi và tách từ',
          15: 'Bài 15: Chiến lược giải đề thi'}


def parse_debai(p):
    t = (p / 'De_Bai.md').read_text(encoding='utf-8')

    def sec(name):
        m = re.search('## ' + name + r'\s*\n(.*?)(?=\n## |\Z)', t, re.S)
        return m.group(1).strip() if m else ''

    title = t.splitlines()[0].lstrip('# ').strip()
    sample = sec('Sample 1') if 'Sample 1' in t else sec('Sample')
    return {'title': title, 'boicanh': sec('Bối cảnh'),
            'nhiemvu': sec('Nhiệm vụ'), 'input': sec('Input'),
            'output': sec('Output'), 'sample': sample,
            'rangbuoc': sec('Ràng buộc'), 'code': p.name}


def tier_bounds(n):
    """Chia theo tu phan vi: P0/P1/P2 moi tang n//4 bai, con lai la P3."""
    q = n // 4
    return [q, 2 * q, 3 * q]


def level(idx, bounds):
    if idx < bounds[0]:
        return 'P0 (Khởi động)'
    if idx < bounds[1]:
        return 'P1 (Cơ bản)'
    if idx < bounds[2]:
        return 'P2 (Luyện tập)'
    return 'P3 (Vận dụng)'


for new, olds in MAPPING.items():
    dirs = []
    for o in olds:
        dirs += sorted((BASE / 'problems').glob('pya_' + o + '_*'))
    scored = []
    for d in dirs:
        src = (d / 'solution.py').read_text(encoding='utf-8')
        sc, _ = score_solution(src)
        scored.append((sc, d.name, d))
    scored.sort(key=lambda r: (r[0], r[1]))
    bt = BASE / ('lessons/lesson-%02d/Bai_Tap.md' % new)
    src = ', '.join(olds)
    n = len(scored)
    b = tier_bounds(n)
    out = ['# Danh Sách Bài Tập Thực Hành: ' + TITLES[new], '',
           '> Nguồn problems: ' + src + ' | Tổng %d bài (sắp từ dễ đến khó theo rubric độ khó).' % n, '',
           '## Ma Trận Phân Tầng',
           '* P0 (Khởi động): Bài 1-%d' % b[0],
           '* P1 (Cơ bản): Bài %d-%d' % (b[0] + 1, b[1]),
           '* P2 (Luyện tập): Bài %d-%d' % (b[1] + 1, b[2]),
           '* P3 (Vận dụng): Bài %d-%d' % (b[2] + 1, n),
           '---', '']
    for i, (sc, name, d) in enumerate(scored, 1):
        info = parse_debai(d)
        lvl = level(i - 1, b)
        short = lvl.split()[0]
        out += ['### Bài %d (%s): %s' % (i, short, info['title']),
                '* **Mã bài toán:** `%s`' % info['code'],
                '* **Độ khó:** %s' % lvl,
                '* **Bối cảnh:** %s' % info['boicanh'],
                '* **Nhiệm vụ:** %s' % info['nhiemvu'],
                '* **Input:** %s' % info['input'],
                '* **Output:** %s' % info['output'],
                '* **Sample:** %s' % info['sample'],
                '* **Ràng buộc:** %s' % info['rangbuoc'], '', '---', '']
    bt.write_text('\n'.join(out), encoding='utf-8')
    p0 = [s[1] for s in scored[:4]]
    p3 = [s[1] for s in scored[12:16]]
    print('L%02d n=%d | P0: %s | P3 dau: %s' % (new, n, p0, p3))
