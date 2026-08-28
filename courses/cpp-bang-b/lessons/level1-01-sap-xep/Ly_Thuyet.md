# MODULE 01 – SẮP XẾP
## Khi thứ tự giúp bài toán dễ hơn

> **Trạng thái:** `draft`  
> **Đối tượng:** Học sinh đã làm quen với Level 0 và bắt đầu học thuật toán  
> **Mã module:** `L1-M01-SORT`

---

## 1. Mục tiêu học tập

Sau module này, em có thể:

- giải thích sắp xếp là gì và vì sao thay đổi thứ tự có thể làm bài toán đơn giản hơn;
- đọc, duyệt và xử lý một mảng hoặc `vector`;
- mô phỏng một quy trình sắp xếp đơn giản bằng tay;
- sử dụng `sort` để sắp xếp tăng dần và giảm dần;
- viết comparator đơn giản cho dãy số nguyên theo một hoặc hai quy tắc;
- biết khi nào cần lưu lại vị trí ban đầu của phần tử;
- nhận ra vai trò của sắp xếp trong các bài ghép cặp, tìm kiếm, tham lam và hai con trỏ;
- phân tích được sự khác nhau cơ bản giữa `O(N²)` và `O(N log N)`;
- tự kiểm tra được các lỗi về chỉ số, thứ tự và comparator.

### Chuẩn hoàn thành

Em được xem là đã nắm chương khi có thể trả lời trước khi viết code:

> **Em sắp xếp theo tiêu chí nào? Sau khi sắp xếp, bước tiếp theo của bài toán dễ hơn ở điểm nào?**

---

## 2. ÔN NHANH LEVEL 0

### Kỹ năng nền đang sử dụng

| Kiến thức | Cần nhớ |
|---|---|
| Biến | Dùng để lưu dữ liệu và kết quả trung gian |
| `vector` | Dùng để lưu một danh sách dữ liệu |
| Vòng lặp `for` | Duyệt lần lượt các phần tử |
| So sánh | Xác định giá trị nào nhỏ hơn, lớn hơn hoặc bằng nhau |
| `max`/`min` | Giữ lại giá trị tốt nhất hiện tại |
| `swap` | Đổi chỗ hai phần tử |
| Hàm | Đóng gói một nhiệm vụ rõ ràng |
| Độ phức tạp | Ước lượng chương trình có đủ nhanh không |

### Mẫu đọc mảng

```cpp
int n;
cin >> n;

vector<int> a(n);
for (int i = 0; i < n; i++) {
    cin >> a[i];
}
```

Với `n` phần tử, chỉ số hợp lệ là:

```text
0, 1, 2, .., n - 1
```

> **Cần chú ý:** `a[n]` là vị trí nằm ngoài mảng. Khi duyệt mảng, điều kiện thường là `i < n`, không phải `i <= n`.

### Câu hỏi khởi động

Cho dãy:

```text
8 3 6 1 5
```

Nếu muốn tìm số lớn nhất, em có thể duyệt từ trái sang phải và giữ lại `max` hiện tại. Nhưng nếu muốn in cả dãy theo thứ tự tăng dần thì chỉ duyệt một lần có đủ không?

---

## 3. SẮP XẾP LÀ GÌ?

Sắp xếp là đưa các phần tử về một trật tự được yêu cầu, chẳng hạn từ nhỏ đến lớn, từ lớn đến nhỏ, theo điểm số, theo thời gian hoặc theo nhiều tiêu chí.

Ví dụ:

```text
Ban đầu:  8  3  6  1  5
Tăng dần: 1  3  5  6  8
```

Sắp xếp không tạo ra dữ liệu mới. Nó chủ yếu thay đổi **vị trí** của các phần tử.

### Vì sao thứ tự lại có ích?

Khi dữ liệu đang lộn xộn, ta có thể phải so sánh rất nhiều phần tử. Sau khi dữ liệu có thứ tự, ta có thể:

- đưa các phần tử nhỏ nhất hoặc lớn nhất về đầu/cuối;
- nhận ra các phần tử bằng nhau vì chúng đứng cạnh nhau;
- tìm các phần tử gần nhau bằng cách chỉ xét các phần tử kề nhau;
- xử lý dữ liệu theo thứ tự ưu tiên;
- kết hợp với hai con trỏ hoặc tìm kiếm nhị phân.

> **Sắp xếp không phải lúc nào cũng là đáp án cuối cùng. Nhiều khi nó là bước chuẩn bị để bước sau trở nên dễ hơn.**

