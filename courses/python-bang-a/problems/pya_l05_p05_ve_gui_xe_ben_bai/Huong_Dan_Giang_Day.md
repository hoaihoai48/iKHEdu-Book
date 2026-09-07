# Hướng Dẫn Giảng Dạy: Vé gửi xe bến bãi
Chuyên đề: **Lựa Chọn Nhiều Hướng (if - elif - else)**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất của bài này là tra bảng giá theo mã đã viết thường: `pt` là `1` hoặc `xe dap` thì `2000`, là `2` hoặc `xe may` thì `5000`, là `3` hoặc `o to` thì `30000`, còn lại in `LOI PHUONG TIEN`.
- Cách làm của lời giải mẫu: đọc `pt = input().strip().lower()` rồi rẽ bốn nhánh. Với mẫu `xe may`: viết thường vẫn là `xe may`, rơi vào nhánh hai nên in `5000`.
- Xử lý biên: thầy cô cho thử `XE DAP` viết hoa (nhờ `.lower()` nên vẫn nhận, in `2000`) và mã lạ `5` (in `LOI PHUONG TIEN`).

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: xe may)
Sample 1 với input mẫu: `xe may`.
| Bước | Việc làm | Giá trị của `pt` | In ra |
|---|---|---|---|
| 1 | Đọc input, cắt khoảng trắng, viết thường | `pt = 'xe may'` | — |
| 2 | Kiểm tra nhánh một (`1` / `xe dap`)? Sai | xuống nhánh hai | — |
| 3 | Kiểm tra `pt == '2' or pt == 'xe may'`? Đúng | rẽ nhánh hai | — |
| 4 | In `5000` | — | `5000` |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1 — quên viết thường: bạn nhỏ viết `pt = input().strip()` rồi so với `'xe may'`. Với mẫu `XE MAY` viết hoa sẽ không khớp, in `LOI PHUONG TIEN`, sai. Cách sửa: thêm `.lower()` như lời giải mẫu.
- Bẫy 2 — đọc `int` cho mã số: bạn nhỏ viết `pt = int(input())`. Với mẫu `xe may` chương trình sẽ lỗi. Cách sửa: đọc chuỗi như lời giải mẫu để nhận cả số và chữ.
- Bẫy 3 — quên nhánh mã lạ: bạn nhỏ chỉ viết ba nhánh xe mà không có `else`. Với mã `5` sẽ không in gì. Cách sửa: giữ nhánh cuối in `LOI PHUONG TIEN`.

---

## 4. Lời giải tham khảo
```python
pt = input().strip().lower()
if pt == "1" or pt == "xe dap":
    print(2000)
elif pt == "2" or pt == "xe may":
    print(5000)
elif pt == "3" or pt == "o to":
    print(30000)
else:
    print("LOI PHUONG TIEN")
```
