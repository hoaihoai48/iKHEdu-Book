# Hướng Dẫn Giảng Dạy: Từ xuất hiện nhiều nhất trong đoạn
Chuyên đề: **Tách Từ & Mật Mã Thay Thế**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: đếm số lần mỗi từ xuất hiện rồi chọn từ có số lần lớn nhất.
- Quy trình với biến thật (`words`, `counts`, `best_word`):
  - Tách `s.split()` được 8 từ: `cam, quyt, mit, dua, cam, xoai, cam, dua`.
  - Duyệt và ghi vào từ điển `counts`: `cam` được 3, `dua` được 2, còn lại mỗi từ 1.
  - `max(counts, key=counts.get)` chọn `best_word = "cam"`, in `cam 3` bằng `print(best_word, counts[best_word])`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: cam quyt mit dua cam xoai cam dua)
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `words = s.split()` | 8 từ, 5 từ khác nhau | `cam` lặp 3 lần |
| 2 | vòng đếm `counts` | `{'cam': 3, 'quyt': 1, 'mit': 1, 'dua': 2, 'xoai': 1}` | đủ 8 lượt cộng |
| 3 | `best_word = max(...)` | `"cam"` | số lần lớn nhất là 3 |
| 4 | `print(best_word, counts[best_word])` | màn hình hiện `cam 3` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: in từ kèm danh sách đếm sai vì không dùng từ điển. Đoạn sai:
```python
s = input()
words = s.split()
print(words[0], words.count(words[0]))
```
Với mẫu trên may mắn vẫn ra `cam 3` vì `cam` đứng đầu, nhưng đoạn mà từ đầu không phải từ nhiều nhất (ví dụ `dua cam cam`) sẽ in `dua 1` là kết quả sai. Cách sửa: đếm đủ bằng từ điển `counts` rồi chọn `max`.
- Bẫy 2: quên in số lần, chỉ in từ. Đoạn sai:
```python
s = input()
words = s.split()
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
print(max(counts, key=counts.get))
```
Với mẫu trên chỉ in `cam`, thiếu số `3`, đáp án đúng là `cam 3`. Cách sửa: in cả hai `print(best_word, counts[best_word])`.

---

## 4. Lời giải tham khảo
```python
s = input()
words = s.split()
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
best_word = max(counts, key=counts.get)
print(best_word, counts[best_word])
```
