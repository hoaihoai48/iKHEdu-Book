# Hướng Dẫn Giảng Dạy: Đếm số từ trong câu
Chuyên đề: **Lập Trình Thuật Toán & Khối Lệnh Scratch 3.0**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: từ là các cụm chữ cách nhau bởi dấu cách; `split()` tự bỏ hết cách thừa.
- Quy trình:
  - Đọc cả dòng vào biến `s`. Với số liệu mẫu, `s = "  Chuc mung nam moi "` (dư cách đầu và cuối).
  - Gọi `s.split()` được danh sách 4 từ `['Chuc', 'mung', 'nam', 'moi']`.
  - In `len(words)` được 4.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: Chuc mung nam moi (thừa cách hai đầu))
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `s = câu trả lời` | `s = "  Chuc mung nam moi "` | dư cách hai đầu |
| 2 | `words = s.split()` | `['Chuc', 'mung', 'nam', 'moi']` | cách thừa tự biến mất |
| 3 | `nói (len(words))` | màn hình hiện `4` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: đếm dấu cách cộng 1 nên sai khi dư cách. Đoạn sai:
```text
s = câu trả lời
print(s.count(' ') + 1)
```
Với mẫu `  Chuc mung nam moi ` có 6 dấu cách nên in ra `7`, đáp án đúng là `4`. Cách sửa: dùng `len(s.split())`.
- Bẫy 2: tách bằng `s.split(' ')` giữ lại chuỗi rỗng. Đoạn sai:
```text
s = câu trả lời
words = s.split(' ')
print(len(words))
```
Với mẫu trên danh sách lẫn chuỗi rỗng nên in ra số lớn hơn `4`. Cách sửa: dùng `s.split()` không truyền gì.

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
