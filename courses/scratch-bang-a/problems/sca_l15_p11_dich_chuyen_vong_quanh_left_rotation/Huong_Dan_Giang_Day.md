# Hướng Dẫn Giảng Dạy: Dịch chuyển vòng quanh (left rotation)
Chuyên đề: **Lập Trình Thuật Toán & Khối Lệnh Scratch 3.0**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: trò tàu lửa nhấc `K` toa đầu đem gắn ra cuối đoàn.
- Quy trình:
  - Đọc chuỗi vào `s` và số vào `k`. Với số liệu mẫu, `s = "ABCDE"`, `k = 2`.
  - Phần còn lại `s[k:]` là `CDE`, phần đem gắn `s[:k]` là `AB`.
  - Nối `CDE + AB` thành `CDEAB` rồi in ra.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: ABCDE và 2)
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `s = câu trả lời` | `s = "ABCDE"` | đoàn tàu 5 toa |
| 2 | `k = int(câu trả lời)` | `k = 2` | nhấc 2 toa đầu |
| 3 | `s[k:] + s[:k]` | `"CDE" + "AB" = "CDEAB"` | gắn AB ra cuối |
| 4 | `nói (...)` | màn hình hiện `CDEAB` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: nối ngược thứ tự `s[:k] + s[k:]`. Đoạn sai:
```text
s = câu trả lời
k = int(câu trả lời)
print(s[:k] + s[k:])
```
Với mẫu `ABCDE` và `2` in ra nguyên `ABCDE`, đáp án đúng là `CDEAB`. Cách sửa: đặt `s[k:]` trước, `s[:k]` sau.
- Bẫy 2: quên đổi `k` sang số nên `s[k:]` báo lỗi. Đoạn sai:
```text
s = câu trả lời
k = câu trả lời
print(s[k:] + s[:k])
```
Với mẫu trên chương trình báo lỗi vì không cắt chuỗi bằng chữ được, đáp án đúng là `CDEAB`. Cách sửa: đọc `k = int(câu trả lời)`.

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - hỏi [Nhập k:] và đợi
> - đặt [k] thành (câu trả lời)
> - đặt [xau] thành (câu trả lời)
> - đặt [do_dai] thành (độ dài của xau)
> - đặt [i] thành (1)
> - lặp lại (do_dai) lần:
> -   nói (ký tự thứ i của xau) trong (1) giây
> -   thay đổi [i] một lượng (1)
