# iKHEDU – LEVEL 1
# GIÁO TRÌNH THUẬT TOÁN CƠ BẢN

## Trạng thái tài liệu

- **Loại tài liệu:** Phác thảo cấu trúc giáo trình in.
- **Phạm vi hiện tại:** Chương 1 – Sắp xếp.
- **Đối tượng:** Học sinh đã được làm quen với phần Level 0 và bắt đầu học tư duy thuật toán.
- **Vai trò:** Đây là bản outline để review trước khi viết nội dung đầy đủ.
- **Nguồn tham chiếu:** Roadmap Level 1 và knowledge base iKHEDU.
- **Nguyên tắc:** Không chỉnh sửa hoặc ghi ngược nội dung vào `IKHEDU_Knowledge_Base.md`.

---

# PHẦN I. NỀN TẢNG THUẬT TOÁN LEVEL 1

## Mục tiêu của phần I

Phần I giúp học sinh chuyển từ việc sử dụng các viên gạch Level 0 sang việc nhận dạng và kết hợp các mẫu thuật toán cơ bản. Mỗi chương không chỉ giới thiệu một kỹ thuật, mà phải trả lời được ba câu hỏi:

1. **Bài toán có dấu hiệu gì?**
2. **Vì sao kỹ thuật này giúp giải bài tốt hơn?**
3. **Khi nào kỹ thuật này không còn phù hợp?**

Mỗi chương Level 1 sẽ nhắc lại một lượng nhỏ kiến thức Level 0 ngay trước khi sử dụng, sau đó đưa học sinh từ bài làm trực tiếp đến bài cần tối ưu.

---

# CHƯƠNG 1. SẮP XẾP – KHI THỨ TỰ GIÚP BÀI TOÁN DỄ HƠN

## 1. Vai trò của chương

Sắp xếp là chương mở đầu phù hợp cho Level 1 vì học sinh đã biết mảng, vòng lặp, so sánh, đổi chỗ và tìm giá trị lớn nhất/nhỏ nhất từ Level 0. Chương này giúp các em nhận ra rằng cùng một tập dữ liệu, nếu được đặt theo một trật tự phù hợp thì việc tìm kiếm, ghép cặp, chọn lựa hoặc tính toán có thể trở nên đơn giản hơn.

Chương không nên được dạy như một danh sách các hàm `sort`. Mục tiêu là giúp học sinh hiểu ba tầng:

> **Dữ liệu ban đầu → thay đổi thứ tự → khai thác trật tự mới để giải bài toán.**

## 2. Chuẩn đầu vào của chương

Trước khi bắt đầu, học sinh cần tự kiểm tra:

| Kiến thức Level 0 | Học sinh cần làm được |
|---|---|
| Biến và kiểu dữ liệu | Khai báo được số nguyên, số lớn và biến tạm |
| Điều kiện | So sánh được hai giá trị |
| Vòng lặp | Duyệt toàn bộ mảng |
| Mảng/`vector` | Đọc, in và truy cập `a[i]` |
| Hàm `max/min` | Tìm giá trị tốt nhất trong một lần duyệt |
| Độ phức tạp | Hiểu trực giác của `O(N²)` và `O(N log N)` |
| Debug | Kiểm tra được chỉ số và kết quả trung gian |

Nếu học sinh chưa chắc phần mảng và vòng lặp, giáo viên nên dành một hoạt động ôn nhanh trước khi vào chương, không cần quay lại toàn bộ Level 0.

## 3. Mục tiêu đầu ra

Sau chương này, học sinh có thể:

1. Giải thích được sắp xếp là gì và vì sao thứ tự dữ liệu có thể giúp giải bài.
2. Duyệt mảng và mô phỏng một thuật toán sắp xếp đơn giản.
3. Sử dụng `sort` cho mảng và `vector`.
4. Sắp xếp tăng dần, giảm dần và theo điều kiện tùy chỉnh.
5. Sắp xếp danh sách đối tượng theo một hoặc nhiều tiêu chí.
6. Nhận ra các bài toán có thể đơn giản hóa sau khi sắp xếp.
7. Phân biệt việc “sắp xếp để lấy đáp án” với việc “sắp xếp chỉ để in ra”.
8. Phân tích được độ phức tạp cơ bản của việc sắp xếp.
9. Kiểm tra được các lỗi thường gặp về comparator, kiểu dữ liệu và thứ tự ưu tiên.
10. Tự giải được bài toán mới ở mức cơ bản và giải thích được hướng làm trước khi viết code.