### Sắp xếp có làm mất dữ liệu không?

Sắp xếp làm thay đổi vị trí. Trong phần cơ bản, bài toán chỉ yêu cầu xử lý các giá trị sau khi sắp xếp nên em chưa cần lưu vị trí ban đầu. Nếu một bài toán sau này yêu cầu biết vị trí gốc, đó sẽ là nội dung mở rộng về cách tổ chức nhiều thông tin cho một phần tử.

---

## 4. SẮP XẾP BẰNG TAY: TỪ Ý TƯỞNG ĐẾN THUẬT TOÁN

Trước khi dùng lệnh có sẵn, hãy thử sắp xếp một dãy nhỏ bằng tay.

```text
8 3 6 1 5
```

Một cách làm là:

1. Tìm số nhỏ nhất trong toàn bộ dãy: `1`.
2. Đưa `1` về vị trí đầu tiên.
3. Trong phần còn lại `3 6 8 5`, tìm số nhỏ nhất: `3`.
4. Đưa `3` về vị trí thứ hai.
5. Tiếp tục với phần chưa sắp xếp.

Ta có:

```text
8 3 6 1 5
1 3 6 8 5
1 3 5 8 6
1 3 5 6 8
```

Sau mỗi vòng, một vị trí bên trái đã chắc chắn đúng. Đây là một ví dụ về **bất biến**: phần bên trái đã sắp xếp thì không cần phá lại.

### Selection Sort

Ý tưởng:

```text
Với mỗi vị trí i:
    tìm phần tử nhỏ nhất từ i đến cuối
    đổi phần tử đó với a[i]
```

Code minh họa:

```cpp
for (int i = 0; i < n - 1; i++) {
    int pos = i;

    for (int j = i + 1; j < n; j++) {
        if (a[j] < a[pos]) {
            pos = j;
        }
    }

    swap(a[i], a[pos]);
}
```

### Theo dõi một vòng lặp

Với dãy `8 3 6 1 5`:

| Vòng | Vị trí đang đặt | Phần tử nhỏ nhất còn lại | Dãy sau khi đổi |
|---:|---:|---:|---|
| 1 | `0` | `1` | `1 3 6 8 5` |
| 2 | `1` | `3` | `1 3 6 8 5` |
| 3 | `2` | `5` | `1 3 5 8 6` |
| 4 | `3` | `6` | `1 3 5 6 8` |

### Vì sao Selection Sort chậm?

Ở mỗi vị trí, ta phải tìm trong phần còn lại. Có thể có gần `N` phép so sánh ở vòng đầu, gần `N - 1` ở vòng sau và tiếp tục như vậy. Tổng số thao tác có bậc `O(N²)`.

Selection Sort rất tốt để **hiểu ý tưởng**, nhưng không phải lựa chọn phù hợp cho dữ liệu lớn.

---

## 5. DÙNG `sort` TRONG C++

### Với `vector`

```cpp
sort(a.begin(), a.end());
```

Lệnh này sắp xếp các phần tử của `a` theo thứ tự tăng dần.

- `a.begin()` là vị trí bắt đầu.
- `a.end()` là vị trí ngay sau phần tử cuối.
- Khoảng `[a.begin(), a.end())` gồm đầu nhưng không gồm cuối.

### Với mảng tĩnh

```cpp
int a[100];

sort(a, a + n);
```

Khoảng `[a, a + n)` chứa đúng `n` phần tử đầu tiên.

### Sắp xếp giảm dần

```cpp
sort(a.begin(), a.end(), greater<int>());
```

Hoặc viết comparator:

```cpp
bool cmp(int x, int y) {
    return x > y;
}

sort(a.begin(), a.end(), cmp);
```

### Bài tự kiểm tra

Không nhìn tài liệu, hãy hoàn thành câu sau:

```cpp
sort(______, ______);
```

- Đối số thứ nhất chỉ vị trí nào?
- Đối số thứ hai chỉ vị trí nào?
- Vì sao đối số thứ hai thường là vị trí “sau phần tử cuối”?

---

## 6. COMPARATOR: QUY TẮC AI ĐỨNG TRƯỚC?

Comparator là một hàm trả lời câu hỏi:

> **Trong hai phần tử `x` và `y`, phần tử nào nên đứng trước?**

### Số giảm dần

```cpp
bool cmp(int x, int y) {
    return x > y;
}
```

