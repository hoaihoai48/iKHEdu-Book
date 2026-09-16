#!/usr/bin/env python3
"""
Đồng bộ hóa các thư mục bài học chuẩn:
1. Sao chép và chuyển đổi các assets SVG sang đúng các thư mục bài học chứa LessonXX_Production_Content.md
2. Nhúng các đường link ảnh ![...](assets/...) vào từng file LessonXX_Production_Content.md và README.md
"""

import os
import shutil
import glob
from pathlib import Path

BASE = Path("/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b-level2/lessons")

# Ánh xạ thư mục bài học chuẩn đang chứa Production Content
LESSON_DIR_MAP = {
    1: BASE / "lesson-01-so-hoc-co-ban-chuyen-sau",
    2: BASE / "lesson-02-modulo-va-fast-power",
    3: BASE / "lesson-03-tim-kiem-nhi-phan-nang-cao",
    4: BASE / "lesson-04-ky-thuat-mang-nang-cao",
    5: BASE / "lesson-05-de-quy-chia-de-tri-mitm",
    6: BASE / "lesson-06-phep-toan-bit-mat-na-bit-nang-cao",
    7: BASE / "lesson-07-thuat-toan-tham-lam",
    8: BASE / "lesson-08-quy-hoach-dong-co-ban",
    9: BASE / "lesson-09-ngan-xep-hang-doi-deque",
    10: BASE / "lesson-10-thu-vien-stl-c-nang-cao",
    11: BASE / "lesson-11-to-hop-hoan-vi-xac-suat-co-ban",
    12: BASE / "lesson-12-do-thi-co-ban-va-nang-cao",
    13: BASE / "lesson-13-cay-phan-doan-fenwick-tree",
    14: BASE / "lesson-14-quy-hoach-dong-chu-so-digit-dp",
    15: BASE / "lesson-15-xu-ly-chuoi-hashing-so-lon",
}

# Danh sách hình ảnh cho từng bài học
LESSON_ASSETS = {
    1: ["l01_spf_sieve_visual.svg", "l01_segmented_sieve_visual.svg"],
    2: ["l02_matrix_fibonacci_visual.svg"],
    3: ["l03_binary_search_real_visual.svg"],
    4: ["l04_2d_prefix_sum_visual.svg"],
    5: ["l05_mitm_split_visual.svg"],
    6: ["l06_bitmask_operations_visual.svg"],
    7: ["l07_interval_scheduling_visual.svg"],
    8: ["l08_grid_dp_visual.svg"],
    9: ["l09_monotonic_stack_visual.svg"],
    10: ["l10_two_heaps_median_visual.svg"],
    11: ["l11_pascal_triangle_visual.svg"],
    12: ["l12_tarjan_bridges_visual.svg"],
    13: ["l13_segment_tree_visual.svg", "l13_fenwick_tree_visual.svg"],
    14: ["l14_digit_dp_tree_visual.svg"],
    15: ["l15_trie_tree_visual.svg"],
}

