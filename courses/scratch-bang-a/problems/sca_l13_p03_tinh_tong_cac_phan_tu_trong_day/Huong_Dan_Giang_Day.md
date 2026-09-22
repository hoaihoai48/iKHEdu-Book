# Hướng Dẫn Giảng Dạy

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là cộng tất cả các số trong danh sách lại thành một tổng duy nhất.
- Với số mẫu `N = 4`, dãy `10 20 30 40`: tổng là `10 + 20 + 30 + 40 = 100`.
- Quy trình trong lời giải với các biến `n`, `a`:
  - Đọc `n = 4`.
  - Đọc dãy `a = [10, 20, 30, 40]`.
  - Gọi `sum(a)` được `100` rồi in ra.
- Giá trị biên cụ thể: mỗi phần tử có thể tới `10^9` và `N` tới `10^5` nên tổng có thể rất lớn, Python cộng số nguyên lớn trực tiếp nên vẫn đúng.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 4 / 10 20 30 40)

| Bước | Thao tác | Giá trị |
|------|----------|---------|
| 1 | Đọc `n` | `n = 4` |
| 2 | Đọc dãy `a` | `a = [10, 20, 30, 40]` |
| 3 | Tính `sum(a)` | `10 + 20 + 30 + 40 = 100` |
| 4 | In kết quả | màn hình hiện `100` |

Kết quả cuối cùng khớp với đáp án mẫu: `100`.

---

## 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — nhầm hàm `max` với `sum`:
```text
n = câu trả lời
a = list(các khối hỏi và đợi cho từng biến)
nói (max(a))

```
Với mẫu trên in ra `40`, không khớp đáp án mẫu `100`. Cách sửa: dùng `nói (sum(a))`.
- Bẫy 2 — đặt tổng ban đầu là `1` rồi nhân nhầm:
```text
n = câu trả lời
a = list(các khối hỏi và đợi cho từng biến)
tong = 1
for x in a:
    tong = tong + x
nói (tong)

```
Với mẫu trên in ra `101` vì cộng dư 1 ban đầu. Cách sửa: đặt `tong = 0` hoặc dùng `sum(a)`.
- Bẫy 3 — quên đổi sang số nguyên khi đọc:
```text
n = câu trả lời
a = câu trả lời
nói (sum(a))

```
Với mẫu trên, `sum` cộng các chuỗi `"10"`, `"20"` gây lỗi chương trình. Cách sửa: đọc bằng `a = list(các khối hỏi và đợi cho từng biến)`.

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - hỏi [Nhập n:] và đợi
> - đặt [n] thành (câu trả lời)
> - xóa tất cả của danh sách [a]
> - đặt [i] thành 1
> - lặp lại (n) lần:
> -   hỏi [Nhập phần tử:] và đợi
> -   thêm (câu trả lời) vào [a]
> -   thay đổi [i] một lượng 1
> - nói (sum(...))
