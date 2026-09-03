# Bài 16: Danh sách và thao tác cơ bản

---

## 1. Khởi động: Chiếc cặp kéo Doraemon chứa được vô vàn đồ vật

Từ đầu khóa học đến giờ, mỗi biến số của chúng ta (`x = 5`, `ten = "An"`) chỉ giống như một chiếc cốc nhỏ, mỗi lần chỉ đựng được **đúng 1 giá trị duy nhất**.
Nhưng nếu cô giáo giao cho em quản lý điểm số của cả một lớp học có **40 bạn học sinh**, chẳng lẽ chúng ta phải tạo ra 40 biến `diem1, diem2, diem3, ..., diem40` sao? Làm như vậy code sẽ dài hàng trăm dòng và rất dễ nhầm lẫn!

Rất may mắn, Python mang đến cho chúng ta một "bảo bối" thần kỳ: **danh sách (List)**!
Danh sách giống như một **chiếc túi thần kỳ có nhiều ngăn**:
* Nó có thể chứa hàng chục, hàng trăm, thậm chí hàng triệu giá trị cùng một lúc!
* Mỗi ngăn được đánh số thứ tự (index) rõ ràng từ **0** đến **$N-1$**.
* Và đặc biệt hơn chuỗi String: **List cho phép em thoải mái sửa đổi, thêm vào hoặc vứt bớt đồ đạc ra ngoài (Mutable)!**

---

## 2. Cú pháp khởi tạo & truy cập phần tử trong list

### 2.1. Tạo list bằng dấu ngoặc vuông `[ ]`
```python
# Danh sách điểm của 5 bạn học sinh
diem = [8, 9, 10, 7, 9]

# Danh sách rỗng ban đầu chưa có gì
ds_rong = []
```

### 2.2. Nhập một dãy số trên cùng 1 dòng thành list (bí thuật phòng thi!)
Trong các đề thi Tin học trẻ, đề bài thường cho: *"Dòng thứ hai chứa $N$ số nguyên cách nhau bởi khoảng trắng"*.
Cao thủ Python chỉ dùng đúng **1 dòng lệnh duy nhất**:
```python
a = list(map(int, input().split()))
```
> 💡 **Giải mã câu thần chú `list(map(int, input().split()))`:**
> 1. `input()`: Đọc dòng chữ vào.
> 2. `.split()`: Cắt thành các từ riêng biệt.
> 3. `map(int, ...)`: Ép từng từ thành số nguyên.
> 4. `list(...)`: Gom tất cả lại thành một danh sách số nguyên hoàn chỉnh!

### 2.3. Hai cách duyệt danh sách

Khi chỉ cần đọc giá trị, dùng `for x in a`. Khi cần biết vị trí hoặc thay đổi phần tử, dùng `for i in range(len(a))`.

```python
for x in a:
    print(x)

for i in range(len(a)):
    a[i] = a[i] * 2
```

Đây là kỹ năng nền cần chắc trước khi học các bài thống kê và sắp xếp ở Bài 17.

---

## 3. Các chiêu thức thao tác cơ bản trên list

| Phép toán / Lệnh | Ý nghĩa | Ví dụ code |
|---|---|---|
| `a[i]` | Lấy hoặc sửa giá trị tại vị trí `i` | `a[0] = 100` (Đổi phần tử đầu tiên thành 100) |
| `a.append(x)` | **Thêm** phần tử `x` vào CUỐI danh sách | `a.append(50)` |
| `a.insert(i, x)` | **Chèn** phần tử `x` vào vị trí `i` | `a.insert(0, 99)` (Chèn lên đầu) |
| `a.pop()` | **Bốc bỏ** phần tử cuối cùng ra | `a.pop()` |
| `a.remove(x)` | **Xóa** phần tử đầu tiên có giá trị `x` | `a.remove(10)` |
| `x in a` | Kiểm tra giá trị `x` có nằm trong list không | `if 10 in a: print("CO")` |
| `len(a)` | Đếm số lượng phần tử trong list | `print(len(a))` |

---

## 4. Concept quiz: 15 câu trắc nghiệm bắt bẫy củng cố khái niệm

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
