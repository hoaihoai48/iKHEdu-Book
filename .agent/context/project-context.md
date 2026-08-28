# Project Context — Điền trước khi viết

> Tệp này là context điều hành của dự án. Cập nhật có kiểm soát; không dùng nó để thay thế source gốc. Mọi thay đổi làm đổi mục tiêu hoặc phạm vi phải ghi thêm vào `decision-log.md`.

## Identity

| Trường | Giá trị |
|---|---|
| Project name | ikhEdu_lessons |
| Chủ biên / owner | Chủ dự án iKHEDU |
| Người duyệt cuối | TBD — cần chủ dự án xác nhận |
| Repository / workspace | `ikhEdu_lessons` |
| Context version | 1.0.0 |
| Last updated | 2026-08-27 |

## Product definition

- Loại tài liệu: hệ thống giáo trình, lesson, editorial, đề bài và tài liệu đào tạo lập trình thi đấu.
- Mục đích sử dụng: dạy học sinh từ nền tảng Level 0 đến Level 1 và các tuyến nâng cao; hỗ trợ giáo viên dẫn dắt tư duy, luyện tập và kiểm tra.
- Đầu ra cần bàn giao: lesson, đề bài, hướng dẫn giảng dạy, editorial C++, quick reference, roadmap, assessment và các tài liệu liên quan.
- Phạm vi bao gồm: C++ cơ bản, tư duy giải bài, mô hình hóa, debug, kiểm thử, độ phức tạp và các mẫu thuật toán/cấu trúc dữ liệu theo roadmap.
- Phạm vi không bao gồm: tự ý thay đổi source-of-truth, tự ý deploy/upload, hoặc phát hành nội dung khi chưa qua review cần thiết.
- Tiêu chí thành công: học sinh hiểu ý tưởng và tự biến đổi lời giải, không chỉ sao chép code; nội dung có prerequisite, learning outcomes, ví dụ, bài tập, kiểm thử và provenance.

## Learner and use context

- Độc giả chính: học sinh bắt đầu từ số 0 hoặc đang xây nền tảng C++ và tư duy thuật toán.
- Trình độ đầu vào: TBD; project hiện tập trung vào tuyến Bảng B — Level 1 theo roadmap hình, cần chủ dự án xác nhận placement cụ thể.
- Kiến thức tiên quyết: tùy module; phải ghi rõ trong từng lesson/chapter.
- Bối cảnh sử dụng: lớp học, tự học có hướng dẫn, luyện thi và đào tạo giáo viên.
- Thời lượng hoặc khối lượng học: TBD theo module.
- Ngôn ngữ và biến thể ngôn ngữ: tiếng Việt; code và thuật ngữ kỹ thuật giữ quy ước C++/English khi cần.
- Ràng buộc accessibility: đoạn văn ngắn, cấu trúc rõ, ví dụ nhỏ, giải thích từng bước, tránh nhồi nhiều khái niệm mới trong một bài.

## Pedagogical contract

- Chuẩn chương trình / learning outcomes cấp cao: đọc đề, mô hình hóa, lập trình, kiểm thử, phân tích độ phức tạp, C++ cơ bản và tự giải bài tương tự.
- Mức độ tư duy mong muốn: hiểu trực giác, làm theo hướng dẫn, giải thích, áp dụng và chuyển giao sang bài biến thể.
- Loại đánh giá: bài kiểm tra đầu vào, formative checks, bài quen thuộc, bài biến thể và cổng năng lực.
- Quy tắc alignment: Xem chapter template và QA checklist
- Cách cung cấp đáp án/feedback: hướng dẫn từng bước, lỗi thường gặp, đáp án hoặc editorial theo đúng kênh người học/giáo viên.

## Editorial contract

- Giọng điệu: trang trọng, chuyên nghiệp, truyền cảm hứng, thực tiễn, phù hợp học sinh Việt Nam.
- Quy ước thuật ngữ: giữ thuật ngữ C++/English khi cần, giải thích tiếng Việt ở lần xuất hiện đầu tiên.
- Quy ước ký hiệu/đơn vị: tuân theo source tương ứng; dùng KaTeX/Markdown đúng quy ước project.
- Style guide: quy tắc lời văn, cấu trúc đề bài và định dạng trong `IKHEDU_Knowledge_Base.md` chỉ dùng tham chiếu, không sửa source gốc.
- Citation style: TBD; mọi claim ngoài source phải có provenance.
- Định dạng xuất bản: Markdown và code; các định dạng khác chỉ tạo khi được yêu cầu.
- Phiên bản và changelog: ghi trong decision log và từng output khi thay đổi có ảnh hưởng ý nghĩa.

## Source policy

- Thư mục source-of-truth: workspace root hiện tại.
- Tệp/nguồn nền bắt buộc đọc: `IKHEDU_Knowledge_Base.md`, `ikhEdu_foundation_framework_report.md` và `/Users/vu/Developer/ikhEdu_lessons/Lo_trinh_hoc_tap_bangB_level1.jpg`; cả ba là read-only.
- Quy tắc ưu tiên khi nguồn xung đột: ba source được chủ dự án chỉ định là nguồn tham chiếu; quyết định của chủ dự án ghi trong decision log được ưu tiên khi diễn giải; phải ghi conflict, không tự hòa giải.
- Nguồn ngoài được phép sử dụng: chỉ khi cần và phải ghi URL/DOI, ngày truy cập, phạm vi sử dụng và trạng thái xác minh.
- Quy tắc bản quyền/license/attribution: TBD; phải hỏi chủ dự án khi dùng nguồn ngoài, ảnh, bảng, code hoặc văn bản không rõ quyền.
- Ngày cắt dữ liệu: 2026-08-27 cho lần tích hợp này; cập nhật khi dùng dữ liệu thời gian-sensitive.

## Current state

- Đã hoàn thành: knowledge base lớn, báo cáo thiết kế nền tảng, quick reference Level 0 và roadmap Level 1; đã tích hợp `.agents`; đã tạo course registry, cấu trúc khóa `cpp-bang-b`, outline curriculum và lesson package draft cho Module 01 – Sắp xếp.
- Đang làm: review lesson package Module 01 – Sắp xếp, chuẩn hóa nội dung giáo trình và duy trì context cho agent.
- Blockers: người duyệt cuối, citation style, license/attribution policy, thời lượng từng module và cấu trúc thư mục bài toán mới cần xác nhận.
- Việc tiếp theo: review `Ly_Thuyet.md`, `Bai_Tap.md`, `QA_Review.md` và code tham chiếu; sau đó chốt assessment/test fixture và tạo problem package nếu cần.
- Lần handoff gần nhất: 2026-08-27 — tích hợp bộ `.agents` vào project.
