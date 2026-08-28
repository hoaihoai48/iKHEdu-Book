# Decision Log — Nhật ký quyết định

> Chỉ ghi quyết định đã được xác nhận hoặc quyết định tạm thời có người chịu trách nhiệm. Không biến suy đoán của agent thành quyết định của dự án.

## Decision registry

| Decision ID | Date | Decision | Status | Rationale | Alternatives considered | Impacted files/claims | Owner/approver |
|---|---|---|---|---|---|---|---|
| `DEC-001` | 2026-08-27 | Dùng cấu trúc chapter/module template làm khung mặc định | adopted | Bảo đảm mỗi bài có mục tiêu, nội dung, hoạt động, đánh giá, glossary và provenance | Tự viết tự do từng bài | Lesson/chapter mới | Chủ dự án xác nhận cần thiết |
| `DEC-002` | 2026-08-27 | `IKHEDU_Knowledge_Base.md` là source tham chiếu read-only | adopted | Chủ dự án chỉ định knowledge base là nguồn tham chiếu; không được sửa file gốc | Sao chép/chỉnh trực tiếp knowledge base | Mọi lesson và editorial | Chủ dự án xác nhận cần thiết |
| `DEC-003` | 2026-08-27 | Không tự coi roadmap 21 chủ đề là thứ tự dạy hoàn chỉnh | provisional | Roadmap hình là bản đồ chủ đề; thứ tự dạy cụ thể cần chủ dự án xác nhận | Dạy đúng thứ tự trên ảnh | Curriculum map | Chủ dự án |
| `DEC-004` | 2026-08-27 | Áp dụng hai hồ sơ `lesson-package` và `problem-package`, có README/index điều hướng cấp nhóm | adopted | Khuôn ebook-ikh cho thấy lý thuyết/bài tập và statement/teacher guide/solution/test cần tách theo mục đích sử dụng | Ép toàn bộ nội dung vào một chapter template duy nhất | Lesson, problem, group README và review gates | Chủ dự án xác nhận yêu cầu tham khảo |
| `DEC-005` | 2026-08-27 | Tổ chức nội dung theo `courses/<course-slug>/` với `curriculum`, `lessons`, `problems`, `assessments` và `assets`; giữ source nền ở workspace root | adopted | Cho phép project chứa nhiều khóa học và tách rõ curriculum khỏi lesson/problem artifacts | Để toàn bộ giáo trình ở workspace root | Course registry và các output giáo trình mới | Chủ dự án yêu cầu |
| `DEC-006` | 2026-08-27 | Chọn Module 01 – Sắp xếp làm MVP đầu tiên của khóa C++ Bảng B – Level 1 | provisional | Chủ đề bám roadmap, liên kết trực tiếp với mảng/vector, vòng lặp, so sánh, swap và complexity; đã có outline để bắt đầu | Bắt đầu bằng chủ đề nâng cao hơn hoặc viết toàn bộ Level 0 trước | `courses/cpp-bang-b/lessons/level1-01-sap-xep/` | Chủ dự án review |
| `DEC-007` | 2026-08-27 | Đổi tên curriculum draft thành `IKHEDU_Level0_Foundation.md` và `IKHEDU_Level1_Textbook_Outline.md`; dành tên `IKHEDU_Quick_Reference.md` cho phụ lục tra cứu siêu nhanh sau này | adopted | Phân biệt rõ nền tảng, outline giáo trình và quick reference; tránh gọi bản outline là textbook hoàn chỉnh | Giữ tên cũ gây nhầm vai trò | `courses/cpp-bang-b/curriculum/` và các README liên quan | Chủ dự án yêu cầu |
| `DEC-008` | 2026-08-27 | Tạo lesson package draft đầu tiên cho Module 01 – Sắp xếp gồm `Ly_Thuyet.md`, `Bai_Tap.md`, `code_reference.cpp` và `QA_Review.md` | provisional | Kiểm chứng cấu trúc sách qua một module nhỏ trước khi nhân rộng; chưa gọi `final` vì còn human review, assessment và test fixture | Viết toàn bộ textbook trước khi thử lesson package | `courses/cpp-bang-b/lessons/level1-01-sap-xep/` | Chủ dự án review |
| `DEC-009` | 2026-08-28 | `courses/cpp-bang-b/BOOK_MASTER.md` là bản thảo canonical duy nhất của sách C++ Bảng B – Level 1; lesson files là artifact hỗ trợ | provisional | Cần có một bản thảo tổng hợp để chuẩn bị bản in/digital, nhưng chưa gọi `print-ready` trước human review | Chỉ giữ nội dung rời ở từng lesson; tạo nhiều master theo chương | `courses/cpp-bang-b/BOOK_MASTER.md`, course README | Chủ dự án review |
| `DEC-010` | 2026-08-28 | BOOK_MASTER là bản thảo sách độc lập dành cho học sinh/in ấn; không chứa path local, source ID, link lesson hoặc quy tắc quản trị nội bộ | adopted | Tách rõ nội dung xuất bản khỏi hồ sơ biên soạn và điều hướng repository | Trộn manifest nội bộ vào bản sách | `courses/cpp-bang-b/BOOK_MASTER.md` | Chủ dự án yêu cầu |
| `DEC-011` | 2026-08-28 | Hoàn thiện coverage bản thảo Level 1 trong cùng BOOK_MASTER với 21 chương theo roadmap; Chương 1 có nội dung chi tiết, các chương còn lại có khung lý thuyết cốt lõi và prerequisite | provisional | Hoàn thành bản đồ và nội dung nền cho toàn tuyến trước khi mở rộng từng chương; không tạo master hoặc file quản trị riêng | Chỉ viết từng chương rời mà chưa có toàn cảnh | `courses/cpp-bang-b/BOOK_MASTER.md` | Chủ dự án review |
| `DEC-012` | 2026-08-28 | Trong bản in, Phần I dùng các mục I.1–I.6 cho nền tảng; Phần II đánh số lại từ Chương 1 — Sắp xếp | adopted | Tách cấu trúc nền tảng khỏi numbering của tuyến thuật toán, giúp học sinh đọc sách tự nhiên hơn | Đánh số liên tục khiến Sắp xếp thành Chương 7 và gây nhầm với module thuật toán đầu tiên | `courses/cpp-bang-b/BOOK_MASTER.md` | Chủ dự án yêu cầu |
| `DEC-013` | 2026-08-28 | Approved cấu trúc Chương 1 — Sắp xếp thành bảy Bài 1.1–1.7 trong BOOK_MASTER; không tách thêm file lesson | adopted | Làm rõ đơn vị kiến thức cho học sinh nhưng vẫn giữ bản in gọn, tránh tạo file rác và không đồng nhất cứng Bài với một buổi học | Tách mỗi Bài thành file riêng hoặc giữ các mục đánh số cũ | `courses/cpp-bang-b/BOOK_MASTER.md` | Chủ dự án xác nhận |

