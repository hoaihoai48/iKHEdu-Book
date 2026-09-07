# Hướng Dẫn Giảng Dạy: Cửa hàng bánh rán
Chuyên đề: **Chào Python & Chiếc Hộp Biến Số**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất của bài này là tính tiền hóa đơn: đơn giá `a = 12` nghìn đồng nhân với số lượng `b = 5` được `60` nghìn đồng. Thầy cô cho các con hình dung mua 5 chiếc bánh, mỗi chiếc 12 nghìn.
- Quy trình gồm ba bước với hai biến `a` và `b` trong lời giải: đọc `12` vào `a` và `5` vào `b` bằng `int(input().strip())`, rồi tính `a * b` tức `12 * 5 = 60` và in ra.
- Xử lý biên: ràng buộc cho `a, b` từ 1 tới 100. Thầy cô cho các con thử cặp biên `1` và `1` cho ra `1`, cặp `100` và `100` cho ra `10000`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 12 và 5)
| Bước | Lệnh chạy | Giá trị biến | Màn hình hiện ra |
|------|-----------|--------------|------------------|
| 1 | `a = int(input().strip())` với dòng 1 gõ `12` | `a = 12` | (chưa in gì) |
| 2 | `b = int(input().strip())` với dòng 2 gõ `5` | `b = 5` | (chưa in gì) |
| 3 | `print(a * b)` tức `print(12 * 5)` | `a = 12`, `b = 5` | `60` |
| 4 | Kết thúc chương trình | — | Kết quả cuối cùng: `60`. |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: cộng thay vì nhân, viết `print(a + b)` thì với mẫu `12` và `5` màn hình hiện `17` thay vì `60`. Cách sửa: tiền hóa đơn bằng đơn giá nhân số lượng, viết `a * b`.
- Bẫy 2: quên `int()`, viết `a = input().strip()` rồi `print(a * b)` thì máy lặp chữ, cho ra kết quả lạ thay vì `60`. Cách sửa: viết `a = int(input().strip())` và `b = int(input().strip())`.
- Bẫy 3: đọc hai số trên một dòng bằng `map(int, input().split())` trong khi đề cho hai dòng riêng thì chương trình sẽ chờ thiếu số. Cách sửa: đọc hai lần `int(input().strip())` cho đúng hai dòng.

---

## 4. Lời giải tham khảo
```python
a = int(input().strip())
b = int(input().strip())
print(a * b)
```
