# Hướng Dẫn Giảng Dạy

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: in dãy số đếm 1, 2, 3, ..., N trên cùng một dòng, mỗi số cách nhau một dấu cách. Đây là bài làm quen với `range(1, n + 1)` sinh đúng N số.
- Quy trình trong lời giải: đọc `n`, rồi `" ".join(str(i) for i in range(1, n + 1))` biến từng số `i` thành chữ rồi nối lại bằng dấu cách, cuối cùng `print` một lần.
- Xử lý biên: với N nhỏ nhất là 1 thì chỉ in `1`; với N lớn nhất là 100 thì in đủ 100 số từ `1` tới `100`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5)
| Bước | Giá trị của `n` | `i` sinh ra từ `range(1, n + 1)` | Chuỗi sau `join` |
|---|---|---|---|
| 1 | 5 | 1, 2, 3, 4, 5 | `1 2 3 4 5` |

Chương trình in ra một dòng duy nhất `1 2 3 4 5`, khớp với kết quả mẫu.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1 — dùng `range(n)`:
```text
n = câu trả lời
nói (" ".join(str(i) for i in range(n)))

```
Với mẫu `5` sẽ in ra `0 1 2 3 4`, cho kết quả sai vì dãy bắt đầu từ 0 và thiếu số 5. Cách sửa: dùng `range(1, n + 1)`.
- Bẫy 2 — mỗi số một dòng:
```text
n = câu trả lời
for i in range(1, n + 1):
    nói (i)

```
Với mẫu `5` sẽ in 5 dòng thay vì một dòng `1 2 3 4 5`. Cách sửa: gom thành một chuỗi bằng `" ".join(...)` rồi in một lần.

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - hỏi [Nhập n:] và đợi
> - đặt [n] thành (câu trả lời)
> - đặt [ket_qua] thành rỗng
> - đặt [i] thành 1
> - lặp lại (n) lần:
> -   đặt [ket_qua] thành kết hợp ket_qua và i và dấu cách
> -   thay đổi [i] một lượng 1
> - nói (ket_qua)
