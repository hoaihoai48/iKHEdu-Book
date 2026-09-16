# Hướng Dẫn Giảng Dạy: Tổng các số tự nhiên
Chuyên đề: **Lập Trình Thuật Toán & Khối Lệnh Scratch 3.0**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: tổng 1 + 2 + ... + N. Với N tới 100 000, lời giải dùng công thức `n * (n + 1) // 2` tính thẳng một phép, giống mẹo ghép cặp của Gauss.
- Quy trình trong lời giải: đọc `n`, tính `n * (n + 1) // 2` rồi `print`. Dấu `//` giữ kết quả là số nguyên.
- Xử lý biên: với N nhỏ nhất là 1 thì `1 * 2 // 2 = 1`; với N lớn nhất là 100 000 thì `100000 * 100001 // 2 = 5000050000`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 4)
| Lượt | Giá trị của `n` | Biểu thức tính | Kết quả in ra |
|---|---|---|---|
| 1 | 4 | 4 * 5 // 2 | 10 |

Kết quả `10` chính là `1 + 2 + 3 + 4`, khớp với kết quả mẫu.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1 — dùng chia `/`:
```text
n = int(câu trả lời.strip())
print(n * (n + 1) / 2)
```
Với mẫu `4` sẽ in ra `10.0` thay vì `10`, cho kết quả sai định dạng. Cách sửa: dùng `//`.
- Bẫy 2 — cộng dồn nhưng quên khởi tạo:
```text
n = int(câu trả lời.strip())
for i in range(1, n + 1):
    s = s + i
print(s)
```
Chương trình báo lỗi vì biến `s` chưa được gán `0` trước vòng lặp. Cách sửa: thêm `s = 0` trước vòng lặp, hoặc dùng thẳng công thức như lời giải.

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - hỏi [Nhập n:] và đợi
> - đặt [n] thành (câu trả lời)
> - đặt [tong] thành (0)
> - đặt [i] thành (1)
> - lặp lại (n) lần:
> -   thay đổi [tong] một lượng (i)
> -   thay đổi [i] một lượng (1)
> - nói (tong)
