# Evidence Ledger — Claim và bằng chứng

> Mỗi claim quan trọng phải có một dòng. Không xóa dòng cũ; khi claim thay đổi, cập nhật trạng thái và ghi lịch sử thay đổi. Bản ledger này không thay thế source.

## Trạng thái

`verified` = đã kiểm tra trực tiếp; `partial` = source chỉ hỗ trợ một phần; `unverified` = chưa kiểm tra; `conflict` = có nguồn mâu thuẫn; `rejected` = bằng chứng không đủ hoặc không được dùng.

## Claim registry

| Claim ID | Claim ngắn | Source ID | Vị trí trang/section/đoạn | Evidence excerpt/paraphrase | Claim type | Status | Limits/conflict | Used in |
|---|---|---|---|---|---|---|---|---|
| `CLAIM-001` | Roadmap hình liệt kê 21 chủ đề của tuyến Bảng B — Level 1 | `SRC-004` | `Lo_trinh_hoc_tap_bangB_level1.jpg` | Visual roadmap gồm các nhóm như sorting, greedy, math, binary search, prefix sum, two pointers, strings, recursion, modulo, combinatorics, STL, DP, graph, stack/queue, segment tree, digit DP, hashing, big integers, bit operations và Fenwick tree | source description | `verified` | Roadmap là bản đồ chủ đề; không tự suy ra thứ tự pedagogical nếu source không nói rõ | curriculum mapping |
| `CLAIM-002` | Knowledge base là nguồn tham chiếu nội bộ cho problem catalog, editorial, code và quy ước liên quan | `SRC-001` | `IKHEDU_Knowledge_Base.md` — header và các mục tương ứng | Dùng để tra cứu nội dung; không sửa file gốc và không sao chép dữ liệu vận hành nhạy cảm | project policy | `verified` | Mọi nội dung mới phải tạo ở file/thư mục khác; cần review trước phát hành | all authoring |
| `CLAIM-003` | Foundation framework report là nguồn định hướng curriculum và quyết định thiết kế nền tảng/Level 1 | `SRC-002` | `ikhEdu_foundation_framework_report.md` — các mục curriculum/framework | Dùng để hiểu framing và thiết kế chương trình; không thay thế knowledge base hoặc roadmap | curriculum reference | `verified` | Chỉ dùng trong phạm vi project đã chỉ định | curriculum mapping |
| `CLAIM-004` | ebook-ikh tách cấu trúc điều hướng nhóm, lesson theory/practice và problem package thành các artifact riêng | `REF-001` | Repository tree; `00_Nhom_Co_Ban_CPlusPlus/README.md`; `Bai_01_Xin_Chao_CPlusPlus/{Ly_Thuyet.md,Bai_Tap.md,bai1_xinchao.cpp}`; `IKH-0001 - Gói kẹo may mắn/{De_Bai.md,Huong_Dan_Giang_Day.md,solution.cpp,test/}` | Quan sát dùng để thiết kế template; không phải bằng chứng nội dung chuyên môn của ikhEdu_lessons | structural reference | `verified` | Repository private; chỉ áp dụng phần khuôn đã được chủ dự án chấp thuận | template design |
## Citation registry

| Citation ID | Full citation | DOI/URL/path | Access date | License/attribution | Verified by | Notes |
|---|---|---|---|---|---|---|
| `CITE-001` | `IKHEDU_Knowledge_Base.md` | `IKHEDU_Knowledge_Base.md` | 2026-08-27 | Project-owned; read-only | Manus AI | Internal knowledge base |
| `CITE-002` | `Lo_trinh_hoc_tap_bangB_level1.jpg` | `/Users/vu/Developer/ikhEdu_lessons/Lo_trinh_hoc_tap_bangB_level1.jpg` | 2026-08-27 | Project-owned; read-only | Manus AI | Roadmap visual |
| `CITE-003` | `ikhEdu_foundation_framework_report.md` | `/Users/vu/Developer/ikhEdu_lessons/ikhEdu_foundation_framework_report.md` | 2026-08-27 | Project-owned; read-only | Manus AI | Curriculum/framework reference |
| `CITE-004` | `DKTECHVN/ebook-ikh` | `https://github.com/DKTECHVN/ebook-ikh` | 2026-08-27 | Private repository; use by permission | Manus AI | Structural reference only; inspected main branch |
## Quy tắc sử dụng

Không đưa `unverified` vào một câu khẳng định chắc chắn. Với `partial`, thu hẹp câu chữ theo đúng phần source hỗ trợ. Với `conflict`, trình bày bất đồng hoặc yêu cầu chủ biên quyết định. Trích dẫn nguyên văn phải giữ nguyên wording và vị trí; diễn giải phải trung thành với phạm vi source.

## Audit history

| Date | Change | Claims affected | Reviewer |
|---|---|---|---|
| 2026-08-27 | Seeded project claims from current source files and structural reference | Template enhancement research | Chủ dự án xác nhận cần thiết |
