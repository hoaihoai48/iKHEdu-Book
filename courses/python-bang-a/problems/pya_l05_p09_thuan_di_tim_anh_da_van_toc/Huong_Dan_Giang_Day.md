# Hướng Dẫn Giảng Dạy: Thuận đi tìm ánh đa vận tốc
Chuyên đề: **Lựa Chọn Nhiều Hướng (if - elif - else)**

---

## 1. Ý tưởng & Phân tích thuật toán
- Thầy cô lưu ý: đề bài kể chuyện gặp nhau theo vị trí `x, y, v`, nhưng lời giải mẫu của lớp mình phân loại vận tốc `v` đọc dạng số thực: `v < 10` in `DI BO`, `v <= 30` in `XE DAP`, còn lại in `XE MAY`. Khi dạy cần bám đúng lời giải mẫu này.
- Cách làm của lời giải mẫu: đọc `v = float(input().strip())` rồi rẽ ba nhánh. Với mẫu `v = 15`: `15 < 10` sai, `15 <= 30` đúng nên in `XE DAP`.
- Xử lý biên: hai mốc cần thử là `v = 10` (vừa chạm mốc giữa, in `XE DAP`) và `v = 30` (vừa chạm mốc trên, vẫn in `XE DAP`), còn `v = 31` thì in `XE MAY`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 15)
Sample 1 với input mẫu: `15`.
| Bước | Việc làm | Giá trị của `v` | In ra |
|---|---|---|---|
| 1 | Đọc input dạng số thực | `v = 15.0` | — |
| 2 | Kiểm tra `15.0 < 10`? Sai | xuống nhánh `elif` | — |
| 3 | Kiểm tra `15.0 <= 30`? Đúng | rẽ nhánh hai | — |
| 4 | In theo nhánh | — | `XE DAP` |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1 — đọc `int` rồi so kiểu khác: không sao với `15`, nhưng với `v = 9.5` mà đọc `int` sẽ lỗi hoặc sai. Cách sửa: đọc `float` như lời giải mẫu.
- Bẫy 2 — đảo mốc `10` và `30`: bạn nhỏ viết `if v <= 30` trước rồi mới `elif v < 10`. Với `v = 5` sẽ rơi ngay nhánh một, trùng cờ vẫn đúng, nhưng cách viết rối dễ sai khi đổi mốc. Cách sửa: giữ đúng thứ tự `v < 10` trước, `v <= 30` sau.
- Bẫy 3 — in sai chữ: bạn nhỏ in `Xe dap` viết hoa chữ đầu. Với mẫu `15`, chương trình kiểm tra sẽ báo kết quả sai. Cách sửa: in đúng `DI BO`, `XE DAP`, `XE MAY` viết hoa toàn bộ.

---

## 4. Lời giải tham khảo
```python
v = float(input().strip())
if v < 10:
    print("DI BO")
elif v <= 30:
    print("XE DAP")
else:
    print("XE MAY")
```
