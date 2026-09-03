# Bài 17: Thống kê danh sách và sắp xếp

---

## 1. Khởi động: Hội đồng trọng tài Olympic & bảng xếp hạng huy chương

Trong một cuộc thi đấu thể thao Olympic, sau khi 10 vận động viên hoàn thành bài thi:
* Trọng tài cần tìm ra **điểm số cao nhất** để trao Huy chương Vàng.
* Cần tìm **điểm số thấp nhất** để loại trừ điểm sai sót.
* Cần tính **điểm trung bình cộng** của tất cả các vận động viên.
* Và quan trọng nhất: Cần **sắp xếp toàn bộ bảng điểm từ cao xuống thấp** để vinh danh các tuyển thủ lên bục nhận giải!

Nếu làm bằng tay, chúng ta sẽ mất rất nhiều thời gian và dễ nhầm lẫn.
Nhưng với Python, hệ thống các hàm thống kê và thuật toán sắp xếp siêu tốc **Timsort** sẽ giúp em làm tất cả những điều này chỉ trong vài dòng code gọn gàng!

---

## 2. Bộ ba hàm thống kê tối thượng: `min()`, `max()`, `sum()`

Python cung cấp sẵn 3 hàm toán học chạy siêu nhanh trên mọi danh sách số:

```python
diem = [8, 10, 7, 9, 6]

print("Diem cao nhat:", max(diem)) # In ra 10
print("Diem thap nhat:", min(diem)) # In ra 6
print("Tong diem:", sum(diem))      # In ra 40
print("Trung binh:", sum(diem) / len(diem)) # In ra 8.0
```

---

## 3. Nghệ thuật sắp xếp: `sort()` và `sorted()`

Đây là một trong những vũ khí quan trọng nhất khi đi thi Tin học trẻ!
Trong Python có 2 cách sắp xếp danh sách:

### 3.1. Phương thức `a.sort()`: Sắp xếp tại chỗ (làm thay đổi trực tiếp mảng gốc)
* **Tăng dần (mặc định):**
  ```python
  a = [5, 2, 8, 1, 9]
  a.sort()
  print(a) # In ra: [1, 2, 5, 8, 9]
  ```
* **Giảm dần (thêm `reverse=True`):**
  ```python
  a.sort(reverse=True)
  print(a) # In ra: [9, 8, 5, 2, 1]
  ```

### 3.2. Hàm `sorted(a)`: Tạo ra một bản sao mới đã được sắp xếp (không làm đổi mảng gốc)
```python
goc = [3, 1, 4]
moi = sorted(goc)
print("Moi:", moi) # [1, 3, 4]
print("Goc:", goc) # [3, 1, 4] (Van giu nguyen!)
```

---

## 4. Kỹ thuật loại bỏ phần tử trùng lặp (lọc số độc nhất)

Khi có một danh sách bị trùng lặp số: `a = [1, 2, 2, 3, 3, 3, 4]`:
* **Cách 1 (Dùng vòng lặp kiểm tra `not in`):**
  ```python
  unique = []
  for x in a:
      if x not in unique:
          unique.append(x)
  print(unique) # [1, 2, 3, 4]
  ```
* **Cách 2 (Dùng cấu trúc tập hợp `set` chuyển đổi nhanh):**
  ```python
  unique = sorted(list(set(a)))
  ```

---

## 5. Concept quiz: 15 câu trắc nghiệm bắt bẫy củng cố khái niệm

#### Câu 1: Hàm nào trong Python trả về giá trị lớn nhất trong danh sách số `a`?
- **A.** `a.maximum()`
- **B.** `a.largest()`
- **C.** **[Đáp án đúng]** `max(a)`
- **D.** `top(a)`
- > *Giải thích:* `max()` là hàm tích hợp sẵn trong Python nhận đầu vào là một danh sách.

#### Câu 2: Hàm `sum(a)` trên danh sách `a = [2, 4, 6, 8]` trả về kết quả bằng bao nhiêu?
- **A.** 10
- **B.** **[Đáp án đúng]** 20
- **C.** 4
- **D.** 24
- > *Giải thích:* $2 + 4 + 6 + 8 = 20$.

#### Câu 3: Điểm khác biệt lớn nhất giữa `a.sort()` và `sorted(a)` là gì?
- **A.** `a.sort()` chạy chậm hơn
- **B.** **[Đáp án đúng]** `a.sort()` làm biến đổi trực tiếp danh sách `a` gốc, còn `sorted(a)` tạo ra danh sách mới và giữ nguyên `a` gốc
- **C.** `sorted(a)` chỉ dùng cho chuỗi
- **D.** Không có sự khác biệt
- > *Giải thích:* `a.sort()` là phương thức in-place (tại chỗ), không trả về giá trị (trả về `None`).

#### Câu 4: Để sắp xếp danh sách `a` theo thứ tự giảm dần, cú pháp nào đúng?
- **A.** `a.sort(down=True)`
- **B.** `a.sort(descending=True)`
- **C.** **[Đáp án đúng]** `a.sort(reverse=True)`
- **D.** `a.reverse_sort()`
- > *Giải thích:* Tham số `reverse=True` đảo chiều thứ tự sắp xếp mặc định sang giảm dần.

#### Câu 5: Cho `a = [10, 5, 20, 15]`. Sau khi chạy `a.sort()`, phần tử `a[0]` và `a[-1]` lần lượt là:
- **A.** 10 và 15
- **B.** **[Đáp án đúng]** 5 và 20
- **C.** 20 và 5
- **D.** 5 và 15
- > *Giải thích:* Sau khi sort tăng dần `[5, 10, 15, 20]`: số nhỏ nhất ở đầu `a[0] = 5`, số lớn nhất ở cuối `a[-1] = 20`.

