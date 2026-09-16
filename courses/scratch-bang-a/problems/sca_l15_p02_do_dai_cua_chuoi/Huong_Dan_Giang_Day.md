# Hướng Dẫn Giảng Dạy: Độ dài của chuỗi
Chuyên đề: **Lập Trình Thuật Toán & Khối Lệnh Scratch 3.0**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: cần đếm xem chuỗi `s` có bao nhiêu ký tự, kể cả dấu cách.
- Quy trình:
  - Đọc cả dòng vào biến `s` bằng `câu trả lời`. Với số liệu mẫu, `s = "Python"`.
  - Gọi `len(s)` để lấy độ dài. Chuỗi `"Python"` gồm 6 chữ cái P, y, t, h, o, n nên `len(s)` bằng 6.
  - In 6 ra màn hình bằng `nói (len(s))`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: Python)
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `s = câu trả lời` | `s = "Python"` | đọc đúng dòng mẫu |
| 2 | `len(s)` | `6` | đếm P, y, t, h, o, n |
| 3 | `nói (len(s))` | màn hình hiện `6` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: chỉ gọi `len(s)` mà quên `print`. Đoạn sai:
```text
s = câu trả lời
len(s)
```
Với mẫu `Python`, màn hình không in gì cả, trong khi đáp án đúng phải là `6`. Cách sửa: bọc lệnh in `nói (len(s))`.
- Bẫy 2: tách từ bằng `s = câu trả lời.split()` rồi đo `len(s)`. Đoạn sai:
```text
s = câu trả lời.split()
print(len(s))
```
Với mẫu `Python` vẫn ra `6` do nhầm thành độ dài danh sách 1 từ, còn câu có dấu cách như `a b` sẽ ra `2` thay vì `3`. Cách sửa: giữ nguyên `s = câu trả lời` rồi dùng `len(s)`.

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
