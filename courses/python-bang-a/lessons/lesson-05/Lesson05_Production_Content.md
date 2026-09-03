# Bài 05: Rẽ nhánh nhiều hướng với elif

---

## 1. Khởi động: Ngã ba, ngã tư và bài toán nhiều lựa chọn

Ở Bài 4, câu lệnh `if - else` giúp chúng ta giải quyết các bài toán có **hai ngã rẽ** (Đúng hoặc Sai).
Nhưng cuộc sống đâu chỉ có 2 ngã rẽ! Hãy thử tưởng tượng:
* Đèn giao thông có tới **3 màu**: Đỏ (Dừng lại), Vàng (Đi chậm), Xanh (Được đi).
* Xếp loại học tập có **4 mức**: Xuất sắc ($\ge 9$), Giỏi ($\ge 8$), Khá ($\ge 6.5$), Cần cố gắng.
* Giá cước taxi, tiền điện bậc thang tính theo từng nấc khoảng cách khác nhau.

Nếu chỉ dùng `if` và `else`, chúng ta sẽ phải lồng các lệnh `if` vào nhau chằng chịt như mạng nhện. Rất may mắn, Python mang đến một trợ thủ đắc lực: **`elif`** (viết tắt của *Else If - Nếu không thì nếu*)!

---

## 2. Cú pháp `if - elif - else`: Chiếc cầu trượt nhiều bậc

### 2.1. Cấu trúc chuẩn
```python
if <Điều kiện 1>:
    # Chạy khi Điều kiện 1 ĐÚNG
elif <Điều kiện 2>:
    # Chạy khi Điều kiện 1 SAI, nhưng Điều kiện 2 ĐÚNG
elif <Điều kiện 3>:
    # Chạy khi Điều kiện 1 và 2 đều SAI, nhưng Điều kiện 3 ĐÚNG
else:
    # Chạy khi TẤT CẢ các điều kiện trên đều SAI
```

### 2.2. Bản chất dòng chảy (flow of control): Trượt từ trên xuống dưới
Hãy tưởng tượng cấu trúc `if - elif - else` giống như một **chiếc cầu trượt có nhiều nấc bậc thang**:
1. Máy tính kiểm tra `if` đầu tiên. **Nếu trúng điều kiện ĐÚNG**, máy lập tức thực hiện khối lệnh đó rồi **TRƯỢT THẲNG RA NGOÀI**, bỏ qua toàn bộ các bậc `elif` và `else` phía dưới!
2. Chỉ khi nấc trên bị SAI, máy mới chịu bước xuống kiểm tra nấc `elif` tiếp theo.
3. Nếu tất cả các nấc đều sai, máy sẽ rơi vào căn phòng cứu cánh cuối cùng: `else`.

```python
diem = 8.5

if diem >= 9.0:
    print("XUAT SAC")
elif diem >= 8.0:
    print("GIOI")
elif diem >= 6.5:
    print("KHA")
else:
    print("CAN CO GANG")
```
*Kết quả:* Máy kiểm tra `diem >= 9.0` (Sai vì 8.5 < 9.0) $\implies$ trượt xuống bậc tiếp theo: `diem >= 8.0` (Đúng!) $\implies$ In ra `GIOI` và kết thúc ngay, không xét `diem >= 6.5` nữa!

---

## 3. Các kỹ thuật thuật toán kinh điển với `elif`

### 3.1. Tìm số lớn nhất (max) giữa 3 số $a, b, c$
```python
a = int(input())
b = int(input())
c = int(input())

# Chiến thuật Đặt lính canh (King of the Hill)
so_lon_nhat = a
if b > so_lon_nhat:
    so_lon_nhat = b
if c > so_lon_nhat:
    so_lon_nhat = c

print("So lon nhat la:", so_lon_nhat)
```

### 3.2. Bài toán Mario cứu công chúa (bài 3 THT củ chi)
* Mario cần $K$ năng lượng để leo và tụt $N$ bậc cầu thang (tốn $2N$ năng lượng nếu đi hết).
* Công chúa có $P$ năng lượng, mỗi bậc tốn 2 năng lượng (tốn $2 \times 2 = 4$ năng lượng mỗi bậc).
* Khi nào hai người gặp nhau? Xét các trường hợp so sánh năng lượng để đưa ra kết luận `YES` hoặc `NO`.

---

## 4. Concept quiz: 14 câu trắc nghiệm bắt bẫy củng cố khái niệm

#### Câu 1: Từ khóa `elif` trong Python là viết tắt của cụm từ nào?
- **A.** `else if`
- **B.** **[Đáp án đúng]** `else if`
- **C.** `early if`
- **D.** `end if`
> *Giải thích:* `elif` là dạng viết tắt của `else if` (nếu không thì nếu).

#### Câu 2: Trong cấu trúc `if - elif - else`, có tối đa bao nhiêu khối `elif`?
- **A.** Chỉ được có 1 khối
- **B.** Tối đa 3 khối
- **C.** **[Đáp án đúng]** Không giới hạn số lượng khối `elif`
- **D.** Bắt buộc phải có ít nhất 2 khối
> *Giải thích:* Em có thể đặt bao nhiêu khối `elif` tùy thích để phân loại nhiều trường hợp khác nhau.

#### Câu 3: Khối `else` ở cuối cùng có bắt buộc phải có không?
- **A.** Bắt buộc
- **B.** **[Đáp án đúng]** Không bắt buộc (có thể bỏ qua nếu không cần xử lý trường hợp còn lại)
- **C.** Chỉ bắt buộc khi có `elif`
- **D.** Báo lỗi cú pháp nếu thiếu `else`
> *Giải thích:* Khối `else` là tùy chọn (optional). Nếu không có trường hợp mặc định thì không cần viết `else`.

