# MODULE 01 – SẮP XẾP
## Bài tập thực hành

> **Trạng thái:** `draft`  
> **Đối tượng:** Học sinh Level 1  
> **Mã module:** `L1-M01-SORT`

## Cách sử dụng

Các bài được sắp xếp từ thao tác trực tiếp đến bài biến thể. Em nên đọc mục tiêu và tự viết hướng làm trước khi code. Không cần cố giải ngay bài khó; hãy quay lại hộp **Ôn nhanh Level 0** khi quên `vector`, vòng lặp, comparator hoặc chỉ số mảng.

Mỗi bài nên được hoàn thành theo chuỗi:

```text
Đọc đề → xác định Input/Output → viết ý tưởng bằng lời
       → code → test nhỏ → kiểm tra độ phức tạp → tự giải thích
```

## Learning outcomes

| Mã | Năng lực |
|---|---|
| `LO-S01` | Sử dụng được `sort` cho mảng/vector |
| `LO-S02` | Viết được comparator đơn giản trên dãy số nguyên |
| `LO-S03` | Nhận ra vai trò của sorting trong lời giải |
| `LO-S04` | Phân tích được độ phức tạp cơ bản |
| `LO-S05` | Nhận biết được khi nào thứ tự ban đầu có thể bị thay đổi |
| `LO-S06` | Giải thích và chuyển giao được mẫu sorting sang bài mới |

---

# TẦNG A – CỦNG CỐ CÚ PHÁP

## Bài 1.1 – Dãy số tăng dần

### Mục tiêu

- `LO-S01`
- Ôn đọc `vector`, chỉ số mảng và sử dụng `sort`.

### Yêu cầu

Đọc `N` số nguyên và in các số theo thứ tự không giảm.

### Input

- Dòng đầu chứa số nguyên `N`.
- Dòng sau chứa `N` số nguyên.

### Output

In ra dãy sau khi sắp xếp tăng dần, cách nhau bởi một dấu cách.

### Ví dụ

```text
Input
5
8 3 6 1 5

Output
1 3 5 6 8
```

### Gợi ý mức 1

Hãy xác định hai iterator biểu diễn đoạn chứa toàn bộ `vector`.

### Tiêu chí tự kiểm tra

- Có đọc đủ `N` phần tử.
- Không truy cập chỉ số ngoài `0..N-1`.
- Output không có chữ giải thích thừa.
- Chạy đúng khi `N = 1`.

---

## Bài 1.2 – Dãy số giảm dần

### Mục tiêu

- `LO-S01`
- Phân biệt thứ tự tăng dần và giảm dần.

### Yêu cầu

Đọc `N` số nguyên và in theo thứ tự không tăng.

### Ví dụ

```text
Input
6
4 9 1 9 3 2

Output
9 9 4 3 2 1
```

### Câu hỏi trước khi code

- Dùng `greater<int>()` hay comparator riêng?
- Khi có hai số bằng nhau, thứ tự của chúng có ảnh hưởng không?

### Tiêu chí tự kiểm tra

Thử thêm trường hợp tất cả các phần tử bằng nhau và trường hợp dãy đã giảm dần.

---

## Bài 1.3 – Kiểm tra dãy đã có thứ tự chưa

### Mục tiêu

- `LO-S03`
- Hiểu khi nào có thể kiểm tra thứ tự bằng cách xét các phần tử kề nhau.

### Yêu cầu

Cho `N` số nguyên. In `YES` nếu dãy đã sắp xếp không giảm; ngược lại in `NO`.

### Ví dụ

```text
Input
5
1 2 2 5 9

Output
YES
```

```text
Input
4
1 4 3 8

Output
NO
```

### Gợi ý mức 1

Duyệt từ `i = 1` và kiểm tra `a[i] < a[i - 1]`.

### Tiêu chí tự kiểm tra

