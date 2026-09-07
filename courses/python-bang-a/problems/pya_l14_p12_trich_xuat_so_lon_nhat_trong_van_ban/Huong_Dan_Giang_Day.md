# Hướng Dẫn Giảng Dạy: Trích xuất số lớn nhất trong văn bản
Chuyên đề: **Duyệt Chuỗi & Biến Đổi Ký Tự Thần Kỳ**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: giúp lớp trưởng gom từng cụm chữ số liên tiếp thành con số rồi giữ lại số to nhất.
- Quy trình với biến thật (`s`, `lon_nhat`, `so_hien_tai`, `ch`):
  - Đọc cả câu mẫu, khởi động `lon_nhat = -1`, `so_hien_tai = ''`.
  - Duyệt từng `ch` (kèm một dấu cách giả ở cuối để chốt số): gom được `5` (lớn nhất thành 5), `38` (thành 38), `105` (thành 105).
  - In `lon_nhat` được 105.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: Lop 5A co 38 hoc sinh va 105 quyen sach)
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `s = input()` | câu báo cáo của lớp trưởng | chứa 5, 38, 105 |
| 2 | gom tới hết `5A` | `lon_nhat = 5` | số đầu tiên |
| 3 | gom tới hết `38` | `lon_nhat = 38` | 38 lớn hơn 5 |
| 4 | gom tới hết `105` | `lon_nhat = 105` | 105 lớn nhất |
| 5 | `print(lon_nhat)` | màn hình hiện `105` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: so chuỗi thay vì so số nên `38` thắng `105`. Đoạn sai:
```python
s = input()
lon_nhat = ''
so_hien_tai = ''
for ch in s + ' ':
    if ch.isdigit():
        so_hien_tai = so_hien_tai + ch
    else:
        if so_hien_tai != '':
            if so_hien_tai > lon_nhat:
                lon_nhat = so_hien_tai
            so_hien_tai = ''
print(lon_nhat)
```
Với mẫu trên so theo vần chữ nên `38` lớn hơn `105`, in ra `38`, đáp án đúng là `105`. Cách sửa: đổi sang số `int(so_hien_tai) > lon_nhat`.
- Bẫy 2: quên dấu cách giả cuối `for ch in s:` nên số cuối mất tích. Đoạn sai khiến với câu kết thúc bằng số (như mẫu kết thúc bằng `sach` thì không sao, nhưng câu `co 105` sẽ chốt thiếu) dễ cho kết quả sai. Cách sửa: duyệt `for ch in s + ' ':` như lời giải.

---

## 4. Lời giải tham khảo
```python
s = input()
lon_nhat = -1
so_hien_tai = ''
for ch in s + ' ':
    if ch.isdigit():
        so_hien_tai = so_hien_tai + ch
    else:
        if so_hien_tai != '':
            if int(so_hien_tai) > lon_nhat:
                lon_nhat = int(so_hien_tai)
            so_hien_tai = ''
print(lon_nhat)
```
