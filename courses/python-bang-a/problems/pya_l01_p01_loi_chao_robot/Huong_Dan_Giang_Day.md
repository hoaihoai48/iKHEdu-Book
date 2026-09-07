# Hướng Dẫn Giảng Dạy: Lời chào robot
Chuyên đề: **Tính Toán Cơ Bản & Nền Tảng Python**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất của bài này là in ra một câu chữ cố định: `Xin chao cac ban! Toi la Robot Python.` Thầy cô giải thích cho các con rằng chương trình không cần đọc gì từ bàn phím, chỉ cần hiện đúng câu chào ra màn hình.
- Quy trình chỉ có một bước duy nhất: gọi lệnh `print(...)` với đúng chuỗi chữ trong ngoặc kép, gồm chữ hoa ở đầu `Xin`, dấu chấm than sau `ban!`, chữ `Toi`, chữ `Robot Python` và dấu chấm cuối câu.
- Xử lý biên: bài này không có số liệu vào nên không có giá trị biên. Thầy cô nhắc các con sao chép từng chữ cái cho khớp, vì thiếu hay thừa một dấu cách cũng làm kết quả khác đi.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: (không có dữ liệu vào))
| Bước | Lệnh chạy | Màn hình hiện ra |
|------|-----------|------------------|
| 1 | `print("Xin chao cac ban! Toi la Robot Python.")` | `Xin chao cac ban! Toi la Robot Python.` |
| 2 | Kết thúc chương trình | Kết quả cuối cùng: `Xin chao cac ban! Toi la Robot Python.` |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: quên dấu ngoặc kép quanh câu chữ, ví dụ viết `print(Xin chao cac ban! Toi la Robot Python.)`. Chương trình báo lỗi và không in ra gì cả. Cách sửa: luôn đặt câu chữ trong cặp dấu ngoặc kép `"..."`.
- Bẫy 2: gõ sai một chữ, ví dụ `print("Xin chao cac ban! Toi la Robot python.")` (chữ `p` thường). Màn hình hiện `... Robot python.` thay vì `... Robot Python.` nên bị tính là kết quả sai. Cách sửa: đối chiếu từng chữ với đề bài trước khi chạy.
- Bẫy 3: thêm lệnh `input()` ở đầu vì tưởng bài nào cũng phải nhập. Khi chạy, chương trình cứ đứng chờ các con gõ thêm, không in ra câu chào ngay. Cách sửa: bài này không có dữ liệu vào nên xóa dòng `input()`, chỉ giữ một dòng `print(...)`.

---

## 4. Lời giải tham khảo
```python
print("Xin chao cac ban! Toi la Robot Python.")
```
