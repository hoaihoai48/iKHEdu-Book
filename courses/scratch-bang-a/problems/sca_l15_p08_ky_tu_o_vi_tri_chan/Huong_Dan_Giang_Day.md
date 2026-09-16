# Hướng Dẫn Giảng Dạy: Ký tự Ở vị trí chẵn
Chuyên đề: **Lập Trình Thuật Toán & Khối Lệnh Scratch 3.0**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: giữ lại các ký tự nằm ở vị trí 0, 2, 4, 6... của chuỗi `s` (đếm từ 0).
- Quy trình:
  - Đọc chuỗi vào biến `s`. Với số liệu mẫu, `s = "ABCDEF"`.
  - Dùng lát cắt bước nhảy 2 là `s[::2]` để nhặt vị trí 0 (`A`), 2 (`C`), 4 (`E`).
  - In ra `ACE` bằng `nói (s[::2])`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: ABCDEF)
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `s = câu trả lời` | `s = "ABCDEF"` | vị trí 0 là A ... 5 là F |
| 2 | `s[::2]` | `"ACE"` | nhặt A (0), C (2), E (4) |
| 3 | `nói (s[::2])` | màn hình hiện `ACE` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: nhầm đếm từ 1 nên lấy vị trí lẻ, viết `s[1::2]`. Đoạn sai:
```text
s = câu trả lời
print(s[1::2])
```
Với mẫu `ABCDEF` in ra `BDF`, đáp án đúng là `ACE`. Cách sửa: bắt đầu từ 0 với `s[::2]`.
- Bẫy 2: dùng vòng lặp từ 1 và cộng chuỗi sai. Đoạn sai:
```text
s = câu trả lời
kq = ''
for i in range(1, len(s), 2):
    kq = kq + s[i]
print(kq)
```
Với mẫu `ABCDEF` in ra `BDF`, đáp án đúng là `ACE`. Cách sửa: cho vòng lặp chạy từ 0 `range(0, len(s), 2)` hoặc dùng `s[::2]`.

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
