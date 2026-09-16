# Hướng Dẫn Giảng Dạy: Viết hoa chữ cái đầu mỗi từ (title case)
Chuyên đề: **Lập Trình Thuật Toán & Khối Lệnh Scratch 3.0**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: chuẩn hóa họ tên sao cho mỗi từ có chữ đầu in hoa, các chữ còn lại in thường.
- Quy trình:
  - Đọc họ tên vào biến `s`. Với số liệu mẫu, `s = "nguyen van an"`.
  - Tách `s.split()` được `['nguyen', 'van', 'an']`, rồi `w.capitalize()` từng từ thành `['Nguyen', 'Van', 'An']`.
  - Nối lại `" ".join(words)` được `Nguyen Van An` rồi in ra.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: nguyen van an)
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `s = câu trả lời` | `s = "nguyen van an"` | 3 từ viết thường |
| 2 | `[w.capitalize() ...]` | `['Nguyen', 'Van', 'An']` | đầu hoa, còn lại thường |
| 3 | `nói (" ".join(words))` | màn hình hiện `Nguyen Van An` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: dùng `upper()` hóa hoa toàn bộ. Đoạn sai:
```text
s = câu trả lời
print(s.upper())
```
Với mẫu `nguyen van an` in ra `NGUYEN VAN AN`, đáp án đúng là `Nguyen Van An`. Cách sửa: dùng `w.capitalize()` cho từng từ.
- Bẫy 2: dùng `title()` trực tiếp mà không tách từ, với họ tên có dấu nháy sẽ lỗi kiểu ít gặp; đoạn minh họa sai thường gặp là quên nối lại:
```text
s = câu trả lời
words = [w.capitalize() for w in s.split()]
print(words)
```
Với mẫu trên in ra `['Nguyen', 'Van', 'An']` kèm ngoặc, đáp án đúng là `Nguyen Van An`. Cách sửa: in `" ".join(words)`.

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