Nếu `x > y`, số lớn hơn đứng trước, nên dãy được sắp xếp giảm dần.

### Trị tuyệt đối tăng dần

```cpp
bool cmp(int x, int y) {
    return abs(x) < abs(y);
}
```

### Comparator cần nhất quán

Không viết comparator theo cảm tính hoặc thay đổi quy tắc giữa các lần so sánh. Hãy diễn đạt quy tắc bằng lời trước:

```text
Nếu điểm khác nhau: điểm cao hơn đứng trước.
Nếu điểm bằng nhau: tên nhỏ hơn theo thứ tự từ điển đứng trước.
```

Sau đó mới viết code.

---

## 7. COMPARATOR TRÊN DÃY SỐ NGUYÊN

Ở phần cơ bản, ta chỉ làm việc với một dãy số nguyên. Comparator vẫn trả lời câu hỏi “số nào đứng trước?”, nhưng quy tắc phải được viết bằng lời trước khi viết code.

### Ví dụ: số chẵn đứng trước, số lẻ đứng sau

Quy tắc:

```text
1. Số chẵn đứng trước số lẻ.
2. Trong nhóm số chẵn, số nhỏ hơn đứng trước.
3. Trong nhóm số lẻ, số nhỏ hơn đứng trước.
```

```cpp
bool cmp(int x, int y) {
    if (x % 2 != y % 2) {
        return x % 2 < y % 2;
    }
    return x < y;
}

sort(a.begin(), a.end(), cmp);
```

Ở đây, `x % 2` cho biết số `x` là chẵn hay lẻ. Khi hai số thuộc cùng một nhóm, ta dùng giá trị của chúng để sắp xếp tăng dần.

### Cách kiểm tra comparator

Với mỗi cặp số, hãy hỏi:

1. Hai số có cùng nhóm chẵn/lẻ không?
2. Nếu khác nhóm, nhóm nào phải đứng trước?
3. Nếu cùng nhóm, số nào nhỏ hơn?

Không nên viết comparator bằng cách thử ngẫu nhiên. Hãy viết quy tắc bằng lời, sau đó chuyển từng quy tắc thành điều kiện.

### Giới hạn của phần cơ bản

Trong chương này, các ví dụ bắt buộc chỉ dùng `int` và `vector<int>`. Những bài cần lưu một đối tượng có nhiều thuộc tính hoặc cần giữ vị trí ban đầu sẽ được xếp vào phần mở rộng sau, khi em đã học thêm cách tổ chức dữ liệu.

---

## 8. LƯU Ý VỀ VỊ TRÍ BAN ĐẦU – PHẦN MỞ RỘNG

Khi sắp xếp một dãy số, vị trí của các số có thể thay đổi. Trong các bài cơ bản của chương này, ta chỉ cần quan tâm đến **giá trị sau khi sắp xếp**, vì vậy không cần lưu vị trí ban đầu.

Ví dụ:

```text
Ban đầu: 80 95 70 95
Sau khi sắp xếp: 70 80 95 95
```

Nếu một bài toán sau này yêu cầu trả lời “giá trị này đứng ở vị trí nào lúc đầu?”, em sẽ cần học thêm cách lưu một phần tử cùng nhiều thông tin liên quan. Đây là nội dung mở rộng, **không thuộc phần bắt buộc của chương nhập môn Sorting**.

> **Câu hỏi cần nhớ:** Đề bài yêu cầu giá trị sau khi sắp xếp, hay yêu cầu cả vị trí ban đầu?

---

## 9. KHI NÀO SẮP XẾP GIÚP GIẢI BÀI?

### 9.1. Tìm hai giá trị gần nhau nhất

Nếu dãy đã sắp xếp tăng dần, hai giá trị gần nhau nhất phải nằm ở hai vị trí kề nhau. Vì vậy thay vì xét mọi cặp, ta chỉ cần xét:

```text
(a[0], a[1]), (a[1], a[2]), .., (a[n-2], a[n-1])
```

Sắp xếp biến bài toán từ “xét mọi cặp” thành “xét các cặp kề nhau”.

### 9.2. Kiểm tra phần tử trùng nhau

Sau khi sắp xếp, các giá trị giống nhau đứng cạnh nhau. Ta chỉ cần so sánh các phần tử kề nhau.

### 9.3. Ghép hai danh sách

Khi cần ghép các giá trị gần nhau từ hai danh sách, việc sắp xếp giúp ta di chuyển theo hướng có ích thay vì thử mọi cặp. Đây là cầu nối tới **Two Pointers**.

