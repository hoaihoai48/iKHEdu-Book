# Hướng Dẫn Giảng Dạy: Điểm trung bình môn học
Chuyên đề: **Tính Toán Cơ Bản & Nền Tảng Python**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất điểm trung bình: cộng ba điểm `d1 + d2 + d3` rồi chia 3, in làm tròn 2 chữ số thập phân.
- Quy trình trong lời giải: đọc một dòng rồi tách thành `d1, d2, d3` kiểu số thực, sau đó in `(d1 + d2 + d3) / 3` với 2 chữ số thập phân; với mẫu `8.5 9.0 7.5` thì tổng `8.5 + 9.0 + 7.5 = 25.0` và `25.0 / 3 = 8.333...` làm tròn thành `8.33`.
- Xử lý biên: mỗi điểm từ 0 đến 10, điểm 10 10 10 cho ra `10.00`, điểm 0 0 0 cho ra `0.00`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 8.5 9.0 7.5)
Với số mẫu một dòng `8.5 9.0 7.5`, chương trình phải in ra `8.33`.

| Bước | Hành động | Giá trị biến | Kết quả |
|---|---|---|---|
| 1 | Đọc `d1, d2, d3` | `8.5, 9.0, 7.5` | đủ ba điểm |
| 2 | Tính tổng | `8.5 + 9.0 + 7.5 = 25.0` | tổng 25.0 |
| 3 | Tính `25.0 / 3` | `8.333...` làm tròn `8.33` | khớp kết quả mẫu `8.33` |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1 — đọc số nguyên: viết `map(int, ...)` thì với mẫu `8.5` bị lỗi đổi chữ; cách sửa là đọc số thực `map(float, ...)`.
- Bẫy 2 — dùng chia nguyên: viết `(d1 + d2 + d3) // 3` thì với mẫu ra `8.0` thay vì `8.33`; cách sửa là chia thực `/` rồi làm tròn 2 chữ số.
- Bẫy 3 — in thô không làm tròn: viết `print((d1 + d2 + d3) / 3)` thì với mẫu ra `8.333333333333334` thay vì `8.33`; cách sửa là ghi định dạng 2 chữ số thập phân.

---

## 4. Lời giải tham khảo
```python
d1, d2, d3 = map(float, input().split())
print(f"{(d1 + d2 + d3) / 3:.2f}")
```
