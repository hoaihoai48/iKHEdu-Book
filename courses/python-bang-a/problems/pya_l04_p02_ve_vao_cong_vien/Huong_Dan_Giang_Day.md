# Hướng Dẫn Giảng Dạy: Vé vào công viên
Chuyên đề: **Ngã Rẽ Quyết Định (if - else)**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất của bài này là một mốc cắt duy nhất `130`: chiều cao `h` từ `130` trở lên là vé người lớn, dưới `130` là vé trẻ em.
- Cách làm của lời giải mẫu: đọc `h`, kiểm tra `if h >= 130` thì in `VE NGUOI LON`, ngược lại in `VE TRE EM`. Với mẫu `h = 135`, vì `135 >= 130` nên in vé người lớn.
- Xử lý biên: ràng buộc `1 <= h <= 200`. Hai mốc cần thử là `h = 130` (vừa chạm mốc, vẫn là `VE NGUOI LON`) và `h = 129` (thấp hơn một đơn vị, là `VE TRE EM`).

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 135)
Sample 1 với input mẫu: `135`.
| Bước | Việc làm | Giá trị của `h` | In ra |
|---|---|---|---|
| 1 | Đọc input | `h = 135` | — |
| 2 | Kiểm tra `135 >= 130`? Đúng | rẽ nhánh `if` | — |
| 3 | In theo nhánh đúng | — | `VE NGUOI LON` |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1 — viết sai mốc so sánh: bạn nhỏ viết `if h > 130`. Với `h = 130` sẽ rơi sang vé trẻ em, sai. Cách sửa: dùng `>=` như lời giải mẫu.
- Bẫy 2 — in sai chữ: bạn nhỏ in `VE NGUOI LON` thiếu chữ hoặc thêm dấu, ví dụ `VE NGUOI LON ` có khoảng trắng thừa hay `VÉ NGƯỜI LỚN` có dấu. Với mẫu `135`, chương trình kiểm tra sẽ báo kết quả sai. Cách sửa: chép đúng từng chữ in hoa không dấu `VE NGUOI LON`.
- Bẫy 3 — đảo hai nhánh: bạn nhỏ cho nhánh `if` in `VE TRE EM`. Với mẫu `135` sẽ in vé trẻ em, sai. Cách sửa: nhánh `h >= 130` in `VE NGUOI LON`, nhánh còn lại in `VE TRE EM`.

---

## 4. Lời giải tham khảo
```python
h = int(input())
if h >= 130:
    print("VE NGUOI LON")
else:
    print("VE TRE EM")
```
