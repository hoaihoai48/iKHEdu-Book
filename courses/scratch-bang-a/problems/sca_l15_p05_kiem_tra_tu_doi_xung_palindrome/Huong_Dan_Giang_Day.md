# Hướng Dẫn Giảng Dạy: Kiểm tra từ đối xứng (palindrome)
Chuyên đề: **Lập Trình Thuật Toán & Khối Lệnh Scratch 3.0**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: từ đối xứng là từ đọc xuôi và đọc ngược giống hệt nhau, như soi gương.
- Quy trình:
  - Đọc từ vào biến `s`. Với số liệu mẫu, `s = "RADAR"`.
  - Lật ngược từ bằng `s[::-1]` được `RADAR`.
  - So sánh `s == s[::-1]`: đúng thì in `YES`, sai thì in `NO`. Với mẫu, hai vế bằng nhau nên in `YES`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: RADAR)
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `s = câu trả lời` | `s = "RADAR"` | từ mẫu |
| 2 | `s[::-1]` | `"RADAR"` | đọc ngược vẫn y nguyên |
| 3 | `s == s[::-1]` | đúng | nên in nhánh YES |
| 4 | `nói ('YES')` | màn hình hiện `YES` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: in chữ thường `yes` hoặc `Yes`. Đoạn sai:
```text
s = câu trả lời
if s == s[::-1]:
    print('Yes')
else:
    print('No')
```
Với mẫu `RADAR` in ra `Yes`, chương trình kiểm tra so khớp từng chữ nên cho kết quả sai, đáp án đúng là `YES`. Cách sửa: in hoa toàn bộ `YES` và `NO`.
- Bẫy 2: so sánh sai `if s == s[::-1]:` viết nhầm thành gán một dấu bằng. Đoạn sai:
```text
s = câu trả lời
if s = s[::-1]:
    print('YES')
else:
    print('NO')
```
Chương trình báo lỗi ngay và không in gì, đáp án đúng là `YES`. Cách sửa: dùng hai dấu bằng `==` để so sánh.

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
