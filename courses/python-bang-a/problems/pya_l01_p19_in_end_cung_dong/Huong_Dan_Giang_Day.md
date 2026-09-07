# Hướng Dẫn Giảng Dạy: In không xuống dòng với end
Chuyên đề: **Tính Toán Cơ Bản & Nền Tảng Python**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất của bài này là ghép khẩu hiệu `Lap trinh rat vui!` từ hai mảnh bằng hai lệnh `print()` nhưng vẫn nằm trên cùng một dòng. Thầy cô giải thích `end=" "` nghĩa là sau khi in xong thì dừng lại bằng một dấu cách thay vì xuống dòng.
- Quy trình gồm hai bước: lệnh thứ nhất `print("Lap trinh", end=" ")` in `Lap trinh` kèm một dấu cách ở cuối và giữ con trỏ ở lại, lệnh thứ hai `print("rat vui!")` in tiếp `rat vui!` ngay sau dấu cách đó, tạo thành `Lap trinh rat vui!`.
- Xử lý biên: bài này không có số liệu vào nên không có giá trị biên. Thầy cô nhắc các con giữ đúng một dấu cách giữa `trinh` và `rat`, vì thiếu dấu cách sẽ dính thành `Lap trinhrat vui!`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: (không có dữ liệu vào))
| Bước | Lệnh chạy | Màn hình hiện ra |
|------|-----------|------------------|
| 1 | `print("Lap trinh", end=" ")` | `Lap trinh ` (con trỏ vẫn ở cùng dòng, chưa xuống dòng) |
| 2 | `print("rat vui!")` | nối tiếp thành `Lap trinh rat vui!` rồi xuống dòng |
| 3 | Kết thúc chương trình | Kết quả cuối cùng: `Lap trinh rat vui!`. |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: quên `end=" "`, viết hai lệnh `print("Lap trinh")` và `print("rat vui!")` thì màn hình hiện hai dòng rời nhau thay vì một dòng `Lap trinh rat vui!`. Cách sửa: thêm `end=" "` vào lệnh thứ nhất.
- Bẫy 2: viết `end=""` không có dấu cách thì màn hình hiện `Lap trinhrat vui!` bị dính chữ. Cách sửa: viết đúng `end=" "` có một dấu cách ở giữa.
- Bẫy 3: gộp dấu cách sai chỗ, ví dụ `print("Lap trinh ", end=" ")` kèm thêm cách sẽ tạo hai dấu cách liên tiếp thành `Lap trinh  rat vui!`. Cách sửa: chỉ để một dấu cách duy nhất, hoặc trong chữ hoặc trong `end`.

---

## 4. Lời giải tham khảo
```python
print("Lap trinh", end=" ")
print("rat vui!")
```
