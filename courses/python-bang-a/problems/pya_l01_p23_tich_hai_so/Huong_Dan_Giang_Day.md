# Hướng Dẫn Giảng Dạy: Tích hai số nguyên
Chuyên đề: **Tính Toán Cơ Bản & Nền Tảng Python**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất của bài này là đếm kẹo trong một thùng: mỗi thùng có `A = 12` hộp, mỗi hộp có `B = 8` chiếc kẹo, vậy tổng là `12 * 8 = 96` chiếc. Thầy cô cho các con xếp 12 hàng, mỗi hàng 8 chiếc rồi đếm gộp.
- Quy trình gồm ba bước với hai biến `a` và `b` trong lời giải: đọc `12` vào `a`, đọc `8` vào `b`, rồi tính `a * b` tức `12 * 8 = 96` và in ra.
- Xử lý biên: ràng buộc cho `A, B` từ 0 tới `10^4`. Thầy cô cho các con thử cặp biên `0` và `10000` cho ra `0`, cặp `10000` và `10000` cho ra `100000000` để thấy chương trình vẫn đúng.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 12 và 8)
| Bước | Lệnh chạy | Giá trị biến | Màn hình hiện ra |
|------|-----------|--------------|------------------|
| 1 | `a = int(input())` với dòng 1 gõ `12` | `a = 12` | (chưa in gì) |
| 2 | `b = int(input())` với dòng 2 gõ `8` | `b = 8` | (chưa in gì) |
| 3 | `print(a * b)` tức `print(12 * 8)` | `a = 12`, `b = 8` | `96` |
| 4 | Kết thúc chương trình | — | Kết quả cuối cùng: `96`. |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: viết dấu nhân toán học `x`, ví dụ `print(a x b)` thì chương trình báo lỗi vì Python chỉ hiểu dấu `*`. Cách sửa: viết `print(a * b)`.
- Bẫy 2: cộng thay vì nhân, viết `print(a + b)` thì với mẫu `12` và `8` màn hình hiện `20` thay vì `96`. Cách sửa: bài hỏi tổng số kẹo trong thùng nên viết dấu `*`.
- Bẫy 3: quên `int()`, viết `a = input()` rồi `print(a * b)` thì với `a` là chữ `"12"` máy lặp chữ, cho ra kết quả lạ thay vì `96`. Cách sửa: viết `a = int(input())` và `b = int(input())`.

---

## 4. Lời giải tham khảo
```python
a = int(input())
b = int(input())
print(a * b)
```