Em phải giải được bài này **không cần gọi `sort`**. Đây là bài giúp phân biệt “kiểm tra thứ tự” với “sắp xếp dữ liệu”.

---

## Bài 1.4 – Đếm các giá trị trùng nhau sau khi sắp xếp

### Mục tiêu

- `LO-S01`, `LO-S03`
- Nhận ra rằng các giá trị giống nhau sẽ đứng cạnh nhau sau khi sắp xếp.

### Yêu cầu

Cho `N` số nguyên. Đếm số giá trị khác nhau trong dãy.

### Ví dụ

```text
Input
8
4 2 4 1 2 2 9 1

Output
4
```

### Câu hỏi dẫn dắt

Sau khi sắp xếp, làm thế nào biết một phần tử là giá trị mới chưa từng gặp?

### Tiêu chí tự kiểm tra

- Không đếm một giá trị nhiều lần.
- Xử lý đúng khi tất cả phần tử giống nhau.
- Xử lý đúng khi mọi phần tử khác nhau.

---

# TẦNG B – VẬN DỤNG MẪU

## Bài 1.5 – Số chẵn đứng trước

### Mục tiêu

- `LO-S02`
- Viết comparator trên `int` với hai quy tắc đơn giản.

### Độ khó

Cơ bản nâng cao.

### Yêu cầu

Cho `N` số nguyên. Hãy sắp xếp sao cho số chẵn đứng trước số lẻ. Trong mỗi nhóm, các số được sắp xếp tăng dần.

### Input

- Dòng đầu chứa `N`.
- Dòng sau chứa `N` số nguyên.

### Output

In dãy sau khi sắp xếp, cách nhau bởi một dấu cách.

### Ví dụ

```text
Input
7
5 2 8 1 4 7 3

Output
2 4 8 1 3 5 7
```

### Gợi ý mức 1

Hãy viết quy tắc bằng lời: kiểm tra nhóm chẵn/lẻ trước, sau đó mới so sánh giá trị.

### Tiêu chí tự kiểm tra

- Tất cả số chẵn đứng trước mọi số lẻ.
- Mỗi nhóm vẫn tăng dần.
- Thử trường hợp không có số chẵn hoặc không có số lẻ.

---

## Bài 1.6 – Sắp xếp theo trị tuyệt đối

### Mục tiêu

- `LO-S02`, `LO-S03`
- Viết comparator theo trị tuyệt đối và xử lý trường hợp bằng nhau.

### Độ khó

Cơ bản nâng cao.

### Yêu cầu

Cho `N` số nguyên. Hãy sắp xếp theo trị tuyệt đối tăng dần. Nếu hai số có cùng trị tuyệt đối, số nhỏ hơn đứng trước.

### Input

- Dòng đầu chứa `N`.
- Dòng sau chứa `N` số nguyên.

### Output

In dãy sau khi sắp xếp, cách nhau bởi một dấu cách.

### Ví dụ

```text
Input
6
-5 2 -1 4 -2 3

Output
-1 -2 2 3 4 -5
```

### Gợi ý mức 1

So sánh `abs(x)` và `abs(y)` trước. Nếu bằng nhau, so sánh `x` và `y`.

### Tiêu chí tự kiểm tra

- Có xử lý đúng số âm và số dương không?
- Khi `x = -2` và `y = 2`, số nào đứng trước?
- Có dùng kiểu dữ liệu phù hợp nếu trị tuyệt đối lớn không?

---

## Bài 1.7 – Khoảng cách nhỏ nhất

### Mục tiêu

- `LO-S03`, `LO-S04`
- Hiểu vì sao sau khi sắp xếp chỉ cần xét các phần tử kề nhau.

### Yêu cầu

Cho `N` vị trí nguyên trên một tuyến đường. Tìm khoảng cách nhỏ nhất giữa hai vị trí khác nhau.

### Input

- Dòng đầu chứa `N`.
- Dòng sau chứa `N` vị trí.

