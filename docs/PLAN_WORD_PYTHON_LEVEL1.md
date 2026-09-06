# Kế hoạch Convert Giáo Trình Python Level 1 sang Word In Màu

**Mục đích:** Chốt phương án trước khi build file Word in màu cho khóa Python Level 1, tái dùng khuôn C++ Quyển 1.
**Tài liệu gốc đối chiếu:**
- `docs/PLAN_CHINH_WORD_IN_MAU.md` (chuẩn in màu + xử lý bảng)
- `docs/MASTER_WORD_BUILD_SPECIFICATION.md` (spec build, mã `IKHEDU-DOCX-SPEC-v2.1`)
- File mẫu: `courses/cpp-bang-b/c++-level-1-quyen-1.docx`

---

## 1. Phạm vi nội dung Python (đã chốt nội dung, quét ngày 05/09/2026)

| Hạng mục | Số lượng | Nguồn |
|---|---|---|
| Chương | 5 | `build_master.py` |
| Bài học lý thuyết | 14 (L01–L14) | `lessons/lesson-*/Lesson*_Production_Content.md` |
| Concept Quiz | 250 câu (counts khớp 14/14) | trong file lý thuyết mỗi bài |
| Bài tập | 287 problems, mapping Bai_Tap ↔ thư mục khớp 100% | `problems/pya_*/` |
| Solutions | 287/287 chạy PASS sample | `problems/*/solution.py` |
| Hình minh họa | 13 SVG, **đã light theme sẵn** (nền `#FFFFFF`) | `courses/python-bang-a/assets/` |
| MASTER tổng hợp | ~12.700 dòng (đã gồm lý thuyết + toàn bộ đề bài) | `MASTER_ALL_LESSONS.md` |

---

## 2. Những gì tái dùng nguyên từ khuôn C++ (không cần bàn)

- Khổ giấy, lề (36pt / gáy 64.35pt), bỏ trang bìa, `pageBreakBefore` chương đầu
- Header/Footer/Watermark (3 header refs + số trang `— PAGE —`)
- Typography: body 12.5pt/1.15 Justify; H1 18/15.5pt, H2 14pt, H3 13pt, H4 12.5pt; **không Justify heading**
- Code block: Consolas 9pt, nền `#F8FAFC`, căn trái tuyệt đối
- Bảng: xóa `tblHeader`, `cantSplit` mọi dòng, Math 12pt, Sample IO căn giữa + dynamic indent
- Callout xanh `#EFF6FF`, tiêu đề "Bài tập thực hành" đỏ `#FF0000`
- TOC cuối sách, Lời nói đầu format P0–P10

---

## 3. Điểm XUNG ĐỘT với spec — cần bạn quyết (chưa build khi chưa chốt)

### C1. `## Ràng buộc` (time/memory) — spec §6 BẮT BUỘC, nhưng bạn đã cho xóa
- Spec yêu cầu mỗi đề có mục 8 `## Ràng buộc` (time $1.0\text{s}$, mem $256\text{MB}$) + cam kết DKOJ integrity.
- Thực tế Python: đã xóa sạch khỏi 287 `De_Bai.md` + 14 `Bai_Tap.md` theo yêu cầu của bạn.
- **Chọn 1:** (a) Giữ nguyên quyết định cũ — Word Python **không có** mục Ràng buộc (cần ghi chú thích lệch spec); (b) Khôi phục Ràng buộc chỉ trong bản Word (giữ markdown sạch).

### C2. Từ ngữ DKOJ / "thi đấu" — spec nhắc nhiều, bạn đã cấm
- Spec §6.1 ví dụ Bối cảnh nhắc `DKOJ`, §3 nhắc `Mẫu cài đặt chuẩn thi đấu`.
- Thực tế Python: 0 từ cấm trong 14 file lý thuyết.
- **Chọn 1:** (a) Thay bằng từ trung tính trong Word (`hệ thống chấm bài`, `mẫu code thường gặp`); (b) Giữ nguyên văn markdown (đã sạch, không cần thay).

### C3. HAI QUYỂN (đã chốt theo đề xuất) — chia theo số bài tập cho cân trang
Số bài tập thực tế mỗi bài: L01: 25, L02: 36, L03: 33, L04: 37, L05: 14, L06: 12, L07: 14, L08: 14, L09: 14, L10: 12, L11: 26, L12: 14, L13: 12, L14: 24 (tổng 287).

