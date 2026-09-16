# Hướng Dẫn Giảng Dạy: Thưởng đọc sách
Chuyên đề: **Lập Trình Thuật Toán & Khối Lệnh Scratch 3.0**

---

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là tính tổng các số từ quyển 1 đến quyển `N`, tức là tổng `1 + 2 + ... + N`.
- Với số mẫu `N = 5`, tổng sao là `1 + 2 + 3 + 4 + 5 = 15`.
- Quy trình trong lời giải với biến `n`:
  - Đọc `n` từ bàn phím, mẫu đọc được `n = 5`.
  - Áp dụng công thức ghép cặp: `n * (n + 1) // 2`, với mẫu là `5 * 6 // 2 = 30 // 2 = 15`.
  - In ra `15`.
- Giá trị biên cụ thể: `N = 1` thì đáp án là `1`; `N = 10^12` thì đáp án là `500000000000500000000000`, Python tính trực tiếp phép nhân số nguyên lớn nên không lo tràn số, cũng không cần cộng từng quyển một.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5)

| Bước | Thao tác | Giá trị |
|------|----------|---------|
| 1 | Đọc `n = int(câu trả lời)` | `n = 5` |
| 2 | Tính `n + 1` | `6` |
| 3 | Tính `n * (n + 1)` | `5 * 6 = 30` |
| 4 | Chia nguyên `30 // 2` | `15` |
| 5 | In kết quả | màn hình hiện `15` |

Kết quả cuối cùng khớp với đáp án mẫu: `15`.

---

## 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — cộng từng quyển bằng vòng lặp tới `N = 10^12`:
```text
n = int(câu trả lời)
tong = 0
for i in range(1, n + 1):
    tong = tong + i
print(tong)
```
Với mẫu `5` vẫn ra `15` nhưng với `N` lớn tới `10^12` vòng lặp chạy gần như không bao giờ xong. Cách sửa: dùng công thức `nói (n * (n + 1) // 2)`.
- Bẫy 2 — dùng phép chia `/` thay vì chia nguyên `//`:
```text
n = int(câu trả lời)
print(n * (n + 1) / 2)
```
Với mẫu `5` in ra `15.0` có dấu chấm, không khớp đáp án mẫu `15`. Cách sửa: dùng `//` để ra số nguyên `15`.
- Bẫy 3 — quên đổi kiểu khi đọc:
```text
n = câu trả lời
print(n * (n + 1) // 2)
```
Với mẫu `5`, `n` là chuỗi nên `n + 1` gây lỗi chương trình. Cách sửa: đọc bằng `n = int(câu trả lời)`.

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - hỏi [Nhập n:] và đợi
> - đặt [n] thành (câu trả lời)
> - xóa tất cả của [danh_sach]
> - đặt [i] thành (1)
> - lặp lại (n) lần:
> -   hỏi [Nhập phần tử:] và đợi
> -   thêm (câu trả lời) vào [danh_sach]
> -   thay đổi [i] một lượng (1)
> - nói (phần tử thứ 1 của [danh_sach])