### Output

In khoảng cách nhỏ nhất.

### Ví dụ

```text
Input
5
8 3 6 1 5

Output
1
```

### Gợi ý mức 1

Sau khi sắp xếp, hãy xét `a[i] - a[i - 1]` với `i` từ `1` đến `N - 1`.

### Tiêu chí tự kiểm tra

- Không xét một phần tử với chính nó.
- Dùng kiểu dữ liệu phù hợp với hiệu giữa hai vị trí.
- Giải thích được vì sao không cần xét mọi cặp.

---

## Bài 1.8 – Giá trị gần mục tiêu nhất

### Mục tiêu

- `LO-S02`, `LO-S03`
- Kết hợp sắp xếp với quy tắc phá hòa.

### Yêu cầu

Cho `N` số nguyên và số nguyên `X`. Tìm giá trị có khoảng cách tuyệt đối tới `X` nhỏ nhất. Nếu có nhiều giá trị cùng khoảng cách, chọn giá trị nhỏ hơn.

### Ví dụ

```text
Input
6 10
4 13 8 12 20 7

Output
8
```

### Câu hỏi dẫn dắt

Có thể sắp xếp rồi duyệt để tìm đáp án không? Có nhất thiết phải dùng binary search ở bài này không?

### Tiêu chí tự kiểm tra

Thử các trường hợp `X` nhỏ hơn mọi phần tử, lớn hơn mọi phần tử và nằm đúng giữa hai phần tử.

---

## Bài 1.9 – Gom nhóm giá trị

### Mục tiêu

- `LO-S03`
- Nhận biết các đoạn liên tiếp bằng nhau sau khi sắp xếp.

### Yêu cầu

Cho `N` mã sản phẩm. Hãy in mỗi mã khác nhau cùng số lần xuất hiện, theo thứ tự tăng dần của mã.

### Ví dụ

```text
Input
7
5 2 5 3 2 2 8

Output
2 3
3 1
5 2
8 1
```

### Gợi ý mức 1

Sắp xếp trước. Sau đó duyệt từng đoạn các phần tử bằng nhau.

### Tiêu chí tự kiểm tra

- Không bỏ sót đoạn cuối.
- Không in một mã nhiều lần.
- Tổng các tần suất phải bằng `N`.

---

# TẦNG C – CHUYỂN GIAO

## Bài 1.10 – Ghép hai danh sách gần nhau

### Mục tiêu

- `LO-S03`, `LO-S04`, `LO-S06`
- Nhận ra sắp xếp là tiền xử lý cho Two Pointers.

### Yêu cầu

Có `N` xe và `M` cảm biến. Mỗi xe có một giá trị công suất, mỗi cảm biến có một giá trị tần số. Tìm độ chênh lệch tuyệt đối nhỏ nhất giữa một xe và một cảm biến bất kỳ.

### Ví dụ

```text
Input
3 2
10 20 30
15 24

Output
4
```

### Gợi ý mức 1

Sắp xếp cả hai danh sách tăng dần. Khi hai giá trị hiện tại khác nhau, di chuyển con trỏ đang đứng ở giá trị nhỏ hơn.

### Tiêu chí tự kiểm tra

- Không thử mọi cặp nếu `N`, `M` lớn.
- Dừng đúng khi một con trỏ đi hết mảng.
- Phân tích được phần sắp xếp và phần hai con trỏ.

> Bài này là bài chuyển tiếp giữa Sorting và Two Pointers. Khi cần đối chiếu với ngân hàng bài toán, có thể tham khảo mã `IKH-0016` trong knowledge base; không coi bài tập này là bản sao thay thế statement nguồn.

---

## Bài 1.11 – Sắp xếp theo chữ số cuối

### Mục tiêu

- `LO-S02`, `LO-S03`, `LO-S06`
- Viết comparator trên số nguyên bằng một quy tắc tính từ giá trị.

