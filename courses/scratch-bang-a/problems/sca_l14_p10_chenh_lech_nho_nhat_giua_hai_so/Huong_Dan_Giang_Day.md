# Hướng Dẫn Giảng Dạy

## 1. Ý tưởng & Phân tích thuật toán

- Lưu ý cho thầy cô: phần Bối cảnh trong đề bài viết chung chung về tìm lớn nhất hoặc nhỏ nhất, nhưng Nhiệm vụ và lời giải đều làm việc khác là tìm độ chênh lệch nhỏ nhất. Khi dạy, bám theo Nhiệm vụ và lời giải.
- Bản chất của bài này là xếp dãy tăng dần rồi so từng đôi đứng cạnh nhau, đôi nào gần nhau nhất cho đáp án.
- Với số mẫu `N = 4`, dãy `10 1 8 15`: xếp lại thành `1 8 10 15`; các độ chênh lệch kề nhau là `7`, `2`, `5`, nhỏ nhất là `2` (cặp `8` và `10`).
- Quy trình trong lời giải với các biến `n`, `a`, `min_diff`, `i`:
  - Đọc `n = 4`, dãy `a = [10, 1, 8, 15]`; gọi `a.sort()` được `[1, 8, 10, 15]`.
  - Tính các hiệu kề nhau `8 - 1 = 7`, `10 - 8 = 2`, `15 - 10 = 5`, lấy nhỏ nhất được `2` rồi in ra.
- Giá trị biên cụ thể: `N = 2` thì đáp án là hiệu của đúng hai số đó; đề bài cho các số đôi một khác nhau nên đáp án luôn lớn hơn 0.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 4 / 10 1 8 15)

| Bước | Thao tác | Giá trị |
|------|----------|---------|
| 1 | Đọc `n` | `n = 4` |
| 2 | Đọc dãy `a` | `a = [10, 1, 8, 15]` |
| 3 | Gọi `a.sort()` | `a = [1, 8, 10, 15]` |
| 4 | Tính hiệu kề nhau | `7`, `2`, `5` |
| 5 | Lấy nhỏ nhất và in | màn hình hiện `2` |

Kết quả cuối cùng khớp với đáp án mẫu: `2`.

---

## 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — lấy hiệu hai số đầu mà quên xếp:
```text
n = câu trả lời
a = list(các khối hỏi và đợi cho từng biến)
nói (abs(a[1] - a[0]))

```
Với mẫu trên in ra `|1 - 10| = 9`, không khớp đáp án mẫu `2`. Cách sửa: xếp tăng dần rồi so các đôi kề nhau.
- Bẫy 2 — so mọi đôi bằng hai vòng lặp:
```text
n = câu trả lời
a = list(các khối hỏi và đợi cho từng biến)
nho = abs(a[0] - a[1])
for i in range(n):
    for j in range(i + 1, n):
        nho = min(nho, abs(a[i] - a[j]))
nói (nho)

```
Với mẫu 4 số vẫn ra `2`, nhưng với `N = 10^5` thì số đôi quá lớn, chạy rất lâu. Cách sửa: xếp rồi chỉ so đôi kề nhau như lời giải.
- Bẫy 3 — lấy hiệu lớn nhất thay vì nhỏ nhất:
```text
n = câu trả lời
a = list(các khối hỏi và đợi cho từng biến)
a.sort()
min_diff = max(a[i + 1] - a[i] for i in range(n - 1))
nói (min_diff)

```
Với mẫu trên in ra `7` sai. Cách sửa: lấy nhỏ nhất bằng `min`.

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
> - đặt [min_diff] thành (min(...))
> - nói (min_diff)
