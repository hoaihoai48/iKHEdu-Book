# Kế Hoạch Chi Tiết & Quy Chuẩn Thực Thi: Xây Dựng Khóa Học Scratch Bảng A

**Tên khóa học:** Scratch — Tư duy Khối lệnh, Đồ họa & Thuật toán Thi đấu  
**Mã khóa học:** `scratch-bang-a` | **Đối tượng:** Học sinh Tiểu học 8–11 tuổi (định hướng Tin học trẻ Bảng A)  
**Tài liệu tham chiếu chuẩn:** [`docs/LO_TRINH_SCRATCH.md`](file:///Users/vu/Developer/ikhEdu_lessons/docs/LO_TRINH_SCRATCH.md) (Spec Rev 4.0) & [`docs/PLAN_PYTHON_TO_SCRATCH_LEVEL1.md`](file:///Users/vu/Developer/ikhEdu_lessons/docs/PLAN_PYTHON_TO_SCRATCH_LEVEL1.md)  
**File quản trị kế hoạch:** `docs/PLAN_BUILD_KHOA_HOC_SCRATCH.md`  

---

## 1. Hệ Thống 4 Nguồn Tài Liệu Thực Tế (Source Inventory)

Khóa học được xây dựng trên **100% tài liệu thật (Zero Dummy / Zero Placeholder)**, kết hợp chặt chẽ từ 4 nguồn tài nguyên có sẵn trong dự án:

1. 🎨 **`CHỦ ĐỀ VẼ HÌNH TRÊN SCRATCH.docx` (219 ảnh minh họa)**:
   - Nguồn chuyên đề **Bút vẽ Pen & Đồ họa** cho **Chương 1 (Bài 01 & Bài 02)**.
   - Chứa 59 câu bài tập hình học: đa giác đều (tam giác, vuông, ngũ giác, lục giác), cung tròn, cánh hoa, hoa tuyết, logo Olympic 5 vòng tròn, cầu vồng 7 màu, hoa thoi, hình xoắn ốc và mê cung.
   - Cung cấp **219 hình ảnh mẫu kết quả** để học sinh quan sát trực quan khi làm bài.
2. 🏆 **`DeTHT.docx` (285 ảnh minh họa, 117 đề thi Tin học trẻ chính thức)**:
   - Nguồn đề thi Tin học trẻ Bảng A toàn quốc qua các năm (2022–2025) từ Hà Nội, Bắc Giang, Nghệ An, Hà Tĩnh, Đà Nẵng, Bắc Ninh, Lâm Đồng, TP.HCM...
   - Cung cấp đề bài gốc, bối cảnh thực tế, bảng testcase chuẩn của Ban tổ chức.
   - Cung cấp **285 sơ đồ đề bài gốc** (đường chạy bộ, ma trận ô vuông, bảng chữ cái, đường ray xe lửa, bảng đèn led...) để nhúng trực tiếp vào đề bài Scratch.
3. 💻 **`52 bài lập trình Scratch.docx` (166 ảnh chụp khối lệnh mẫu)**:
   - Nguồn giải mẫu các bài toán Tin học trẻ bằng khối lệnh Scratch trực quan.
   - Cung cấp **166 ảnh chụp màn hình các khối lệnh Scratch thật** đã được lập trình và chạy thử thành công để đưa vào phần Hướng dẫn giảng dạy cho giáo viên.
4. 📚 **Kho bài tập chuẩn hóa Python Bảng A (`courses/python-bang-a/problems/` — 287 bài toán)**:
   - Nguồn bài tập toán học & thuật toán cho **Chương 2 đến Chương 6 (Bài 03 đến Bài 16)**.
   - Đã được phân tầng chuẩn $P0 \to P3$, có đầy đủ bối cảnh sư phạm, ràng buộc kỹ thuật và dữ liệu mẫu kiểm thử, ánh xạ 1-1 sang Scratch (`sca_l01_p01` $\longleftrightarrow$ `pya_l01_p01`).

---

## 2. Chiến Lược Hình Ảnh & Trực Quan Hóa 3 Trụ Cột

Đối với lứa tuổi 8–11 tuổi, khóa học **tuyệt đối không dùng văn bản khô khan**, 100% nội dung bài học và bài tập đều có hình ảnh trực quan:

```text
               CHIẾN LƯỢC HÌNH ẢNH TRỰC QUAN HÓA (VISUAL SUITE)
                                       │
        ┌──────────────────────────────┼──────────────────────────────┐
        ▼                              ▼                              ▼
 [1. KHỐI LỆNH SCRATCH 3.0]     [2. KHO ẢNH GỐC THỰC TẾ]      [3. SƠ ĐỒ SƯ PHẠM VECTOR]
  Render từ DSL sang SVG/PNG     Trích xuất 670+ ảnh từ        Vẽ đồ họa hệ tọa độ Oxy,
  chuẩn màu sắc & hình dạng      3 file docx (hình mẫu đề bài  mô hình hộp biến nhớ,
  (Mũ, C-block, Lục giác...)     và khối lệnh chụp thực tế).   ngăn kéo List, nổi bọt.
```

1. **Khối lệnh Scratch 3.0 Tiếng Việt dạng hình trực quan (Visual Block Rendering)**:
   - **100% Giao diện & Thuật ngữ Tiếng Việt (.vi)**: Học sinh Tiểu học (8–11 tuổi) học tập và thi Tin học trẻ Bảng A trên giao diện Scratch Tiếng Việt. Tuyệt đối không dùng mã lệnh Tiếng Anh (`when green flag clicked`, `erase all`, `pen up`...). Toàn bộ khối lệnh phải dùng thuật ngữ Tiếng Việt chuẩn: `khi bấm vào cờ xanh`, `xóa tất cả`, `nhấc bút`, `đặt bút`, `đi tới điểm x: () y: ()`, `đặt hướng bằng ()`, `lặp lại () lần`, `di chuyển () bước`, `xoay phải ↻ () độ`, `hỏi () và đợi`, `đặt [biến] thành ()`...
   - **Tuyệt đối không dùng code text box đen ngòm**: Không dùng khối code text monospace (` ```scratchblocks ` hay ` ```text `) làm học sinh nhầm lẫn với code văn bản. Mọi kịch bản mẫu bắt buộc phải nhúng **file ảnh vector/PNG trực quan (`![khối lệnh](assets/rendered_blocks/...)`)** hiển thị rõ ràng hình dáng khớp ghép puzzle (mũ, lồi, lõm, chữ C) và màu sắc nhận diện nhóm lệnh.
   - Khi nhắc câu lệnh trong văn bản hoặc bảng tra cứu, dùng biểu tượng màu sắc trực quan (như 🟡 `[khi bấm vào cờ xanh]`, 🟢 `[xóa tất cả]`, 🔵 `[đi tới điểm x: (0) y: (0)]`, 🟠 `[lặp lại () lần]`).
2. **Kho ảnh thực tế từ tài liệu gốc (670+ ảnh trích xuất)**:
   - Đã trích xuất toàn bộ hơn **670 hình ảnh** từ `CHỦ ĐỀ VẼ HÌNH TRÊN SCRATCH.docx` (219 ảnh), `DeTHT.docx` (285 ảnh), và `52 bài lập trình Scratch.docx` (166 ảnh).
   - Chỉ mục tại `courses/scratch-bang-a/assets/image_manifest.json` ánh xạ từng ảnh vào mã bài toán tương ứng.
3. **Sơ đồ nhận thức sư phạm (Scenario Diagrams)**:
   - Bộ hình vẽ vector minh họa: Hệ tọa độ sân khấu Scratch (trục X $-240..240$, trục Y $-180..180$, la bàn 4 hướng), mô hình "chiếc hộp dán nhãn" lưu trữ biến số và bẫy ghi đè `answer`, mô hình "tủ ngăn kéo" danh sách chỉ số bắt đầu từ 1.

---

## 3. Cấu Trúc Khóa Học & Quy Hoạch Thư Mục Chuẩn (`courses/scratch-bang-a/`)

Dưới đây là kiến trúc toàn diện của thư mục `courses/scratch-bang-a/` — được thiết kế đồng bộ với hệ thống xuất bản kép (Sách in Word/PDF & Web LMS DKOJ) của iKHEDU:

```text
courses/scratch-bang-a/
├── README.md                                    # Bản đồ khóa học, chuẩn đầu ra LO, quy tắc sư phạm, timebox 90'
├── BOOK_MASTER.md                               # Bản thảo canonical toàn khóa phục vụ biên dịch sách in Word/PDF
├── CURRICULUM_AUDIT.md                          # Ma trận kiểm toán chuẩn đầu ra (LO) & phân tầng độ khó P0-P3
├── word_build_manifest.json                     # Metadata xuất bản sách giáo trình học sinh
├── word_build_manifest_gv.json                  # Metadata xuất bản sách hướng dẫn giảng dạy giáo viên
├── build_word_scratch.py                        # Script biên dịch tự động sang Word giáo trình học sinh
├── build_word_teacher_scratch.py                # Script biên dịch tự động sang Word sách giáo viên
│
├── reference/                                   # Tài liệu tham khảo, cẩm nang và bảng tra cứu chuẩn
│   ├── SCRATCHBLOCKS_DSL_GUIDE.md               # Cẩm nang chuẩn hóa cú pháp viết mã khối text Scratchblocks
│   ├── BANG_CHUYEN_DOI_PYTHON_SCRATCH.md        # Từ điển 12 quy tắc chuyển giao thuật toán từ Python sang Scratch
│   └── KIEN_THUC_TRONG_TAM_CAN_NHO.md           # Bảng tra cứu khối lệnh, công thức hình học, bẫy lỗi lập trình
│
├── assets/                                      # Kho tài nguyên hình ảnh dùng chung toàn khóa
│   ├── image_manifest.json                      # File chỉ mục tra cứu ảnh theo mã bài toán (sca_pen_*, sca_l*)
│   ├── pen_drawings/                            # 219 ảnh mẫu hình vẽ thực tế trích từ CHỦ ĐỀ VẼ HÌNH TRÊN SCRATCH.docx
│   │   ├── pen_p01_da_giac_deu.png              # Hình mẫu tam giác đều, vuông, ngũ giác, lục giác
│   │   ├── pen_p05_vuong_dong_tam.png           # Hình mẫu hình vuông đồng tâm & bậc thang
│   │   ├── pen_p12_logo_olympic.png             # Hình mẫu logo Olympic 5 vòng tròn
│   │   ├── pen_p15_cau_vong_7_mau.png           # Hình mẫu cầu vồng 7 màu cung tròn 180 độ
│   │   └── pen_p16_bong_hoa_8_canh.png          # Hình mẫu bông hoa cánh cung đối xứng
│   ├── contest_scenarios/                       # 285 ảnh sơ đồ đề thi Tin học trẻ trích từ DeTHT.docx
│   │   ├── tht_duong_chay_bo.png                # Sơ đồ sân chạy bộ (THT Bắc Giang)
│   │   ├── tht_ma_tran_to_mau.png               # Sơ đồ ma trận chữ cái (THT Sơ khảo toàn quốc)
│   │   └── tht_bang_den_quang_cao.png           # Sơ đồ viền bóng đèn (THT Sơn Trà - Đà Nẵng)
│   ├── block_screenshots/                       # 166 ảnh chụp màn hình khối lệnh mẫu từ 52 bài Scratch
│   │   ├── sol_bong_den.png                     # Ảnh chụp khối lệnh giải bài Bóng đèn
│   │   └── sol_ho_ca_sau.png                    # Ảnh chụp khối lệnh giải bài Hồ cá sấu
│   ├── pedagogical_diagrams/                    # Sơ đồ vector minh họa bản chất nhận thức
│   │   ├── oxy_stage_coordinate_system.svg      # Sân khấu tọa độ Oxy (-240..240, -180..180, 4 hướng quay)
│   │   ├── variable_memory_box_model.svg        # Mô hình chiếc hộp RAM lưu biến số & bẫy ghi đè answer
│   │   ├── list_drawer_1_based_index.svg        # Mô hình tủ ngăn kéo List (chỉ số bắt đầu từ 1)
│   │   └── bubble_sort_swap_visual.svg          # Mô phỏng trực quan hoán đổi nổi bọt các thẻ số
│   └── rendered_blocks/                         # Ảnh vector khối lệnh tự động render từ file solution.dsl
│
├── lessons/                                     # 16 THƯ MỤC BÀI HỌC CHÍNH QUY (6 CHƯƠNG)
│   # --- CHƯƠNG 1: BÚT VẼ PEN & ĐỒ HỌA (TRACK 1: NATIVE SCRATCH FOUNDATION) ---
├── lesson-01-ve-hinh-pen-repeat/
│   │   ├── Lesson01_Production_Content.md        # Lý thuyết tọa độ, 4 hướng, đặt/nhấc bút, lặp 360/n, bẫy lỗi, 10 Quiz
│   │   └── Bai_Tap.md                           # Danh mục bài tập sca_pen_p00..p05, vd03 phân tầng P0-P3
│   ├── lesson-02-hinh-tron-cung-tron-hoa-van/
│   │   ├── Lesson02_Production_Content.md        # Lý thuyết đường cong 360 bước, My Blocks có tham số R, 10 Quiz
│   │   └── Bai_Tap.md                           # Danh mục bài tập sca_pen_p10..p18, vd04..vd07 phân tầng P0-P3
│   │
│   │   # --- CHƯƠNG 2: TÍNH TOÁN CƠ BẢN (KHỚP CHƯƠNG 1 PYTHON) ---
│   ├── lesson-03-lenh-xuat-nhap-bien-so-kieu-du-lieu/
│   │   ├── Lesson03_Production_Content.md        # Khớp Bài 01 Python: Lệnh xuất nhập, biến số và kiểu dữ liệu (12 Quiz)
│   │   └── Bai_Tap.md                           # 25 bài tập sca_l01_p01..p25 (nguồn pya_l01_*)
│   ├── lesson-04-toan-tu-va-bieu-thuc/
│   │   ├── Lesson04_Production_Content.md        # Khớp Bài 02 Python: Toán tử và biểu thức (12 Quiz)
│   │   └── Bai_Tap.md                           # 36 bài tập sca_l02_p01..p36 (nguồn pya_l02_*)
│   ├── lesson-05-phep-chia-nguyen-chia-du-luy-thua/
│   │   ├── Lesson05_Production_Content.md        # Khớp Bài 03 Python: Phép chia nguyên, chia dư và lũy thừa (12 Quiz)
│   │   └── Bai_Tap.md                           # 33 bài tập sca_l03_p01..p33 (nguồn pya_l03_*)
│   │
│   │   # --- CHƯƠNG 3: CẤU TRÚC RẼ NHÁNH & CẤU TRÚC VÒNG LẶP (KHỚP CHƯƠNG 2 PYTHON) ---
│   ├── lesson-06-cau-truc-re-nhanh-va-dieu-kien-logic/
│   │   ├── Lesson06_Production_Content.md        # Khớp Bài 04 Python: Cấu trúc rẽ nhánh và điều kiện logic (12 Quiz)
│   │   └── Bai_Tap.md                           # 37 bài tập sca_l04_p01..p37 (nguồn pya_l04/l05/l06_*)
│   ├── lesson-07-vong-lap-for-va-dem-tay/
│   │   ├── Lesson07_Production_Content.md        # Khớp Bài 05 Python: Vòng lặp for và hàm range (12 Quiz)
│   │   └── Bai_Tap.md                           # 14 bài tập sca_l05_p01..p14 (nguồn pya_l07_*)
│   ├── lesson-08-vong-lap-until-va-bien-co/
│   │   ├── Lesson08_Production_Content.md        # Khớp Bài 06 Python: Vòng lặp while, biến cờ và điều khiển vòng lặp (12 Quiz)
│   │   └── Bai_Tap.md                           # 12 bài tập sca_l06_p01..p12 (nguồn pya_l08_*)
│   │
│   │   # --- CHƯƠNG 4: BÀI TOÁN SỐ HỌC & TÁCH CHỮ SỐ (KHỚP CHƯƠNG 3 PYTHON) ---
│   ├── lesson-09-quy-luat-day-so-va-tam-giac-so/
│   │   ├── Lesson09_Production_Content.md        # Khớp Bài 07 Python: Quy luật dãy số và tam giác số (12 Quiz)
│   │   └── Bai_Tap.md                           # 14 bài tập sca_l07_p01..p14 (nguồn pya_l09_*)
│   ├── lesson-10-ky-thuat-tach-chu-so-so-nguyen/
│   │   ├── Lesson10_Production_Content.md        # Khớp Bài 08 Python: Kỹ thuật tách chữ số và xử lý số nguyên qua vòng lặp while (12 Quiz)
│   │   └── Bai_Tap.md                           # 14 bài tập sca_l08_p01..p14 (nguồn pya_l10_*)
│   ├── lesson-11-uoc-so-boi-so-va-so-nguyen-to/
│   │   ├── Lesson11_Production_Content.md        # Khớp Bài 09 Python: Ước số, bội số và số nguyên tố (12 Quiz)
│   │   └── Bai_Tap.md                           # 14 bài tập sca_l09_p01..p14 (nguồn pya_l11_*)
│   ├── lesson-12-dem-so-theo-quy-luat-va-so-dac-biet/
│   │   ├── Lesson12_Production_Content.md        # Khớp Bài 10 Python: Đếm số theo quy luật và số đặc biệt (12 Quiz)
│   │   └── Bai_Tap.md                           # 12 bài tập sca_l10_p01..p12 (nguồn pya_l12_*)
│   │
│   │   # --- CHƯƠNG 5: DANH SÁCH (LIST) & THỐNG KÊ (KHỚP CHƯƠNG 4 PYTHON) ---
│   ├── lesson-13-danh-sach-list-va-thao-tac-co-ban/
│   │   ├── Lesson13_Production_Content.md        # Khớp Bài 11 Python: Danh sách và thao tác cơ bản (12 Quiz)
│   │   └── Bai_Tap.md                           # 26 bài tập sca_l11_p01..p26 (nguồn pya_l16_*)
│   ├── lesson-14-thong-ke-danh-sach-va-sap-xep/
│   │   ├── Lesson14_Production_Content.md        # Khớp Bài 12 Python: Thống kê danh sách và sắp xếp (12 Quiz)
│   │   └── Bai_Tap.md                           # 14 bài tập sca_l12_p01..p14 (nguồn pya_l17_*)
│   │
│   │   # --- CHƯƠNG 6: XỬ LÝ CHUỖI KÝ TỰ (KHỚP CHƯƠNG 5 PYTHON) ---
│   ├── lesson-15-chuoi-ky-tu-chi-so-cat-lat/
│   │   ├── Lesson15_Production_Content.md        # Khớp Bài 13 Python: Chuỗi ký tự — Chỉ số, cắt lát và duyệt ký tự (12 Quiz)
│   │   └── Bai_Tap.md                           # 12 bài tập sca_l13_p01..p12 (nguồn pya_l13_*)
│   └── lesson-16-duyet-chuoi-bien-doi-ky-tu-tach-tu/
│       ├── Lesson16_Production_Content.md        # Khớp Bài 14 Python: Duyệt chuỗi, biến đổi ký tự và tách từ (12 Quiz)
│       └── Bai_Tap.md                           # 24 bài tập sca_l14_p01..p24 (nguồn pya_l14/l15_*)so-va-tam-giac-so/
│   │   ├── Lesson09_Production_Content.md        # Cấp số cộng, Fibonacci/Tribonacci cuộn chiếu, tam giác Floyd, 12 Quiz
│   │   └── Bai_Tap.md                           # Danh mục 14 bài tập sca_l07_p01..p14 (nguồn pya_l09_*)
│   ├── lesson-10-ky-thuat-tach-chu-so-so-nguyen/
│   │   ├── Lesson10_Production_Content.md        # until N=0, bóc mod 10, cắt floor(/10), Palindrome, Armstrong, 12 Quiz
│   │   └── Bai_Tap.md                           # Danh mục 14 bài tập sca_l08_p01..p14 (nguồn pya_l10_*)
│   ├── lesson-11-uoc-so-boi-so-va-so-nguyen-to/
│   │   ├── Lesson11_Production_Content.md        # Lặp tối ưu i*i<=n, cờ nguyên tố, thuật toán Euclid UCLN/BCNN, 12 Quiz
│   │   └── Bai_Tap.md                           # Danh mục 14 bài tập sca_l09_p01..p14 (nguồn pya_l11_*)
│   ├── lesson-12-dem-so-theo-quy-luat-va-so-dac-biet/
│   │   ├── Lesson12_Production_Content.md        # Đếm O(1) bao hàm-loại trừ, số hoàn hảo, cặp số thân thiết, 12 Quiz
│   │   └── Bai_Tap.md                           # Danh mục 12 bài tập sca_l10_p01..p12 (nguồn pya_l12_*)
│   │
│   │   # --- CHƯƠNG 5: DANH SÁCH (LIST) & THỐNG KÊ ---
│   ├── lesson-13-danh-sach-list-va-thao-tac-co-ban/
│   │   ├── Lesson13_Production_Content.md        # List 1-based, thêm/xóa/chèn, duyệt danh sách, lọc chẵn lẻ, 12 Quiz
│   │   └── Bai_Tap.md                           # Danh mục 26 bài tập sca_l11_p01..p26 (nguồn pya_l16_*)
│   ├── lesson-14-thong-ke-danh-sach-va-sap-xep/
│   │   ├── Lesson14_Production_Content.md        # Max/Min/Unique, cài đặt Bubble Sort khối lệnh trực quan, 12 Quiz
│   │   └── Bai_Tap.md                           # Danh mục 14 bài tập sca_l12_p01..p14 (nguồn pya_l17_*)
│   │
│   │   # --- CHƯƠNG 6: XỬ LÝ CHUỖI KÝ TỰ ---
│   ├── lesson-15-chuoi-ky-tu-chi-so-cat-lat/
│   │   ├── Lesson15_Production_Content.md        # letter of, length of, ghép ngược, soi từ đối xứng Palindrome, 12 Quiz
│   │   └── Bai_Tap.md                           # Danh mục 12 bài tập sca_l13_p01..p12 (nguồn pya_l13_*)
│   └── lesson-16-duyet-chuoi-bien-doi-ky-tu-tach-tu/
│       ├── Lesson16_Production_Content.md        # Đếm hoa/thường, thuật toán duyệt khoảng trắng tách từ vào List, Caesar, 12 Quiz
│       └── Bai_Tap.md                           # Danh mục 24 bài tập sca_l14_p01..p24 (nguồn pya_l14/l15_*)
│
├── problems/                                    # KHO PROBLEM PACKAGES ĐỘC LẬP (308 BÀI TOÁN THẬT)
│   ├── sca_pen_p00_setup_net_ve/                # Khởi tạo nét vẽ, tọa độ tâm, dấu cộng
│   │   ├── De_Bai.md                            # Đề bài student-facing (kèm ảnh mẫu nét vẽ)
│   │   ├── Huong_Dan_Giang_Day.md               # 9 phần sư phạm giáo viên + ảnh khối lệnh giải
│   │   ├── solution.dsl                         # Kịch bản Scratchblocks text chuẩn
│   │   └── interaction-check.json               # Kịch bản kiểm thử hành vi tương tác
│   ├── sca_pen_p01_da_giac_deu/                 # Vẽ tam giác đều, hình vuông, ngũ giác, lục giác
│   ├── sca_pen_p05_hinh_vuong_dong_tam/         # Vẽ 3 hình vuông đồng tâm & bậc thang
│   ├── sca_pen_p12_logo_olympic/                # Vẽ logo Olympic 5 vòng tròn
│   ├── sca_pen_p15_cau_vong_7_mau/              # Vẽ cầu vồng 7 màu cung tròn 180 độ
│   ├── sca_pen_p16_bong_hoa_8_canh/             # Vẽ bông hoa 8 cánh cung đối xứng
│   │   # ... (toàn bộ 21 bài vẽ hình Pen nền tảng)
│   ├── sca_l01_p01_loi_chao_robot/              # Lời chào robot (pya_l01_p01)
│   ├── sca_l01_p20_doi_thuoc_ke_milimet/        # Đổi thước kẻ mm (THTA Bắc Ninh)
│   ├── sca_l01_p24_ve_tham_quan_chua_huong/     # Vé tham quan chùa Hương (THTA Nghệ An)
│   ├── sca_l02_p05_bong_den_vien_bien_hieu/     # Bóng đèn viền biển hiệu (THTA Sơn Trà)
│   ├── sca_l02_p13_luy_thua_cau_thang/          # Cầu thang Mario (THTA Củ Chi)
│   ├── sca_l02_p26_trong_cay_dai_lo/            # Trồng cây đại lộ (THTA Toàn quốc)
│   ├── sca_l03_p08_thuan_di_gap_anh/            # Vận tốc Thuận Ánh (THTA Từ Sơn)
│   ├── sca_l03_p21_chu_vi_tam_giac_abc/         # Chu vi tam giác ABC (THTA Hà Tĩnh)
│   ├── sca_l03_p23_ho_ca_sau_va_dao_nho/        # Hồ cá sấu (THTA Lâm Đồng)
│   ├── sca_l04_p06_dien_phep_tinh_lon_nhat/     # Điền phép tính lớn nhất (THTA Bắc Giang)
│   └── ... (toàn bộ 287 bài toán thuật toán từ sca_l01_p01 đến sca_l14_p24)
│
└── tools/                                       # BỘ CÔNG CỤ TỰ ĐỘNG HÓA CỦA KHÓA HỌC
    ├── extract_docx_assets.py                   # Script tự động quét & giải nén 670+ ảnh từ 3 file docx
    ├── render_scratchblocks.py                  # Script gọi scratchblocks render solution.dsl sang SVG/PNG
    ├── verify_problem_packages.py               # Script kiểm tra tính toàn vẹn 308 bài (đủ 4 file, đúng ID)
    └── sync_book_master.py                      # Script đồng bộ tự động 16 bài học vào file BOOK_MASTER.md
```

---

## 4. Lộ Trình Triển Khai 6 Bước Chi Tiết (Detailed Step-by-Step)

### 🚀 Bước 1: Trích xuất & Lập chỉ mục Kho tài nguyên ảnh (Asset Pipeline)
- **Công việc cụ thể**:
  1. Viết script `tools/extract_docx_assets.py` quét và giải nén toàn bộ media từ:
     - `CHỦ ĐỀ VẼ HÌNH TRÊN SCRATCH.docx` $\to$ `courses/scratch-bang-a/assets/pen_drawings/`
     - `DeTHT.docx` $\to$ `courses/scratch-bang-a/assets/contest_scenarios/`
     - `52 bài lập trình Scratch.docx` $\to$ `courses/scratch-bang-a/assets/block_screenshots/`
  2. Tạo file chỉ mục `courses/scratch-bang-a/assets/image_manifest.json` ghi nhận: tên file, kích thước, bài học liên quan và bài tập đích.
- **Tiêu chuẩn nghiệm thu (Gate 1)**: Thư mục `assets/` có đầy đủ hơn 670 ảnh, file manifest có thể tra cứu nhanh tên ảnh theo mã bài (`sca_pen_*`, `sca_l*`).

---

### 🚀 Bước 2: Khởi tạo Scaffolding & Shared Infrastructure
- **Công việc cụ thể**:
  1. Tạo cây thư mục khóa học `courses/scratch-bang-a/` và các thư mục con `lessons/`, `problems/`, `reference/`.
  2. Biên soạn file điều hướng tổng thể `courses/scratch-bang-a/README.md` (giới thiệu mục tiêu, đối tượng học sinh, lộ trình 6 Chương — 16 Bài).
  3. Biên soạn tài liệu quy chuẩn cú pháp khối lệnh text `reference/SCRATCHBLOCKS_DSL_GUIDE.md` làm từ điển chuẩn cho việc viết mã nguồn `.dsl`.
- **Tiêu chuẩn nghiệm thu (Gate 2)**: Cây thư mục được tạo sạch sẽ, README điều hướng rõ ràng, tài liệu DSL khóa toàn bộ cú pháp khối lệnh.

---

### 🚀 Bước 3: Triển khai Track 1 — Bút Vẽ Pen Bản Địa (Bài 01 & Bài 02)
- **Nguồn dữ liệu**: `CHỦ ĐỀ VẼ HÌNH TRÊN SCRATCH.docx` (kho bài `sca_pen_p00..p18`, `vd01..vd07`).
- **Nội dung thực hiện**:
  1. **Bài 01: Vẽ hình với Pen và Repeat**
     - `Lesson01_Production_Content.md`: Khám phá tọa độ sân khấu, 4 hướng quay, khối lệnh đặt/nhấc bút, đổi màu/nét vẽ, công thức lặp $\text{Góc quay} = 360^\circ / n$, bẫy quên xóa màn hình, bẫy quên nhấc bút khi di chuyển.
     - **10 câu Concept Quiz** đo lường chuẩn đầu ra (có đáp án + giải thích).
     - `Bai_Tap.md`: Danh mục bài tập 2 trục P0–P3.
     - Đóng gói các Problem Packages thật: `sca_pen_p00` (Setup & nét vẽ), `sca_pen_p01` (4 đa giác đều), `sca_pen_p02..p04` (vẽ theo mẫu), `sca_pen_p05` (vuông đồng tâm & bậc thang) — **mỗi bài nhúng trực tiếp ảnh mẫu kết quả từ kho ảnh**.
  2. **Bài 02: Hình tròn, Cung tròn và Hoa văn**
     - `Lesson02_Production_Content.md`: Khám phá đường cong từ 360 bước ngắn, công thức bước đi $(2 \times R \times 3.14)/360$, My Blocks tham số bán kính, chế độ chạy không làm mới màn hình (Run-without-refresh) chống giật.
     - **10 câu Concept Quiz**.
     - `Bai_Tap.md` và đóng gói Problem Packages thật: Cầu vồng 7 màu, Cánh hoa đối xứng, Hoa tuyết 8 cánh, Logo Olympic 5 vòng tròn.
- **Tiêu chuẩn nghiệm thu (Gate 3)**: Hoàn thành 2 bài học đồ họa, 20 câu Quiz, 21 Problem Packages thật kèm ảnh kết quả và code DSL.

---

### 🚀 Bước 4: Triển khai Track 2 — Tính Toán Cơ Bản Chương 2 (Bài 03, 04, 05)
- **Nguồn dữ liệu**: 94 bài toán thật từ `courses/python-bang-a/problems/` (`pya_l01_*`, `pya_l02_*`, `pya_l03_*`) đối chiếu với `DeTHT.docx` và `52 bài lập trình Scratch.docx`.
- **Nội dung thực hiện**:
  1. **Bài 03: Lệnh xuất nhập, biến số và kiểu dữ liệu** (L01 Python):
     - Lý thuyết `ask/answer/say`, cơ chế lưu biến vào RAM, bẫy ghi đè `answer`, hoán đổi giá trị qua biến tạm.
     - 12 câu Quiz.
     - Chuyển giao trọn vẹn **25 bài tập thật** (`sca_l01_p01..p25`): *Lời chào robot, Cặp số nhân đôi, Đổi thước kẻ mm (THT Bắc Ninh), Vé tham quan chùa Hương (THT Nghệ An)...*
  2. **Bài 04: Toán tử và biểu thức** (L02 Python):
     - Lý thuyết biểu thức lồng khối (thay thế dấu ngoặc đơn), thứ tự ưu tiên tính toán, lũy thừa $A \times A$, phép chia kẹo, bóc chữ số tận cùng.
     - 12 câu Quiz.
     - Chuyển giao trọn vẹn **36 bài tập thật** (`sca_l02_p01..p36`): *Bóng đèn viền biển hiệu (THT Sơn Trà), Trồng cây đại lộ (THT Toàn quốc), Cầu thang Mario (THT Củ Chi)...*
  3. **Bài 05: Phép chia nguyên, chia dư và lũy thừa** (L03 Python):
     - Lý thuyết `floor(A/B)`, phép toán `mod`, quy đổi thời gian $H:M:S$, tính toán hình học thực tế.
     - 12 câu Quiz.
     - Chuyển giao trọn vẹn **33 bài tập thật** (`sca_l03_p01..p33`): *Hồ cá sấu (THT Lâm Đồng), Vận tốc Thuận Ánh (THT Từ Sơn), Gạch lát sân trường...*
- **Tiêu chuẩn nghiệm thu (Gate 4)**: Hoàn thành 3 bài học, 36 câu Quiz, 94 bài toán thật có kịch bản tương tác `interaction-check` và ảnh khối lệnh giải mẫu.

---

### 🚀 Bước 5: Triển khai Cấu Trúc Điều Khiển Chương 3 (Bài 06, 07, 08)
- **Nguồn dữ liệu**: 63 bài toán thật từ `courses/python-bang-a/problems/` (`pya_l04/l05/l06_*`, `pya_l07_*`, `pya_l08_*`).
- **Nội dung thực hiện**:
  1. **Bài 06: Cấu trúc rẽ nhánh** (37 bài `sca_l04_p01..p37`): Khối `if`, `if...else`, lồng điều kiện, toán tử logic `and / or / not`, bài toán năm nhuận, cước taxi, phân loại tam giác, điền phép tính (THT Bắc Giang).
  2. **Bài 07: Vòng lặp for và hàm range** (14 bài `sca_l05_p01..p14`): Khối `repeat n` kết hợp biến đếm tay `i`, tích dồn/tổng dồn, bảng cửu chương, đếm ước số, tam giác dấu sao.
  3. **Bài 08: Vòng lặp while và biến cờ** (12 bài `sca_l06_p01..p12`): Khối `repeat until` (phân tích bẫy tư duy điều kiện ngược so với `while`), biến cờ hiệu (flag 0/1), trò chơi đoán số nhị phân, gấp giấy lên mặt trăng, bẫy treo vô tận.
- **Tiêu chuẩn nghiệm thu (Gate 5)**: Hoàn thành 3 bài học, 36 câu Quiz, 63 bài toán thật.

---

### 🚀 Bước 6: Triển khai Số Học, Danh Sách & Chuỗi Ký Tự (Bài 09 đến Bài 16)
- **Nguồn dữ liệu**: 130 bài toán thật từ `courses/python-bang-a/problems/` (`pya_l09_*` đến `pya_l17_*`).
- **Nội dung thực hiện**:
  1. **Chương 4: Bài toán số học & Tách chữ số (Bài 09–12, 54 bài thật)**:
     - Bài 09 (Dãy số & Tam giác số): Cấp số cộng, dãy Fibonacci/Tribonacci cuộn chiếu biến tạm, tam giác Floyd.
     - Bài 10 (Kỹ thuật tách chữ số): Khung lặp `until N = 0`, bóc `mod 10` và cắt `floor(/10)`, số Palindrome đối xứng, số Armstrong.
     - Bài 11 (Ước số, Bội số & Số nguyên tố): Định lý lặp $i \times i \le n$ chống giật máy tính, thuật toán Euclid tìm UCLN/BCNN.
     - Bài 12 (Đếm số theo quy luật & Số đặc biệt): Đếm $O(1)$ bao hàm-loại trừ, kiểm tra số hoàn hảo, cặp số thân thiết.
  2. **Chương 5: Danh sách (List) & Thống kê (Bài 13–14, 40 bài thật)**:
     - Bài 13 (Danh sách cơ bản): Cơ chế danh sách khối lệnh Scratch, **đặc biệt chỉ số bắt đầu từ 1 (1-based index)**, duyệt danh sách, tìm kiếm phần tử, lọc danh sách chẵn lẻ.
     - Bài 14 (Thống kê danh sách & Sắp xếp): Tìm Max/Min/Unique, cài đặt thuật toán **Sắp xếp nổi bọt (Bubble Sort)** trực quan bằng khối lệnh.
  3. **Chương 6: Xử lý chuỗi ký tự (Bài 15–16, 36 bài thật)**:
     - Bài 15 (Chuỗi ký tự — Chỉ số & Cắt lát): Khối `letter of`, `length of`, duyệt chuỗi, ghép ngược kiểm tra từ đối xứng Palindrome.
     - Bài 16 (Duyệt chuỗi, Biến đổi & Tách từ): Đếm ký tự hoa/thường, thuật toán duyệt khoảng trắng tách từ nạp vào List, mã hóa mật thư Caesar, nén xâu Run-Length.
- **Tiêu chuẩn nghiệm thu (Gate 6)**: Hoàn thành trọn vẹn 8 bài học còn lại, hoàn tất 100% mục tiêu **16 Bài học & 308 Problem Packages thật**.

---

## 5. Quy Chuẩn Đóng Gói 1 Problem Package Scratch

Mọi bài toán được lưu trong thư mục `courses/scratch-bang-a/problems/[ma_bai]/` phải có đủ 4 thành phần:

1. **`De_Bai.md` (Dành cho học sinh)**:
   - `# Tiêu đề bài toán` (gợi hình đời sống, gắn với sân khấu Scratch).
   - `## Bối cảnh` (cốt truyện sinh động, nhân vật chú Mèo, robot hoặc đề thi Tin học trẻ).
   - `## Nhiệm vụ` ("Em hãy lập trình giúp chú Mèo...").
   - `## Kịch bản tương tác (Input Scenario)`: Chú Mèo hỏi mấy câu, dữ liệu nhập vào là gì.
   - `## Kết quả mong đợi (Expected Behavior / Output)`: Chú Mèo nói (`say`) câu gì, vẽ ra hình gì trên sân khấu.
   - `## Sample 1`: Kịch bản mẫu + **Giải thích trace từng bước (TUYỆT ĐỐI CẤM SPOIL THUẬT TOÁN)**.
   - `## Hình ảnh minh họa`: Nhúng trực tiếp ảnh mẫu kết quả (đối với bài Pen) hoặc sơ đồ bối cảnh (đối với bài toán).
2. **`Huong_Dan_Giang_Day.md` (Dành cho giáo viên)**:
   - Đủ chuẩn 9 phần sư phạm: (1) Chuẩn đầu ra LO, (2) Phân tích đề & Edge cases, (3) Câu hỏi gợi mở Socratic, (4) Bất biến thuật toán, (5) Bảng chạy thử Dry-run, (6) Độ phức tạp, (7) Bẫy lỗi thường gặp, (8) Mã khối lệnh tham chiếu + ảnh chụp khối lệnh thật, (9) Mở rộng bài toán.
3. **`solution.dsl`**:
   - Mã nguồn khối lệnh dạng text Scratchblocks chuẩn, sẵn sàng render thành ảnh SVG/PNG.
4. **`interaction-check.json`**:
   - Bộ kịch bản kiểm thử tương tác (input sequence $\to$ expected state / say text).

---

## 6. Sẵn Sàng Tiến Hành (Action Trigger)

Kế hoạch đã được chuẩn hóa chi tiết từng bước. Bước hành động đầu tiên sẽ thực hiện ngay:
👉 **Chạy script trích xuất toàn bộ hơn 670 ảnh từ 3 file docx vào `courses/scratch-bang-a/assets/` và khởi tạo bộ khung khóa học.**
