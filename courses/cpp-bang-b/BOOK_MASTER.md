# iKHEDU C++ Bảng B

## Thông tin xuất bản

| Trường | Giá trị |
|---|---|
| Title | iKHEDU C++ Bảng B |
| Subtitle | Từ nền tảng lập trình đến thuật toán |
| Author | Chủ biên iKHEDU |
| Đối tượng | Học sinh bắt đầu từ số 0 hoặc đang xây nền tảng C++; chương trình Bảng B |
| Language | Tiếng Việt; giữ thuật ngữ C++/English khi cần |

## Mục lục

- [Lời nói đầu](#lời-nói-đầu)
- [Cách sử dụng sách](#cách-sử-dụng-sách)
- [Mở đầu — Cách học và tư duy giải bài](#mở-đầu--cách-học-và-tư-duy-giải-bài)
- [Phần I — Nền tảng lập trình](#phần-i--nền-tảng-lập-trình)
  - [Tổng quan Phần I](#tổng-quan-phần-i)
  - [I.1. Làm quen với chương trình](#i1-làm-quen-với-chương-trình)
  - [I.2. Dữ liệu, biến và phép tính](#i2-dữ-liệu-biến-và-phép-tính)
  - [I.3. Điều kiện và vòng lặp](#i3-điều-kiện-và-vòng-lặp)
  - [I.4. Những viên gạch xử lý dữ liệu](#i4-những-viên-gạch-xử-lý-dữ-liệu)
  - [I.5. Hàm, debug và độ phức tạp](#i5-hàm-debug-và-độ-phức-tạp)
  - [I.6. Bảng tra cứu nhanh](#i6-bảng-tra-cứu-nhanh)
- [Phần II — Thuật toán nền tảng](#phần-ii--thuật-toán-nền-tảng)
  - [Bản đồ thuật toán](#bản-đồ-thuật-toán)
  - [Chương 1 — Sắp xếp](#chương-1--sắp-xếp)
    - [Bài 1.1 — Vì sao cần sắp xếp và sắp xếp bằng tay](#bài-11--vì-sao-cần-sắp-xếp-và-sắp-xếp-bằng-tay)
    - [Bài 1.2 — Selection Sort: ý tưởng, mô phỏng và `swap`](#bài-12--selection-sort-ý-tưởng-mô-phỏng-và-swap)
    - [Bài 1.3 — Sử dụng `sort` để sắp xếp tăng dần và giảm dần](#bài-13--sử-dụng-sort-để-sắp-xếp-tăng-dần-và-giảm-dần)
    - [Bài 1.4 — Comparator trên dãy số nguyên](#bài-14--comparator-trên-dãy-số-nguyên)
    - [Bài 1.5 — Sắp xếp như một bước tiền xử lý](#bài-15--sắp-xếp-như-một-bước-tiền-xử-lý)
    - [Bài 1.6 — Độ phức tạp và quy trình giải bài](#bài-16--độ-phức-tạp-và-quy-trình-giải-bài)
    - [Bài 1.7 — Ôn tập, kiểm tra và bài chuyển giao](#bài-17--ôn-tập-kiểm-tra-và-bài-chuyển-giao)
    - [Tổng kết chương](#tổng-kết-chương)
    - [Code tham chiếu](#code-tham-chiếu)
  - [Chương 2 — Tham lam](#chương-2--tham-lam)
  - [Chương 3 — Số học](#chương-3--số-học)
  - [Chương 4 — Đếm phân phối](#chương-4--đếm-phân-phối)
  - [Chương 5 — Tìm kiếm nhị phân](#chương-5--tìm-kiếm-nhị-phân)
  - [Chương 6 — Mảng tiền tố](#chương-6--mảng-tiền-tố)
  - [Chương 7 — Hai con trỏ](#chương-7--hai-con-trỏ)
  - [Chương 8 — Xử lý xâu cơ bản](#chương-8--xử-lý-xâu-cơ-bản)
  - [Chương 9 — Đệ quy và chia để trị](#chương-9--đệ-quy-và-chia-để-trị)
  - [Chương 10 — Modulo](#chương-10--modulo)
  - [Chương 11 — Tổ hợp cơ bản](#chương-11--tổ-hợp-cơ-bản)
  - [Chương 12 — STL C++](#chương-12--stl-c)
  - [Chương 13 — Quy hoạch động cơ bản](#chương-13--quy-hoạch-động-cơ-bản)
  - [Chương 14 — Đồ thị](#chương-14--đồ-thị)
  - [Chương 15 — Stack và Queue](#chương-15--stack-và-queue)
  - [Chương 16 — Segment Tree](#chương-16--segment-tree)
  - [Chương 17 — Digit DP](#chương-17--digit-dp)
  - [Chương 18 — String Hashing](#chương-18--string-hashing)
  - [Chương 19 — Số nguyên lớn](#chương-19--số-nguyên-lớn)
  - [Chương 20 — Phép toán trên bit](#chương-20--phép-toán-trên-bit)
  - [Chương 21 — Fenwick Tree](#chương-21--fenwick-tree)
- [Thuật ngữ](#thuật-ngữ)
- [Tài liệu tham khảo](#tài-liệu-tham-khảo)
- [Phụ lục: Bảng tra cứu cuối sách](#phụ-lục-bảng-tra-cứu-cuối-sách)

# Lời nói đầu

Lập trình thi đấu và khoa học máy tính không bắt đầu từ những dòng mã phức tạp, mà bắt đầu từ tư duy giải quyết vấn đề. Cuốn sách **"iKHEDU C++ Bảng B — Từ nền tảng lập trình đến thuật toán"** được biên soạn với một mục tiêu xuyên suốt: **giúp học sinh hiểu rõ bản chất của từng kỹ thuật và có thể tự mình tìm ra lời giải**, thay vì chỉ ghi nhớ máy móc hay sao chép các đoạn mã mẫu có sẵn.

Học lập trình là một hành trình xây dựng năng lực liên tục. Cuốn sách này được thiết kế theo một lộ trình liền mạch, dẫn dắt các em qua từng chặng đường:

- **Nền tảng lập trình:** Bắt đầu từ cách một chương trình hoạt động, cách tổ chức dữ liệu, biến, điều kiện, vòng lặp cho đến kỹ năng chia nhỏ bài toán bằng hàm, gỡ lỗi (debug) và ước lượng độ phức tạp.
- **Những viên gạch tư duy:** Khái quát các mẫu xử lý cốt lõi lặp lại trong mọi bài toán — như đếm tần suất, tích lũy cộng dồn, cập nhật lớn nhất/nhỏ nhất, tìm kiếm trực tiếp và mô hình hóa bài toán.
- **Thuật toán nền tảng:** Làm chủ các phương pháp kinh điển trong lập trình thi đấu như Sắp xếp, Tham lam, Tìm kiếm nhị phân, Mảng tiền tố, Hai con trỏ, Xử lý xâu và Đệ quy – Chia để trị.
- **Chuyên đề mở rộng:** Khám phá các cấu trúc dữ liệu và kỹ thuật nâng cao như Quy hoạch động, Đồ thị, Cây phân đoạn (Segment Tree), Cây chỉ số nhị phân (Fenwick Tree), Băm xâu (String Hashing) và Phép toán trên bit.

Trong thực tế, việc học sinh quên cú pháp hoặc lúng túng khi gặp một bài toán mới là điều hoàn toàn tự nhiên. Cuốn sách đã được tính toán kỹ lưỡng cho trải nghiệm này: mỗi chương thuật toán đều có phần **Ôn nhanh kiến thức nền**, phân tích trực giác từ ví dụ nhỏ bằng tay, bảng nhận diện **"Khi nào nên dùng?"**, bộ bài tập phân tầng và hệ thống **Bảng tra cứu cuối sách** để hỗ trợ tra cứu tức thì.

> Mục tiêu của cuốn sách không phải là biến học sinh thành cỗ máy học thuộc lòng, mà là rèn luyện phản xạ tư duy vững vàng: **Cần nhớ gì, cần hỏi gì và cần tra ở đâu** khi đối diện với một bài toán chưa từng gặp.

Chúng tôi hy vọng cuốn sách sẽ là người bạn đồng hành tin cậy của các em học sinh trên con đường chinh phục các kỳ thi Tin học, đồng thời hỗ trợ Quý Thầy Cô trong việc tổ chức bài giảng, phân tầng bài tập và truyền cảm hứng tư duy khoa học.

Chúc các em có một hành trình học tập đầy say mê và vững bước!

*— Ban chuyên môn iKHEDU —*

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

Khi quên cú pháp, học sinh có thể xem lại các mục tương ứng trong Phần I hoặc Bảng tra cứu nhanh. Khi quên cách nhận dạng thuật toán, học sinh quay lại phần “Khi nào dùng?” và “Câu hỏi tự kiểm tra” của chương tương ứng.
 Giáo viên nên ưu tiên hỏi học sinh về dữ liệu, mục tiêu và bước xử lý trước khi cho xem code.

Các bài học trong sách không mặc định yêu cầu học sinh phải biết toàn bộ công cụ C++ nâng cao. Mỗi chương cần nêu rõ prerequisite và tránh đưa nhiều khái niệm mới vào cùng một ví dụ.

# Mở đầu — Cách học và tư duy giải bài

## Quy trình sáu câu hỏi

Trước khi viết code, hãy trả lời:

1. Đề bài cho dữ liệu gì?
2. Cần in hoặc tìm kết quả gì?
3. Dữ liệu sẽ được lưu ở biến, mảng hay `vector` nào phù hợp?
4. Có công thức hoặc quy tắc nào cần viết ra trước không?
5. Các bước xử lý được thực hiện một lần hay lặp lại nhiều lần?
6. Làm thế nào để kiểm tra kết quả trên test nhỏ và test biên?

Mô hình chung là:

```text
Input → Process → Output
```

Một lời giải tốt phải giải thích được cả ba phần, không chỉ có code chạy được.

## Công thức trước code

Với bài toán tính tổng, hãy viết `sum = a + b` trước khi chuyển thành C++. Với bài toán có nhiều bước, hãy viết các bước bằng lời hoặc pseudocode. Việc này giúp tách lỗi toán học, lỗi thuật toán và lỗi cú pháp.

## Debug là một phần của lời giải

Khi chương trình sai, không đoán ngẫu nhiên. Hãy kiểm tra một test rất nhỏ, in giá trị trung gian nếu cần, kiểm tra số lần lặp, chỉ số, điều kiện dừng và kiểu dữ liệu. Sau khi sửa, phải chạy lại test cũ và thêm một test mới.

# Phần I — Nền tảng lập trình

Phần này cung cấp lớp kiến thức nền được dùng xuyên suốt các chương thuật toán. Học sinh không nhất thiết phải học thuộc toàn bộ trong một lần; các em cần biết cách quay lại đúng mục khi quên.

## Tổng quan Phần I

Phần I cung cấp những kiến thức tối thiểu để học sinh có thể đọc đề, viết chương trình, xử lý dữ liệu đơn giản và tự kiểm tra lời giải. Các mục dưới đây là bản đồ tra cứu; những kiến thức này sẽ được nhắc lại đúng lúc trong các chương thuật toán, không yêu cầu học sinh ghi nhớ tất cả ngay từ đầu.

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

## I.1. Làm quen với chương trình

Chương này giúp học sinh hiểu một chương trình bắt đầu từ đâu, nhận dữ liệu như thế nào, xử lý ra sao và in kết quả ở đâu.

### Cấu trúc chương trình tối giản

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

## I.2. Dữ liệu, biến và phép tính

Biến có thể được hình dung như một chiếc hộp có tên. Kiểu dữ liệu cho biết chiếc hộp được dùng để lưu loại giá trị nào. Với dữ liệu lớn, cần đọc giới hạn trong đề và cân nhắc `long long` thay vì mặc định dùng `int`.

Một số lỗi cần nhớ:

| Lỗi | Cách tự kiểm tra |
|---|---|
| Nhầm `=` với `==` | `=` là gán; `==` là so sánh |
| Nhầm chia nguyên | Kiểm tra kiểu dữ liệu và kết quả khi tử số không chia hết mẫu số |
| Quên dấu ngoặc trong điều kiện ghép | Viết điều kiện thành từng ý bằng lời trước |
| Tràn số | So sánh giới hạn dữ liệu với miền giá trị của kiểu |
| Sai phép chia dư | Nhớ rằng `a % b` là phần dư của phép chia `a` cho `b` |

## I.3. Điều kiện và vòng lặp

`if` dùng khi chương trình cần lựa chọn. `for` phù hợp khi biết hoặc mô tả được số lần lặp; `while` phù hợp khi lặp cho đến khi một điều kiện không còn đúng.

```cpp
for (int i = 0; i < n; i++) {
    // Xử lý phần tử thứ i.
}
```

Với mảng hoặc `vector` có `n` phần tử, chỉ số hợp lệ thường là `0` đến `n - 1`. Đây là lý do điều kiện `i < n` thường an toàn hơn `i <= n`.

## I.4. Những viên gạch xử lý dữ liệu

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

### Mảng, vector và string

Mảng hoặc `vector` dùng để lưu nhiều giá trị cùng loại. Khi xử lý dãy số, học sinh cần phân biệt rõ giá trị của phần tử `a[i]` với vị trí `i`. `vector<int>` là công cụ chính trong các ví dụ cơ bản của chương Sắp xếp.

`string` sẽ được học sâu hơn ở các chuyên đề về xâu. Trong một bài cơ bản, không nên đưa `string` vào chỉ để minh họa một đối tượng có nhiều thuộc tính.

## I.5. Hàm, debug và độ phức tạp

Hàm giúp chia chương trình thành các nhiệm vụ nhỏ như `readInput`, `check` hoặc `solve`. Độ phức tạp được dùng để ước lượng số thao tác khi kích thước dữ liệu tăng. Một vòng lặp qua `N` phần tử thường có dạng `O(N)`; hai vòng lặp lồng nhau thường có dạng `O(N²)`; sắp xếp bằng thư viện thường được dùng với mục tiêu `O(N log N)`.

Học sinh cần tập thói quen hỏi: “Nếu dữ liệu lớn gấp đôi thì chương trình có chậm lên khoảng bao nhiêu?”

## I.6. Bảng tra cứu nhanh

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

# Phần II — Thuật toán nền tảng

## Chương 1 — Sắp xếp

### Bản đồ chương

| Trường | Nội dung |
|---|---|
| Mục tiêu | Hiểu sắp xếp là cách tạo trật tự để bước tiếp theo của bài toán dễ hơn |
| Prerequisites | `int`, `vector<int>`, vòng lặp, so sánh, biến tạm, `swap`, `max/min`, complexity cơ bản |
| Phạm vi core | Dãy số nguyên; sắp xếp bằng tay; Selection Sort; `sort`; comparator trên số nguyên; ứng dụng của thứ tự |
| Nội dung mở rộng | Vị trí ban đầu, dữ liệu nhiều thuộc tính, `pair`/`struct` — không bắt buộc trong chương này |
| Số bài | 7 bài học, kết hợp lý thuyết, luyện tập và kiểm tra |

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

### Bài 1.1 — Vì sao cần sắp xếp và sắp xếp bằng tay

Xét dãy:

```text
8 3 6 1 5
```

Dãy chưa có trật tự khiến ta khó nhìn thấy phần tử nhỏ nhất, phần tử lớn nhất hoặc các giá trị gần nhau. Sau khi sắp xếp tăng dần:

```text
1 3 5 6 8
```

Sắp xếp không tự tạo ra đáp án cuối cùng. Nó tạo ra một trật tự để ta tiếp tục tìm kiếm, kiểm tra phần tử trùng nhau, xét cặp gần nhau, ghép dữ liệu hoặc chuẩn bị cho hai con trỏ.

### Bài 1.2 — Selection Sort: ý tưởng, mô phỏng và `swap`

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

### Bài 1.3 — Sử dụng `sort` để sắp xếp tăng dần và giảm dần

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

### Bài 1.4 — Comparator trên dãy số nguyên

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

### Bài 1.5 — Sắp xếp như một bước tiền xử lý

| Dấu hiệu trong đề | Sau khi sắp xếp có thể làm gì? |
|---|---|
| Tìm hai giá trị gần nhau nhất | Chỉ cần xét các phần tử kề nhau |
| Kiểm tra trùng nhau | Các giá trị giống nhau đứng cạnh nhau |
| Tìm phần tử nhỏ/lớn | Đưa phần tử cần quan tâm về đầu/cuối |
| Ghép hai danh sách | Chuẩn bị cho việc di chuyển hai con trỏ |
| Tìm kiếm trên dữ liệu có thứ tự | Chuẩn bị cho Binary Search |
| Chọn theo thứ tự ưu tiên | Chuẩn bị cho tư duy Greedy |

Ví dụ, sau khi sắp xếp dãy tăng dần, khoảng cách nhỏ nhất giữa hai giá trị phải xuất hiện giữa một cặp phần tử kề nhau. Nhờ vậy, ta không cần xét mọi cặp.

#### Khi nào không cần sắp xếp?

Nếu chỉ cần tìm giá trị lớn nhất một lần, duyệt dãy và giữ `max` có thể đủ:

```cpp
int mx = a[0];
for (int x : a) {
    mx = max(mx, x);
}
```

Không nên sắp xếp chỉ vì biết lệnh `sort`. Hãy xác định mục đích của bước sắp xếp trước.

### Bài 1.6 — Độ phức tạp và quy trình giải bài

Selection Sort có độ phức tạp `O(N²)`. Sắp xếp thư viện thường được dùng với mục tiêu `O(N log N)`. Học sinh cần hiểu đây là cách so sánh tốc độ tăng theo kích thước dữ liệu, không phải một con số thời gian cố định.

#### Nội dung mở rộng: vị trí ban đầu và dữ liệu nhiều thuộc tính

Sắp xếp có thể làm thay đổi vị trí ban đầu của phần tử. Trong chương cơ bản, ta chỉ quan tâm đến giá trị sau khi sắp xếp. Nếu một bài toán yêu cầu giữ vị trí gốc hoặc sắp xếp một đối tượng theo nhiều thuộc tính, học sinh sẽ cần học thêm cách tổ chức nhiều thông tin cho một phần tử.

Nội dung này không thuộc luồng bắt buộc của chương nhập môn Sorting. Không dùng `pair` hoặc `struct` trong các ví dụ cơ bản của chương.

#### Quy trình giải một bài Sorting

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

#### Lịch học gợi ý

| Buổi | Nội dung | Sản phẩm học tập |
|---:|---|---|
| 1 | Vì sao cần sắp xếp; sắp xếp bằng tay; ôn mảng và so sánh | Pseudocode |
| 2 | Selection Sort; tracing từng lượt; `swap` | Bảng tracing và code mô phỏng |
| 3 | `sort` tăng/giảm; iterator và output | Ba bài code ngắn |
| 4 | Comparator trên số nguyên | Một comparator có hai quy tắc |
| 5 | Sắp xếp như bước tiền xử lý | Bài mẫu khoảng cách nhỏ nhất |
| 6 | Bài tập phân tầng và sửa code sai | Bài độc lập |
| 7 | Kiểm tra và bài chuyển giao | Lời giải mới kèm giải thích |

### Tổng kết chương

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

### Bài 1.7 — Ôn tập, kiểm tra và bài chuyển giao

Bài tập được chia thành ba tầng để học sinh đi từ thao tác trực tiếp đến chuyển giao:

| Tầng | Mục tiêu | Nội dung tiêu biểu |
|---|---|---|
| A — Củng cố cú pháp | Dùng `sort`, kiểm tra thứ tự và nhận biết giá trị trùng | Sắp xếp tăng/giảm, kiểm tra dãy, đếm giá trị khác nhau |
| B — Vận dụng mẫu | Dùng comparator và nhận ra tác dụng của thứ tự | Số chẵn trước số lẻ, sắp xếp theo trị tuyệt đối, khoảng cách nhỏ nhất, gom nhóm |
| C — Chuyển giao | Kết hợp Sorting với ý tưởng khác | Ghép hai danh sách, hai con trỏ, Greedy và bài hỏi có cần sắp xếp không |

Bộ bài tập cuối chương được trình bày theo ba tầng: củng cố cú pháp, vận dụng mẫu và chuyển giao. Giáo viên có thể chọn số lượng bài phù hợp với thời lượng lớp học.

### Code tham chiếu

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

Đoạn code này chỉ minh họa một mục tiêu: đọc một dãy số nguyên, sắp xếp tăng dần và in kết quả. Học sinh nên thử thay đổi dữ liệu đầu vào và dự đoán kết quả trước khi chạy chương trình.

## Bản đồ thuật toán

Bản đồ thuật toán gồm các nhóm thuật toán và cấu trúc dữ liệu từ nền tảng đến cầu nối nâng cao.
 Danh sách dưới đây là bản đồ phạm vi; giáo viên có thể thay đổi thứ tự dạy khi trình độ lớp học hoặc mục tiêu kỳ thi yêu cầu.

| Cụm | Chương | Quan hệ prerequisite chính |
|---|---|---|
| Nền tảng xử lý dãy | 1–7 | phần nền tảng, mảng, vòng lặp, tích lũy, sắp xếp |
| Xâu và tư duy chia nhỏ | 8–9 | vòng lặp, hàm, `string`, complexity |
| Số học và đếm | 3, 10–11 | toán tử, modulo, tích lũy, đệ quy |
| Công cụ dữ liệu | 12, 15 | `vector`, tư duy thứ tự truy cập |
| Mô hình hóa trạng thái | 13–14 | mảng, hàm, queue, graph traversal |
| Cầu nối nâng cao | 16–21 | đệ quy, prefix/query, complexity và các cấu trúc dữ liệu phù hợp |

Teaching sequence khuyến nghị cho lớp bắt đầu từ số 0 là: **Đếm và thống kê → Sắp xếp → Mảng tiền tố → Hai con trỏ → Tham lam → Tìm kiếm nhị phân → Xử lý xâu → Stack/Queue → Số học/Modulo → Đệ quy → Tổ hợp → Quy hoạch động → Đồ thị → Bitmask → STL nâng cao**. Segment Tree, Digit DP, String Hashing, số nguyên lớn và Fenwick Tree nên được dạy như các chương cầu nối sau khi học sinh đã vững các phần trước.

## Chương 2 — Tham lam

### Mục tiêu và ôn nhanh

Học sinh nhận ra bài toán trong đó một quyết định tốt ở hiện tại có thể dẫn tới lời giải tối ưu toàn cục, đồng thời biết khi nào không được dùng tham lam. Ôn lại Sorting, so sánh, `max/min`, vòng lặp và cách mô tả quy tắc lựa chọn bằng lời.

### Ý tưởng cốt lõi

Thuật toán tham lam xây dựng lời giải từng bước. Ở mỗi bước, ta chọn phương án có vẻ tốt nhất theo một tiêu chí đã xác định, sau đó chứng minh rằng lựa chọn đó không làm mất lời giải tối ưu. Ví dụ kinh điển là chọn nhiều hoạt động không giao nhau: sắp xếp theo thời điểm kết thúc sớm nhất, chọn hoạt động hợp lệ đầu tiên và lặp lại.

```text
Sắp xếp theo tiêu chí phù hợp
→ chọn phương án hợp lệ tốt nhất
→ cập nhật trạng thái
→ lặp lại
```

### Cần phân biệt

Không phải bài toán nào có câu “chọn lớn nhất” hoặc “chọn nhỏ nhất” cũng dùng được tham lam. Học sinh phải thử phản ví dụ nhỏ. Nếu một lựa chọn hiện tại có thể ảnh hưởng phức tạp đến tương lai, cần cân nhắc DP hoặc tìm kiếm.

### Bài tập và lỗi thường gặp

Bài tập nên đi từ chọn hoạt động, đổi tiền với hệ mệnh giá đặc biệt, xếp lịch và ghép đoạn. Lỗi phổ biến là chọn theo thời điểm bắt đầu thay vì kết thúc, không chứng minh tiêu chí, hoặc quên sắp xếp trước khi chọn. Về sau, tư duy này được dùng trong scheduling, MST và nhiều bài tối ưu cục bộ.

## Chương 3 — Số học

### Mục tiêu và ôn nhanh

Học sinh sử dụng được ước, bội, số nguyên tố, GCD và LCM trong các bài đơn giản. Ôn vòng lặp, `%`, hàm và `long long`.

### Ý tưởng cốt lõi

GCD có thể tính hiệu quả bằng thuật toán Euclid:

```text
gcd(a, b) = gcd(b, a % b)
```

Lặp đến khi `b = 0`; khi đó kết quả là `a`. LCM thường liên hệ với GCD:

```text
lcm(a, b) = a / gcd(a, b) * b
```

Cần chia trước khi nhân để giảm nguy cơ tràn số. Kiểm tra số nguyên tố chỉ cần thử các ước đến khi bình phương vượt quá số đang xét.

### Bài tập và lỗi thường gặp

Luyện GCD nhiều số, đếm ước, kiểm tra nguyên tố và phân tích thừa số nhỏ. Cần chú ý số âm, số 0, `1`, thứ tự phép nhân/chia và giới hạn `long long`. Kiến thức này là nền cho Modulo, Tổ hợp và các bài số học nâng cao.

## Chương 4 — Đếm phân phối

### Mục tiêu và ôn nhanh

Học sinh biết đếm tần suất, phân phối dữ liệu vào các nhóm và dùng nguyên lý Dirichlet ở mức trực giác. Ôn `count`, mảng, `vector` và điều kiện.

### Ý tưởng cốt lõi

Thay vì so sánh mọi cặp, ta lưu số lần xuất hiện của mỗi giá trị hoặc mỗi nhóm. Khi số nhóm ít, một mảng tần suất thường đủ nhanh. Nguyên lý Dirichlet nhắc rằng nếu phân phối nhiều vật vào ít hộp, chắc chắn có hộp nhận từ hai vật trở lên.

```text
Khởi tạo bảng tần suất
→ duyệt từng dữ liệu
→ tăng nhóm tương ứng
→ đọc kết quả từ bảng đếm
```

### Bài tập và lỗi thường gặp

Luyện đếm giá trị trùng, tìm nhóm đông nhất, kiểm tra phân phối và đếm cặp bằng tần suất. Lỗi thường gặp là chọn kích thước bảng sai, quên khởi tạo về 0 và nhầm giá trị với chỉ số. Chương này nối tự nhiên sang Prefix Sum, Map và các bài đếm tổ hợp.

## Chương 5 — Tìm kiếm nhị phân

### Mục tiêu và ôn nhanh

Học sinh hiểu tìm kiếm nhị phân trên dãy đã sắp xếp và nhận ra dạng “tìm đáp án nhỏ nhất/lớn nhất thỏa điều kiện”. Ôn Sorting, comparator, hàm và complexity.

### Ý tưởng cốt lõi

Tìm kiếm nhị phân loại bỏ một nửa miền tìm kiếm sau mỗi lần kiểm tra. Điều kiện quan trọng là tính đơn điệu: khi một giá trị đã thỏa hoặc không thỏa, các giá trị cùng phía phải có hành vi nhất quán.

```text
left = miền trái, right = miền phải
while left <= right:
    mid = (left + right) / 2
    nếu mid phù hợp: lưu đáp án và thu hẹp về phía tốt hơn
    ngược lại: bỏ nửa miền không phù hợp
```

Khi tìm trên đáp án, hãy viết riêng hàm `check(x)` trả lời “x có đủ tốt không?”.

### Bài tập và lỗi thường gặp

Luyện tìm phần tử, vị trí đầu/cuối, căn bậc hai nguyên, năng lực tối thiểu và tốc độ nhỏ nhất. Lỗi thường gặp là áp dụng khi điều kiện không đơn điệu, cập nhật sai biên, vòng lặp không kết thúc hoặc tràn ở `left + right`. Đây là nền cho nhiều bài tối ưu phần thuật toán.

## Chương 6 — Mảng tiền tố

### Mục tiêu và ôn nhanh

Học sinh trả lời nhanh tổng, XOR hoặc số lượng trên nhiều đoạn liên tiếp. Ôn tích lũy, mảng, chỉ số và kiểu dữ liệu.

### Ý tưởng cốt lõi

Tạo mảng tiền tố `P`, trong đó `P[i]` lưu thông tin từ đầu dãy đến vị trí `i`. Với tổng, tổng đoạn từ `l` đến `r` có thể lấy bằng hiệu giữa hai giá trị tiền tố thích hợp.

```text
Tạo P từ trái sang phải
→ mỗi truy vấn đoạn dùng hai giá trị P
→ thời gian mỗi truy vấn giảm xuống O(1)
```

Cần thống nhất dùng chỉ số 0-based hoặc tạo `P[0] = 0` để tránh nhiều trường hợp biên.

### Bài tập và lỗi thường gặp

Luyện tổng đoạn, số phần tử thỏa điều kiện trên đoạn, Prefix XOR và truy vấn hai chiều đơn giản. Lỗi phổ biến là lệch chỉ số, dùng `int` cho tổng lớn và quên rằng tiền tố tĩnh không tự xử lý cập nhật.

## Chương 7 — Hai con trỏ

### Mục tiêu và ôn nhanh

Học sinh duy trì được một đoạn hoặc hai vị trí đang xét mà không duyệt lại dữ liệu không cần thiết. Ôn Sorting, điều kiện, vòng lặp và tính đơn điệu.

### Ý tưởng cốt lõi

Hai con trỏ thường di chuyển từ trái sang phải. Một con trỏ mở rộng đoạn, con trỏ còn lại thu hẹp đoạn khi điều kiện bị vi phạm. Trong bài tìm hai số có tổng bằng `X`, sau khi sắp xếp, ta tăng con trỏ trái khi tổng quá nhỏ và giảm con trỏ phải khi tổng quá lớn.

```text
while left < right:
    kiểm tra đoạn/cặp hiện tại
    di chuyển một con trỏ theo dấu hiệu của điều kiện
```

### Bài tập và lỗi thường gặp

Luyện tìm cặp tổng X, đoạn dài nhất thỏa điều kiện, sliding window và trộn hai dãy đã sắp xếp. Lỗi thường gặp là di chuyển sai con trỏ, dùng kỹ thuật khi điều kiện không đơn điệu và quên kiểm tra đoạn rỗng.

## Chương 8 — Xử lý xâu cơ bản

### Mục tiêu và ôn nhanh

Học sinh duyệt, đếm, so sánh và xây dựng xâu ở mức cơ bản. Ôn vòng lặp, điều kiện, mảng và `string` trong phần nền tảng.

### Ý tưởng cốt lõi

Xâu là một dãy ký tự có thể duyệt bằng chỉ số. Các pattern quan trọng gồm đếm ký tự, kiểm tra đối xứng, tìm đoạn liên tiếp và chuẩn hóa chữ hoa/chữ thường khi đề yêu cầu.

```text
duyệt từng ký tự
→ kiểm tra điều kiện
→ cập nhật bộ đếm/trạng thái
→ kết luận
```

Học sinh cần phân biệt độ dài xâu, chỉ số ký tự và ký tự cuối cùng. Chưa đưa hashing hoặc KMP vào phần cơ bản.

### Bài tập và lỗi thường gặp

Luyện đếm nguyên âm, kiểm tra palindrome, tách từ đơn giản và tìm đoạn liên tiếp dài nhất. Lỗi thường gặp là truy cập ngoài xâu, nhầm khoảng trắng với ký tự chữ và xử lý xâu rỗng không đúng.

## Chương 9 — Đệ quy và chia để trị

### Mục tiêu và ôn nhanh

Học sinh hiểu hàm gọi lại chính nó, điều kiện dừng và cách chia bài toán thành các phần nhỏ hơn. Ôn hàm, vòng lặp và complexity.

### Ý tưởng cốt lõi

Một hàm đệ quy cần có trạng thái nhỏ hơn ở lời gọi tiếp theo và điều kiện dừng rõ ràng. Chia để trị tách bài toán thành các phần, giải từng phần rồi ghép kết quả. Merge Sort là ví dụ điển hình: chia dãy, sắp xếp hai nửa và trộn.

```text
Nếu là trường hợp nhỏ: trả lời trực tiếp
Ngược lại:
    chia bài toán
    giải các phần con
    ghép kết quả
```

### Bài tập và lỗi thường gặp

Luyện tính giai thừa, tổng dãy, tìm kiếm nhị phân, merge sort và lũy thừa nhanh. Lỗi phổ biến là thiếu điều kiện dừng, không làm giảm kích thước bài toán, hoặc dùng đệ quy khi vòng lặp đơn giản hơn.

## Chương 10 — Modulo

### Mục tiêu và ôn nhanh

Học sinh thực hiện phép tính với số lớn bằng phép chia dư và biết các quy tắc cộng, trừ, nhân modulo. Ôn toán tử `%`, `long long` và lũy thừa.

### Ý tưởng cốt lõi

Với mô-đun `M`, ta có thể giảm giá trị sau mỗi phép toán để tránh số trung gian quá lớn:

```text
(a + b) mod M = ((a mod M) + (b mod M)) mod M
(a * b) mod M = ((a mod M) * (b mod M)) mod M
```

Lũy thừa nhanh dùng chia đôi số mũ, giảm số phép nhân từ tuyến tính xuống dạng logarit.

### Bài tập và lỗi thường gặp

Luyện tính lũy thừa modulo, tổng chu kỳ, số chữ số cuối và bài đếm kết quả theo modulo. Cần chú ý số âm, thứ tự `%`, kiểu dữ liệu khi nhân và việc chuẩn hóa kết quả về miền không âm nếu đề yêu cầu.

## Chương 11 — Tổ hợp cơ bản

### Mục tiêu và ôn nhanh

Học sinh nhận ra các bài đếm lựa chọn, sắp xếp và đường đi trên lưới ở mức cơ bản. Ôn tích lũy, đệ quy và modulo.

### Ý tưởng cốt lõi

Tổ hợp đếm số cách chọn không xét thứ tự; chỉnh hợp/hoán vị có xét thứ tự. Tam giác Pascal cho quan hệ:

```text
C(n, k) = C(n - 1, k - 1) + C(n - 1, k)
```

Khi giới hạn nhỏ, bảng động Pascal dễ hiểu và an toàn. Khi giới hạn lớn, cần học thêm tiền xử lý giai thừa và nghịch đảo modulo, nhưng đó là phần nâng cao.

### Bài tập và lỗi thường gặp

Luyện chọn đội, chọn vật, đường đi chỉ sang phải/xuống và đếm cách chia nhỏ. Lỗi phổ biến là nhầm “có xét thứ tự”, sai điều kiện `k > n` và dùng công thức gây tràn số.

## Chương 12 — STL C++

### Mục tiêu và ôn nhanh

Học sinh chọn được công cụ chuẩn phù hợp với nhu cầu: `vector` cho dãy thay đổi kích thước, `set` cho giá trị phân biệt có thứ tự, `map` cho ánh xạ khóa–giá trị, `stack` và `queue` cho quy tắc truy cập đặc biệt.

### Ý tưởng cốt lõi

Không học STL như danh sách lệnh rời rạc. Hãy bắt đầu từ câu hỏi: dữ liệu cần lưu thế nào, cần truy cập theo cách nào và cần thao tác gì nhanh. Các công cụ có chi phí và hành vi khác nhau.

| Công cụ | Dùng khi |
|---|---|
| `vector` | Lưu dãy và truy cập theo chỉ số |
| `set` | Lưu giá trị không trùng và có thứ tự |
| `map` | Đếm hoặc ánh xạ khóa tới giá trị |
| `stack` | Vào sau, ra trước |
| `queue` | Vào trước, ra trước |

`pair` có thể được giới thiệu ở phần STL mở rộng sau khi học sinh đã vững các kiểu dữ liệu cơ bản; không phải prerequisite của Sorting nhập môn.

### Bài tập và lỗi thường gặp

Luyện tần suất bằng `map`, loại trùng bằng `set`, thao tác cuối dãy bằng `stack` và mô phỏng hàng chờ bằng `queue`. Lỗi phổ biến là chọn container theo thói quen, quên kiểm tra phần tử tồn tại và nhầm quy tắc truy cập.

## Chương 13 — Quy hoạch động cơ bản

### Mục tiêu và ôn nhanh

Học sinh biết nhận ra bài toán có các trạng thái lặp lại, định nghĩa trạng thái, công thức chuyển và thứ tự tính. Ôn mảng, vòng lặp, `max/min` và complexity.

### Ý tưởng cốt lõi

Quy hoạch động gồm ba câu hỏi: trạng thái biểu diễn điều gì, từ trạng thái trước chuyển sang trạng thái sau thế nào, và đáp án cuối nằm ở đâu. Ví dụ Fibonacci không nên tính lại cùng một nhánh nhiều lần; lưu kết quả giúp giảm thời gian.

```text
dp[state] = kết quả tốt nhất/số cách của state
khởi tạo trạng thái nhỏ
duyệt theo thứ tự phụ thuộc
cập nhật trạng thái tiếp theo
```

### Bài tập và lỗi thường gặp

Luyện bước đi một hoặc hai bước, dãy con tăng, ba lô 0/1 ở mức nhỏ và đường đi trên lưới. Lỗi thường gặp là định nghĩa trạng thái mơ hồ, khởi tạo sai, duyệt ngược/thuận sai và nhầm “tối ưu” với “đếm số cách”.

## Chương 14 — Đồ thị

### Mục tiêu và ôn nhanh

Học sinh mô hình hóa đối tượng và quan hệ thành đỉnh/cạnh, sau đó duyệt được thành phần liên thông bằng BFS hoặc DFS. Ôn `vector`, vòng lặp, hàm và queue/stack ở mức phù hợp.

### Ý tưởng cốt lõi

Một đồ thị gồm các đỉnh và cạnh. Danh sách kề lưu những đỉnh nối trực tiếp với mỗi đỉnh. DFS đi sâu trước; BFS đi theo từng lớp khoảng cách.

```text
đưa đỉnh bắt đầu vào cấu trúc chờ
đánh dấu khi đưa vào
lấy một đỉnh ra
duyệt các hàng xóm chưa thăm
```

### Bài tập và lỗi thường gặp

Luyện đếm thành phần, kiểm tra đường đi, khoảng cách không trọng số và duyệt mê cung. Lỗi phổ biến là không đánh dấu đã thăm, thêm cạnh một chiều cho đồ thị hai chiều và nhầm số đỉnh với số cạnh.

## Chương 15 — Stack và Queue

### Mục tiêu và ôn nhanh

Học sinh hiểu rằng cách dữ liệu đi vào và đi ra có thể quyết định lời giải. Ôn mảng, vòng lặp và STL nhập môn.

### Ý tưởng cốt lõi

`stack` theo quy tắc vào sau–ra trước, phù hợp với ngoặc đúng, undo và phần tử lớn hơn gần nhất. `queue` theo quy tắc vào trước–ra trước, phù hợp với BFS và mô phỏng hàng chờ.

```text
Stack: push → top → pop
Queue: push → front → pop
```

### Bài tập và lỗi thường gặp

Luyện kiểm tra ngoặc, xóa phần tử theo thứ tự, mô phỏng hàng chờ và BFS đơn giản. Lỗi phổ biến là gọi `top/front` khi rỗng, pop nhầm thời điểm và không xác định rõ thứ tự xử lý trước khi code.

## Chương 16 — Segment Tree

### Mục tiêu và prerequisite

Học sinh làm quen với cấu trúc cây cho truy vấn đoạn và cập nhật điểm. Chỉ học sau khi đã vững mảng tiền tố, đệ quy và độ phức tạp.

### Ý tưởng cốt lõi

Segment Tree chia dãy thành các đoạn lồng nhau. Mỗi nút lưu thông tin tổng, min hoặc max của một đoạn. Truy vấn và cập nhật chỉ đi qua các nhánh liên quan, thường có độ phức tạp `O(log N)`.

```text
build(node, left, right)
update(node, left, right, position, value)
query(node, left, right, queryLeft, queryRight)
```

### Bài tập và lỗi thường gặp

Bắt đầu với tổng đoạn và cập nhật một điểm, sau đó mới đến min/max. Lỗi thường gặp là chia đoạn sai, nhầm đoạn giao nhau hoàn toàn với một phần và quên cập nhật nút cha.

## Chương 17 — Digit DP

### Mục tiêu và prerequisite

Học sinh nhận diện bài đếm các số trong một khoảng khi điều kiện phụ thuộc vào từng chữ số. Đây là chương cầu nối sau DP cơ bản, modulo và đệ quy.

### Ý tưởng cốt lõi

Ta xây số từ trái sang phải với trạng thái thường gồm vị trí chữ số, giới hạn có đang bám tiền tố của số biên hay không, và thông tin cần theo dõi như tổng chữ số hoặc phần dư.

```text
dp[position][tight][state]
```

Khi đã vượt giới hạn ở một vị trí, các vị trí sau được tự do hơn. Cần xử lý số 0 ở đầu một cách nhất quán.

### Bài tập và lỗi thường gặp

Luyện đếm số có tổng chữ số cho trước, không chứa một chữ số và chia hết cho M trong đoạn `[0, X]`. Lỗi phổ biến là thiếu trạng thái `tight`, xử lý số 0 đầu sai và quên lấy hiệu kết quả `F(R) - F(L-1)`.

## Chương 18 — String Hashing

### Mục tiêu và prerequisite

Học sinh hiểu cách biểu diễn xâu bằng giá trị băm để so sánh nhanh các đoạn, sau khi đã vững `string`, mảng tiền tố và modulo.

### Ý tưởng cốt lõi

Gán mỗi ký tự một giá trị và xây hash tiền tố. Hash của một đoạn có thể lấy từ hai hash tiền tố, tương tự Prefix Sum nhưng có phép nhân theo cơ số. Vì có khả năng va chạm, cần hiểu hashing là kỹ thuật xác suất hoặc dùng nhiều mô-đun khi yêu cầu cao.

### Bài tập và lỗi thường gặp

Luyện so sánh hai đoạn, kiểm tra palindrome và đếm xâu con độ dài cố định. Lỗi phổ biến là sai quy ước chỉ số, quên chuẩn hóa modulo và xem hai hash bằng nhau là bằng chứng tuyệt đối trong mọi bối cảnh.

## Chương 19 — Số nguyên lớn

### Mục tiêu và prerequisite

Học sinh xử lý số vượt miền của kiểu chuẩn bằng `string` hoặc mảng chữ số. Chương này cần đặt sau mảng, xâu, phép tính và modulo.

### Ý tưởng cốt lõi

Lưu các chữ số theo thứ tự thuận tiện, thực hiện cộng/trừ/nhân từng chữ số và truyền nhớ giống cách tính tay. Khi cần so sánh, bỏ các số 0 đầu và so độ dài trước.

```text
duyệt từ chữ số thấp lên cao
→ tính tổng cùng phần nhớ
→ lưu chữ số kết quả
→ xử lý phần nhớ còn lại
```

### Bài tập và lỗi thường gặp

Luyện cộng hai số lớn, so sánh, nhân với số nhỏ và tính modulo của xâu. Lỗi phổ biến là giữ số 0 đầu, duyệt sai hướng và quên phần nhớ cuối.

## Chương 20 — Phép toán trên bit

### Mục tiêu và prerequisite

Học sinh biểu diễn trạng thái nhỏ bằng bit và hiểu các phép AND, OR, XOR, NOT, dịch bit. Ôn số nguyên, điều kiện và tập hợp nhỏ.

### Ý tưởng cốt lõi

Mỗi bit có thể biểu diễn một lựa chọn có/không. Một số nguyên vì thế có thể biểu diễn một tập con nhỏ. `mask | (1 << i)` thêm phần tử; `mask & (1 << i)` kiểm tra; `mask ^ (1 << i)` đảo trạng thái.

### Bài tập và lỗi thường gặp

Luyện kiểm tra bit, đếm số bit 1, liệt kê tập con của một tập nhỏ và XOR. Lỗi thường gặp là dịch quá số bit, nhầm `&` với `&&`, và dùng bitmask cho dữ liệu có quá nhiều phần tử.

## Chương 21 — Fenwick Tree

### Mục tiêu và prerequisite

Học sinh làm quen với cấu trúc hỗ trợ cập nhật một điểm và truy vấn tổng tiền tố nhanh. Chương này đặt sau Prefix Sum, bit và complexity.

### Ý tưởng cốt lõi

Fenwick Tree lưu các đoạn có độ dài liên quan đến bit thấp nhất của chỉ số. Hai thao tác chính là cập nhật một điểm và tính tổng từ đầu đến vị trí, đều có độ phức tạp `O(log N)`.

```text
add(index, delta)
→ index += index & -index

prefixSum(index)
→ index -= index & -index
```

### Bài tập và lỗi thường gặp

Bắt đầu với tổng tiền tố động, sau đó mở rộng sang tổng đoạn và đếm nghịch thế. Lỗi phổ biến là nhầm chỉ số 0-based với 1-based, quên nén tọa độ khi giá trị lớn và cập nhật sai hướng.

## Tổng ôn thuật toán

### Bản đồ nhận dạng nhanh

| Dấu hiệu của bài toán | Hướng cần thử |
|---|---|
| Cần đếm hoặc lưu thông tin qua một lượt duyệt | Tần suất, tích lũy, max/min |
| Cần tạo thứ tự để bước sau đơn giản hơn | Sorting |
| Nhiều truy vấn đoạn tĩnh | Prefix Sum/XOR |
| Hai vị trí hoặc một đoạn di chuyển đơn điệu | Two Pointers/Sliding Window |
| Chọn quyết định từng bước | Greedy, nhưng phải tìm phản ví dụ và lập luận |
| Tìm giá trị nhỏ nhất/lớn nhất thỏa điều kiện | Binary Search on Answer |
| Quan hệ giữa các đối tượng | Graph, BFS/DFS |
| Kết quả của trạng thái nhỏ lặp lại | Dynamic Programming |
| Truy cập theo thứ tự vào/ra | Stack/Queue |
| Cập nhật và truy vấn đoạn động | Fenwick/Segment Tree |
| Trạng thái là tập nhỏ | Bitmask |
| So sánh nhiều đoạn xâu | Prefix/Hashing |

### Chu trình tự học

Với mỗi chủ đề, học sinh cần đi qua bốn mức: nhận biết dấu hiệu, mô phỏng bằng tay, viết lời giải có hướng dẫn và tự giải bài biến thể. Chỉ khi giải thích được vì sao thuật toán đúng, độ phức tạp là gì và trường hợp biên nằm ở đâu thì mới xem là đã nắm được chương.

## Thuật ngữ

| Thuật ngữ | Định nghĩa dùng trong sách | Vị trí xuất hiện |
|---|---|---|
| Input | Dữ liệu chương trình nhận vào | Mở đầu, Phần I |
| Output | Kết quả chương trình cần in ra | Mở đầu, Phần I |
| Pattern | Mẫu tư duy hoặc thao tác lặp lại trong nhiều bài | Phần I |
| Comparator | Quy tắc trả lời phần tử nào đứng trước | Chương 1 |
| Sorting | Sắp xếp dữ liệu theo một trật tự | Chương 1 |
| Selection Sort | Mỗi lượt chọn phần tử phù hợp nhất trong phần chưa xử lý | Chương 1 |
| Iterator | Đối tượng biểu diễn vị trí trong một khoảng dữ liệu | Chương 1; cần giải thích khi dùng |
| Độ phức tạp | Cách mô tả tốc độ tăng số thao tác theo kích thước dữ liệu | Phần I, mục I.5 |
| Test biên | Dữ liệu ở giới hạn hoặc trường hợp đặc biệt | Phần I và các chương thuật toán |

## Tài liệu tham khảo

Nội dung cuốn sách được biên soạn theo chương trình iKHEDU C++ Bảng B – phần thuật toán và các nguyên tắc sư phạm của chương trình. Phần tài liệu tham chiếu chuyên môn được quản lý trong hồ sơ biên soạn riêng; bản in dành cho học sinh chỉ giữ lại những nội dung cần thiết để học và tra cứu.

## Phụ lục: Bảng tra cứu cuối sách

### Câu hỏi trước khi viết code

| Câu hỏi | Mục đích |
|---|---|
| Đề bài cho dữ liệu gì? | Xác định input và cách lưu dữ liệu |
| Cần tìm hoặc in gì? | Xác định output |
| Có công thức hay quy tắc nào? | Viết ý tưởng trước khi viết code |
| Có cần duyệt dữ liệu không? | Chọn vòng lặp phù hợp |
| Có cần đếm, cộng dồn hoặc giữ max/min không? | Nhận ra pattern nền tảng |
| Sắp xếp có làm bước sau dễ hơn không? | Nhận ra cơ hội dùng Sorting |
| Dữ liệu lớn đến mức nào? | Ước lượng độ phức tạp |
| Trường hợp nhỏ nhất và lớn nhất là gì? | Tạo test biên |

### Checklist trước khi nộp bài

```text
Đọc lại đề
→ kiểm tra Input/Output
→ thử test nhỏ
→ thử test biên
→ kiểm tra chỉ số
→ kiểm tra kiểu dữ liệu
→ kiểm tra điều kiện dừng
→ kiểm tra output không có chữ thừa
→ tự giải thích ý tưởng bằng lời
```

### Nguyên tắc ghi nhớ

> **Hiểu ý tưởng trước, viết code sau; làm được bài quen thuộc rồi mới chuyển sang bài biến thể.**

> **Không dùng một công cụ chỉ vì đã biết cú pháp của nó. Hãy luôn trả lời: công cụ này giúp bước nào của bài toán trở nên dễ hơn?**

## Ghi chú biên tập

Đây là bản thảo sách đang được hoàn thiện. Các chương tiếp theo sẽ tiếp tục theo cùng cấu trúc: mục tiêu, kiến thức nền, ví dụ, cách làm, bài tập, tự kiểm tra và tóm tắt. Trước khi in chính thức, toàn bộ nội dung cần được giáo viên đọc thử và kiểm tra lại với học sinh.
