# Hướng Dẫn Giảng Dạy

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là tách số có 2 chữ số thành chữ số hàng chục và chữ số hàng đơn vị.
- Quy trình từng bước với đúng tên biến trong lời giải:
  - Bước 1: `n = câu trả lời` đọc số. Với mẫu, `n = 47`.
  - Bước 2: `don_vi = (n mod 10)` lấy phần dư khi chia 10, tức chữ số cuối. Với mẫu, `don_vi = 7`.
  - Bước 3: sao chép `temp = n` rồi lặp `while temp >= 10: temp = làm tròn xuống của (temp / 10)` để gọt dần tới khi còn chữ số đầu. Với mẫu, `temp` đi từ 47 về 4.
  - Bước 4: gán `chuc = temp` rồi in `nói (chuc, don_vi)` được `4 7`.
- Giá trị biên cụ thể: số nhỏ nhất là 10 (chục 1, đơn vị 0), số lớn nhất là 99 (chục 9, đơn vị 9).

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 47)

| Bước | Lệnh chạy | `n` | `don_vi` | `temp` | `chuc` | In ra |
|---|---|---|---|---|---|---|
| 1 | `n = câu trả lời` với `47` | 47 | — | — | — | (chưa in) |
| 2 | `don_vi = (47 mod 10)` | 47 | 7 | — | — | (chưa in) |
| 3 | `temp = n` | 47 | 7 | 47 | — | (chưa in) |
| 4 | `47 >= 10` đúng nên `temp = làm tròn xuống của (47 / 10)` | 47 | 7 | 4 | — | (chưa in) |
| 5 | `4 >= 10` sai, dừng lặp | 47 | 7 | 4 | — | (chưa in) |
| 6 | `chuc = temp`, in `chuc, don_vi` | 47 | 7 | 4 | 4 | `4 7` |

- Kết quả cuối `4 7` trùng kết quả mẫu.

---

## 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1: in ngược thứ tự `nói (don_vi, chuc)`. Với mẫu sẽ ra `7 4`, là kết quả sai vì đề bài yêu cầu chục trước đơn vị sau. Cách sửa: in `nói (chuc, don_vi)`.
```text
n = câu trả lời
don_vi = (n mod 10)
temp = n
while temp >= 10:
    temp = làm tròn xuống của (temp / 10)
chuc = temp
nói (don_vi, chuc)

```
- Bẫy 2: lấy chữ số chục bằng `làm tròn xuống của (n / 10)` mà quên vòng lặp vẫn đúng với 2 chữ số, nhưng nếu viết `chuc = (n mod 10)` nhầm thì cả hai đều là 7. Với mẫu sẽ in `7 7`, là kết quả sai. Cách sửa: chục lấy từ `temp` sau khi gọt, đơn vị lấy từ `(n mod 10)`.
```text
n = câu trả lời
don_vi = (n mod 10)
chuc = (n mod 10)
nói (chuc, don_vi)

```
- Bẫy 3: in mỗi chữ số một dòng bằng hai lệnh `nói (chuc)` rồi `nói (don_vi)`. Với mẫu sẽ in hai dòng `4` và `7`, là kết quả sai vì đề bài yêu cầu cùng một dòng. Cách sửa: in một lần `nói (chuc, don_vi)`.
```text
n = câu trả lời
don_vi = (n mod 10)
temp = n
while temp >= 10:
    temp = làm tròn xuống của (temp / 10)
chuc = temp
nói (chuc)
nói (don_vi)

```

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - hỏi [Nhập n:] và đợi
> - đặt [n] thành (câu trả lời)
> - đặt [don_vi] thành (n mod 10)
> - đặt [temp] thành (n)
> - lặp lại cho đến khi không còn <temp >= 10>:
> -   đặt [temp] thành (temp chia nguyên 10)
> - đặt [chuc] thành (temp)
> - nói (kết hợp chuc và ' ' và don_vi)
