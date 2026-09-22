# Hướng Dẫn Giảng Dạy

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là xếp dãy tăng dần rồi nhặt bạn đứng chính giữa, vì `N` luôn là số lẻ nên lúc nào cũng có đúng một bạn giữa hàng.
- Với số mẫu `N = 5`, dãy `10 2 8 4 6`: xếp lại thành `2 4 6 8 10`, vị trí giữa (đếm từ 0 là vị trí `làm tròn xuống của (5 / 2) = 2`) là số `6`.
- Quy trình trong lời giải với các biến `n`, `a`:
  - Đọc `n = 5`, dãy `a = [10, 2, 8, 4, 6]`.
  - Gọi `a.sort()` được `[2, 4, 6, 8, 10]`.
  - Lấy `a[làm tròn xuống của (5 / 2)]` tức `a[2]` được `6` rồi in ra.
- Giá trị biên cụ thể: `N = 1` thì trung vị chính là số duy nhất đó; `N` lẻ tới `10^5` thì vị trí giữa là `làm tròn xuống của (n / 2)`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5 / 10 2 8 4 6)

| Bước | Thao tác | Giá trị |
|------|----------|---------|
| 1 | Đọc `n` | `n = 5` |
| 2 | Đọc dãy `a` | `a = [10, 2, 8, 4, 6]` |
| 3 | Gọi `a.sort()` | `a = [2, 4, 6, 8, 10]` |
| 4 | Tính vị trí giữa `làm tròn xuống của (n / 2)` | `làm tròn xuống của (5 / 2) = 2` |
| 5 | Lấy `a[2]` và in | màn hình hiện `6` |

Kết quả cuối cùng khớp với đáp án mẫu: `6`.

---

## 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — lấy vị trí giữa mà quên xếp:
```text
n = câu trả lời
a = list(các khối hỏi và đợi cho từng biến)
nói (a[làm tròn xuống của (n / 2)])

```
Với mẫu trên, `a[2]` của dãy gốc là `8`, không khớp đáp án mẫu `6`. Cách sửa: gọi `a.sort()` trước khi lấy.
- Bẫy 2 — lấy lệch sang vị trí kế bên:
```text
n = câu trả lời
a = list(các khối hỏi và đợi cho từng biến)
a.sort()
nói (a[làm tròn xuống của (n / 2) + 1])

```
Với mẫu trên in ra `a[3] = 8` sai. Cách sửa: vị trí giữa đếm từ 0 là `a[làm tròn xuống của (n / 2)]`.
- Bẫy 3 — lấy trung bình của dãy thay vì bạn đứng giữa:
```text
n = câu trả lời
a = list(các khối hỏi và đợi cho từng biến)
nói (sum(a) / n)

```
Với mẫu trên in ra `6.0` có dấu chấm, không khớp đáp án mẫu `6`. Cách sửa: xếp rồi nhặt phần tử giữa bằng `a[làm tròn xuống của (n / 2)]`.

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
> - nói (giá trị)
