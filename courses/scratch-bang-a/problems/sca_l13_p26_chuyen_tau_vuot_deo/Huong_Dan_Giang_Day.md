# Hướng Dẫn Giảng Dạy: Chuyến tàu vượt đèo
Chuyên đề: **Lập Trình Thuật Toán & Khối Lệnh Scratch 3.0**

---

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là đếm các ngọn đèo cao hơn mọi ngọn đã đi qua, ngọn đầu tiên luôn được tính một lần.
- Với số mẫu `N = 6`, các độ cao `1 3 5 2 4 7`: ngọn `1` reo lần 1, `3` cao hơn `1` reo lần 2, `5` cao hơn reo lần 3, `2` và `4` thấp hơn `5` nên lặng im, `7` cao nhất reo lần 4. Đáp án là `4`.
- Quy trình trong lời giải với các biến `n`, `data`, `best`, `c`, `x`:
  - Đọc `n = 6`, gom `data = [1, 3, 5, 2, 4, 7]`; đặt `best = 1`, `c = 1`.
  - Xét `3 > 1` nên `best = 3`, `c = 2`. Xét `5 > 3` nên `best = 5`, `c = 3`. Xét `2` và `4` không vượt `5`. Xét `7 > 5` nên `best = 7`, `c = 4`.
  - In `4`.
- Giá trị biên cụ thể: `N = 1` thì chỉ reo đúng 1 lần; dãy xếp giảm dần thì cũng chỉ reo 1 lần ở ngọn đầu.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 6 / 1 3 5 2 4 7)

| Bước | Thao tác | Giá trị |
|------|----------|---------|
| 1 | Đọc `n`, gom `data` | `n = 6`, `data = [1, 3, 5, 2, 4, 7]` |
| 2 | Khởi đầu | `best = 1`, `c = 1` |
| 3 | Xét `3` | `3 > 1` nên `best = 3`, `c = 2` |
| 4 | Xét `5` | `5 > 3` nên `best = 5`, `c = 3` |
| 5 | Xét `2`, `4` | không vượt `5` nên bỏ qua |
| 6 | Xét `7` | `7 > 5` nên `best = 7`, `c = 4` |
| 7 | In kết quả | màn hình hiện `4` |

Kết quả cuối cùng khớp với đáp án mẫu: `4`.

---

## 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — dùng `>=` nên đếm cả đèo cao bằng:
```text
n = int(câu trả lời)
data = []
while len(data) < n:
    data += list(map(int, câu trả lời.split()))
data = data[:n]
best = data[0]
c = 1
for x in data[1:]:
    if x >= best:
        best = x
        c += 1
print(c)
```
Đề bài yêu cầu đèo cao hơn hẳn mới reo; dãy như `5 5 5` phải reo 1 lần nhưng cách này đếm 3. Cách sửa: điều kiện đúng là `x > best`.
- Bẫy 2 — đặt đỉnh cao nhất ban đầu là 0:
```text
n = int(câu trả lời)
data = []
while len(data) < n:
    data += list(map(int, câu trả lời.split()))
data = data[:n]
best = 0
c = 0
for x in data:
    if x > best:
        best = x
        c += 1
print(c)
```
Với mẫu trên vẫn ra `4`, nhưng dãy toàn số âm (ví dụ `-5 -2`) thì `best = 0` chặn hết và in `0` sai. Cách sửa: đặt `best = data[0]`, `c = 1`.
- Bẫy 3 — quên đếm ngọn đèo đầu tiên:
```text
n = int(câu trả lời)
data = []
while len(data) < n:
    data += list(map(int, câu trả lời.split()))
data = data[:n]
best = data[0]
c = 0
for x in data[1:]:
    if x > best:
        best = x
        c += 1
print(c)
```
Với mẫu trên in ra `3` vì mất lần reo của ngọn `1`. Cách sửa: đặt `c = 1` ngay từ đầu.

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - hỏi [Nhập n:] và đợi
> - đặt [n] thành (câu trả lời)
> - xóa tất cả của [danh_sach]
> - đặt [i] thành (1)
> - lặp lại (n) lần:
> -   hỏi [Nhập phần tử:] và đợi
> -   thêm (câu trả lời) vào [danh_sach]
> -   thay đổi [i] một lượng (1)
> - nói (phần tử thứ 1 của [danh_sach])
