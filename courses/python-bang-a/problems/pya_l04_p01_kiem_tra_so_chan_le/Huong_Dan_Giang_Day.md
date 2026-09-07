# Hướng Dẫn Giảng Dạy: Kiểm tra số chẵn lẻ
Chuyên đề: **Ngã Rẽ Quyết Định (if - else)**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất của bài này là phép chia lấy dư cho `2`: số `n` mà `n % 2 == 0` là số chẵn, còn dư `1` là số lẻ.
- Cách làm của lời giải mẫu: đọc `n`, kiểm tra `if n % 2 == 0` thì in `CHAN`, ngược lại in `LE`. Với mẫu `n = 18`, vì `18 % 2 = 0` nên in `CHAN`.
- Xử lý biên: ràng buộc `0 <= N <= 10^9`. Hai mốc cần nhớ là `N = 0` (vì `0 % 2 = 0` nên là `CHAN`) và `N = 10^9` vẫn tính bình thường.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 18)
Sample 1 với input mẫu: `18`.
| Bước | Việc làm | Giá trị của `n` | In ra |
|---|---|---|---|
| 1 | Đọc input | `n = 18` | — |
| 2 | Tính `18 % 2` được `0`, điều kiện đúng | rẽ nhánh `if` | — |
| 3 | In theo nhánh chẵn | — | `CHAN` |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1 — chia hết cho `3` thay vì `2`: bạn nhỏ viết `if n % 3 == 0`. Với mẫu `18` thì trùng cờ vẫn đúng, nhưng với `n = 9` sẽ in `CHAN` sai. Cách sửa: luôn chia dư cho `2`.
- Bẫy 2 — in chữ thường: bạn nhỏ in `Chan` hoặc `chan`. Với mẫu `18`, chương trình kiểm tra sẽ báo kết quả sai vì thiếu chữ in hoa. Cách sửa: in đúng `CHAN` và `LE` viết hoa toàn bộ.
- Bẫy 3 — quên số 0: bạn nhỏ nghĩ `0` là số lẻ. Thực ra `0 % 2 = 0` nên `0` là `CHAN`. Cách sửa: tin vào phép chia dư, không đoán bằng cảm giác.

---

## 4. Lời giải tham khảo
```python
n = int(input())
if n % 2 == 0:
    print("CHAN")
else:
    print("LE")
```
