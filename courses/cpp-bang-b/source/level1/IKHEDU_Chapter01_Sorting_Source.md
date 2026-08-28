# TÀI LIỆU GỐC — CHƯƠNG 1: SẮP XẾP

## Vai trò tài liệu

Tài liệu này là bản gốc nội dung dùng để biên soạn Chương 1 — Sắp xếp. Nội dung được review và hoàn thiện tại đây trước khi tổng hợp sang bản thảo sách.

## Đối tượng và phạm vi

Tài liệu dành cho học sinh bắt đầu học thuật toán, đã biết các thao tác C++ nền tảng. Luồng nhập môn chỉ dùng `int`, `vector<int>`, vòng lặp, so sánh, `swap` và `sort`; nội dung nhiều thuộc tính là phần mở rộng.

## Nguyên tắc biên soạn

Mỗi bài gồm mục tiêu, giải thích, ví dụ, thực hành, tự kiểm tra và tóm tắt. Nội dung phải được kiểm tra về tính đúng đắn, độ khó, code C++17 và khả năng sử dụng trong lớp học trước khi đưa vào BOOK_MASTER.

---

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
