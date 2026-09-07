# Hướng Dẫn Giảng Dạy: Chênh lệch tuổi của hai anh em
Chuyên đề: **Tính Toán Cơ Bản & Nền Tảng Python**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất của bài này là tính anh hơn em bao nhiêu tuổi: tuổi anh `A = 12` trừ tuổi em `E = 7` được `5`, rồi đặt số `5` vào khung câu `Anh hon em 5 tuoi.`. Thầy cô cho các con đếm từ 7 lên 12 xem chênh mấy tuổi.
- Quy trình gồm hai bước với hai biến `a` và `e` trong lời giải: dùng `map(int, input().split())` để cắt dòng `12 7` thành `12` và `7` rồi cất vào `a` và `e`, sau đó dùng chuỗi `f"Anh hon em {a - e} tuoi."` để tính `12 - 7 = 5` và ghép vào câu.
- Xử lý biên: ràng buộc cho `1 <= E <= A <= 100` nên anh luôn lớn tuổi hơn hoặc bằng em. Thầy cô cho các con thử biên bằng nhau `100 100` cho ra `Anh hon em 0 tuoi.`, và biên `100 1` cho ra `Anh hon em 99 tuoi.`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 12 7)
| Bước | Lệnh chạy | Giá trị biến | Màn hình hiện ra |
|------|-----------|--------------|------------------|
| 1 | `a, e = map(int, input().split())` với bàn phím gõ `12 7` | `a = 12`, `e = 7` | (chưa in gì) |
| 2 | `print(f"Anh hon em {a - e} tuoi.")` tức tính `12 - 7 = 5` rồi ghép vào câu | `a = 12`, `e = 7` | `Anh hon em 5 tuoi.` |
| 3 | Kết thúc chương trình | — | Kết quả cuối cùng: `Anh hon em 5 tuoi.`. |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: chỉ in hiệu `print(a - e)` thì với mẫu `12 7` màn hình hiện `5` thay vì `Anh hon em 5 tuoi.` nên bị tính là kết quả sai. Cách sửa: in cả câu bằng `print(f"Anh hon em {a - e} tuoi.")`.
- Bẫy 2: trừ ngược `e - a` thì với mẫu `12 7` câu hiện `Anh hon em -5 tuoi.` có số âm lạ. Cách sửa: nhớ anh trừ em, viết `a - e`.
- Bẫy 3: quên dấu chấm cuối câu, in ra `Anh hon em 5 tuoi` thiếu dấu `.` nên bị tính là kết quả sai. Cách sửa: sao chép đúng mẫu có dấu chấm ở cuối.

---

## 4. Lời giải tham khảo
```python
a, e = map(int, input().split())
print(f"Anh hon em {a - e} tuoi.")
```
