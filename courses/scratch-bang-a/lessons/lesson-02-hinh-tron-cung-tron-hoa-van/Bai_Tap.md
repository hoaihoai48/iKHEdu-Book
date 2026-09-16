# DANH SÁCH BÀI TẬP THỰC HÀNH: BÀI 02 — HÌNH TRÒN, CUNG TRÒN VÀ HOA VĂN

**Khóa học:** iKHEDU Scratch — Bảng A (Level 1)  
**Chuyên đề:** Chương 1: Bút Vẽ Pen & Đồ Họa  
> **Tổng số bài tập thực hành:** `15 bài` chuẩn hóa 100% (Từ kho bài tập `courses/scratch-bang-a/problems/`).  

---

## 1. Ma Trận Phân Tầng Bài Tập Toàn Diện

| STT | Mã bài toán | Tên bài tập | Phân tầng | Mức nhận thức | Thao tác trọng tâm |
|:---:|---|---|:---:|:---:|---|
| 1 | `sca_pen_p21_hinh_tron_co_ban` | Hình Tròn Chuẩn Bằng 360 Bước Cong | **P0** | Khởi động & Quan sát | Lập trình vẽ hình tròn bán kính R theo công thức bước đi bướ... |
| 2 | `sca_pen_p22_hinh_tron_dong_tam_da_sac` | Hình Tròn Đồng Tâm Đa Sắc | **P0** | Khởi động & Quan sát | Viết thủ tục vẽ hình tròn với tham số bán kính, sau đó vẽ cá... |
| 3 | `sca_pen_p23_logo_olympic_5_mau` | Biểu Tượng 5 Vòng Tròn Olympic | **P0** | Khởi động & Quan sát | Lập trình vẽ chính xác 5 vòng tròn nét to (size = 10) tại cá... |
| 4 | `sca_pen_p24_cung_tron_cau_vong_7_mau` | Cầu Vồng 7 Sắc Rực Rỡ | **P1** | Cơ bản & Hoàn thành | Vẽ 7 cung tròn 180 độ lồng nhau với nét vẽ dày 12, theo thứ ... |
| 5 | `sca_pen_p25_canh_hoa_cung_tron_90` | Cánh Hoa Mảnh Ghép Cung Tròn 90 Độ | **P1** | Cơ bản & Hoàn thành | Tạo thủ tục Canh_Hoa: Lặp 2 lần [Lặp 90 lần (đi, xoay 1 độ),... |
| 6 | `sca_pen_p26_bong_hoa_da_canh` | Bông Hoa K Cánh Nở Rộ | **P1** | Cơ bản & Hoàn thành | Sử dụng thủ tục Canh_Hoa, xoay quanh tâm 360 / K độ để vẽ bô... |
| 7 | `sca_pen_p27_chong_chong_gio` | Chong Chóng Gió Xoay Tít | **P1** | Cơ bản & Hoàn thành | Vẽ các cánh chong chóng lệch tâm cong vút kết hợp màu sắc tư... |
| 8 | `sca_pen_p28_bong_hoa_tuyet_pha_le` | Bông Hoa Tuyết Pha Lê 6 Nhánh | **P2** | Luyện tập & Vận dụng | Tạo thủ tục Nhánh_Tuyết có các nhánh con đối xứng, sau đó lặ... |
| 9 | `sca_pen_p29_hinh_tron_khuyet` | Vầng Trăng Khuyết Nghệ Thuật | **P2** | Luyện tập & Vận dụng | Vẽ cung tròn lớn, sau đó quay ngược lại vẽ cung tròn nhỏ để ... |
| 10 | `sca_pen_p30_chia_banh_pizza_n_phan` | Chia Bánh Pizza N Miếng Đa Sắc | **P2** | Luyện tập & Vận dụng | Vẽ đường tròn và các nan quạt từ tâm ra đường viền, chia góc... |
| 11 | `sca_pen_p31_hoa_van_xoan_oc` | Vỏ Ốc Xoắn Archimedes | **P2** | Luyện tập & Vận dụng | Vòng lặp vẽ đường cong với bán kính hoặc bước đi tăng dần sa... |
| 12 | `sca_pen_p32_chuoi_vong_ngoc_trai` | Chuỗi Vòng Ngọc Trai Lấp Lánh | **P3** | Vận dụng cao & Sáng tạo | Đi theo đường tròn lớn, tại mỗi khoảng cách đều đặn dừng lại... |
| 13 | `sca_pen_p33_hoa_tiet_trang_tri_vien` | Họa Tiết Đường Viền Sóng Biển | **P3** | Vận dụng cao & Sáng tạo | Lặp lại N lần cung tròn 180 độ uốn lượn liên tiếp theo chiều... |
| 14 | `sca_pen_p34_hoa_van_gach_hoa_co_dien` | Gạch Hoa Cổ Điển Đông Dương | **P3** | Vận dụng cao & Sáng tạo | Vẽ hình vuông trung tâm và 4 cánh hoa uốn cong tại 4 cạnh hì... |
| 15 | `sca_pen_p35_dai_ngan_ha_van_hoa` | Kính Vạn Hoa Đa Chiều (Kaleidoscope) | **P3** | Vận dụng cao & Sáng tạo | Xoay một cụm họa tiết gồm đa giác và cung tròn 36 lần quanh ... |

---

## 2. Chi Tiết Từng Bài Tập Thực Hành

### Bài 1 (P0): Hình Tròn Chuẩn Bằng 360 Bước Cong
* **Mã bài toán:** `sca_pen_p21_hinh_tron_co_ban`
* **Độ khó & Phân tầng:** P0 (Khởi động & Quan sát)
* **Bối cảnh:** Khám phá bí mật đường cong: Hình tròn thực chất là một đa giác 360 cạnh siêu nhỏ.
* **Nhiệm vụ:** Lập trình vẽ hình tròn bán kính R theo công thức bước đi bước_cong = (2 * 3.14 * R) / 360.
* **Dữ liệu vào (Input):** Nhập bán kính R từ bàn phím.
* **Kết quả ra (Output):** Đường tròn tròn xoe, mượt mà không góc cạnh.
* **Dữ liệu mẫu (Sample):**

### Input
```text
Sự kiện: Nhập bán kính R từ bàn phím.
```

### Output
```text
Kết quả: Đường tròn tròn xoe, mượt mà không góc cạnh.
```

### Giải thích

Lặp 360 [đi bước_cong, xoay phải 1 độ].

---

### Bài 2 (P0): Hình Tròn Đồng Tâm Đa Sắc
* **Mã bài toán:** `sca_pen_p22_hinh_tron_dong_tam_da_sac`
* **Độ khó & Phân tầng:** P0 (Khởi động & Quan sát)
* **Bối cảnh:** Tấm bia bắn cung Thế vận hội gồm 5 vòng tròn đồng tâm với các màu sắc: vàng, đỏ, xanh lam, đen, trắng.
* **Nhiệm vụ:** Viết thủ tục vẽ hình tròn với tham số bán kính, sau đó vẽ các vòng tròn có bán kính tăng dần cùng tâm (0,0).
* **Dữ liệu vào (Input):** Nhập số vòng tròn N.
* **Kết quả ra (Output):** Bia ngắm bắn hình tròn đồng tâm rực rỡ.
* **Dữ liệu mẫu (Sample):**

### Input
```text
Sự kiện: Nhập số vòng tròn N.
```

### Output
```text
Kết quả: Bia ngắm bắn hình tròn đồng tâm rực rỡ.
```

### Giải thích

R = 30, 60, 90, 120...

---

### Bài 3 (P0): Biểu Tượng 5 Vòng Tròn Olympic
* **Mã bài toán:** `sca_pen_p23_logo_olympic_5_mau`
* **Độ khó & Phân tầng:** P0 (Khởi động & Quan sát)
* **Bối cảnh:** Logo Thế vận hội Olympic gồm 5 vòng tròn đan xen nhau đại diện cho 5 châu lục: Xanh lam, Vàng, Đen, Xanh lá, Đỏ.
* **Nhiệm vụ:** Lập trình vẽ chính xác 5 vòng tròn nét to (size = 10) tại các tọa độ chuẩn xác lồng vào nhau.
* **Dữ liệu vào (Input):** Nhấn cờ xanh.
* **Kết quả ra (Output):** Logo Olympic hoàn chỉnh đúng chuẩn quốc tế.
* **Dữ liệu mẫu (Sample):**

### Input
```text
Sự kiện: Nhấn cờ xanh.
```

### Output
```text
Kết quả: Logo Olympic hoàn chỉnh đúng chuẩn quốc tế.
```

### Giải thích

3 vòng hàng trên, 2 vòng so le hàng dưới.

---

### Bài 4 (P1): Cầu Vồng 7 Sắc Rực Rỡ
* **Mã bài toán:** `sca_pen_p24_cung_tron_cau_vong_7_mau`
* **Độ khó & Phân tầng:** P1 (Cơ bản & Hoàn thành)
* **Bối cảnh:** Sau cơn mưa rào, một chiếc cầu vồng 7 sắc xuất hiện uốn cong trên bầu trời.
* **Nhiệm vụ:** Vẽ 7 cung tròn 180 độ lồng nhau với nét vẽ dày 12, theo thứ tự màu: Đỏ, Cam, Vàng, Lục, Lam, Chàm, Tím.
* **Dữ liệu vào (Input):** Nhấn cờ xanh.
* **Kết quả ra (Output):** Cầu vồng 7 sắc cong vút tuyệt đẹp.
* **Dữ liệu mẫu (Sample):**

### Input
```text
Sự kiện: Nhấn cờ xanh.
```

### Output
```text
Kết quả: Cầu vồng 7 sắc cong vút tuyệt đẹp.
```

### Giải thích

Cung tròn 180 độ: lặp 180 [đi bước_cong, xoay 1 độ].

---

### Bài 5 (P1): Cánh Hoa Mảnh Ghép Cung Tròn 90 Độ
* **Mã bài toán:** `sca_pen_p25_canh_hoa_cung_tron_90`
* **Độ khó & Phân tầng:** P1 (Cơ bản & Hoàn thành)
* **Bối cảnh:** Một cánh hoa mềm mại được tạo thành bởi 2 cung tròn 90 độ khép cong đối xứng nhau.
* **Nhiệm vụ:** Tạo thủ tục Canh_Hoa: Lặp 2 lần [Lặp 90 lần (đi, xoay 1 độ), xoay phải 90 độ].
* **Dữ liệu vào (Input):** Nhấn cờ xanh.
* **Kết quả ra (Output):** Một cánh hoa hình thoi cong thanh thoát.
* **Dữ liệu mẫu (Sample):**

### Input
```text
Sự kiện: Nhấn cờ xanh.
```

### Output
```text
Kết quả: Một cánh hoa hình thoi cong thanh thoát.
```

### Giải thích

Hai cung tròn 90 độ cong úp vào nhau.

---

### Bài 6 (P1): Bông Hoa K Cánh Nở Rộ
* **Mã bài toán:** `sca_pen_p26_bong_hoa_da_canh`
* **Độ khó & Phân tầng:** P1 (Cơ bản & Hoàn thành)
* **Bối cảnh:** Từ cánh hoa cơ bản, ta có thể tạo ra bông hoa 6 cánh, 8 cánh hoặc 12 cánh bằng cách quay quanh tâm.
* **Nhiệm vụ:** Sử dụng thủ tục Canh_Hoa, xoay quanh tâm 360 / K độ để vẽ bông hoa K cánh đổi màu.
* **Dữ liệu vào (Input):** Nhập số cánh hoa K từ bàn phím.
* **Kết quả ra (Output):** Bông hoa đa cánh nở rộ rực rỡ.
* **Dữ liệu mẫu (Sample):**

### Input
```text
Sự kiện: Nhập số cánh hoa K từ bàn phím.
```

### Output
```text
Kết quả: Bông hoa đa cánh nở rộ rực rỡ.
```

### Giải thích

K = 8 cánh -> Xoay mỗi lần 45 độ.

---

### Bài 7 (P1): Chong Chóng Gió Xoay Tít
* **Mã bài toán:** `sca_pen_p27_chong_chong_gio`
* **Độ khó & Phân tầng:** P1 (Cơ bản & Hoàn thành)
* **Bối cảnh:** Chiếc chong chóng gió tuổi thơ quay tít trước hiên nhà trong những ngày hè lộng gió.
* **Nhiệm vụ:** Vẽ các cánh chong chóng lệch tâm cong vút kết hợp màu sắc tương phản.
* **Dữ liệu vào (Input):** Nhập số cánh chong chóng (4 hoặc 6).
* **Kết quả ra (Output):** Chong chóng gió chuyển động xoay đều.
* **Dữ liệu mẫu (Sample):**

### Input
```text
Sự kiện: Nhập số cánh chong chóng (4 hoặc 6).
```

### Output
```text
Kết quả: Chong chóng gió chuyển động xoay đều.
```

### Giải thích

Vẽ 4 cánh chong chóng xoay góc 90 độ.

---

### Bài 8 (P2): Bông Hoa Tuyết Pha Lê 6 Nhánh
* **Mã bài toán:** `sca_pen_p28_bong_hoa_tuyet_pha_le`
* **Độ khó & Phân tầng:** P2 (Luyện tập & Vận dụng)
* **Bối cảnh:** Những bông hoa tuyết mùa đông rơi xuống mang hình dạng đối xứng 6 nhánh tinh xảo.
* **Nhiệm vụ:** Tạo thủ tục Nhánh_Tuyết có các nhánh con đối xứng, sau đó lặp lại 6 lần quanh tâm.
* **Dữ liệu vào (Input):** Nhấn cờ xanh.
* **Kết quả ra (Output):** Bông hoa tuyết pha lê màu xanh lấp lánh.
* **Dữ liệu mẫu (Sample):**

### Input
```text
Sự kiện: Nhấn cờ xanh.
```

### Output
```text
Kết quả: Bông hoa tuyết pha lê màu xanh lấp lánh.
```

### Giải thích

6 nhánh tuyết xoay góc 60 độ quanh tâm.

---

### Bài 9 (P2): Vầng Trăng Khuyết Nghệ Thuật
* **Mã bài toán:** `sca_pen_p29_hinh_tron_khuyet`
* **Độ khó & Phân tầng:** P2 (Luyện tập & Vận dụng)
* **Bối cảnh:** Bầu trời đêm rằm với vầng trăng khuyết dịu dàng chiếu sáng không gian.
* **Nhiệm vụ:** Vẽ cung tròn lớn, sau đó quay ngược lại vẽ cung tròn nhỏ để tạo hình trăng khuyết.
* **Dữ liệu vào (Input):** Nhấn cờ xanh.
* **Kết quả ra (Output):** Hình vầng trăng khuyết màu vàng óng ả.
* **Dữ liệu mẫu (Sample):**

### Input
```text
Sự kiện: Nhấn cờ xanh.
```

### Output
```text
Kết quả: Hình vầng trăng khuyết màu vàng óng ả.
```

### Giải thích

Cung tròn ngoài bán kính lớn, cung trong bán kính nhỏ.

---

### Bài 10 (P2): Chia Bánh Pizza N Miếng Đa Sắc
* **Mã bài toán:** `sca_pen_p30_chia_banh_pizza_n_phan`
* **Độ khó & Phân tầng:** P2 (Luyện tập & Vận dụng)
* **Bối cảnh:** Bữa tiệc sinh nhật có chiếc bánh pizza tròn cần chia đều cho N bạn nhỏ, mỗi miếng một vị và màu sắc khác nhau.
* **Nhiệm vụ:** Vẽ đường tròn và các nan quạt từ tâm ra đường viền, chia góc 360 / N độ.
* **Dữ liệu vào (Input):** Nhập số phần N (ví dụ N = 6 hoặc 8).
* **Kết quả ra (Output):** Chiếc bánh tròn được chia thành N nan quạt màu sắc rực rỡ.
* **Dữ liệu mẫu (Sample):**

### Input
```text
Sự kiện: Nhập số phần N (ví dụ N = 6 hoặc 8).
```

### Output
```text
Kết quả: Chiếc bánh tròn được chia thành N nan quạt màu sắc rực rỡ.
```

### Giải thích

Mỗi nan quạt đi từ tâm ra bán kính R, xoay góc, đi về tâm.

---

### Bài 11 (P2): Vỏ Ốc Xoắn Archimedes
* **Mã bài toán:** `sca_pen_p31_hoa_van_xoan_oc`
* **Độ khó & Phân tầng:** P2 (Luyện tập & Vận dụng)
* **Bối cảnh:** Quy luật xoắn ốc tuyệt mỹ trong thiên nhiên được tìm thấy trên vỏ ốc biển và dải ngân hà.
* **Nhiệm vụ:** Vòng lặp vẽ đường cong với bán kính hoặc bước đi tăng dần sau mỗi góc xoay nhỏ.
* **Dữ liệu vào (Input):** Nhấn cờ xanh.
* **Kết quả ra (Output):** Đường xoắn ốc Archimedes mượt mà từ tâm lan tỏa ra ngoài.
* **Dữ liệu mẫu (Sample):**

### Input
```text
Sự kiện: Nhấn cờ xanh.
```

### Output
```text
Kết quả: Đường xoắn ốc Archimedes mượt mà từ tâm lan tỏa ra ngoài.
```

### Giải thích

Lặp 500 lần: đi (i * 0.05) bước, xoay 5 độ.

---

### Bài 12 (P3): Chuỗi Vòng Ngọc Trai Lấp Lánh
* **Mã bài toán:** `sca_pen_p32_chuoi_vong_ngoc_trai`
* **Độ khó & Phân tầng:** P3 (Vận dụng cao & Sáng tạo)
* **Bối cảnh:** Chuỗi vòng cổ quý phái đính các viên ngọc trai tròn xoe xếp đều trên một đường tròn lớn.
* **Nhiệm vụ:** Đi theo đường tròn lớn, tại mỗi khoảng cách đều đặn dừng lại vẽ một viên ngọc trai nhỏ.
* **Dữ liệu vào (Input):** Nhập số lượng hạt ngọc trai K.
* **Kết quả ra (Output):** Chuỗi vòng ngọc trai lộng lẫy.
* **Dữ liệu mẫu (Sample):**

### Input
```text
Sự kiện: Nhập số lượng hạt ngọc trai K.
```

### Output
```text
Kết quả: Chuỗi vòng ngọc trai lộng lẫy.
```

### Giải thích

K = 12 hạt ngọc xếp tròn quanh tâm.

---

### Bài 13 (P3): Họa Tiết Đường Viền Sóng Biển
* **Mã bài toán:** `sca_pen_p33_hoa_tiet_trang_tri_vien`
* **Độ khó & Phân tầng:** P3 (Vận dụng cao & Sáng tạo)
* **Bối cảnh:** Trang trí mép thảm trải sàn hoặc khung ảnh bằng chuỗi cung tròn sóng biển dập dềnh liên tiếp.
* **Nhiệm vụ:** Lặp lại N lần cung tròn 180 độ uốn lượn liên tiếp theo chiều ngang.
* **Dữ liệu vào (Input):** Nhập chiều dài đường viền.
* **Kết quả ra (Output):** Dải hoa văn viền sóng biển uốn lượn liên tục.
* **Dữ liệu mẫu (Sample):**

### Input
```text
Sự kiện: Nhập chiều dài đường viền.
```

### Output
```text
Kết quả: Dải hoa văn viền sóng biển uốn lượn liên tục.
```

### Giải thích

Cung uốn lên rồi cung uốn xuống xen kẽ.

---

### Bài 14 (P3): Gạch Hoa Cổ Điển Đông Dương
* **Mã bài toán:** `sca_pen_p34_hoa_van_gach_hoa_co_dien`
* **Độ khó & Phân tầng:** P3 (Vận dụng cao & Sáng tạo)
* **Bối cảnh:** Nền nhà cổ kính với những viên gạch hoa văn kết hợp tinh tế giữa hình vuông và 4 cánh hoa tròn bao quanh.
* **Nhiệm vụ:** Vẽ hình vuông trung tâm và 4 cánh hoa uốn cong tại 4 cạnh hình vuông.
* **Dữ liệu vào (Input):** Nhấn cờ xanh.
* **Kết quả ra (Output):** Họa tiết viên gạch hoa Đông Dương sang trọng.
* **Dữ liệu mẫu (Sample):**

### Input
```text
Sự kiện: Nhấn cờ xanh.
```

### Output
```text
Kết quả: Họa tiết viên gạch hoa Đông Dương sang trọng.
```

### Giải thích

1 hình vuông + 4 cung tròn cánh hoa.

---

### Bài 15 (P3): Kính Vạn Hoa Đa Chiều (Kaleidoscope)
* **Mã bài toán:** `sca_pen_p35_dai_ngan_ha_van_hoa`
* **Độ khó & Phân tầng:** P3 (Vận dụng cao & Sáng tạo)
* **Bối cảnh:** Ống kính vạn hoa đồ chơi tạo nên vô số hoa văn kỳ ảo khi xoay chuyển trước ánh sáng.
* **Nhiệm vụ:** Xoay một cụm họa tiết gồm đa giác và cung tròn 36 lần quanh tâm (mỗi lần 10 độ) với màu sắc cầu vồng ngẫu nhiên.
* **Dữ liệu vào (Input):** Nhấn cờ xanh.
* **Kết quả ra (Output):** Bức tranh kính vạn hoa lộng lẫy, choáng ngợp.
* **Dữ liệu mẫu (Sample):**

### Input
```text
Sự kiện: Nhấn cờ xanh.
```

### Output
```text
Kết quả: Bức tranh kính vạn hoa lộng lẫy, choáng ngợp.
```

### Giải thích

Hiệu ứng xoay tròn 36 lần liên tục đổi màu.

---
