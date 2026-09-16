# Hướng Dẫn Giảng Dạy: Ký tự đầu & ký tự cuối
Chuyên đề: **Lập Trình Thuật Toán & Khối Lệnh Scratch 3.0**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: lấy chữ cái đầu tiên và chữ cái cuối cùng của chuỗi `s`, nối bằng một dấu cách.
- Quy trình:
  - Đọc chuỗi vào biến `s`. Với số liệu mẫu, `s = "PYTHON"`.
  - Lấy ký tự đầu `s[0]` được `P`, ký tự cuối `s[-1]` được `N`.
  - Nối thành `P + ' ' + N` rồi in ra `P N`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: PYTHON)
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `s = câu trả lời` | `s = "PYTHON"` | đầu là P, cuối là N |
| 2 | `s[0] + ' ' + s[-1]` | `"P N"` | có đúng một dấu cách |
| 3 | `nói (...)` | màn hình hiện `P N` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: nối trực tiếp không có dấu cách. Đoạn sai:
```text
s = câu trả lời
print(s[0] + s[-1])
```
Với mẫu `PYTHON` in ra `PN` dính nhau, đáp án đúng là `P N`. Cách sửa: chèn `' '` ở giữa.
- Bẫy 2: lấy ký tự cuối bằng `s[len(s)]`. Đoạn sai:
```text
s = câu trả lời
print(s[0] + ' ' + s[len(s)])
```
Với mẫu `PYTHON`, `len(s)` bằng 6 vượt quá vị trí cuối (5) nên chương trình báo lỗi và không in gì, đáp án đúng là `P N`. Cách sửa: dùng `s[-1]` hoặc `s[len(s) - 1]`.

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
