# PLAN — Build sách giáo viên Scratch (2 quyển)

> Mục đích: sách đứng lớp cho thầy cô (hiểu đề, mạch giảng, demo dry-run, đón bẫy lỗi, chấm bài). KHÔNG phát cho học sinh vì chứa lời giải.
> Khuôn mẫu: `python-giaovien-quyen-1/2.docx` (mỗi bài = Đề HS + 4 mục GV: Ý tưởng & Phân tích → Dry Run Table → Bẫy lỗi → Lời giải tham khảo).
> Nguồn: `courses/scratch-bang-a/problems/*/De_Bai.md + Huong_Dan_Giang_Day.md + solution.dsl + solution_blocks_vi.png + test/`.

## Step 0 — Chốt phạm vi (trước khi động tay)

- [ ] Chia quyển: Q1 = Bài 01–08 (gồm Pen, 194 bài) hay Q1 = Bài 03–08 (thuật toán, 157 bài như Python)? Đề xuất: theo Scratch (Bài 01–08 / Bài 09–16) để khớp sách học sinh mới.
- [ ] Lời nói đầu GV: viết mới (đối tượng thầy cô, hướng dẫn dùng sách) — không tái dùng bản học sinh.
- [ ] Tên file ra: `scratch-giaovien-quyen-1.docx`, `scratch-giaovien-quyen-2.docx`.

## Step 1 — Kiểm kê nguồn (ĐÃ XONG 2026-09-21)

- [x] Quét 324 thư mục problems: `De_Bai.md` đủ 324/324; `Huong_Dan_Giang_Day.md` đủ 324/324; ảnh `solution_blocks_vi.png` đủ 324/324.
- [x] Huong_Dan đúng 4 mục (Ý tưởng → Dry Run bảng → Bẫy lỗi → Lời giải + ảnh + kịch bản).
- [x] Gate PASS — không bài nào phải bù nội dung.
- [ ] Nợ riêng (ngoài critical path sách GV): `solution.dsl` thiếu 317/324 — Lời giải sách GV dùng ảnh blocks nên không chặn build.

- [ ] Quét 324 thư mục problems, với mỗi bài ghi: có `De_Bai.md` / `Huong_Dan_Giang_Day.md` / `solution.dsl` / `solution_blocks_vi.png` / `test/` hay không.
- [ ] Với mỗi `Huong_Dan_Giang_Day.md`, kiểm tra đủ 4 mục: Ý tưởng & Phân tích; Dry Run (bảng ask/answer/biến/say); Bẫy lỗi; Lời giải/Transfer.
- [ ] Output: bảng coverage (đủ/thiếu theo bài) + danh sách bài phải bù nội dung.
- [ ] Gate: coverage 100% De_Bai + solution ảnh; Huong_Dan thiếu → liệt kê bù ở Step 2, không build mù.

## Step 2 — Bù nội dung thiếu + chốt khuôn

- [ ] Viết/bổ sung Huong_Dan cho bài thiếu theo đúng 4 mục (Ý tưởng → Dry Run bảng → Bẫy lỗi → Lời giải DSL + ảnh).
- [ ] Chốt khuôn mỗi bài trong Word: H3 `Bài NN [mã]: tên` → Bối cảnh → Hình minh họa → Nhiệm vụ → Input/Output/Sample/Giải thích → H4 (1. Ý tưởng; 2. Dry Run; 3. Bẫy lỗi; 4. Lời giải + ảnh blocks).
- [ ] Lời nói đầu GV + Mục lục (TOC field như bản học sinh gộp).
- [ ] Không đưa lý thuyết vào sách GV (lý thuyết nằm sách học sinh).

## Step 2 — Lời nói đầu GV + manifest (ĐÃ XONG 2026-09-21)

- [x] `reference/Loi_Noi_Dau_GV_Quyen1.md` + `Quyen2.md` (đối tượng thầy cô, cách dùng 4 mục, không phát HS).
- [x] `tools/word_build_manifest_giaovien.json` (2 volumes, output `scratch-giaovien-quyen-1/2.docx`, header GV).

## Step 3 — Build (ĐÃ XONG 2026-09-21)

- [x] Chế độ `giaovien1/2` trong `build_word_scratch.py` (dùng manifest GV, bỏ lý thuyết/phụ lục, thêm H1 từ manifest, parse Huong_Dan thành 4 mục H4).
- [x] Chuẩn hóa 7 file Pen 9-mục về đúng 4 mục (giữ đủ nội dung, bỏ khối Lời giải trùng).
- [x] `scratch-giaovien-quyen-1.docx` (194 bài × 4 mục), `scratch-giaovien-quyen-2.docx` (130 bài × 4 mục).

## Step 4 — QA (sẵn sàng duyệt)

- [ ] Thêm chế độ `giaovien` vào `tools/build_word_scratch.py`: đọc manifest GV mới (`word_build_manifest_giaovien.json`), parse Huong_Dan thành 4 mục H4, nhúng ảnh `solution_blocks_vi.png`.
- [ ] Tái dùng nguyên: style chữ/bảng/code, header/footer, watermark, TOC field + update tay, cap ảnh 6.5cm/4cm, quy tắc quote-list.
- [ ] Ra 2 file `scratch-giaovien-quyen-1/2.docx`.

## Step 4 — QA + bàn giao

- [ ] Mỗi bài đủ 4 mục H4; ảnh lời giải khớp đề (đúng mã bài); bảng Dry Run đúng logic ask→say.
- [ ] Mục lục Update Field đủ số trang; không còn blocker/major mới `final`.
- [ ] Cập nhật `docs/LO_TRINH_SCRATCH.md` (phụ lục sách GV) sau khi xong.
