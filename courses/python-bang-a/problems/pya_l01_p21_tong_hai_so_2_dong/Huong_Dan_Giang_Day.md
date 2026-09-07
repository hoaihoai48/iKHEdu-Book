# Hướng Dẫn Giảng Dạy: Tổng hai số nguyên 2 dòng
Chuyên đề: **Tính Toán Cơ Bản & Nền Tảng Python**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất của bài này là cộng số bi của Minh và Nam: `A = 15` cộng `B = 25` được `40`. Thầy cô cho các con đếm gộp 15 viên rồi thêm 25 viên nữa.
- Quy trình gồm ba bước với hai biến `a` và `b` trong lời giải: đọc `15` vào `a`, đọc `25` vào `b`, rồi tính `a + b` tức `15 + 25 = 40` và in ra.
- Xử lý biên: ràng buộc cho `A, B` từ 0 tới `10^9`. Thầy cô cho các con thử cặp biên `0` và `0` cho ra `0`, cặp `1000000000` và `1000000000` cho ra `2000000000` để thấy chương trình vẫn đúng.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 15 và 25)
| Bước | Lệnh chạy | Giá trị biến | Màn hình hiện ra |
|------|-----------|--------------|------------------|
| 1 | `a = int(input())` với dòng 1 gõ `15` | `a = 15` | (chưa in gì) |
| 2 | `b = int(input())` với dòng 2 gõ `25` | `b = 25` | (chưa in gì) |
| 3 | `print(a + b)` tức `print(15 + 25)` | `a = 15`, `b = 25` | `40` |
| 4 | Kết thúc chương trình | — | Kết quả cuối cùng: `40`. |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: quên `int()`, viết `a = input()` và `b = input()` rồi `print(a + b)` thì với mẫu `15` và `25` máy nối chữ thành `1525` thay vì `40`. Cách sửa: viết `a = int(input())` và `b = int(input())`.
- Bẫy 2: trừ thay vì cộng, viết `print(a - b)` thì với mẫu `15` và `25` màn hình hiện `-10` thay vì `40`. Cách sửa: nhớ bài hỏi tổng nên viết dấu `+`.
- Bẫy 3: đọc hai số trên một dòng bằng `map(int, input().split())` trong khi đề cho hai dòng riêng thì với mẫu nhập từng số một dòng chương trình sẽ chờ thiếu số. Cách sửa: đọc hai lần `int(input())` cho đúng hai dòng.

---

## 4. Lời giải tham khảo
```python
a = int(input())
b = int(input())
print(a + b)
```
