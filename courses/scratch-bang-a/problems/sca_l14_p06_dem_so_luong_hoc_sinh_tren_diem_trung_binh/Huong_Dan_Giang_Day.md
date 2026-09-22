# Hướng Dẫn Giảng Dạy

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là tính điểm trung bình cả lớp trước, rồi đếm các bạn có điểm từ mức trung bình trở lên.
- Với số mẫu `N = 4`, các điểm `8 6 10 4`: tổng `28` chia `4` được trung bình `7.0`; các bạn đạt từ `7.0` trở lên là bạn điểm `8` và bạn điểm `10`, tổng cộng `2` bạn.
- Quy trình trong lời giải với các biến `n`, `a`, `tb`, `x`:
  - Đọc `n = 4`, dãy điểm `a = [8.0, 6.0, 10.0, 4.0]`.
  - Tính `tb = 28.0 / 4 = 7.0`.
  - Đếm `x >= 7.0`: `8` đạt, `6` trượt, `10` đạt, `4` trượt, được `2` rồi in ra.
- Giá trị biên cụ thể: `N = 1` thì bạn duy nhất luôn bằng trung bình nên đáp án là `1`; bạn đúng bằng trung bình vẫn được tính vì đề bài ghi lớn hơn hoặc bằng.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 4 / 8 6 10 4)

| Bước | Thao tác | Giá trị |
|------|----------|---------|
| 1 | Đọc `n` | `n = 4` |
| 2 | Đọc dãy `a` | `a = [8.0, 6.0, 10.0, 4.0]` |
| 3 | Tính `tb = sum(a) / n` | `28.0 / 4 = 7.0` |
| 4 | Xét `8`, `6`, `10`, `4` | đạt, trượt, đạt, trượt |
| 5 | In kết quả | màn hình hiện `2` |

Kết quả cuối cùng khớp với đáp án mẫu: `2`.

---

## 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — dùng lớn hơn hẳn thay vì lớn hơn hoặc bằng:
```text
n = câu trả lời
a = list(map(float, câu trả lời))
tb = sum(a) / n
nói (sum(1 for x in a if x > tb))

```
Với mẫu trên vẫn ra `2`, nhưng lớp như `7 7 7 7` (trung bình `7.0`) thì đáp án đúng là `4` mà cách này in `0`. Cách sửa: điều kiện đúng là `x >= tb`.
- Bẫy 2 — đọc điểm bằng số nguyên nên lỗi khi gặp điểm lẻ:
```text
n = câu trả lời
a = list(các khối hỏi và đợi cho từng biến)
tb = sum(a) / n
nói (sum(1 for x in a if x >= tb))

```
Với mẫu toàn điểm nguyên vẫn ra `2`, nhưng điểm `7.5` trong đề là số thực nên `int("7.5")` gây lỗi chương trình. Cách sửa: đọc bằng `map(float, câu trả lời)`.
- Bẫy 3 — đếm trước khi tính trung bình:
```text
n = câu trả lời
a = list(map(float, câu trả lời))
dem = sum(1 for x in a if x >= sum(a) / len(a) - 1)
nói (dem)

```
Với mẫu trên, ngưỡng bị trừ 1 thành `6.0` nên đếm cả bạn điểm `6`, in ra `3` sai. Cách sửa: tính `tb = sum(a) / n` rồi đếm `x >= tb`.

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
> - đặt [tb] thành (sum(...) / n)
> - nói (sum(...))
