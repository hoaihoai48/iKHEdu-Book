# Hướng Dẫn Giảng Dạy: Tổng bình phương
Chuyên đề: **Lập Trình Thuật Toán & Khối Lệnh Scratch 3.0**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: tổng `S = 1^2 + 2^2 + ... + N^2`. Mỗi bước cộng thêm bình phương `i * i` của số hiện tại vào biến `s`.
- Quy trình trong lời giải: đọc `n`, đặt `s = 0`, vòng lặp cho `i` chạy 1 tới `n`, mỗi lượt `s = s + i * i`, cuối cùng in `s`.
- Xử lý biên: với N nhỏ nhất là 1 thì `s = 1`; với N lớn nhất là 1000 thì tổng là `1000 * 1001 * 2001 // 6 = 333833500`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 3)
| Lượt lặp | Giá trị của `i` | Cộng thêm `i * i` | Giá trị mới của `s` |
|---|---|---|---|
| đầu | — | `s = 0` | 0 |
| 1 | 1 | 1 | 1 |
| 2 | 2 | 4 | 5 |
| 3 | 3 | 9 | 14 |

In ra `14` (vì `1 + 4 + 9 = 14`), khớp với kết quả mẫu.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1 — cộng `i` thay vì `i * i`:
```text
n = int(câu trả lời)
s = 0
for i in range(1, n + 1):
    s = s + i
print(s)
```
Với mẫu `3` sẽ in ra `6` thay vì `14`. Cách sửa: cộng `s = s + i * i`.
- Bẫy 2 — dùng `i ** 2` nhưng đặt trong `print` mỗi lượt:
```text
n = int(câu trả lời)
s = 0
for i in range(1, n + 1):
    s = s + i * i
    print(s)
```
Với mẫu `3` sẽ in 3 dòng `1 / 5 / 14` thay vì chỉ một dòng `14`. Cách sửa: để `nói (s)` ngoài vòng lặp, không thụt đầu dòng.

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
