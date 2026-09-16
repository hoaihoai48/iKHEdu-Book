#!/usr/bin/env python3
"""Cham diem do kho that cua tung problem de gan lai P0-P3.

Rubric (cang cao = cang kho):
  inputs   : so luong input() (doc nhieu dong kho hon)
  split    : +2 neu dung split/map (tach dong)
  decisions: moi if/elif/else +3, long nhau (nested) +3 them
  loops    : moi for/while +4, long nhau +4, break/continue/flag +2
  arith    : moi toan tu so hoc +1; //, %, **, round/lam tron +2
  calls    : string/list methods (split/join/upper/append/sort/...) +2 moi loai
  outfmt   : sep/end/f-string/format +2; nhieu print +1/print
  steps    : so dong logic (gan/tinh) +0.5/dong
  cond     : and/or/not +1 moi cai
"""
from pathlib import Path
import ast
import re

BASE = Path(__file__).parent


def score_solution(src):
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return 99.0, {'parse-error': True}
    s = 0.0
    f = {}

    class V(ast.NodeVisitor):
        def __init__(self):
            self.depth = 0
            self.maxdepth = 0

        def generic_visit(self, node):
            if isinstance(node, (ast.If, ast.For, ast.While)):
                self.depth += 1
                self.maxdepth = max(self.maxdepth, self.depth)
                super().generic_visit(node)
                self.depth -= 1
            else:
                super().generic_visit(node)

    v = V()
    v.visit(tree)
    inputs = src.count('input()')
    decisions = len([n for n in ast.walk(tree) if isinstance(n, (ast.If,))])
    boolops = sum(len(n.values) - 1 for n in ast.walk(tree)
                  if isinstance(n, ast.BoolOp))
    loops = len([n for n in ast.walk(tree)
                 if isinstance(n, (ast.For, ast.While))])
    breaks = len([n for n in ast.walk(tree)
                  if isinstance(n, (ast.Break, ast.Continue))])
    arith = len([n for n in ast.walk(tree)
                 if isinstance(n, (ast.BinOp,))])
    floordiv = src.count('//') + src.count('%') + src.count('**')
    calls = [n.func.attr for n in ast.walk(tree)
             if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)]
    strlist_calls = len(set(calls) & {'split', 'join', 'upper', 'lower',
                                      'append', 'pop', 'remove', 'sort',
                                      'isdigit', 'isalpha', 'strip',
                                      'replace', 'find', 'count', 'extend',
                                      'insert', 'reverse', 'strip'})
    prints = src.count('print(')
    fmt = (('sep=' in src) + ('end=' in src) + ('f"' in src or "f'" in src)
           + ('.2f' in src or ':.2f' in src or 'round(' in src))
    has_map = 'map(' in src
    lines = len([l for l in src.splitlines()
                 if l.strip() and not l.strip().startswith('#')])

    s += inputs * 1.0
    s += has_map * 2.0
    s += decisions * 3.0
    s += boolops * 1.0
    s += loops * 4.0 + max(0, v.maxdepth - 1) * 3.0
    s += breaks * 2.0
    s += arith * 1.0 + floordiv * 1.0
    s += strlist_calls * 2.0
    s += prints * 0.5 + fmt * 2.0
    s += lines * 0.3
    f.update({'in': inputs, 'if': decisions, 'andor': boolops,
              'loop': loops, 'nest': v.maxdepth, 'arith': arith,
              'calls': strlist_calls, 'fmt': fmt, 'lines': lines})
    return round(s, 1), f


if __name__ == '__main__':
    import collections
    MAPPING = {1: ['l01'], 2: ['l02'], 3: ['l03'], 4: ['l04', 'l05', 'l06'],
               5: ['l07'], 6: ['l08'], 7: ['l09'], 8: ['l10'], 9: ['l11'],
               10: ['l12'], 11: ['l16'], 12: ['l17'], 13: ['l13'],
               14: ['l14', 'l15'], 15: ['l18']}
    for new, olds in MAPPING.items():
        rows = []
        for o in olds:
            for d in sorted((BASE / 'problems').glob('pya_' + o + '_*')):
                src = (d / 'solution.py').read_text(encoding='utf-8')
                sc, feat = score_solution(src)
                rows.append((sc, d.name, feat))
        rows.sort()
        print('=== L%02d (n=%d) de nhat: %s | kho nhat: %s'
              % (new, len(rows), rows[0][:2], rows[-1][:2]))
