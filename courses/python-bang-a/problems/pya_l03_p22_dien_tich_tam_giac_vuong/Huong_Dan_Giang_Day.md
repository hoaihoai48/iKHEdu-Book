# Hướng Dẫn Giảng Dạy: Diện tích tam giác vuông
Chuyên đề: **Tính Toán Cơ Bản & Nền Tảng Python**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất diện tích tam giác vuông: nửa tích hai cạnh góc vuông `(a * b) / 2`, bài này in đúng 1 chữ số thập phân.
- Quy trình trong lời giải: đọc một dòng rồi tách thành `a, b`, sau đó in `(a * b) / 2` với 1 chữ số thập phân; với mẫu `5 7` thì `5 * 7 = 35` và `35 / 2 = 17.5`.
- Xử lý biên: `A` và `B` tới 10000, diện tích lớn nhất là 50000000.0, số lẻ như `17.5` vẫn hiện đúng 1 chữ số.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5 7)
Với số mẫu một dòng `5 7`, chương trình phải in ra `17.5`.

| Bước | Hành động | Giá trị biến | Kết quả |
|---|---|---|---|
| 1 | Đọc `a, b` | `a = 5`, `b = 7` | hai cạnh 5 và 7 |
| 2 | Tính `a * b` | `5 * 7 = 35` | tích 35 |
| 3 | Tính `35 / 2` | `17.5` | khớp kết quả mẫu `17.5` |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1 — dùng chia nguyên: viết `(a * b) // 2` thì với mẫu ra `17` thay vì `17.5`; cách sửa là chia thực `/` và giữ 1 chữ số thập phân.
- Bẫy 2 — in thô không làm tròn: viết `print((a * b) / 2)` với cặp số cho kết quả nguyên sẽ thiếu `.0`; cách sửa là luôn ghi định dạng 1 chữ số thập phân.
- Bẫy 3 — đọc hai dòng riêng: dùng hai lần `input()` thì với mẫu một dòng `5 7` sẽ bị treo chờ; cách sửa là tách một dòng bằng `split()`.

---

## 4. Lời giải tham khảo
```python
a, b = map(int, input().split())
print(f"{(a * b) / 2:.1f}")
```
