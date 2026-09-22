# Hướng Dẫn Giảng Dạy

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là viết dãy số theo chiều từ cuối về đầu, phần tử cuối lên trước.
- Với số mẫu `N = 4`, dãy `1 2 3 4`: đọc ngược lại được `4 3 2 1`.
- Quy trình trong lời giải với các biến `n`, `a`:
  - Đọc `n = 4`.
  - Đọc dãy `a = [1, 2, 3, 4]`.
  - Lấy lát cắt đảo `a[::-1]` được `[4, 3, 2, 1]` rồi in ra.
- Giá trị biên cụ thể: `N = 1` thì dãy đảo giống hệt dãy ban đầu (ví dụ `7` vẫn in `7`).

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 4 / 1 2 3 4)

| Bước | Thao tác | Giá trị |
|------|----------|---------|
| 1 | Đọc `n` | `n = 4` |
| 2 | Đọc dãy `a` | `a = [1, 2, 3, 4]` |
| 3 | Lấy `a[::-1]` | `[4, 3, 2, 1]` |
| 4 | In kết quả | màn hình hiện `4 3 2 1` |

Kết quả cuối cùng khớp với đáp án mẫu: `4 3 2 1`.

---

## 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — in ra cả dãy gốc vì quên đảo:
```text
n = câu trả lời
a = list(các khối hỏi và đợi cho từng biến)
nói (*a)

```
Với mẫu trên in ra `1 2 3 4`, không khớp đáp án mẫu `4 3 2 1`. Cách sửa: in `nói (*(a[::-1]))`.
- Bẫy 2 — dùng `reversed` mà không tách sao:
```text
n = câu trả lời
a = list(các khối hỏi và đợi cho từng biến)
nói (reversed(a))

```
Với mẫu trên in ra dòng mô tả vật đảo thay vì dãy số. Cách sửa: in `nói (*reversed(a))` hoặc `nói (*(a[::-1]))`.
- Bẫy 3 — in cả ngoặc của danh sách:
```text
n = câu trả lời
a = list(các khối hỏi và đợi cho từng biến)
nói (a[::-1])

```
Với mẫu trên in ra `[4, 3, 2, 1]` có ngoặc và dấu phẩy, không khớp đáp án mẫu `4 3 2 1`. Cách sửa: thêm dấu sao `nói (*(a[::-1]))`.

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
> - đặt [ket_qua] thành rỗng
> - đặt [i] thành 1
> - lặp lại (kích thước của [danh_sach]) lần:
> -   đặt [ket_qua] thành kết hợp ket_qua và phần tử i và dấu cách
> -   thay đổi [i] một lượng 1
> - nói (ket_qua)
