# Hướng Dẫn Giảng Dạy: Hoán đổi vị trí hai biến
Chuyên đề: **Tính Toán Cơ Bản & Nền Tảng Python**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất của bài này là hai bạn An và Bình đổi thẻ cho nhau: thẻ `A = 10` sang tay bạn kia và thẻ `B = 99` sang tay bạn này. Thầy cô ví lệnh `a, b = b, a` như hai bàn tay bắt chéo nhau đổi thẻ cùng một lúc.
- Quy trình gồm ba bước với hai biến `a` và `b` trong lời giải: đọc `10` vào `a` và `99` vào `b` bằng hai lệnh `int(input())`, đổi chỗ cùng lúc bằng `a, b = b, a` để được `a = 99` và `b = 10`, rồi `print(a, b)` in ra `99 10`.
- Xử lý biên: ràng buộc cho `A, B` từ `-10^9` tới `10^9`. Thầy cô cho các con thử cặp biên `-1000000000` và `1000000000` để thấy lệnh đổi chỗ vẫn đúng cả với số âm.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 10 và 99)
| Bước | Lệnh chạy | Giá trị biến | Màn hình hiện ra |
|------|-----------|--------------|------------------|
| 1 | `a = int(input())` với dòng 1 gõ `10` | `a = 10` | (chưa in gì) |
| 2 | `b = int(input())` với dòng 2 gõ `99` | `b = 99` | (chưa in gì) |
| 3 | `a, b = b, a` | `a = 99`, `b = 10` | (chưa in gì) |
| 4 | `print(a, b)` | `a = 99`, `b = 10` | `99 10` |
| 5 | Kết thúc chương trình | — | Kết quả cuối cùng: `99 10`. |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: đổi từng dòng lệch thứ tự như `a = b` rồi `b = a` thì sau dòng đầu `a` đã thành `99`, dòng sau `b` cũng thành `99` nên in ra `99 99` thay vì `99 10`. Cách sửa: đổi cùng lúc bằng `a, b = b, a`.
- Bẫy 2: quên đổi mà in luôn, viết `print(a, b)` ngay sau khi đọc thì với mẫu `10` và `99` màn hình hiện `10 99` thay vì `99 10`. Cách sửa: thêm dòng `a, b = b, a` trước lệnh in.
- Bẫy 3: in mỗi số một dòng bằng hai lệnh `print(a)` và `print(b)` thì màn hình hiện `99` rồi `10` xuống hai dòng thay vì `99 10` trên một dòng. Cách sửa: viết gọn `print(a, b)` trên một lệnh.

---

## 4. Lời giải tham khảo
```python
a = int(input())
b = int(input())
a, b = b, a
print(a, b)
```
