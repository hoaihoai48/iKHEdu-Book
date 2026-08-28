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
- [Phần mở đầu — Làm quen & Tư duy giải bài](#phần-mở-đầu--làm-quen--tư-duy-giải-bài)
- [C++ Cơ bản — Tờ ghi nhớ (CẦN NHỚ — Tra cứu)](#c-cơ-bản--tờ-ghi-nhớ-cần-nhớ--tra-cứu)
  - [Tổng quan Tra cứu](#tổng-quan-tra-cứu)
  - [I.1. Khung chương trình chuẩn & I-P-O](#i1-khung-chương-trình-chuẩn--i-p-o)
  - [I.2. Dữ liệu, biến và phép tính](#i2-dữ-liệu-biến-và-phép-tính)
  - [I.3. Điều kiện và vòng lặp](#i3-điều-kiện-và-vòng-lặp)
  - [I.4. Những viên gạch xử lý dữ liệu](#i4-những-viên-gạch-xử-lý-dữ-liệu)
  - [I.5. Hàm, debug và độ phức tạp](#i5-hàm-debug-và-độ-phức-tạp)
  - [I.6. Bảng tra cứu nhanh](#i6-bảng-tra-cứu-nhanh)
- [Phần II — Chuyên đề thuật toán](#phần-ii--chuyên-đề-thuật-toán)
  - [Bản đồ thuật toán](#bản-đồ-thuật-toán)
  - [Chương 1 — Sắp xếp](#chương-1--sắp-xếp)
    - [Bài 1.1 — Bản chất của Sắp xếp & Thuật toán Selection Sort](#bài-11--bản-chất-của-sắp-xếp--thuật-toán-selection-sort)
    - [Bài 1.2 — Sắp xếp tối ưu với std::sort & Hàm so sánh (Comparator)](#bài-12--sắp-xếp-tối-ưu-với-stdsort--hàm-so-sánh-comparator)
    - [Bài 1.3 — Các dạng bài toán ứng dụng Trật tự sắp xếp](#bài-13--các-dạng-bài-toán-ứng-dụng-trật-tự-sắp-xếp)
    - [Bài 1.4 — Tổng kết chương & Bộ đề luyện tập phân tầng](#bài-14--tổng-kết-chương--bộ-đề-luyện-tập-phân-tầng)
  - [Chương 2 — Tham lam](#chương-2--tham-lam)
    - [Bài 2.1 — Tham lam là gì?](#bài-21--tham-lam-là-gì)
    - [Bài 2.2 — Chọn nhiều hoạt động không giao nhau](#bài-22--chọn-nhiều-hoạt-động-không-giao-nhau)
    - [Bài 2.3 — Sắp xếp theo thời điểm kết thúc và viết code](#bài-23--sắp-xếp-theo-thời-điểm-kết-thúc-và-viết-code)
    - [Bài 2.4 — Vì sao lựa chọn kết thúc sớm là đúng?](#bài-24--vì-sao-lựa-chọn-kết-thúc-sớm-là-đúng)
    - [Bài 2.5 — Khi nào tham lam thất bại?](#bài-25--khi-nào-tham-lam-thất-bại)
    - [Bài 2.6 — Ôn tập và bài chuyển giao](#bài-26--ôn-tập-và-bài-chuyển-giao)
    - [Tổng kết chương](#tổng-kết-chương-1)
  - [Chương 3 — Số học](#chương-3--số-học)
    - [Bài 3.1 — Ước, bội và quy luật đối xứng cặp ước $\mathcal{O}(\sqrt{N})$](#bài-31--ước-bội-và-quy-luật-đối-xứng-cặp-ước-mathcalosqrtn)
    - [Bài 3.2 — Ước chung lớn nhất (GCD) và Thuật toán Euclid](#bài-32--ước-chung-lớn-nhất-gcd-và-thuật-toán-euclid)
    - [Bài 3.3 — Bội chung nhỏ nhất (LCM) và Kỹ thuật chống tràn số](#bài-33--bội-chung-nhỏ-nhất-lcm-và-kỹ-thuật-chống-tràn-số)
    - [Bài 3.4 — Số nguyên tố và Kỹ thuật kiểm tra tối ưu $\mathcal{O}(\sqrt{N})$](#bài-34--số-nguyên-tố-và-kỹ-thuật-kiểm-tra-tối-ưu-mathcalosqrtn)
    - [Bài 3.5 — Phân tích thừa số nguyên tố](#bài-35--phân-tích-thừa-số-nguyên-tố)
    - [Bài 3.6 — Sàng số nguyên tố Eratosthenes](#bài-36--sàng-số-nguyên-tố-eratosthenes)
    - [Bài 3.7 — Ôn tập, kiểm tra và bài chuyển giao](#bài-37--ôn-tập-kiểm-tra-và-bài-chuyển-giao)
    - [Tổng kết chương](#tổng-kết-chương-2)
    - [Code tham chiếu](#code-tham-chiếu-2)
  - [Chương 4 — Đếm phân phối](#chương-4--đếm-phân-phối)
    - [Bài 4.1 — Mảng tần suất trực tiếp và Tư duy chuyển giá trị thành chỉ số](#bài-41--mảng-tần-suất-trực-tiếp-và-tư-duy-chuyển-giá-trị-thành-chỉ-số)
    - [Bài 4.2 — Thống kê tần suất: Tìm Mode, Min-Max và Phần tử đa số](#bài-42--thống-kê-tần-suất-tìm-mode-min-max-và-phần-tử-đa-số)
    - [Bài 4.3 — Mảng tần suất trên bảng chữ cái và Kiểm tra chuỗi Anagram](#bài-43--mảng-tần-suất-trên-bảng-chữ-cái-và-kiểm-tra-chuỗi-anagram)
    - [Bài 4.4 — Kỹ thuật đếm cặp $\mathcal{O}(N)$ bằng Bảng tần suất](#bài-44--kỹ-thuật-đếm-cặp-mathcalon-bằng-bảng-tần-suất)
    - [Bài 4.5 — Nguyên lý Dirichlet trong Tin học](#bài-45--nguyên-lý-dirichlet-trong-tin-học)
    - [Bài 4.6 — Ôn tập, kiểm tra và bài chuyển giao](#bài-46--ôn-tập-kiểm-tra-và-bài-chuyển-giao)
    - [Tổng kết chương](#tổng-kết-chương-3)
    - [Code tham chiếu](#code-tham-chiếu-3)
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

# Phần mở đầu — Làm quen & Tư duy giải bài

## Lập trình là gì?

Lập trình là cách chúng ta hướng dẫn máy tính giải quyết một công việc cụ thể thông qua các câu lệnh rõ ràng, chính xác. Máy tính xử lý rất nhanh, nhưng nó chỉ làm đúng những gì được lập trình.

Trong lập trình thi đấu, nhiệm vụ của em là: **Đọc một đề bài → Hiểu yêu cầu và dữ liệu → Tìm ra phương pháp giải tối ưu → Viết chương trình C++ để máy tính tự động giải quyết bài toán đó.**

## Quy trình sáu câu hỏi

Trước khi viết code, hãy luôn trả lời:

1. Đề bài cho dữ liệu gì? (Input)
2. Cần in hoặc tìm kết quả gì? (Output)
3. Dữ liệu sẽ được lưu ở biến, mảng hay `vector` nào phù hợp?
4. Có công thức hoặc quy tắc nào cần viết ra trước không?
5. Các bước xử lý được thực hiện một lần hay lặp lại nhiều lần? (Process)
6. Làm thế nào để kiểm tra kết quả trên test nhỏ và test biên? (Debug & Verify)

Mô hình chung xuyên suốt mọi bài toán:

```text
Input → Process → Output
```

Một lời giải tốt phải giải thích được cả ba phần, không chỉ có code chạy được.

## Công thức trước code

Với bài toán tính tổng, hãy viết `sum = a + b` trước khi chuyển thành C++. Với bài toán có nhiều bước, hãy viết các bước bằng lời hoặc pseudocode. Việc này giúp tách bạch lỗi toán học, lỗi thuật toán và lỗi cú pháp.

## Debug là một phần của lời giải

Khi chương trình chạy sai hoặc nhận kết quả Wrong Answer, tuyệt đối không đoán ngẫu nhiên. Hãy kiểm tra một test rất nhỏ bằng tay, in giá trị trung gian nếu cần, kiểm tra số lần lặp, chỉ số `0.n-1`, điều kiện dừng và kiểu dữ liệu có bị tràn số (`long long`) hay không.

---

# C++ Cơ bản — Tờ ghi nhớ (CẦN NHỚ — Tra cứu)

Tờ ghi nhớ này tổng hợp những **công cụ C++ nền tảng** dùng xuyên suốt cuốn sách. Em không cần học thuộc toàn bộ ngay từ đầu; hãy mở phần này ra **tra cứu tức thì** mỗi khi quên cú pháp hoặc cần kiểm tra bẫy lỗi.

## Tổng quan Tra cứu

| Nhóm công cụ | Cú pháp cốt lõi | Dùng khi nào? |
|---|---|---|
| Khung chương trình | `main()`, `cin`, `cout`, fast I/O | Bắt đầu mọi bài toán |
| Biến & Kiểu dữ liệu | `int`, `long long`, `double`, `char`, `string`, `bool` | Lưu trữ dữ liệu phù hợp |
| Toán tử & Điều kiện | `+ - * / %`, `== != < >`, `&& || !`, `if/else` | Tính toán & Ra quyết định |
| Vòng lặp & Tích lũy | `for`, `while`, `sum`, `count`, `max`, `min` | Lặp & Xử lý dãy dữ liệu |
| Mảng động vector | `vector<int> a(n)`, `push_back`, `size()` | Lưu danh sách dữ liệu |
| Hàm & Debug | `return_type name()`, test biên, `cerr` | Chia nhỏ bài & Tìm lỗi |
| Độ phức tạp | `O(1)`, `O(N)`, `O(N log N)`, `O(N²)` | Ước lượng thời gian chạy |

## I.1. Khung chương trình chuẩn & I-P-O

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    // 1. Tối ưu vào ra (Fast I/O)
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // 2. Đọc dữ liệu (Input)
    // 3. Xử lý bài toán (Process)
    // 4. In kết quả (Output)

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
| Kiểm tra mảng | Chú ý chỉ số `0.n-1` và điều kiện biên |
| Debug | Test nhỏ → test biên → kiểm tra trung gian → test lại |

> Trong luồng nhập môn, chỉ dùng các công cụ học sinh đã được xây nền. `struct`, `pair` và cách lưu nhiều thuộc tính là nội dung mở rộng, không phải prerequisite của các bài Sorting cơ bản.

# Phần II — Chuyên đề thuật toán

## Chương 1 — Sắp xếp (Sorting)

### Bản đồ chương

| Trường | Nội dung |
|---|---|
| Mục tiêu | Hiểu sắp xếp là bước tiền xử lý tạo trật tự dữ liệu, làm chủ thuật toán Selection Sort và hàm `std::sort`, viết được hàm so sánh tùy biến và ứng dụng giải quyết các bài toán gom nhóm, khoảng cách |
| Kiến thức cần có | Cú pháp C++ cơ bản (`int`, `vector<int>`, vòng lặp `for`, câu lệnh `if`, hoán vị `swap`) |
| Phạm vi | Bản chất sắp xếp, Selection Sort $\mathcal{O}(N^2)$, `std::sort` $\mathcal{O}(N \log N)$, Comparator `bool cmp()`, bài toán gom nhóm và cặp kề nhau |
| Cấu trúc chương | 3 Bài học lý thuyết & thực hành + 1 Bài tổng kết & luyện tập phân tầng |

### Learning outcomes

Sau chương này, em có thể:
1. Giải thích vì sao trật tự dữ liệu giúp các bước tìm kiếm, đếm và gom nhóm trở nên đơn giản hơn.
2. Mô phỏng bằng tay và cài đặt được thuật toán Selection Sort $\mathcal{O}(N^2)$ với thao tác `swap`.
3. Sử dụng thành thạo hàm `sort()` của thư viện C++ để sắp xếp tăng dần, giảm dần trong thời gian $\mathcal{O}(N \log N)$.
4. Tự viết hàm so sánh tùy biến (Custom Comparator) theo các quy tắc đặc thù (chẵn/lẻ, trị tuyệt đối).
5. Nhận diện và áp dụng trật tự sắp xếp để đếm số giá trị phân biệt và tìm cặp phần tử gần nhau nhất.
6. Hoàn thành bộ bài tập phân tầng từ củng cố cú pháp đến vận dụng thi đấu.

---

### Bài 1.1 — Bản chất của Sắp xếp & Thuật toán Selection Sort

#### 1. Mục tiêu bài

Sau Bài 1.1, em hiểu rõ tại sao cần sắp xếp, mô phỏng được quá trình chọn phần tử nhỏ nhất bằng tay và tự tay viết được thuật toán Selection Sort $\mathcal{O}(N^2)$.

#### 2. Khởi động: Vì sao cần sắp xếp?

Cho dãy số nguyên chưa có thứ tự:

```text
8  3  6  1  5
```

- Nếu muốn tìm số lớn nhất, em chỉ cần duyệt một lượt từ trái sang phải và giữ lại số lớn nhất đã gặp.
- Nhưng nếu cần **tìm khoảng cách nhỏ nhất giữa hai số bất kỳ**, hoặc **đếm xem có bao nhiêu số khác nhau**, việc dữ liệu nằm lộn xộn sẽ khiến em phải so sánh từng cặp một ($\mathcal{O}(N^2)$).
- Nếu dãy số đã được xếp tăng dần:

```text
1  3  5  6  8
```

Mọi thứ trở nên cực kỳ rõ ràng: hai số gần nhau nhất chắc chắn phải đứng cạnh nhau, các số giống nhau sẽ tự động nằm liền kề nhau!

> **Sắp xếp không tạo ra dữ liệu mới. Sắp xếp là bước tạo trật tự để các bước xử lý tiếp theo trở nên dễ dàng và nhanh chóng hơn.**

#### 3. Ý tưởng thuật toán Selection Sort (Sắp xếp chọn)

Ý tưởng cốt lõi của Selection Sort gói gọn trong một câu:
> **Ở mỗi vị trí $i$ từ đầu đến cuối mảng, tìm phần tử nhỏ nhất trong phần chưa sắp xếp rồi đổi chỗ (`swap`) nó về vị trí $i$.**

##### Mô phỏng từng bước cho dãy `8 3 6 1 5` ($N = 5$):

| Lượt $i$ | Vị trí đang xét | Phần chưa sắp xếp | Phần tử nhỏ nhất tìm được | Thao tác đổi chỗ | Dãy số sau lượt đó |
|:---:|:---:|:---:|:---:|:---:|---|
| **Lượt 1** | $i = 0$ | `[8, 3, 6, 1, 5]` | Số `1` tại vị trí 3 | `swap(a[0], a[3])` | `[1, 3, 6, 8, 5]` *(Số 1 đã đúng vị trí)* |
| **Lượt 2** | $i = 1$ | `[3, 6, 8, 5]` | Số `3` tại vị trí 1 | `swap(a[1], a[1])` | `[1, 3, 6, 8, 5]` *(Số 3 đã đúng vị trí)* |
| **Lượt 3** | $i = 2$ | `[6, 8, 5]` | Số `5` tại vị trí 4 | `swap(a[2], a[4])` | `[1, 3, 5, 8, 6]` *(Số 5 đã đúng vị trí)* |
| **Lượt 4** | $i = 3$ | `[8, 6]` | Số `6` tại vị trí 4 | `swap(a[3], a[4])` | `[1, 3, 5, 6, 8]` *(Toàn bộ dãy đã tăng dần)* |

#### 4. Cài đặt C++

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

    // Thuat toan Selection Sort O(N^2)
    for (int i = 0; i < n - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < n; j++) {
            if (a[j] < a[min_idx]) {
                min_idx = j;
            }
        }
        swap(a[i], a[min_idx]);
    }

    // In ket qua
    for (int i = 0; i < n; i++) {
        if (i > 0) cout << ' ';
        cout << a[i];
    }
    cout << '\n';

    return 0;
}
```

#### 5. Bảng theo dõi biến khi Debug

| Biến | Ý nghĩa | Lưu ý quan trọng |
|---|---|---|
| `i` | Vị trí đang cần đặt phần tử đúng | Vòng lặp ngoài chỉ cần chạy đến `n - 2` vì khi $n-1$ phần tử đầu đã đúng, phần tử cuối cùng tự động đúng. |
| `j` | Vị trí đang duyệt tìm phần tử nhỏ nhất | Luôn bắt đầu từ `i + 1` đến `n - 1`. Điều kiện dừng là `j < n`, không viết `j <= n`. |
| `min_idx` | Chỉ số của phần tử nhỏ nhất tìm được | Khởi tạo bằng `i` trước khi chạy vòng lặp `j`. |

#### 6. Quiz Trắc nghiệm nhanh

**Câu 1:** Thao tác sắp xếp một mảng số nguyên làm thay đổi điều gì?  
- A. Làm thay đổi giá trị của các phần tử trong mảng.  
- B. Làm thay đổi số lượng phần tử trong mảng.  
- C. Làm thay đổi vị trí (thứ tự) của các phần tử trong mảng.  
- D. Tự động xóa bỏ các phần tử có giá trị trùng nhau.  
👉 **Đáp án:** **C**. Sắp xếp chỉ hoán đổi vị trí của các phần tử để tạo trật tự, bảo toàn 100% giá trị và số lượng ban đầu.

**Câu 2:** Với dãy $N$ phần tử, thuật toán Selection Sort thực hiện bao nhiêu lượt duyệt ở vòng lặp ngoài?  
- A. Đúng $N$ lượt.  
- B. $N - 1$ lượt.  
- C. $N / 2$ lượt.  
- D. $N^2$ lượt.  
👉 **Đáp án:** **B**. Khi $N - 1$ phần tử đã được đưa về đúng vị trí ở bên trái, phần tử cuối cùng chắc chắn là phần tử lớn nhất và đã tự nằm đúng chỗ.

**Câu 3:** Cho dãy số `5 2 4 1`. Sau lượt đầu tiên ($i = 0$) của Selection Sort, trạng thái dãy số là gì?  
- A. `2 5 4 1`  
- B. `1 2 4 5`  
- C. `1 5 4 2`  
- D. `1 2 5 4`  
👉 **Đáp án:** **C**. Phần tử nhỏ nhất là `1` tại chỉ số 3, đổi chỗ với phần tử đầu tiên `5` $\implies$ dãy thành `1 5 4 2`.

#### 7. Bài tập thực hành nộp code tại chỗ

##### Bài thực hành 1.1A — Kiểm tra dãy đã tăng dần chưa
- **Mục tiêu:** Rèn luyện kỹ năng duyệt mảng kiểm tra điều kiện thứ tự kề nhau.
- **Đề bài:** Cho mảng gồm $N$ số nguyên $A_1, A_2, \dots, A_N$. Kiểm tra xem mảng đã được sắp xếp theo thứ tự không giảm ($A_i \le A_{i+1}$ với mọi $1 \le i < N$) hay chưa.
- **Input:** 
  - Dòng 1 ghi số nguyên dương $N$ ($1 \le N \le 10^5$).
  - Dòng 2 ghi $N$ số nguyên $A_i$ ($|A_i| \le 10^9$).
- **Output:** In `YES` nếu dãy đã tăng dần, ngược lại in `NO`.
- **Sample:**
  ```text
  Input:
  4
  1 3 5 8
  Output:
  YES
  ```

##### Bài thực hành 1.1B — Cài đặt Selection Sort
- **Mục tiêu:** Cài đặt chính xác thuật toán Selection Sort để hiểu bản chất đổi chỗ.
- **Đề bài:** Cho mảng $N$ số nguyên ($1 \le N \le 1000$). Hãy sắp xếp mảng theo thứ tự tăng dần bằng thuật toán Selection Sort và in ra kết quả.
- **Sample:**
  ```text
  Input:
  5
  8 3 6 1 5
  Output:
  1 3 5 6 8
  ```

#### 8. Tóm tắt bài

- Sắp xếp là bước tiền xử lý giúp tạo trật tự cho dữ liệu.
- Selection Sort lặp lại việc chọn phần tử nhỏ nhất và đưa về vị trí hiện tại bằng `swap`.
- Độ phức tạp thời gian của Selection Sort là $\mathcal{O}(N^2)$, phù hợp khi $N \le 1000$.

---

### Bài 1.2 — Sắp xếp tối ưu với `std::sort` & Hàm so sánh (Comparator)

#### 1. Mục tiêu bài

Sau Bài 1.2, em biết cách sử dụng hàm `std::sort()` có sẵn trong thư viện C++ để sắp xếp cực nhanh với $\mathcal{O}(N \log N)$, biết cách đảo ngược thứ tự và tự viết hàm so sánh (Comparator) theo luật riêng.

#### 2. Hàm `std::sort()` trong C++

Trong thi đấu lập trình, khi $N = 10^5$, thuật toán $\mathcal{O}(N^2)$ mất $10^{10}$ phép tính (chạy mất $\approx 10$ giây $\implies$ quá thời gian TLE).  
C++ cung cấp sẵn hàm `std::sort()` trong thư viện `<algorithm>` (đã có sẵn trong `#include <bits/stdc++.h>`).

- **Cú pháp sắp xếp tăng dần:**
  ```cpp
  sort(a.begin(), a.end());
  ```
- **Cú pháp sắp xếp giảm dần:**
  ```cpp
  sort(a.begin(), a.end(), greater<int>());
  ```
- **Độ phức tạp:** $\mathcal{O}(N \log N)$. Với $N = 10^5$, số phép tính chỉ khoảng $1.7 \times 10^6$ thao tác, chạy trong chưa tới **0.02 giây**!

#### 3. Tùy biến thứ tự với Hàm so sánh (Custom Comparator)

Khi đề bài yêu cầu thứ tự đặc thù (ví dụ: số chẵn đứng trước số lẻ, sắp xếp theo giá trị tuyệt đối...), ta tự định nghĩa một hàm so sánh:

```cpp
bool cmp(int u, int v) {
    // Tra ve true neu muon 'u' dung truoc 'v' trong day ket qua
    // Tra ve false neu nguoc lai
}
```

##### Ví dụ 1: Sắp xếp theo giá trị tuyệt đối tăng dần
Nếu hai số có trị tuyệt đối bằng nhau thì số nhỏ hơn đứng trước:

```cpp
bool cmpAbs(int u, int v) {
    if (abs(u) != abs(v)) {
        return abs(u) < abs(v); // Tri tuyet doi nho hon dung truoc
    }
    return u < v; // Neu tri tuyet doi bang nhau, so nho hon dung truoc
}
```

##### Ví dụ 2: Số chẵn đứng trước, số lẻ đứng sau
Trong cùng nhóm chẵn hoặc nhóm lẻ, số nào nhỏ hơn đứng trước:

```cpp
bool cmpEvenOdd(int u, int v) {
    if (u % 2 != v % 2) {
        return (u % 2 == 0); // So chan (u % 2 == 0) dung truoc so le
    }
    return u < v; // Cung tinh chan le: xep tang dan
}
```

> **Nguyên tắc sống còn (Strict Weak Ordering):** Trong hàm `cmp`, chỉ dùng toán tử `<` hoặc `>`, **tuyệt đối KHÔNG dùng `<=` hoặc `>=`**. Nếu hai phần tử bằng nhau (`u == v`), hàm `cmp` **bắt buộc phải trả về `false`** để tránh lỗi bộ nhớ (Runtime Error).

#### 4. Cài đặt C++ mẫu

```cpp
#include <bits/stdc++.h>
using namespace std;

// Sap xep: Chan dung truoc tang dan, Le dung sau giam dan
bool customCmp(int u, int v) {
    bool u_even = (abs(u) % 2 == 0);
    bool v_even = (abs(v) % 2 == 0);

    if (u_even != v_even) {
        return u_even; // Chan dung truoc Le
    }
    if (u_even) {
        return u < v;  // Ca hai deu chan: tang dan
    }
    return u > v;      // Ca hai deu le: giam dan
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    sort(a.begin(), a.end(), customCmp);

    for (int i = 0; i < n; i++) {
        if (i > 0) cout << ' ';
        cout << a[i];
    }
    cout << '\n';

    return 0;
}
```

#### 5. Quiz Trắc nghiệm nhanh

**Câu 1:** Độ phức tạp thời gian của hàm `std::sort()` trong C++ trên mảng $N$ phần tử là bao nhiêu?  
- A. $\mathcal{O}(N)$  
- B. $\mathcal{O}(N \log N)$  
- C. $\mathcal{O}(N^2)$  
- D. $\mathcal{O}(\log N)$  
👉 **Đáp án:** **B**. `std::sort` sử dụng thuật toán lai IntroSort kết hợp QuickSort, HeapSort và InsertionSort, đảm bảo $\mathcal{O}(N \log N)$ trong mọi trường hợp.

**Câu 2:** Khi viết hàm so sánh `bool cmp(int a, int b)`, nếu $a$ và $b$ bằng nhau ($a == b$), hàm phải trả về kết quả gì?  
- A. Luôn trả về `true`.  
- B. Luôn trả về `false`.  
- C. Trả về `1`.  
- D. Tùy ý trả về `true` hay `false`.  
👉 **Đáp án:** **B**. C++ yêu cầu tính chất Strict Weak Ordering, khi $a == b$ thì $a$ không thể đứng trước $b$ và ngược lại, bắt buộc trả về `false`.

**Câu 3:** Lệnh nào sau đây sắp xếp `vector<int> a` theo thứ tự giảm dần?  
- A. `sort(a.begin(), a.end());`  
- B. `sort(a.rbegin(), a.rend());`  
- C. `sort(a.begin(), a.end(), greater<int>());`  
- D. Cả B và C đều đúng.  
👉 **Đáp án:** **D**. Cả hai cách dùng `rbegin()/rend()` hoặc `greater<int>()` đều cho kết quả sắp xếp giảm dần chính xác.

#### 6. Bài tập thực hành nộp code tại chỗ

##### Bài thực hành 1.2A — Sắp xếp theo trị tuyệt đối
- **Đề bài:** Cho mảng $N$ số nguyên ($N \le 10^5, |A_i| \le 10^9$). Hãy sắp xếp mảng theo giá trị tuyệt đối tăng dần. Nếu hai số có cùng trị tuyệt đối, số âm đứng trước số dương.
- **Sample:**
  ```text
  Input:
  5
  -3 2 -1 3 1
  Output:
  -1 1 2 -3 3
  ```

##### Bài thực hành 1.2B — Số lớn nhất ghép từ hai số
- **Đề bài:** Cho hai số nguyên dương $A$ và $B$. Ghép $A$ và $B$ lại theo thứ tự nào để tạo thành số lớn hơn ($AB$ hay $BA$)?
- **Gợi ý:** Dùng so sánh xâu `to_string(a) + to_string(b) > to_string(b) + to_string(a)`.

#### 7. Tóm tắt bài

- Dùng `sort(a.begin(), a.end())` để đạt tốc độ tối đa $\mathcal{O}(N \log N)$.
- Dùng `greater<int>()` để sắp xếp giảm dần.
- Tự viết hàm `bool cmp()` khi cần quy tắc sắp xếp tùy biến, luôn tuân thủ nguyên tắc trả về `false` khi hai phần tử bằng nhau.

---

### Bài 1.3 — Các dạng bài toán ứng dụng Trật tự sắp xếp

#### 1. Mục tiêu bài

Sau Bài 1.3, em biết cách biến đổi bài toán thực tế bằng bước tiền xử lý sắp xếp, nhận diện được 2 dạng bài toán kinh điển: gom nhóm phần tử trùng lặp và tìm cặp kề nhau tối ưu.

#### 2. Dạng 1: Gom nhóm & Đếm số giá trị phân biệt

##### Bài toán
Cho dãy $N$ số nguyên ($N \le 10^5$). Đếm xem trong dãy có bao nhiêu số **khác nhau** (phân biệt)?

##### Nhận xét trực quan
- Nếu dãy chưa sắp xếp `[3, 1, 3, 2, 1]`, các số giống nhau nằm rải rác.
- Sau khi sắp xếp: `[1, 1, 2, 3, 3]`.
- **Tính chất vàng:** Các phần tử giống nhau sẽ tự động dồn lại thành từng khối đứng cạnh nhau!
- **Thuật toán:** Phần tử đầu tiên luôn là 1 giá trị mới. Từ phần tử thứ 2 trở đi, nếu $A[i] \ne A[i-1]$ thì ta vừa gặp thêm một giá trị phân biệt mới!

```cpp
sort(a.begin(), a.end());
int distinct_count = 1;
for (int i = 1; i < n; i++) {
    if (a[i] != a[i - 1]) {
        distinct_count++;
    }
}
```

#### 3. Dạng 2: Tìm khoảng cách nhỏ nhất giữa hai phần tử bất kỳ

##### Bài toán
Cho dãy $N$ số nguyên ($N \le 10^5$). Tìm độ chênh lệch nhỏ nhất $|A[i] - A[j]|$ giữa hai phần tử bất kỳ ($i \ne j$).

##### Nhận xét trực quan
- So sánh mọi cặp mất $\mathcal{O}(N^2)$ $\implies$ Quá thời gian.
- **Định lý khoảng cách:** Sau khi sắp xếp tăng dần $A_1 \le A_2 \le \dots \le A_N$, hai số có khoảng cách nhỏ nhất **bắt buộc phải là hai số đứng liền kề nhau** ($A_i$ và $A_{i+1}$).
- **Thuật toán:** Chỉ cần sắp xếp trong $\mathcal{O}(N \log N)$, sau đó duyệt 1 vòng lặp từ $0$ đến $N-2$ để tìm $\min(A_{i+1} - A_i)$ trong $\mathcal{O}(N)$!

```cpp
sort(a.begin(), a.end());
int min_diff = a[1] - a[0];
for (int i = 1; i < n - 1; i++) {
    min_diff = min(min_diff, a[i + 1] - a[i]);
}
```

#### 4. Cài đặt C++ mẫu (Tìm cặp số gần nhau nhất)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n) || n < 2) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    sort(a.begin(), a.end());

    int min_diff = a[1] - a[0];
    for (int i = 1; i < n - 1; i++) {
        min_diff = min(min_diff, a[i + 1] - a[i]);
    }

    cout << min_diff << '\n';

    return 0;
}
```

#### 5. Quiz Trắc nghiệm nhanh

**Câu 1:** Sau khi sắp xếp một mảng số nguyên tăng dần, các phần tử có giá trị bằng nhau sẽ nằm ở đâu?  
- A. Nằm ở đầu mảng.  
- B. Nằm ở cuối mảng.  
- C. Nằm liền kề nhau liên tục thành một đoạn.  
- D. Nằm rải rác ngẫu nhiên.  
👉 **Đáp án:** **C**. Sắp xếp đưa các giá trị bằng nhau về đứng cạnh nhau.

**Câu 2:** Để tìm độ chênh lệch nhỏ nhất giữa hai phần tử bất kỳ trong mảng đã sắp xếp tăng dần, ta cần kiểm tra những cặp phần tử nào?  
- A. Tất cả các cặp $(i, j)$ với $i < j$.  
- B. Chỉ cần kiểm tra các cặp phần tử đứng liền kề nhau $(A_i, A_{i+1})$.  
- C. Phần tử đầu tiên và phần tử cuối cùng.  
- D. Phần tử nhỏ nhất và phần tử lớn nhất.  
👉 **Đáp án:** **B**. Khoảng cách giữa hai số bất kỳ luôn lớn hơn hoặc bằng khoảng cách giữa hai số đứng liền kề ở giữa chúng.

#### 6. Bài tập thực hành nộp code tại chỗ

##### Bài thực hành 1.3A — Đếm số giá trị phân biệt
- **Đề bài:** Cho mảng $N$ số nguyên ($N \le 10^5, |A_i| \le 10^9$). Đếm số lượng giá trị khác nhau trong mảng.
- **Sample:**
  ```text
  Input:
  6
  3 1 4 1 5 9
  Output:
  5
  ```

##### Bài thực hành 1.3B — Tìm phần tử nhỏ thứ K
- **Đề bài:** Cho mảng $N$ số nguyên ($N \le 10^5$). In ra giá trị của phần tử nhỏ thứ $K$ sau khi sắp xếp tăng dần (chỉ số tính từ 1).
- **Sample:**
  ```text
  Input:
  5 3
  7 10 4 3 20
  Output:
  7
  ```

#### 7. Tóm tắt bài

- Sắp xếp biến bài toán so sánh mọi cặp ($\mathcal{O}(N^2)$) thành bài toán chỉ cần duyệt các cặp kề nhau ($\mathcal{O}(N)$).
- Ứng dụng tiêu biểu: Đếm số giá trị phân biệt, tìm khoảng cách nhỏ nhất, tìm phần tử thứ $K$.

---

### Bài 1.4 — Tổng kết chương & Bộ đề luyện tập phân tầng

#### 1. Bảng tóm tắt kiến thức cốt lõi

| Khái niệm | Ý nghĩa | Độ phức tạp | Cú pháp C++ |
|---|---|:---:|---|
| **Selection Sort** | Tìm phần tử nhỏ nhất và swap về vị trí đúng | $\mathcal{O}(N^2)$ | 2 vòng for lồng nhau + `swap(a[i], a[min_idx])` |
| **`std::sort`** | Hàm sắp xếp tối ưu của C++ | $\mathcal{O}(N \log N)$ | `sort(a.begin(), a.end())` |
| **Sắp xếp giảm dần** | Sắp xếp từ lớn đến bé | $\mathcal{O}(N \log N)$ | `sort(a.begin(), a.end(), greater<int>())` |
| **Custom Comparator** | Tùy biến quy tắc so sánh | $\mathcal{O}(N \log N)$ | `sort(a.begin(), a.end(), cmp)` |
| **Gom nhóm** | Gom các số bằng nhau lại cạnh nhau | $\mathcal{O}(N \log N)$ | `sort` rồi kiểm tra `a[i] != a[i-1]` |
| **Khoảng cách nhỏ nhất** | Tìm hiệu nhỏ nhất giữa 2 phần tử | $\mathcal{O}(N \log N)$ | `sort` rồi lấy $\min(a[i+1] - a[i])$ |

#### 2. Những bẫy lỗi thường gặp

| Lỗi thường gặp | Hậu quả | Cách phòng tránh |
|---|---|---|
| Dùng toán tử `<=` hoặc `>=` trong hàm `cmp` | Gây lỗi tràn bộ nhớ (Runtime Error) do vi phạm Strict Weak Ordering | Chỉ dùng `<` hoặc `>`, khi $a == b$ luôn trả về `false` |
| Quên dùng `#include <bits/stdc++.h>` | Báo lỗi hàm `sort()` chưa được khai báo | Luôn có `#include <bits/stdc++.h>` ở đầu chương trình |
| Truy cập ngoài mảng khi duyệt cặp kề nhau | Báo lỗi Out of Bound (`a[i+1]` khi $i = n-1$) | Vòng lặp duyệt cặp kề nhau chỉ chạy đến `i < n - 1` |

#### 3. Phiếu tự đánh giá năng lực

| Năng lực mục tiêu | Chưa chắc chắn | Làm được khi có gợi ý | Tự làm thành thạo |
|---|:---:|:---:|:---:|
| Mô phỏng và cài đặt Selection Sort bằng tay |  |  |  |
| Sử dụng thành thạo `std::sort` tăng/giảm |  |  |  |
| Tự viết hàm so sánh `bool cmp()` không bị lỗi |  |  |  |
| Đếm số giá trị phân biệt bằng `sort` trong $\mathcal{O}(N \log N)$ |  |  |  |
| Tìm cặp phần tử kề nhau tối ưu |  |  |  |

---

### Bộ đề luyện tập phân tầng (Problem Set)

#### TẦNG A — CỦNG CỐ CÚ PHÁP & NỀN TẢNG

##### Bài 1.4.1 — Dãy số tăng dần
- **Đề bài:** Đọc vào $N$ số nguyên và in các số theo thứ tự tăng dần.
- **Input:** Dòng 1 ghi số nguyên dương $N$ ($1 \le N \le 10^5$). Dòng 2 ghi $N$ số nguyên $A_i$ ($|A_i| \le 10^9$).
- **Output:** Dãy số sau khi sắp xếp tăng dần, cách nhau bởi dấu cách.
- **Sample:**
  ```text
  Input:
  5
  8 3 6 1 5
  Output:
  1 3 5 6 8
  ```

##### Bài 1.4.2 — Dãy số giảm dần
- **Đề bài:** Đọc vào $N$ số nguyên và in các số theo thứ tự giảm dần.
- **Input:** $N$ và dãy $N$ số nguyên ($N \le 10^5$).
- **Output:** Dãy số sau khi sắp xếp giảm dần.
- **Sample:**
  ```text
  Input:
  6
  4 9 1 9 3 2
  Output:
  9 9 4 3 2 1
  ```

##### Bài 1.4.3 — Tìm phần tử lớn thứ K
- **Đề bài:** Cho mảng $N$ số nguyên ($1 \le K \le N \le 10^5$). Tìm phần tử lớn thứ $K$ trong mảng.
- **Sample:**
  ```text
  Input:
  5 2
  10 30 20 50 40
  Output:
  40
  ```

---

#### TẦNG B — VẬN DỤNG MẪU & KỸ THUẬT

##### Bài 1.4.4 — Sắp xếp chẵn trước lẻ sau
- **Đề bài:** Cho dãy $N$ số nguyên. Hãy sắp xếp sao cho các số chẵn đứng trước (tăng dần), các số lẻ đứng sau (tăng dần).
- **Sample:**
  ```text
  Input:
  6
  5 2 8 7 1 4
  Output:
  2 4 8 1 5 7
  ```

##### Bài 1.4.5 — Cặp đôi hoàn hảo
- **Đề bài:** Cho dãy $N$ số nguyên ($N \le 10^5$). Tìm hai phần tử có độ chênh lệch $|A_i - A_j|$ nhỏ nhất ($i \ne j$). In ra độ chênh lệch nhỏ nhất đó.
- **Sample:**
  ```text
  Input:
  4
  1 9 5 3
  Output:
  2
  ```
  *(Giải thích: Cặp $(1, 3)$ và $(3, 5)$ đều có hiệu là 2).*

##### Bài 1.4.6 — Đếm phần tử duy nhất
- **Đề bài:** Cho mảng $N$ số nguyên. Đếm xem có bao nhiêu phần tử chỉ xuất hiện **đúng 1 lần** trong mảng.
- **Sample:**
  ```text
  Input:
  6
  2 3 2 5 3 7
  Output:
  2
  ```
  *(Giải thích: Có 2 số chỉ xuất hiện 1 lần là số 5 và số 7).*

---

#### TẦNG C — NÂNG CAO & VẬN DỤNG THỰC TẾ

##### Bài 1.4.7 — Ghép số lớn nhất
- **Đề bài:** Cho $N$ số nguyên không âm ($N \le 10^5, A_i \le 10^9$). Hãy sắp xếp và ghép tất cả các số lại với nhau để tạo thành số có giá trị lớn nhất.
- **Gợi ý:** Dùng comparator xâu `bool cmp(string a, string b) { return a + b > b + a; }`.
- **Sample:**
  ```text
  Input:
  4
  3 30 34 5 9
  Output:
  9534330
  ```

##### Bài 1.4.8 — Thu gom rác tối ưu
- **Đề bài:** Trên một trục đường thẳng có $N$ thùng rác tại các tọa độ $X_1, X_2, \dots, X_N$. Một xe chở rác có thể chở tối đa 2 thùng mỗi chuyến. Tìm số chuyến xe ít nhất để thu gom hết các thùng rác nếu mỗi chuyến tổng khoảng cách từ gốc không vượt quá $D$.
- **Gợi ý:** Sắp xếp tọa độ tăng dần và dùng kỹ thuật tham lam kết hợp hai đầu mút.

---

### Code tham chiếu tổng hợp toàn chương

```cpp
#include <bits/stdc++.h>
using namespace std;

// 1. Thuat toan Selection Sort O(N^2)
void selectionSort(vector<int> &a) {
    int n = a.size();
    for (int i = 0; i < n - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < n; j++) {
            if (a[j] < a[min_idx]) {
                min_idx = j;
            }
        }
        swap(a[i], a[min_idx]);
    }
}

// 2. Custom Comparator: Chan truoc (tang dan), Le sau (tang dan)
bool customComparator(int u, int v) {
    bool u_even = (abs(u) % 2 == 0);
    bool v_even = (abs(v) % 2 == 0);
    if (u_even != v_even) {
        return u_even;
    }
    return u < v;
}

// 3. Dem so gia tri phan biet O(N log N)
int countDistinct(vector<int> a) {
    if (a.empty()) return 0;
    sort(a.begin(), a.end());
    int cnt = 1;
    for (size_t i = 1; i < a.size(); i++) {
        if (a[i] != a[i - 1]) cnt++;
    }
    return cnt;
}

// 4. Tim khoang cach nho nhat O(N log N)
int minDifference(vector<int> a) {
    if (a.size() < 2) return 0;
    sort(a.begin(), a.end());
    int min_diff = a[1] - a[0];
    for (size_t i = 1; i < a.size() - 1; i++) {
        min_diff = min(min_diff, a[i + 1] - a[i]);
    }
    return min_diff;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    cout << "Distinct elements: " << countDistinct(a) << "\n";
    cout << "Min difference: " << minDifference(a) << "\n";

    return 0;
}
```

---

## Chương 2 — Tham lam

### Bản đồ chương

| Trường | Nội dung |
|---|---|
| Mục tiêu | Hiểu cách xây dựng lời giải bằng các lựa chọn cục bộ có căn cứ |
| Kiến thức cần có | Sắp xếp, comparator, vòng lặp, điều kiện, `vector` và mô tả Input–Process–Output |
| Phạm vi | Khái niệm tham lam, chọn hoạt động, chứng minh đổi chỗ, phản ví dụ và các biến thể cơ bản |
| Số bài | 6 bài học, kết hợp mô phỏng, code, lập luận và bài chuyển giao |

**Vị trí trong lộ trình:** Sách trình bày Chương 2 ngay sau Chương 1 để tạo mạch đọc liền nhau từ Sorting sang Greedy. Giáo viên có thể điều chỉnh thứ tự dạy theo mức độ lớp học và teaching sequence của trung tâm, miễn là học sinh đã có prerequisite về sắp xếp, vòng lặp và so sánh.

### Learning outcomes

Sau chương này, em có thể:

1. Giải thích thuật toán tham lam bằng một ví dụ cụ thể.
2. Phân biệt lựa chọn cục bộ với mục tiêu tối ưu toàn cục.
3. Nhận biết bài toán chọn nhiều hoạt động không giao nhau.
4. Sắp xếp hoạt động theo thời điểm kết thúc và duyệt để chọn hoạt động hợp lệ.
5. Mô phỏng trạng thái sau từng lựa chọn.
6. Trình bày vì sao chọn hoạt động kết thúc sớm là an toàn.
7. Dùng phản ví dụ để kiểm tra một quy tắc tham lam đáng ngờ.
8. Phân biệt bài dùng được tham lam với bài cần phân tích thêm hoặc cân nhắc quy hoạch động, tìm kiếm.
9. Phân tích độ phức tạp `O(N log N)` của lời giải chọn hoạt động.
10. Giải thích sau khi chọn một phương án thì phần còn lại của bài toán thay đổi như thế nào.

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

#### Gom hai mốc thời gian bằng vector lồng nhau (`vector<vector<int>>`)

Mỗi hoạt động gồm hai thông tin đi liền nhau: thời điểm bắt đầu (`start`) và thời điểm kết thúc (`finish`). Học sinh đã quen với mảng 2 chiều; trong C++, ta lưu danh sách hoạt động dưới dạng một `vector<vector<int>>`, trong đó mỗi phần tử là một vector 2 số nguyên `{finish, start}`:

```cpp
vector<int> activity = {finish, start};
```

Khi đặt `finish` ở vị trí `0` và `start` ở vị trí `1`, hàm `sort()` mặc định của C++ sẽ **tự động sắp xếp tăng dần theo cột 0 (`finish`)**; nếu hai hoạt động có cùng thời điểm kết thúc, `sort()` sẽ tự động so sánh tiếp cột 1 (`start`).

Cách làm này hoàn toàn dựa trên kiểu dữ liệu `vector` quen thuộc, không cần học thêm cú pháp mới.

#### Code đầy đủ

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    // Lưu từng hoạt động dưới dạng vector 2 phần tử: {finish, start}
    vector<vector<int>> activities(n, vector<int>(2));
    for (int i = 0; i < n; i++) {
        int start, finish;
        cin >> start >> finish;
        activities[i] = {finish, start};
    }

    // sort() mặc định tự động sắp xếp tăng dần theo cột 0 (finish)
    sort(activities.begin(), activities.end());

    int answer = 0;
    int lastFinish = -1;

    for (int i = 0; i < n; i++) {
        int finish = activities[i][0];
        int start = activities[i][1];

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
| `start` (`activities[i][1]`) | Hoạt động này bắt đầu lúc nào? |
| `finish` (`activities[i][0]`) | Hoạt động này kết thúc lúc nào? |
| `lastFinish` | Lựa chọn gần nhất kết thúc lúc nào? |

Nếu chương trình chọn hai hoạt động giao nhau, hãy kiểm tra điều kiện `start >= lastFinish`. Nếu số lượng thấp bất thường, hãy kiểm tra comparator có thật sự sắp xếp theo `finish` hay không.

#### Tự kiểm tra

1. Vì sao phải sắp xếp trước khi duyệt?
2. `lastFinish` được cập nhật vào lúc nào?
3. Nếu dùng `start > lastFinish` thay vì `>=`, chương trình sẽ sai ở trường hợp nào?
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

Trong lúc chương trình chạy, ta giữ **bất biến (invariant)**, tức là điều luôn đúng sau mỗi bước:

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

Nếu một lựa chọn hiện tại có nhiều trạng thái tương lai khác nhau và chưa thể chứng minh việc chọn sớm là an toàn, ta **chưa đủ cơ sở để dùng Greedy**. Khi đó cần phân tích thêm mục tiêu, trạng thái và các lựa chọn; có thể cân nhắc:

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

- **Input:** Năm hoạt động `[1,4]`, `[3,5]`, `[0,6]`, `[5,7]`, `[8,9]`.
- **Output:** Danh sách hoạt động được chọn và số lượng hoạt động.
- **Ví dụ:** Một đáp án tối ưu là `[1,4]`, `[5,7]`, `[8,9]`, nên số lượng là `3`.
- **Expected evidence:** Bảng sắp xếp theo `finish`, các hoạt động được chọn theo thứ tự và lý do mỗi hoạt động bị bỏ qua.

##### Bài 2.6.2 — Kiểm tra hai hoạt động

Cho hai hoạt động `[s1, f1]` và `[s2, f2]`. In `YES` nếu có thể chọn cả hai theo đúng thứ tự đã cho, tức là hoạt động thứ hai bắt đầu không sớm hơn thời điểm kết thúc của hoạt động thứ nhất; ngược lại in `NO`.

- **Input:** Một dòng gồm `s1 f1 s2 f2`, với `0 <= s1 < f1` và `0 <= s2 < f2`.
- **Output:** In `YES` hoặc `NO`.
- **Ví dụ:** `[2,5]` rồi `[5,8]` cho `YES`; `[2,5]` rồi `[4,8]` cho `NO`.
- **Expected evidence:** Dùng đúng điều kiện `s2 >= f1`, đặc biệt không loại trường hợp hai hoạt động nối tiếp tại cùng một mốc.

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

- **Input:** `N` và `N` cặp `start finish`, với `0 <= start < finish`.
- **Output:** Dòng đầu là số hoạt động được chọn; dòng sau in các cặp `start finish` theo thứ tự đã chọn.
- **Yêu cầu:** Các hoạt động được in ra không giao nhau và giữ nguyên dữ liệu của từng hoạt động.
- **Expected evidence:** Có sort theo `finish`, điều kiện chọn đúng và danh sách in ra có thể kiểm tra được bằng mắt.

##### Bài 2.6.8 — Tìm phản ví dụ

Viết một input có ít nhất bốn hoạt động để chứng minh quy tắc “chọn hoạt động bắt đầu sớm nhất” không luôn cho số lượng lớn nhất.

Bài làm cần có ba phần: input, kết quả của quy tắc sai và một lời giải tốt hơn. **Expected evidence:** Em chỉ ra được số lượng của hai cách và giải thích vì sao input đó đủ để bác bỏ quy tắc sai.

#### Tầng C — Chuyển giao

##### Bài 2.6.9 — Lập lịch có điểm thưởng

Mỗi hoạt động có thêm một điểm thưởng. Mục tiêu là chọn các hoạt động không giao nhau để tổng điểm lớn nhất. Đây là **bài thảo luận có hướng dẫn**, chưa yêu cầu viết lời giải tối ưu hoàn chỉnh.

- **Dữ liệu mẫu:** `A = [1,4]` có điểm `5`, `B = [4,7]` có điểm `5`, `C = [1,7]` có điểm `12`.
- **Nhiệm vụ:** So sánh lựa chọn theo thời điểm kết thúc sớm với lựa chọn có tổng điểm lớn hơn.
- **Expected evidence:** Em chỉ ra được rằng `A + B` có tổng điểm `10`, còn `C` có điểm `12`, từ đó giải thích vì sao tiêu chí của bài chọn nhiều hoạt động không thể áp dụng nguyên xi.

##### Bài 2.6.10 — Đổi tiền và phản ví dụ

Cho các mệnh giá và số tiền cần đổi, với mục tiêu dùng **ít đồng nhất cho input đang xét**. Kiểm tra chiến lược chọn mệnh giá lớn nhất trước. Nếu chiến lược sai trên input đó, đưa ra một cách đổi tốt hơn và giải thích vì sao đây là phản ví dụ; không kết luận về mọi hệ mệnh giá từ một input duy nhất.

- **Ví dụ:** Mệnh giá `1, 3, 4`, số tiền `6`: Greedy cho `4+1+1`, nhưng đáp án tốt hơn là `3+3`.
- **Expected evidence:** Nêu rõ mục tiêu, dãy lựa chọn của Greedy, cách đổi tốt hơn và số đồng của mỗi cách.

##### Bài 2.6.11 — Chọn việc theo thời hạn

Mỗi công việc cần đúng một đơn vị thời gian và có thời hạn hoàn thành. Trong mỗi thời điểm `1, 2, ., D`, ta chỉ làm được một công việc; công việc có deadline `d` phải được thực hiện không muộn hơn thời điểm `d`. Hãy thử xây dựng chiến lược tham lam để thực hiện nhiều công việc nhất.

- **Dữ liệu mẫu:** Có năm công việc với deadline `1, 1, 2, 2, 3`.
- **Expected evidence:** Em giải thích được vì sao tối đa có thể làm `3` công việc trong ba vị trí thời gian, đồng thời nêu tiêu chí sắp xếp hoặc câu hỏi cần kiểm tra trước khi code.
- **Giới hạn:** Đây là bài mở rộng có hướng dẫn; chưa yêu cầu học thuộc một công thức mới hay triển khai priority queue.

##### Bài 2.6.12 — Nói rõ vì sao

Với mỗi mô tả, hãy trả lời `DÙNG GREEDY`, `CẦN KIỂM TRA THÊM` hoặc `KHÔNG ĐỦ THÔNG TIN`, rồi giải thích:

1. Chọn nhiều hoạt động không giao nhau nhất.
2. Đổi tiền bằng các mệnh giá `1, 3, 4`, số tiền `6`, với mục tiêu dùng ít đồng nhất.
3. Chọn dãy có tổng điểm lớn nhất nhưng các phần tử có thể xung đột.
4. Chọn các đoạn không giao nhau nhưng muốn tổng độ dài lớn nhất.
5. Chọn một số lượng lớn nhất trong một lần duyệt.

Điểm quan trọng là em phải nêu mục tiêu và lý do, không chỉ ghi tên thuật toán.

**Rubric cho Bài 2.6.12:** Mỗi câu được xem là đạt khi em nêu được mục tiêu của bài, chỉ ra tiêu chí hoặc thông tin còn thiếu, và đưa ra lý do/ phản ví dụ phù hợp. Một câu chỉ ghi tên thuật toán mà không có giải thích chưa được tính là hoàn thành.

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

#### Rubric hoàn thành chương

| Bằng chứng | Đạt khi |
|---|---|
| Mô phỏng | Chọn đúng các hoạt động hợp lệ và cập nhật đúng `lastFinish` |
| Code | Sort theo `finish`, dùng điều kiện `start >= lastFinish`, không chọn hai hoạt động giao nhau |
| Chứng minh | Nêu được ý nghĩa của `finish(A) <= finish(B)` trong lập luận đổi chỗ |
| Phản ví dụ | Tạo được input làm một tiêu chí sai cho kết quả kém hơn |
| Phân tích | Tách được chi phí sort `O(N log N)` và duyệt `O(N)` |
| Chuyển giao | Nhận ra khi mục tiêu đổi từ số lượng sang tổng giá trị thì cần phân tích lại |

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

    // Lưu từng hoạt động dưới dạng vector 2 phần tử: {finish, start}
    vector<vector<int>> activities(n, vector<int>(2));
    for (int i = 0; i < n; i++) {
        int start, finish;
        cin >> start >> finish;
        activities[i] = {finish, start};
    }

    // sort() mặc định tự động sắp xếp tăng dần theo cột 0 (finish)
    sort(activities.begin(), activities.end());

    int answer = 0;
    int lastFinish = -1;

    for (int i = 0; i < n; i++) {
        int finish = activities[i][0];
        int start = activities[i][1];

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

## Ghi chú mở rộng cho giáo viên

Các chủ đề như lập lịch công việc có thời hạn, ba lô phân số, Kruskal hoặc chia tải bằng hàng đợi ưu tiên đều có thể dùng Greedy, nhưng không nên đưa tất cả vào bài đầu tiên. Trước hết, học sinh cần nắm vững bốn năng lực: nhận ra mục tiêu tối ưu, viết tiêu chí lựa chọn, mô phỏng trạng thái và bảo vệ lựa chọn bằng lập luận hoặc kiểm tra phản ví dụ.

## Ma trận alignment nội bộ

| Outcome | Evidence chính | Tiêu chí đạt |
|---|---|---|
| `LO-01`, `LO-02` — Giải thích Greedy và phân biệt cục bộ/toàn cục | Bài 2.1, Bài 2.6.12 | Nêu được mục tiêu, lựa chọn và lý do không chọn tùy tiện |
| `LO-03`, `LO-05` — Nhận biết interval scheduling và mô phỏng trạng thái | Bài 2.2, Bài 2.6.1, 2.6.5, 2.6.6 | Mô hình hóa đúng khoảng, điều kiện nối tiếp và `lastFinish` |
| `LO-04` — Viết lời giải chọn hoạt động | Bài 2.3, Bài 2.6.3–2.6.7 | Sort theo `finish`, kiểm tra `start >= lastFinish`, cập nhật trạng thái |
| `LO-06`, `LO-10` — Giải thích tính đúng đắn và phần bài toán còn lại | Bài 2.4, rubric chương | Trình bày được lập luận đổi chỗ và bất biến (invariant) |
| `LO-07` — Tìm giới hạn/phản ví dụ | Bài 2.1, Bài 2.5, Bài 2.6.8–2.6.10 | Tạo hoặc phân tích được phản ví dụ có mục tiêu rõ |
| `LO-09` — Phân tích độ phức tạp | Bài 2.3, rubric chương | Tách được chi phí sort và chi phí duyệt |
| `LO-08` — Chuyển giao sang bài biến thể | Bài 2.6.9–2.6.12 | Nhận ra khi mục tiêu/điều kiện đổi thì tiêu chí Greedy phải được kiểm tra lại |

Ma trận này là ghi chú biên soạn, không đồng bộ vào bản in học sinh.

---

## Chương 3 — Số học

### Bản đồ chương

| Trường | Nội dung |
|---|---|
| Mục tiêu | Hiểu bản chất các quy luật số học để giảm số phép tính từ hàng tỷ bước xuống vài chục thao tác |
| Kiến thức cần có | Vòng lặp `for`/`while`, câu lệnh `if-else`, toán tử chia dư `%`, mảng/vector, kiểu dữ liệu `long long` |
| Phạm vi | Ước và bội, thuật toán Euclid tìm GCD, tính LCM an toàn, kiểm tra số nguyên tố $\mathcal{O}(\sqrt{N})$, phân tích thừa số và Sàng Eratosthenes |
| Số bài | 6 bài học lý thuyết & thực hành + 1 bài tổng kết và bài tập phân tầng |

### Learning outcomes

Sau chương này, em có thể:
1. Giải thích quy luật đối xứng của các cặp ước và tìm toàn bộ ước trong $\mathcal{O}(\sqrt{N})$.
2. Mô phỏng và cài đặt thuật toán Euclid tìm ước chung lớn nhất (GCD) trong $\mathcal{O}(\log(\min(A, B)))$.
3. Tính bội chung nhỏ nhất (LCM) an toàn bằng quy tắc "chia trước khi nhân" chống tràn số nguyên 64-bit.
4. Kiểm tra một số nguyên có phải số nguyên tố trong $\mathcal{O}(\sqrt{N})$ với bước nhảy $6k \pm 1$.
5. Phân tích một số nguyên dương thành tích các thừa số nguyên tố bằng thuật toán chia dần.
6. Cài đặt và sử dụng Sàng Eratosthenes $\mathcal{O}(N \log \log N)$ để trả lời nhanh các truy vấn số nguyên tố.
7. Xử lý chính xác các trường hợp biên: $N = 0, 1$, số âm và số lớn vượt kiểu `int` ($10^9 \to 10^{18}$).

### Câu hỏi trung tâm của chương

> **Làm thế nào để kiểm tra, đếm và phân tích tính chất chia hết của một số nguyên lớn mà không làm chương trình bị quá thời gian hay tràn bộ nhớ?**

---

### Bài 3.1 — Ước, bội và quy luật đối xứng cặp ước

#### Mục tiêu bài

Sau Bài 3.1, em có thể giải thích định nghĩa ước - bội, nhận biết quy luật đối xứng qua $\sqrt{N}$ và viết được chương trình tìm toàn bộ ước của số nguyên $N \le 10^{12}$ trong thời gian dưới $0.01$ giây.

#### Khởi động

Giả sử em có $N = 36$ chiếc kẹo và muốn chia đều vào các túi, mỗi túi có đúng $d$ chiếc.
- Nếu mỗi túi có $d = 2$ chiếc $\implies$ cần $36 / 2 = 18$ túi. Cặp số $(2, 18)$ cùng xuất hiện từ một phép chia hết!
- Liệu em có cần thử duyệt từ $1$ đến tận $36$ để tìm tất cả các cách chia không?

#### Ước, bội và quy luật đối xứng

- Số nguyên dương $d$ là **ước** của $N$ nếu phép chia $N$ cho $d$ có phần dư bằng $0$ (`N % d == 0`). Khi đó $N$ là **bội** của $d$.
- Nếu $d$ là một ước của $N$ thì thương số $N / d$ cũng chắc chắn là một ước của $N$:
  $$d \times \frac{N}{d} = N$$
- Trong mỗi cặp ước $(d, N/d)$, số nhỏ hơn không bao giờ vượt quá $\sqrt{N}$. Vì nếu cả hai số đều lớn hơn $\sqrt{N}$ thì tích của chúng sẽ lớn hơn $\sqrt{N} \times \sqrt{N} = N$ (vô lý).

> **Chỉ cần duyệt $d$ từ $1$ đến $\lfloor\sqrt{N}\rfloor$ ($d \times d \le N$). Với mỗi ước $d$ tìm thấy, ta lấy thêm ước đối xứng $N/d$.**

#### Mô phỏng từng lượt tìm ước của $N = 36$ ($\sqrt{36} = 6$)

| Lượt duyệt $d$ | $36 \% d == 0$? | Cặp ước thu được $(d, 36/d)$ | Ghi chú |
|:---:|:---:|:---:|---|
| $1$ | Có | $(1, 36)$ | Lấy cả 1 và 36 |
| $2$ | Có | $(2, 18)$ | Lấy cả 2 và 18 |
| $3$ | Có | $(3, 12)$ | Lấy cả 3 và 12 |
| $4$ | Có | $(4, 9)$ | Lấy cả 4 và 9 |
| $5$ | Không | Bỏ qua | 36 không chia hết cho 5 |
| $6$ | Có | $(6, 6)$ | $d = N/d \implies$ chỉ lấy một số 6 |

#### Pseudocode

```text
divisors = danh sách rỗng
for d từ 1 đến khi d * d > n:
    nếu n % d == 0:
        thêm d vào divisors
        nếu d != n / d:
            thêm (n / d) vào divisors
sắp xếp divisors tăng dần
in số lượng và danh sách ước
```

#### Code C++

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;

    vector<long long> divisors;
    for (long long d = 1; d * d <= n; d++) {
        if (n % d == 0) {
            divisors.push_back(d);
            if (d * d != n) {
                divisors.push_back(n / d);
            }
        }
    }

    sort(divisors.begin(), divisors.end());

    cout << divisors.size() << '\n';
    for (int i = 0; i < (int)divisors.size(); i++) {
        if (i > 0) cout << ' ';
        cout << divisors[i];
    }
    cout << '\n';

    return 0;
}
```

#### Điều cần theo dõi khi debug

| Biến | Câu hỏi kiểm tra |
|---|---|
| `d` | Đã khai báo kiểu `long long` chưa? (Nếu khai báo `int d`, khi $N = 10^{12}$ thì `d * d` sẽ tràn số gây lặp vô hạn). |
| `d * d != n` | Có bị trùng ước khi $N$ là số chính phương ($36 = 6 \times 6$) không? |
| `d * d <= n` | Đã dùng phép nhân nguyên thay vì gọi hàm `sqrt(n)` chưa? |

#### Tự kiểm tra

1. Vì sao trong mỗi cặp ước $(d, N/d)$ luôn có ít nhất một số $\le \sqrt{N}$?
2. Số nguyên dương $N$ có số lượng ước là số lẻ khi và chỉ khi $N$ là số gì?
3. Với $N = 10^{12}$, vòng lặp `for` chạy tối đa bao nhiêu lần?

#### Luyện tập ngắn

- **LT 3.1A:** Viết chương trình tính tổng tất cả các ước của $N$ ($N \le 10^9$) trong $\mathcal{O}(\sqrt{N})$.
- **LT 3.1B:** Kiểm tra xem số $N$ có phải là số hoàn hảo không (số hoàn hảo bằng tổng các ước thực sự nhỏ hơn nó, ví dụ $6 = 1 + 2 + 3$).

#### Tóm tắt bài

Ước số luôn đi theo từng cặp $(d, N/d)$. Duyệt $d$ từ $1$ đến $\sqrt{N}$ giúp giảm độ phức tạp từ $\mathcal{O}(N)$ xuống $\mathcal{O}(\sqrt{N})$, giải quyết nhẹ nhàng bài toán $N \le 10^{12}$.

---

### Bài 3.2 — Ước chung lớn nhất (GCD) và Thuật toán Euclid

#### Mục tiêu bài

Sau Bài 3.2, em hiểu bản chất của ước chung lớn nhất, nắm vững thuật toán Euclid $\mathcal{O}(\log(\min(A, B)))$ và tự tin cài đặt hàm `gcd` để rút gọn phân số hoặc tìm chu kỳ chung.

#### Khởi động

Em có một mảnh sân hình chữ nhật dài $105\text{ cm}$, rộng $45\text{ cm}$. Em muốn lát kín sân bằng các viên gạch vuông có kích thước lớn nhất mà không phải cắt gọt viên nào.
- Cạnh viên gạch phải là ước chung của cả $105$ và $45$.
- Viên gạch lớn nhất có cạnh bằng **Ước chung lớn nhất** $\gcd(105, 45)$.

#### Thuật toán Euclid

- **Ước chung lớn nhất ($\gcd(a, b)$):** Là số nguyên dương lớn nhất chia hết cả $a$ và $b$. Nếu $\gcd(a, b) = 1$, ta gọi $a$ và $b$ là hai số **nguyên tố cùng nhau**.
- **Định lý Euclid:** Ước chung lớn nhất của hai số không thay đổi khi thay số lớn bằng số dư của phép chia số lớn cho số nhỏ:
  $$\gcd(a, b) = \gcd(b, a \% b)$$
  Quá trình dừng lại khi số dư bằng $0$, khi đó số còn lại chính là $\gcd$.

#### Mô phỏng từng bước cho cặp $(a = 105, b = 45)$

| Bước | $a$ | $b$ | Phép chia dư $a \% b$ | Cập nhật tiếp theo |
|:---:|:---:|:---:|:---:|---|
| 1 | $105$ | $45$ | $105 \% 45 = 15$ | $a = 45, b = 15$ |
| 2 | $45$ | $15$ | $45 \% 15 = 0$ | $a = 15, b = 0$ |
| 3 | $15$ | $0$ | Dừng vì $b = 0$ | **Kết quả: $\gcd = 15$** |

Sau mỗi bước, số dư giảm đi ít nhất một nửa. Thuật toán chạy với độ phức tạp $\mathcal{O}(\log(\min(A, B)))$, với hai số $10^{18}$ chỉ mất chưa tới 60 phép chia dư!

#### Pseudocode

```text
hàm gcd(a, b):
    trong khi b != 0:
        r = a % b
        a = b
        b = r
    trả về a
```

#### Code C++

```cpp
#include <bits/stdc++.h>
using namespace std;

long long gcd(long long a, long long b) {
    while (b != 0) {
        long long r = a % b;
        a = b;
        b = r;
    }
    return a;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, b;
    if (!(cin >> a >> b)) return 0;

    long long g = gcd(a, b);
    cout << a / g << " " << b / g << '\n';

    return 0;
}
```

#### Điều cần theo dõi khi debug

| Biến | Câu hỏi kiểm tra |
|---|---|
| `b != 0` | Vòng lặp dừng khi $b = 0$, kết quả trả về là $a$. |
| $a < b$ | Nếu truyền vào $a = 45, b = 105$, bước đầu tiên $45 \% 105 = 45 \implies$ thuật toán tự động đảo lại thành $a = 105, b = 45$. |

#### Tự kiểm tra

1. Điều kiện dừng của thuật toán Euclid là gì?
2. Hai số nguyên dương được gọi là nguyên tố cùng nhau khi $\gcd(a, b)$ bằng bao nhiêu?
3. Muốn tìm $\gcd$ của 3 số $a, b, c$, ta làm thế nào?

#### Luyện tập ngắn

- **LT 3.2A:** Nhập vào dãy $N$ số nguyên ($N \le 10^5, A_i \le 10^9$). Tìm ước chung lớn nhất của cả dãy.
- **LT 3.2B:** Rút gọn phân số $\frac{A}{B}$ về dạng tối giản $\frac{P}{Q}$.

#### Tóm tắt bài

Thuật toán Euclid $\gcd(a, b) = \gcd(b, a \% b)$ chạy với tốc độ logarithmic $\mathcal{O}(\log(\min(A, B)))$, là công cụ nhanh nhất để tìm ước chung và rút gọn phân số.

---

### Bài 3.3 — Bội chung nhỏ nhất (LCM) và Kỹ thuật chống tràn số

#### Mục tiêu bài

Sau Bài 3.3, em hiểu mối liên hệ giữa GCD và LCM, nắm vững quy tắc **"Chia trước khi Nhân"** để tính LCM của các số lớn mà không bao giờ bị tràn số.

#### Khởi động

Hai chiếc xe cùng xuất phát từ bến lúc 6h sáng. Xe A cứ $12$ phút quay lại bến một lần, xe B cứ $18$ phút quay lại bến một lần. Sau bao lâu hai xe lại cùng lúc về bến?
- Khoảng thời gian đó chính là **Bội chung nhỏ nhất** $\text{lcm}(12, 18) = 36$ phút.

#### Mối liên hệ và Bẫy tràn số

- **Bội chung nhỏ nhất ($\text{lcm}(a, b)$):** Số nguyên dương nhỏ nhất chia hết cho cả $a$ và $b$.
- **Công thức liên hệ:**
  $$a \times b = \gcd(a, b) \times \text{lcm}(a, b) \implies \text{lcm}(a, b) = \frac{a \times b}{\gcd(a, b)}$$
- **Bẫy tràn số:** Nếu tính `(a * b) / gcd(a, b)` khi $a, b = 10^9$, tích $a \times b = 10^{18}$ sẽ tràn số `int` ngay lập tức.
- **Quy tắc an toàn:** Vì $a$ luôn chia hết cho $\gcd(a, b)$, ta chia trước rồi mới nhân:
  $$\text{lcm}(a, b) = \left( \frac{a}{\gcd(a, b)} \right) \times b$$

#### Pseudocode

```text
hàm lcm(a, b):
    nếu a == 0 hoặc b == 0: trả về 0
    trả về (a / gcd(a, b)) * b
```

#### Code C++

```cpp
#include <bits/stdc++.h>
using namespace std;

long long gcd(long long a, long long b) {
    while (b != 0) {
        long long r = a % b;
        a = b;
        b = r;
    }
    return a;
}

long long lcm(long long a, long long b) {
    if (a == 0 || b == 0) return 0;
    return (a / gcd(a, b)) * b;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, b;
    if (!(cin >> a >> b)) return 0;

    cout << lcm(a, b) << '\n';

    return 0;
}
```

#### Điều cần theo dõi khi debug

| Thao tác | Đánh giá |
|---|---|
| `(a * b) / gcd(a, b)` | ❌ Nguy hiểm, dễ tràn số trung gian. |
| `(a / gcd(a, b)) * b` |  An toàn, luôn là phép chia hết. |

#### Tự kiểm tra

1. Tại sao phép chia `a / gcd(a, b)` không bao giờ có dư?
2. Nếu $a$ và $b$ nguyên tố cùng nhau thì $\text{lcm}(a, b)$ bằng bao nhiêu?

#### Luyện tập ngắn

- **LT 3.3A:** Nhập vào 3 số $A, B, C \le 10^6$. Tính $\text{lcm}(A, B, C)$.
- **LT 3.3B:** Tìm số nguyên dương nhỏ nhất chia cho cả 4, 5, 6 đều dư 1.

#### Tóm tắt bài

$\text{lcm}(a, b) = (a / \gcd(a, b)) \times b$. Luôn **chia trước khi nhân** để bảo vệ chương trình khỏi bẫy tràn số 64-bit.

---

### Bài 3.4 — Số nguyên tố và Kỹ thuật kiểm tra tối ưu $\mathcal{O}(\sqrt{N})$

#### Mục tiêu bài

Sau Bài 3.4, em hiểu định nghĩa số nguyên tố, cài đặt được hàm kiểm tra nguyên tố $\mathcal{O}(\sqrt{N})$ và nắm được kỹ thuật tăng tốc bước nhảy $6k \pm 1$.

#### Khởi động

Số nguyên tố giống như các "viên gạch nguyên tử" của thế giới số tự nhiên — chúng không thể phân tách thành tích của các số nhỏ hơn. Mọi thuật toán mã hóa ngân hàng và bảo mật ngày nay đều dựa trên tính chất này.

#### Khái niệm & Thuật toán kiểm tra

- **Số nguyên tố:** Là số nguyên $> 1$ chỉ có đúng 2 ước nguyên dương phân biệt là $1$ và chính nó ($2, 3, 5, 7, 11, 13, \dots$).
- Số $0$ và $1$ **không phải** là số nguyên tố.
- **Quy tắc $\mathcal{O}(\sqrt{N})$:** Nếu $N > 1$ là hợp số, nó luôn có ít nhất một ước nguyên tố $d \le \sqrt{N}$. Do đó, chỉ cần kiểm tra xem $N$ có chia hết cho số nào từ $2$ đến $\sqrt{N}$ không.
- **Tối ưu bước nhảy $6k \pm 1$:** Mọi số nguyên tố $> 3$ đều có dạng $6k - 1$ hoặc $6k + 1$. Sau khi kiểm tra chia hết cho 2 và 3, ta chỉ cần thử các số $i$ và $i + 2$ với bước nhảy $i += 6$, giúp giảm bớt $2/3$ số phép chia.

#### Mô phỏng kiểm tra $N = 29$ ($\sqrt{29} \approx 5.38$)

| Bước | Số thử chia | $29 \% i == 0$? | Kết luận |
|:---:|:---:|:---:|---|
| 1 | $2$ | Không | 29 là số lẻ |
| 2 | $3$ | Không | 29 không chia hết cho 3 |
| 3 | $5$ ($i = 5$) | Không | $5 \times 5 = 25 \le 29$, không chia hết |
| 4 | $7$ ($i + 2 = 7$) | Bỏ qua | $7 \times 7 = 49 > 29$, dừng vòng lặp |

👉 **Kết luận:** 29 là số nguyên tố.

#### Pseudocode

```text
hàm isPrime(n):
    nếu n < 2: trả về false
    nếu n == 2 hoặc n == 3: trả về true
    nếu n % 2 == 0 hoặc n % 3 == 0: trả về false
    i = 5
    trong khi i * i <= n:
        nếu n % i == 0 hoặc n % (i + 2) == 0:
            trả về false
        i = i + 6
    trả về true
```

#### Code C++

```cpp
#include <bits/stdc++.h>
using namespace std;

bool isPrime(long long n) {
    if (n < 2) return false;
    if (n == 2 || n == 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    for (long long i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;

    if (isPrime(n)) {
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }

    return 0;
}
```

#### Điều cần theo dõi khi debug

| Giá trị biên | Kết quả đúng | Lỗi thường gặp |
|---|---|---|
| $N = 0, 1$ | `false` | Quên chặn điều kiện $N < 2$. |
| $N = 2, 3$ | `true` | Bị loại nhầm bởi các điều kiện chia hết. |
| $N = 10^{12}$ | Chạy dưới $0.001$s | Dùng `int i` gây tràn số ở `i * i`. |

#### Tự kiểm tra

1. Số nguyên tố chẵn duy nhất là số nào?
2. Vì sao một hợp số $N$ luôn có ước nguyên tố $\le \sqrt{N}$?

#### Luyện tập ngắn

- **LT 3.4A:** Tìm số nguyên tố nhỏ nhất lớn hơn số nguyên dương $N$ ($N \le 10^9$).
- **LT 3.4B:** Đếm số lượng số nguyên tố trong đoạn $[L, R]$ với $R - L \le 10^5, R \le 10^{12}$.

#### Tóm tắt bài

Kiểm tra số nguyên tố chỉ cần duyệt đến $\sqrt{N}$. Kết hợp bước nhảy $6k \pm 1$ giúp hàm `isPrime()` đạt tốc độ tối đa cho mọi $N \le 10^{12}$.

---

### Bài 3.5 — Phân tích thừa số nguyên tố

#### Mục tiêu bài

Sau Bài 3.5, em biết cách phân rã một số nguyên dương thành tích các thừa số nguyên tố bằng thuật toán chia dần $\mathcal{O}(\sqrt{N})$ và ứng dụng để đếm số lượng ước.

#### Khởi động

Số $60$ có thể viết thành $2 \times 2 \times 3 \times 5 = 2^2 \times 3^1 \times 5^1$. Mọi số nguyên $> 1$ đều có duy nhất một cách phân tích như vậy.

#### Thuật toán chia dần

1. Cho $p$ chạy từ $2$ đến khi $p \times p > N$.
2. Nếu $N \% p == 0$, ta đếm số mũ của $p$ bằng cách chia $N$ liên tục cho $p$ trong khi $N \% p == 0$.
3. Sau vòng lặp, nếu giá trị $N$ còn lại $> 1$ thì giá trị đó chính là thừa số nguyên tố cuối cùng (với số mũ 1).

#### Mô phỏng từng bước phân tích $N = 60$

| Bước | $N$ hiện tại | $p$ đang xét | Thao tác chia rút gọn | Thừa số thu được | $N$ sau khi chia |
|:---:|:---:|:---:|---|:---:|:---:|
| 1 | $60$ | $p = 2$ | $60 \% 2 == 0 \implies 60 / 2 = 30 \implies 30 / 2 = 15$ | $2^2$ | $15$ |
| 2 | $15$ | $p = 3$ | $15 \% 3 == 0 \implies 15 / 3 = 5$ | $3^1$ | $5$ |
| 3 | $5$ | $p = 4$ | $4 \times 4 = 16 > 5 \implies$ dừng vòng lặp | - | $5$ |
| 4 | $5 > 1$ | - | Thừa số nguyên tố cuối cùng là $5^1$ | $5^1$ | $1$ |

👉 **Kết quả:** $60 = 2^2 \times 3^1 \times 5^1$.

#### Pseudocode

```text
for p từ 2 đến khi p * p > n:
    nếu n % p == 0:
        exp = 0
        trong khi n % p == 0:
            exp tăng 1
            n = n / p
        in p và exp
nếu n > 1:
    in n và exp = 1
```

#### Code C++

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;

    bool first = true;
    for (long long p = 2; p * p <= n; p++) {
        if (n % p == 0) {
            int exp = 0;
            while (n % p == 0) {
                exp++;
                n /= p;
            }
            if (!first) cout << " * ";
            cout << p << "^" << exp;
            first = false;
        }
    }

    if (n > 1) {
        if (!first) cout << " * ";
        cout << n << "^1";
    }
    cout << '\n';

    return 0;
}
```

#### Điều cần theo dõi khi debug

| Tình huống | Hiện tượng | Cách xử lý đúng |
|---|---|---|
| Số nguyên tố $N = 13$ | Vòng lặp dừng ngay ở $p = 2$ | Khối lệnh `if (n > 1)` sẽ in ra $13^1$. |
| Hợp số $p = 4, 6$ | Có bị in nhầm làm thừa số không? | Không, vì các thừa số nguyên tố nhỏ hơn ($2, 3$) đã chia rút gọn hết $N$ từ trước. |

#### Tự kiểm tra

1. Vì sao không cần kiểm tra $p$ có phải số nguyên tố trước khi chia?
2. Nếu $N = 2^3 \times 3^2 \times 5^1$, số lượng ước của $N$ tính bằng công thức nào? (Đáp án: $(3+1)(2+1)(1+1) = 24$ ước).

#### Luyện tập ngắn

- **LT 3.5A:** Nhập vào số nguyên dương $N \le 10^{12}$. Tìm ước nguyên tố lớn nhất của $N$.
- **LT 3.5B:** Đếm số lượng ước nguyên dương của $N$ ($N \le 10^{12}$) dựa vào phân tích thừa số nguyên tố.

#### Tóm tắt bài

Thuật toán chia dần $\mathcal{O}(\sqrt{N})$ tự động lọc ra các thừa số nguyên tố. Đây là chìa khóa tính nhanh số lượng ước và tổng ước của số cực lớn.

---

### Bài 3.6 — Sàng số nguyên tố Eratosthenes

#### Mục tiêu bài

Sau Bài 3.6, em hiểu nguyên lý sàng lọc bội số, cài đặt thành thạo Sàng Eratosthenes $\mathcal{O}(N \log \log N)$ và biết cách trả lời tức thì $\mathcal{O}(1)$ các truy vấn kiểm tra nguyên tố cho hàng triệu số.

#### Khởi động

Nếu cần kiểm tra số nguyên tố cho $Q = 10^6$ truy vấn, mỗi truy vấn $x \le 10^7$:
- Dùng `isPrime(x)` tốn $10^6 \times \sqrt{10^7} \approx 3 \times 10^9$ phép tính $\implies$ Mất 30 giây (TLE).
- **Giải pháp:** Tiền xử lý một lần duy nhất bằng **Sàng Eratosthenes** trong $0.1$ giây, sau đó mỗi truy vấn chỉ mất $\mathcal{O}(1)$ để tra cứu!

#### Cơ chế Sàng lọc

1. Ban đầu giả sử tất cả các số từ $2$ đến $N$ đều là số nguyên tố (`is_prime[i] = true`).
2. Xét từ số nguyên tố đầu tiên $p = 2$: Giữ lại số 2, gạch bỏ các bội số của 2 ($4, 6, 8, \dots$).
3. Tìm số tiếp theo chưa bị gạch là $p = 3$: Giữ lại số 3, gạch bỏ các bội của 3 ($9, 12, 15, \dots$, bắt đầu từ $p \times p = 9$).
4. Tiếp tục đến $p \le \sqrt{N}$. Tất cả các số chưa bị gạch còn lại chính là **toàn bộ số nguyên tố trong đoạn $[2, N]$**.

#### Mô phỏng sàng từ 2 đến 20

```text
Ban đầu:     2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
Gạch bội 2:  2  3  .  5  .  7  .  9  . 11  . 13  . 15  . 17  . 19  .
Gạch bội 3:  2  3  .  5  .  7  .  .  . 11  . 13  .  .  . 17  . 19  .
Còn lại:     2, 3, 5, 7, 11, 13, 17, 19
```

#### Pseudocode

```text
is_prime[0] = is_prime[1] = false
mọi vị trí từ 2 đến N gán bằng true

for p từ 2 đến khi p * p > N:
    nếu is_prime[p] == true:
        for i từ p * p đến N, mỗi bước tăng p:
            is_prime[i] = false
```

#### Code C++

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAX_N = 10000000;
vector<bool> is_prime(MAX_N + 1, true);

void sieve() {
    is_prime[0] = is_prime[1] = false;
    for (int p = 2; p * p <= MAX_N; p++) {
        if (is_prime[p]) {
            for (int i = p * p; i <= MAX_N; i += p) {
                is_prime[i] = false;
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    sieve();

    int q;
    if (!(cin >> q)) return 0;

    while (q--) {
        int x;
        cin >> x;
        if (is_prime[x]) {
            cout << "YES\n";
        } else {
            cout << "NO\n";
        }
    }

    return 0;
}
```

#### Điều cần theo dõi khi debug

| Chi tiết | Lý do |
|---|---|
| `i = p * p` | Các bội nhỏ hơn ($2p, 3p$) đã bị các số $2, 3$ gạch từ trước, bắt đầu từ $p \times p$ giúp tiết kiệm thời gian. |
| `vector<bool>` | Mỗi phần tử chỉ tốn 1 bit, $10^7$ phần tử chỉ tốn $\approx 1.2\text{ MB}$ RAM. |

#### Tự kiểm tra

1. Vì sao vòng lặp ngoài chỉ cần chạy đến $p \times p \le N$?
2. Sàng Eratosthenes cho $N = 10^7$ mất bao lâu để hoàn thành? (Đáp án: $\approx 0.08$ giây).

#### Luyện tập ngắn

- **LT 3.6A:** In ra toàn bộ số nguyên tố trong đoạn $[1, N]$ với $N \le 10^6$.
- **LT 3.6B:** Đếm số lượng số nguyên tố trong đoạn $[L, R]$ với $1 \le L \le R \le 10^6$.

#### Tóm tắt bài

Sàng Eratosthenes là thuật toán tiền xử lý số nguyên tố kinh điển $\mathcal{O}(N \log \log N)$. Sau khi sàng, việc kiểm tra nguyên tố chỉ tốn $\mathcal{O}(1)$.

---

### Bài 3.7 — Ôn tập, kiểm tra và bài chuyển giao

#### Mục tiêu bài

Bài này giúp em củng cố toàn bộ kỹ năng số học từ cơ bản đến nâng cao. Mỗi bài tập tập trung vào việc áp dụng đúng công thức và xử lý số lớn an toàn.

#### Tầng A — Củng cố nền tảng

##### Bài 3.7.1 — Tính tổng các ước
Đọc số nguyên dương $N$ ($1 \le N \le 10^9$). Tính tổng tất cả các ước nguyên dương của $N$.
- **Input:** Một số nguyên $N$.
- **Output:** Tổng các ước nguyên dương của $N$.
- **Ví dụ:** `12` $\implies$ Output: `28` (vì $1 + 2 + 3 + 4 + 6 + 12 = 28$).

##### Bài 3.7.2 — Ước chung lớn nhất của hai số lớn
Cho hai số nguyên dương $A$ và $B$ ($1 \le A, B \le 10^{18}$). Tìm $\gcd(A, B)$.
- **Input:** Hai số nguyên $A$ và $B$.
- **Output:** Giá trị $\gcd(A, B)$.
- **Ví dụ:** `1000000000000 250000000000` $\implies$ Output: `250000000000`.

##### Bài 3.7.3 — Kiểm tra nhiều số nguyên tố
Cho $T$ số nguyên dương $N$ ($T \le 100, N \le 10^{12}$). Với mỗi số, kiểm tra xem có phải số nguyên tố không.
- **Input:** Dòng đầu ghi $T$. $T$ dòng sau, mỗi dòng ghi một số $N$.
- **Output:** In `YES` nếu là số nguyên tố, ngược lại in `NO`.
- **Ví dụ:** `17` cho `YES`; `1` cho `NO`.

##### Bài 3.7.4 — Tổng chữ số nguyên tố
Cho số nguyên dương $N$ ($1 \le N \le 10^{18}$). Kiểm tra xem tổng các chữ số của $N$ có phải là số nguyên tố hay không.
- **Input:** Số nguyên $N$.
- **Output:** In `YES` hoặc `NO`.
- **Ví dụ:** `124` $\implies$ Output: `YES` (vì $1 + 2 + 4 = 7$).

---

#### Tầng B — Vận dụng mẫu

##### Bài 3.7.5 — Số bán nguyên tố (Semi-Prime)
Số bán nguyên tố là số bằng tích của đúng hai số nguyên tố (ví dụ $4 = 2 \times 2, 6 = 2 \times 3$). Kiểm tra xem $N$ ($1 \le N \le 10^9$) có phải là số bán nguyên tố không.
- **Input:** Số nguyên $N$.
- **Output:** In `YES` hoặc `NO`.
- **Ví dụ:** `6` cho `YES`; `8` cho `NO` (vì $8 = 2^3$, có 3 thừa số).

##### Bài 3.7.6 — Rút gọn dãy phân số
Cho $N$ cặp số nguyên dương $A_i, B_i$ ($N \le 10^5, A_i, B_i \le 10^9$). Rút gọn từng phân số $\frac{A_i}{B_i}$ về dạng tối giản $\frac{P_i}{Q_i}$.
- **Input:** Dòng đầu ghi $N$. $N$ dòng sau, mỗi dòng ghi $A_i, B_i$.
- **Output:** Ghi $N$ dòng, mỗi dòng chứa hai số $P_i, Q_i$.

##### Bài 3.7.7 — Đếm cặp nguyên tố cùng nhau
Cho dãy $N$ số nguyên ($N \le 2000, A_i \le 10^9$). Đếm số cặp $(i, j)$ với $1 \le i < j \le N$ thỏa mãn $\gcd(A_i, A_j) = 1$.
- **Input:** Dòng 1 ghi $N$. Dòng 2 ghi $N$ số $A_i$.
- **Output:** Số lượng cặp nguyên tố cùng nhau.

##### Bài 3.7.8 — Tìm số nhỏ nhất có đúng K ước
Cho số nguyên $K$ ($1 \le K \le 30$). Tìm số nguyên dương $N$ nhỏ nhất có đúng $K$ ước số nguyên dương.
- **Input:** Số nguyên $K$.
- **Output:** Số $N$ nhỏ nhất tìm được.
- **Ví dụ:** `3` $\implies$ Output: `4` (ước là 1, 2, 4).

---

#### Tầng C — Chuyển giao

##### Bài 3.7.9 — Bội chung nhỏ nhất của dãy số
Cho $N$ số nguyên $A_1, A_2, \dots, A_N$ ($N \le 100, A_i \le 1000$). Tính $\text{lcm}(A_1, \dots, A_N) \pmod{10^9+7}$.
- **Gợi ý:** Phân tích từng số ra thừa số nguyên tố, lấy số mũ lớn nhất của mỗi thừa số trên toàn dãy.

##### Bài 3.7.10 — Đếm số chữ số 0 tận cùng của N!
Cho số nguyên dương $N$ ($1 \le N \le 10^{18}$). Đếm số chữ số 0 liên tiếp ở tận cùng của $N!$.
- **Gợi ý:** Áp dụng định lý Legendre tính số mũ của thừa số 5 trong $N!$: $\lfloor N/5 \rfloor + \lfloor N/25 \rfloor + \dots$
- **Ví dụ:** `10` $\implies$ Output: `2`.

##### Bài 3.7.11 — Khôi phục hai số từ GCD và LCM
Cho $G = \gcd(A, B)$ và $L = \text{lcm}(A, B)$ ($G, L \le 10^{12}$). Tìm hai số nguyên dương $A \le B$ sao cho $A + B$ nhỏ nhất. Nếu không tồn tại, in `-1`.
- **Ví dụ:** `2 60` $\implies$ Output: `10 12`.

##### Bài 3.7.12 — Sàng nguyên tố hàng loạt
Cài đặt Sàng Eratosthenes cho $10^7$ số và trả lời $Q$ truy vấn kiểm tra số nguyên tố ($Q \le 10^6$).
- **Input:** Dòng đầu ghi $Q$. $Q$ dòng sau, mỗi dòng ghi một số $x \le 10^7$.
- **Output:** Với mỗi truy vấn, in `1` nếu là số nguyên tố, ngược lại in `0`.

---

#### Phiếu tự đánh giá

| Năng lực | Chưa chắc | Làm khi có gợi ý | Tự làm được |
|---|:---:|:---:|:---:|
| Tìm ước trong $\mathcal{O}(\sqrt{N})$ |  |  |  |
| Cài đặt thuật toán Euclid tìm GCD |  |  |  |
| Tính LCM an toàn (chia trước nhân) |  |  |  |
| Kiểm tra số nguyên tố tối ưu $6k \pm 1$ |  |  |  |
| Phân tích thừa số nguyên tố bằng chia dần |  |  |  |
| Cài đặt Sàng Eratosthenes $\mathcal{O}(N \log \log N)$ |  |  |  |
| Xử lý số lớn $10^{18}$ với `long long` |  |  |  |

#### Tiêu chí hoàn thành chương

Em có thể xem mình đã nắm chắc chương khi:
1. Giải thích được vì sao chỉ cần duyệt đến $\sqrt{N}$ để tìm ước và kiểm tra nguyên tố.
2. Viết được hàm `gcd` và `lcm` an toàn không quá 5 dòng code.
3. Cài đặt được Sàng Eratosthenes từ trí nhớ trong 2 phút.
4. Không mắc bẫy tràn số khi làm việc với số nguyên $10^9 \to 10^{18}$.

---

### Tổng kết chương

> **Số học là nền tảng của các thuật toán tối ưu. Nắm vững tính chất đối xứng $\sqrt{N}$, thuật toán Euclid và Sàng Eratosthenes giúp em biến những bài toán duyệt hàng triệu số phức tạp thành những câu lệnh chớp nhoáng.**

| Cần nhớ | Nội dung |
|---|---|
| Tập ước số | Duyệt $d \times d \le N$, mỗi lần lấy cặp $(d, N/d)$ với $\mathcal{O}(\sqrt{N})$ |
| Thuật toán Euclid | $\gcd(a, b) = \gcd(b, a \% b)$ với $\mathcal{O}(\log(\min(A, B)))$ |
| Quy tắc an toàn LCM | $\text{lcm}(a, b) = (a / \gcd(a, b)) \times b$ (chia trước khi nhân) |
| Số nguyên tố | Số $> 1$ chỉ có 2 ước; kiểm tra chia hết từ $2$ đến $\sqrt{N}$ bước nhảy $6k \pm 1$ |
| Thừa số nguyên tố | Chia dần cho $p$ từ $2$ đến $\sqrt{N}$; nếu sau cùng $N > 1$ thì $N$ là thừa số cuối |
| Sàng Eratosthenes | Gạch bội số bắt đầu từ $p \times p$ với $\mathcal{O}(N \log \log N)$ |

#### Những lỗi thường gặp

| Lỗi | Cách tự kiểm tra |
|---|---|
| Tràn số khi tính tích trong LCM | Luôn lấy `(a / gcd(a, b)) * b` |
| Quên trường hợp $N = 0, 1$ khi kiểm tra nguyên tố | Luôn chặn `if (n < 2) return false;` đầu tiên |
| Bỏ sót ước nguyên tố cuối cùng sau vòng lặp $\sqrt{N}$ | Luôn kiểm tra `if (n > 1)` sau vòng lặp |
| Dùng `int` cho biến lặp `d * d <= n` | Khi $N = 10^{12}$, biến lặp $d$ phải là `long long` |
| Tràn mảng trong Sàng Eratosthenes | Khai báo kích thước mảng là `MAX_N + 1` |

---

### Code tham chiếu

```cpp
#include <bits/stdc++.h>
using namespace std;

// 1. Uoc chung lon nhat (Euclid)
long long gcd(long long a, long long b) {
    while (b != 0) {
        long long r = a % b;
        a = b;
        b = r;
    }
    return a;
}

// 2. Boi chung nho nhat an toan (Chia truoc khi nhan)
long long lcm(long long a, long long b) {
    if (a == 0 || b == 0) return 0;
    return (a / gcd(a, b)) * b;
}

// 3. Kiem tra so nguyen to toi uu O(sqrt(N)) buoc nhay 6k +- 1
bool isPrime(long long n) {
    if (n < 2) return false;
    if (n == 2 || n == 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    for (long long i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) {
            return false;
        }
    }
    return true;
}

// 4. Sang so nguyen to Eratosthenes O(N log log N)
const int MAX_VAL = 1000000;
vector<bool> is_prime_sieve(MAX_VAL + 1, true);

void sieve() {
    is_prime_sieve[0] = is_prime_sieve[1] = false;
    for (int p = 2; p * p <= MAX_VAL; p++) {
        if (is_prime_sieve[p]) {
            for (int i = p * p; i <= MAX_VAL; i += p) {
                is_prime_sieve[i] = false;
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    sieve();

    long long a, b;
    if (!(cin >> a >> b)) return 0;

    cout << "GCD: " << gcd(a, b) << "\n";
    cout << "LCM: " << lcm(a, b) << "\n";
    cout << "a is Prime: " << (isPrime(a) ? "YES" : "NO") << "\n";
    cout << "b is Prime: " << (isPrime(b) ? "YES" : "NO") << "\n";

    return 0;
}
```

---

## Chương 4 — Đếm phân phối

### Bản đồ chương

| Trường | Nội dung |
|---|---|
| Mục tiêu | Nắm vững kỹ thuật dùng giá trị làm chỉ số mảng để thống kê, đếm cặp và phân tích dữ liệu trong $\mathcal{O}(N)$ |
| Kiến thức cần có | Mảng 1 chiều (`vector<int>`), chỉ số mảng, vòng lặp, chuỗi ký tự (`string`), kiểu `long long` |
| Phạm vi | Mảng tần suất trực tiếp, tìm Mode/Min-Max tần suất, mảng chữ cái 26 ký tự, kỹ thuật đếm cặp trong $\mathcal{O}(N)$ và nguyên lý Dirichlet |
| Số bài | 5 bài học lý thuyết & thực hành + 1 bài tổng kết và bài tập phân tầng |

### Learning outcomes

Sau chương này, em có thể:
1. Xây dựng và cập nhật bảng đếm tần suất các giá trị trong thời gian $\mathcal{O}(N)$ bằng kỹ thuật chuyển giá trị thành chỉ số mảng.
2. Tìm phần tử xuất hiện nhiều nhất, ít nhất hoặc kiểm tra phần tử đa số tuyệt đối trong một dãy số.
3. Ánh xạ các ký tự chữ cái thường `'a'..'z'` thành chỉ số `0..25` để kiểm tra chuỗi Anagram trong thời gian tuyến tính.
4. Đếm số lượng cặp phần tử thỏa mãn điều kiện bằng nhau hoặc có tổng bằng $S$ trong $\mathcal{O}(N)$ mà không dùng hai vòng lặp lồng nhau.
5. Vận dụng nguyên lý Dirichlet để tìm kiếm đoạn con liên tiếp có tổng chia hết cho $N$.
6. Tránh bẫy tràn số khi đếm số lượng cặp phần tử vượt ngưỡng 32-bit ($2 \times 10^9$).

### Câu hỏi trung tâm của chương

> **Làm thế nào để đếm tần suất, tìm phần tử xuất hiện nhiều nhất và đếm hàng tỷ cặp phần tử chỉ qua MỘT lần duyệt mảng duy nhất mà không bị quá thời gian?**

---

### Bài 4.1 — Mảng tần suất trực tiếp: biến giá trị thành chỉ số

#### Mục tiêu bài

Sau Bài 4.1, em hiểu bản chất của mảng tần suất, biết cách dùng chính giá trị của phần tử làm chỉ số mảng để đếm số lần xuất hiện của các phần tử trong $\mathcal{O}(N)$.

#### Khởi động

Khi kiểm phiếu bầu cử lớp trưởng cho 3 ứng viên mang số báo danh 1, 2, 3:
- Thay vì mỗi lần đọc một phiếu lại phải lật lại toàn bộ danh sách phiếu trước đó để đếm, thư ký vẽ 3 ô số 1, 2, 3 lên bảng.
- Mỗi khi đọc một phiếu ghi số nào, thư ký chỉ cần gạch thêm một vạch vào đúng ô số đó.
- Sau khi đọc xong $N$ phiếu, số vạch trong từng ô chính là số phiếu của từng ứng viên!
- Chiếc bảng chia ô đó trong lập trình chính là **Mảng tần suất (Frequency Array)**.

#### Ý tưởng mảng tần suất

- **Cách làm ngây thơ ($\mathcal{O}(N^2)$):** Với mỗi phần tử $A[i]$, duyệt lại toàn bộ mảng từ đầu đến cuối để đếm. Với $N = 10^5$, hai vòng lặp lồng nhau mất $10^{10}$ phép tính $\implies$ Quá thời gian (TLE).
- **Mảng tần suất ($\mathcal{O}(N)$):**
  1. Khởi tạo một mảng đếm `cnt` kích thước đủ lớn, ban đầu tất cả bằng `0`.
  2. Khi đọc phần tử giá trị `x`, ta tăng biến đếm tại chỉ số `x` lên 1:
     $$\text{cnt}[x] = \text{cnt}[x] + 1 \quad (\text{hoặc } \text{cnt}[x]\text{++})$$
  3. Sau khi đọc xong, `cnt[v]` lưu trữ chính xác số lần xuất hiện của giá trị `v`.

#### Mô phỏng ghi nhận tần suất cho dãy $A = [3, 1, 3, 2, 1, 3]$

| Bước | Đọc giá trị $x$ | Thao tác | Trạng thái mảng `cnt` (`cnt[0..3]`) |
|:---:|:---:|:---:|:---:|
| Khởi tạo | - | `cnt = {0, 0, 0, 0}` | `[0: 0, 1: 0, 2: 0, 3: 0]` |
| 1 | $3$ | `cnt[3]++` | `[0: 0, 1: 0, 2: 0, 3: 1]` |
| 2 | $1$ | `cnt[1]++` | `[0: 0, 1: 1, 2: 0, 3: 1]` |
| 3 | $3$ | `cnt[3]++` | `[0: 0, 1: 1, 2: 0, 3: 2]` |
| 4 | $2$ | `cnt[2]++` | `[0: 0, 1: 1, 2: 1, 3: 2]` |
| 5 | $1$ | `cnt[1]++` | `[0: 0, 1: 2, 2: 1, 3: 2]` |
| 6 | $3$ | `cnt[3]++` | `[0: 0, 1: 2, 2: 1, 3: 3]` |

👉 **Kết quả:** Số 1 xuất hiện 2 lần, số 2 xuất hiện 1 lần, số 3 xuất hiện 3 lần.

#### Pseudocode

```text
cnt = mảng kích thước MAX_VAL + 1, khởi tạo bằng 0
for x trong dãy A:
    cnt[x] = cnt[x] + 1

distinctCount = 0
for v từ 0 đến MAX_VAL:
    nếu cnt[v] > 0:
        distinctCount tăng 1

in distinctCount
for v từ 0 đến MAX_VAL:
    nếu cnt[v] > 0:
        in v và cnt[v]
```

#### Code C++

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAX_VAL = 100000;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> cnt(MAX_VAL + 1, 0);
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        cnt[x]++;
    }

    int distinctCount = 0;
    for (int v = 0; v <= MAX_VAL; v++) {
        if (cnt[v] > 0) {
            distinctCount++;
        }
    }

    cout << distinctCount << '\n';
    for (int v = 0; v <= MAX_VAL; v++) {
        if (cnt[v] > 0) {
            cout << v << " xuat hien " << cnt[v] << " lan\n";
        }
    }

    return 0;
}
```

#### Điều cần theo dõi khi debug

| Chi tiết | Lưu ý |
|---|---|
| Kích thước mảng | Luôn khai báo `MAX_VAL + 1` để truy cập được chỉ số `MAX_VAL`. |
| Giá trị $A_i$ âm | Nếu có số âm, cần tịnh tiến chỉ số: `cnt[x + OFFSET]++`. |

#### Tự kiểm tra

1. Mảng tần suất trực tiếp áp dụng tốt nhất khi giá trị các phần tử nằm trong khoảng nào?
2. Vì sao mảng tần suất giúp giảm độ phức tạp từ $\mathcal{O}(N^2)$ xuống $\mathcal{O}(N)$?

#### Luyện tập ngắn

- **LT 4.1A:** Nhập dãy $N$ số nguyên ($N \le 10^5, 0 \le A_i \le 10^5$). In ra các giá trị chỉ xuất hiện đúng 1 lần theo thứ tự tăng dần.
- **LT 4.1B:** Cho dãy $N$ số nguyên trong đoạn $[-1000, 1000]$. Dùng mảng tần suất tịnh tiến để đếm số lần xuất hiện của từng số.

#### Tóm tắt bài

Mảng tần suất biến **giá trị thành chỉ số** giúp tra cứu và cập nhật số lần xuất hiện trong $\mathcal{O}(1)$.

---

### Bài 4.2 — Thống kê tần suất: Tìm Mode, Min-Max và Phần tử đa số

#### Mục tiêu bài

Sau Bài 4.2, em biết cách tìm phần tử xuất hiện nhiều nhất (Mode) và xác định phần tử đa số tuyệt đối (xuất hiện $> N/2$ lần) bằng một lần duyệt mảng tần suất.

#### Khởi động

Trong cuộc bỏ phiếu bầu lớp trưởng với $N = 7$ phiếu, ứng viên chỉ trúng cử nếu nhận được quá bán (nhiều hơn $7/2 = 3.5 \implies$ ít nhất 4 phiếu). Giá trị xuất hiện $> N/2$ lần này được gọi là **Phần tử đa số (Majority Element)**.

#### Ý tưởng thống kê

1. **Tìm phần tử xuất hiện nhiều nhất (Mode):**  
   Duyệt `v` từ `0` đến `MAX_VAL`. Duy trì biến `maxFreq` và `bestVal`. Nếu `cnt[v] > maxFreq`, cập nhật `maxFreq = cnt[v]` và `bestVal = v`.
2. **Tìm phần tử đa số tuyệt đối:**  
   Kiểm tra xem có giá trị `v` nào thỏa mãn `cnt[v] > n / 2` không. Trong mảng $N$ phần tử, **tối đa chỉ có thể có duy nhất một phần tử đa số tuyệt đối**.

#### Mô phỏng tìm phần tử đa số cho $A = [3, 3, 4, 2, 3, 3, 5]$ ($N = 7$, ngưỡng $> 3$)

| Giá trị $v$ | Tần suất `cnt[v]` | Điều kiện `cnt[v] > 3` | Kết luận |
|:---:|:---:|:---:|---|
| 2 | 1 | Sai | Không phải đa số |
| 3 | 4 | Đúng ($4 > 3$) | **Là phần tử đa số tuyệt đối!** |
| 4 | 1 | Sai | Không phải đa số |
| 5 | 1 | Sai | Không phải đa số |

#### Pseudocode

```text
majority = -1
for v từ 0 đến MAX_VAL:
    nếu cnt[v] > n / 2:
        majority = v
        dừng vòng lặp
in majority
```

#### Code C++

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAX_VAL = 100000;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> cnt(MAX_VAL + 1, 0);
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        cnt[x]++;
    }

    int majority = -1;
    for (int v = 0; v <= MAX_VAL; v++) {
        if (cnt[v] > n / 2) {
            majority = v;
            break;
        }
    }

    cout << majority << '\n';

    return 0;
}
```

#### Điều cần theo dõi khi debug

| Tình huống | Kiểm tra |
|---|---|
| Không có ai đa số | Biến `majority` giữ nguyên giá trị `-1`. |
| Nhiều số cùng tần suất lớn nhất | Dùng `cnt[v] > maxFreq` khi duyệt từ nhỏ đến lớn sẽ tự động giữ lại giá trị nhỏ nhất. |

#### Tự kiểm tra

1. Một mảng có độ dài $N = 10$ có thể có 2 phần tử cùng xuất hiện 6 lần không? Vì sao?
2. Vì sao phần tử đa số tuyệt đối nếu tồn tại thì luôn là duy nhất?

#### Luyện tập ngắn

- **LT 4.2A:** Tìm giá trị xuất hiện nhiều lần nhất trong mảng $N$ số. Nếu có nhiều giá trị, in giá trị nhỏ nhất.
- **LT 4.2B:** Tìm giá trị xuất hiện ít nhất một lần nhưng có số lần xuất hiện nhỏ nhất trong mảng.

#### Tóm tắt bài

Duyệt mảng tần suất $\mathcal{O}(\text{MAX\_VAL})$ cho phép dễ dàng tìm Mode và xác định phần tử đa số tuyệt đối trong chớp mắt.

---

### Bài 4.3 — Mảng tần suất trên bảng chữ cái và Kiểm tra chuỗi Anagram

#### Mục tiêu bài

Sau Bài 4.3, em biết cách ánh xạ các chữ cái `'a'..'z'` thành chỉ số `0..25` để đếm tần suất ký tự và kiểm tra hai chuỗi Anagram trong thời gian $\mathcal{O}(N)$.

#### Khởi động

Hai từ tiếng Anh **"listen"** và **"silent"** tuy viết khác nhau nhưng gồm đúng cùng một bộ chữ cái: 1 chữ 'e', 1 chữ 'i', 1 chữ 'l', 1 chữ 'n', 1 chữ 's', 1 chữ 't'. Hai từ như vậy gọi là **Anagram** (từ đảo mã).

#### Ánh xạ chữ cái thành chỉ số mảng

- Bảng chữ cái tiếng Anh in thường có 26 ký tự từ `'a'` đến `'z'`.
- Công thức ánh xạ: Trừ đi ký tự gốc `'a'`:
  $$\text{Index} = c - \text{'a'}$$
  - `'a' - 'a' = 0`
  - `'b' - 'a' = 1`
  - `'z' - 'a' = 25`
- Chỉ cần mảng `vector<int> cnt(26, 0)` để đếm tần suất mọi ký tự.

> **Hai chuỗi $S$ và $T$ là Anagram của nhau khi và chỉ khi chúng có cùng độ dài và mảng tần suất 26 chữ cái của chúng hoàn toàn giống nhau.**

#### Pseudocode

```text
nếu độ dài S != độ dài T: trả về false
cntS = mảng 26 số 0
cntT = mảng 26 số 0

for c trong S: cntS[c - 'a']++
for c trong T: cntT[c - 'a']++

for i từ 0 đến 25:
    nếu cntS[i] != cntT[i]: trả về false
trả về true
```

#### Code C++

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s, t;
    if (!(cin >> s >> t)) return 0;

    if (s.length() != t.length()) {
        cout << "NO\n";
        return 0;
    }

    vector<int> cntS(26, 0);
    vector<int> cntT(26, 0);

    for (char c : s) cntS[c - 'a']++;
    for (char c : t) cntT[c - 'a']++;

    bool isAnagram = true;
    for (int i = 0; i < 26; i++) {
        if (cntS[i] != cntT[i]) {
            isAnagram = false;
            break;
        }
    }

    if (isAnagram) cout << "YES\n";
    else cout << "NO\n";

    return 0;
}
```

#### Điều cần theo dõi khi debug

| Chi tiết | Kiểm tra |
|---|---|
| `c - 'a'` | Đảm bảo ký tự `c` là chữ cái in thường (`'a' <= c <= 'z'`). |
| So sánh độ dài | Luôn kiểm tra `s.length() != t.length()` đầu tiên để thoát sớm. |

#### Tự kiểm tra

1. Phép trừ `c - 'a'` cho kết quả là kiểu dữ liệu gì?
2. Làm thế nào để kiểm tra một xâu có thể sắp xếp lại thành xâu đối xứng (Palindrome) không? (Gợi ý: Có tối đa 1 ký tự có số lần xuất hiện lẻ).

#### Luyện tập ngắn

- **LT 4.3A:** Tìm chữ cái xuất hiện nhiều lần nhất trong xâu $S$ ($|S| \le 10^5$).
- **LT 4.3B:** Kiểm tra xâu $S$ có thể đổi chỗ các ký tự để tạo thành xâu đối xứng không.

#### Tóm tắt bài

Ánh xạ `c - 'a'` biến bảng chữ cái thành mảng 26 phần tử, là công cụ tối ưu $\mathcal{O}(N)$ cho các bài toán xử lý xâu ký tự.

---

### Bài 4.4 — Kỹ thuật đếm cặp $\mathcal{O}(N)$ bằng Bảng tần suất

#### Mục tiêu bài

Sau Bài 4.4, em làm chủ kỹ thuật đếm số lượng cặp $(i, j)$ ($i < j$) có tổng bằng $S$ hoặc bằng nhau trong $\mathcal{O}(N)$ và biết cách phòng tránh bẫy tràn số.

#### Khởi động

Một bãi xe cần ghép từng cặp 2 xe sao cho tổng trọng tải đúng bằng $S = 6$ tấn.
- Thay vì với mỗi xe lại đi tìm trong toàn bộ bãi ($\mathcal{O}(N^2)$), bác tài xế vừa kéo xe tải trọng $x$ vào, vừa nhìn sổ xem trước đó đã có bao nhiêu xe tải trọng bù $6 - x$.
- Có bao nhiêu xe bù có sẵn $\implies$ tạo được bấy nhiêu cặp mới ngay lập tức!

#### Kỹ thuật "Vừa duyệt vừa đếm"

- Khi xét phần tử đứng sau tại vị trí $j$ có giá trị $x = A[j]$, phần tử đứng trước $A[i]$ ($i < j$) muốn ghép đôi để có tổng bằng $S$ phải có giá trị:
  $$\text{comp} = S - x$$
- Số phần tử đứng trước thỏa mãn chính là số lần `comp` đã xuất hiện trong mảng `cnt` tính đến trước bước $j$.
- **Thứ tự thực hiện:**
  1. `totalPairs += cnt[comp]` (cộng số cặp tạo được với các phần tử đứng trước).
  2. `cnt[x]++` (ghi nhận phần tử hiện tại vào mảng đếm).

> **Bẫy tràn số:** Với $N = 10^5$, số lượng cặp có thể đạt tới $\frac{N(N-1)}{2} \approx 5 \times 10^9 > 2 \times 10^9 \implies$ Bắt buộc dùng kiểu `long long` cho biến đếm kết quả.

#### Mô phỏng đếm cặp tổng $S = 6$ cho $A = [1, 5, 3, 3, 5]$

| Bước $j$ | Giá trị $x = A[j]$ | Giá trị bù $\text{comp} = 6 - x$ | `cnt[comp]` hiện có | Cộng dồn `totalPairs` | Cập nhật `cnt` |
|:---:|:---:|:---:|:---:|:---:|---|
| 0 | $1$ | $5$ | $0$ | $0$ | `cnt[1] = 1` |
| 1 | $5$ | $1$ | $1$ | $0 + 1 = 1$ | `cnt[5] = 1` |
| 2 | $3$ | $3$ | $0$ | $1$ | `cnt[3] = 1` |
| 3 | $3$ | $3$ | $1$ | $1 + 1 = 2$ | `cnt[3] = 2` |
| 4 | $5$ | $1$ | $1$ | $2 + 1 = 3$ | `cnt[5] = 2` |

👉 **Tổng số cặp: 3 cặp** (chính xác 100%).

#### Pseudocode

```text
totalPairs = 0 (kiểu long long)
cnt = mảng MAX_VAL + 1 số 0

for x trong dãy A:
    comp = S - x
    nếu comp nằm trong khoảng [0, MAX_VAL]:
        totalPairs = totalPairs + cnt[comp]
    cnt[x] = cnt[x] + 1

in totalPairs
```

#### Code C++

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAX_VAL = 200000;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, s;
    if (!(cin >> n >> s)) return 0;

    vector<int> cnt(MAX_VAL + 1, 0);
    long long totalPairs = 0;

    for (int j = 0; j < n; j++) {
        int x;
        cin >> x;

        int comp = s - x;
        if (comp >= 0 && comp <= MAX_VAL) {
            totalPairs += cnt[comp];
        }

        if (x >= 0 && x <= MAX_VAL) {
            cnt[x]++;
        }
    }

    cout << totalPairs << '\n';

    return 0;
}
```

#### Điều cần theo dõi khi debug

| Thao tác | Đánh giá |
|---|---|
| Cộng `cnt[comp]` trước rồi mới `cnt[x]++` |  Đúng, tự động bảo đảm chỉ ghép với phần tử đứng trước ($i < j$). |
| Khai báo `long long totalPairs` |  Đúng, chống tràn số khi số cặp vượt $2 \times 10^9$. |

#### Tự kiểm tra

1. Nếu đổi thứ tự thực hiện `cnt[x]++` trước rồi mới cộng `totalPairs += cnt[comp]`, điều gì sẽ xảy ra khi $x + x = S$?
2. Muốn đếm số cặp bằng nhau ($A_i = A_j$), giá trị `comp` bằng bao nhiêu?

#### Luyện tập ngắn

- **LT 4.4A:** Đếm số cặp $(i, j)$ với $i < j$ thỏa mãn $A_i = A_j$ trong mảng $N$ phần tử ($N \le 10^5$).
- **LT 4.4B:** Đếm số cặp $(i, j)$ với $i < j$ thỏa mãn $A_i - A_j = D$ ($D \ge 0$).

#### Tóm tắt bài

Kỹ thuật "vừa duyệt vừa đếm" kết hợp mảng tần suất giúp đếm cặp trong $\mathcal{O}(N)$. Luôn dùng `long long` cho biến đếm kết quả.

---

### Bài 4.5 — Nguyên lý Dirichlet trong Tin học

#### Mục tiêu bài

Sau Bài 4.5, em hiểu nguyên lý Dirichlet (nguyên lý chuồng bồ câu) và biết cách áp dụng mảng số dư tiền tố để tìm đoạn con liên tiếp có tổng chia hết cho $N$.

#### Khởi động

Nếu có **4 chiếc áo** và chỉ có **3 chiếc móc treo**, khi treo hết 4 chiếc áo chắc chắn sẽ có **ít nhất một chiếc móc treo từ 2 chiếc áo trở lên**.

#### Nguyên lý Dirichlet và Đoạn con chia hết

- **Nguyên lý cơ bản:** Nhốt $N + 1$ đồ vật vào $N$ chiếc hộp $\implies$ tồn tại ít nhất một hộp chứa từ 2 đồ vật trở lên.
- **Ứng dụng tìm đoạn con chia hết cho $N$:**  
  Xét $N$ tổng tiền tố $S_1, S_2, \dots, S_N$. Lấy số dư khi chia cho $N$: $R_i = S_i \pmod N$.
  - Nếu có $S_k \pmod N == 0 \implies$ đoạn $[1, k]$ chia hết cho $N$.
  - Nếu không, $N$ số dư chỉ nhận $N - 1$ giá trị từ $1$ đến $N - 1$. Theo Dirichlet, chắc chắn có hai vị trí $u < v$ sao cho $S_u \equiv S_v \pmod N \implies$ tổng đoạn từ $u + 1$ đến $v$ là $S_v - S_u$ chia hết cho $N$!

#### Mô phỏng cho dãy $N = 5$: $A = [2, 3, 7, 1, 4]$

| $i$ | $A_i$ | Tổng tiền tố $S_i$ | Số dư $R_i = S_i \pmod 5$ | Ghi nhận vị trí đầu tiên của số dư |
|:---:|:---:|:---:|:---:|---|
| $0$ | - | $S_0 = 0$ | $0$ | `firstPos[0] = 0` |
| $1$ | $2$ | $S_1 = 2$ | $2$ | `firstPos[2] = 1` |
| $2$ | $3$ | $S_2 = 5$ | $0$ | Trùng số dư 0 $\implies$ **Đoạn $[1, 2]$ tổng bằng 5 chia hết cho 5!** |

#### Pseudocode

```text
firstPos = mảng kích thước n, gán toàn bộ bằng -1
firstPos[0] = 0
prefix = 0

for i từ 1 đến n:
    prefix = prefix + a[i]
    rem = (prefix % n + n) % n
    nếu firstPos[rem] != -1:
        in (firstPos[rem] + 1) và i
        dừng
    firstPos[rem] = i
```

#### Code C++

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> firstPos(n, -1);
    firstPos[0] = 0;

    long long currentPrefix = 0;
    int ansL = -1, ansR = -1;

    for (int i = 1; i <= n; i++) {
        long long x;
        cin >> x;
        currentPrefix += x;
        int rem = (currentPrefix % n + n) % n;

        if (firstPos[rem] != -1) {
            ansL = firstPos[rem] + 1;
            ansR = i;
            break;
        } else {
            firstPos[rem] = i;
        }
    }

    cout << ansL << " " << ansR << '\n';

    return 0;
}
```

#### Điều cần theo dõi khi debug

| Biến | Lưu ý |
|---|---|
| `firstPos[0] = 0` | Mốc số dư 0 ở trước mảng (tổng rỗng). |
| `(prefix % n + n) % n` | Công thức an toàn đảm bảo số dư không âm. |

#### Tự kiểm tra

1. Vì sao mảng $N$ phần tử luôn tìm được ít nhất một đoạn con có tổng chia hết cho $N$?
2. Công thức `ansL = firstPos[rem] + 1` vì sao phải cộng thêm 1?

#### Luyện tập ngắn

- **LT 4.5A:** Đếm tổng số đoạn con liên tiếp có tổng chia hết cho $K$ ($K \le 10^5$) bằng mảng tần suất số dư tiền tố.
- **LT 4.5B:** Cho $N + 1$ số nguyên thuộc $[1, 2N]$. Chứng minh luôn có 2 số mà số này là bội của số kia.

#### Tóm tắt bài

Nguyên lý Dirichlet kết hợp mảng lưu vị trí số dư tiền tố giải quyết bài toán tìm đoạn con chia hết trong $\mathcal{O}(N)$.

---

### Bài 4.6 — Ôn tập, kiểm tra và bài chuyển giao

#### Mục tiêu bài

Bài này giúp em củng cố các kỹ thuật thống kê tần suất, đếm cặp và đoạn con chia hết.

#### Tầng A — Củng cố nền tảng

##### Bài 4.6.1 — Phổ điểm kỳ thi
Cho điểm thi của $N$ thí sinh từ $0$ đến $10$ ($N \le 10^5, 0 \le A_i \le 10$). In số thí sinh đạt từng mức điểm từ 0 đến 10.
- **Input:** $N$ và dãy $N$ điểm số.
- **Output:** 11 số nguyên tương ứng số lượng thí sinh đạt điểm $0..10$.
- **Ví dụ:** `5` và `8 9 8 10 8` $\implies$ Output: `0 0 0 0 0 0 0 0 3 1 1`.

##### Bài 4.6.2 — Phần tử độc nhất
Cho dãy $N$ số nguyên ($N \le 10^5, 1 \le A_i \le 10^5$). Tìm giá trị nhỏ nhất chỉ xuất hiện đúng 1 lần. Nếu không có, in `-1`.
- **Ví dụ:** `6` và `4 2 7 2 4 9` $\implies$ Output: `7`.

##### Bài 4.6.3 — Ký tự hiếm nhất
Cho xâu $S$ gồm các chữ cái in thường ($|S| \le 10^5$). Tìm chữ cái xuất hiện ít nhất một lần nhưng có số lần xuất hiện nhỏ nhất.
- **Ví dụ:** `banana` $\implies$ Output: `b`.

##### Bài 4.6.4 — Thống kê độ tuổi
Cho độ tuổi của $N$ người và $Q$ truy vấn $[L, R]$. Đếm số người có độ tuổi trong đoạn $[L, R]$ ($N, Q \le 10^5, 18 \le L \le R \le 60$).

---

#### Tầng B — Vận dụng mẫu

##### Bài 4.6.5 — Đếm cặp có tổng bằng K
Cho dãy $N$ số nguyên ($N \le 10^5, 0 \le A_i \le 10^5$). Đếm số cặp $(i, j)$ với $i < j$ thỏa mãn $A_i + A_j = K$.
- **Ví dụ:** `4 10` và `3 7 5 7` $\implies$ Output: `2`.

##### Bài 4.6.6 — Đếm cặp có hiệu bằng D
Cho dãy $N$ số nguyên ($N \le 10^5, 0 \le A_i \le 10^5$). Đếm số cặp $(i, j)$ với $i < j$ thỏa mãn $|A_i - A_j| = D$.

##### Bài 4.6.7 — Phần tử xuất hiện nhiều hơn N/3 lần
Cho dãy $N$ số nguyên. Tìm tất cả các giá trị xuất hiện nhiều hơn $\lfloor N / 3 \rfloor$ lần theo thứ tự tăng dần. Nếu không có, in `-1`.

##### Bài 4.6.8 — Ghép đôi hoàn hảo
Cho $2N$ số nguyên. Kiểm tra xem có thể ghép $2N$ số thành $N$ cặp số bằng nhau hay không. In `YES` hoặc `NO`.
- **Ví dụ:** `4` số `41 42 41 42` $\implies$ Output: `YES`.

---

#### Tầng C — Chuyển giao

##### Bài 4.6.9 — Đếm bộ ba có tổng bằng S
Cho dãy $N$ số nguyên ($N \le 2000, 0 \le A_i \le 10^5$). Đếm số bộ ba $(i, j, k)$ với $i < j < k$ thỏa mãn $A_i + A_j + A_k = S$.
- **Gợi ý:** Cố định phần tử ở giữa $j$, dùng mảng tần suất đếm các phần tử $i < j$.

##### Bài 4.6.10 — Đếm đoạn con có tổng chia hết cho K
Cho dãy $N$ số nguyên ($N \le 10^5, A_i \le 10^9$). Đếm số đoạn con liên tiếp có tổng chia hết cho $K$ ($K \le 10^5$).
- **Ví dụ:** `4 3` và `1 2 3 3` $\implies$ Output: `4`.

##### Bài 4.6.11 — Ghép đôi cùng điểm số
Cho dãy $A$ gồm $N$ số và dãy $B$ gồm $M$ số ($N, M \le 10^5, 0 \le A_i, B_j \le 10^5$). Đếm số cách chọn một số từ $A$ và một số từ $B$ bằng nhau.
- **Công thức:** $\sum \text{cntA}[v] \times \text{cntB}[v]$.

##### Bài 4.6.12 — Đếm cặp chuỗi Anagram
Cho $N$ chuỗi ký tự ngắn ($N \le 10^5, |S_i| \le 10$). Đếm số cặp chuỗi $(i, j)$ với $i < j$ là Anagram của nhau.

---

#### Phiếu tự đánh giá

| Năng lực | Chưa chắc | Làm khi có gợi ý | Tự làm được |
|---|:---:|:---:|:---:|
| Xây dựng mảng tần suất $\mathcal{O}(N)$ |  |  |  |
| Tìm Mode và Phần tử đa số tuyệt đối |  |  |  |
| Ánh xạ chữ cái `'a'..'z'` kiểm tra Anagram |  |  |  |
| Đếm cặp có tổng bằng $S$ trong $\mathcal{O}(N)$ |  |  |  |
| Khai báo `long long` chống tràn số khi đếm cặp |  |  |  |
| Tìm đoạn con chia hết cho $N$ bằng Dirichlet |  |  |  |

#### Tiêu chí hoàn thành chương

Em có thể xem mình đã nắm chắc chương khi:
1. Giải thích được tại sao mảng tần suất giúp giảm độ phức tạp từ $\mathcal{O}(N^2)$ xuống $\mathcal{O}(N)$.
2. Viết được hàm đếm cặp tổng bằng $S$ không dùng 2 vòng lặp lồng nhau.
3. Biết cách ánh xạ chữ cái bằng phép trừ `c - 'a'`.
4. Không mắc bẫy tràn số khi đếm số lượng cặp.

---

### Tổng kết chương

> **Mảng tần suất là bước đột phá từ tư duy so sánh tuần tự sang tư duy định vị trực tiếp. Bằng cách biến giá trị thành chỉ số, ta giải quyết bài toán thống kê và đếm cặp trong thời gian tuyến tính $\mathcal{O}(N)$.**

| Cần nhớ | Nội dung |
|---|---|
| Mảng tần suất | `cnt[x]++` với $0 \le x \le \text{MAX\_VAL}$, thời gian $\mathcal{O}(N)$, bộ nhớ $\mathcal{O}(\text{MAX\_VAL})$ |
| Bảng chữ cái | Mảng kích thước 26 phần tử với chỉ số `c - 'a'` |
| Đếm cặp tổng $S$ | Cộng `cnt[S - x]` trước rồi mới `cnt[x]++` |
| Đếm cặp bằng nhau | Cộng dồn `cnt[x]` khi duyệt hoặc tính $\sum \frac{C(C-1)}{2}$ |
| Chống tràn số | Biến đếm cặp bắt buộc dùng kiểu `long long` |
| Dirichlet | $N$ tổng tiền tố chia cho $N$ luôn có 2 tổng cùng số dư $\implies$ đoạn con chia hết |

#### Những lỗi thường gặp

| Lỗi | Cách tự kiểm tra |
|---|---|
| Kích thước mảng `cnt` nhỏ hơn $\max(A_i)$ | Luôn khai báo `MAX_VAL >= max(A_i)` |
| Tràn số khi đếm số lượng cặp | Biến đếm số cặp phải là `long long` |
| Quên trường hợp $A_i$ âm | Tịnh tiến chỉ số `cnt[x + OFFSET]` |
| Số dư bị âm khi tính `prefix % N` | Dùng công thức an toàn `(prefix % N + N) % N` |

---

### Code tham chiếu

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAX_VAL = 100000;

// 1. Dem so cap co tong bang S trong O(N)
long long countPairsWithSum(const vector<int> &a, int s) {
    vector<int> cnt(MAX_VAL + 1, 0);
    long long totalPairs = 0;

    for (int x : a) {
        int comp = s - x;
        if (comp >= 0 && comp <= MAX_VAL) {
            totalPairs += cnt[comp];
        }
        if (x >= 0 && x <= MAX_VAL) {
            cnt[x]++;
        }
    }
    return totalPairs;
}

// 2. Kiem tra hai chuoi Anagram O(N)
bool isAnagram(const string &s, const string &t) {
    if (s.length() != t.length()) return false;
    vector<int> cnt(26, 0);
    for (char c : s) cnt[c - 'a']++;
    for (char c : t) cnt[c - 'a']--;
    for (int i = 0; i < 26; i++) {
        if (cnt[i] != 0) return false;
    }
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, s;
    if (!(cin >> n >> s)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    cout << "Pairs with sum " << s << ": " << countPairsWithSum(a, s) << "\n";

    return 0;
}
```

---

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
