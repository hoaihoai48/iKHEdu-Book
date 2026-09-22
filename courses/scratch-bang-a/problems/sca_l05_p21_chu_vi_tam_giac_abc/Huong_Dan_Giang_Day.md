# Hướng Dẫn Giảng Dạy

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất chu vi tam giác: cộng cả ba cạnh `a + b + c`, bài này mỗi cạnh nằm một dòng riêng.
- Quy trình trong lời giải: đọc `a`, `b`, `c` mỗi biến một lần `câu trả lời`, rồi in `a + b + c`; với mẫu `3`, `4`, `5` thì `3 + 4 + 5 = 12`.
- Xử lý biên: mỗi cạnh từ 1 đến 100000000, tổng lớn nhất là 300000000, phép cộng số nguyên luôn đúng.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 3\n4\n5)
Với số mẫu ba dòng `3`, `4`, `5`, chương trình phải in ra `12`.

| Bước | Hành động | Giá trị biến | Kết quả |
|---|---|---|---|
| 1 | Đọc `a` | `a = 3` | cạnh 3 |
| 2 | Đọc `b` | `b = 4` | cạnh 4 |
| 3 | Đọc `c` | `c = 5` | cạnh 5 |
| 4 | Tính `a + b + c` | `3 + 4 + 5 = 12` | khớp kết quả mẫu `12` |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1 — đọc cả ba số một dòng: viết `a, b, c = các khối hỏi và đợi cho từng biến` thì với mẫu mỗi số một dòng sẽ bị lỗi thiếu số; cách sửa là đọc ba lần riêng.
- Bẫy 2 — nhầm thành diện tích: viết `nói (a * b * c)` thì với mẫu ra `60` thay vì `12`; cách sửa là cộng ba cạnh.
- Bẫy 3 — quên đổi kiểu một biến: nếu `c` còn là chuỗi thì phép cộng bị lỗi; cách sửa là cả ba đều `câu trả lời`.

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - hỏi [Nhập a:] và đợi
> - đặt [a] thành (câu trả lời)
> - hỏi [Nhập b:] và đợi
> - đặt [b] thành (câu trả lời)
> - hỏi [Nhập c:] và đợi
> - đặt [c] thành (câu trả lời)
> - nói (a + b + c)