| Quyển | Phạm vi | Bài | Problems | Trọng tâm |
|---|---|---|---|---|
| **Quyển 1 — Nền tảng lập trình** | Chương 1–2 (L01–L06) | 6 | 157 | Tính toán cơ bản, rẽ nhánh, vòng lặp — học xong viết được chương trình hoàn chỉnh |
| **Quyển 2 — Số học & dữ liệu** | Chương 3–5 (L07–L14) | 8 | 130 | Số học/tách chữ số, danh sách, chuỗi ký tự |

*Lý do không chia theo Chương 1–3 / 4–5: phương án đó lệch nặng (211 vs 76 problems). Chia 157/130 cân trang hơn, mỗi quyển ước ~170–190 trang (tham chiếu C++ Q1: 188 problems ≈ 210 trang). Mỗi quyển có Phụ lục A + Phụ lục B lời giải của quyển đó.*

### C4. Đưa gì vào sách? (ngoài lý thuyết + đề bài)
- **250 Concept Quiz: KHÔNG in** (đã kiểm chứng: 0 quiz trong cả 2 quyển C++ — quiz chỉ ở bản digital).
- **Phạm vi cô đọng: CHỈ phần lý thuyết bài học.** 287 đề bài giữ nguyên 100%.
- **Phụ lục B lời giải: CÓ** (287 solutions chia theo quyển, như C++).
- **Phụ lục A nền tảng: CÓ** (viết mới cho Python, theo cấu trúc Phụ lục A C++).
- **`Huong_Dan_Giang_Day.md`: KHÔNG in chung** (tài liệu giáo viên).
- **Bảng kiến thức trọng tâm: TẠM KHÔNG đưa vào.**

### C5. Lời nói đầu + tên sách
- Cần text Lời nói đầu mới cho Python (không dùng lại của C++).
- Đã chốt: **tên sách** `Giáo trình Python cơ bản - quyển N` (header phải) + **tên file output** `python-level-1-quyen-N.docx` (theo quy ước C++).

### C6. Logo watermark
- Spec dùng `media/image13.jpeg` từ bản C++. **Tái dùng luôn** hay bạn đưa logo mới?

---

## 4. Khuôn thực tế trích xuất từ 2 file Word (kiểm chứng 05/09/2026)

Mổ trực tiếp `c++-level-1-quyen-1.docx` (3.802 đoạn, 233 bảng, 12 ảnh) và `quyen-2.docx` (2.996 đoạn, 152 bảng):

- **Khổ giấy:** A4 (595×842pt), lề trên/dưới/phải 36pt, lề gáy trái 64.3pt — khớp spec.
- **Headings (SỬA so với khuôn C++):** khuôn C++ dùng màu `0F4761` (xanh teal) — **sai so với spec, user đã bắt lỗi (Hình 1)**. Word Python dùng màu **`#1E293B`** cho toàn bộ H1/H2/H3/H4 (đen xám; Q1 inherit từ Normal, Q2 explicit — render giống nhau, đều đúng). Cỡ giữ nguyên: H1 20pt, H2 16pt, H3 14pt. Riêng `Bài tập thực hành` = H2 + direct formatting đỏ `#FF0000` 14pt Bold (giữ).
- **Normal:** Times New Roman 12.5pt, màu `#1E293B`, giãn dòng 264 (≈1.1).
- **Styles dùng nhiều nhất:** Compact (1.186) > First Paragraph (697) > Body Text (616) > Heading 3 (511) > Source Code (256) > Heading 2 (119) > Block Text (39).
- **Bảng:** 0 `tblHeader`, 626 `cantSplit`, 3.092 `oMath` — khớp spec.
- **Độ rộng cột bảng (quy tắc mới từ Hình 2):** bảng dữ liệu lý thuyết/dry-run dùng **autofit theo nội dung** (cột ít chữ như `int`/`float` thu hẹp, cột nhiều chữ giãn ra — tiết kiệm giấy in, hàng không bị kéo cao vô lý). Chỉ bảng Sample giữ width cố định theo spec (w=6800, cột 3400).
- **Header/Footer:** đủ 3 header (first/default/even) + watermark VML; footer số trang tự động `— PAGE —` (field thật, không phải text tĩnh).
- **Ảnh:** 12 PNG inline + `image13.jpeg` (logo watermark).
- **Cấu trúc mỗi quyển:** LỜI NÓI ĐẦU → CHƯƠNG (H1) → Bài (H1) → Phụ lục A → Phụ lục B (lời giải) → Mục lục (cuối sách).
- **Kết luận chiến thuật:** KHÔNG build Word từ số 0. **Clone `quyen-1.docx` làm khuôn** (giữ nguyên styles, header/watermark, TOC), chỉ thay nội dung Python vào. Mọi số liệu trên là tham số khóa cho script build.

