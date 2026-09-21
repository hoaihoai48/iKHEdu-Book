# HƯỚNG DẪN GIẢNG DẠY: SCA_PEN_P12 — LOGO 5 VÒNG TRÒN OLYMPIC

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)

- **Kiến thức:** Hiểu rõ cách tái sử dụng khối lệnh vẽ hình tròn nhiều lần thông qua thủ tục con **Khối của tôi (My Blocks)**.
- **Kỹ năng:**
  - Thành thạo tính toán độ dài bước đi cho hình tròn bán kính $R = 40$: $\text{Bước đi} = \dfrac{2 \times 3.14 \times 40}{360} \approx 0.7$ bước.
  - Phối hợp nhịp nhàng các thao tác: 🟢 **nhấc bút** $\to$ 🔵 **đi tới điểm** $\to$ 🟢 **chọn màu vẽ** $\to$ 🟢 **đặt bút**.
  - Tính toán khoảng cách tọa độ để các vòng tròn hàng trên và hàng dưới đan lồng so le cân đối.
- **Phẩm chất:** Rèn luyện tính cẩn thận, mắt thẩm mỹ và sự chính xác trong sắp đặt hình học đồ họa.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học (Edge Cases)

- **Bản chất hình học:**
  - Mỗi vòng tròn có chu vi $C = 2 \times 3.14 \times 40 \approx 251.2$ bước.
  - Chia cho $360^\circ$: mỗi bước đi vi phân dài $\approx 0.7$ bước.
- **Quy luật tọa độ so le:**
  - Khoảng cách ngang giữa hai tâm vòng tròn liên tiếp cùng hàng là $\Delta x = 80$ bước (đúng bằng đường kính $2R$).
  - Khoảng cách dọc giữa hàng trên và hàng dưới là $\Delta y = 40$ bước (đúng bằng bán kính $R$).
  - Hai vòng hàng dưới nằm lệch tâm đúng $\Delta x / 2 = 40$ bước so với các vòng hàng trên, tạo nên thế lồng ghép so le kinh điển của biểu tượng Olympic.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt (Socratic Method)

1. *"Nếu ta phải vẽ 5 hình tròn giống hệt nhau, việc kéo 5 cụm lệnh 'lặp lại 360 lần' có làm kịch bản bị dài dòng và rối mắt không? Ta nên dùng công cụ gì để chỉ cần viết 1 lần mà dùng được 5 lần?"*  
   $\to$ Định hướng học sinh tạo **Khối của tôi (My Blocks)** mang tên `ve_hinh_tron`.

2. *"Tại sao khi Mèo vẽ xong vòng tròn màu xanh và chạy sang vẽ vòng tròn màu đen, trên màn hình lại xuất hiện một vệt mực nối giữa hai vòng?"*  
   $\to$ Nhắc học sinh quy tắc: **Muốn đi mà không vẽ, phải nhấc bút trước khi đi!**

3. *"Làm thế nào để hai vòng tròn hàng dưới nằm lọt vào giữa các vòng tròn hàng trên?"*  
   $\to$ Giúp học sinh phân tích tọa độ $x$ của hàng dưới: $x_4 = \dfrac{x_1 + x_2}{2} = \dfrac{-110 + (-30)}{2} = -70$.

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)

- **Bất biến hình tròn:** Sau khi nhân vật thực hiện xong khối `ve_hinh_tron (0.7)`, nhân vật luôn quay trọn vẹn $360^\circ$ và trở về đúng vị trí xuất phát với cùng hướng nhìn ban đầu.
- **Đóng gói My Blocks:**
  ```text
  định nghĩa ve_hinh_tron (buoc)
  lặp lại (360) lần:
      di chuyển (buoc) bước
      xoay phải ↻ (1) độ
  ```
- **Kịch bản chính:** Chỉ cần gọi tuần tự 5 lần khối `ve_hinh_tron` kèm theo tọa độ và màu sắc tương ứng.

---

## 5. Mô Phỏng Từng Bước Trên Sample (Dry Run Table)

| STT Vòng | Tên màu | Tọa độ xuất phát ($x, y$) | Mã màu HEX | Trạng thái bút vẽ | Thao tác thực hiện |
|:---:|---|:---:|:---:|:---:|---|
| **1** | Xanh da trời | $(-110, 40)$ | `#0085C7` | Đặt bút | Vẽ vòng 1 hàng trên bên trái |
| **2** | Đen | $(-30, 40)$ | `#000000` | Nhấc $\to$ Đi $\to$ Đặt | Vẽ vòng 2 hàng trên chính giữa |
| **3** | Đỏ | $(50, 40)$ | `#DF0024` | Nhấc $\to$ Đi $\to$ Đặt | Vẽ vòng 3 hàng trên bên phải |
| **4** | Vàng | $(-70, 0)$ | `#F4C300` | Nhấc $\to$ Đi $\to$ Đặt | Vẽ vòng 4 hàng dưới bên trái |
| **5** | Xanh lá cây | $(10, 0)$ | `#009F3D` | Nhấc $\to$ Đi $\to$ Đặt | Vẽ vòng 5 hàng dưới bên phải |

