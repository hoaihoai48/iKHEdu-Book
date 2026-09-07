# Hướng Dẫn Giảng Dạy: Hiệu hai số nguyên
Chuyên đề: **Tính Toán Cơ Bản & Nền Tảng Python**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất của bài này là tính vải còn lại: cuộn vải dài `A = 100` mét trừ đi `B = 35` mét đã cắt, còn `65` mét. Thầy cô cho các con hình dung cắt bớt một đoạn thì độ dài ngắn lại.
- Quy trình gồm ba bước với hai biến `a` và `b` trong lời giải: đọc `100` vào `a`, đọc `35` vào `b`, rồi tính `a - b` tức `100 - 35 = 65` và in ra.
- Xử lý biên: ràng buộc cho `0 <= B <= A <= 10^9` nên hiệu không bao giờ âm. Thầy cô cho các con thử cặp biên bằng nhau như `100` và `100` cho ra `0`, và cặp `1000000000` và `0` cho ra `1000000000`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 100 và 35)
| Bước | Lệnh chạy | Giá trị biến | Màn hình hiện ra |
|------|-----------|--------------|------------------|
| 1 | `a = int(input())` với dòng 1 gõ `100` | `a = 100` | (chưa in gì) |
| 2 | `b = int(input())` với dòng 2 gõ `35` | `b = 35` | (chưa in gì) |
| 3 | `print(a - b)` tức `print(100 - 35)` | `a = 100`, `b = 35` | `65` |
| 4 | Kết thúc chương trình | — | Kết quả cuối cùng: `65`. |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: viết ngược thứ tự `print(b - a)` thì với mẫu `100` và `35` màn hình hiện `-65` thay vì `65`. Cách sửa: nhớ lấy số lớn trừ số nhỏ, viết `a - b`.
- Bẫy 2: cộng thay vì trừ, viết `print(a + b)` thì với mẫu `100` và `35` màn hình hiện `135` thay vì `65`. Cách sửa: bài hỏi phần còn lại nên viết dấu `-`.
- Bẫy 3: quên `int()` khiến `a - b` báo lỗi vì không trừ được chữ. Cách sửa: viết `a = int(input())` và `b = int(input())`.

---

## 4. Lời giải tham khảo
```python
a = int(input())
b = int(input())
print(a - b)
```
