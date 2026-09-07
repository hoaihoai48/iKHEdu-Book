# Hướng Dẫn Giảng Dạy: Dịch chuyển vòng quanh (left rotation)
Chuyên đề: **Chỉ Số Indexing & Nghệ Thuật Cắt Lát (Slicing)**

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
| 1 | `s = input()` | `s = "ABCDE"` | đoàn tàu 5 toa |
| 2 | `k = int(input())` | `k = 2` | nhấc 2 toa đầu |
| 3 | `s[k:] + s[:k]` | `"CDE" + "AB" = "CDEAB"` | gắn AB ra cuối |
| 4 | `print(...)` | màn hình hiện `CDEAB` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: nối ngược thứ tự `s[:k] + s[k:]`. Đoạn sai:
```python
s = input()
k = int(input())
print(s[:k] + s[k:])
```
Với mẫu `ABCDE` và `2` in ra nguyên `ABCDE`, đáp án đúng là `CDEAB`. Cách sửa: đặt `s[k:]` trước, `s[:k]` sau.
- Bẫy 2: quên đổi `k` sang số nên `s[k:]` báo lỗi. Đoạn sai:
```python
s = input()
k = input()
print(s[k:] + s[:k])
```
Với mẫu trên chương trình báo lỗi vì không cắt chuỗi bằng chữ được, đáp án đúng là `CDEAB`. Cách sửa: đọc `k = int(input())`.

---

## 4. Lời giải tham khảo
```python
s = input()
k = int(input())
print(s[k:] + s[:k])
```