### 9.4. Chọn theo thứ tự ưu tiên

Khi một bài yêu cầu xem xét đối tượng theo thời điểm, điểm số, khối lượng hoặc tiêu chí ưu tiên, sắp xếp có thể là bước chuẩn bị cho **Greedy**.

### 9.5. Tìm kiếm trên dữ liệu có thứ tự

Khi dữ liệu đã tăng dần, ta có thể bỏ qua một nửa phạm vi sau mỗi lần kiểm tra trong **Binary Search**.

---

## 10. SẮP XẾP CÓ PHẢI LÚC NÀO CŨNG CẦN?

Không. Nếu chỉ cần tìm giá trị lớn nhất một lần, duyệt mảng và giữ `max` có thể đủ:

```cpp
int mx = a[0];
for (int x : a) {
    mx = max(mx, x);
}
```

Sắp xếp toàn bộ mảng trong trường hợp này có thể là công việc dư thừa.

Hãy phân biệt:

| Nhu cầu | Hướng thường nghĩ đến |
|---|---|
| Chỉ cần một giá trị lớn nhất/nhỏ nhất | Duyệt + `max/min` |
| Cần toàn bộ dữ liệu theo thứ tự | Sorting |
| Cần nhiều giá trị gần nhau | Sorting + xét kề nhau |
| Cần ghép cặp gần nhau | Sorting + Two Pointers |
| Cần chọn theo ưu tiên | Sorting + Greedy |
| Cần tìm nhanh nhiều lần | Sorting + Binary Search |

> **Không chọn thuật toán vì tên nghe quen. Hãy chọn vì nó giải quyết đúng nhu cầu của bài toán.**

---

## 11. ĐỘ PHỨC TẠP

### So sánh hai cách

| Cách làm | Ý tưởng | Độ phức tạp thường gặp |
|---|---|---:|
| Selection Sort | Nhiều vòng tìm phần tử nhỏ nhất | `O(N²)` |
| `std::sort` | Dùng thuật toán thư viện chuẩn | `O(N log N)` |
| Duyệt một lần | Xử lý từng phần tử | `O(N)` |

Nếu `N` rất lớn, sự khác nhau giữa `N²` và `N log N` là rất đáng kể.

### Bộ nhớ

Sắp xếp trực tiếp một `vector` thường không cần tạo thêm một bản sao lớn của toàn bộ dữ liệu. Tuy vậy, nếu lưu thêm chỉ số ban đầu hoặc tạo mảng phụ, hãy tính cả phần bộ nhớ đó.

### Câu hỏi kiểm tra

- Nếu có hai vòng lặp đều chạy theo `N`, độ phức tạp thường là bao nhiêu?
- Nếu sắp xếp rồi duyệt thêm một lần, phần nào quyết định độ phức tạp tổng thể?
- Nếu bài chỉ cần `max`, vì sao sắp xếp có thể là dư thừa?

---

## 12. BÀI MẪU DẪN DẮT

### Bài toán: Khoảng cách nhỏ nhất

Một hệ thống có `N` vị trí trên một tuyến đường. Hãy tìm khoảng cách nhỏ nhất giữa hai vị trí bất kỳ.

#### Bước 1: Input – Process – Output

- **Input:** `N` và `N` vị trí.
- **Process:** chọn hai vị trí khác nhau, tính khoảng cách, giữ khoảng cách nhỏ nhất.
- **Output:** khoảng cách nhỏ nhất.

#### Bước 2: Cách làm trực tiếp

Thử mọi cặp `(i, j)` với `i < j`. Có thể có `O(N²)` cặp.

#### Bước 3: Câu hỏi tối ưu

Nếu sắp xếp vị trí tăng dần, hai vị trí gần nhau nhất có nhất thiết phải đứng cạnh nhau không?

Có. Nếu giữa hai vị trí còn một điểm khác, điểm đó sẽ nằm giữa chúng và tạo ra một khoảng cách không lớn hơn khoảng cách đang xét.

#### Bước 4: Cách làm sau khi sắp xếp

```text
1. Sắp xếp các vị trí tăng dần.
2. Chỉ xét các cặp kề nhau.
3. Giữ khoảng cách nhỏ nhất.
```

#### Bước 5: Pseudocode

```text
sort(a)
answer = rất lớn
for i từ 1 đến N - 1:
    answer = min(answer, a[i] - a[i - 1])
print(answer)
```

#### Bước 6: Bài học rút ra