## 4. Bản đồ chương

```text
Bài toán chưa có trật tự
        ↓
Có cần sắp xếp không?
        ↓
Chọn thứ tự phù hợp
        ↓
Sắp xếp dữ liệu
        ↓
Duyệt / ghép cặp / chọn / tìm kiếm
        ↓
Kiểm tra đáp án và độ phức tạp
```

## 5. Cấu trúc chương dự kiến

| Phần | Tiêu đề | Hình thức |
|---|---|---|
| 1 | Câu chuyện mở đầu: Vì sao thứ tự quan trọng? | Tình huống thực tế + câu hỏi gợi mở |
| 2 | Ôn nhanh Level 0 | Hộp tra cứu 1 trang |
| 3 | Sắp xếp bằng tay | Hoạt động kéo thẻ/sắp số |
| 4 | Ý tưởng đổi chỗ và tìm phần tử phù hợp | Ví dụ trực quan |
| 5 | Sắp xếp đơn giản để hiểu bản chất | Code có chú thích |
| 6 | Dùng `sort` trong C++ | Cú pháp và thực hành |
| 7 | Tăng dần, giảm dần, comparator | Ví dụ ngắn |
| 8 | Sắp xếp nhiều tiêu chí | `pair`, `struct`, comparator |
| 9 | Từ sắp xếp đến giải bài | Các mẫu nhận dạng |
| 10 | Bài mẫu có hướng dẫn | Phân tích từ đề đến code |
| 11 | Luyện tập phân tầng | Cơ bản, chuẩn, biến thể |
| 12 | Debug và lỗi thường gặp | Bảng lỗi + bài sửa code |
| 13 | Tóm tắt cuối chương | Bảng nhớ nhanh |
| 14 | Kiểm tra cuối chương | Trắc nghiệm, tracing, coding |

---

## 6. Nội dung chi tiết từng mục

### 6.1. Câu chuyện mở đầu: Vì sao thứ tự quan trọng?

**Bối cảnh đề xuất:** Một trung tâm cần xếp danh sách điểm học sinh từ thấp đến cao để phân nhóm, hoặc một kho hàng cần xếp các kiện hàng theo khối lượng để dễ lựa chọn.

**Câu hỏi dẫn dắt:**

- Nếu danh sách đang lộn xộn, việc tìm người điểm cao nhất có khó không?
- Nếu muốn tìm hai số gần nhau nhất, sắp xếp trước có giúp ích không?
- Có phải bài toán nào cũng cần sắp xếp không?
- Sắp xếp có làm thay đổi dữ liệu hay chỉ thay đổi vị trí?

**Mục tiêu sư phạm:** Học sinh hiểu rằng sắp xếp không phải là đích đến. Nó là một bước tiền xử lý giúp tạo ra trật tự để các bước sau dễ thực hiện hơn.

### 6.2. Ôn nhanh Level 0

Hộp ôn nhanh đặt ở đầu chương, không quá nửa đến một trang:

```cpp
vector<int> a(n);
for (int i = 0; i < n; i++) cin >> a[i];

for (int i = 0; i < n; i++) {
    // xử lý a[i]
}
```

| Kiến thức cần gọi lại | Câu hỏi nhắc nhớ |
|---|---|
| Mảng/`vector` | Có bao nhiêu phần tử? Chỉ số cuối là gì? |
| So sánh | Khi nào `a[i] < a[j]`? |
| Đổi chỗ | Muốn đổi hai giá trị cần biến tạm nào? |
| Vòng lặp | Đang xét phần tử nào? |
| Độ phức tạp | Hai vòng lặp theo `N` thường là bao nhiêu? |
| Debug | Sau mỗi bước, mảng đang có dạng gì? |

**Bài khởi động 5 phút:** Cho một mảng 5 số, yêu cầu học sinh tự viết ra thứ tự tăng dần bằng tay và mô tả các lần đổi chỗ.

