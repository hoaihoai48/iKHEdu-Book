# Hướng Dẫn Giảng Dạy: Tìm ước số của N
Chuyên đề: **Lập Trình Thuật Toán & Khối Lệnh Scratch 3.0**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: ước của N là những số `i` mà `N % i == 0`. Duyệt `i` từ 1 tới N theo thứ tự tăng dần nên kết quả đã đúng thứ tự, không cần sắp xếp.
- Quy trình trong lời giải: đọc `n`, cờ `first` đánh dấu số đầu tiên để in dấu cách cho đẹp; gặp ước thì nếu không phải số đầu in `' '` trước rồi in `i`; cuối cùng xuống dòng.
- Xử lý biên: với N nhỏ nhất là 1 thì chỉ in `1`; với N lớn nhất là 10 000 thì duyệt 10 000 lượt, vẫn nhẹ.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 12)
| Giá trị của `i` | `12 % i == 0`? | `first` | Phần in ra |
|---|---|---|---|
| 1 | có (12 % 1 = 0) | True thành False | `1` |
| 2 | có | False | ` 2` |
| 3 | có | False | ` 3` |
| 4 | có | False | ` 4` |
| 5 | không | — | — |
| 6 | có | False | ` 6` |
| 7-11 | không | — | — |
| 12 | có | False | ` 12` |

Một dòng `1 2 3 4 6 12`, khớp với kết quả mẫu.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1 — kiểm tra ngược `i % n == 0`:
```text
n = int(câu trả lời)
for i in range(1, n + 1):
    if i % n == 0:
        print(i, end=' ')
```
Với mẫu `12` chỉ in ra `12` vì chỉ có 12 chia hết cho 12. Cách sửa: điều kiện đúng là `n % i == 0`.
- Bẫy 2 — dấu cách thừa ở cuối:
```text
n = int(câu trả lời)
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=' ')
```
Với mẫu `12` sẽ in `1 2 3 4 6 12 ` dư một dấu cách cuối, chương trình kiểm tra có thể báo kết quả sai. Cách sửa: dùng cờ `first` như lời giải để chỉ chèn cách ở giữa.

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
