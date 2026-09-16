#!/usr/bin/env python3
"""
Nhúng các đường link hình ảnh ![...](assets/...) vào các bài học trong MASTER_ALL_LESSONS.md
"""

from pathlib import Path
import re

BASE_DIR = Path("/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b-level2")
MASTER_FILE = BASE_DIR / "MASTER_ALL_LESSONS.md"

def main():
    with open(MASTER_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Nhúng hình vào các bài học tương ứng
    replacements = [
        # Lesson 01
        ("## 3. Sàng ước số nguyên tố nhỏ nhất (SPF — Smallest Prime Factor)",
         "![Sơ đồ cơ chế Sàng SPF](lessons/lesson-01-so-hoc-co-ban-chuyen-sau/assets/l01_spf_sieve_visual.svg)\n\n## 3. Sàng ước số nguyên tố nhỏ nhất (SPF — Smallest Prime Factor)"),
        
        ("## 4. Sàng nguyên tố phân đoạn (Segmented Sieve): Vượt qua ranh giới $10^9$",
         "![Mô phỏng Sàng số nguyên tố phân đoạn](lessons/lesson-01-so-hoc-co-ban-chuyen-sau/assets/l01_segmented_sieve_visual.svg)\n\n## 4. Sàng nguyên tố phân đoạn (Segmented Sieve): Vượt qua ranh giới $10^9$"),

        # Lesson 02
        ("## 4. Nhân ma trận & Ứng dụng giải hệ thức truy hồi tuyến tính",
         "![Sơ đồ nhân ma trận Fibonacci](lessons/lesson-02-modulo-va-fast-power/assets/l02_matrix_fibonacci_visual.svg)\n\n## 4. Nhân ma trận & Ứng dụng giải hệ thức truy hồi tuyến tính"),

        # Lesson 03
        ("## 3. Chặt nhị phân trên tập số thực (Real Binary Search)",
         "![Chặt nhị phân tập số thực](lessons/lesson-03-tim-kiem-nhi-phan-nang-cao/assets/l03_binary_search_real_visual.svg)\n\n## 3. Chặt nhị phân trên tập số thực (Real Binary Search)"),

        # Lesson 04
        ("## 4. Kỹ thuật Mảng cộng dồn 2D (2D Prefix Sum)",
         "![Sơ đồ 2D Prefix Sum](lessons/lesson-04-ky-thuat-mang-nang-cao/assets/l04_2d_prefix_sum_visual.svg)\n\n## 4. Kỹ thuật Mảng cộng dồn 2D (2D Prefix Sum)"),

        # Lesson 05
        ("## 4. Kỹ thuật Phân đôi tập hợp (Meet in the Middle — MITM)",
         "![Kỹ thuật Meet in the Middle](lessons/lesson-05-de-quy-chia-de-tri-mitm/assets/l05_mitm_split_visual.svg)\n\n## 4. Kỹ thuật Phân đôi tập hợp (Meet in the Middle — MITM)"),

        # Lesson 06
        ("## 2. Các thao tác Bitmask cơ bản & nâng cao",
         "![Bảng thao tác Bitmask](lessons/lesson-06-phep-toan-bit-va-bitmask-nang-cao/assets/l06_bitmask_operations_visual.svg)\n\n## 2. Các thao tác Bitmask cơ bản & nâng cao"),

        # Lesson 07
        ("## 3. Bài toán Lập lịch sự kiện (Interval Scheduling)",
         "![Lập lịch sự kiện tham lam](lessons/lesson-07-thuat-toan-tham-lam-greedy/assets/l07_interval_scheduling_visual.svg)\n\n## 3. Bài toán Lập lịch sự kiện (Interval Scheduling)"),

        # Lesson 08
        ("## 3. Quy hoạch động trên Lưới 2D (Grid DP)",
         "![Quy hoạch động trên lưới 2D](lessons/lesson-08-quy-hoach-dong-co-ban-va-chuyen-sau/assets/l08_grid_dp_visual.svg)\n\n## 3. Quy hoạch động trên Lưới 2D (Grid DP)"),

        # Lesson 09
        ("## 3. Ngăn xếp đơn điệu (Monotonic Stack): Tìm phần tử lớn hơn gần nhất",
         "![Ngăn xếp đơn điệu Monotonic Stack](lessons/lesson-09-ngan-xep-hang-doi-deque-don-dieu/assets/l09_monotonic_stack_visual.svg)\n\n## 3. Ngăn xếp đơn điệu (Monotonic Stack): Tìm phần tử lớn hơn gần nhất"),

        # Lesson 10
        ("## 4. Kỹ thuật Hai Heap duy trì Trung vị động (Running Median)",
         "![Hai Heap duy trì Trung vị động](lessons/lesson-10-thu-vien-stl-c-nang-cao/assets/l10_two_heaps_median_visual.svg)\n\n## 4. Kỹ thuật Hai Heap duy trì Trung vị động (Running Median)"),

        # Lesson 11
        ("## 2. Tam giác Pascal & Bảng tổ hợp Modulo",
         "![Tam giác Pascal](lessons/lesson-11-to-hop-hoan-vi-va-xac-suat-co-ban/assets/l11_pascal_triangle_visual.svg)\n\n## 2. Tam giác Pascal & Bảng tổ hợp Modulo"),

        # Lesson 12
        ("## 4. Thuật toán Tarjan: Tìm Cầu và Khớp",
         "![Thuật toán Tarjan tìm Khớp và Cầu](lessons/lesson-12-ly-thuyet-do-thi-chuyen-sau/assets/l12_tarjan_bridges_visual.svg)\n\n## 4. Thuật toán Tarjan: Tìm Cầu và Khớp"),

        # Lesson 13
        ("## 2. Cây phân đoạn (Segment Tree): Kiến trúc & Nguyên lý",
         "![Kiến trúc Cây phân đoạn Segment Tree](lessons/lesson-13-cay-phan-doan-segment-tree-va-fenwick-tree/assets/l13_segment_tree_visual.svg)\n\n## 2. Cây phân đoạn (Segment Tree): Kiến trúc & Nguyên lý"),
        ("## 4. Cây Fenwick (Binary Indexed Tree — BIT)",
         "![Cấu trúc Cây Fenwick BIT](lessons/lesson-13-cay-phan-doan-segment-tree-va-fenwick-tree/assets/l13_fenwick_tree_visual.svg)\n\n## 4. Cây Fenwick (Binary Indexed Tree — BIT)"),

        # Lesson 14
        ("## 3. Mô hình phân nhánh trạng thái Digit DP",
         "![Mô hình phân nhánh Digit DP](lessons/lesson-14-quy-hoach-dong-chu-so-digit-dp/assets/l14_digit_dp_tree_visual.svg)\n\n## 3. Mô hình phân nhánh trạng thái Digit DP"),

        # Lesson 15
        ("## 4. Cây tiền tố (Trie): Kiến trúc & Tìm kiếm từ",
         "![Cây tiền tố Trie](lessons/lesson-15-xu-ly-chuoi-string-hashing-va-bigint/assets/l15_trie_tree_visual.svg)\n\n## 4. Cây tiền tố (Trie): Kiến trúc & Tìm kiếm từ"),
    ]

    for target, repl in replacements:
        if target in content and repl not in content:
            content = content.replace(target, repl)
            print(f"  ✅ Đã nhúng hình cho mục: {target[:50]}...")

    with open(MASTER_FILE, "w", encoding="utf-8") as f:
        f.write(content)
    print("🎉 Đã nhúng toàn bộ sơ đồ minh họa vào MASTER_ALL_LESSONS.md!")

if __name__ == "__main__":
    main()