### 6.3. Hoạt động không code: Sắp xếp bằng tay

Giáo viên đưa cho học sinh các thẻ số hoặc thẻ tên. Học sinh phải sắp xếp tăng dần trong thời gian ngắn.

Hoạt động cần làm rõ:

- Ta đang so sánh hai phần tử nào?
- Ta chọn phần tử nào đưa về vị trí đúng?
- Sau mỗi vòng, phần nào của danh sách đã chắc chắn đúng?
- Ta có cần kiểm tra lại phần đã đúng không?

Phần này giúp học sinh hình thành khái niệm **bất biến đơn giản** trước khi nhìn code.

### 6.4. Sắp xếp đơn giản để hiểu bản chất

Có thể giới thiệu Selection Sort hoặc một quy trình chọn phần tử nhỏ nhất, nhưng mục đích chính là hiểu ý tưởng, không phải bắt học sinh sử dụng thuật toán này trong mọi bài thi.

**Mô hình tư duy:**

```text
Vị trí i đang cần một giá trị.
Tìm giá trị nhỏ nhất trong phần chưa sắp xếp.
Đưa giá trị đó về vị trí i.
Lặp lại cho vị trí tiếp theo.
```

**Pseudocode:**

```text
for mỗi vị trí i:
    tìm phần tử nhỏ nhất từ i đến cuối
    đổi phần tử nhỏ nhất với a[i]
```

**Câu hỏi kiểm tra hiểu:**

- Sau vòng đầu tiên, điều gì chắc chắn đúng?
- Vì sao phần bên trái không cần xét lại?
- Nếu có các giá trị bằng nhau, thuật toán có còn hoạt động không?
- Có bao nhiêu lần so sánh khi `N` tăng?

**Code minh họa dự kiến:**

```cpp
for (int i = 0; i < n - 1; i++) {
    int pos = i;
    for (int j = i + 1; j < n; j++) {
        if (a[j] < a[pos]) pos = j;
    }
    swap(a[i], a[pos]);
}
```

**Thông điệp cần chốt:** Selection Sort giúp hiểu bản chất nhưng có độ phức tạp `O(N²)`. Khi `N` lớn, cần dùng công cụ sắp xếp hiệu quả hơn.

### 6.5. Dùng `sort` trong C++

**Mẫu cơ bản:**

```cpp
sort(a.begin(), a.end());
```

**Mảng tĩnh:**

```cpp
sort(a, a + n);
```

**Sắp xếp giảm dần:**

```cpp
sort(a.begin(), a.end(), greater<int>());
```

**Điểm phải hiểu:**

- `a.begin()` là vị trí bắt đầu.
- `a.end()` là vị trí ngay sau phần tử cuối.
- Khoảng `[begin, end)` bao gồm đầu nhưng không bao gồm cuối.
- `sort` thay đổi thứ tự các phần tử trong cấu trúc dữ liệu.

**Bài thực hành ngắn:** Đọc `N` số, in dãy tăng dần, rồi in dãy giảm dần.

### 6.6. Comparator và thứ tự tùy chỉnh

Học sinh cần hiểu comparator như câu trả lời cho câu hỏi:

> **Trong hai phần tử `x` và `y`, phần tử nào nên đứng trước?**

**Ví dụ sắp xếp số giảm dần:**

```cpp
bool cmp(int x, int y) {
    return x > y;
}

sort(a.begin(), a.end(), cmp);
```

**Ví dụ sắp xếp theo trị tuyệt đối tăng dần:**

```cpp
bool cmp(int x, int y) {
    return abs(x) < abs(y);
}
```

Ở mức đầu, không cần đưa ngay các tính chất hình thức của strict weak ordering, nhưng giáo viên cần nhắc rằng comparator phải đưa ra một quy tắc nhất quán.

### 6.7. Sắp xếp nhiều tiêu chí

Dùng cấu trúc `pair` hoặc `struct` để mô tả một đối tượng có nhiều thông tin.

**Ví dụ:** Sắp xếp học sinh theo điểm giảm dần; nếu bằng điểm thì tên tăng dần.

```cpp
struct Student {
    string name;
    int score;
};

bool cmp(const Student& a, const Student& b) {
    if (a.score != b.score) return a.score > b.score;
    return a.name < b.name;
}
```

