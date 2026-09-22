# Hướng Dẫn Giảng Dạy

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là lướt qua dãy và đếm các số chia hết cho 2.
- Với số mẫu `N = 5`, dãy `2 5 8 10 13`: các số chẵn là `2`, `8`, `10`, tổng cộng `3` số.
- Quy trình trong lời giải với các biến `n`, `a`, `x`:
  - Đọc `n = 5`, dãy `a = [2, 5, 8, 10, 13]`.
  - Với mỗi `x`, kiểm tra `(x mod 2) == 0`: `2` đạt, `5` trượt, `8` đạt, `10` đạt, `13` trượt.
  - Cộng được `3` rồi in ra.
- Giá trị biên cụ thể: dãy không có số chẵn nào thì in `0`; dãy toàn số chẵn thì in `N`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5 / 2 5 8 10 13)

| Bước | Thao tác | Giá trị |
|------|----------|---------|
| 1 | Đọc `n` | `n = 5` |
| 2 | Đọc dãy `a` | `a = [2, 5, 8, 10, 13]` |
| 3 | Xét `2` | `(2 mod 2) == 0` nên đếm 1 |
| 4 | Xét `5` | `(5 mod 2) == 1` nên bỏ qua |
| 5 | Xét `8` | đếm 2 |
| 6 | Xét `10` | đếm 3 |
| 7 | Xét `13` | bỏ qua |
| 8 | In kết quả | màn hình hiện `3` |

Kết quả cuối cùng khớp với đáp án mẫu: `3`.

---

## 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — đếm nhầm số lẻ:
```text
n = câu trả lời
a = list(các khối hỏi và đợi cho từng biến)
nói (sum(1 for x in a if (x mod 2) == 1))

```
Với mẫu trên in ra `2` (số `5` và `13`), không khớp đáp án mẫu `3`. Cách sửa: điều kiện đúng là `(x mod 2) == 0`.
- Bẫy 2 — quên so sánh, chỉ viết `if (x mod 2)`:
```text
n = câu trả lời
a = list(các khối hỏi và đợi cho từng biến)
nói (sum(1 for x in a if (x mod 2)))

```
Với mẫu trên, `(x mod 2)` khác 0 với số lẻ nên lại đếm số lẻ, in ra `2` sai. Cách sửa: viết rõ `if (x mod 2) == 0`.
- Bẫy 3 — in ra danh sách các số chẵn thay vì số lượng:
```text
n = câu trả lời
a = list(các khối hỏi và đợi cho từng biến)
nói ([x for x in a if (x mod 2) == 0])

```
Với mẫu trên in ra `[2, 8, 10]`, không khớp đáp án mẫu `3`. Cách sửa: đếm bằng `sum(1 for x in a if (x mod 2) == 0)`.

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