---

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian

- **Thời gian:** $5 \times 360 = 1800$ bước lặp vi phân. Ở chế độ chạy Turbo Mode hoặc My Blocks không làm mới màn hình (Run without screen refresh), chương trình hoàn thành vẽ chỉ trong $0.1$ giây.
- **Không gian:** $\mathcal{O}(1)$ bộ nhớ RAM, dùng 1 Sprite mặc định.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)

- **Bẫy 1: Quên nhấc bút khi đổi tọa độ** $\to$ Hình vẽ xuất hiện nét gạch nối ngang làm hỏng logo.
- **Bẫy 2: Sai thứ tự đổi màu và đặt bút** $\to$ Đặt bút trước rồi mới đổi màu khiến điểm xuất phát bị dính màu của vòng trước. Khắc phục: Luôn chọn màu vẽ *trước* khi đặt bút.
- **Bẫy 3: Quên lệnh xóa màn hình đầu chương trình** $\to$ Bấm Cờ Xanh lần thứ hai các vòng tròn đè lên nhau gây nhòe nét.

---

## 8. Mã Nguồn Khối Lệnh Tham Chiếu Chuẩn (Visual Scratch Blocks)

*Quy trình thực hiện bằng Scratch Tiếng Việt:*

1. **Định nghĩa Khối của tôi:**
   - 🔴 **`định nghĩa ve_hinh_tron (buoc)`**
     - 🟠 `lặp lại (360) lần`:
       - 🔵 `di chuyển (buoc) bước`
       - 🔵 `xoay phải ↻ (1) độ`

2. **Kịch bản sự kiện chính:**
   - 🟡 **Khi bấm vào cờ xanh**
   - 🟢 **Xóa tất cả**
   - 🟢 **Đặt kích thước bút vẽ bằng (6)**
   - 🟢 **Nhấc bút**
   - *Vòng 1 (Xanh da trời):* 🔵 `đi tới điểm x: (-110) y: (40)` $\to$ 🟢 `chọn màu vẽ [#0085C7]` $\to$ 🟢 `đặt bút` $\to$ 🔴 `ve_hinh_tron (0.7)` $\to$ 🟢 `nhấc bút`.
   - *Vòng 2 (Đen):* 🔵 `đi tới điểm x: (-30) y: (40)` $\to$ 🟢 `chọn màu vẽ [#000000]` $\to$ 🟢 `đặt bút` $\to$ 🔴 `ve_hinh_tron (0.7)` $\to$ 🟢 `nhấc bút`.
   - *Vòng 3 (Đỏ):* 🔵 `đi tới điểm x: (50) y: (40)` $\to$ 🟢 `chọn màu vẽ [#DF0024]` $\to$ 🟢 `đặt bút` $\to$ 🔴 `ve_hinh_tron (0.7)` $\to$ 🟢 `nhấc bút`.
   - *Vòng 4 (Vàng):* 🔵 `đi tới điểm x: (-70) y: (0)` $\to$ 🟢 `chọn màu vẽ [#F4C300]` $\to$ 🟢 `đặt bút` $\to$ 🔴 `ve_hinh_tron (0.7)` $\to$ 🟢 `nhấc bút`.
   - *Vòng 5 (Xanh lá):* 🔵 `đi tới điểm x: (10) y: (0)` $\to$ 🟢 `chọn màu vẽ [#009F3D]` $\to$ 🟢 `đặt bút` $\to$ 🔴 `ve_hinh_tron (0.7)` $\to$ 🟢 `nhấc bút`.
   - 🟣 **Ẩn** nhân vật để nhìn rõ toàn bộ logo.

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)

- **Mở rộng 1:** Em hãy thêm tính năng khi bấm phím `Space`, các vòng tròn Olympic tự động phóng to dần bán kính từ $20 \to 50$ bước.
- **Mở rộng 2:** Ứng dụng kỹ thuật này để vẽ biểu tượng 3 vòng tròn của hãng xe nổi tiếng (Audi - 4 vòng tròn lồng ngang, Mercedes - hình tròn 3 cánh sao).


## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - xóa tất cả, đặt kích thước bút vẽ bằng (6)
> - vòng 1 (Xanh lam): đi tới x: (-110) y: (20), đặt bút, lặp 360 [đi 0.8, xoay 1]
> - vòng 2 (Đen): đi tới x: (0) y: (20), đặt bút, lặp 360 [đi 0.8, xoay 1]
> - vòng 3 (Đỏ): đi tới x: (110) y: (20), đặt bút, lặp 360 [đi 0.8, xoay 1]
