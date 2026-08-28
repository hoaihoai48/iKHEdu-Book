# Source Index — Manifest nguồn

> Đây là danh mục điều hướng, không phải nội dung nguồn. Hãy cập nhật khi thêm, thay thế hoặc loại bỏ source. Source gốc nên được giữ nguyên và chỉ đọc.

## Quy tắc ưu tiên

`P0` là source-of-truth do chủ dự án cung cấp và có quyền quyết định. `P1` là văn bản pháp quy, chuẩn chương trình, tiêu chuẩn tổ chức hoặc tài liệu chính thức. `P2` là nghiên cứu học thuật/primary source có thể kiểm chứng. `P3` là giáo trình, handbook hoặc tổng quan có uy tín. `P4` là tài liệu giải thích, blog hoặc nguồn khám phá; không dùng làm bằng chứng cuối nếu có nguồn tốt hơn.

Khi các nguồn xung đột, không tự hòa giải. Ghi conflict vào evidence ledger và decision log; nêu nguồn nào được ưu tiên, vì sao và ai cần phê duyệt.

## Source registry

| Source ID | Priority | Title / description | Author / org | Path or URL | Version/date | License/rights | Relevant sections | Status |
|---|---:|---|---|---|---|---|---|---|
| `SRC-001` | P0 | IKHEDU Knowledge Base | iKHEDU project | `IKHEDU_Knowledge_Base.md` | Current / 2026-08-27 | Project-owned; read-only | Problem catalog, editorial, code, testing/deploy conventions | `registered-read-only` |
| `SRC-002` | P0 | Foundation framework report | iKHEDU project | `ikhEdu_foundation_framework_report.md` | Current / 2026-08-27 | Project-owned; read-only | Curriculum framing and foundation/Level 1 design decisions | `registered-read-only` |
| `SRC-004` | P0 | Bảng B Level 1 roadmap image | iKHEDU project | `Lo_trinh_hoc_tap_bangB_level1.jpg` | Current / 2026-08-27 | Project-owned; read-only | Visual topic map of 21 Level 1 subjects | `registered-read-only` |

## External structural references

| Reference ID | Priority | Title / description | Author / org | Path or URL | Permitted use | Status |
|---|---:|---|---|---|---|---|
| `REF-001` | P3 | ebook-ikh repository — structure reference | DKTECHVN | https://github.com/DKTECHVN/ebook-ikh | Tham khảo cách tổ chức README/group, `Ly_Thuyet.md`, `Bai_Tap.md`, `De_Bai.md`, `Huong_Dan_Giang_Day.md`, `solution.cpp` và `test/`; không sao chép nội dung hoặc xem là source-of-truth | `reference-only` |

## Project files

| File ID | Path | Role | Read-only? | Last checked | Notes |
|---|---|---|---|---|---|
| `FILE-001` | `IKHEDU_Knowledge_Base.md` | source-of-truth/reference | yes | 2026-08-27 | Do not copy secrets or operational credentials into context/output |
| `FILE-002` | `ikhEdu_foundation_framework_report.md` | curriculum/framework reference | yes | 2026-08-27 | Project-owned report; do not treat as permission to edit source content |
| `FILE-004` | `Lo_trinh_hoc_tap_bangB_level1.jpg` | roadmap visual | yes | 2026-08-27 | Topic map, not a complete teaching sequence |
| `FILE-005` | `.agents/context/project-context.md` | project context | controlled | 2026-08-27 | Context contract for agent |
| `FILE-006` | `.agents/context/evidence-ledger.md` | claims/citations | controlled | 2026-08-27 | Provenance registry |
| `FILE-007` | `.agents/context/decision-log.md` | decisions/handoff | controlled | 2026-08-27 | Record material decisions |
| `FILE-008` | `courses/cpp-bang-b/BOOK_MASTER.md` | canonical book manuscript | no | 2026-08-28 | Canonical draft for print/digital integration; lesson files are supporting artifacts |

## Retrieval rules

Đọc manifest này trước. Chỉ nạp các source liên quan đến claim hoặc chapter đang xử lý. Khi trích source, ghi `source_id`, path/URL và vị trí chính xác vào evidence ledger. Không coi tên file hoặc thứ tự thư mục là bằng chứng về nội dung.

## Change history

| Date | Change | Reason | Approved by |
|---|---|---|---|
| 2026-08-27 | Registered current project sources and context files | Agent integration | Chủ dự án xác nhận cần thiết |
