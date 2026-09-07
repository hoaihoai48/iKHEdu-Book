# Hướng Dẫn Giảng Dạy: Liệt kê tất cả ước số
Chuyên đề: **Ước Số, Bội Số & Số Nguyên Tố Cơ Bản**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất của bài này: với `n = 12`, duyệt `i` từ `1` tới `12`, số nào chia hết `12` thì góp vào danh sách `uoc`.
- Danh sách `uoc` chứa chuỗi ký tự (`str(i)`), vì duyệt `i` tăng dần nên các ước đã sẵn theo thứ tự tăng dần.
- Với `n = 12` thu được `["1", "2", "3", "4", "6", "12"]` rồi nối bằng `" ".join(uoc)` thành `1 2 3 4 6 12`.
- Thầy cô cho các em khoanh các ước của `12` trên giấy rồi đối chiếu với danh sách.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 12)
| `i` | `12 % i` | Danh sách `uoc` sau bước |
| --- | --- | --- |
| 1 | 0 | `["1"]` |
| 2 | 0 | `["1", "2"]` |
| 3 | 0 | `["1", "2", "3"]` |
| 4 | 0 | `["1", "2", "3", "4"]` |
| 5 | 2 | không đổi |
| 6 | 0 | `["1", "2", "3", "4", "6"]` |
| 7 | 5 | không đổi |
| 8 | 4 | không đổi |
| 9 | 3 | không đổi |
| 10 | 2 | không đổi |
| 11 | 1 | không đổi |
| 12 | 0 | `["1", "2", "3", "4", "6", "12"]` |

Kết quả in ra: `1 2 3 4 6 12`, khớp với kết quả mẫu.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: thêm số nguyên vào danh sách rồi mới nối chuỗi:
```python
uoc.append(i)
print(" ".join(uoc))
```
với mẫu `12` chương trình báo lỗi vì không nối được số với chuỗi. Sửa lại: `uoc.append(str(i))`.
- Bẫy 2: in danh sách trực tiếp `print(uoc)`. Với mẫu `12` sẽ in `['1', '2', ...]` kèm ngoặc và dấu phẩy, là kết quả sai. Sửa lại: `print(" ".join(uoc))`.
- Bẫy 3: duyệt `range(1, n)` thiếu `n`. Với mẫu `12` sẽ mất ước `12` và chỉ in `1 2 3 4 6`. Sửa lại: `range(1, n + 1)`.

---

## 4. Lời giải tham khảo
```python
n = int(input())
uoc = []
for i in range(1, n + 1):
    if n % i == 0:
        uoc.append(str(i))
print(" ".join(uoc))
```
