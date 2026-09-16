# HƯỚNG DẪN GIẢNG DẠY: BIỂU TƯỢNG 5 VÒNG TRÒN OLYMPIC
Chuyên đề: **Đồ Họa Bút Vẽ (Pen) & Thuật Toán Hình Học Scratch 3.0**  
Mã bài toán: `sca_pen_p23_logo_olympic_5_mau` | Nguồn tham chiếu: `Câu 12`

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất hình học:** Bài toán rèn luyện tư duy chia nhỏ hình phức tạp thành các hình con cơ bản (đa giác đều, cung tròn, nhánh hoa văn).
- **Quy tắc bảo toàn góc quay:** Tổng các góc quay khi đi hết 1 vòng khép kín luôn bằng $360^\circ$.
- **Kỹ thuật đóng gói My Blocks:** Khuyến khích học sinh định nghĩa thủ tục con (ví dụ: `Vẽ_Cánh_Hoa`, `Vẽ_Nhánh`) với các tham số độ dài, bán kính để tái sử dụng nhiều lần.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table)
| Bước | Khối lệnh Scratch Tiếng Việt | Vị trí (x, y) | Hướng | Tác dụng |
|:---:|---|:---:|:---:|---|
| 1 | `khi bấm vào cờ xanh` | (0, 0) | 90 | Khởi động kịch bản |
| 2 | `xóa tất cả` | (0, 0) | 90 | Dọn sạch sân khấu |
| 3 | `nhấc bút`, `đi tới điểm x: 0 y: 0` | (0, 0) | 90 | Đưa nhân vật về tâm |
| 4 | `đặt kích thước bút vẽ bằng (3)` | (0, 0) | 90 | Đặt nét vẽ rõ nét |
| 5 | `đặt bút`, thực hiện vòng lặp | Thay đổi | Thay đổi | Vẽ hình theo yêu cầu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- **Bẫy 1 (Góc trong vs Góc ngoài):** Học sinh hay nhầm góc quay ngoài của nhân vật với góc trong của đa giác (ví dụ tam giác đều quay $120^\circ$ chứ không phải $60^\circ$).
- **Bẫy 2 (Lem nét vẽ thừa):** Quên `nhấc bút` khi di chuyển nhân vật đến vị trí xuất phát mới khiến đường đi để lại vệt mực xấu.
- **Bẫy 3 (Vẽ tràn sân khấu):** Chọn bán kính hoặc độ dài cạnh quá lớn khiến nhân vật chạm biên màn hình và hình vẽ bị méo mó.

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - xóa tất cả, đặt kích thước bút vẽ bằng (8)
> - vẽ 3 vòng hàng trên: Xanh lam (-110, 30), Đen (0, 30), Đỏ (110, 30)
> - vẽ 2 vòng đan xen hàng dưới: Vàng (-55, -15), Xanh lá (55, -15)
> - mỗi vòng tròn lặp 360 lần [di chuyển 0.8 bước, xoay phải 1 độ]
