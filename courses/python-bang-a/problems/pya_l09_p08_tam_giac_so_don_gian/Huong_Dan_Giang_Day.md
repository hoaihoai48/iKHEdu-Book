# Hướng Dẫn Giảng Dạy: Tam giác số đơn giản
Chuyên đề: **Quy Luật Dãy Số & Tam Giác Số Kỳ Ảo**

---

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là in tháp số có `N` dòng, dòng thứ `i` in các số từ 1 tới `i`, các số cách nhau một dấu cách.
- Quy trình từng bước với đúng tên biến trong lời giải:
  - Bước 1: `n = int(input().strip())` đọc chiều cao tháp. Với mẫu, `n = 4`.
  - Bước 2: vòng ngoài `for i in range(1, n + 1)` cho `i` lần lượt là 1, 2, 3, 4, mỗi giá trị `i` là một dòng.
  - Bước 3: với mỗi dòng, `" ".join(str(j) for j in range(1, i + 1))` ghép các số từ 1 tới `i` thành một chuỗi rồi in.
- Giá trị biên cụ thể: khi `n = 1` tháp chỉ có một dòng duy nhất là `1`; đề bài giới hạn `1 <= N <= 20` nên tháp cao nhất 20 dòng.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 4)

| Dòng (`i`) | Các số `j` từ 1 tới `i` | Chuỗi được ghép | In ra màn hình |
|---|---|---|---|
| 1 | 1 | `1` | `1` |
| 2 | 1, 2 | `1 2` | `1 2` |
| 3 | 1, 2, 3 | `1 2 3` | `1 2 3` |
| 4 | 1, 2, 3, 4 | `1 2 3 4` | `1 2 3 4` |

- Bốn dòng in ra đúng như kết quả mẫu.

---

## 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1: vòng trong chạy sai thành `range(1, i)`, mỗi dòng thiếu số cuối. Với mẫu `n = 4` dòng 4 chỉ in `1 2 3`, là kết quả sai. Cách sửa: dùng `range(1, i + 1)`.
```python
n = int(input().strip())
for i in range(1, n + 1):
    print(" ".join(str(j) for j in range(1, i)))
```
- Bẫy 2: in số từ 0, tức `range(i)`, khiến dòng đầu in chuỗi rỗng. Với mẫu `n = 4` dòng 1 in ra dòng trắng, là kết quả sai. Cách sửa: cho `j` chạy từ 1.
```python
n = int(input().strip())
for i in range(1, n + 1):
    print(" ".join(str(j) for j in range(i)))
```
- Bẫy 3: dùng `print(j, end=" ")` cho từng số mà không ngắt dòng đúng chỗ, khiến cả tháp dồn thành một dòng `1 1 2 1 2 3 1 2 3 4`, là kết quả sai. Cách sửa: ghép cả dòng bằng `" ".join(...)` rồi `print` một lần cho mỗi dòng.
```python
n = int(input().strip())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
```

---

## 4. Lời giải tham khảo

```python
n = int(input().strip())
for i in range(1, n + 1):
    print(" ".join(str(j) for j in range(1, i + 1)))
```
