# Hướng Dẫn Giảng Dạy: Cắt đôi chuỗi ký tự
Chuyên đề: **Lập Trình Thuật Toán & Khối Lệnh Scratch 3.0**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: chuỗi có độ dài chẵn nên chia đều thành 2 nửa.
- Quy trình:
  - Đọc chuỗi vào `s`. Với số liệu mẫu, `s = "PYTHON"` dài 6 ký tự.
  - Tính điểm giữa `n = len(s) // 2` được 3.
  - In nửa đầu `s[:3]` là `PYT` trên dòng 1, nửa sau `s[3:]` là `HON` trên dòng 2.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: PYTHON)
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `s = câu trả lời` | `s = "PYTHON"` | dài 6, chẵn |
| 2 | `n = len(s) // 2` | `n = 3` | điểm giữa |
| 3 | `nói (s[:n])` | dòng 1 hiện `PYT` | nửa đầu |
| 4 | `nói (s[n:])` | dòng 2 hiện `HON` | nửa sau, khớp mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: chia bằng `/` ra số thực 3.0. Đoạn sai:
```text
s = câu trả lời
n = len(s) / 2
print(s[:n])
print(s[n:])
```
Với mẫu `PYTHON` chương trình báo lỗi vì không cắt chuỗi bằng số thực, đáp án đúng là hai dòng `PYT` và `HON`. Cách sửa: dùng chia nguyên `n = len(s) // 2`.
- Bẫy 2: in cả hai nửa trên cùng một dòng. Đoạn sai:
```text
s = câu trả lời
n = len(s) // 2
print(s[:n] + s[n:])
```
Với mẫu `PYTHON` in ra `PYTHON` trên một dòng, đáp án đúng là `PYT` và `HON` trên hai dòng. Cách sửa: dùng hai khối lệnh `nói` riêng.

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
