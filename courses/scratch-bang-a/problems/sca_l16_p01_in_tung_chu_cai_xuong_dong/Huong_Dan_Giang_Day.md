# Hướng Dẫn Giảng Dạy: In từng chữ cái xuống dòng
Chuyên đề: **Lập Trình Thuật Toán & Khối Lệnh Scratch 3.0**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: đi thăm từng chữ cái trong từ `s`, mỗi chữ nằm một dòng riêng.
- Quy trình:
  - Đọc từ vào biến `s`. Với số liệu mẫu, `s = "CAT"`.
  - Lặp `for ch in s`: lượt 1 `ch = "C"`, lượt 2 `ch = "A"`, lượt 3 `ch = "T"`.
  - Mỗi lượt `nói (ch)` xuống dòng một lần nên được 3 dòng `C`, `A`, `T`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: CAT)
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `s = câu trả lời` | `s = "CAT"` | 3 chữ cái |
| 2 | lượt 1 `ch = "C"` | in dòng 1 `C` | chữ đầu |
| 3 | lượt 2 `ch = "A"` | in dòng 2 `A` | chữ giữa |
| 4 | lượt 3 `ch = "T"` | in dòng 3 `T` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: in cả từ một lần `nói (s)`. Đoạn sai:
```text
s = câu trả lời
print(s)
```
Với mẫu `CAT` chỉ in một dòng `CAT`, đáp án đúng là 3 dòng `C`, `A`, `T`. Cách sửa: dùng vòng lặp `for ch in s: print(ch)`.
- Bẫy 2: in các chữ trên cùng một dòng bằng `end`. Đoạn sai:
```text
s = câu trả lời
for ch in s:
    print(ch, end='')
```
Với mẫu `CAT` in ra `CAT` trên một dòng, đáp án đúng là mỗi chữ một dòng. Cách sửa: để `nói (ch)` xuống dòng tự nhiên.

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
