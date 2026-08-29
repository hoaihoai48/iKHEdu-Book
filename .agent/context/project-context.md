# Project Context — Điền trước khi viết

> Tệp này là context điều hành của dự án. Cập nhật có kiểm soát; không dùng nó để thay thế source gốc. Mọi thay đổi làm đổi mục tiêu hoặc phạm vi phải ghi thêm vào `decision-log.md`.

## Identity

| Trường | Giá trị |
|---|---|
| Project name | ikhEdu_lessons |
| Chủ biên / owner | Chủ dự án iKHEDU |
| Người duyệt cuối | Chủ dự án iKHEDU |
| Repository / workspace | `ikhEdu_lessons` |
| Context version | 2.0.0 |
| Last updated | 2026-08-28 |

## Product definition

- **Loại tài liệu**: Hệ thống giáo trình chuẩn quốc tế, bài giảng đa phương tiện, ngân hàng đề bài có kiểm thử tự động, editorial và tài liệu đào tạo lập trình thi đấu (Tin học trẻ Bảng B, HSG THCS, Level 1).
- **Mục đích sử dụng**: Dạy học sinh từ nền tảng C++ Foundation đến 8 Master Modules chuyên sâu; đồng bộ xuất bản kép giữa **Sách in (Print/PDF)** và **Web DKOJ LMS Platform**.
- **Đầu ra cần bàn giao**: 8 Master Modules, 7 Lessons/Module, Problem Packages chuẩn (`De_Bai.md`, `Huong_Dan_Giang_Day.md`, `solution.cpp`, `test/` với 20 testcases), Quick Reference, Quiz kiểm tra và Assessment.
- **Phân cấp 5 tầng (5-Tier Hierarchy)**:
  $$\text{PROGRAM (C++ Level 1)} \longrightarrow \text{MODULE (8 Chuyên đề)} \longrightarrow \text{LESSON (Bài học)} \longrightarrow \text{CONCEPT (Khái niệm)} \longrightarrow \text{ACTIVITY / PROBLEM (IKH-xxxx)}$$
- **Định danh Problem độc lập**:
  - `IKH-xxxx` là Global Unique Problem Code trong Problem Library.
  - `LessonActivity` là Placement / Slot tham chiếu tới Problem, cho phép tái sử dụng bài toán mà không nhân bản dữ liệu.

## Learner and use context

- **Độc giả chính**: Học sinh bắt đầu bước vào lập trình thi đấu (Tin học trẻ Bảng B, HSG).
- **Trình độ đầu vào**: Hoàn thành lớp C++ Foundation (Fast I/O, biến, điều kiện, vòng lặp, vector 1D/2D, hàm).
- **Ngôn ngữ**: Tiếng Việt sư phạm truyền cảm hứng; code C++17/20 chuẩn thi đấu iKHEDU.
- **Ràng buộc sư phạm**: Vòng lặp học tập 8 bước (`Hook → Simulation → Invariant → Code → Micro Practice P0 → Quiz → Practice P1-P3 → Mastery P4/P5`). Không nhồi lý thuyết suông.

## Editorial contract

- **C++ Boilerplate chuẩn**:
  - `#include <bits/stdc++.h>` và `using namespace std;`.
  - Fast I/O: `ios::sync_with_stdio(false); cin.tie(nullptr);`.
  - Safe input: `if (!(cin >> n >> ...)) return 0;`.
- **Cấu trúc dữ liệu tối giản**: Ưu tiên kiểu nguyên thủy và `vector<vector<int>>` (vector lồng nhau / 2 chiều). `pair` và `struct` chỉ dùng khi bất đắc dĩ (sắp xếp đa trường hoặc hàm so sánh đặc thù).
- **Ranh giới công cụ (Not Yet Boundary)**: Trong Module 01, cấm dùng `set`, `map`, `deque`, `priority_queue`, `Segment Tree`, `Fenwick Tree`, Quy hoạch động.

## Source policy

- **Source-of-truth chuẩn kiến trúc**:
  1. `docs/MASTER_MODULE_01_DESIGN.md` (Golden Specification — 🔒 FROZEN).
  2. `IKHEDU_Knowledge_Base.md` (Master Problem Bank & 5-Step Editorial Guide).
  3. `Lo_trinh_hoc_tap_bangB_level1.jpg` (Bản đồ lộ trình 21 chủ đề gốc).

- **8 Master Modules (Level 1 — Bảng B)**:
  1. Module 01: Sorting / Two Pointers / Sliding Window (✅ 3 Lessons + 42 Problems Hoàn Tất)
  2. Module 02: Prefix / Difference / Binary Search / Bit (✅ 3 Lessons + 42 Problems Hoàn Tất)
  3. Module 03: Number Theory / Modulo / Big Integer (🎯 Kế hoạch tiếp theo)
  4. Module 04: Frequency / Counting / Combinatorics
  5. Module 05: String / Hashing
  6. Module 06: Recursion / Backtracking / DP
  7. Module 07: STL / Stack / Queue
  8. Module 08: Graph / Tree / Range Query

## Current state

- **Đã hoàn thành**:
  - Khóa toàn diện **Curriculum Architecture v2** tại `docs/MASTER_MODULE_01_DESIGN.md` và `docs/MASTER_MODULE_02_DESIGN.md`.
  - Master Roadmap 8 chuyên đề tại `docs/MASTER_CURRICULUM_ROADMAP.md`.
  - Hoàn thiện trọn vẹn **Module 01: Sorting / Two Pointers / Sliding Window** (3 Lessons + 42 Problems).
  - Hoàn thiện trọn vẹn **Module 02: Prefix / Difference / Binary Search / Bit** gồm:
    - **Lesson 01 (Mảng Tiền Tố & Mảng Hiệu)**: `Lesson04_Production_Content.md` + 12 Quiz + 16 bài `CPPB-PT-01..16`.
    - **Lesson 02 (Tìm Kiếm Nhị Phân)**: `Lesson05_Production_Content.md` + 14 Quiz + 18 bài `CPPB-BS-01..18`.
    - **Lesson 03 (Phép Toán Bit & Mặt Nạ Bit)**: `Lesson06_Production_Content.md` + 12 Quiz + 16 bài `CPPB-BIT-01..16`.
    - **100% 50 Problem Packages** đã được biên dịch cú pháp thử nghiệm qua `g++ -std=c++17` thành công $100\%$.
    - **Tổng số Problem Packages trong thư viện toàn hệ thống:** **92 bài toán**.
- **Đang làm**:
  - Chuẩn bị bước sang **Module 03: Number Theory / Modulo / Big Integer**.
