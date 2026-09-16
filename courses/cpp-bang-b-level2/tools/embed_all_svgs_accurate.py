#!/usr/bin/env python3
"""
Nhúng toàn bộ sơ đồ minh họa SVG vào đúng vị trí H2 của 15 bài học trong MASTER_ALL_LESSONS.md
"""

from pathlib import Path

BASE_DIR = Path("/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b-level2")
MASTER_FILE = BASE_DIR / "MASTER_ALL_LESSONS.md"

def main():
    with open(MASTER_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Ánh xạ chính xác theo H2 trong MASTER_ALL_LESSONS.md
    replacements = [
        # Lesson 01
        ("## 3. Sàng ước số nguyên tố nhỏ nhất (SPF — Smallest Prime Factor)",
         "![Sơ đồ cơ chế Sàng SPF](lessons/lesson-01-so-hoc-co-ban-chuyen-sau/assets/l01_spf_sieve_visual.svg)\n\n## 3. Sàng ước số nguyên tố nhỏ nhất (SPF — Smallest Prime Factor)"),
        ("## 4. Sàng nguyên tố phân đoạn (Segmented Sieve trên $[L, R]$)",
         "![Mô phỏng Sàng số nguyên tố phân đoạn](lessons/lesson-01-so-hoc-co-ban-chuyen-sau/assets/l01_segmented_sieve_visual.svg)\n\n## 4. Sàng nguyên tố phân đoạn (Segmented Sieve trên $[L, R]$)"),

        # Lesson 02
        ("## 3. Thuật toán lũy thừa nhanh (Binary Exponentiation / Fast Power)",
         "![Sơ đồ nhân ma trận Fibonacci](lessons/lesson-02-modulo-va-fast-power/assets/l02_matrix_fibonacci_visual.svg)\n\n## 3. Thuật toán lũy thừa nhanh (Binary Exponentiation / Fast Power)"),

        # Lesson 03
        ("## 4. Chặt nhị phân số thực & Tìm kiếm tam phân (Ternary Search)",
         "![Chặt nhị phân tập số thực](lessons/lesson-03-tim-kiem-nhi-phan-nang-cao/assets/l03_binary_search_real_visual.svg)\n\n## 4. Chặt nhị phân số thực & Tìm kiếm tam phân (Ternary Search)"),

        # Lesson 04
        ("## 2. Mảng tiền tố 2D & Mảng hiệu 2D (2D Prefix & Difference)",
         "![Sơ đồ 2D Prefix Sum](lessons/lesson-04-ky-thuat-mang-nang-cao/assets/l04_2d_prefix_sum_visual.svg)\n\n## 2. Mảng tiền tố 2D & Mảng hiệu 2D (2D Prefix & Difference)"),

        # Lesson 05
        ("## 3. Kỹ thuật Meet in the Middle (MITM)",
         "![Kỹ thuật Meet in the Middle](lessons/lesson-05-de-quy-chia-de-tri-mitm/assets/l05_mitm_split_visual.svg)\n\n## 3. Kỹ thuật Meet in the Middle (MITM)"),

        # Lesson 06
        ("## 2. Bảng tổng hợp các thủ thuật Bitwise kinh điển (Bit Tricks)",
         "![Bảng thao tác Bitmask](lessons/lesson-06-phep-toan-bit-va-bitmask-nang-cao/assets/l06_bitmask_operations_visual.svg)\n\n## 2. Bảng tổng hợp các thủ thuật Bitwise kinh điển (Bit Tricks)"),

        # Lesson 07
        ("## 2. Các mô hình bài toán tham lam kinh điển & chứng minh toán học",
         "![Lập lịch sự kiện tham lam](lessons/lesson-07-thuat-toan-tham-lam-greedy/assets/l07_interval_scheduling_visual.svg)\n\n## 2. Các mô hình bài toán tham lam kinh điển & chứng minh toán học"),

        # Lesson 08
        ("## 2. Các mô hình Quy hoạch động kinh điển",
         "![Quy hoạch động trên lưới 2D](lessons/lesson-08-quy-hoach-dong-co-ban-va-chuyen-sau/assets/l08_grid_dp_visual.svg)\n\n## 2. Các mô hình Quy hoạch động kinh điển"),

        # Lesson 09
        ("## 2. Ngăn xếp đơn điệu (Monotonic Stack)",
         "![Ngăn xếp đơn điệu Monotonic Stack](lessons/lesson-09-ngan-xep-hang-doi-deque-don-dieu/assets/l09_monotonic_stack_visual.svg)\n\n## 2. Ngăn xếp đơn điệu (Monotonic Stack)"),

        # Lesson 10
        ("## 4. Mẫu cài đặt chuẩn thi đấu: Duy trì trung vị động (Running Median) bằng 2 Heap",
         "![Hai Heap duy trì Trung vị động](lessons/lesson-10-thu-vien-stl-c-nang-cao/assets/l10_two_heaps_median_visual.svg)\n\n## 4. Mẫu cài đặt chuẩn thi đấu: Duy trì trung vị động (Running Median) bằng 2 Heap"),

        # Lesson 11
        ("## 2. Tiền xử lý giai thừa và tính $C_n^k \\bmod (10^9+7)$ trong $\\mathcal{O}(1)$",
         "![Tam giác Pascal](lessons/lesson-11-to-hop-hoan-vi-va-xac-suat-co-ban/assets/l11_pascal_triangle_visual.svg)\n\n## 2. Tiền xử lý giai thừa và tính $C_n^k \\bmod (10^9+7)$ trong $\\mathcal{O}(1)$"),

        # Lesson 12
        ("## 3. Thuật toán Dijkstra tìm đường đi ngắn nhất đồ thị có trọng số dương",
         "![Thuật toán Tarjan tìm Khớp và Cầu](lessons/lesson-12-ly-thuyet-do-thi-chuyen-sau/assets/l12_tarjan_bridges_visual.svg)\n\n## 3. Thuật toán Dijkstra tìm đường đi ngắn nhất đồ thị có trọng số dương"),

        # Lesson 13
        ("## 2. Cây Fenwick (Binary Indexed Tree — BIT)",
         "![Cấu trúc Cây Fenwick BIT](lessons/lesson-13-cay-phan-doan-segment-tree-va-fenwick-tree/assets/l13_fenwick_tree_visual.svg)\n\n## 2. Cây Fenwick (Binary Indexed Tree — BIT)"),
        ("## 3. Cây phân đoạn (Segment Tree — Point Update / Range Query)",
         "![Kiến trúc Cây phân đoạn Segment Tree](lessons/lesson-13-cay-phan-doan-segment-tree-va-fenwick-tree/assets/l13_segment_tree_visual.svg)\n\n## 3. Cây phân đoạn (Segment Tree — Point Update / Range Query)"),

        # Lesson 14
        ("## 2. Các tham số trạng thái cốt lõi trong Digit DP",
         "![Mô hình phân nhánh Digit DP](lessons/lesson-14-quy-hoach-dong-chu-so-digit-dp/assets/l14_digit_dp_tree_visual.svg)\n\n## 2. Các tham số trạng thái cốt lõi trong Digit DP"),

        # Lesson 15
        ("## 2. Kỹ thuật Băm chuỗi đa thức (Polynomial Rolling Hash)",
         "![Cây tiền tố Trie](lessons/lesson-15-xu-ly-chuoi-string-hashing-va-bigint/assets/l15_trie_tree_visual.svg)\n\n## 2. Kỹ thuật Băm chuỗi đa thức (Polynomial Rolling Hash)"),
    ]

    count = 0
    for target, repl in replacements:
        if target in content and repl not in content:
            content = content.replace(target, repl)
            print(f"  ✅ Đã nhúng hình cho mục: {target[:50]}...")
            count += 1

    with open(MASTER_FILE, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"🎉 Đã nhúng thành công {count} sơ đồ minh họa vector vào MASTER_ALL_LESSONS.md!")

if __name__ == "__main__":
    main()
