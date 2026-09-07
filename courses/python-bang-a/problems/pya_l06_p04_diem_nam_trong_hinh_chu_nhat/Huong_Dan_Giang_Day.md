# Hướng Dẫn Giảng Dạy: Điểm nằm trong hình chữ nhật
Chuyên đề: **Liên Minh Điều Kiện (and - or - not)**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất của bài này là kiểm tra điểm có nằm trong khung từ `(0, 0)` tới `(w, h)` hay không, tính cả mép biên: `0 <= x <= w` và `0 <= y <= h`.
- Cách làm của lời giải mẫu: đọc một dòng bốn số theo thứ tự `x, y, w, h`, nếu cả hai điều kiện đúng thì in `TRONG`, ngược lại in `NGOAI`. Với mẫu `2 3 5 5`: `x = 2, y = 3, w = 5, h = 5`; `0 <= 2 <= 5` đúng và `0 <= 3 <= 5` đúng nên in `TRONG`.
- Xử lý biên: thầy cô lưu ý thứ tự đọc của lời giải mẫu là `x, y, w, h` (điểm trước, khung sau). Điểm nằm đúng mép như `x = 5, y = 5` vẫn là `TRONG` vì dấu `<=` bao cả biên.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 2 3 5 5)
Sample 1 với input mẫu: `2 3 5 5`.
| Bước | Việc làm | Giá trị các biến | In ra |
|---|---|---|---|
| 1 | Đọc một dòng, tách bốn số | `x = 2, y = 3, w = 5, h = 5` | — |
| 2 | Kiểm tra `0 <= 2 <= 5`? Đúng | tiếp tục | — |
| 3 | Kiểm tra `0 <= 3 <= 5`? Đúng, cả hai đúng | rẽ nhánh `if` | — |
| 4 | In kết quả | — | `TRONG` |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1 — đọc sai thứ tự: bạn nhỏ tưởng thứ tự là `w, h, x, y` rồi gán ngược. Với mẫu `2 3 5 5` sẽ kiểm tra khung `(2, 3)` và điểm `(5, 5)`, cho `NGOAI`, sai. Cách sửa: giữ đúng thứ tự `x, y, w, h` như lời giải mẫu.
- Bẫy 2 — dùng `<` thay vì `<=`: bạn nhỏ viết `0 <= x < w`. Với điểm nằm đúng mép `x = 5, w = 5` sẽ in `NGOAI`, sai vì đề cho tính cả mép. Cách sửa: dùng `<=` hai đầu.
- Bẫy 3 — dùng `or` thay vì `and`: bạn nhỏ viết `if 0 <= x <= w or 0 <= y <= h`. Với điểm `x = 99` ngoài khung nhưng `y` còn trong khung sẽ in `TRONG`, sai. Cách sửa: nối hai vế bằng `and`.

---

## 4. Lời giải tham khảo
```python
# Nhap x, y va HCN (0, 0) den (W, H)
parts = list(map(int, input().split()))
x, y, w, h = parts[0], parts[1], parts[2], parts[3]
if 0 <= x <= w and 0 <= y <= h:
    print("TRONG")
else:
    print("NGOAI")
```
