# Decision Log — Nhật ký quyết định

> Chỉ ghi quyết định đã được xác nhận hoặc quyết định tạm thời có người chịu trách nhiệm. Không biến suy đoán của agent thành quyết định của dự án.

## Decision registry

| Decision ID | Date | Decision | Status | Rationale | Alternatives considered | Impacted files/claims | Owner/approver |
|---|---|---|---|---|---|---|---|
| `DEC-001` | 2026-08-27 | Dùng cấu trúc chapter/module template làm khung mặc định | adopted | Bảo đảm mỗi bài có mục tiêu, nội dung, hoạt động, đánh giá, glossary và provenance | Tự viết tự do từng bài | Lesson/chapter mới | Chủ dự án xác nhận cần thiết |
| `DEC-002` | 2026-08-27 | `IKHEDU_Knowledge_Base.md` là source tham chiếu read-only | adopted | Chủ dự án chỉ định knowledge base là nguồn tham chiếu; không được sửa file gốc | Sao chép/chỉnh trực tiếp knowledge base | Mọi lesson và editorial | Chủ dự án xác nhận cần thiết |
| `DEC-003` | 2026-08-27 | Không tự coi roadmap 21 chủ đề là thứ tự dạy hoàn chỉnh | provisional | Roadmap hình là bản đồ chủ đề; thứ tự dạy cụ thể cần chủ dự án xác nhận | Dạy đúng thứ tự trên ảnh | Curriculum map | Chủ dự án |

## Working assumptions

| Assumption ID | Assumption | Confidence | Must be confirmed by | Due / trigger | Affected work |
|---|---|---|---|---|---|
| `ASM-001` | Người học chính bắt đầu từ số 0 hoặc đang xây nền tảng C++ | medium | Chủ dự án | Khi chốt syllabus/placement test | Độ sâu và thứ tự module |

## Handoff summary

- Mục tiêu hiện tại: chuẩn hóa quy trình viết lesson/giáo trình và duy trì context cho agent trong ikhEdu_lessons.
- Đã quyết định: dùng `.agents` với Rule Always On, skill academic authoring, context ledger và workflow `/write-book`; giữ knowledge base/roadmap gốc read-only.
- Chưa quyết định: người duyệt cuối, citation style, license/attribution policy, thời lượng module và cấu trúc bài mới.
- Blockers: cần chủ dự án xác nhận các mục chưa quyết định trước release tài liệu lớn.
- Hành động tiếp theo: chọn module MVP, lập chapter/module map và tạo một bài mẫu qua đủ QA gates.

## Change history

| Date | Change | Reason | Author |
|---|---|---|---|
| 2026-08-27 | Added ikhEdu_lessons decisions and handoff state | Direct project integration | Manus AI |