**Mẫu suy nghĩ:**

```text
Tiêu chí 1 khác nhau → quyết định theo tiêu chí 1.
Tiêu chí 1 bằng nhau → xét tiêu chí 2.
Tiêu chí 2 vẫn bằng nhau → xét tiêu chí tiếp theo nếu có.
```

**Bài luyện dẫn dắt:** Xếp sản phẩm theo giá tăng dần; nếu cùng giá thì số lượng giảm dần.

### 6.8. Khi nào sắp xếp giúp giải bài?

Học sinh cần được luyện các dấu hiệu sau:

| Dấu hiệu | Tác dụng của sắp xếp |
|---|---|
| Cần lấy các phần tử nhỏ/lớn nhất | Đưa các phần tử cần xét về đầu hoặc cuối |
| Cần ghép các phần tử gần nhau | Sau khi sắp xếp, chỉ cần xét các phần tử kề nhau |
| Cần kiểm tra trùng lặp | Các giá trị bằng nhau đứng cạnh nhau |
| Cần xử lý theo thứ tự ưu tiên | Sắp xếp theo tiêu chí ưu tiên |
| Cần dùng hai con trỏ | Thứ tự giúp di chuyển con trỏ có định hướng |
| Cần chọn hoạt động hoặc đoạn | Sắp xếp theo thời điểm kết thúc hoặc tiêu chí phù hợp |

**Câu hỏi bắt buộc:** Sắp xếp có làm mất thông tin vị trí ban đầu không? Nếu bài yêu cầu vị trí gốc, cần lưu cả giá trị và chỉ số ban đầu.

### 6.9. Mẫu bài toán minh họa chính của chương

Mỗi bài mẫu cần được trình bày theo cùng một khuôn:

1. Đọc đề và gạch chân dữ liệu quan trọng.
2. Xác định Input – Process – Output.
3. Thử cách làm trực tiếp.
4. Tìm điểm khó hoặc điểm chậm của cách trực tiếp.
5. Đặt câu hỏi: “Nếu sắp xếp trước thì điều gì thay đổi?”
6. Mô tả thuật toán bằng lời.
7. Viết pseudocode.
8. Viết code C++.
9. Kiểm tra sample và test biên.
10. Phân tích độ phức tạp.

**Nhóm bài mẫu nên có:**

| Bài mẫu | Kỹ năng chính |
|---|---|
| In danh sách theo thứ tự tăng/giảm | Cú pháp `sort` |
| Tìm hai phần tử gần nhau nhất | Sắp xếp rồi xét phần tử kề nhau |
| Đếm số giá trị khác nhau | Sắp xếp và gom nhóm |
| Xếp hạng học sinh | Sắp xếp nhiều tiêu chí |
| Chọn các đối tượng theo thứ tự ưu tiên | Tiền đề cho tư duy greedy |

### 6.10. Liên hệ với bài toán iKHEDU

Mỗi bài lấy từ knowledge base cần được gắn mã bài, chủ đề, kiến thức Level 0 được gọi lại và kỹ thuật Level 1 được sử dụng. Không nên đưa toàn bộ bài nâng cao vào chương chỉ vì bài có sử dụng `sort`.

Mẫu thông tin đặt trước mỗi bài:

```text
Mã bài: IKH-XXXX
Kỹ thuật chính: Sorting
Kiến thức Level 0 cần dùng: vector, vòng lặp, so sánh, hàm, long long
Mức độ: Cơ bản / Chuẩn / Thử thách
Mục tiêu: Sau bài này học sinh nhận ra được...
```

### 6.11. Lỗi thường gặp và bài sửa code

| Lỗi | Biểu hiện | Cách sửa |
|---|---|---|
| Sai khoảng sắp xếp | Bỏ sót phần tử cuối hoặc sắp xếp ngoài phạm vi | Kiểm tra `[begin, end)` |
| Nhầm tăng/giảm | Dùng sai comparator | Đọc lại câu hỏi “ai đứng trước?” |
| Comparator không nhất quán | Kết quả khó đoán | Viết quy tắc theo từng tiêu chí |
| Mất chỉ số ban đầu | Không trả lời được vị trí gốc | Lưu `pair<value, index>` hoặc `struct` |
| Dùng `int` cho dữ liệu lớn | Kết quả bị tràn | Đọc giới hạn và cân nhắc `long long` |
| Sắp xếp khi không cần | Code dài hoặc làm mất ý nghĩa thứ tự gốc | Xác định mục đích sắp xếp trước |
| Chỉ học thuộc `sort` | Gặp bài biến thể không biết làm gì | Luôn trả lời “sắp xếp để làm bước nào tiếp theo?” |

