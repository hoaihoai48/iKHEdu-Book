# Hướng Dẫn Giảng Dạy: Bốn phép tính đồng thời
Chuyên đề: **Tính Toán Cơ Bản & Nền Tảng Python**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất của bài này là từ hai số `A = 8` và `B = 5` tính ra ba kết quả: tổng `8 + 5 = 13`, hiệu `8 - 5 = 3`, tích `8 * 5 = 40`, mỗi kết quả nằm trên một dòng. Thầy cô ví như máy tính bỏ túi bấm một lần hiện đủ ba đáp số.
- Quy trình gồm hai bước với hai biến `a` và `b` trong lời giải: dùng `map(int, input().split())` để cắt dòng `8 5` thành `8` và `5` rồi cất vào `a` và `b`, sau đó in ba dòng `print(a + b)`, `print(a - b)`, `print(a * b)` cho ra `13`, `3`, `40`.
- Xử lý biên: ràng buộc cho `A, B` từ `-10^4` tới `10^4`. Thầy cô cho các con thử cặp biên `-10000 -10000` cho ra `-20000`, `0`, `100000000`, và cặp `10000 10000` cho ra `20000`, `0`, `100000000`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 8 5)
| Bước | Lệnh chạy | Giá trị biến | Màn hình hiện ra |
|------|-----------|--------------|------------------|
| 1 | `a, b = map(int, input().split())` với bàn phím gõ `8 5` | `a = 8`, `b = 5` | (chưa in gì) |
| 2 | `print(a + b)` tức `print(8 + 5)` | `a = 8`, `b = 5` | `13` |
| 3 | `print(a - b)` tức `print(8 - 5)` | `a = 8`, `b = 5` | `3` |
| 4 | `print(a * b)` tức `print(8 * 5)` | `a = 8`, `b = 5` | `40` |
| 5 | Kết thúc chương trình | — | Kết quả cuối cùng đúng ba dòng `13`, `3`, `40`. |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: in cả ba kết quả trên một dòng như `print(a + b, a - b, a * b)` thì với mẫu `8 5` màn hình hiện `13 3 40` chung một dòng thay vì ba dòng riêng. Cách sửa: viết ba lệnh `print` riêng.
- Bẫy 2: sai thứ tự các dòng, ví dụ in tích trước tổng thì ba dòng hiện `40`, `3`, `13` bị đảo chỗ. Cách sửa: giữ đúng thứ tự tổng rồi hiệu rồi tích.
- Bẫy 3: quên `int()` khi cắt dòng, viết `a, b = input().split()` rồi `print(a + b)` thì với mẫu `8 5` máy nối chữ thành `85` thay vì `13`. Cách sửa: bọc `map(int, ...)` để đổi thành số.

---

## 4. Lời giải tham khảo
```python
a, b = map(int, input().split())
print(a + b)
print(a - b)
print(a * b)
```