## Working assumptions

| Assumption ID | Assumption | Confidence | Must be confirmed by | Due / trigger | Affected work |
|---|---|---|---|---|---|
| `ASM-001` | Người học chính bắt đầu từ số 0 hoặc đang xây nền tảng C++ | medium | Chủ dự án | Khi chốt syllabus/placement test | Độ sâu và thứ tự module |

## Handoff summary

- Mục tiêu hiện tại: chuẩn hóa quy trình viết lesson/giáo trình và duy trì context cho agent trong ikhEdu_lessons.
- Đã quyết định: dùng `.agents` với Rule Always On, skill academic authoring, context ledger và workflow `/write-book`; giữ ba source project read-only; áp dụng hai hồ sơ lesson/problem và README/index cấp nhóm; tổ chức output theo `courses/<course-slug>/`.
- Chưa quyết định: người duyệt cuối, citation style, license/attribution policy, thời lượng module và cấu trúc bài mới.
- Blockers: cần chủ dự án xác nhận các mục chưa quyết định trước release tài liệu lớn.
- Hành động tiếp theo: review toàn bộ coverage Level 1 trong `BOOK_MASTER.md`; sau đó mở rộng từng chương theo ưu tiên lớp học, bắt đầu từ các chương nền tảng như Đếm, Prefix Sum, Hai con trỏ và Tham lam.

## Change history

| Date | Change | Reason | Author |
|---|---|---|---|
| 2026-08-27 | Added ikhEdu_lessons decisions and handoff state | Direct project integration | Manus AI |
