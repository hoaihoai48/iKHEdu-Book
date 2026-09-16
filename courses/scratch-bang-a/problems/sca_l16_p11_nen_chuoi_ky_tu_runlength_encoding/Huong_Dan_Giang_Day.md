# Hướng Dẫn Giảng Dạy: Nén chuỗi ký tự (Run-Length encoding)
Chuyên đề: **Lập Trình Thuật Toán & Khối Lệnh Scratch 3.0**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: giúp bạn Nam ghi hàng ngôi sao thật gọn, mỗi dãy chữ giống nhau liên tiếp thành chữ kèm số lần lặp (ví dụ `AAABBC` thành `A3B2C1`).
- Quy trình với biến thật (`s`, `kq`, `dem`, `i`):
  - Đọc `s = "AAABBCCCC"` (dài 9), khởi động `kq = ''`, `dem = 1`.
  - Duyệt `i` từ 1 đến 8: `A` lặp 3 lần nên ghi `A3`, `B` lặp 2 lần nên ghi `B2`.
  - Sau vòng lặp ghi nốt nhóm cuối `C4`, được `kq = "A3B2C4"` rồi in ra.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: AAABBCCCC)
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `s = câu trả lời` | `s = "AAABBCCCC"` | 3 nhóm A, B, C |
| 2 | `i = 1, 2` giống trước | `dem` tăng tới 3 | nhóm A |
| 3 | `i = 3` khác trước | `kq = "A3"`, `dem = 1` | chốt nhóm A |
| 4 | `i = 4, 5...` | `kq = "A3B2"` rồi chốt `C4` | nhóm B dài 2, C dài 4 |
| 5 | `nói (kq)` | màn hình hiện `A3B2C4` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: quên ghi nhóm cuối sau vòng lặp. Đoạn sai:
```text
s = câu trả lời
kq = ''
dem = 1
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        dem = dem + 1
    else:
        kq = kq + s[i - 1] + str(dem)
        dem = 1
print(kq)
```
Với mẫu `AAABBCCCC` chỉ in ra `A3B2`, mất nhóm `C4`, đáp án đúng là `A3B2C4`. Cách sửa: thêm dòng chốt `kq = kq + s[-1] + str(dem)` trước khi in.
- Bẫy 2: không đặt lại `dem = 1` khi sang nhóm mới. Đoạn sai khiến nhóm `B` bị ghi `B3` và nhóm `C` bị ghi `C7`, với mẫu in ra `A3B3C7`, đáp án đúng là `A3B2C4`. Cách sửa: sau khi chốt nhóm cũ phải cho `dem = 1`.

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - hỏi [Nhập s:] và đợi
> - đặt [s] thành (câu trả lời)
> - đặt [xau] thành (câu trả lời)
> - đặt [do_dai] thành (độ dài của xau)
> - đặt [i] thành (1)
> - lặp lại (do_dai) lần:
> -   nói (ký tự thứ i của xau) trong (1) giây
> -   thay đổi [i] một lượng (1)