#### Câu 6: Muốn tìm số lớn thứ hai trong danh sách các số đôi một khác nhau `a`, sau khi gọi `a.sort()`, số đó nằm ở vị trí nào?
- **A.** `a[1]`
- **B.** **[Đáp án đúng]** `a[-2]` (Phần tử kế cuối)
- **C.** `a[-1] - 1`
- **D.** `a[len(a)]`
- > *Giải thích:* Trong mảng đã sắp xếp tăng dần, phần tử lớn nhất là `a[-1]`, phần tử lớn thứ nhì là `a[-2]`.

#### Câu 7: Công thức tính trung bình cộng của các số trong danh sách `a` là:
- **A.** `average(a)`
- **B.** `sum(a) // len(a)`
- **C.** **[Đáp án đúng]** `sum(a) / len(a)`
- **D.** `mean(a)`
- > *Giải thích:* Tổng chia cho số lượng phần tử: `sum(a) / len(a)`. Dùng phép chia thực `/` để kết quả chính xác có phần thập phân.

#### Câu 8: Đoạn code sau in ra kết quả gì?
```python
a = [3, 1, 2]
b = a.sort()
print(b)
```
- **A.** `[1, 2, 3]`
- **B.** **[Đáp án đúng]** `None` (Bẫy lỗi kinh điển!)
- **C.** `[3, 1, 2]`
- **D.** Báo lỗi cú pháp
- > *Giải thích:* Bẫy kinh điển: Phương thức `a.sort()` sắp xếp tại chỗ và trả về `None`. Biến `b` sẽ nhận giá trị `None`! Muốn lấy danh sách mới phải dùng `b = sorted(a)`.

#### Câu 9: Lệnh `a.reverse()` có tác dụng gì?
- **A.** Sắp xếp giảm dần
- **B.** **[Đáp án đúng]** Đảo ngược thứ tự các phần tử hiện tại của danh sách (không quan tâm giá trị lớn hay nhỏ)
- **C.** Sắp xếp tăng dần
- **D.** Xóa phần tử cuối
- > *Giải thích:* `reverse()` chỉ lật ngược thứ tự trước sau của mảng hiện tại.

#### Câu 10: Cho danh sách `a = [4, 7, 2, 7, 9, 7]`. Lệnh `a.count(max(a))` trả về:
- **A.** 3
- **B.** **[Đáp án đúng]** 1 (Số lớn nhất là 9, xuất hiện 1 lần)
- **C.** 7
- **D.** 9
- > *Giải thích:* `max(a)` là 9. Số 9 xuất hiện đúng 1 lần trong mảng.

#### Câu 11: Khi sắp xếp danh sách các chuỗi chữ cái `['banana', 'apple', 'cherry']`, Python sẽ sắp xếp theo quy tắc nào?
- **A.** Theo độ dài ngắn của từ
- **B.** **[Đáp án đúng]** Theo thứ tự từ điển (Lexicographical order - tra từ điển A-Z)
- **C.** Theo số lượng nguyên âm
- **D.** Ngẫu nhiên
- > *Giải thích:* Thứ tự từ điển so sánh mã ASCII của từng ký tự từ trái qua phải: `'apple' < 'banana' < 'cherry'`.

#### Câu 12: Đoạn code sau in ra giá trị gì?
```python
a = [10, 20, 30]
print(sum(a) - max(a) - min(a))
```
- **A.** 0
- **B.** 10
- **C.** **[Đáp án đúng]** 20
- **D.** 30
- > *Giải thích:* Tổng $10+20+30=60$. Trừ max (30) trừ min (10) còn lại đúng phần tử ở giữa là 20.

#### Câu 13: Cú pháp nào sau đây dùng để lọc bỏ toàn bộ phần tử trùng lặp và giữ lại các số độc nhất sắp xếp tăng dần?
- **A.** `unique(a)`
- **B.** **[Đáp án đúng]** `sorted(list(set(a)))`
- **C.** `a.distinct()`
- **D.** `a.filter()`
- > *Giải thích:* `set(a)` loại bỏ phần tử trùng lặp, `list(...)` chuyển lại thành danh sách, `sorted(...)` sắp xếp tăng dần.

#### Câu 14: Thuật toán sắp xếp tích hợp sẵn trong Python có tên là gì?
- **A.** Bubble Sort (Sắp xếp nổi bọt)
- **B.** Quick Sort (Sắp xếp nhanh)
- **C.** **[Đáp án đúng]** Timsort (Thuật toán lai ghép tối ưu cực nhanh)
- **D.** Selection Sort (Sắp xếp chọn)
- > *Giải thích:* Timsort do Tim Peters sáng tạo năm 2002, kết hợp Merge Sort và Insertion Sort, có độ phức tạp trung bình $\mathcal{O}(N \log N)$.

#### Câu 15: Cho danh sách `diem = [9.5, 8.0, 10.0, 7.5]`. Để in ra điểm số cao thứ nhì, câu lệnh chuẩn nhất là:
- **A.** `diem.sort(); print(diem[1])`
- **B.** **[Đáp án đúng]** `diem.sort(); print(diem[-2])`
- **C.** `print(max(diem) - 1)`
- **D.** `print(diem[2])`
- > *Giải thích:* Sắp xếp tăng dần: điểm cao nhất ở `diem[-1]`, điểm cao thứ nhì ở `diem[-2]`.