#### Câu 4: Đoạn code sau in ra kết quả gì?
```python
x = 10
if x > 5:
    print("A")
elif x > 8:
    print("B")
else:
    print("C")
```
- **A.** `B`
- **B.** `A` và `B`
- **C.** **[Đáp án đúng]** `A`
- **D.** `C`
> *Giải thích:* Mặc dù $10 > 8$ cũng đúng, nhưng máy tính gặp `x > 5` đúng trước nên in `A` và thoát ra ngay, không xét tới `elif` nữa.

#### Câu 5: Đoạn code sau in ra gì?
```python
tuoi = 4
if tuoi >= 18:
    print("Nguoi lon")
elif tuoi >= 6:
    print("Hoc sinh")
else:
    print("Mam non")
```
- **A.** `Nguoi lon`
- **B.** `Hoc sinh`
- **C.** **[Đáp án đúng]** `Mam non`
- **D.** Không in gì cả
> *Giải thích:* Cả 2 điều kiện đầu đều sai nên rơi vào khối `else`, in `Mam non`.

#### Câu 6: Thứ tự sắp xếp các điều kiện trong chuỗi `if - elif` có quan trọng không?
- **A.** Không quan trọng, viết cái nào trước cũng được
- **B.** **[Đáp án đúng]** Rất quan trọng, phải sắp xếp theo trật tự logic (từ chặt chẽ nhất đến lỏng hơn)
- **C.** Python tự động sắp xếp lại cho đúng
- **D.** Chỉ quan trọng khi có số âm
> *Giải thích:* Nếu viết `if diem >= 5:` lên trước `elif diem >= 9:`, mọi điểm 9 và 10 đều bị rơi vào điều kiện $\ge 5$ và không bao giờ xuống được điều kiện $\ge 9$!

#### Câu 7: Bác bảo vệ phân loại xe: Xe đạp phí 2k, xe máy 5k, ô tô 20k. Cần ít nhất bao nhiêu nhánh điều kiện?
- **A.** 1 nhánh
- **B.** 2 nhánh
- **C.** **[Đáp án đúng]** 3 nhánh (hoặc 1 `if`, 1 `elif`, 1 `else`)
- **D.** 4 nhánh
> *Giải thích:* Có 3 loại xe nên cần cấu trúc 3 nhánh.

#### Câu 8: Đoạn code nào sau đây báo lỗi cú pháp?
- **A.** `if a > 0: print("Duong")`
- **B.** `elif a == 0: print("Khong")` (đứng một mình không có `if`)
- **C.** **[Đáp án đúng]** Câu B vì `elif` không thể đứng mở đầu mà không có `if`
- **D.** Cả A và B đều đúng
> *Giải thích:* `elif` bắt buộc phải đi sau một lệnh `if`.

#### Câu 9: Để tìm số lớn nhất trong 3 số $a, b, c$, hàm nào có sẵn trong Python giúp ta làm việc này chỉ trong 1 dòng?
- **A.** `maximum(a, b, c)`
- **B.** **[Đáp án đúng]** `max(a, b, c)`
- **C.** `greatest(a, b, c)`
- **D.** `top(a, b, c)`
> *Giải thích:* Hàm `max()` trong Python có thể nhận nhiều đối số và trả về số lớn nhất.

#### Câu 10: Cho đoạn code sau:
```python
a = 0
if a > 0:
    print("Duong")
elif a < 0:
    print("Am")
else:
    print("Khong")
```
Màn hình sẽ in ra:
- **A.** `Duong`
- **B.** `Am`
- **C.** **[Đáp án đúng]** `Khong`
- **D.** Báo lỗi
> *Giải thích:* Số 0 không dương cũng không âm nên chạy vào `else`.

#### Câu 11: Có thể lồng một khối lệnh `if - else` vào bên trong một khối `if` khác không?
- **A.** Không được phép
- **B.** **[Đáp án đúng]** Hoàn toàn được phép (gọi là Nested if - If lồng nhau)
- **C.** Chỉ được lồng tối đa 2 lần
- **D.** Python sẽ báo lỗi bộ nhớ
> *Giải thích:* Python cho phép lồng các cấu trúc điều kiện thoải mái, chỉ cần chú ý thụt lề cho chính xác.

#### Câu 12: Đoạn code sau in ra gì?
```python
n = 15
if n % 3 == 0:
    print("Chia het cho 3")
elif n % 5 == 0:
    print("Chia het cho 5")
```
- **A.** `Chia het cho 5`
- **B.** In cả hai dòng
- **C.** **[Đáp án đúng]** `Chia het cho 3`
- **D.** Không in gì
> *Giải thích:* 15 chia hết cho cả 3 và 5, nhưng điều kiện `n % 3 == 0` đứng trước nên thực hiện xong là kết thúc.

#### Câu 13: Làm thế nào để in ra cả hai dòng nếu số chia hết cho cả 3 và 5?
- **A.** Dùng `elif`
- **B.** **[Đáp án đúng]** Dùng 2 lệnh `if` độc lập nhau
- **C.** Dùng `else`
- **D.** Dùng phép chia dư `% 15`
> *Giải thích:* Hai lệnh `if` độc lập sẽ không loại trừ nhau, máy tính sẽ kiểm tra và thực thi cả hai nếu cùng đúng.

#### Câu 14: Đoạn code sau in ra gì?
```python
x = 5
if x == 1:
    print(1)
elif x == 2:
    print(2)
elif x == 3:
    print(3)
```
- **A.** `0`
- **B.** `None`
- **C.** **[Đáp án đúng]** Không in ra bất kỳ ký tự nào
- **D.** Báo lỗi
> *Giải thích:* Cả 3 điều kiện đều sai và không có nhánh `else`, chương trình kết thúc êm đẹp mà không in gì.