## 5. Việc kỹ thuật đã rõ (làm ngay sau khi chốt C1–C6)

1. **SVG → PNG 300 DPI:** 13 file. Tool hiện chưa có (`resvg`/`cairosvg`/`libreoffice` đều thiếu) — cần `pip install cairosvg` (hoặc `brew install librsvg`) trước khi build. Không cần vẽ lại (đã light theme).
2. **Công cụ build:** `python-docx 1.2.0` đã có; `pandoc` đã có (dự phòng). Viết script `build_word_python.py` theo pipeline 4 bước của spec §7, nhưng bước 1 đổi thành **clone khuôn từ `quyen-1.docx`** (xóa body cũ, giữ styles/headers/watermark/TOC) thay vì dựng khổ giấy từ đầu.
3. **Nguồn đọc:** `lessons/*/Lesson*_Production_Content.md` + `lessons/*/Bai_Tap.md` + `problems/*/solution.py` (nếu C4b = Có). Không đọc `MASTER_ALL_LESSONS.md` trực tiếp (file dẫn xuất).
4. **Audit sau build:** watermark 100% trang, 0 `tblHeader`, Math 12pt, Sample IO centered + indent động, số trang footer, TOC.

---

## 5. Quy tắc cô đọng nội dung bài học cho bản in (đã chốt nguyên tắc)

- **Phạm vi: CHỈ lý thuyết.** 287 đề bài giữ nguyên 100%. 250 quiz không vào Word (digital only).
- **Kiểu "print profile":** markdown gốc giữ nguyên đầy đủ; script build render bản cô đọng. Không cắt trực tiếp file gốc.
- **Văn xuôi (~1.000 dòng): gọt ~30%** tay từng bài (bỏ lặp ý, giữ giọng văn). Không để script tự cắt.
- **Bảng + code + hình: giữ 100%.** Dry-run giữ tối đa 2 bảng/bài.

## 6. Đáp án S0 trích từ 2 file Word C++ (kiểm chứng trực tiếp)

- **Khối đề bài trong Word:** H3 `Bài XX [CODE]: Tên` → `Bối cảnh:` (First Paragraph) → `Nhiệm vụ:` (Body Text) → `Đầu vào (Input):` + dòng Compact → `Đầu ra (Output):` + dòng Compact → `Ví dụ mẫu (Sample 1):` + bảng Sample IO → `Giải thích:` + các đoạn Normal (căn trái). **Có mục Ràng buộc** (172 lượt trong Quyển 1) → xem C1.
- **Lời nói đầu:** P0 `LỜI NÓI ĐẦU` (Center) + First Paragraph chào mừng + 3 Body Text + 5 Compact gạch đầu dòng (Khái niệm / Mô hình / Mẫu cài đặt / Bài tập / Lời giải) + First Paragraph kết. Python viết lại theo khung này (bỏ từ thi cử).
- **Header:** trái `Trung tâm giáo dục & đào tạo tin học iKH`, phải `Giáo trình C++ cơ bản - quyển 1` → Python: `Giáo trình Python cơ bản - quyển N`.
- **Phụ lục A:** các H2 đánh số (`KHUNG TƯ DUY`, `KHUNG CHƯƠNG TRÌNH`, `BIẾN VÀ KIỂU DỮ LIỆU`, `NHẬP VÀ XUẤT`, `TOÁN TỬ VÀ BIỂU THỨC`, `ĐIỀU KIỆN — RẼ NHÁNH`...) → Phụ lục A Python mirror theo khung này.
- **Phụ lục B:** H2 `Chương XX — Bài XX: ...` + H3 `CODE — Tên bài` + code lời giải.
- **C1 chốt:** problems Python **không có** mục Ràng buộc → **bản Word cũng KHÔNG tự tạo thêm**. Khối đề bài Word Python gồm: H3 `Bài XX [CODE]: Tên` → Bối cảnh → Nhiệm vụ → Input → Output → Sample → Giải thích (hết, không Ràng buộc).
- **C2 chốt:** nội dung Python giữ sạch như hiện tại (0 từ cấm); không bê từ thi cử của sách C++ sang.
- **C5 chốt:** Lời nói đầu viết mới theo khung trên; tên sách `Giáo trình Python cơ bản - quyển N`; tên file `python-level-1-quyen-1.docx` / `python-level-1-quyen-2.docx` (theo quy ước C++).
- **C6 chốt:** tái dùng logo `image13.jpeg` làm watermark.

## 7. S2 — Cô đọng lý thuyết nghĩa là gì (định nghĩa chính xác)