### 6.12. Hệ thống bài tập phân tầng

#### Tầng A – Củng cố cú pháp

1. Sắp xếp `N` số tăng dần.
2. Sắp xếp `N` số giảm dần.
3. Tìm phần tử nhỏ nhất/lớn nhất sau khi sắp xếp.
4. Đếm số giá trị trùng nhau.
5. In danh sách theo thứ tự từ điển.

#### Tầng B – Vận dụng mẫu

1. Tìm khoảng cách nhỏ nhất giữa hai số.
2. Xếp học sinh theo điểm và tên.
3. Kiểm tra một danh sách có phần tử trùng nhau không.
4. Ghép các phần tử theo thứ tự phù hợp.
5. Sắp xếp rồi dùng hai con trỏ để tìm một cặp thỏa điều kiện.

#### Tầng C – Chuyển giao

1. Bài có bối cảnh khác nhưng cùng mẫu sắp xếp.
2. Bài yêu cầu giữ lại vị trí ban đầu.
3. Bài có hai hoặc ba tiêu chí sắp xếp.
4. Bài cần nhận ra rằng sắp xếp chỉ là bước tiền xử lý.
5. Bài mà sắp xếp trực tiếp chưa đủ và cần kết hợp với greedy hoặc two pointers.

Mỗi tầng nên có ít nhất một bài học sinh phải giải thích được **vì sao sắp xếp là bước phù hợp**, không chỉ viết đúng lệnh `sort`.

### 6.13. Tóm tắt cuối chương

> **Sắp xếp không chỉ là đổi vị trí các phần tử. Sắp xếp là cách tạo ra trật tự để nhìn thấy cấu trúc của bài toán.**

| Cần nhớ | Nội dung |
|---|---|
| Cú pháp | `sort(a.begin(), a.end())` |
| Giảm dần | `greater<int>()` hoặc comparator |
| Comparator | Trả lời phần tử nào đứng trước |
| Nhiều tiêu chí | Xét tiêu chí sau khi tiêu chí trước bằng nhau |
| Mục đích | Tạo trật tự để tìm, ghép, chọn hoặc kiểm tra |
| Cẩn thận | Khoảng chỉ số, comparator, vị trí ban đầu, kiểu dữ liệu |
| Câu hỏi chính | Sắp xếp xong thì bước tiếp theo dễ hơn ở điểm nào? |

### 6.14. Bảng kết nối Level 0 → Chương 1

| Viên gạch Level 0 | Được nâng lên thành |
|---|---|
| Duyệt mảng | Duyệt dữ liệu sau khi sắp xếp |
| So sánh hai giá trị | Quy tắc thứ tự |
| Đổi chỗ | Ý tưởng của các thuật toán sắp xếp |
| `max/min` | Chọn phần tử nhỏ/lớn nhất |
| Hàm | Comparator và hàm xử lý |
| `vector` | Danh sách dữ liệu cần sắp xếp |
| Độ phức tạp | So sánh `O(N²)` với `O(N log N)` |
| Debug | Kiểm tra thứ tự và phạm vi sắp xếp |

## 7. Thiết kế buổi học đề xuất

| Buổi | Nội dung | Sản phẩm của học sinh |
|---:|---|---|
| 1 | Vì sao cần sắp xếp; hoạt động sắp xếp bằng tay; ôn mảng và so sánh | Pseudocode quy trình sắp xếp |
| 2 | Selection Sort để hiểu bản chất; theo dõi bất biến | Code mô phỏng và tracing từng vòng |
| 3 | `sort`, tăng/giảm, khoảng iterator | 3 bài cú pháp ngắn |
| 4 | Comparator và sắp xếp nhiều tiêu chí | Code sắp xếp `struct` |
| 5 | Bài mẫu: sắp xếp để giải bài | Một lời giải hoàn chỉnh từ đề đến phân tích |
| 6 | Luyện tập phân tầng và sửa code sai | Bài độc lập + phiếu tự đánh giá |
| 7 | Kiểm tra chương và bài chuyển giao | Bài coding mới, không trùng ví dụ |

