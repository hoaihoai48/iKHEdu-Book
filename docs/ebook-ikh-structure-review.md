# Đối chiếu khuôn `DKTECHVN/ebook-ikh`

**Ngày khảo sát:** 2026-08-27  
**Mục đích:** xem khuôn tổ chức giáo trình/bài toán hiện tại để bổ sung có kiểm soát vào `.agents` của `ikhEdu_lessons`.

## Kết luận ngắn

Repository `DKTECHVN/ebook-ikh` đang tổ chức nội dung theo nhiều tầng. Ở cấp nhóm có README làm mục lục điều hướng. Ở cấp lesson, lý thuyết, bài tập và code được tách thành các file riêng. Ở cấp problem package, statement cho học sinh, hướng dẫn giảng dạy, solution và test được tách thành bốn artifact. Đây là phần khuôn có thể tái sử dụng cho quy trình của `ikhEdu_lessons`; nội dung chuyên môn của repository không được tự động nhập vào project.

## Quan sát từ repository

| Tầng | Khuôn quan sát được | Ý nghĩa khi áp dụng |
|---|---|---|
| Group/chapter | `00_Nhom_Co_Ban_CPlusPlus/README.md` | README/index liên kết buổi học, chủ đề, file chi tiết và bài tập |
| Lesson theory/practice | `Bai_XX/.../Ly_Thuyet.md`, `Bai_Tap.md`, code `.cpp` | Tách phần giảng khái niệm khỏi phần luyện tập và code |
| Problem package | `IKH-XXXX - [Tên bài]/De_Bai.md`, `Huong_Dan_Giang_Day.md`, `solution.cpp`, `test/` | Tách trải nghiệm học sinh, tài liệu giáo viên, lời giải và kiểm thử |
| Workspace rule | `.agents/rules/python_learning.md` | Rule ngắn dùng để định vị mục tiêu và giới hạn phạm vi workspace |

## Bổ sung đã tích hợp

Bộ `.agents` trong project đã được mở rộng với ba template mới. `group-index-template.md` định nghĩa README cấp nhóm/chương. `lesson-package-template.md` định nghĩa lesson gồm README/index, `Ly_Thuyet.md`, `Bai_Tap.md`, code và test nếu có. `problem-package-template.md` định nghĩa problem package gồm `De_Bai.md`, `Huong_Dan_Giang_Day.md`, `solution.cpp` và `test/`.

Skill `academic-book-authoring` và workflow `/write-book` đã được cập nhật để chọn profile trước khi viết, không ép mọi nội dung vào một template, kiểm tra liên kết README → lesson → exercise → code hoặc statement → teacher guide → solution → tests, đồng thời chỉ định bản canonical khi tồn tại cả `.docx` và `.md`.

Rule Always On cũng ghi rõ `ebook-ikh` là `REF-001`, chỉ dùng làm **reference-only** cho cấu trúc. Ba source nội dung của `ikhEdu_lessons` vẫn được giữ riêng trong source registry và không bị thay thế:

1. `IKHEDU_Knowledge_Base.md`.
2. `ikhEdu_foundation_framework_report.md`.
3. `/Users/vu/Developer/ikhEdu_lessons/Lo_trinh_hoc_tap_bangB_level1.jpg`.

`IKHEDU_Level0_Foundation.md` không được thêm lại vào source registry.

## Giới hạn và lưu ý

Khuôn ebook-ikh cho thấy cách tổ chức file tốt, nhưng không tự chứng minh rằng mọi nội dung, thuật toán, pedagogical decision hoặc test đều đúng. Vì vậy, project chỉ tiếp nhận cấu trúc đã được chủ dự án chấp thuận; mọi claim chuyên môn vẫn phải đi qua source index, evidence ledger và QA gates của `ikhEdu_lessons`.

## Reference

- [DKTECHVN/ebook-ikh](https://github.com/DKTECHVN/ebook-ikh) — repository được chủ dự án cho phép tham khảo cấu trúc; không phải source-of-truth của `ikhEdu_lessons`.
