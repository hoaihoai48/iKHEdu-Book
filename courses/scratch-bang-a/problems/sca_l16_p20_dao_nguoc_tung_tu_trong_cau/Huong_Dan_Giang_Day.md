# Hướng Dẫn Giảng Dạy

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: lật ngược chữ cái bên trong từng từ, nhưng thứ tự các từ trong câu giữ nguyên.
- Quy trình:
  - Đọc câu vào biến `s`. Với số liệu mẫu, `s = "Toi yeu Viet Nam"`.
  - Tách `s.split()` được `['Toi', 'yeu', 'Viet', 'Nam']`, lật từng từ `w[::-1]` thành `['ioT', 'uey', 'teiV', 'maN']`.
  - Nối lại được `ioT uey teiV maN` rồi in ra.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: Toi yeu Viet Nam)
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `s = câu trả lời` | `s = "Toi yeu Viet Nam"` | 4 từ |
| 2 | `[w[::-1] ...]` | `['ioT', 'uey', 'teiV', 'maN']` | từng từ bị lật |
| 3 | `nói (" ".join(words))` | màn hình hiện `ioT uey teiV maN` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: lật cả câu `s[::-1]` nên thứ tự từ cũng đảo. Đoạn sai:
```text
s = câu trả lời
nói (s[::-1])

```
Với mẫu trên in ra `maN teiV uey ioT`, đáp án đúng là `ioT uey teiV maN`. Cách sửa: lật từng từ rồi mới nối lại.
- Bẫy 2: tách từ nhưng quên nối, in danh sách. Đoạn sai:
```text
s = câu trả lời
words = [w[::-1] for w in s.split()]
nói (words)

```
Với mẫu trên in ra `['ioT', 'uey', 'teiV', 'maN']` kèm ngoặc, đáp án đúng là `ioT uey teiV maN`. Cách sửa: in `" ".join(words)`.

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - hỏi [Nhập s:] và đợi
> - đặt [s] thành (câu trả lời)
> - đặt [words] thành (giá trị)
> - nói (words)
