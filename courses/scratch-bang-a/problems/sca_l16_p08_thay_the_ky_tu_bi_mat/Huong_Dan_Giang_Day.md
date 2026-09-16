# Hướng Dẫn Giảng Dạy: Thay thế ký tự bí mật
Chuyên đề: **Lập Trình Thuật Toán & Khối Lệnh Scratch 3.0**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: thay mọi dấu cách trong chuỗi `s` thành dấu gạch dưới `_`.
- Quy trình:
  - Đọc cả dòng vào biến `s`. Với số liệu mẫu, `s = "hoc lap trinh de vui"` (4 dấu cách).
  - Gọi `s.replace(' ', '_')` để đổi từng dấu cách thành `_`.
  - In ra `hoc_lap_trinh_de_vui` bằng `nói (s.replace(' ', '_'))`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: hoc lap trinh de vui)
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `s = câu trả lời` | `s = "hoc lap trinh de vui"` | có 4 dấu cách |
| 2 | `s.replace(' ', '_')` | `"hoc_lap_trinh_de_vui"` | cả 4 dấu cách đều đổi |
| 3 | `nói (...)` | màn hình hiện `hoc_lap_trinh_de_vui` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: đổi ngược chiều `s.replace('_', ' ')`. Đoạn sai:
```text
s = câu trả lời
print(s.replace('_', ' '))
```
Với mẫu `hoc lap trinh de vui` (không có `_`) in ra nguyên văn không đổi, đáp án đúng là `hoc_lap_trinh_de_vui`. Cách sửa: đặt dấu cách trước `s.replace(' ', '_')`.
- Bẫy 2: quên `print`, chỉ gọi thay thế. Đoạn sai:
```text
s = câu trả lời
s.replace(' ', '_')
```
Với mẫu trên màn hình không in gì cả, đáp án đúng là `hoc_lap_trinh_de_vui`. Cách sửa: bọc lệnh in `nói (s.replace(' ', '_'))`.

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
