---
name: 03-print-publish
version: 2.1.0
priority: P0
trigger: always_on
---

# iKHEDU Print-Ready Word DOCX

Mọi `.docx` tuân thủ `docs/MASTER_WORD_BUILD_SPECIFICATION.md` + `docs/PLAN_CHINH_WORD_IN_MAU.md`:

1. Bỏ bìa, vào Lời nói đầu trang 1. Margins Top/Bottom/Right `36pt`, Left `64.35pt` (gáy). Chương đầu `pageBreakBefore=True`.
2. Watermark logo đủ 3 Header (even/default/first), VML `alt="logo_in"` -> `media/image13.jpeg`.
3. Lời nói đầu Center `14pt Bold`, body `14pt`, line `1.5`, Justify 100%.
4. Body `12.5pt`, line `1.15`, Justify. Toàn bộ chữ Body, Bảng và Headings bắt buộc màu đen tuyền `#000000` (đảm bảo in màu không bị mờ nét, cấm dùng màu xanh đen `#0F2A44` hay `#1E293B`). Duy nhất tiêu đề "Bài tập thực hành" dùng màu đỏ `#FF0000` (Bold 14pt Heading 2).
5. Khung Code `Source Code`: Consolas 9pt, line `1.05`, nền `#F8FAFC`, viền `#E2E8F0`, căn trái 100%, cấm `w:numPr`, cấm Justify style Normal.
6. Bảng: xóa `<w:tblHeader/>`, thêm `<w:cantSplit/>`; font chữ bảng nội dung chuẩn 12.0pt Times New Roman chữ đen `#000000`; công thức `m:oMath` 12pt; Sample IO bảng giữa `w=6800`, multiline testcase tách từng `<w:p>` với Dynamic Left Indent `max(10pt, 72pt - max(0,maxlen-4)*3.25pt)`; Input mô tả đủ số dòng/kích thước ma trận.
7. Mục lục (TOC) & Đánh số trang:
   - Tiêu đề "Mục lục" 18pt Bold Đen tuyền `#000000`, `pageBreakBefore=True`.
   - Chương/Lời nói đầu/Phụ lục 14pt Bold, Bài học 13pt Regular (thụt lề `320dxa`), màu `#000000`.
   - Tab leader dấu chấm `pos="9899"`.
   - Trường số trang động dùng mẫu phân rã OpenXML `PAGEREF <bookmark> \h` kèm `<w:noProof/>`.
   - **TUYỆT ĐỐI CẤM** gắn `<w:updateFields w:val="true"/>` trong `word/settings.xml` (tránh bật popup cảnh báo bảo mật khi mở Word).

Trước bàn giao chạy `.agents/skills/ikhedu-authoring/references/qa-checklist.md`, cập nhật evidence-ledger/decision-log.
