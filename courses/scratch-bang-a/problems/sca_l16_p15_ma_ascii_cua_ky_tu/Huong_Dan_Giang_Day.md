# Hướng Dẫn Giảng Dạy: Mã ASCII của ký tự
Chuyên đề: **Lập Trình Thuật Toán & Khối Lệnh Scratch 3.0**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: mỗi ký tự trên máy tính tương ứng với một con số, tra bằng hàm `ord`.
- Quy trình:
  - Đọc ký tự vào biến `ch`. Với số liệu mẫu, sau `câu trả lời.strip()`, `ch = "A"`.
  - Gọi `ord(ch)` được 65 vì chữ `A` in hoa mang mã 65.
  - In 65 ra màn hình.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: A)
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `ch = câu trả lời.strip()` | `ch = "A"` | ký tự mẫu |
| 2 | `ord(ch)` | `65` | mã của chữ A in hoa |
| 3 | `nói (ord(ch))` | màn hình hiện `65` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: dùng `chr` ngược lại. Đoạn sai:
```text
ch = câu trả lời.strip()
print(chr(ch))
```
Với mẫu `A` chương trình báo lỗi vì `chr` cần số chứ không nhận chữ, đáp án đúng là `65`. Cách sửa: dùng `ord(ch)`.
- Bẫy 2: quên `strip()` nên dư khoảng trắng khi nhập kèm cách. Đoạn sai:
```text
ch = câu trả lời
print(ord(ch))
```
Nếu nhập `A` kèm dấu cách ở đầu, máy đọc nhầm dấu cách (mã 32) và in ra `32`, đáp án đúng là `65`. Cách sửa: đọc `ch = câu trả lời.strip()`.

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - hỏi [Nhập ch:] và đợi
> - đặt [ch] thành (câu trả lời)
> - đặt [xau] thành (câu trả lời)
> - đặt [do_dai] thành (độ dài của xau)
> - đặt [i] thành (1)
> - lặp lại (do_dai) lần:
> -   nói (ký tự thứ i của xau) trong (1) giây
> -   thay đổi [i] một lượng (1)
