# Hướng Dẫn Giảng Dạy: Đảo ngược tên riêng
Chuyên đề: **Lập Trình Thuật Toán & Khối Lệnh Scratch 3.0**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: đọc ngược toàn bộ chuỗi `s` để tạo biệt danh bí mật.
- Quy trình:
  - Đọc chuỗi vào biến `s`. Với số liệu mẫu, `s = "DORAEMON"` (độ dài 8).
  - Dùng lát cắt bước nhảy âm `s[::-1]` để lật ngược thứ tự ký tự.
  - In ra `NOMEAROD` bằng `nói (s[::-1])`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: DORAEMON)
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `s = câu trả lời` | `s = "DORAEMON"` | D-O-R-A-E-M-O-N |
| 2 | `s[::-1]` | `"NOMEAROD"` | đọc ngược từng chữ cái |
| 3 | `nói (s[::-1])` | màn hình hiện `NOMEAROD` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: quên dấu trừ, viết `s[::1]`. Đoạn sai:
```text
s = câu trả lời
print(s[::1])
```
Với mẫu `DORAEMON` in ra nguyên `DORAEMON`, đáp án đúng là `NOMEAROD`. Cách sửa: viết đủ `s[::-1]`.
- Bẫy 2: dùng `reversed(s)` rồi in trực tiếp. Đoạn sai:
```text
s = câu trả lời
print(reversed(s))
```
Với mẫu `DORAEMON` màn hình hiện dòng mô tả vật lạ thay vì `NOMEAROD`. Cách sửa: dùng `nói (s[::-1])`.

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
