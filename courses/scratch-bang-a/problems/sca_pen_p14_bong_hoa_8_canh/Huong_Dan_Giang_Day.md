# HƯỚNG DẪN GIẢNG DẠY: SCA_PEN_P14 — ĐÓA HOA 8 CÁNH SẮC MÀU

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)

- **Kiến thức:** Nắm vững cấu trúc lồng nhau (Nested procedures): hàm con vẽ cung tròn $\to$ hàm con ghép cánh hoa $\to$ vòng lặp đối xứng tâm vẽ cả đóa hoa.
- **Kỹ năng:**
  - Định nghĩa khối lệnh tham số hóa `ve_cung_tron (goc) (buoc)`.
  - Định nghĩa khối lệnh ghép `ve_canh_hoa (buoc)`.
  - Vận dụng vòng lặp lặp lại và toán tử chia $360 / 8 = 45^\circ$ để chia đều không gian mặt phẳng.
- **Phẩm chất:** Khơi dậy tư duy sáng tạo nghệ thuật toán học (Algorithmic Art) và sự tự hào khi tạo ra sản phẩm đồ họa đẹp mắt.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học (Edge Cases)

- **Cấu trúc cánh hoa:**
  - Cung 1: Góc $90^\circ$, xoay phải mỗi lần $1^\circ$. Sau $90$ bước, nhân vật đổi hướng $90^\circ$.
  - Đỉnh nhọn: Xoay bù $180^\circ - 90^\circ = 90^\circ$.
  - Cung 2: Góc $90^\circ$. Sau $90$ bước, nhân vật uốn cong quay về đúng gốc tọa độ ban đầu.
  - Chân cánh hoa: Xoay tiếp $90^\circ$ để trở lại hướng nhìn lúc xuất phát.
  - Tổng góc xoay nội bộ của 1 cánh hoa: $90^\circ + 90^\circ + 90^\circ + 90^\circ = 360^\circ$ $\implies$ **Bảo toàn hoàn hảo hướng nhìn và vị trí**!
- **Đối xứng tâm $360^\circ$:**
  - Chia đều 8 cánh hoa: $\text{Góc xoay tâm} = \dfrac{360^\circ}{8} = 45^\circ$.
  - Đủ 8 lần xoay: $8 \times 45^\circ = 360^\circ$ khép kín trọn vẹn bông hoa.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt (Socratic Method)

1. *"Để vẽ 1 cánh hoa uốn cong, ta ghép 2 đường cong lại với nhau. Nếu cung thứ nhất là $90^\circ$, tại đỉnh nhọn Mèo cần quay bao nhiêu độ để mũi quay ngược trở lại vẽ cung thứ hai?"*  
   $\to$ Giúp học sinh nhận ra góc bù: $180^\circ - 90^\circ = 90^\circ$.

2. *"Sau khi vẽ xong 1 cánh hoa, chú Mèo đang đứng ở đâu và nhìn về hướng nào?"*  
   $\to$ Cho học sinh chạy thử chậm từng khối lệnh để thấy: Mèo đã trở về đúng $(0, 0)$ và nhìn đúng hướng ban đầu!

3. *"Vậy muốn vẽ bông hoa 8 cánh tỏa đều như chiếc bánh pizza 8 miếng, giữa các cánh hoa Mèo cần xoay thêm bao nhiêu độ?"*  
   $\to$ Học sinh tự tính ra: $360 / 8 = 45^\circ$.

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)

- **Nguyên lý phân rã bài toán (Decomposition):**
  - Cấp 1 (Cơ sở): `ve_cung_tron (goc) (buoc)`
  - Cấp 2 (Mảnh ghép): `ve_canh_hoa (buoc)`
  - Cấp 3 (Hệ thống): Vòng lặp chính `lặp lại (8) lần`
- **Bất biến vị trí:** Điểm xuất phát và điểm kết thúc của mỗi cánh hoa luôn trùng khớp tại $(0, 0)$.

---

## 5. Mô Phỏng Từng Bước Trên Sample (Dry Run Table)

| Vòng lặp cánh | Hướng trước khi vẽ cánh | Hành động thực hiện | Màu sắc nét vẽ | Hướng sau khi vẽ & xoay tâm |
|:---:|:---:|---|:---:|:---:|
| **Cánh 1** | $0^\circ$ (Bắc) | `ve_canh_hoa`, đổi màu, xoay $45^\circ$ | Màu đỏ | $45^\circ$ (Đông Bắc) |
| **Cánh 2** | $45^\circ$ (Đông Bắc) | `ve_canh_hoa`, đổi màu, xoay $45^\circ$ | Màu cam | $90^\circ$ (Đông) |
| **Cánh 3** | $90^\circ$ (Đông) | `ve_canh_hoa`, đổi màu, xoay $45^\circ$ | Màu vàng | $135^\circ$ (Đông Nam) |
| **Cánh 4** | $135^\circ$ (Đông Nam) | `ve_canh_hoa`, đổi màu, xoay $45^\circ$ | Màu xanh lá | $180^\circ$ (Nam) |
| **Cánh 5** | $180^\circ$ (Nam) | `ve_canh_hoa`, đổi màu, xoay $45^\circ$ | Màu xanh lơ | $225^\circ$ (Tây Nam) |
| **Cánh 6** | $225^\circ$ (Tây Nam) | `ve_canh_hoa`, đổi màu, xoay $45^\circ$ | Màu xanh lam | $270^\circ$ (Tây) |
| **Cánh 7** | $270^\circ$ (Tây) | `ve_canh_hoa`, đổi màu, xoay $45^\circ$ | Màu tím | $315^\circ$ (Tây Bắc) |
| **Cánh 8** | $315^\circ$ (Tây Bắc) | `ve_canh_hoa`, đổi màu, xoay $45^\circ$ | Màu hồng | $360^\circ \equiv 0^\circ$ (Bắc) |

