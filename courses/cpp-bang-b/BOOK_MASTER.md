# BOOK_MASTER — iKHEDU C++ Bảng B – Level 1

> **Trạng thái bản thảo:** `draft`  
> Đây là bản thảo canonical của cuốn sách. Các file lesson là artifact chi tiết để biên soạn và kiểm tra; nội dung phát hành cần được đồng bộ vào file này sau mỗi vòng review.

## Publication metadata

| Trường | Giá trị |
|---|---|
| Title | iKHEDU C++ Bảng B – Level 1 |
| Subtitle | Nền tảng tư duy lập trình và thuật toán cơ bản |
| Edition/version | Draft 0.1.0 |
| Author/editor | Chủ biên iKHEDU; Manus AI hỗ trợ biên soạn |
| Audience/level | Học sinh bắt đầu từ số 0 hoặc đang xây nền tảng C++; tuyến Bảng B – Level 1 |
| Language | Tiếng Việt; giữ thuật ngữ C++/English khi cần |
| Output target | `print` / `digital` |
| Book root | `courses/cpp-bang-b/` |
| Source IDs | `SRC-001`, `SRC-002`, `SRC-004` |
| Status | `draft` |

## Mục lục

- [Lời nói đầu](#lời-nói-đầu)
- [Cách sử dụng sách](#cách-sử-dụng-sách)
- [Phần 0 — Cách học và tư duy giải bài](#phần-0--cách-học-và-tư-duy-giải-bài)
- [Phần 1 — Level 0: Nền tảng C++ và tư duy lập trình](#phần-1--level-0-nền-tảng-c-và-tư-duy-lập-trình)
  - [Bản đồ kiến thức Level 0](#bản-đồ-kiến-thức-level-0)
  - [Bộ viên gạch tư duy cơ bản](#bộ-viên-gạch-tư-duy-cơ-bản)
  - [Quick Reference](#quick-reference)
- [Phần 2 — Level 1: Thuật toán cơ bản](#phần-2--level-1-thuật-toán-cơ-bản)
  - [Chương 1 — Sắp xếp](#chương-1--sắp-xếp)
- [Thuật ngữ](#thuật-ngữ)
- [Tài liệu tham khảo](#tài-liệu-tham-khảo)
- [Phụ lục: Artifact hỗ trợ và quy tắc cập nhật](#phụ-lục-artifact-hỗ-trợ-và-quy-tắc-cập-nhật)

# Lời nói đầu

Cuốn sách này được xây dựng cho học sinh học lập trình theo hướng hiểu bản chất và có thể tự giải bài, không chỉ sao chép một đoạn code mẫu. Mỗi thuật toán được trình bày như một cách tổ chức các viên gạch nền tảng đã học: dữ liệu, biến, điều kiện, vòng lặp, so sánh, hàm, kiểm thử và phân tích tốc độ.

Học sinh có thể quên một phần kiến thức cũ sau khi học xong một chương. Điều đó được dự liệu trong thiết kế sách. Level 0 cung cấp nền tảng và bảng tra cứu; mỗi chương Level 1 gọi lại đúng kiến thức cần dùng; bài tập yêu cầu học sinh vận dụng và chuyển giao sang bối cảnh mới.

> Mục tiêu của sách không phải là làm cho học sinh nhớ mọi thứ ngay lần đầu, mà là giúp các em biết **cần nhớ gì, cần hỏi gì và cần tra ở đâu** khi gặp một bài toán mới.

# Cách sử dụng sách

Mỗi chương nên được học theo chu trình:

```text
Ôn nhanh kiến thức cũ
        ↓
Hiểu vấn đề mới
        ↓
Làm ví dụ nhỏ bằng tay
        ↓
Viết ý tưởng và pseudocode
        ↓
Viết code có hướng dẫn
        ↓
Tự làm bài biến thể
        ↓
Kiểm thử và tự giải thích
```

Khi quên cú pháp, học sinh có thể xem lại Level 0 hoặc Quick Reference. Khi quên cách nhận dạng thuật toán, học sinh quay lại phần “Khi nào dùng?” và “Câu hỏi tự kiểm tra” của chương tương ứng. Giáo viên nên ưu tiên hỏi học sinh về dữ liệu, mục tiêu và bước xử lý trước khi cho xem code.

Các bài học trong sách không mặc định yêu cầu học sinh phải biết toàn bộ công cụ C++ nâng cao. Mỗi chương cần nêu rõ prerequisite và tránh đưa nhiều khái niệm mới vào cùng một ví dụ.

# Phần 0 — Cách học và tư duy giải bài

## 0.1. Quy trình sáu câu hỏi

Trước khi viết code, hãy trả lời:

1. Đề bài cho dữ liệu gì?
2. Cần in hoặc tìm kết quả gì?
3. Dữ liệu sẽ được lưu ở biến, mảng, `vector` hay cấu trúc nào?
4. Có công thức hoặc quy tắc nào cần viết ra trước không?
5. Các bước xử lý được thực hiện một lần hay lặp lại nhiều lần?
6. Làm thế nào để kiểm tra kết quả trên test nhỏ và test biên?

Mô hình chung là:

```text
Input → Process → Output
```

Một lời giải tốt phải giải thích được cả ba phần, không chỉ có code chạy được.

## 0.2. Công thức trước code

Với bài toán tính tổng, hãy viết `sum = a + b` trước khi chuyển thành C++. Với bài toán có nhiều bước, hãy viết các bước bằng lời hoặc pseudocode. Việc này giúp tách lỗi toán học, lỗi thuật toán và lỗi cú pháp.

## 0.3. Debug là một phần của lời giải

Khi chương trình sai, không đoán ngẫu nhiên. Hãy kiểm tra một test rất nhỏ, in giá trị trung gian nếu cần, kiểm tra số lần lặp, chỉ số, điều kiện dừng và kiểu dữ liệu. Sau khi sửa, phải chạy lại test cũ và thêm một test mới.

# Phần 1 — Level 0: Nền tảng C++ và tư duy lập trình

Level 0 là lớp kiến thức tham chiếu được dùng xuyên suốt Level 1. Học sinh không nhất thiết phải học thuộc toàn bộ trong một lần; các em cần biết cách quay lại đúng mục khi quên.

## Bản đồ kiến thức Level 0

| Nhóm | Kiến thức cốt lõi | Năng lực cần đạt |
|---|---|---|
| Chương trình đầu tiên | `main`, biên dịch, chạy chương trình | Viết và chạy được chương trình tối giản |
| Input/Output | `cin`, `cout`, dữ liệu đầu vào/đầu ra | Đọc đúng dữ liệu và in đúng format |
| Biến và kiểu dữ liệu | `int`, `long long`, `double`, `char`, `string` | Chọn kiểu phù hợp với dữ liệu |
| Toán tử | số học, so sánh, logic, `%` | Viết được biểu thức và điều kiện |
| Điều kiện | `if`, `else`, điều kiện ghép | Ra quyết định trong chương trình |
| Vòng lặp | `for`, `while` | Lặp một hành động đúng số lần |
| Tích lũy | `sum`, `count`, `max`, `min` | Xử lý dãy dữ liệu bằng một lượt duyệt |
| Mảng và vector | chỉ số, duyệt, cập nhật | Lưu và xử lý nhiều giá trị |
| Hàm | tham số, giá trị trả về | Chia bài toán thành nhiệm vụ nhỏ |
| Debug và kiểm thử | test nhỏ, test biên, giá trị trung gian | Tự tìm và sửa lỗi |
| Độ phức tạp | `O(1)`, `O(N)`, `O(N²)`, `O(N log N)` | Nhận biết lời giải có thể chạy đủ nhanh hay không |

## Cấu trúc chương trình tối giản

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // Đọc dữ liệu.
    // Xử lý dữ liệu.
    // In kết quả.

    return 0;
}
```

Học sinh cần hiểu ý nghĩa của từng phần trước khi sử dụng như một mẫu cố định. `cin` đọc dữ liệu, `cout` in kết quả, còn `main` là nơi chương trình bắt đầu thực hiện.

## Biến, kiểu dữ liệu và toán tử

Biến có thể được hình dung như một chiếc hộp có tên. Kiểu dữ liệu cho biết chiếc hộp được dùng để lưu loại giá trị nào. Với dữ liệu lớn, cần đọc giới hạn trong đề và cân nhắc `long long` thay vì mặc định dùng `int`.

Một số lỗi cần nhớ:

| Lỗi | Cách tự kiểm tra |
|---|---|
| Nhầm `=` với `==` | `=` là gán; `==` là so sánh |
| Nhầm chia nguyên | Kiểm tra kiểu dữ liệu và kết quả khi tử số không chia hết mẫu số |
| Quên dấu ngoặc trong điều kiện ghép | Viết điều kiện thành từng ý bằng lời trước |
| Tràn số | So sánh giới hạn dữ liệu với miền giá trị của kiểu |
| Sai phép chia dư | Nhớ rằng `a % b` là phần dư của phép chia `a` cho `b` |

## Điều kiện và vòng lặp

`if` dùng khi chương trình cần lựa chọn. `for` phù hợp khi biết hoặc mô tả được số lần lặp; `while` phù hợp khi lặp cho đến khi một điều kiện không còn đúng.

```cpp
for (int i = 0; i < n; i++) {
    // Xử lý phần tử thứ i.
}
```

Với mảng hoặc `vector` có `n` phần tử, chỉ số hợp lệ thường là `0` đến `n - 1`. Đây là lý do điều kiện `i < n` thường an toàn hơn `i <= n`.

## Các pattern nền tảng

| Pattern | Mẫu code/ý tưởng | Câu hỏi dẫn đường |
|---|---|---|
| Tính toán | `result = công_thức` | Kết quả được tính từ những dữ liệu nào? |
| Kiểm tra | `if (condition)` | Khi nào điều kiện đúng? |
| Duyệt | Vòng lặp qua từng phần tử | Có cần xử lý mọi phần tử không? |
| Đếm | `count++` | Một phần tử có thỏa điều kiện không? |
| Cộng dồn | `sum += x` | Kết quả được tích lũy qua các phần tử thế nào? |
| Cập nhật lớn nhất/nhỏ nhất | `max`, `min` | Kết quả tốt nhất hiện tại là gì? |
| Tìm kiếm tuyến tính | Duyệt và dừng khi gặp phần tử phù hợp | Có thể tìm lần lượt từ đầu đến cuối không? |
| Lưu nhiều dữ liệu | Mảng hoặc `vector` | Cần giữ lại bao nhiêu giá trị? |
| Đóng gói | Viết hàm cho một nhiệm vụ | Có thể tách bài thành phần nhỏ hơn không? |
| Kiểm thử | Test nhỏ, test biên, kiểm tra trung gian | Nếu `N=1`, toàn bộ bằng nhau hoặc dữ liệu rất lớn thì sao? |

## Mảng, vector và string

Mảng hoặc `vector` dùng để lưu nhiều giá trị cùng loại. Khi xử lý dãy số, học sinh cần phân biệt rõ giá trị của phần tử `a[i]` với vị trí `i`. `vector<int>` là công cụ chính trong các ví dụ cơ bản của chương Sắp xếp.

`string` sẽ được học sâu hơn ở các chuyên đề về xâu. Trong một bài cơ bản, không nên đưa `string` vào chỉ để minh họa một đối tượng có nhiều thuộc tính.

## Hàm và độ phức tạp

Hàm giúp chia chương trình thành các nhiệm vụ nhỏ như `readInput`, `check` hoặc `solve`. Độ phức tạp được dùng để ước lượng số thao tác khi kích thước dữ liệu tăng. Một vòng lặp qua `N` phần tử thường có dạng `O(N)`; hai vòng lặp lồng nhau thường có dạng `O(N²)`; sắp xếp bằng thư viện thường được dùng với mục tiêu `O(N log N)`.

Học sinh cần tập thói quen hỏi: “Nếu dữ liệu lớn gấp đôi thì chương trình có chậm lên khoảng bao nhiêu?”

## Quick Reference

| Cần làm | Nhớ nhanh |
|---|---|
| Đọc `N` số | Tạo `vector<int> a(n)` rồi đọc từng `a[i]` |
| Duyệt dãy | `for (int i = 0; i < n; i++)` |
| Cộng dồn | Khởi tạo `sum = 0`, sau đó `sum += a[i]` |
| Đếm | Khởi tạo `count = 0`, thỏa điều kiện thì `count++` |
| Tìm max/min | Khởi tạo từ phần tử đầu hoặc giá trị phù hợp |
| Đổi chỗ | Dùng `swap(a[i], a[j])` |
| Sắp xếp tăng | `sort(a.begin(), a.end())` |
| Sắp xếp giảm | Dùng comparator rõ ràng sau khi đã hiểu thứ tự cần thiết |
| Kiểm tra mảng | Chú ý chỉ số `0..n-1` và điều kiện biên |
| Debug | Test nhỏ → test biên → kiểm tra trung gian → test lại |

> Trong luồng nhập môn, chỉ dùng các công cụ học sinh đã được xây nền. `struct`, `pair` và cách lưu nhiều thuộc tính là nội dung mở rộng, không phải prerequisite của các bài Sorting cơ bản.

# Phần 2 — Level 1: Thuật toán cơ bản

## Chương 1 — Sắp xếp

### Bản đồ chương

| Trường | Nội dung |
|---|---|
| Mục tiêu | Hiểu sắp xếp là cách tạo trật tự để bước tiếp theo của bài toán dễ hơn |
| Prerequisites | `int`, `vector<int>`, vòng lặp, so sánh, biến tạm, `swap`, `max/min`, complexity cơ bản |
| Phạm vi core | Dãy số nguyên; sắp xếp bằng tay; Selection Sort; `sort`; comparator trên số nguyên; ứng dụng của thứ tự |
| Nội dung mở rộng | Vị trí ban đầu, dữ liệu nhiều thuộc tính, `pair`/`struct` — không bắt buộc trong chương này |
| Số buổi dự kiến | 7 buổi; cần giáo viên chốt trước khi phát hành |
| Trạng thái | `draft` |

### Learning outcomes

Sau chương này, học sinh có thể:

- giải thích sắp xếp là gì và vì sao thay đổi thứ tự có thể làm bài toán đơn giản hơn;
- duyệt và xử lý một `vector<int>`;
- mô phỏng một quy trình sắp xếp đơn giản bằng tay;
- sử dụng `sort` để sắp xếp tăng dần và giảm dần;
- viết comparator cho dãy số nguyên theo một hoặc hai quy tắc;
- nhận biết rằng sắp xếp có thể làm thay đổi vị trí ban đầu;
- phân tích trực giác sự khác nhau giữa `O(N²)` và `O(N log N)`;
- giải thích được sau khi sắp xếp thì bước nào của bài toán trở nên dễ hơn.

### 1. Vì sao cần sắp xếp?

Xét dãy:

```text
8 3 6 1 5
```

Dãy chưa có trật tự khiến ta khó nhìn thấy phần tử nhỏ nhất, phần tử lớn nhất hoặc các giá trị gần nhau. Sau khi sắp xếp tăng dần:

```text
1 3 5 6 8
```

Sắp xếp không tự tạo ra đáp án cuối cùng. Nó tạo ra một trật tự để ta tiếp tục tìm kiếm, kiểm tra phần tử trùng nhau, xét cặp gần nhau, ghép dữ liệu hoặc chuẩn bị cho hai con trỏ.

### 2. Sắp xếp bằng tay và Selection Sort

Với Selection Sort, ở mỗi lượt ta tìm phần tử nhỏ nhất trong phần chưa được xử lý rồi đưa nó về vị trí đầu tiên của phần đó.

```text
Ban đầu: 8 3 6 1 5
Lượt 1:  1 3 6 8 5
Lượt 2:  1 3 6 8 5
Lượt 3:  1 3 5 8 6
Lượt 4:  1 3 5 6 8
```

Pseudocode:

```text
for i từ 0 đến n - 2:
    pos = vị trí phần tử nhỏ nhất trong đoạn i..n-1
    đổi chỗ a[i] và a[pos]
```

Selection Sort phù hợp để học ý tưởng, tracing, vòng lặp lồng nhau và `swap`. Với `N` phần tử, số lần so sánh có dạng `O(N²)`.

### 3. Dùng `sort`

Khi đã hiểu ý tưởng sắp xếp, ta có thể dùng công cụ thư viện:

```cpp
sort(a.begin(), a.end());
```

Lệnh này sắp xếp `vector` theo thứ tự tăng dần. Để sắp xếp giảm dần, cần viết rõ quy tắc thứ tự hoặc dùng cách viết thư viện sau khi học sinh đã hiểu ý nghĩa của comparator.

```cpp
bool greaterValue(int x, int y) {
    return x > y;
}

sort(a.begin(), a.end(), greaterValue);
```

Điều quan trọng không phải là nhớ riêng lệnh `sort`, mà là biết câu trả lời cho câu hỏi: **sắp xếp để làm bước nào tiếp theo?**

### 4. Comparator trên dãy số nguyên

Comparator trả lời câu hỏi: “Trong hai giá trị này, giá trị nào đứng trước?” Hãy viết quy tắc bằng lời trước.

Ví dụ: số chẵn đứng trước số lẻ; trong mỗi nhóm, số nhỏ hơn đứng trước.

```cpp
bool cmp(int x, int y) {
    if (x % 2 != y % 2) {
        return x % 2 < y % 2;
    }
    return x < y;
}
```

Sau đó dùng:

```cpp
sort(a.begin(), a.end(), cmp);
```

Ở phần cơ bản, comparator chỉ làm việc với `int` hoặc biểu thức tính từ `int`. Dữ liệu nhiều thuộc tính và lưu vị trí ban đầu được để cho phần mở rộng sau.

### 5. Khi nào sắp xếp giúp giải bài?

| Dấu hiệu trong đề | Sau khi sắp xếp có thể làm gì? |
|---|---|
| Tìm hai giá trị gần nhau nhất | Chỉ cần xét các phần tử kề nhau |
| Kiểm tra trùng nhau | Các giá trị giống nhau đứng cạnh nhau |
| Tìm phần tử nhỏ/lớn | Đưa phần tử cần quan tâm về đầu/cuối |
| Ghép hai danh sách | Chuẩn bị cho việc di chuyển hai con trỏ |
| Tìm kiếm trên dữ liệu có thứ tự | Chuẩn bị cho Binary Search |
| Chọn theo thứ tự ưu tiên | Chuẩn bị cho tư duy Greedy |

Ví dụ, sau khi sắp xếp dãy tăng dần, khoảng cách nhỏ nhất giữa hai giá trị phải xuất hiện giữa một cặp phần tử kề nhau. Nhờ vậy, ta không cần xét mọi cặp.

### 6. Khi nào không cần sắp xếp?

Nếu chỉ cần tìm giá trị lớn nhất một lần, duyệt dãy và giữ `max` có thể đủ:

```cpp
int mx = a[0];
for (int x : a) {
    mx = max(mx, x);
}
```

Không nên sắp xếp chỉ vì biết lệnh `sort`. Hãy xác định mục đích của bước sắp xếp trước.

### 7. Độ phức tạp

Selection Sort có độ phức tạp `O(N²)`. Sắp xếp thư viện thường được dùng với mục tiêu `O(N log N)`. Học sinh cần hiểu đây là cách so sánh tốc độ tăng theo kích thước dữ liệu, không phải một con số thời gian cố định.

### 8. Nội dung mở rộng: vị trí ban đầu và dữ liệu nhiều thuộc tính

Sắp xếp có thể làm thay đổi vị trí ban đầu của phần tử. Trong chương cơ bản, ta chỉ quan tâm đến giá trị sau khi sắp xếp. Nếu một bài toán yêu cầu giữ vị trí gốc hoặc sắp xếp một đối tượng theo nhiều thuộc tính, học sinh sẽ cần học thêm cách tổ chức nhiều thông tin cho một phần tử.

Nội dung này không thuộc luồng bắt buộc của chương nhập môn Sorting. Không dùng `pair` hoặc `struct` trong các ví dụ cơ bản của chương.

### 9. Quy trình giải một bài Sorting

```text
Đọc đề
→ xác định dữ liệu và kết quả
→ thử cách làm trực tiếp
→ hỏi sắp xếp có làm bước sau dễ hơn không
→ mô tả quy tắc bằng lời
→ viết pseudocode
→ viết code
→ test nhỏ và test biên
→ phân tích độ phức tạp
→ giải thích lại bằng lời
```

### 10. Lịch học đề xuất

| Buổi | Nội dung | Sản phẩm học tập |
|---:|---|---|
| 1 | Vì sao cần sắp xếp; sắp xếp bằng tay; ôn mảng và so sánh | Pseudocode |
| 2 | Selection Sort; tracing từng lượt; `swap` | Bảng tracing và code mô phỏng |
| 3 | `sort` tăng/giảm; iterator và output | Ba bài code ngắn |
| 4 | Comparator trên số nguyên | Một comparator có hai quy tắc |
| 5 | Sắp xếp như bước tiền xử lý | Bài mẫu khoảng cách nhỏ nhất |
| 6 | Bài tập phân tầng và sửa code sai | Bài độc lập |
| 7 | Kiểm tra và bài chuyển giao | Lời giải mới kèm giải thích |

### 11. Tóm tắt chương

> **Sắp xếp không chỉ là đổi vị trí các phần tử. Sắp xếp là cách tạo ra trật tự để nhìn thấy cấu trúc của bài toán.**

| Cần nhớ | Nội dung |
|---|---|
| Tăng dần | `sort(a.begin(), a.end())` |
| Comparator | Quy tắc quyết định phần tử nào đứng trước |
| Mục đích | Tạo trật tự để tìm, ghép, chọn hoặc kiểm tra |
| Complexity | So sánh cách `O(N²)` với `O(N log N)` |
| Cẩn thận | Chỉ số, khoảng xử lý, thứ tự, kiểu dữ liệu và test biên |
| Giới hạn core | Chỉ dùng `int`, `vector<int>`, vòng lặp, so sánh, `swap`, `sort` |
| Câu hỏi chính | Sắp xếp xong thì bước tiếp theo dễ hơn ở điểm nào? |

### 12. Bài tập cuối chương

Bài tập được chia thành ba tầng để học sinh đi từ thao tác trực tiếp đến chuyển giao:

| Tầng | Mục tiêu | Nội dung tiêu biểu |
|---|---|---|
| A — Củng cố cú pháp | Dùng `sort`, kiểm tra thứ tự và nhận biết giá trị trùng | Sắp xếp tăng/giảm, kiểm tra dãy, đếm giá trị khác nhau |
| B — Vận dụng mẫu | Dùng comparator và nhận ra tác dụng của thứ tự | Số chẵn trước số lẻ, sắp xếp theo trị tuyệt đối, khoảng cách nhỏ nhất, gom nhóm |
| C — Chuyển giao | Kết hợp Sorting với ý tưởng khác | Ghép hai danh sách, hai con trỏ, Greedy và bài hỏi có cần sắp xếp không |

Bộ bài tập đầy đủ nằm ở [`lessons/level1-01-sap-xep/Bai_Tap.md`](lessons/level1-01-sap-xep/Bai_Tap.md). Trong bản in, các bài sẽ được đồng bộ vào phần bài tập của chương sau khi giáo viên review.

### 13. Code tham chiếu

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    sort(a.begin(), a.end());

    for (int i = 0; i < n; i++) {
        if (i > 0) cout << ' ';
        cout << a[i];
    }
    cout << '\n';

    return 0;
}
```

Bản code này chỉ minh họa một mục tiêu: đọc một dãy số nguyên, sắp xếp tăng dần và in kết quả. File tham chiếu đầy đủ nằm ở [`lessons/level1-01-sap-xep/code_reference.cpp`](lessons/level1-01-sap-xep/code_reference.cpp).

## Thuật ngữ

| Thuật ngữ | Định nghĩa dùng trong sách | Vị trí xuất hiện |
|---|---|---|
| Input | Dữ liệu chương trình nhận vào | Phần 0, Level 0 |
| Output | Kết quả chương trình cần in ra | Phần 0, Level 0 |
| Pattern | Mẫu tư duy hoặc thao tác lặp lại trong nhiều bài | Level 0 |
| Comparator | Quy tắc trả lời phần tử nào đứng trước | Chương 1 |
| Sorting | Sắp xếp dữ liệu theo một trật tự | Chương 1 |
| Selection Sort | Mỗi lượt chọn phần tử phù hợp nhất trong phần chưa xử lý | Chương 1 |
| Iterator | Đối tượng biểu diễn vị trí trong một khoảng dữ liệu | Chương 1; cần giải thích khi dùng |
| Độ phức tạp | Cách mô tả tốc độ tăng số thao tác theo kích thước dữ liệu | Level 0, Chương 1 |
| Test biên | Dữ liệu ở giới hạn hoặc trường hợp đặc biệt | Level 0, mọi chương |

## Tài liệu tham khảo

Các nguồn dưới đây là nguồn tham chiếu nội bộ của project và được giữ nguyên read-only:

1. `SRC-001` — [`IKHEDU_Knowledge_Base.md`](../../IKHEDU_Knowledge_Base.md), nguồn tham chiếu problem catalog, editorial, code và quy ước liên quan.
2. `SRC-002` — [`ikhEdu_foundation_framework_report.md`](../../ikhEdu_foundation_framework_report.md), nguồn định hướng thiết kế nền tảng và Level 1.
3. `SRC-004` — [`Lo_trinh_hoc_tap_bangB_level1.jpg`](../../Lo_trinh_hoc_tap_bangB_level1.jpg), roadmap chủ đề Bảng B – Level 1.
4. `REF-001` — cấu trúc artifact của ebook-ikh, chỉ được dùng làm reference cho cách tổ chức file, không dùng làm source nội dung chuyên môn.

## Phụ lục: Artifact hỗ trợ và quy tắc cập nhật

### Artifact của khóa học

| Artifact | Vai trò |
|---|---|
| `curriculum/level0/IKHEDU_Level0_Foundation.md` | Bản nền tảng chi tiết để tham chiếu |
| `curriculum/level1/IKHEDU_Level1_Textbook_Outline.md` | Outline tổng quát của tuyến Level 1 |
| `lessons/level1-01-sap-xep/README.md` | Điều hướng Module 01 |
| `lessons/level1-01-sap-xep/Ly_Thuyet.md` | Lesson source chi tiết |
| `lessons/level1-01-sap-xep/Bai_Tap.md` | Bộ bài tập chi tiết |
| `lessons/level1-01-sap-xep/code_reference.cpp` | Code tham chiếu |

### Master maintenance rules

Mỗi chương/bài chỉ có một phiên bản nội dung xuất bản trong `BOOK_MASTER.md`. Các file lesson là artifact biên soạn và kiểm tra; khi nội dung lesson được chốt, phần tương ứng trong master phải được cập nhật trong cùng tác vụ.

Không tạo `BOOK_MASTER_2.md`, master riêng cho từng chương hoặc một bản Word/PDF độc lập làm nguồn mới. Word/PDF là artifact dẫn xuất từ master. Trạng thái `print-ready` chỉ được dùng sau khi nội dung đã qua review chuyên môn, kiểm tra bản in và chốt các câu hỏi mở về reviewer, thời lượng, assessment và bản quyền.

### Trạng thái bản thảo

BOOK_MASTER hiện là **bản tích hợp đầu tiên**, gồm phần Level 0 cô đọng và phần Chương 1 – Sắp xếp đã được đơn giản hóa cho học sinh mới. Các chương Level 1 còn lại mới có trong roadmap/outline và sẽ được bổ sung từng chương, không tạo thêm master riêng.
