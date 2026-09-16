# Hướng Dẫn Giảng Dạy: Đếm ngược phóng tên lửa
Chuyên đề: **Lập Trình Thuật Toán & Khối Lệnh Scratch 3.0**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: đếm ngược từ N về 1, mỗi số một dòng, rồi dòng cuối in chữ `PHONG!`. Dùng `range(n, 0, -1)` để bước nhảy là trừ 1 và dừng trước 0.
- Quy trình trong lời giải: đọc `n`, vòng lặp cho `i` chạy 3, 2, 1 và `nói (i)` từng dòng, sau vòng lặp in thêm `nói ("PHONG!")`.
- Xử lý biên: với N nhỏ nhất là 1 thì chỉ in `1` rồi `PHONG!`; với N lớn nhất là 20 thì in đủ 20 dòng số cộng dòng `PHONG!`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 3)
| Lượt lặp | Giá trị của `i` | Dòng in ra |
|---|---|---|
| 1 | 3 | 3 |
| 2 | 2 | 2 |
| 3 | 1 | 1 |
| sau lặp | — | PHONG! |

Kết quả cuối cùng là 4 dòng `3 / 2 / 1 / PHONG!`, khớp với kết quả mẫu.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1 — dùng `range(n, 1, -1)`:
```text
n = int(câu trả lời)
for i in range(n, 1, -1):
    print(i)
print("PHONG!")
```
Với mẫu `3` chỉ in `3 / 2 / PHONG!`, thiếu mất số `1`. Cách sửa: điểm dừng là `0`, tức `range(n, 0, -1)`.
- Bẫy 2 — quên dòng `PHONG!` hoặc viết sai chữ hoa:
```text
n = int(câu trả lời)
for i in range(n, 0, -1):
    print(i)
```
Với mẫu `3` chỉ in `3 / 2 / 1`, thiếu dòng cuối nên chương trình kiểm tra báo kết quả sai. Cách sửa: thêm `nói ("PHONG!")` sau vòng lặp.

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