---

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian

- **Thời gian:** $8 \text{ cánh} \times 2 \text{ cung} \times 90 \text{ bước} = 1440$ phép di chuyển và quay vi phân. Khuyến khích tích chọn *"Chạy không làm mới màn hình"* trên My Blocks để đóa hoa nở rộ tức thì.
- **Không gian:** $\mathcal{O}(1)$ bộ nhớ RAM.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)

- **Bẫy 1: Xoay đỉnh cánh hoa sai độ** $\to$ Cánh hoa không khép lại được ở đỉnh hoặc bị phình to bất thường.
- **Bẫy 2: Quên đưa nhân vật về hướng chuẩn $0^\circ$ hoặc $90^\circ$ lúc đầu** $\to$ Bông hoa bị nghiêng ngả không cân xứng với trục đứng.
- **Bẫy 3: Đặt bước đi vi phân quá lớn (ví dụ $3$)** $\to$ Cánh hoa dài hơn $270$ pixel, văng ra ngoài mép sân khấu khiến các cánh chạm tường bị gãy khúc. Khắc phục: Giữ độ dài bước đi vi phân trong khoảng $0.8 \to 1.5$.

---

## 8. Mã Nguồn Khối Lệnh Tham Chiếu Chuẩn (Visual Scratch Blocks)

![Khối lệnh vẽ bông hoa 8 cánh](../../assets/rendered_blocks/l02_bong_hoa_8_canh_vi.png)

*Quy trình thực hiện bằng Scratch Tiếng Việt:*

1. **Khối thủ tục Cung tròn:**
   - 🔴 **`định nghĩa ve_cung_tron (goc) (buoc)`**
     - 🟠 `lặp lại (goc) lần`:
       - 🔵 `di chuyển (buoc) bước`
       - 🔵 `xoay phải ↻ (1) độ`

2. **Khối thủ tục Cánh hoa:**
   - 🔴 **`định nghĩa ve_canh_hoa (buoc)`**
     - 🟠 `lặp lại (2) lần`:
       - 🔴 `ve_cung_tron (90) (buoc)`
       - 🔵 `xoay phải ↻ (90) độ`

3. **Kịch bản sự kiện chính:**
   - 🟡 **Khi bấm vào cờ xanh**
   - 🟢 **Xóa tất cả**
   - 🟢 **Nhấc bút**
   - 🔵 **Đi tới điểm x: (0) y: (0)**
   - 🔵 **Đặt hướng bằng (0)**
   - 🟢 **Chọn màu vẽ [Đỏ]**
   - 🟢 **Đặt kích thước bút vẽ bằng (3)**
   - 🟢 **Đặt bút**
   - 🟠 **Lặp lại (8) lần**:
     - 🔴 `ve_canh_hoa (1.2)`
     - 🟢 `thay đổi màu bút vẽ một lượng (15)`
     - 🔵 `xoay phải ↻ (45) độ`
   - 🟣 **Ẩn** nhân vật.

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)

- **Mở rộng 1 (Nhập số cánh tự động):** Thêm khối 🔵 `hỏi [Nhập số cánh hoa:] và đợi` rồi lặp lại `câu trả lời` lần với góc xoay `(360) / (câu trả lời)` để chương trình vẽ được hoa $5, 6, 12, 16$ cánh tùy thích.
- **Mở rộng 2 (Cánh hoa 2 màu):** Trong khối `ve_canh_hoa`, sau khi vẽ nửa cánh 1 thì đổi màu sang vàng, vẽ nửa cánh 2 đổi màu sang xanh để tạo ra cánh hoa viền đôi kỳ ảo.


## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - xóa tất cả, nhấc bút, đi tới điểm x: (0) y: (0)
> - đặt kích thước bút vẽ bằng (2), đặt [so_canh] thành (8)
> - lặp lại (8) lần:
> -   đổi màu bút, đặt bút
> -   vẽ 1 cánh hoa: lặp 2 [lặp 90 (đi 1, xoay phải 1 độ), xoay phải 90 độ]
> -   nhấc bút, xoay phải ↻ (360 / 8) độ
