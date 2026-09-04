# KẾ HOẠCH BUILD QUYỂN 1 LEVEL 2 TRƯỚC (`IKHEDU_CPP_Nang_Cao_Quyen_1.docx`)

**Mã kế hoạch:** `IKHEDU-BUILD-L2Q1-v1.0`
**Phạm vi:** 134 bài `cppb2_l01`–`cppb2_l06` (Chương 01–03) — build trước, Quyển 2 làm sau.
**Căn cứ:** `docs/REPORT_DE_XUAT_REBUILD_LEVEL2.md` (v3.0), `docs/MASTER_WORD_BUILD_SPECIFICATION.md` (v2.1), `.agent/rules/academic-authoring-always-on.md` (§7–§8).

> Nguyên tắc: Quyển 1 build trước để chốt pipeline + visual, Quyển 2 chỉ việc chạy lại. Không đụng Quyển 2 trong kế hoạch này.

---

## 0. Hiện trạng Quyển 1 (quét tự động, đã xác minh)

| Hạng mục | Số lượng |
|---|---|
| Tổng problems Quyển 1 | 134 |
| Bối cảnh template rập khuôn | 75 |
| Nhiệm vụ sáo rỗng ("với độ phức tạp tối ưu nhất") | 124 |
| Thiếu Giải thích | 6 (`l02_01`, `l02_02`, `l03_01`, `l04_01`, `l05_01`, `l06_01`) |
| Test dummy (`test01.out` = `15`) | 114 |

---

## Giai đoạn 1 — Chuẩn hóa Markdown 134 bài (Rule §7)

- [ ] **B1.1. Chốt ca test lũy thừa** (`l02_01`): test ghi 323 (= mod 1000), đề + solution ghi mod 1e9+7 (= 1594323). Quyết định: **A** sửa test về 1594323 / **B** đổi MOD của đề. *(Đang chờ chủ dự án chọn — cấm tự sửa vì đụng toàn vẹn DKOJ.)*
- [x] **B1.2. Viết lại 75 Bối cảnh** thành lời văn story thực tế (1–2 đoạn, gắn đời sống). Giữ nguyên 100% dữ kiện toán, Input/Output/Ràng buộc bất động. *(+ 14 stub biến thể l05_17–22/l06_17–24 đã viết story; quét còn 0 sót.)*
- [x] **B1.3. Viết lại 124 Nhiệm vụ** thành *"Cho... Hãy lập trình..."* cụ thể, xóa câu sáo rỗng. *(Quét còn 0 sót toàn Quyển 1.)*
- [ ] **B1.4. Thay 114 sample/test dummy** bằng sample thật khớp `solution.cpp` (chạy code sinh output, đối chiếu tay từng bài). *(Cần phê duyệt: sinh lại output test dummy — Input giữ nguyên.)*
- [x] **B1.5. Viết 6 Giải thích**: đã viết 5 (`l02_02, l03_01, l04_01, l05_01, l06_01`); `l02_01` treo theo quyết định MOD.
- [x] **B1.6. Verify**: **133/134 đủ 7 phần** (thiếu duy nhất Giải thích `l02_01` có chủ đích). 29 tiêu đề đã có dấu; `l06_09/l06_11` trùng tiêu đề đã phân biệt theo Bối cảnh. Phát hiện ngoài phạm vi (dời giai đoạn server): lệch De_Bai ↔ solution (`l01_13, l01_15, l01_08/09/18, l02_12`); `l06_09/l06_11` nội dung gần như giống hệt.

---

## Giai đoạn 2 — Nâng cấp `courses/cpp-bang-b-level2/build_docx.py`

- [x] **B2.1.** Xóa logic sinh trang bìa (YAML + khối cover transform). Đoạn đầu file = H1 Lời nói đầu.
- [x] **B2.2.** Sample → bảng 2 cột; Giải thích mỗi dòng một đoạn (verify 171/171 LEFT).
- [x] **B2.3.** Tách `<w:br/>` → từng `<w:p>` + bảng Sample `tblW 6800`/`tcW 3400`, header Consolas 11 Bold Center, Dynamic Indent.
- [x] **B2.4.** Margins `36/36/64.35/36pt` (verify).
- [x] **B2.5.** Lời nói đầu H1 Center 14pt; thân Justify 14pt/1.5; Chương 01 `pageBreakBefore`.
- [x] **B2.6.** 6 H2 "Bài tập thực hành" đỏ `#FF0000` (verify).
- [x] **B2.7.** Justify đúng 4 style; `Normal` không Justify (verify = 0).
- [x] **B2.8.** Code Consolas 9pt/1.05, căn trái (194 paras LEFT), xóa `numPr`.
- [x] **B3.2.** `tblHeader` còn lại = 0; `cantSplit` đủ.
- [x] **B3.3.** 7369 math runs về 12pt; 16 bảng Phụ lục A về 12pt.

---

## Giai đoạn 3 — Post-process OpenXML + Watermark

- [x] **B3.1.** Watermark VML logo 286pt cả 3 header (`first`/`default`/`even` đều có `w:pict` + `imagedata` trỏ logo nhúng); bật `evenAndOddHeaders`. Logo lưu thành asset `courses/cpp-bang-b-level2/watermark_logo.jpeg` (tách từ `image13.jpeg` Quyển 1 chuẩn).
- [x] **B3.2.** `tblHeader` còn lại = 0; `cantSplit` đủ mọi hàng.
- [x] **B3.3.** 7369 math runs về 12pt (`sz/szCs val="24"`); 16 bảng Phụ lục A về 12pt.
- [x] **B3.4.** Dynamic Indent (làm chung B2.3, verify trong audit mục 4).

---

## Giai đoạn 4 — Rebuild Quyển 1 + kiểm toán + chốt QA

- [x] **B4.1.** Backup có sẵn (`IKHEDU_CPP_Nang_Cao_Quyen_1.docx.bak-prebuild` + git history); rebuild `--volume 1` thành công (1.50 MB).
- [x] **B4.2.** Audit 7/7 PASS: 0 bìa • watermark 3 header • `Normal` Justify = 0 • 134/134 Sample chuẩn • 0 `tblHeader` • code trái + 0 `numPr` trong code • 7369/7369 math 12pt.
- [ ] **B4.3.** Đối chiếu visual với `c++-level-1-quyen-1.docx` (mẫu chuẩn) — cần mở bằng Word thật, chưa làm được ở đây.
- [ ] **B4.4.** Chốt QA: `qa-checklist`, cập nhật evidence ledger / decision log.

---

## Quyết định đã chốt với chủ dự án

1. **Test/testcase để sau**: test hiện tại chưa đúng, input/output cũng có thể chưa chính xác. KHÔNG đụng tới thư mục `test/` trong đợt này. Test sẽ được sinh và update lên server sau (server hiện chưa có testcase).
2. **Phạm vi đợt này**: De_Bai đúng khuôn 7 phần + input/output đặc tả đúng + rebuild Word. B1.1 và B1.4 (test) dời sang giai đoạn server.
3. Riêng sample `l02_01` (323 vs MOD): giữ nguyên trong De_Bai, chưa viết Giải thích cho bài này cho tới khi chốt MOD ở giai đoạn server.
