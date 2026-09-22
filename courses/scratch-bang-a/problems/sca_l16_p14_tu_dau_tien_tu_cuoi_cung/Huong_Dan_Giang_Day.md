# Hướng Dẫn Giảng Dạy

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: tách câu thành danh sách từ rồi lấy phần tử đầu và phần tử cuối.
- Quy trình:
  - Đọc câu vào biến `s`. Với số liệu mẫu, `s = "Hoc Python cuc vui"`.
  - Gọi `s.split()` được `['Hoc', 'Python', 'cuc', 'vui']`.
  - In `words[0]` là `Hoc` trên dòng 1, in `words[-1]` là `vui` trên dòng 2.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: Hoc Python cuc vui)
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `s = câu trả lời` | `s = "Hoc Python cuc vui"` | 4 từ |
| 2 | `words = s.split()` | `['Hoc', 'Python', 'cuc', 'vui']` | đầu là Hoc, cuối là vui |
| 3 | `nói (words[0])` | dòng 1 hiện `Hoc` | từ đầu tiên |
| 4 | `nói (words[-1])` | dòng 2 hiện `vui` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: in từ cuối nhầm thành `words[1]`. Đoạn sai:
```text
s = câu trả lời
words = s.split()
nói (words[0])
nói (words[1])

```
Với mẫu trên dòng 2 in ra `Python`, đáp án đúng là `vui`. Cách sửa: dùng `words[-1]` cho từ cuối.
- Bẫy 2: in hai từ trên cùng một dòng. Đoạn sai:
```text
s = câu trả lời
words = s.split()
nói (words[0] + ' ' + words[-1])

```
Với mẫu trên in ra `Hoc vui` trên một dòng, đáp án đúng là hai dòng `Hoc` và `vui`. Cách sửa: dùng hai khối lệnh `nói` riêng.

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - hỏi [Nhập s:] và đợi
> - đặt [s] thành (câu trả lời)
> - nói (giá trị)
> - nói (giá trị)
