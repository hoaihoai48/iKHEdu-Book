# Hướng Dẫn Giảng Dạy

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là rút ra ba con số của cả lớp: cao nhất, thấp nhất và trung bình.
- Với số mẫu `N = 5`, các điểm `8 7 10 6 9`: cao nhất là `10`, thấp nhất là `6`, tổng `40` chia `5` được trung bình `8.0`.
- Quy trình trong lời giải với các biến `n`, `data`:
  - Đọc `n = 5`, gom đủ 5 điểm vào `data = [8, 7, 10, 6, 9]`.
  - In `max(data)` được `10`, in `min(data)` được `6`, in `sum(data) / n` với 1 chữ số thập phân được `8.0`.
- Giá trị biên cụ thể: `N = 1` thì cao nhất, thấp nhất và trung bình đều bằng điểm duy nhất đó; điểm từ `0` đến `10` nên tổng vừa trong số nguyên thường.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5 / 8 7 10 6 9)

| Bước | Thao tác | Giá trị |
|------|----------|---------|
| 1 | Đọc `n` | `n = 5` |
| 2 | Gom `data` | `data = [8, 7, 10, 6, 9]` |
| 3 | In `max(data)` | màn hình dòng 1 hiện `10` |
| 4 | In `min(data)` | màn hình dòng 2 hiện `6` |
| 5 | Tính `sum(data) / n` | `40 / 5 = 8.0` |
| 6 | In trung bình | màn hình dòng 3 hiện `8.0` |

Kết quả cuối cùng khớp với đáp án mẫu: `10` rồi `6` rồi `8.0`.

---

## 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — in trung bình thiếu phần thập phân:
```text
n = câu trả lời
data = []
while len(data) < n:
    data += list(các khối hỏi và đợi cho từng biến)
data = data[:n]
nói (max(data))
nói (min(data))
nói (sum(data) // n)

```
Với mẫu trên dòng 3 in ra `8`, không khớp đáp án mẫu `8.0`. Cách sửa: in bằng `nói (f"{sum(data) / n:.1f}")`.
- Bẫy 2 — in cao nhất và thấp nhất trên cùng một dòng:
```text
n = câu trả lời
data = []
while len(data) < n:
    data += list(các khối hỏi và đợi cho từng biến)
data = data[:n]
nói (max(data), min(data))
nói (f"{sum(data) / n:.1f}")

```
Với mẫu trên dòng đầu in ra `10 6`, không khớp đáp án mẫu mỗi số một dòng. Cách sửa: in `max` và `min` bằng hai lệnh riêng.
- Bẫy 3 — chỉ đọc một dòng điểm nên thiếu khi điểm rải nhiều dòng:
```text
n = câu trả lời
data = list(các khối hỏi và đợi cho từng biến)
nói (max(data))
nói (min(data))
nói (f"{sum(data) / n:.1f}")

```
Với mẫu một dòng điểm vẫn ra đúng, nhưng khi điểm nằm rải nhiều dòng thì `data` thiếu số và kết quả sai. Cách sửa: gom bằng vòng lặp `while len(data) < n`.

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - hỏi [Nhập n:] và đợi
> - đặt [n] thành (câu trả lời)
> - xóa tất cả của [data]
> - lặp lại cho đến khi không còn <độ dài của data < n>:
> -   thay đổi [data] một lượng (list(...))
> - đặt [data] thành (giá trị)
> - nói (max(...))
> - nói (min(...))
> - nói (giá trị)
