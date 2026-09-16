# Hướng Dẫn Giảng Dạy: Mật mã thay thế hoán vị (anagram)
Chuyên đề: **Lập Trình Thuật Toán & Khối Lệnh Scratch 3.0**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: hai từ là hoán vị của nhau khi chúng gồm đúng cùng một bộ chữ cái, chỉ khác thứ tự xếp.
- Quy trình:
  - Đọc hai từ vào `s1` và `s2`. Với số liệu mẫu, `s1 = "listen"`, `s2 = "silent"`.
  - Sắp xếp chữ cái hai từ bằng `sorted(...)`: cả hai đều thành `['e', 'i', 'l', 'n', 's', 't']`.
  - Hai danh sách bằng nhau nên in `YES` (ngược lại in `NO`).

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: listen và silent)
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `s1 = câu trả lời.strip()` | `s1 = "listen"` | từ thứ nhất |
| 2 | `s2 = câu trả lời.strip()` | `s2 = "silent"` | từ thứ hai |
| 3 | `sorted(s1)` và `sorted(s2)` | cùng `['e', 'i', 'l', 'n', 's', 't']` | cùng bộ chữ cái |
| 4 | so sánh bằng nhau | đúng nên `nói ("YES")` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: so trực tiếp `s1 == s2` mà không sắp xếp. Đoạn sai:
```text
s1 = câu trả lời.strip()
s2 = câu trả lời.strip()
if s1 == s2:
    print("YES")
else:
    print("NO")
```
Với mẫu `listen` và `silent` in ra `NO`, đáp án đúng là `YES`. Cách sửa: so `sorted(s1) == sorted(s2)`.
- Bẫy 2: so độ dài thay vì so chữ cái. Đoạn sai:
```text
s1 = câu trả lời.strip()
s2 = câu trả lời.strip()
if len(s1) == len(s2):
    print("YES")
else:
    print("NO")
```
Với hai từ dài bằng nhau nhưng khác chữ (ví dụ `abc` và `xyz`) vẫn in `YES` là kết quả sai. Cách sửa: so `sorted(s1) == sorted(s2)`.

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - hỏi [Nhập s1:] và đợi
> - đặt [s1] thành (câu trả lời)
> - đặt [xau] thành (câu trả lời)
> - đặt [do_dai] thành (độ dài của xau)
> - đặt [i] thành (1)
> - lặp lại (do_dai) lần:
> -   nói (ký tự thứ i của xau) trong (1) giây
> -   thay đổi [i] một lượng (1)
