# Bài 11: Danh sách và thao tác cơ bản

## 1. Tóm tắt kiến thức trọng tâm
- Danh sách (List) là tập hợp nhiều phần tử lưu trong dấu ngoặc vuông `[]`.
- Cho phép thay đổi giá trị tại từng vị trí (Mutable): `a[0] = 100`.
- **Cú pháp nhập danh sách số trên 1 dòng chuẩn thi đấu:**
  ```python
  a = list(map(int, input().split()))
  ```
- **Các lệnh thao tác danh sách cơ bản:**
  - `a.append(x)`: Thêm $x$ vào cuối danh sách.
  - `a.remove(x)`: Xóa phần tử đầu tiên có giá trị $x$.
  - `a.insert(i, x)`: Chèn giá trị $x$ vào vị trí index $i$.
  - `len(a)`: Trả về số lượng phần tử.
  - `if x in a:`: Kiểm tra $x$ có nằm trong danh sách không.

## 2. Concept quiz: 15 câu trắc nghiệm bắt bẫy củng cố khái niệm

#### Câu 1: Để khai báo một danh sách rỗng trong Python, cú pháp nào đúng?
- **A.** `a = ()`
- **B.** `a = {}`
- **C.** **[Đáp án đúng]** `a = []` hoặc `a = list()`
- **D.** `a = ""`
- > *Giải thích:* List trong Python được định nghĩa bằng cặp dấu ngoặc vuông `[]`.

#### Câu 2: Cho `a = [10, 20, 30, 40]`. Phần tử `a[0]` có giá trị là:
- **A.** 20
- **B.** **[Đáp án đúng]** 10
- **C.** 40
- **D.** 0
- > *Giải thích:* Chỉ số index của List trong Python luôn bắt đầu từ số 0.

#### Câu 3: Lệnh nào sau đây dùng để thêm một số `99` vào cuối danh sách `a`?
- **A.** `a.add(99)`
- **B.** `a.push(99)`
- **C.** **[Đáp án đúng]** `a.append(99)`
- **D.** `a.insert(99)`
- > *Giải thích:* Phương thức `append(x)` luôn nối phần tử `x` vào vị trí cuối cùng của List.

#### Câu 4: Cho `a = [1, 2, 3]`. Lệnh `a[1] = 9` sẽ biến danh sách `a` thành:
- **A.** `[9, 2, 3]`
- **B.** **[Đáp án đúng]** `[1, 9, 3]`
- **C.** `[1, 2, 9]`
- **D.** Báo lỗi vì List không thể thay đổi
- > *Giải thích:* Khác với String (bất biến), List là đối tượng thay đổi được (Mutable), ta có thể gán đè giá trị tại bất kỳ index nào.

#### Câu 5: Lệnh `a.pop()` không truyền tham số có tác dụng gì?
- **A.** Xóa phần tử đầu tiên
- **B.** **[Đáp án đúng]** Xóa và trả về phần tử CUỐI CÙNG của danh sách
- **C.** Xóa toàn bộ danh sách
- **D.** Đảo ngược danh sách
- > *Giải thích:* `pop()` mặc định loại bỏ phần tử ở vị trí cuối cùng của danh sách.

#### Câu 6: Dòng code nào sau đây dùng để đọc một mảng các số nguyên cách nhau bởi dấu cách từ bàn phím chuẩn xác nhất?
- **A.** `a = input()`
- **B.** `a = int(input())`
- **C.** **[Đáp án đúng]** `a = list(map(int, input().split()))`
- **D.** `a = list(input())`
- > *Giải thích:* Cú pháp chuẩn trong thi đấu: `input().split()` tách chuỗi, `map(int, ...)` ép kiểu số nguyên, `list(...)` tạo mảng.

#### Câu 7: Cho `a = [5, 8, 12, 20]`. Biểu thức `15 in a` trả về giá trị gì?
- **A.** `True`
- **B.** **[Đáp án đúng]** `False`
- **C.** Báo lỗi
- **D.** 0
- > *Giải thích:* Toán tử `in` kiểm tra sự tồn tại của một giá trị trong List. Số 15 không có trong `a` nên trả về `False`.