Sắp xếp không trực tiếp trả lời khoảng cách nhỏ nhất. Nó tạo ra trật tự để ta có thể **bỏ qua phần lớn các cặp không cần xét**.

---

## 13. LỖI THƯỜNG GẶP

| Lỗi | Cách tự kiểm tra |
|---|---|
| Dùng `i <= n` | Chỉ số cuối của `n` phần tử là `n - 1` |
| Nhầm tăng và giảm | Viết bằng lời “ai đứng trước ai?” |
| Sắp xếp sai khoảng | Nhớ khoảng `[begin, end)` |
| Comparator ngược | Thử comparator trên hai giá trị cụ thể |
| Quên tiêu chí phụ | Xét trường hợp hai phần tử bằng tiêu chí chính |
| Mất vị trí ban đầu | Lưu `value` cùng `original_index` |
| Dùng `int` cho dữ liệu lớn | Đọc giới hạn và cân nhắc `long long` |
| Sắp xếp dù không cần | Xác định sau khi sort sẽ làm bước gì |
| Chỉ chép `sort` | Giải thích vai trò của sort trong toàn bộ lời giải |

---

## 14. TỰ KIỂM TRA CUỐI BÀI

Không nhìn tài liệu, hãy trả lời:

1. Sắp xếp thay đổi giá trị hay vị trí của phần tử?
2. Với `n` phần tử, chỉ số cuối là gì?
3. Vì sao `sort(a.begin(), a.end())` không dùng `a.end() - 1`?
4. Comparator trả lời câu hỏi nào?
5. Muốn sắp xếp điểm giảm dần, tên tăng dần khi bằng điểm, em làm thế nào?
6. Khi nào phải lưu vị trí ban đầu?
7. Vì sao sắp xếp giúp tìm hai phần tử gần nhau nhất?
8. Vì sao Selection Sort phù hợp để học ý tưởng nhưng không phù hợp với dữ liệu lớn?
9. Nếu chỉ cần tìm `max` một lần, có nhất thiết phải sort không?
10. Trước khi viết code sorting, em cần trả lời câu hỏi nào?

### Nhiệm vụ giải thích bằng lời

Hãy nói trong tối đa một phút:

> “Sắp xếp giúp giải bài toán của em như thế nào?”

Nếu câu trả lời chỉ là “vì dùng `sort`”, em cần quay lại phần 9 và tìm rõ **bước tiếp theo sau khi sắp xếp**.

---

## 15. TÓM TẮT CHƯƠNG

| Thành phần | Ghi nhớ |
|---|---|
| Ý tưởng | Đưa dữ liệu về một trật tự phù hợp |
| Cú pháp tăng dần | `sort(a.begin(), a.end())` |
| Cú pháp giảm dần | `sort(a.begin(), a.end(), greater<int>())` |
| Comparator | Quy tắc phần tử nào đứng trước |
| Quy tắc nâng cao | Có thể sắp xếp theo nhiều tiêu chí sau khi học thêm cách tổ chức dữ liệu |
| Vị trí ban đầu | Chỉ cần xử lý khi đề bài yêu cầu; cách lưu sẽ học ở phần mở rộng |
| Hiệu quả | Thường dùng `O(N log N)` thay cho cách `O(N²)` |
| Câu hỏi chính | Sắp xếp xong thì bước nào của bài toán trở nên dễ hơn? |

### Kiến thức sẽ dùng về sau

```text
Sorting
   ↓
Greedy
   ↓
Two Pointers
   ↓
Binary Search
   ↓
Interval Scheduling / Graph / Geometry
```

Sắp xếp là một viên gạch quan trọng, nhưng sức mạnh của nó thường xuất hiện khi được **kết hợp với một kỹ thuật khác**.

---

## Tài liệu tham chiếu nội bộ

- `SRC-001`: `IKHEDU_Knowledge_Base.md` — nguồn tham chiếu bài toán, editorial, code và quy ước project; không chỉnh sửa.
- `SRC-002`: `ikhEdu_foundation_framework_report.md` — định hướng nền tảng, prerequisite, learning outcomes và cách gọi lại Level 0.
- `SRC-004`: `Lo_trinh_hoc_tap_bangB_level1.jpg` — roadmap chủ đề Level 1; chủ đề Sắp xếp là module mở đầu của bản roadmap.

**Trạng thái kiểm duyệt:** `draft`; cần review chuyên môn và kiểm tra alignment với bài tập trước khi phát hành.