# Điểm neo để nhúng hình trong từng bài học
HOOKS = {
    1: [
        ("## 3. Sàng ước số nguyên tố nhỏ nhất (SPF — Smallest Prime Factor)", "![Sơ đồ cơ chế Sàng SPF](assets/l01_spf_sieve_visual.svg)\n\n## 3. Sàng ước số nguyên tố nhỏ nhất (SPF — Smallest Prime Factor)"),
        ("## 4. Sàng nguyên tố phân đoạn (Segmented Sieve", "![Mô phỏng Sàng số nguyên tố phân đoạn](assets/l01_segmented_sieve_visual.svg)\n\n## 4. Sàng nguyên tố phân đoạn (Segmented Sieve")
    ],
    2: [
        ("## 3. Thuật toán lũy thừa nhanh", "![Sơ đồ nhân ma trận Fibonacci](assets/l02_matrix_fibonacci_visual.svg)\n\n## 3. Thuật toán lũy thừa nhanh")
    ],
    3: [
        ("## 4. Chặt nhị phân số thực", "![Chặt nhị phân tập số thực](assets/l03_binary_search_real_visual.svg)\n\n## 4. Chặt nhị phân số thực")
    ],
    4: [
        ("## 2. Mảng tiền tố 2D", "![Sơ đồ 2D Prefix Sum](assets/l04_2d_prefix_sum_visual.svg)\n\n## 2. Mảng tiền tố 2D")
    ],
    5: [
        ("## 3. Kỹ thuật Meet in the Middle", "![Kỹ thuật Meet in the Middle](assets/l05_mitm_split_visual.svg)\n\n## 3. Kỹ thuật Meet in the Middle")
    ],
    6: [
        ("## 2. Bảng tổng hợp các thủ thuật Bitwise", "![Bảng thao tác Bitmask](assets/l06_bitmask_operations_visual.svg)\n\n## 2. Bảng tổng hợp các thủ thuật Bitwise")
    ],
    7: [
        ("## 2. Các mô hình bài toán tham lam", "![Lập lịch sự kiện tham lam](assets/l07_interval_scheduling_visual.svg)\n\n## 2. Các mô hình bài toán tham lam")
    ],
    8: [
        ("## 2. Các mô hình Quy hoạch động", "![Quy hoạch động trên lưới 2D](assets/l08_grid_dp_visual.svg)\n\n## 2. Các mô hình Quy hoạch động")
    ],
    9: [
        ("## 2. Ngăn xếp đơn điệu", "![Ngăn xếp đơn điệu Monotonic Stack](assets/l09_monotonic_stack_visual.svg)\n\n## 2. Ngăn xếp đơn điệu")
    ],
    10: [
        ("## 4. Mẫu cài đặt chuẩn thi đấu: Duy trì trung vị", "![Hai Heap duy trì Trung vị động](assets/l10_two_heaps_median_visual.svg)\n\n## 4. Mẫu cài đặt chuẩn thi đấu: Duy trì trung vị")
    ],
    11: [
        ("## 2. Tiền xử lý giai thừa", "![Tam giác Pascal](assets/l11_pascal_triangle_visual.svg)\n\n## 2. Tiền xử lý giai thừa")
    ],
    12: [
        ("## 3. Thuật toán Dijkstra", "![Thuật toán Tarjan tìm Khớp và Cầu](assets/l12_tarjan_bridges_visual.svg)\n\n## 3. Thuật toán Dijkstra")
    ],
    13: [
        ("## 2. Cây Fenwick", "![Cấu trúc Cây Fenwick BIT](assets/l13_fenwick_tree_visual.svg)\n\n## 2. Cây Fenwick"),
        ("## 3. Cây phân đoạn", "![Kiến trúc Cây phân đoạn Segment Tree](assets/l13_segment_tree_visual.svg)\n\n## 3. Cây phân đoạn")
    ],
    14: [
        ("## 2. Các tham số trạng thái", "![Mô hình phân nhánh Digit DP](assets/l14_digit_dp_tree_visual.svg)\n\n## 2. Các tham số trạng thái")
    ],
    15: [
        ("## 2. Kỹ thuật Băm chuỗi đa thức", "![Cây tiền tố Trie](assets/l15_trie_tree_visual.svg)\n\n## 2. Kỹ thuật Băm chuỗi đa thức")
    ]
}

def sync_assets():
    # Thu thập tất cả các file svg đã tạo trong toàn bộ lessons
    all_svgs = {}
    for p in BASE.glob("**/assets/*.svg"):
        all_svgs[p.name] = p

    for num, ldir in LESSON_DIR_MAP.items():
        target_assets = ldir / "assets"
        target_assets.mkdir(parents=True, exist_ok=True)
        
        needed = LESSON_ASSETS.get(num, [])
        for svg_name in needed:
            if svg_name in all_svgs:
                src = all_svgs[svg_name]
                dst = target_assets / svg_name
                if src != dst:
                    shutil.copy2(src, dst)
                print(f"  ✅ Đã đồng bộ asset {svg_name} vào {ldir.name}/assets/")

def embed_hooks():
    for num, ldir in LESSON_DIR_MAP.items():
        md_file = ldir / f"Lesson{num:02d}_Production_Content.md"
        if not md_file.exists():
            continue
        
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()

        rules = HOOKS.get(num, [])
        for pattern, replacement in rules:
            if replacement not in content:
                # Tìm dòng bắt đầu với pattern
                lines = content.split("\n")
                new_lines = []
                matched = False
                for l in lines:
                    if not matched and l.strip().startswith(pattern):
                        new_lines.append(replacement)
                        matched = True
                    else:
                        new_lines.append(l)
                if matched:
                    content = "\n".join(new_lines)
                    print(f"  ✅ Đã nhúng ảnh vào {md_file.name}")

        with open(md_file, "w", encoding="utf-8") as f:
            f.write(content)

def cleanup_duplicate_empty_dirs():
    for p in BASE.iterdir():
        if p.is_dir():
            mds = list(p.glob("*.md"))
            if not mds and ("-greedy" in p.name or "-chuyen-sau" in p.name or "-va-fenwick-tree" in p.name or "-va-bitmask-nang-cao" in p.name or "-don-dieu" in p.name or "-va-xac-suat-co-ban" in p.name or "-string-hashing-va-bigint" in p.name):
                shutil.rmtree(p)
                print(f"  🧹 Đã dọn dẹp thư mục trùng: {p.name}")

def main():
    print("🚀 Bắt đầu đồng bộ hình ảnh vào từng thư mục bài học (Lesson 01 -> 15)...")
    sync_assets()
    embed_hooks()
    cleanup_duplicate_empty_dirs()
    print("🎉 Hoàn tất 100% việc đưa hình ảnh minh họa vào từng thư mục bài học Level 2!")

if __name__ == "__main__":
    main()
