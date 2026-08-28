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
    - [Bài 2.1 — Tham lam là gì?](#bài-21--tham-lam-là-gì)
    - [Bài 2.2 — Chọn nhiều hoạt động không giao nhau](#bài-22--chọn-nhiều-hoạt-động-không-giao-nhau)
    - [Bài 2.3 — Sắp xếp theo thời điểm kết thúc và viết code](#bài-23--sắp-xếp-theo-thời-điểm-kết-thúc-và-viết-code)
    - [Bài 2.4 — Vì sao lựa chọn kết thúc sớm là đúng?](#bài-24--vì-sao-lựa-chọn-kết-thúc-sớm-là-đúng)
    - [Bài 2.5 — Khi nào tham lam thất bại?](#bài-25--khi-nào-tham-lam-thất-bại)
    - [Bài 2.6 — Ôn tập và bài chuyển giao](#bài-26--ôn-tập-và-bài-chuyển-giao)
    - [Tổng kết chương](#tổng-kết-chương-1)
    - [Code tham chiếu](#code-tham-chiếu-1)
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
| Kiến thức cần có | Biến, `int`, `vector<int>`, vòng lặp `for`, so sánh, `max/min`, `swap` và cách đọc chỉ số |
| Phạm vi | Sắp xếp bằng tay, Selection Sort, `sort`, comparator trên số nguyên và ứng dụng của thứ tự |
| Số bài | 7 bài học, kết hợp lý thuyết, luyện tập và kiểm tra |

### Learning outcomes

Sau chương này, em có thể:

- giải thích sắp xếp là gì và vì sao thay đổi thứ tự có thể làm bài toán đơn giản hơn;
- đọc, duyệt và xử lý một `vector<int>`;
- mô phỏng Selection Sort bằng tay và viết được phiên bản cơ bản;
- sử dụng `sort` để sắp xếp tăng dần và giảm dần;
- viết comparator cho dãy số nguyên theo một hoặc hai quy tắc;
- nhận biết khi nào sắp xếp làm thay đổi vị trí ban đầu;
- phân biệt một bài cần sắp xếp với một bài chỉ cần duyệt bằng `max/min`;
- giải thích trực giác sự khác nhau giữa `O(N²)` và `O(N log N)`;
- nói rõ sau khi sắp xếp thì bước nào của bài toán trở nên dễ hơn.

---

### Bài 1.1 — Vì sao cần sắp xếp và sắp xếp bằng tay

#### Mục tiêu bài

Sau Bài 1.1, em có thể nhận biết một dãy đã có trật tự hay chưa, mô tả được kết quả cần đạt và tự sắp xếp một dãy nhỏ bằng tay.

#### Khởi động

Cho dãy số:

```text
8 3 6 1 5
```

Nếu chỉ cần tìm số lớn nhất, em có thể duyệt từ trái sang phải và giữ lại giá trị lớn nhất đã gặp. Nhưng nếu cần in **toàn bộ dãy theo thứ tự tăng dần**, việc tìm một giá trị lớn nhất có đủ không?

Câu trả lời là không. Ta cần đưa nhiều phần tử về một trật tự chung.

#### Sắp xếp là gì?

**Sắp xếp** là đưa các phần tử về thứ tự được yêu cầu. Thứ tự đó có thể là:

- tăng dần: từ nhỏ đến lớn;
- giảm dần: từ lớn đến nhỏ;
- hoặc một thứ tự do đề bài quy định.

Ví dụ:

```text
Ban đầu:  8 3 6 1 5
Tăng dần: 1 3 5 6 8
Giảm dần: 8 6 5 3 1
```

Trong phần cơ bản, ta đang sắp xếp **các giá trị nguyên**. Sắp xếp chủ yếu thay đổi vị trí của các phần tử, không tự tạo ra một giá trị mới.

#### Vì sao thứ tự có ích?

Khi dữ liệu còn lộn xộn, ta khó nhìn thấy các mối quan hệ giữa các phần tử. Sau khi sắp xếp, ta có thể:

- đưa giá trị nhỏ nhất về đầu hoặc giá trị lớn nhất về cuối;
- nhận ra các giá trị bằng nhau vì chúng đứng cạnh nhau;
- chỉ cần xét các phần tử kề nhau khi tìm hai giá trị gần nhau;
- ghép hai dãy theo thứ tự;
- chuẩn bị cho tìm kiếm nhị phân, hai con trỏ hoặc tham lam.

> **Sắp xếp thường là bước chuẩn bị. Nó tạo ra trật tự để bước tiếp theo của lời giải trở nên dễ hơn.**

#### Sắp xếp bằng tay

Hãy sắp xếp dãy `8 3 6 1 5` tăng dần bằng cách luôn tìm số nhỏ nhất trong phần còn lại.

```text
Ban đầu: 8 3 6 1 5
```

Số nhỏ nhất của cả dãy là `1`. Đưa `1` về đầu:

```text
Lượt 1: 1 3 6 8 5
```

Bây giờ phần đầu `1` đã đúng vị trí. Trong phần còn lại `3 6 8 5`, số nhỏ nhất là `3`, nên vị trí thứ hai đã đúng. Tiếp tục:

```text
Lượt 2: 1 3 6 8 5
Lượt 3: 1 3 5 8 6
Lượt 4: 1 3 5 6 8
```

Sau mỗi lượt, một vị trí ở bên trái được xác nhận là đúng. Phần đã đúng không cần sắp xếp lại.

#### Tự kiểm tra

1. Dãy `4 2 9 2` sau khi sắp xếp tăng dần là gì?
2. Khi sắp xếp, giá trị của các phần tử có thay đổi không?
3. Vì sao sau khi đã đặt đúng phần tử nhỏ nhất ở vị trí đầu, ta có thể bỏ qua vị trí đó?
4. Hãy nói bằng lời: “Sau khi sắp xếp, em được lợi gì?”

#### Luyện tập ngắn

- Viết ra từng bước khi sắp xếp dãy `7 4 1 6` tăng dần bằng cách chọn phần tử nhỏ nhất.
- Cho dãy `2 2 5 1 3`. Hãy viết kết quả tăng dần và giảm dần.
- Tự tạo một dãy năm số, sau đó giải thích vì sao thứ tự mới giúp em nhìn dãy rõ hơn.

#### Tóm tắt bài

Sắp xếp là đưa dữ liệu về một trật tự phù hợp. Trước khi viết code, em cần biết **sắp xếp theo tiêu chí nào** và **bước sau sẽ dễ hơn ở điểm nào**.

---

### Bài 1.2 — Selection Sort: ý tưởng, mô phỏng và `swap`

#### Mục tiêu bài

Sau Bài 1.2, em có thể mô phỏng Selection Sort, hiểu vai trò của hai vòng lặp và viết code sắp xếp tăng dần bằng cách chọn phần tử nhỏ nhất.

#### Ý tưởng Selection Sort

Selection Sort có thể hiểu bằng câu nói:

> Ở mỗi vị trí, tìm phần tử nhỏ nhất trong phần chưa sắp xếp rồi đưa phần tử đó về vị trí đang xét.

Với dãy:

```text
8 3 6 1 5
```

Ở lượt đầu, ta tìm số nhỏ nhất trong toàn bộ dãy là `1`, sau đó đưa `1` về vị trí `0`.

Ở lượt tiếp theo, vị trí `0` đã đúng nên chỉ tìm trong đoạn từ vị trí `1` đến cuối. Cứ như vậy, phần bên trái ngày càng dài và luôn được sắp xếp đúng.

#### Mô phỏng từng lượt

| Lượt | Vị trí đang đặt | Phần tử nhỏ nhất còn lại | Dãy sau lượt đó |
|---:|---:|---:|---|
| 1 | `0` | `1` | `1 3 6 8 5` |
| 2 | `1` | `3` | `1 3 6 8 5` |
| 3 | `2` | `5` | `1 3 5 8 6` |
| 4 | `3` | `6` | `1 3 5 6 8` |

Trong bảng trên, có lượt phần tử nhỏ nhất đã nằm đúng vị trí nên dãy nhìn như không thay đổi. Điều đó hoàn toàn bình thường.

#### Pseudocode

```text
for i từ 0 đến n - 2:
    pos = i
    for j từ i + 1 đến n - 1:
        nếu a[j] < a[pos]:
            pos = j
    đổi chỗ a[i] và a[pos]
```

Biến `i` chỉ vị trí đang cần đặt. Biến `j` dùng để tìm trong phần còn lại. Biến `pos` ghi nhớ vị trí của phần tử nhỏ nhất đã tìm thấy.

#### Code C++

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    for (int i = 0; i < n - 1; i++) {
        int pos = i;

        for (int j = i + 1; j < n; j++) {
            if (a[j] < a[pos]) {
                pos = j;
            }
        }

        swap(a[i], a[pos]);
    }

    for (int i = 0; i < n; i++) {
        if (i > 0) {
            cout << ' ';
        }
        cout << a[i];
    }
    cout << '\n';

    return 0;
}
```

`swap(a[i], a[pos])` đổi chỗ hai phần tử. Nếu `pos` bằng `i`, lệnh này không làm thay đổi dãy và vẫn an toàn.

#### Điều cần theo dõi khi debug

Khi code sai, em hãy in hoặc ghi ra giấy ba giá trị:

- `i`: vị trí đang được đặt;
- `j`: vị trí đang được kiểm tra;
- `pos`: vị trí nhỏ nhất hiện tại.

Một lỗi phổ biến là viết `j <= n`. Chỉ số cuối cùng của dãy có `n` phần tử là `n - 1`, vì vậy điều kiện đúng là `j < n`.

#### Tự kiểm tra

1. Vì sao vòng ngoài chỉ cần chạy đến `n - 2`?
2. `pos` có ý nghĩa gì?
3. Sau khi kết thúc lượt `i`, phần nào của dãy đã chắc chắn đúng?
4. Với dãy `5 2 4`, hãy ghi giá trị của `pos` ở lượt đầu.
5. Nếu `n = 1`, chương trình có truy cập ngoài mảng không?

#### Luyện tập ngắn

- Mô phỏng Selection Sort cho dãy `6 1 4 2`.
- Sửa code để sắp xếp giảm dần bằng cách tìm phần tử lớn nhất trong phần chưa xử lý.
- Viết một câu giải thích cho nhận xét: “Selection Sort phù hợp để học ý tưởng, nhưng không phải lựa chọn tốt cho dữ liệu rất lớn.”

#### Tóm tắt bài

Selection Sort lặp lại thao tác **tìm phần tử phù hợp nhất rồi đưa về vị trí hiện tại**. Hai vòng lặp giúp ta tìm phần tử đó, còn `swap` giúp đưa nó về đúng chỗ.

---

### Bài 1.3 — Sử dụng `sort` để sắp xếp tăng dần và giảm dần

#### Mục tiêu bài

Sau Bài 1.3, em có thể dùng `sort` trên `vector<int>`, hiểu khoảng `[begin, end)` và sắp xếp tăng dần hoặc giảm dần.

#### Từ thuật toán tự viết đến công cụ thư viện

Selection Sort giúp em hiểu bản chất. Khi giải bài thật, ta thường dùng công cụ có sẵn để code ngắn, rõ và hiệu quả hơn:

```cpp
sort(a.begin(), a.end());
```

Lệnh này sắp xếp toàn bộ `vector<int> a` theo thứ tự tăng dần.

- `a.begin()` biểu diễn vị trí bắt đầu của `a`;
- `a.end()` biểu diễn vị trí ngay sau phần tử cuối;
- khoảng `[a.begin(), a.end())` gồm điểm đầu nhưng không gồm điểm cuối.

Cách viết “không gồm điểm cuối” giúp các thuật toán xử lý khoảng dữ liệu đồng nhất.

#### Ví dụ đầy đủ

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    sort(a.begin(), a.end());

    for (int i = 0; i < n; i++) {
        if (i > 0) {
            cout << ' ';
        }
        cout << a[i];
    }
    cout << '\n';

    return 0;
}
```

Với input:

```text
5
8 3 6 1 5
```

output là:

```text
1 3 5 6 8
```

#### Sắp xếp giảm dần

Có thể viết một comparator đơn giản:

```cpp
bool greaterValue(int x, int y) {
    return x > y;
}
```

Sau đó truyền comparator vào `sort`:

```cpp
sort(a.begin(), a.end(), greaterValue);
```

Ở đây, hàm trả về `true` khi `x` nên đứng trước `y`. Vì số lớn hơn phải đứng trước, dãy được sắp xếp giảm dần.

#### Đừng nhầm `end()` với phần tử cuối

Nếu `a` có `n` phần tử, phần tử cuối là `a[n - 1]`. `a.end()` không phải là một phần tử để truy cập; đó là vị trí ngay sau phần tử cuối.

Vì vậy, ta viết:

```cpp
sort(a.begin(), a.end());
```

chứ không viết:

```cpp
sort(a.begin(), a.end() - 1);
```

Cách viết thứ hai bỏ qua phần tử cuối và thường không cho kết quả mong muốn.

#### Tự kiểm tra

Hoàn thành câu lệnh sau:

```cpp
sort(______, ______);
```

Sau đó trả lời:

1. Đối số thứ nhất biểu diễn vị trí nào?
2. Đối số thứ hai biểu diễn vị trí nào?
3. Muốn giảm dần, comparator phải trả lời thế nào cho hai số `x`, `y`?
4. Với `n = 1`, `sort` có gây lỗi không?

#### Luyện tập ngắn

- Đọc `N` số nguyên và in tăng dần.
- Đọc `N` số nguyên và in giảm dần.
- Viết chương trình kiểm tra kết quả sau khi sắp xếp tăng dần có đúng với dãy đã cho hay không, bằng cách xét từng cặp kề nhau.

#### Tóm tắt bài

`sort` nhận một khoảng dữ liệu. Với toàn bộ `vector`, khoảng đúng là `[a.begin(), a.end())`. Hãy hiểu ý nghĩa của khoảng trước khi học thuộc câu lệnh.

---

### Bài 1.4 — Comparator trên dãy số nguyên

#### Mục tiêu bài

Sau Bài 1.4, em có thể biến một quy tắc bằng lời thành comparator trên `int` và kiểm tra comparator bằng các cặp giá trị cụ thể.

#### Comparator trả lời câu hỏi nào?

Comparator trả lời câu hỏi:

> **Trong hai giá trị `x` và `y`, giá trị nào nên đứng trước?**

Ví dụ, sắp xếp giảm dần nghĩa là số lớn hơn đứng trước:

```cpp
bool cmp(int x, int y) {
    return x > y;
}
```

Không nên bắt đầu bằng việc viết điều kiện ngẫu nhiên. Hãy viết quy tắc bằng lời trước, sau đó chuyển từng quy tắc thành code.

#### Ví dụ: số chẵn trước, số lẻ sau

Quy tắc:

1. Mọi số chẵn đứng trước mọi số lẻ.
2. Trong nhóm số chẵn, số nhỏ hơn đứng trước.
3. Trong nhóm số lẻ, số nhỏ hơn đứng trước.

Code:

```cpp
bool evenFirst(int x, int y) {
    bool xIsEven = (x % 2 == 0);
    bool yIsEven = (y % 2 == 0);

    if (xIsEven != yIsEven) {
        return xIsEven;
    }

    return x < y;
}
```

Sử dụng:

```cpp
sort(a.begin(), a.end(), evenFirst);
```

Với dãy:

```text
5 2 8 1 4 7 3
```

kết quả là:

```text
2 4 8 1 3 5 7
```

Ta đã xử lý tiêu chí chính là nhóm chẵn/lẻ trước, rồi mới xử lý tiêu chí phụ là giá trị tăng dần.

#### Comparator phải nhất quán

Một comparator tốt cần giữ cùng một quy tắc trong mọi lần so sánh. Nếu hai phần tử cùng nhóm, phải luôn dùng cùng tiêu chí phụ. Không được lúc thì cho `x` đứng trước `y`, lúc khác lại cho `y` đứng trước `x` trong cùng điều kiện.

Với mỗi cặp `x`, `y`, hãy tự hỏi:

1. Hai số có thuộc cùng nhóm không?
2. Nếu khác nhóm, nhóm nào đứng trước?
3. Nếu cùng nhóm, tiêu chí phụ là gì?

#### Một ví dụ comparator khác

Sắp xếp theo trị tuyệt đối tăng dần; nếu trị tuyệt đối bằng nhau, số nhỏ hơn đứng trước:

```cpp
bool byAbsoluteValue(int x, int y) {
    long long ax = x;
    long long ay = y;
    if (ax < 0) {
        ax = -ax;
    }
    if (ay < 0) {
        ay = -ay;
    }

    if (ax != ay) {
        return ax < ay;
    }

    return x < y;
}
```

Trong các bài có giới hạn số rất lớn, cần đọc kỹ giới hạn trước khi tính trị tuyệt đối để chọn kiểu dữ liệu phù hợp. Với luồng nhập môn, em hãy tập trung vào cách tách **tiêu chí chính** và **tiêu chí phụ**.

#### Giới hạn của phần cơ bản

Các ví dụ bắt buộc trong chương này chỉ dùng `int` và `vector<int>`. Dữ liệu có nhiều thuộc tính hoặc yêu cầu giữ vị trí ban đầu là nội dung mở rộng, chưa cần đưa vào bài đầu tiên về comparator.

#### Tự kiểm tra

1. Comparator tăng dần trả về `true` trong trường hợp nào?
2. Vì sao ví dụ chẵn trước lẻ cần hai bước kiểm tra?
3. Với `x = 2`, `y = 5`, comparator `evenFirst(x, y)` trả về gì?
4. Nếu tất cả số đều là số lẻ, quy tắc phụ được dùng như thế nào?
5. Hãy viết bằng lời một thứ tự có hai tiêu chí trước khi viết code.

#### Luyện tập ngắn

- Sắp xếp dãy số nguyên giảm dần bằng comparator riêng.
- Sắp xếp số âm và số dương theo trị tuyệt đối tăng dần.
- Sắp xếp theo chữ số hàng đơn vị tăng dần; nếu bằng nhau, số nhỏ hơn đứng trước.

#### Tóm tắt bài

Comparator không phải là một mẹo viết code. Đó là bản dịch của câu trả lời **“ai đứng trước ai?”**. Quy tắc nhiều tiêu chí phải được viết theo thứ tự ưu tiên.

---

### Bài 1.5 — Sắp xếp như một bước tiền xử lý

#### Mục tiêu bài

Sau Bài 1.5, em có thể nhận ra những tình huống mà sắp xếp giúp giảm số trường hợp cần xét và biết khi nào không cần sắp xếp.

#### Tiền xử lý là gì?

**Tiền xử lý** là bước chuẩn bị dữ liệu trước khi thực hiện thao tác chính. Sắp xếp là một bước tiền xử lý phổ biến vì nó làm cho dữ liệu có cấu trúc dễ quan sát hơn.

| Dấu hiệu trong đề | Sau khi sắp xếp có thể làm gì? |
|---|---|
| Tìm hai giá trị gần nhau nhất | Chỉ xét các phần tử kề nhau |
| Kiểm tra giá trị trùng nhau | Các giá trị bằng nhau đứng cạnh nhau |
| Ghép hai danh sách | Di chuyển qua hai dãy theo thứ tự |
| Tìm kiếm nhiều lần | Chuẩn bị cho Binary Search |
| Chọn theo thứ tự ưu tiên | Chuẩn bị cho tư duy Greedy |

#### Bài mẫu: khoảng cách nhỏ nhất

Cho dãy vị trí:

```text
8 3 6 1 5
```

Cần tìm khoảng cách nhỏ nhất giữa hai vị trí khác nhau.

**Cách trực tiếp:** xét mọi cặp, tính hiệu giữa hai vị trí và giữ lại hiệu nhỏ nhất. Cách này có thể cần rất nhiều cặp.

**Câu hỏi tối ưu:** nếu sắp xếp dãy tăng dần, hai vị trí gần nhau nhất có thể nằm cách nhau bởi một phần tử khác không?

Không. Nếu một phần tử nằm giữa hai vị trí, nó sẽ tạo ra một khoảng cách không lớn hơn khoảng cách của hai vị trí ở hai bên. Vì vậy, sau khi sắp xếp, chỉ cần xét các cặp kề nhau.

```text
Dãy sau khi sắp xếp: 1 3 5 6 8
Khoảng cách kề nhau: 2, 2, 1, 2
Đáp án: 1
```

Quy trình:

```text
1. Sắp xếp dãy tăng dần.
2. Với mỗi i từ 1 đến n - 1, tính a[i] - a[i - 1].
3. Giữ lại khoảng cách nhỏ nhất.
```

Code minh họa:

```cpp
sort(a.begin(), a.end());

long long answer = 1LL * a[1] - a[0];
for (int i = 2; i < n; i++) {
    answer = min(answer, 1LL * a[i] - a[i - 1]);
}

cout << answer << '\n';
```

Khi `n` có thể nhỏ hơn `2`, cần đọc giới hạn đề bài và xử lý trường hợp đặc biệt trước khi dùng `a[1]`.

#### Khi nào không cần sắp xếp?

Nếu chỉ cần tìm giá trị lớn nhất một lần, sắp xếp cả dãy là công việc dư thừa:

```cpp
int mx = a[0];
for (int i = 1; i < n; i++) {
    mx = max(mx, a[i]);
}
```

Hãy phân biệt:

| Nhu cầu | Hướng thường nghĩ đến |
|---|---|
| Chỉ cần một giá trị lớn nhất/nhỏ nhất | Duyệt và dùng `max/min` |
| Cần toàn bộ dữ liệu theo thứ tự | Sắp xếp |
| Cần tìm hai giá trị gần nhau | Sắp xếp rồi xét kề nhau |
| Cần ghép các phần tử gần nhau | Sắp xếp kết hợp hai con trỏ |
| Cần tìm nhanh nhiều lần | Sắp xếp kết hợp tìm kiếm nhị phân |

> **Không chọn thuật toán chỉ vì nhớ tên lệnh. Hãy chọn vì nó giải quyết đúng nhu cầu của bài toán.**

#### Tự kiểm tra

1. Vì sao sau khi sắp xếp chỉ cần xét các cặp kề nhau trong bài khoảng cách nhỏ nhất?
2. Sau khi sắp xếp, các giá trị trùng nhau có đặc điểm gì?
3. Bài tìm `max` một lần có cần `sort` không? Vì sao?
4. Hãy nêu một bài mà sắp xếp là bước chuẩn bị, chưa phải đáp án cuối cùng.

#### Luyện tập ngắn

- Đếm số giá trị khác nhau sau khi sắp xếp.
- Tìm khoảng cách nhỏ nhất trong một dãy vị trí.
- Cho hai dãy số, giải thích vì sao sắp xếp cả hai dãy có thể dẫn tới kỹ thuật hai con trỏ.

#### Tóm tắt bài

Sắp xếp đáng giá nhất khi nó làm giảm số trường hợp phải xét hoặc làm lộ ra cấu trúc của dữ liệu. Trước khi gọi `sort`, hãy trả lời: **sắp xếp xong thì bước nào dễ hơn?**

---

### Bài 1.6 — Độ phức tạp và quy trình giải bài

#### Mục tiêu bài

Sau Bài 1.6, em có thể ước lượng độ phức tạp cơ bản, kiểm tra lỗi thường gặp và trình bày một lời giải Sorting theo từng bước.

#### So sánh tốc độ tăng

Độ phức tạp mô tả số thao tác tăng lên như thế nào khi kích thước dữ liệu `N` tăng. Đây không phải là số giây cố định trên mọi máy.

| Cách làm | Ý tưởng | Độ phức tạp thường gặp |
|---|---|---:|
| Duyệt một lần | Xử lý từng phần tử | `O(N)` |
| Selection Sort | Nhiều lần tìm phần tử phù hợp | `O(N²)` |
| `std::sort` | Sắp xếp bằng thư viện chuẩn | `O(N log N)` |

Nếu `N` tăng, `N²` tăng nhanh hơn nhiều so với `N log N`. Vì vậy Selection Sort rất phù hợp để học ý tưởng, còn `std::sort` thường phù hợp hơn khi dữ liệu lớn.

Khi một chương trình vừa sắp xếp vừa duyệt một lần, phần sắp xếp thường quyết định độ phức tạp tổng thể:

```text
O(N log N) + O(N) = O(N log N)
```

#### Quy trình giải một bài Sorting

Em có thể dùng quy trình sau:

```text
Đọc đề
→ xác định Input và Output
→ hỏi sắp xếp có làm bước sau dễ hơn không
→ viết quy tắc thứ tự bằng lời
→ thử một ví dụ nhỏ bằng tay
→ viết pseudocode
→ viết code
→ thử test nhỏ và test biên
→ phân tích độ phức tạp
→ giải thích lại lời giải bằng lời
```

Không nên bắt đầu bằng việc chép ngay `sort`. Lệnh đúng nhưng dùng sai mục đích vẫn có thể dẫn tới một lời giải không phù hợp.

#### Kiểm tra lỗi bằng test nhỏ

Với chương trình Sorting, hãy thử ít nhất các trường hợp:

- chỉ có một phần tử;
- dãy đã tăng dần;
- dãy đã giảm dần;
- tất cả phần tử bằng nhau;
- có nhiều phần tử trùng nhau;
- có số âm nếu đề cho phép;
- giá trị nhỏ nhất hoặc lớn nhất theo giới hạn đề bài.

Khi chương trình sai, kiểm tra theo thứ tự: số phần tử đọc vào, chỉ số vòng lặp, khoảng truyền cho `sort`, quy tắc comparator và định dạng output.

#### Vị trí ban đầu và nội dung mở rộng

Sắp xếp có thể làm thay đổi vị trí ban đầu của phần tử. Nếu đề chỉ yêu cầu in các giá trị sau khi sắp xếp, ta chưa cần lưu vị trí cũ. Nếu đề hỏi “giá trị này ban đầu ở đâu”, ta phải lưu thêm thông tin cho mỗi phần tử. Đây là nội dung mở rộng, không đưa vào luồng nhập môn dùng `int` và `vector<int>`.

#### Tự kiểm tra

1. Một vòng lặp qua `N` phần tử thường có dạng độ phức tạp nào?
2. Hai vòng lặp lồng nhau thường dẫn tới dạng nào?
3. Vì sao `O(N log N) + O(N)` vẫn được viết là `O(N log N)`?
4. Hãy nêu ba test biên cho bài sắp xếp.
5. Khi nào cần quan tâm đến vị trí ban đầu?

#### Luyện tập ngắn

- Viết độ phức tạp dự kiến của các đoạn code có một vòng lặp, hai vòng lặp lồng nhau và một lệnh `sort`.
- Tạo ba input khiến một chương trình Sorting dễ lộ lỗi chỉ số.
- Viết năm câu mô tả quy trình giải một bài Sorting từ đọc đề đến kiểm thử.

#### Tóm tắt bài

Một lời giải tốt không chỉ có output đúng. Em cần biết dữ liệu được xử lý ra sao, vì sao chọn Sorting, chương trình chạy nhanh đến đâu và đã kiểm tra những trường hợp nào.

---

### Bài 1.7 — Ôn tập, kiểm tra và bài chuyển giao

#### Mục tiêu bài

Bài này giúp em kiểm tra xem mình đã hiểu ý tưởng hay mới chỉ nhớ cú pháp. Hãy làm theo thứ tự từ Tầng A đến Tầng C; không cần làm tất cả trong một lần nếu giáo viên đã giao phạm vi cụ thể.

Mỗi bài lập trình cần được hoàn thành theo chuỗi:

```text
Đọc đề → xác định Input/Output → viết ý tưởng bằng lời
       → code → test nhỏ → kiểm tra độ phức tạp → tự giải thích
```

#### Tầng A — Củng cố cú pháp

##### Bài 1.7.1 — Dãy số tăng dần

Đọc `N` số nguyên và in các số theo thứ tự không giảm.

- **Input:** Dòng đầu chứa `N`; dòng sau chứa `N` số nguyên.
- **Output:** Dãy sau khi sắp xếp tăng dần, các số cách nhau bởi một dấu cách.
- **Ví dụ:** Input `5` và dãy `8 3 6 1 5` cho output `1 3 5 6 8`.

Em cần kiểm tra đã đọc đủ `N` phần tử và không truy cập chỉ số ngoài `0..N-1`.

##### Bài 1.7.2 — Dãy số giảm dần

Đọc `N` số nguyên và in theo thứ tự không tăng.

- **Input:** `N` và một dãy `N` số nguyên.
- **Output:** Dãy sau khi sắp xếp giảm dần.
- **Ví dụ:** Với dãy `4 9 1 9 3 2`, output là `9 9 4 3 2 1`.

Hãy thử thêm trường hợp tất cả phần tử bằng nhau và trường hợp dãy đã giảm dần.

##### Bài 1.7.3 — Kiểm tra dãy đã có thứ tự chưa

Cho `N` số nguyên. In `YES` nếu dãy đã sắp xếp không giảm; ngược lại in `NO`.

- **Input:** `N` và một dãy `N` số nguyên.
- **Output:** Một từ `YES` hoặc `NO`.
- **Ví dụ:** `1 2 2 5 9` cho `YES`; `1 4 3 8` cho `NO`.

Bài này không cần gọi `sort`. Duyệt từ `i = 1` và kiểm tra xem có lần nào `a[i] < a[i - 1]` hay không.

##### Bài 1.7.4 — Đếm giá trị khác nhau

Cho `N` số nguyên. Hãy đếm số giá trị khác nhau trong dãy.

- **Input:** `N` và một dãy `N` số nguyên.
- **Output:** Số lượng giá trị khác nhau.
- **Ví dụ:** Dãy `4 2 4 1 2 2 9 1` có kết quả `4`.

Gợi ý: sắp xếp trước, sau đó đếm phần tử đầu tiên và mỗi phần tử khác phần tử đứng ngay trước nó. Hãy thử riêng trường hợp mọi phần tử giống nhau và mọi phần tử khác nhau.

#### Tầng B — Vận dụng mẫu

##### Bài 1.7.5 — Số chẵn đứng trước

Cho `N` số nguyên. Sắp xếp sao cho số chẵn đứng trước số lẻ. Trong mỗi nhóm, các số được sắp xếp tăng dần.

- **Input:** `N` và một dãy `N` số nguyên.
- **Output:** Dãy sau khi sắp xếp theo hai quy tắc.
- **Ví dụ:** Dãy `5 2 8 1 4 7 3` cho output `2 4 8 1 3 5 7`.

Hãy viết quy tắc bằng lời trước: kiểm tra nhóm chẵn/lẻ, rồi mới so sánh giá trị.

##### Bài 1.7.6 — Sắp xếp theo trị tuyệt đối

Cho `N` số nguyên. Sắp xếp theo trị tuyệt đối tăng dần. Nếu hai số có cùng trị tuyệt đối, số nhỏ hơn đứng trước.

- **Input:** `N` và một dãy `N` số nguyên.
- **Output:** Dãy đã sắp xếp theo quy tắc trên.
- **Ví dụ:** Dãy `-5 2 -1 4 -2 3` cho output `-1 -2 2 3 4 -5`.

Em cần kiểm tra cả số âm, số dương và trường hợp `x = -2`, `y = 2`.

##### Bài 1.7.7 — Khoảng cách nhỏ nhất

Cho `N` vị trí nguyên trên một tuyến đường, với `N ≥ 2`. Tìm khoảng cách nhỏ nhất giữa hai vị trí khác nhau.

- **Input:** `N` và một dãy `N` vị trí nguyên.
- **Output:** Khoảng cách nhỏ nhất.
- **Ví dụ:** Dãy `8 3 6 1 5` cho kết quả `1`.

Sau khi sắp xếp, chỉ cần xét `a[i] - a[i - 1]` với `i` từ `1` đến `N - 1`. Hãy giải thích vì sao không cần xét mọi cặp.

##### Bài 1.7.8 — Giá trị gần mục tiêu nhất

Cho `N` số nguyên và số nguyên `X`. Tìm giá trị có khoảng cách tuyệt đối tới `X` nhỏ nhất. Nếu có nhiều giá trị cùng khoảng cách, chọn giá trị nhỏ hơn.

- **Input:** Dòng đầu chứa `N` và `X`; dòng sau chứa `N` số nguyên.
- **Output:** Giá trị được chọn.
- **Ví dụ:** Với `N = 6`, `X = 10` và dãy `4 13 8 12 20 7`, output là `8`.

Thử các trường hợp `X` nhỏ hơn mọi phần tử, lớn hơn mọi phần tử và nằm giữa hai phần tử.

##### Bài 1.7.9 — Gom nhóm giá trị

Cho `N` số nguyên. In mỗi giá trị khác nhau cùng số lần xuất hiện, theo thứ tự tăng dần của giá trị.

- **Input:** `N` và một dãy `N` số nguyên.
- **Output:** Mỗi dòng gồm một giá trị và tần suất của nó.
- **Ví dụ:** Dãy `5 2 5 3 2 2 8` cho:

```text
2 3
3 1
5 2
8 1
```

Sau khi sắp xếp, hãy duyệt từng đoạn các phần tử bằng nhau và nhớ xử lý cả đoạn cuối.

#### Tầng C — Chuyển giao

##### Bài 1.7.10 — Ghép hai danh sách gần nhau

Có `N` giá trị trong danh sách A và `M` giá trị trong danh sách B. Tìm độ chênh lệch tuyệt đối nhỏ nhất giữa một phần tử của A và một phần tử của B.

- **Input:** Dòng đầu chứa `N`, `M`; dòng thứ hai chứa A; dòng thứ ba chứa B.
- **Output:** Độ chênh lệch nhỏ nhất.
- **Ví dụ:** A = `10 20 30`, B = `15 24` cho kết quả `4`.

Hãy sắp xếp cả hai danh sách, sau đó nghĩ về việc di chuyển con trỏ đang đứng ở giá trị nhỏ hơn. Phân tích riêng chi phí sắp xếp và chi phí di chuyển hai con trỏ.

##### Bài 1.7.11 — Sắp xếp theo chữ số hàng đơn vị

Cho `N` số nguyên không âm. Sắp xếp theo chữ số hàng đơn vị tăng dần. Nếu hai số có cùng chữ số hàng đơn vị, số nhỏ hơn đứng trước.

- **Input:** `N` và một dãy `N` số nguyên không âm.
- **Output:** Dãy đã sắp xếp theo quy tắc trên.
- **Ví dụ:** Dãy `23 41 18 35 12 29` cho output `41 12 23 35 18 29`.

Chữ số hàng đơn vị của `x` là `x % 10`. Hãy chuyển quy tắc chính và quy tắc phụ thành comparator.

##### Bài 1.7.12 — Có cần sắp xếp không?

Với mỗi yêu cầu sau, ghi `CÓ` hoặc `KHÔNG` cần sắp xếp, rồi giải thích bằng một hoặc hai câu:

1. Tìm điểm cao nhất trong một danh sách.
2. In toàn bộ danh sách theo thứ tự tăng dần.
3. Đếm số phần tử chẵn.
4. Tìm hai phần tử gần nhau nhất.
5. Kiểm tra một giá trị có xuất hiện hay không bằng một lần duyệt.
6. Ghép hai danh sách sao cho chênh lệch nhỏ nhất.

Câu trả lời phải nêu được kết quả cần tìm, lợi ích của Sorting nếu có, và một hướng khác nếu không cần sắp xếp.

#### Phiếu tự đánh giá

| Năng lực | Chưa chắc | Làm khi có gợi ý | Tự làm được |
|---|:---:|:---:|:---:|
| Sắp xếp tăng/giảm bằng `sort` |  |  |  |
| Mô phỏng Selection Sort |  |  |  |
| Viết comparator trên số nguyên |  |  |  |
| Viết comparator có hai tiêu chí |  |  |  |
| Nhận biết vị trí ban đầu có thể thay đổi |  |  |  |
| Giải thích lợi ích của Sorting |  |  |  |
| Phân tích `O(N²)` và `O(N log N)` |  |  |  |
| Tự tạo test biên |  |  |  |

#### Tiêu chí hoàn thành chương

Em có thể xem mình đã nắm chương khi có thể nói rõ, trước khi viết code:

> **Em sắp xếp theo tiêu chí nào? Sau khi sắp xếp, bước tiếp theo của bài toán dễ hơn ở điểm nào?**

Ngoài ra, em cần biên dịch được chương trình, chạy đúng các ví dụ, thử ít nhất ba test tự tạo và giải thích được vì sao code của mình không truy cập ngoài mảng.

---

### Tổng kết chương

> **Sắp xếp không chỉ là đổi vị trí các phần tử. Sắp xếp là cách tạo ra trật tự để nhìn thấy cấu trúc của bài toán.**

| Cần nhớ | Nội dung |
|---|---|
| Khái niệm | Đưa dữ liệu về một trật tự phù hợp |
| Selection Sort | Mỗi lượt chọn phần tử phù hợp nhất trong phần chưa xử lý |
| Tăng dần | `sort(a.begin(), a.end())` |
| Giảm dần | Dùng comparator mô tả số lớn đứng trước |
| Comparator | Quy tắc trả lời phần tử nào đứng trước |
| Mục đích | Tạo trật tự để tìm, ghép, chọn hoặc kiểm tra |
| Hiệu quả | So sánh trực giác `O(N²)` với `O(N log N)` |
| Cẩn thận | Chỉ số, khoảng xử lý, thứ tự, kiểu dữ liệu và test biên |
| Câu hỏi chính | Sắp xếp xong thì bước tiếp theo dễ hơn ở điểm nào? |

#### Những lỗi thường gặp

| Lỗi | Cách tự kiểm tra |
|---|---|
| Dùng `i <= n` | Chỉ số hợp lệ cuối cùng là `n - 1` |
| Nhầm tăng và giảm | Viết bằng lời “ai đứng trước ai?” |
| Dùng sai khoảng `sort` | Nhớ khoảng có đầu và không có cuối |
| Comparator thiếu tiêu chí phụ | Xét trường hợp hai phần tử bằng tiêu chí chính |
| Sắp xếp dù không cần | Xác định lợi ích của bước Sorting |
| Quên test dãy có một phần tử | Thử `n = 1` và kiểm tra mọi truy cập |
| Chỉ chép code | Tự giải thích vai trò của từng bước |

---

### Code tham chiếu

Đoạn code dưới đây chỉ minh họa mục tiêu tối giản: đọc một dãy số nguyên, sắp xếp tăng dần và in kết quả. Em nên thử dự đoán output trước khi chạy.

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    sort(a.begin(), a.end());

    for (int i = 0; i < n; i++) {
        if (i > 0) {
            cout << ' ';
        }
        cout << a[i];
    }
    cout << '\n';

    return 0;
}
```

Với input:

```text
5
8 3 6 1 5
```

output là:

```text
1 3 5 6 8
```

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

### Bản đồ chương

| Trường | Nội dung |
|---|---|
| Mục tiêu | Hiểu cách xây dựng lời giải bằng các lựa chọn cục bộ có căn cứ |
| Kiến thức cần có | Sắp xếp, comparator, vòng lặp, điều kiện, `vector` và mô tả Input–Process–Output |
| Phạm vi | Khái niệm tham lam, chọn hoạt động, chứng minh đổi chỗ, phản ví dụ và các biến thể cơ bản |
| Số bài | 6 bài học, kết hợp mô phỏng, code, lập luận và bài chuyển giao |

### Learning outcomes

Sau chương này, em có thể:

- giải thích được thuật toán tham lam là gì bằng một ví dụ cụ thể;
- phân biệt lựa chọn cục bộ với mục tiêu tối ưu toàn cục;
- nhận biết bài toán chọn nhiều hoạt động không giao nhau;
- sắp xếp hoạt động theo thời điểm kết thúc và duyệt để chọn hoạt động hợp lệ;
- mô phỏng được trạng thái sau từng lựa chọn;
- trình bày được ý tưởng vì sao chọn hoạt động kết thúc sớm là an toàn;
- dùng phản ví dụ để kiểm tra một quy tắc tham lam đáng ngờ;
- phân biệt bài dùng được tham lam với bài cần cân nhắc quy hoạch động hoặc tìm kiếm;
- phân tích được độ phức tạp `O(N log N)` của lời giải chọn hoạt động;
- giải thích sau khi chọn một phương án thì phần còn lại của bài toán thay đổi như thế nào.

### Câu hỏi trung tâm của chương

> **Ở mỗi bước, ta chọn gì để vừa tốt ngay lúc này, vừa không làm mất cơ hội đạt lời giải tốt nhất về sau?**

---

### Bài 2.1 — Tham lam là gì?

#### Mục tiêu bài

Sau Bài 2.1, em có thể mô tả một chiến lược tham lam, phân biệt “chọn ngay” với “thử mọi khả năng”, và biết rằng một quy tắc nghe có vẻ hợp lý vẫn cần được kiểm tra.

#### Khởi động

Có một hàng người đang chờ lấy vé. Mỗi người có một khoảng thời gian có thể vào quầy. Nếu quầy chỉ phục vụ được một người tại một thời điểm, ta muốn phục vụ càng nhiều người càng tốt.

Một suy nghĩ tự nhiên là chọn người đến sớm nhất. Nhưng người đến sớm nhất có thể chờ rất lâu và chiếm mất phần lớn thời gian. Một suy nghĩ khác là chọn người có khoảng thời gian ngắn nhất. Điều đó cũng chưa chắc đúng, vì một khoảng ngắn nằm ở giữa có thể chặn hai khoảng khác.

Muốn chọn đúng, ta phải tìm **tiêu chí liên quan trực tiếp đến mục tiêu**.

#### Ý tưởng “chọn tốt trước”

Một thuật toán tham lam thường làm như sau:

```text
1. Xác định mục tiêu cần tối ưu.
2. Chọn một phương án hợp lệ có vẻ tốt nhất theo tiêu chí đã đặt ra.
3. Cố định lựa chọn đó.
4. Cập nhật phần bài toán còn lại.
5. Lặp lại cho đến khi hoàn thành.
```

Điểm quan trọng là bước 2 không được chọn tùy tiện. Ta cần trả lời vì sao lựa chọn hiện tại không làm mất lời giải tối ưu về sau.

#### Cục bộ và toàn cục

**Lựa chọn cục bộ** là lựa chọn tốt ở bước hiện tại. **Lời giải toàn cục** là kết quả tốt nhất sau khi hoàn thành tất cả các bước.

Tham lam chỉ đúng khi các lựa chọn cục bộ theo tiêu chí phù hợp có thể dẫn tới một lời giải toàn cục tối ưu. Không phải cứ “chọn tốt nhất trước” là sẽ đúng.

#### Phản ví dụ với đổi tiền

Giả sử có các mệnh giá `1`, `3`, `4` và cần đổi số tiền `6` bằng ít đồng nhất.

Nếu luôn chọn đồng lớn nhất trước:

```text
6 → chọn 4, còn 2 → chọn 1, còn 1 → chọn 1
Số đồng: 3
```

Nhưng cách tốt hơn là:

```text
6 → chọn 3 và 3
Số đồng: 2
```

Vậy quy tắc “luôn chọn mệnh giá lớn nhất” **không phải lúc nào cũng đúng**. Đây là một phản ví dụ: một trường hợp nhỏ đủ để bác bỏ một quy tắc tổng quát.

#### Ba câu hỏi kiểm tra một ý tưởng tham lam

Trước khi code, em hãy hỏi:

1. Mục tiêu là tối đa, tối thiểu hay chỉ kiểm tra khả năng?
2. Tiêu chí chọn hiện tại có liên quan trực tiếp đến mục tiêu không?
3. Em có thể giải thích hoặc chứng minh vì sao lựa chọn đó không làm mất đáp án tốt nhất không?

Nếu chưa trả lời được câu thứ ba, đừng vội gọi thuật toán là đúng.

#### Tự kiểm tra

1. Lựa chọn cục bộ khác lời giải toàn cục ở điểm nào?
2. Trong ví dụ mệnh giá `1, 3, 4`, vì sao chọn `4` trước lại không tối ưu cho số tiền `6`?
3. Một phản ví dụ có tác dụng gì?
4. Tham lam có phải là thử mọi cách rồi chọn kết quả tốt nhất không?

#### Luyện tập ngắn

- Tạo một bộ mệnh giá khác mà chiến lược chọn đồng lớn nhất trước bị sai.
- Với mệnh giá `1, 5, 10, 25`, hãy thử số tiền `30` và kiểm tra xem chiến lược tham lam có cho kết quả tốt không. Chưa cần chứng minh cho mọi số tiền.
- Viết bằng lời một tình huống trong đó chọn phương án kết thúc sớm có thể hữu ích hơn chọn phương án bắt đầu sớm.

#### Tóm tắt bài

Tham lam là cách xây dựng lời giải bằng các quyết định từng bước. **Tiêu chí chọn phải được giải thích và kiểm tra**, vì một quy tắc hợp lý trong vài ví dụ chưa đủ để bảo đảm đúng trong mọi trường hợp.

---

### Bài 2.2 — Chọn nhiều hoạt động không giao nhau

#### Mục tiêu bài

Sau Bài 2.2, em có thể mô hình hóa bài toán lịch hoạt động, hiểu điều kiện hai hoạt động không giao nhau và mô phỏng việc chọn nhiều hoạt động bằng tay.

#### Bài toán

Một phòng học chỉ phục vụ được một hoạt động tại một thời điểm. Hoạt động thứ `i` bắt đầu tại `start[i]` và kết thúc tại `finish[i]`. Trong các ví dụ của chương, ta giả sử `0 <= start[i] < finish[i]`. Hai hoạt động được xem là không giao nhau nếu hoạt động sau bắt đầu khi hoạt động trước đã kết thúc.

Hãy chọn **nhiều hoạt động nhất** sao cho không có hai hoạt động được chọn nào giao nhau.

Nếu hoạt động A kết thúc lúc `5` và hoạt động B bắt đầu lúc `5`, ta cho phép chọn cả hai. Điều kiện tương ứng là:

```text
start của hoạt động mới >= finish của hoạt động vừa chọn
```

#### Ví dụ bằng tay

Cho các hoạt động:

| Hoạt động | Bắt đầu | Kết thúc |
|---|---:|---:|
| A | 1 | 4 |
| B | 3 | 5 |
| C | 0 | 6 |
| D | 5 | 7 |
| E | 3 | 8 |
| F | 5 | 9 |
| G | 6 | 10 |
| H | 8 | 11 |
| I | 8 | 12 |
| J | 2 | 13 |
| K | 12 | 14 |

Một lựa chọn tốt là:

```text
A: [1, 4] → D: [5, 7] → H: [8, 11] → K: [12, 14]
```

Ta chọn được `4` hoạt động. Nhưng vì sao không chọn C trước? C kết thúc lúc `6`, làm mất cơ hội chọn A và D.

#### Quan sát quan trọng

Trong mục tiêu chọn **nhiều hoạt động nhất**, hoạt động kết thúc sớm để lại nhiều thời gian còn lại hơn. Đây là dấu hiệu để thử tiêu chí:

> **Ưu tiên hoạt động có thời điểm kết thúc nhỏ nhất.**

Tiêu chí này khác với:

- bắt đầu sớm nhất;
- có thời lượng ngắn nhất;
- có thời điểm bắt đầu muộn nhất;
- có tên hoặc số thứ tự nhỏ nhất.

Các tiêu chí trên có thể đúng trong một bài khác, nhưng không tự động đúng cho bài này.

#### Mô phỏng sau khi sắp xếp theo thời điểm kết thúc

Danh sách theo `finish` tăng dần:

```text
A(1,4), B(3,5), C(0,6), D(5,7), E(3,8), F(5,9), G(6,10), H(8,11), I(8,12), J(2,13), K(12,14)
```

Duyệt lần lượt:

| Hoạt động xét | Có hợp lệ không? | Hành động | Thời điểm kết thúc mới |
|---|---|---|---:|
| A(1,4) | Có, là hoạt động đầu tiên | Chọn | 4 |
| B(3,5) | Không, `3 < 4` | Bỏ qua | 4 |
| C(0,6) | Không, `0 < 4` | Bỏ qua | 4 |
| D(5,7) | Có, `5 >= 4` | Chọn | 7 |
| E(3,8) | Không, `3 < 7` | Bỏ qua | 7 |
| F(5,9) | Không, `5 < 7` | Bỏ qua | 7 |
| G(6,10) | Không, `6 < 7` | Bỏ qua | 7 |
| H(8,11) | Có, `8 >= 7` | Chọn | 11 |
| I(8,12) | Không, `8 < 11` | Bỏ qua | 11 |
| J(2,13) | Không, `2 < 11` | Bỏ qua | 11 |
| K(12,14) | Có, `12 >= 11` | Chọn | 14 |

Trạng thái cần nhớ chỉ là `lastFinish`: thời điểm kết thúc của hoạt động gần nhất đã chọn.

#### Tự kiểm tra

1. Hai hoạt động `[1, 4]` và `[4, 6]` có giao nhau theo quy ước của bài không?
2. Sau khi chọn `[1, 4]`, hoạt động `[3, 5]` có được chọn không? Vì sao?
3. Vì sao hoạt động kết thúc sớm để lại nhiều thời gian hơn?
4. Trong bảng trên, tại sao hoạt động `D(5,7)` được chọn sau `A(1,4)`?

#### Luyện tập ngắn

- Vẽ các đoạn thời gian của sáu hoạt động bất kỳ rồi tự chọn số hoạt động không giao nhau.
- Với các khoảng `[2,3]`, `[1,5]`, `[4,6]`, `[6,8]`, `[5,7]`, hãy tìm một tập hoạt động lớn nhất.
- Thử chọn theo “bắt đầu sớm nhất” và so sánh với chọn theo “kết thúc sớm nhất”. Tìm một input làm hai cách cho kết quả khác nhau.

#### Tóm tắt bài

Bài toán chọn hoạt động yêu cầu tối đa số khoảng không giao nhau. Khi một hoạt động được chọn, phần còn lại chỉ phụ thuộc vào thời điểm kết thúc của hoạt động đó. Đây là nền tảng để dùng tiêu chí **kết thúc sớm nhất**.

---

### Bài 2.3 — Sắp xếp theo thời điểm kết thúc và viết code

#### Mục tiêu bài

Sau Bài 2.3, em có thể chuyển ý tưởng chọn hoạt động thành code C++17, viết comparator theo thời điểm kết thúc và duyệt các hoạt động hợp lệ.

#### Từ ý tưởng đến pseudocode

```text
Đọc N hoạt động
Sắp xếp hoạt động theo thời điểm kết thúc tăng dần
answer = 0
lastFinish = thời điểm nhỏ hơn mọi thời điểm bắt đầu

Với mỗi hoạt động:
    nếu start >= lastFinish:
        chọn hoạt động
        answer tăng 1
        lastFinish = finish

In answer
```

Mỗi lần chọn, ta cập nhật `lastFinish`. Các hoạt động bắt đầu trước `lastFinish` chắc chắn giao với hoạt động vừa chọn nên bị bỏ qua.

#### Gom hai mốc thời gian bằng `pair<int, int>`

Mỗi hoạt động gồm hai thông tin đi liền nhau: thời điểm bắt đầu (`start`) và thời điểm kết thúc (`finish`). Trong lập trình thi đấu, ta dùng kiểu `pair<int, int>` có sẵn của C++ để lưu một cặp hai số nguyên mà không cần định nghĩa `struct`:

```cpp
pair<int, int> activity = {finish, start};
```

Khi đặt `finish` vào vị trí `first` và `start` vào vị trí `second`, hàm `sort()` mặc định của C++ sẽ **tự động sắp xếp tăng dần theo thời điểm kết thúc (`finish`)**; nếu hai hoạt động kết thúc cùng lúc, `sort()` sẽ tự động so sánh tiếp theo `start`.

#### Code đầy đủ

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    // Lưu từng hoạt động dưới dạng {finish, start}
    vector<pair<int, int>> activities(n);
    for (int i = 0; i < n; i++) {
        int start, finish;
        cin >> start >> finish;
        activities[i] = {finish, start};
    }

    // sort() mặc định sẽ sắp xếp tăng dần theo finish (phần tử first)
    sort(activities.begin(), activities.end());

    int answer = 0;
    int lastFinish = -1;

    for (int i = 0; i < n; i++) {
        int finish = activities[i].first;
        int start = activities[i].second;

        if (start >= lastFinish) {
            answer++;
            lastFinish = finish;
        }
    }

    cout << answer << '\n';
    return 0;
}
```

Với input:

```text
4
1 3
2 5
3 9
6 8
```

chương trình chọn được `2` hoạt động, chẳng hạn `[1,3]` và `[6,8]`.

#### Theo dõi biến khi debug

Với mỗi hoạt động, em có thể kiểm tra ba thông tin:

| Biến | Câu hỏi cần trả lời |
|---|---|
| `start` (`activities[i].second`) | Hoạt động này bắt đầu lúc nào? |
| `finish` (`activities[i].first`) | Hoạt động này kết thúc lúc nào? |
| `lastFinish` | Lựa chọn gần nhất kết thúc lúc nào? |

Nếu chương trình chọn hai hoạt động giao nhau, hãy kiểm tra điều kiện `start >= lastFinish`. Nếu số lượng thấp bất thường, hãy kiểm tra comparator có thật sự sắp xếp theo `finish` hay không.

#### Tự kiểm tra

1. Vì sao phải sắp xếp trước khi duyệt?
2. `lastFinish` được cập nhật vào lúc nào?
3. Nếu dùng `activity.start > lastFinish` thay vì `>=`, chương trình sẽ sai ở trường hợp nào?
4. Vì sao comparator không được sắp xếp theo `start` trong bài này?
5. Với `n = 0`, chương trình in gì? Nếu đề bảo đảm `n >= 1`, điều này có ảnh hưởng không?

#### Luyện tập ngắn

- Viết lại comparator chỉ dùng tiêu chí `finish`.
- Sửa chương trình để in ra số thứ tự của các hoạt động được chọn, không chỉ in số lượng.
- Tự tạo input có hai hoạt động cùng thời điểm kết thúc và quan sát kết quả.

#### Tóm tắt bài

Code Greedy của bài chọn hoạt động có ba bước chính: **sort theo thời điểm kết thúc, kiểm tra điều kiện hợp lệ, cập nhật trạng thái**. Khi đã xác định được tiêu chí đúng, phần duyệt chỉ cần một biến `lastFinish`.

---

### Bài 2.4 — Vì sao lựa chọn kết thúc sớm là đúng?

#### Mục tiêu bài

Sau Bài 2.4, em có thể trình bày lập luận đổi chỗ và hiểu vì sao code đúng, thay vì chỉ nhớ một comparator.

#### Vì sao cần chứng minh?

Một chương trình có thể chạy đúng trên nhiều ví dụ nhưng vẫn sai ở một input khác. Với Greedy, phần khó thường không nằm ở vòng lặp mà nằm ở việc chứng minh **tiêu chí chọn là an toàn**.

Trong bài này, tiêu chí là chọn hoạt động kết thúc sớm nhất trong các hoạt động còn hợp lệ.

#### Lập luận đổi chỗ

Gọi `A` là hoạt động hợp lệ có thời điểm kết thúc sớm nhất. Giả sử có một lời giải tối ưu bắt đầu bằng hoạt động `B`.

Vì `A` kết thúc không muộn hơn `B`, ta có:

```text
finish(A) <= finish(B)
```

Nếu thay `B` bằng `A`, mọi hoạt động đứng sau `B` trong lời giải cũ vẫn bắt đầu sau hoặc đúng lúc `finish(B)`. Do `finish(A)` sớm hơn hoặc bằng `finish(B)`, các hoạt động đó cũng vẫn không giao với `A`.

Vậy ta có thể thay `B` bằng `A` mà không làm giảm số hoạt động được chọn. Điều này cho thấy tồn tại một lời giải tối ưu bắt đầu bằng hoạt động kết thúc sớm nhất.

Sau khi chọn `A`, bài toán còn lại có cùng dạng nhưng chỉ xét các hoạt động bắt đầu từ `finish(A)` trở đi. Lặp lại lập luận này cho phần còn lại, ta thu được thuật toán tham lam đúng.

#### Invariant khi duyệt

Trong lúc chương trình chạy, ta giữ invariant:

> Sau khi xử lý một đoạn đầu của danh sách đã sắp xếp, `lastFinish` là thời điểm kết thúc của hoạt động cuối cùng trong lời giải tham lam; các hoạt động đã chọn không giao nhau.

Khi gặp hoạt động mới:

- nếu `start < lastFinish`, hoạt động mới giao với lựa chọn trước nên bỏ qua;
- nếu `start >= lastFinish`, hoạt động mới hợp lệ và được chọn;
- vì danh sách đã sắp xếp theo `finish`, lựa chọn mới là hoạt động kết thúc sớm nhất trong các ứng viên đang xét.

#### Không cần thử mọi khả năng

Nếu có `N` hoạt động, thử mọi tập con có thể cần xét đến rất nhiều khả năng. Thuật toán tham lam tránh việc đó bằng cách cố định một lựa chọn an toàn ở mỗi bước. Đây là lý do Greedy thường có code ngắn, nhưng phần lập luận phải rõ.

#### Tự kiểm tra

1. Trong lập luận đổi chỗ, vì sao `finish(A) <= finish(B)` là điều quan trọng?
2. Sau khi thay `B` bằng `A`, tại sao các hoạt động phía sau vẫn hợp lệ?
3. Invariant của vòng duyệt nói điều gì?
4. Nếu chỉ cho biết code chạy đúng trên ba ví dụ, ta đã có chứng minh chưa?

#### Luyện tập ngắn

- Viết lại lập luận đổi chỗ bằng bốn câu của riêng em.
- Chỉ ra trạng thái được cập nhật sau mỗi lần chọn hoạt động.
- Vẽ một input trong đó lựa chọn đầu tiên kết thúc muộn làm số hoạt động tối đa giảm.

#### Tóm tắt bài

Greedy không đúng vì “trông có vẻ hợp lý”. Bài chọn hoạt động đúng vì ta có thể đổi lựa chọn đầu tiên của một lời giải tối ưu thành hoạt động kết thúc sớm nhất mà không làm mất các lựa chọn còn lại.

---

### Bài 2.5 — Khi nào tham lam thất bại?

#### Mục tiêu bài

Sau Bài 2.5, em có thể dùng phản ví dụ để bác bỏ một chiến lược tham lam sai và biết khi nào cần xem xét phương pháp khác.

#### Một số quy tắc dễ nhầm

Trong bài chọn hoạt động, các quy tắc sau không luôn tối ưu:

| Quy tắc | Vì sao có thể sai? |
|---|---|
| Chọn hoạt động bắt đầu sớm nhất | Có thể chọn một hoạt động kéo dài quá lâu |
| Chọn hoạt động ngắn nhất | Một hoạt động ngắn ở giữa vẫn có thể chặn hai hoạt động khác |
| Chọn hoạt động có ít xung đột nhất | Cần biết ảnh hưởng của nhiều hoạt động về sau |
| Chọn hoạt động có số thứ tự nhỏ nhất | Số thứ tự không liên quan mục tiêu |
| Chọn hoạt động kết thúc sớm nhất | Đây là tiêu chí phù hợp cho mục tiêu tối đa số hoạt động không giao nhau |

Không được dùng bảng này như một danh sách học thuộc. Hãy luôn quay lại mục tiêu và tìm phản ví dụ cho quy tắc đang định dùng.

#### Phản ví dụ cho “bắt đầu sớm nhất”

Cho các hoạt động:

```text
A = [0, 10]
B = [1, 2]
C = [2, 3]
D = [3, 4]
E = [4, 5]
```

Nếu chọn bắt đầu sớm nhất, ta chọn `A` và chỉ được `1` hoạt động. Nếu chọn kết thúc sớm nhất, ta chọn `B, C, D, E` và được `4` hoạt động.

#### Khi cần cân nhắc DP hoặc tìm kiếm

Nếu một lựa chọn hiện tại có nhiều trạng thái tương lai khác nhau và không thể chứng minh việc chọn sớm là an toàn, Greedy có thể không phù hợp. Khi đó, em có thể cần:

- **quy hoạch động**, nếu bài toán có các bài toán con lặp lại;
- **quay lui hoặc tìm kiếm**, nếu cần thử các lựa chọn trong phạm vi nhỏ;
- **sắp xếp kết hợp cấu trúc dữ liệu**, nếu quyết định phụ thuộc nhiều trạng thái đang hoạt động;
- một tiêu chí khác, nếu mục tiêu của bài đã thay đổi.

Ví dụ đổi tiền với mệnh giá `1, 3, 4` cho thấy cùng một ý tưởng “chọn đồng lớn nhất trước” có thể thất bại. Không nên lấy một Greedy đúng ở bài này áp dụng nguyên xi cho bài khác.

#### Phân biệt “tối đa số lượng” và “tối đa giá trị”

Bài chọn hoạt động tối đa **số lượng** hoạt động. Nếu mỗi hoạt động có thêm điểm thưởng và ta muốn tối đa **tổng điểm**, việc chọn kết thúc sớm nhất có thể không còn đủ. Mục tiêu mới thường đòi hỏi phân tích khác.

Thay đổi một từ trong đề — “nhiều hoạt động nhất” thành “tổng lợi ích lớn nhất” — có thể làm thay đổi hoàn toàn thuật toán.

#### Tự kiểm tra

1. Hãy dùng phản ví dụ để giải thích vì sao không chọn hoạt động bắt đầu sớm nhất.
2. “Ngắn nhất” và “kết thúc sớm nhất” có giống nhau không?
3. Nếu mỗi hoạt động có điểm thưởng, thông tin mới này có thể ảnh hưởng tiêu chí chọn như thế nào?
4. Vì sao không được kết luận “bài tối ưu nào cũng dùng Greedy”?

#### Luyện tập ngắn

- Tạo phản ví dụ cho quy tắc chọn hoạt động ngắn nhất.
- Cho một bộ mệnh giá và một số tiền, kiểm tra bằng tay xem chọn mệnh giá lớn nhất trước có tối ưu không.
- Viết hai đề bài gần giống nhau nhưng một bài tối đa số lượng, một bài tối đa tổng điểm. Nêu vì sao không nên dùng cùng một lập luận.

#### Tóm tắt bài

Một chiến lược tham lam chỉ đáng tin khi có lập luận phù hợp với mục tiêu cụ thể. **Phản ví dụ nhỏ là công cụ nhanh nhất để phát hiện một quy tắc sai.**

---

### Bài 2.6 — Ôn tập và bài chuyển giao

#### Mục tiêu bài

Bài này kiểm tra em có thể nhận dạng chiến lược tham lam, triển khai bài chọn hoạt động và tự kiểm tra tính đúng đắn hay không.

#### Tầng A — Củng cố

##### Bài 2.6.1 — Mô phỏng chọn hoạt động

Cho các khoảng thời gian. Sắp xếp chúng theo thời điểm kết thúc tăng dần, sau đó ghi lại các khoảng được chọn.

- **Input:** Không bắt buộc viết chương trình; giáo viên cung cấp một bảng hoạt động.
- **Output:** Danh sách hoạt động được chọn và số lượng hoạt động.
- **Ví dụ:** Với `[1,4]`, `[3,5]`, `[0,6]`, `[5,7]`, `[8,9]`, một đáp án tối ưu là `[1,4]`, `[5,7]`, `[8,9]`.

##### Bài 2.6.2 — Kiểm tra hai hoạt động

Cho hai hoạt động `[s1, f1]` và `[s2, f2]`. In `YES` nếu có thể chọn cả hai theo đúng thứ tự đã cho, tức là hoạt động thứ hai bắt đầu không sớm hơn thời điểm kết thúc của hoạt động thứ nhất; ngược lại in `NO`.

- **Ví dụ:** `[2,5]` rồi `[5,8]` cho `YES`; `[2,5]` rồi `[4,8]` cho `NO`.

##### Bài 2.6.3 — Chọn hoạt động từ danh sách đã sắp xếp

Cho danh sách đã được sắp xếp theo thời điểm kết thúc. Viết vòng lặp duyệt danh sách và đếm số hoạt động được chọn.

- **Input:** `N`, sau đó là `N` cặp `start finish` đã được sắp xếp.
- **Output:** Số hoạt động không giao nhau được chọn.
- **Lưu ý:** Bài này tập trung vào điều kiện `start >= lastFinish`, chưa cần tự viết `sort`.

##### Bài 2.6.4 — Viết comparator

Viết comparator để sắp xếp các hoạt động theo `finish` tăng dần; nếu bằng nhau, sắp xếp theo `start` tăng dần.

Hãy kiểm tra comparator bằng ít nhất ba cặp hoạt động, trong đó có hai hoạt động cùng thời điểm kết thúc.

#### Tầng B — Vận dụng mẫu

##### Bài 2.6.5 — Lịch phòng học

Có `N` lớp học, mỗi lớp cần dùng một phòng trong khoảng `[start, finish]`. Chỉ có một phòng. Tìm số lớp lớn nhất có thể xếp vào phòng mà không trùng thời gian.

- **Input:** `N` và `N` cặp thời gian, với `0 <= start < finish`.
- **Output:** Số lớp lớn nhất.
- **Ví dụ:** Với `4` khoảng `[1,3]`, `[2,5]`, `[3,4]`, `[4,6]`, kết quả là `3`.

##### Bài 2.6.6 — Chọn chuyến bay

Có `N` chuyến bay sử dụng một đường băng duy nhất. Giả sử các mốc thời gian không âm và `start < finish`. Hai chuyến bay có thể nối tiếp nếu chuyến sau bắt đầu tại hoặc sau thời điểm chuyến trước kết thúc. Tìm số chuyến bay tối đa.

- **Input:** `N`, sau đó là `N` cặp `start finish`.
- **Output:** Số chuyến bay tối đa.
- **Ví dụ:** Với `[1,3]`, `[2,5]`, `[3,9]`, `[6,8]`, kết quả là `2`.

##### Bài 2.6.7 — In danh sách được chọn

Từ bài chọn hoạt động, không chỉ in số lượng mà còn in các hoạt động được chọn theo thứ tự thời gian.

Hãy bảo đảm các hoạt động được in ra không giao nhau và giữ nguyên cặp `start finish` của từng hoạt động.

##### Bài 2.6.8 — Tìm phản ví dụ

Viết một input có ít nhất bốn hoạt động để chứng minh quy tắc “chọn hoạt động bắt đầu sớm nhất” không luôn cho số lượng lớn nhất.

Bài làm cần có ba phần: input, kết quả của quy tắc sai và một lời giải tốt hơn.

#### Tầng C — Chuyển giao

##### Bài 2.6.9 — Lập lịch có điểm thưởng

Mỗi hoạt động có thêm một điểm thưởng. Mục tiêu là chọn các hoạt động không giao nhau để tổng điểm lớn nhất.

Không được mặc định dùng tiêu chí kết thúc sớm nhất. Hãy thử tạo phản ví dụ cho việc đó và viết nhận xét về thông tin mới của bài toán.

##### Bài 2.6.10 — Đổi tiền và phản ví dụ

Cho các mệnh giá và số tiền cần đổi. Kiểm tra chiến lược chọn mệnh giá lớn nhất trước. Nếu chiến lược sai, in ra một cách đổi tốt hơn cho input đã cho.

- **Ví dụ:** Mệnh giá `1, 3, 4`, số tiền `6`: Greedy cho `4+1+1`, nhưng đáp án tốt hơn là `3+3`.

##### Bài 2.6.11 — Chọn việc theo thời hạn

Mỗi công việc cần đúng một đơn vị thời gian và có thời hạn hoàn thành. Hãy thử xây dựng chiến lược tham lam để thực hiện nhiều công việc nhất.

Bài này cần giáo viên hướng dẫn thêm về cách sắp xếp theo thời hạn và cách kiểm tra phản ví dụ. Mục tiêu chính là so sánh với bài chọn hoạt động, không yêu cầu học thuộc một công thức mới.

##### Bài 2.6.12 — Nói rõ vì sao

Với mỗi mô tả, hãy trả lời `DÙNG GREEDY`, `CẦN KIỂM TRA THÊM` hoặc `KHÔNG ĐỦ THÔNG TIN`, rồi giải thích:

1. Chọn nhiều hoạt động không giao nhau nhất.
2. Đổi tiền với mọi mệnh giá đều là bội phù hợp.
3. Chọn dãy có tổng điểm lớn nhất nhưng các phần tử có thể xung đột.
4. Chọn các đoạn không giao nhau nhưng muốn tổng độ dài lớn nhất.
5. Chọn một số lượng lớn nhất trong một lần duyệt.

Điểm quan trọng là em phải nêu mục tiêu và lý do, không chỉ ghi tên thuật toán.

#### Phiếu tự đánh giá

| Năng lực | Chưa chắc | Làm khi có gợi ý | Tự làm được |
|---|:---:|:---:|:---:|
| Giải thích tham lam bằng ví dụ |  |  |  |
| Phân biệt cục bộ và toàn cục |  |  |  |
| Chọn hoạt động kết thúc sớm nhất |  |  |  |
| Viết comparator theo `finish` |  |  |  |
| Duyệt và cập nhật `lastFinish` |  |  |  |
| Mô phỏng lời giải bằng tay |  |  |  |
| Viết phản ví dụ cho quy tắc sai |  |  |  |
| Trình bày lập luận đổi chỗ |  |  |  |
| Phân tích `O(N log N)` |  |  |  |
| Nhận biết khi cần kiểm tra phương pháp khác |  |  |  |

#### Tiêu chí hoàn thành chương

Em có thể xem mình đã nắm chương khi có thể trả lời rõ:

> **Tiêu chí tham lam của em là gì, vì sao lựa chọn đó an toàn, và có phản ví dụ nào làm nó thất bại không?**

Ngoài ra, em cần biên dịch được chương trình chọn hoạt động, chạy đúng ví dụ, thử ít nhất ba test tự tạo và giải thích được ý nghĩa của `lastFinish`.

---

### Tổng kết chương

> **Tham lam không phải là chọn tùy ý phương án tốt nhất trước mắt. Tham lam là chọn từng bước theo một tiêu chí có thể bảo vệ bằng lập luận.**

| Cần nhớ | Nội dung |
|---|---|
| Khái niệm | Xây dựng lời giải bằng lựa chọn cục bộ từng bước |
| Bài mẫu | Chọn nhiều hoạt động không giao nhau nhất |
| Tiêu chí | Sắp xếp theo thời điểm kết thúc tăng dần |
| Trạng thái | `lastFinish` của hoạt động gần nhất đã chọn |
| Điều kiện chọn | `start >= lastFinish` |
| Chứng minh | Lập luận đổi chỗ: kết thúc sớm không làm mất phần còn lại |
| Phản ví dụ | Dùng để bác bỏ quy tắc tham lam không đúng |
| Cẩn thận | “Lớn nhất”, “nhỏ nhất”, “ngắn nhất” chưa đủ để kết luận |
| Độ phức tạp | `O(N log N)` do sắp xếp và `O(N)` do duyệt |
| Câu hỏi chính | Chọn gì, vì sao an toàn, và khi nào thất bại? |

#### Những lỗi thường gặp

| Lỗi | Cách tự kiểm tra |
|---|---|
| Sắp xếp theo thời điểm bắt đầu | Nhắc lại mục tiêu là tối đa số hoạt động |
| Dùng `>` thay cho `>=` | Kiểm tra hai hoạt động nối tiếp tại cùng một thời điểm |
| Quên cập nhật `lastFinish` | Theo dõi trạng thái sau mỗi lần chọn |
| Comparator không theo `finish` | In danh sách sau sort để kiểm tra |
| Tin rằng mọi bài tối ưu đều tham lam | Tìm phản ví dụ nhỏ |
| Chỉ code mà không chứng minh | Viết lập luận đổi chỗ bằng lời |
| Quên hoạt động cuối danh sách | Kiểm tra vòng lặp chạy đến `n - 1` |
| Nhầm số lượng với tổng giá trị | Đọc kỹ mục tiêu trong đề |

#### Code tham chiếu

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    // Lưu từng hoạt động dưới dạng {finish, start}
    vector<pair<int, int>> activities(n);
    for (int i = 0; i < n; i++) {
        int start, finish;
        cin >> start >> finish;
        activities[i] = {finish, start};
    }

    // sort() mặc định sẽ sắp xếp tăng dần theo finish (phần tử first)
    sort(activities.begin(), activities.end());

    int answer = 0;
    int lastFinish = -1;

    for (int i = 0; i < n; i++) {
        int finish = activities[i].first;
        int start = activities[i].second;

        if (start >= lastFinish) {
            answer++;
            lastFinish = finish;
        }
    }

    cout << answer << '\n';
    return 0;
}
```

Với input:

```text
4
1 3
2 5
3 9
6 8
```

output là:

```text
2
```

---

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
