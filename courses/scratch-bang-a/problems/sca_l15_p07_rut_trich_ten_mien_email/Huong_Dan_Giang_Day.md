# Hướng Dẫn Giảng Dạy: Rút trích tên miền email
Chuyên đề: **Lập Trình Thuật Toán & Khối Lệnh Scratch 3.0**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: phần tên miền là đoạn đứng sau ký tự `@` trong chuỗi `s`.
- Quy trình:
  - Đọc địa chỉ vào biến `s`. Với số liệu mẫu, `s = "hocsinh@ikhedu.vn"`, ký tự `@` nằm ở vị trí 7.
  - Tìm vị trí `@` bằng `s.index('@')` được 7, cộng 1 thành 8 là điểm bắt đầu của tên miền.
  - Cắt `s[8:]` được `ikhedu.vn` rồi in ra.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: hocsinh@ikhedu.vn)
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `s = câu trả lời` | `s = "hocsinh@ikhedu.vn"` | `@` ở vị trí 7 |
| 2 | `s.index('@') + 1` | `8` | điểm bắt đầu tên miền |
| 3 | `s[8:]` rồi in | màn hình hiện `ikhedu.vn` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: quên cộng 1 nên lấy dính cả `@`. Đoạn sai:
```text
s = câu trả lời
print(s[s.index('@'):])
```
Với mẫu `hocsinh@ikhedu.vn` in ra `@ikhedu.vn`, đáp án đúng là `ikhedu.vn`. Cách sửa: cộng 1 `s[s.index('@') + 1:]`.
- Bẫy 2: tách rồi lấy nhầm nửa đầu `s.split('@')[0]`. Đoạn sai:
```text
s = câu trả lời
print(s.split('@')[0])
```
Với mẫu `hocsinh@ikhedu.vn` in ra `hocsinh`, đáp án đúng là `ikhedu.vn`. Cách sửa: lấy nửa sau `s.split('@')[1]`.

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