- **Giữ 100%:** mọi bảng, mọi code ví dụ, mọi hình, mọi hộp cảnh báo/lưu ý, dry-run tối đa 2 bảng/bài.
- **Gọt ~30% văn xuôi:** xóa câu lặp ý (ví dụ L02 vừa có bảng 7 toán tử vừa có 4 đoạn văn giải thích lại y hệt bảng → giữ bảng, gọt văn); rút gọn mở đầu/kết đoạn dài; giữ nguyên giọng văn và thuật ngữ đã chốt.
- **Không đụng:** đề bài (100%), quiz (ngoài Word), solutions.
- **Cơ chế:** làm TAY từng bài, lưu bản cô đọng thành file riêng `lessons/lesson-XX/LessonXX_Print.md` (markdown gốc chi tiết giữ nguyên làm bản digital). Script build chỉ đọc file `*_Print.md`.
- **Thứ tự:** Quyển 1 (L01–L06) trước.

## 8. Steps thực hiện (chốt)

- [ ] **S1. Spec ảnh (plan only, antigravity build):** tool `cairosvg` (fallback `librsvg`), 13 SVG → PNG rộng 2800px (~300 DPI), nền trắng giữ nguyên, tên `py_img01..13.png`, đặt vào `courses/python-bang-a/assets_png/`.
- [x] **S2. Cô đọng lý thuyết Quyển 1 XONG** (file `lessons/lesson-0X/Lesson0X_Print.md`, đã verify): bảng/hình/code khớp 100% body gốc, 0 quiz, 0 từ cấm, **0 icon trang trí** (đã xóa `❌`/`⚠️`/`✅`; giữ `→`/`—` vì là nội dung).
  | Bài | Gốc | Print | Giữ |
  |---|---|---|---|
  | L01 | 430 | 272 | bảng 25/25, hình 3/3, code 40/40 fences |
  | L02 | 519 | 375 | bảng 61/61, code 42/42 fences |
  | L03 | 390 | 260 | bảng 21/21, hình 4/4, code 24/24 fences |
  | L04 | 469 | 229 | bảng 18/18, hình 1/1, code 22/22 fences |
  | L05 | 371 | 173 | bảng 13/13, hình 1/1, code 18/18 fences |
  | L06 | 417 | 192 | bảng 7/7, hình 1/1, code 18/18 fences |
- [x] **S2b. Cô đọng lý thuyết Quyển 2 XONG** (`Lesson07–14_Print.md`, đã verify): bảng/hình/code khớp body gốc, 0 quiz, 0 từ cấm, 0 icon (kể cả trong comment code và ô bảng; `? ✅/❌` trong dry-run thay bằng chữ Đúng/Sai).
- [x] **S3. Viết Phụ lục A Python XONG** (`reference/Phu_Luc_A_Python.md`, 329 dòng, 11 H2, code compile OK, 0 từ cấm).
- [x] **Lời nói đầu Q1 + Q2 XONG** (`reference/Loi_Noi_Dau_Quyen1.md`, `Loi_Noi_Dau_Quyen2.md`, theo khung C++, không từ thi cử).
- [ ] **S4. Build Word (antigravity, đọc `word_build_manifest.json` làm nguồn khóa duy nhất):** clone khuôn `quyen-1.docx` (giữ styles/header/watermark/TOC), nạp Lời nói đầu mới → Chương → Bài (từ `*_Print.md`) → đề bài (khối H3, **không** Ràng buộc; mỗi Sample 1 bảng riêng) → Phụ lục A → Phụ lục B (solutions chia quyển) → Mục lục field tự động cuối sách. Format căn chỉnh y hệt 2 file C++ (mục 4). Manifest đã verify: Q1 157 + Q2 130 = 287 đề, 0 thiếu.
- [ ] **S5. Build FULL Quyển 1** → audit → bạn duyệt in thử. Vòng 2 (15:47): ảnh treo đã xóa ✅; màu heading Q1 đúng (inherit Normal 1E293B) ✅; tên file đúng quy ước ✅. Còn lỗi thật: (1) câu TLE tự chế VẪN CÒN (chứng minh: không tồn tại trong cả Print lẫn Production); (2) bảng vẫn fixed-layout, 0 autofit (Hình 2 chưa sửa).
- [ ] **S6. Build full Quyển 2** (L07–L14, 130 đề + lời giải) → audit tương tự → bàn giao 2 file `.docx`.
- [ ] **S6. Build full Quyển 2** (L07–L14, 130 đề + lời giải) → audit tương tự → bàn giao 2 file `.docx`.

---
*S0 đã chốt hết từ 2 file C++. Không còn mục treo.*
