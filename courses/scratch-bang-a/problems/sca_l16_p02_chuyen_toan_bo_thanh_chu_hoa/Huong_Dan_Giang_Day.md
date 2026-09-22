# Hướng Dẫn Giảng Dạy

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: biến mọi chữ cái trong chuỗi `s` thành chữ in hoa.
- Quy trình:
  - Đọc cả dòng vào biến `s`. Với số liệu mẫu, `s = "ikhedu vietnam"`.
  - Gọi `s.upper()` để đổi toàn bộ chữ thường thành chữ hoa, dấu cách giữ nguyên.
  - In ra `IKHEDU VIETNAM` bằng `nói (s.upper())`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: ikhedu vietnam)
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `s = câu trả lời` | `s = "ikhedu vietnam"` | 14 ký tự cả dấu cách |
| 2 | `s.upper()` | `"IKHEDU VIETNAM"` | từng chữ đều hóa in hoa |
| 3 | `nói (s.upper())` | màn hình hiện `IKHEDU VIETNAM` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: gọi `s.upper()` mà quên `print`. Đoạn sai:
```text
s = câu trả lời
s.upper()

```
Với mẫu `ikhedu vietnam`, màn hình không in gì cả, đáp án đúng là `IKHEDU VIETNAM`. Cách sửa: bọc lệnh in `nói (s.upper())`.
- Bẫy 2: dùng `s.lower()` ngược yêu cầu. Đoạn sai:
```text
s = câu trả lời
nói (s.lower())

```
Với mẫu trên vẫn in ra `ikhedu vietnam` chữ thường, đáp án đúng là `IKHEDU VIETNAM`. Cách sửa: dùng `s.upper()`.

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - hỏi [Nhập s:] và đợi
> - đặt [s] thành (câu trả lời)
> - nói (giá trị)