Có thể điều chỉnh số buổi theo trình độ lớp. Mỗi buổi vẫn cần giữ chu trình: **gọi lại Level 0 → hình thành ý tưởng → làm có hướng dẫn → làm độc lập → tổng kết**.

## 8. Đánh giá cuối chương

### Phần A – Nhớ và hiểu

- Giải thích `sort(a.begin(), a.end())` sắp xếp đoạn nào.
- Phân biệt sắp xếp tăng dần và giảm dần.
- Cho biết comparator nào đặt `x` trước `y`.
- Dự đoán trạng thái mảng sau một bước của Selection Sort.

### Phần B – Đọc và sửa code

- Phát hiện lỗi `i <= n` khi duyệt mảng.
- Sửa comparator bị ngược thứ tự.
- Bổ sung tiêu chí thứ hai khi hai phần tử bằng nhau.
- Xác định lỗi làm mất chỉ số ban đầu.

### Phần C – Viết code

- Một bài áp dụng trực tiếp `sort`.
- Một bài sắp xếp theo hai tiêu chí.
- Một bài cần sắp xếp rồi mới thực hiện bước xử lý tiếp theo.

### Phần D – Chuyển giao

Học sinh phải trả lời bằng lời trước khi code:

> “Tôi sắp xếp theo tiêu chí nào, và sau khi sắp xếp thì bài toán còn lại trở nên đơn giản như thế nào?”

## 9. Chuẩn hoàn thành chương

Học sinh được xem là hoàn thành chương khi:

- Sử dụng được `sort` mà không phụ thuộc hoàn toàn vào việc chép mẫu.
- Viết được comparator đơn giản và giải thích được comparator đó.
- Biết sắp xếp nhiều tiêu chí.
- Nhận ra ít nhất ba tình huống mà sắp xếp giúp ích.
- Biết khi nào cần lưu vị trí ban đầu.
- Phân tích được ở mức cơ bản vì sao không nên dùng Selection Sort cho dữ liệu lớn.
- Giải được ít nhất một bài biến thể chưa xuất hiện trong ví dụ trên lớp.

## 10. Ghi chú cho giáo viên

Giáo viên không nên biến chương này thành một buổi học thuộc cú pháp `sort`. Cần dành thời gian cho hoạt động “sắp xếp bằng tay”, tracing và câu hỏi “sau khi sắp xếp thì ta được lợi gì?”.

Selection Sort chỉ nên được sử dụng như chiếc cầu trực quan để học sinh thấy quá trình chọn và đổi chỗ. Trong các bài có giới hạn lớn, cần hướng học sinh tới `sort` chuẩn của C++ và phân tích độ phức tạp.

Khi học sinh quên `vector`, vòng lặp hoặc comparator, hãy đưa các em về hộp **Ôn nhanh Level 0** thay vì viết lại toàn bộ phần lý thuyết trong chương. Việc nhắc lại ngắn, đúng thời điểm sẽ giúp kiến thức cũ được củng cố qua sử dụng thực tế.

## 11. Phần sẽ viết đầy đủ sau khi outline được duyệt

- Lời dẫn nhập của chương.
- Các hình minh họa sắp xếp bằng thẻ.
- Nội dung giảng giải hoàn chỉnh cho 7 buổi.
- 3 bài mẫu có đề, phân tích, pseudocode, code và test.
- Bộ bài tập phân tầng có mã bài và đáp án/gợi ý.
- Phiếu kiểm tra cuối chương.
- Trang tổng kết in cuối chương.
- Bản hướng dẫn giáo viên tương ứng.

---

## Tài liệu tham chiếu nội bộ

Tài liệu này được tạo độc lập trong project để review và không chỉnh sửa knowledge base gốc:

- `IKHEDU_Knowledge_Base.md`
- `Lo_trinh_hoc_tap_bangB_level1.jpg`
- `IKHEDU_Level0_Foundation.md`
