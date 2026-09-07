# Hướng Dẫn Giảng Dạy: Tổng chữ số lớn nhất
Chuyên đề: **Chiếc Hộp Thần Kỳ list & Thao Tác Cơ Bản**

---

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là tính tổng các chữ số của từng số báo danh rồi chọn số có tổng lớn nhất; nếu hòa thì chọn số báo danh nhỏ hơn.
- Với số mẫu `N = 5`, các số `12 99 45 100 38`: tổng chữ số lần lượt là `3`, `18`, `9`, `1`, `11`; lớn nhất là `18` của số `99` nên đáp án là `99`.
- Quy trình trong lời giải với các biến `n`, `data`, `best`, `bs`, `x`, `s`:
  - Đọc `n = 5`, gom `data = [12, 99, 45, 100, 38]`; đặt `best = 12`, `bs = 3`.
  - Xét `99` có tổng `18 > 3` nên `best = 99`, `bs = 18`. Các số `45`, `100`, `38` có tổng `9`, `1`, `11` đều nhỏ hơn `18` nên bị loại.
  - In `99`.
- Giá trị biên cụ thể: số `0` có tổng chữ số là `0`; hai số hòa tổng (ví dụ `12` và `21` cùng tổng 3) thì số nhỏ hơn (`12`) thắng.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5 / 12 99 45 100 38)

| Bước | Thao tác | Giá trị |
|------|----------|---------|
| 1 | Đọc `n`, gom `data` | `n = 5`, `data = [12, 99, 45, 100, 38]` |
| 2 | Khởi đầu | `best = 12`, `bs = 1 + 2 = 3` |
| 3 | Xét `99` | tổng `18 > 3` nên `best = 99`, `bs = 18` |
| 4 | Xét `45` | tổng `9 < 18` nên loại |
| 5 | Xét `100` | tổng `1 < 18` nên loại |
| 6 | Xét `38` | tổng `11 < 18` nên loại |
| 7 | In kết quả | màn hình hiện `99` |

Kết quả cuối cùng khớp với đáp án mẫu: `99`.

---

## 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — quên luật hòa thì số nhỏ thắng:
```python
n = int(input())
data = []
while len(data) < n:
    data += list(map(int, input().split()))
data = data[:n]
best = data[0]
bs = sum(map(int, str(best)))
for x in data[1:]:
    s = sum(map(int, str(x)))
    if s > bs:
        best = x
        bs = s
print(best)
```
Với mẫu trên vẫn ra `99`, nhưng dãy như `12 21` (cùng tổng 3) thì cách thiếu `x < best` giữ số gặp trước hay sau tùy cách viết, dễ sai luật hòa. Cách sửa: điều kiện đủ là `if s > bs or (s == bs and x < best)`.
- Bẫy 2 — in tổng lớn nhất thay vì số báo danh:
```python
n = int(input())
data = []
while len(data) < n:
    data += list(map(int, input().split()))
data = data[:n]
print(max(sum(map(int, str(x))) for x in data))
```
Với mẫu trên in ra `18`, không khớp đáp án mẫu `99`. Cách sửa: ghi nhớ `best` là số báo danh rồi in `best`.
- Bẫy 3 — so sánh trực tiếp các số báo danh:
```python
n = int(input())
data = []
while len(data) < n:
    data += list(map(int, input().split()))
print(max(data[:n]))
```
Với mẫu trên in ra `100`, không khớp đáp án mẫu `99`. Cách sửa: so sánh tổng các chữ số, không so giá trị số.

---

## 4. Lời giải tham khảo

```python
n = int(input())
data = []
while len(data) < n:
    data += list(map(int, input().split()))
data = data[:n]
best = data[0]
bs = sum(map(int, str(best)))
for x in data[1:]:
    s = sum(map(int, str(x)))
    if s > bs or (s == bs and x < best):
        best = x
        bs = s
print(best)
```
