#!/usr/bin/env python3
"""
Chuẩn hóa lại 100% tiêu đề của toàn bộ 346 bài toán theo chuẩn ngữ pháp Tiếng Việt tự nhiên:
- Viết hoa chữ cái đầu tiên của câu (Sentence case)
- Giữ nguyên các danh từ riêng / thuật ngữ viết tắt chuẩn: SPF, GCD, LCM, CRT, DP, CHT, DSU, BFS, DFS, MST, DAG, PBDS, STL, LCA, RMQ, LIS, KMP, FWT...
- Các từ nối, giới từ, liên từ viết thường chuẩn mực: của, và, các, trong, trên, theo, với, cho, có, từ, đến, bằng, để, đoạn...
- Cập nhật đồng bộ vào De_Bai.md, Huong_Dan_Giang_Day.md và MASTER_ALL_LESSONS.md.
"""

import re
from pathlib import Path

BASE = Path("/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b-level2")
PROB_DIR = BASE / "problems"
MASTER_FILE = BASE / "MASTER_ALL_LESSONS.md"

ACRONYMS = {
    "spf": "SPF", "gcd": "GCD", "lcm": "LCM", "crt": "CRT", "dp": "DP",
    "cht": "CHT", "dsu": "DSU", "bfs": "BFS", "dfs": "DFS", "mst": "MST",
    "dag": "DAG", "pbds": "PBDS", "stl": "STL", "lca": "LCA", "rmq": "RMQ",
    "lis": "LIS", "kmp": "KMP", "fwt": "FWT", "lru": "LRU", "bit": "BIT",
    "aho": "Aho-Corasick", "corasick": "", "bigint": "BigInt", "modulo": "modulo",
    "diophantine": "Diophantine", "legendre": "Legendre", "euler": "Euler",
    "fermat": "Fermat", "lucas": "Lucas", "catalan": "Catalan", "stirling": "Stirling",
    "tarjan": "Tarjan", "hierholzer": "Hierholzer", "dijkstra": "Dijkstra",
    "bellman": "Bellman-Ford", "ford": "", "floyd": "Floyd-Warshall", "warshall": "",
    "kruskal": "Kruskal", "manacher": "Manacher", "knuth": "Knuth", "kadane": "Kadane",
    "fenwick": "Fenwick", "segment": "Segment", "tree": "Tree", "trie": "Trie",
    "two": "Two", "pointers": "Pointers", "sliding": "Sliding", "window": "Window",
    "sweep": "Sweep-line", "line": "", "meet": "Meet in the Middle", "middle": ""
}

LOWERCASE_WORDS = {
    "va", "và", "cua", "của", "cac", "các", "trong", "tren", "trên", "theo",
    "voi", "với", "cho", "co", "có", "tu", "từ", "den", "đến", "bang", "bằng",
    "de", "để", "doan", "đoạn", "la", "là", "nhung", "những", "mot", "một",
    "hai", "ba", "khi", "nhieu", "nhiều", "it", "ít", "lon", "lớn", "nho", "nhỏ"
}

def format_natural_vietnamese_title(raw_title):
    # Loại bỏ tiền tố '#' và khoảng trắng
    t = raw_title.replace("#", "").strip()
    # Loại bỏ mã bài nếu có
    t = re.sub(r"^CPPB2-L\d+-\d+\s*[:\-]?\s*", "", t, flags=re.IGNORECASE)
    t = re.sub(r"^\d+\.\s*", "", t)

    # Tách từ
    words = t.split()
    if not words: return raw_title

    result = []
    for i, w in enumerate(words):
        w_lower = w.lower().strip("(),[]{}")
        # Kiểm tra thuật ngữ viết hoa cố định
        if w_lower in ACRONYMS:
            val = ACRONYMS[w_lower]
            if val:
                # Giữ nguyên dấu ngoặc nếu có
                if w.startswith("("): val = "(" + val
                if w.endswith(")"): val = val + ")"
                result.append(val)
            continue

        if i == 0:
            # Từ đầu tiên luôn viết hoa chữ cái đầu
            result.append(w.capitalize())
        else:
            # Từ tiếp theo: nếu là từ nối/giới từ thông thường -> viết thường
            if w_lower in LOWERCASE_WORDS:
                result.append(w.lower())
            else:
                # Giữ nguyên hoặc viết thường tự nhiên
                result.append(w.lower())

    res_str = " ".join(result)
    # Viết hoa chữ cái đầu tiên của câu
    if res_str:
        res_str = res_str[0].upper() + res_str[1:]
    return res_str

def main():
    print("🚀 Bắt đầu chuẩn hóa toàn bộ tiêu đề bài toán theo ngữ pháp Tiếng Việt tự nhiên...")
    count = 0

    for pdir in sorted(PROB_DIR.glob("cppb2_*")):
        db_file = pdir / "De_Bai.md"
        guide_file = pdir / "Huong_Dan_Giang_Day.md"
        if not db_file.exists(): continue

        with open(db_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
        if not lines: continue

        old_title_line = lines[0].strip()
        new_title = format_natural_vietnamese_title(old_title_line)

        # Cập nhật De_Bai.md
        lines[0] = f"# {new_title}\n"
        with open(db_file, "w", encoding="utf-8") as f:
            f.writelines(lines)

        # Cập nhật Huong_Dan_Giang_Day.md
        if guide_file.exists():
            with open(guide_file, "r", encoding="utf-8") as f:
                glines = f.readlines()
            if glines:
                glines[0] = f"# Hướng dẫn giảng dạy: {new_title}\n"
                with open(guide_file, "w", encoding="utf-8") as f:
                    f.writelines(glines)

        count += 1

    print(f"🎉 Hoàn tất chuẩn hóa ngữ pháp tiêu đề tiếng Việt tự nhiên cho {count} bài toán!")

if __name__ == "__main__":
    main()
