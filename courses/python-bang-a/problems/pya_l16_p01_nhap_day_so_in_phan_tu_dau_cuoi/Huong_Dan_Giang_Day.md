# Hướng Dẫn Giảng Dạy: Nhập dãy số & in phần tử đầu - cuối
Chuyên đề: **Chiếc Hộp Thần Kỳ list & Thao Tác Cơ Bản**

---

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là lấy hai phần tử ở hai đầu của danh sách: phần tử đầu tiên và phần tử cuối cùng.
- Với số mẫu `N = 5`, dãy `10 25 3 47 99`: phần tử đầu là `10`, phần tử cuối là `99` nên đáp án là `10 99`.
- Quy trình trong lời giải với các biến `n`, `a`:
  - Đọc `n = 5`.
  - Đọc dãy `a = [10, 25, 3, 47, 99]`.
  - Lấy `a[0]` được `10` và `a[-1]` được `99`, in ra `10 99`.
- Giá trị biên cụ thể: `N = 1` thì phần tử đầu và cuối là cùng một số (ví dụ dãy `7` thì in `7 7`).

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5 / 10 25 3 47 99)

| Bước | Thao tác | Giá trị |
|------|----------|---------|
| 1 | Đọc `n` | `n = 5` |
| 2 | Đọc dãy `a` | `a = [10, 25, 3, 47, 99]` |
| 3 | Lấy `a[0]` | `10` |
| 4 | Lấy `a[-1]` | `99` |
| 5 | In kết quả | màn hình hiện `10 99` |

Kết quả cuối cùng khớp với đáp án mẫu: `10 99`.

---

## 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — lấy vị trí cuối bằng `a[n]`:
```python
n = int(input().strip())
a = list(map(int, input().split()))
print(a[0], a[n])
```
Với mẫu `n = 5`, `a[5]` vượt khỏi dãy (vị trí cuối là `a[4]`) nên chương trình báo lỗi. Cách sửa: dùng `a[-1]` hoặc `a[n - 1]`.
- Bẫy 2 — in mỗi số một dòng:
```python
n = int(input().strip())
a = list(map(int, input().split()))
print(a[0])
print(a[-1])
```
Với mẫu trên in ra hai dòng `10` rồi `99`, không khớp đáp án mẫu `10 99` trên một dòng. Cách sửa: in chung một lệnh `print(a[0], a[-1])`.
- Bẫy 3 — quên đọc dòng `N` nên đọc nhầm dãy:
```python
a = list(map(int, input().split()))
print(a[0], a[-1])
```
Với mẫu trên, lệnh đọc đầu tiên lấy nhầm dòng `5` thành dãy `[5]` rồi in ra `5 5` sai. Cách sửa: đọc `n` trước rồi mới đọc dãy `a`.

---

## 4. Lời giải tham khảo

```python
n = int(input().strip())
a = list(map(int, input().split()))
print(a[0], a[-1])
```
