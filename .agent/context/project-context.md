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

## Current state

- **Đã hoàn thành**:
  - Khóa toàn diện **Curriculum Architecture v2** tại `docs/MASTER_MODULE_01_DESIGN.md`.
  - Tách biệt C++ Foundation Layer và 8 Master Modules.
  - Hoàn thiện Golden Specification cho **Module 01: Sorting → Two Pointers → Sliding Window → Greedy** gồm 7 Lessons, 7 Pattern (`PAT-00` đến `PAT-06`), DAG Dependency, Thang nhận thức P0–P5 và 43 Problem Activity Slots.
  - Đồng bộ Platform DKOJ: Sửa hiển thị title trùng lặp, cập nhật mô tả khóa học, deploy uwsgi live.
- **Đang làm**:
  - Thiết kế Problem Blueprint & Lập danh mục chi tiết 43 Problem Activity Slots của Module 01 gắn mã `IKH-01xx`.
  - Biên soạn Lesson Content cho 7 Lessons của Module 01 theo chu trình 8 bước.
- **Việc tiếp theo**: Hoàn thiện Pilot Module 01 làm mẫu chuẩn mực (Golden Template), sau đó nhân rộng cho 7 Module còn lại.
