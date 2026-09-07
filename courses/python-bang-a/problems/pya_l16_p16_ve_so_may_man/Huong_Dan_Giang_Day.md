# Hướng Dẫn Giảng Dạy: Vé số may mắn
Chuyên đề: **Chiếc Hộp Thần Kỳ list & Thao Tác Cơ Bản**

---

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là cộng các chữ số của tấm vé rồi xem tổng có chia hết cho 7 không.
- Với số mẫu `N = 1234`: tổng các chữ số là `1 + 2 + 3 + 4 = 10`, `10` chia 7 dư 3 nên không may mắn, đáp án `NO`. (Đề bài cho thêm ví dụ vé `16` có tổng `7` nên đáp án là `YES`.)
- Quy trình trong lời giải với các biến `s`, `t`, `c`:
  - Đọc chuỗi `s = "1234"`, đặt `t = 0`.
  - Với mỗi ký tự `c`, nếu là chữ số thì cộng giá trị của nó vào `t`: `t` lần lượt thành `1`, `3`, `6`, `10`.
  - Vì `10 % 7 = 3` khác 0 nên in `NO`.
- Giá trị biên cụ thể: `N` dài tới 19 chữ số nên giữ nguyên dạng chuỗi, không đổi sang số nguyên rồi tách; tổng các chữ số bằng đúng 7 hoặc 14 thì in `YES`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 1234)

| Bước | Thao tác | Giá trị |
|------|----------|---------|
| 1 | Đọc `s` | `s = "1234"`, `t = 0` |
| 2 | Xét `1` | `t = 1` |
| 3 | Xét `2` | `t = 3` |
| 4 | Xét `3` | `t = 6` |
| 5 | Xét `4` | `t = 10` |
| 6 | Kiểm tra `t % 7` | `10 % 7 = 3` khác 0 |
| 7 | In kết quả | màn hình hiện `NO` |

Kết quả cuối cùng khớp với đáp án mẫu: `NO`.

---

## 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — viết ngược hai nhánh kết quả:
```python
s = input().strip()
t = 0
for c in s:
    if "0" <= c <= "9":
        t += ord(c) - ord("0")
if t % 7 == 0:
    print("NO")
else:
    print("YES")
```
Với mẫu `1234` in ra `YES` sai. Cách sửa: tổng chia hết cho 7 thì in `YES`, ngược lại in `NO`.
- Bẫy 2 — cộng mã ký tự mà quên đổi ra giá trị số:
```python
s = input().strip()
t = 0
for c in s:
    t += ord(c)
if t % 7 == 0:
    print("YES")
else:
    print("NO")
```
Với mẫu `1234`, `t` thành `49 + 50 + 51 + 52 = 202` thay vì `10`; với vé `16` thì `t = 103`, `103` chia 7 dư 5 nên in `NO` trong khi đáp án đúng phải là `YES`. Cách sửa: cộng `ord(c) - ord("0")`.
- Bẫy 3 — kiểm tra số vé thay vì tổng chữ số:
```python
s = input().strip()
if int(s) % 7 == 0:
    print("YES")
else:
    print("NO")
```
Đề bài yêu cầu xét tổng các chữ số, không phải số vé; vé `16` có tổng `7` nên phải `YES` nhưng `16` chia 7 dư 2 nên cách này in `NO`. Cách sửa: cộng từng chữ số rồi mới xét chia hết cho 7.

---

## 4. Lời giải tham khảo

```python
s = input().strip()
t = 0
for c in s:
    if "0" <= c <= "9":
        t += ord(c) - ord("0")
if t % 7 == 0:
    print("YES")
else:
    print("NO")
```