#### Câu 8: Cho `a = [1, 2, 3]`. Lệnh `a * 2` sẽ tạo ra kết quả gì?
- **A.** `[2, 4, 6]`
- **B.** **[Đáp án đúng]** `[1, 2, 3, 1, 2, 3]`
- **C.** Báo lỗi
- **D.** `[1, 2, 3, 2]`
- > *Giải thích:* Phép nhân List với một số nguyên $K$ sẽ nhân bản danh sách đó lên $K$ lần (không phải nhân giá trị từng phần tử).

#### Câu 9: Lệnh `a.insert(0, 100)` có tác dụng gì?
- **A.** Gán đè phần tử đầu tiên bằng 100
- **B.** **[Đáp án đúng]** Chèn giá trị 100 vào ĐẦU danh sách (vị trí index 0) và đẩy các phần tử khác lùi về sau
- **C.** Thêm 100 vào cuối
- **D.** Tìm số 100
- > *Giải thích:* `insert(index, value)` chèn phần tử vào vị trí chỉ định và dồn các phần tử sau sang phải.

#### Câu 10: Cho `a = [10, 20, 30, 20]`. Sau khi gọi `a.remove(20)`, danh sách `a` sẽ là:
- **A.** `[10, 30]` (Xóa hết các số 20)
- **B.** **[Đáp án đúng]** `[10, 30, 20]` (Chỉ xóa số 20 ĐẦU TIÊN gặp được)
- **C.** `[10, 20, 30]`
- **D.** Báo lỗi
- > *Giải thích:* `remove(x)` chỉ tìm và xóa phần tử có giá trị $x$ đầu tiên tính từ trái sang phải.

#### Câu 11: Đoạn code sau in ra màn hình bao nhiêu số?
```python
a = [2, 4, 6, 8, 10]
for x in a:
    if x > 5:
        print(x)
```
- **A.** 5 số
- **B.** 2 số
- **C.** **[Đáp án đúng]** 3 số (gồm 6, 8, 10)
- **D.** 4 số
- > *Giải thích:* Các số lớn hơn 5 trong danh sách là 6, 8, 10.

#### Câu 12: Biểu thức `a[-1]` trên một danh sách không rỗng trả về:
- **A.** Phần tử đầu tiên
- **B.** **[Đáp án đúng]** Phần tử cuối cùng của danh sách
- **C.** Báo lỗi chỉ số âm
- **D.** Độ dài danh sách
- > *Giải thích:* Tương tự chuỗi, chỉ số âm `-1` là phần tử cuối cùng của List.

#### Câu 13: Cú pháp slicing `a[1:3]` trên danh sách `a = ['A', 'B', 'C', 'D']` trả về:
- **A.** `['A', 'B']`
- **B.** **[Đáp án đúng]** `['B', 'C']`
- **C.** `['B', 'C', 'D']`
- **D.** `['C', 'D']`
- > *Giải thích:* Lấy từ index 1 (`'B'`) đến index 2 (`'C'`), không lấy index 3.

#### Câu 14: Đoạn code sau in ra giá trị gì?
```python
a = [1, 2, 3]
b = [4, 5]
c = a + b
print(len(c))
```
- **A.** 3
- **B.** 2
- **C.** **[Đáp án đúng]** 5
- **D.** Báo lỗi
- > *Giải thích:* Phép cộng `+` hai danh sách sẽ nối chúng lại thành `[1, 2, 3, 4, 5]` có độ dài 5.

#### Câu 15: Để xóa toàn bộ các phần tử trong danh sách `a` đưa về danh sách rỗng, ta dùng lệnh nào?
- **A.** `a.delete()`
- **B.** **[Đáp án đúng]** `a.clear()`
- **C.** `a.remove_all()`
- **D.** `a = None`
- > *Giải thích:* `clear()` dọn sạch toàn bộ các phần tử trong danh sách.
