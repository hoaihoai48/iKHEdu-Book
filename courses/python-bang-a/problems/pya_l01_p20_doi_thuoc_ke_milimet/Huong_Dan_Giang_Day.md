# Hướng Dẫn Giảng Dạy: Đổi thước kẻ milimet
Chuyên đề: **Chào Python & Chiếc Hộp Biến Số**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất của bài này là đổi đơn vị độ dài: `1 cm = 10 mm` nên `a = 2` cm chính là `20` mm, cộng thêm `b = 5` mm được `25` mm. Thầy cô cho các con đổi thước kẻ thật trên bàn để hình dung.
- Quy trình gồm ba bước với hai biến `a` và `b` trong lời giải: đọc `2` vào `a` và `5` vào `b` bằng `int(input().strip())`, rồi tính `a * 10 + b` tức `2 * 10 + 5 = 25` và in ra.
- Xử lý biên: ràng buộc cho `a, b` từ 1 tới 1000. Thầy cô cho các con thử cặp biên `1` và `1` cho ra `11`, cặp `1000` và `1000` cho ra `11000`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 2 và 5)
| Bước | Lệnh chạy | Giá trị biến | Màn hình hiện ra |
|------|-----------|--------------|------------------|
| 1 | `a = int(input().strip())` với dòng 1 gõ `2` | `a = 2` | (chưa in gì) |
| 2 | `b = int(input().strip())` với dòng 2 gõ `5` | `b = 5` | (chưa in gì) |
| 3 | `print(a * 10 + b)` tức `print(2 * 10 + 5)` | `a = 2`, `b = 5` | `25` |
| 4 | Kết thúc chương trình | — | Kết quả cuối cùng: `25`. |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: quên đổi cm sang mm, viết `print(a + b)` thì với mẫu `2` và `5` màn hình hiện `7` thay vì `25`. Cách sửa: nhân phần cm với 10 trước, viết `a * 10 + b`.
- Bẫy 2: nhân sai số đổi, viết `print(a * 100 + b)` thì với mẫu `2` và `5` màn hình hiện `205` thay vì `25`. Cách sửa: nhớ `1 cm = 10 mm` nên chỉ nhân với 10.
- Bẫy 3: in hai kết quả trên hai dòng như `print(a * 10)` rồi `print(b)` thì màn hình hiện `20` rồi `5` thay vì `25` trên một dòng. Cách sửa: cộng gộp rồi in một lần bằng `print(a * 10 + b)`.

---

## 4. Lời giải tham khảo
```python
a = int(input().strip())
b = int(input().strip())
print(a * 10 + b)
```