### Độ khó

Thử thách trong phần cơ bản.

### Yêu cầu

Cho `N` số nguyên không âm. Hãy sắp xếp theo chữ số hàng đơn vị tăng dần. Nếu hai số có cùng chữ số hàng đơn vị, số nhỏ hơn đứng trước.

### Input

- Dòng đầu chứa `N`.
- Dòng sau chứa `N` số nguyên không âm.

### Output

In dãy sau khi sắp xếp, cách nhau bởi một dấu cách.

### Ví dụ

```text
Input
6
23 41 18 35 12 29

Output
41 12 23 35 18 29
```

### Gợi ý mức 1

Chữ số hàng đơn vị của `x` là `x % 10`. Hãy so sánh chữ số hàng đơn vị trước, sau đó so sánh giá trị nếu cần.

### Tiêu chí tự kiểm tra

- Tất cả số có chữ số hàng đơn vị nhỏ hơn đứng trước.
- Khi chữ số hàng đơn vị bằng nhau, số nhỏ hơn đứng trước.
- Thử trường hợp các số có cùng chữ số hàng đơn vị.

---

## Bài 1.12 – Có cần sắp xếp không?

### Mục tiêu

- `LO-S03`, `LO-S04`, `LO-S06`
- Biết đánh giá việc sử dụng sorting có thực sự cần thiết không.

### Yêu cầu

Với mỗi mô tả sau, hãy chọn `CÓ` hoặc `KHÔNG` cần sắp xếp, rồi giải thích bằng một hoặc hai câu:

1. Tìm điểm cao nhất trong một danh sách.
2. In toàn bộ danh sách theo thứ tự tăng dần.
3. Đếm số phần tử chẵn.
4. Tìm hai phần tử gần nhau nhất.
5. Tìm xem một giá trị có xuất hiện hay không trong một mảng chưa sắp xếp.
6. Ghép hai danh sách sao cho chênh lệch nhỏ nhất.

### Tiêu chí tự kiểm tra

Câu trả lời phải nêu được:

- Kết quả cần tìm là gì.
- Sắp xếp giúp ích ở bước nào.
- Nếu không sắp xếp, có thể dùng duyệt một lần hoặc cách khác hay không.

---

## 3. Phiếu tự đánh giá

Đánh dấu sau khi làm bài:

| Năng lực | Chưa chắc | Làm khi có gợi ý | Tự làm được |
|---|:---:|:---:|:---:|
| Sắp xếp tăng/giảm bằng `sort` |  |  |  |
| Viết comparator trên số nguyên |  |  |  |
| Viết comparator với hai quy tắc trên `int` |  |  |  |
| Nhận biết thứ tự ban đầu có thể thay đổi |  |  |  |
| Giải thích vì sao sorting giúp bài toán |  |  |  |
| Phân tích `O(N²)` và `O(N log N)` |  |  |  |
| Kết hợp sorting với hai con trỏ |  |  |  |
| Tự tạo test biên |  |  |  |

## 4. Tiêu chí nộp bài

Trước khi gửi bài, em cần kiểm tra:

- Code biên dịch thành công.
- Không còn dòng debug trong output.
- Tên biến và comparator dễ hiểu.
- Không truy cập ngoài mảng.
- Đã thử sample và ít nhất ba test tự tạo.
- Có thể giải thích bằng lời mục đích của bước sắp xếp.
- Nếu dùng `sort`, biết độ phức tạp dự kiến của lời giải.

## 5. Gợi ý cho giáo viên

Không nên chấm các bài chỉ dựa trên output đúng. Với các bài từ `1.7` trở đi, nên yêu cầu học sinh viết thêm một đoạn ngắn trả lời: **“Sau khi sắp xếp, tôi được lợi gì?”**. Câu trả lời này là bằng chứng học sinh hiểu vai trò của thuật toán chứ không chỉ biết gọi thư viện.
