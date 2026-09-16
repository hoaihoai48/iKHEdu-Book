# Hướng Dẫn Giảng Dạy: Tìm từ dài nhất trong câu
Chuyên đề: **Lập Trình Thuật Toán & Khối Lệnh Scratch 3.0**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: tách câu thành các từ rồi chọn từ có nhiều chữ cái nhất.
- Quy trình:
  - Đọc câu vào biến `s`. Với số liệu mẫu, `s = "Hoc lap trinh rat thu vi"`.
  - Gọi `s.split()` được `['Hoc', 'lap', 'trinh', 'rat', 'thu', 'vi']` với độ dài 3, 3, 5, 3, 3, 2.
  - Dùng `max(words, key=len)` chọn `trinh` (dài 5, dài nhất, xuất hiện đầu tiên trong các từ dài nhất) rồi in ra.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: Hoc lap trinh rat thu vi)
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `s = câu trả lời` | `s = "Hoc lap trinh rat thu vi"` | 6 từ |
| 2 | `words = s.split()` | 6 từ, dài nhất là `trinh` (5 chữ) | `max` theo `len` |
| 3 | `nói (longest)` | màn hình hiện `trinh` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: dùng `max(words)` so theo vần chữ cái. Đoạn sai:
```text
s = câu trả lời
words = s.split()
print(max(words))
```
Với mẫu trên in ra `vi` (lớn nhất theo thứ tự chữ), đáp án đúng là `trinh`. Cách sửa: thêm tiêu chí `max(words, key=len)`.
- Bẫy 2: in độ dài thay vì từ `nói (len(longest))`. Đoạn sai:
```text
s = câu trả lời
words = s.split()
longest = max(words, key=len)
print(len(longest))
```
Với mẫu trên in ra `5`, đáp án đúng là `trinh`. Cách sửa: in trực tiếp `nói (longest)`.

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
