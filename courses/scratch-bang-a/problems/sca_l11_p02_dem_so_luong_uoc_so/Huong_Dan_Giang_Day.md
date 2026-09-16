# Hướng Dẫn Giảng Dạy: Đếm số lượng ước số
Chuyên đề: **Lập Trình Thuật Toán & Khối Lệnh Scratch 3.0**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất của bài này: với `n = 10`, duyệt mọi `i` từ `1` tới `10` và đếm các `i` mà `10 % i == 0`.
- Biến `dem` bắt đầu bằng `0`, mỗi khi gặp ước thì `dem = dem + 1`.
- Với `n = 10` các ước là `1, 2, 5, 10` nên `dem` tăng đúng 4 lần và in ra `4`.
- Thầy cô cho các em kể tay các ước của `10` trước khi chạy vòng lặp để đối chiếu.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 10)
| `i` | `10 % i` | `dem` sau bước | Ghi chú |
| --- | --- | --- | --- |
| 1 | 0 | 1 | `10 % 1 == 0`, đếm |
| 2 | 0 | 2 | `10 % 2 == 0`, đếm |
| 3 | 1 | 2 | không đếm |
| 4 | 2 | 2 | không đếm |
| 5 | 0 | 3 | `10 % 5 == 0`, đếm |
| 6 | 4 | 3 | không đếm |
| 7 | 3 | 3 | không đếm |
| 8 | 2 | 3 | không đếm |
| 9 | 1 | 3 | không đếm |
| 10 | 0 | 4 | `10 % 10 == 0`, đếm |

Kết quả in ra: `4`, khớp với kết quả mẫu.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: quên gắn lại biến đếm, chỉ viết `dem + 1` mà không gán. Với mẫu `10` chương trình in ra `0`, là kết quả sai. Sửa lại một dòng: `dem = dem + 1`.
- Bẫy 2: duyệt `range(1, n)` thiếu số `n`. Với mẫu `10` sẽ bỏ mất ước `10` nên in ra `3`. Sửa lại: `range(1, n + 1)`.
- Bẫy 3: đọc nhầm đề, in ra các ước thay vì số lượng. Với mẫu `10` sẽ in `1 2 5 10` thay vì `4`. Sửa lại: chỉ `nói (dem)`.

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - hỏi [Nhập n:] và đợi
> - đặt [n] thành (câu trả lời)
> - nói (dem)
