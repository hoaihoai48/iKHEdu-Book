---
title: "Khoá học C++ cơ bản"
subtitle: "Từ nền tảng lập trình đến thuật toán thi đấu"
author: "Trung tâm tin học iKH"
lang: vi
documentclass: report
geometry: "a4paper, margin=2.5cm"
fontsize: 12pt
mainfont: "Times New Roman"
monofont: "Courier New"
header-includes:
  - \usepackage{fancyhdr}
  - \pagestyle{fancy}
  - \fancyhead[L]{\textit{Khoá học C++ cơ bản}}
  - \fancyhead[R]{\textit{Trung tâm tin học iKH}}
---


# Lời nói đầu

Cuốn sách **Khoá học C++ cơ bản** được biên soạn bởi **Trung tâm tin học iKH** nhằm cung cấp cho các em học sinh một lộ trình học tập toàn diện, hệ thống và chuyên sâu về lập trình C++ — từ nền tảng cơ bản đến các thuật toán nâng cao trong lập trình thi đấu.

Sách được thiết kế dành cho học sinh chuẩn bị tham gia các kỳ thi **Tin học trẻ Bảng B**, **Học sinh giỏi THCS** và các cuộc thi lập trình thuật toán. Nội dung được tổ chức theo **7 Chương trọng tâm** với **21 Bài học** bao phủ toàn bộ kiến thức cần thiết, từ thuật toán sắp xếp, kỹ thuật hai con trỏ, cửa sổ trượt, mảng tiền tố, tìm kiếm nhị phân cho đến quy hoạch động, cấu trúc dữ liệu nâng cao, đồ thị và cây truy vấn đoạn.

Mỗi bài học trong sách tuân theo một khung logic sư phạm nhất quán:

- **Khái niệm & bản chất toán học** — giúp học sinh hiểu sâu thay vì chỉ nhớ cú pháp.
- **Chứng minh & bất biến thuật toán** — rèn tư duy phân tích nghiêm ngặt.
- **Mẫu cài đặt chuẩn thi đấu** — code C++ sạch, tối ưu, sẵn sàng nộp bài.
- **Bẫy lỗi lập trình kinh điển** — cảnh báo những sai lầm phổ biến nhất.
- **Bài tập thực hành phân tầng** — từ cơ bản đến nâng cao, mỗi bài có đề bài chi tiết.

Toàn bộ code C++ trong sách tuân theo chuẩn thi đấu iKHEDU: sử dụng `#include <bits/stdc++.h>`, Fast I/O và Safe Input, giúp học sinh làm quen với phong cách lập trình chuyên nghiệp ngay từ đầu.

Chúng tôi tin rằng lập trình không chỉ là viết code, mà là **tư duy giải quyết vấn đề**. Mỗi bài toán trong sách đều được thiết kế để rèn luyện khả năng phân tích, mô hình hóa và tối ưu hóa — những kỹ năng sẽ đồng hành cùng các em trong suốt hành trình học tập và sự nghiệp.

Chúc các em học tập hiệu quả và đạt kết quả cao!

**Trung tâm tin học iKH**

\newpage




# CHƯƠNG 01: THUẬT TOÁN SẮP XẾP & KỸ THUẬT MẢNG


# Bài 01: Thuật toán sắp xếp


## 1. Khái niệm & bản chất của sắp xếp trong tối ưu thuật toán

**Sắp xếp (Sorting)** là quá trình tái sắp đặt các phần tử trong một tập dữ liệu theo một trật tự xác định (thường là tăng dần hoặc giảm dần theo một hoặc nhiều tiêu chí).

Trong lập trình thi đấu và khoa học máy tính, sắp xếp không đơn thuần là định dạng lại dữ liệu hiển thị, mà là một **phép biến đổi cấu trúc dữ liệu** nhằm:

* **Tạo tính đơn điệu (Monotonicity):** Đưa dãy số về trạng thái có trật tự để áp dụng các kỹ thuật tối ưu như *Hai con trỏ (Two Pointers)*, *Tìm kiếm nhị phân (Binary Search)* hoặc *Tham lam (Greedy)*.
* **Khai thác tính chất lân cận (Adjacency Property):** Gom các phần tử có giá trị bằng nhau hoặc gần nhau nhất về các vị trí liền kề, giúp giảm không gian tìm kiếm từ $\mathcal{O}(N^2)$ xuống $\mathcal{O}(N)$.

## 2. Tính chất lân cận & chứng minh toán học

### 2.1. Định lý về cặp phần tử có khoảng cách nhỏ nhất

> **Định lý:** Trong một tập hợp các số thực $A = \{A_1, A_2, \dots, A_N\}$, sau khi sắp xếp tăng dần $A_1 \le A_2 \le \dots \le A_N$, giá trị nhỏ nhất của $|A_i - A_j|$ giữa hai phần tử phân biệt ($i < j$) luôn đạt được tại ít nhất một cặp phần tử kề nhau $(A_k, A_{k+1})$.

### 2.2. Chứng minh toán học
Xét hai chỉ số bất kỳ $i < j$. Nếu $j > i + 1$ (hai phần tử không kề nhau), tồn tại phần tử trung gian $A_{i+1}$ thỏa mãn:

$$A_i \le A_{i+1} \le A_j$$

Hiệu khoảng cách giữa $A_i$ và $A_j$:
$$A_j - A_i = (A_j - A_{i+1}) + (A_{i+1} - A_i)$$

Vì $A_j - A_{i+1} \ge 0$, ta luôn có:
$$A_j - A_i \ge A_{i+1} - A_i$$

**Hệ quả:** Mọi cặp phần tử không kề nhau đều có khoảng cách lớn hơn hoặc bằng khoảng cách của cặp kề nhau $(A_i, A_{i+1})$. Do đó, để tìm khoảng cách nhỏ nhất, ta chỉ cần duyệt qua $N - 1$ cặp kề nhau sau khi sắp xếp.

#### Ví dụ minh họa 1: Tìm khoảng cách nhỏ nhất giữa hai phần tử
Cho mảng gồm 6 phần tử chưa sắp xếp: $A = [15, 3, 9, 22, 4, 11]$

1. **Bước 1: Sắp xếp tăng dần $\mathcal{O}(N \log N)$:**
$$A = [3, 4, 9, 11, 15, 22]$$

2. **Bước 2: Quét $N - 1 = 5$ cặp kề nhau $\mathcal{O}(N)$:**

| Cặp Kề Nhau $(A_i, A_{i+1})$ | Tính Hiệu Số $A_{i+1} - A_i$ | Hiệu Nhỏ Nhất Tạm Thời ($\min$) |
|:---:|:---:|:---:|
| $(3, 4)$ | $4 - 3 = \mathbf{1}$ | $\mathbf{1}$ |
| $(4, 9)$ | $9 - 4 = 5$ | $1$ |
| $(9, 11)$ | $11 - 9 = 2$ | $1$ |
| $(11, 15)$ | $15 - 11 = 4$ | $1$ |
| $(15, 22)$ | $22 - 15 = 7$ | $1$ |

$$\implies \text{Kết quả: Khoảng cách nhỏ nhất là } \mathbf{1} \text{ (giữa cặp 3 và 4), tìm ra trong đúng 5 phép trừ!}$$

## 3. Các ứng dụng thuật toán kinh điển của sắp xếp

| Dạng Bài Toán | Cách Xử Lý Chưa Sắp Xếp | Sau Khi Sắp Xếp $\mathcal{O}(N \log N)$ | Độ Phức Tạp Tối Ưu |
|---|---|---|:---:|
| **Tìm cặp có hiệu nhỏ nhất** | Duyệt mọi cặp $(i, j)$ | So sánh $N-1$ cặp kề $(A_i, A_{i+1})$ | $\mathcal{O}(N \log N)$ |
| **Đếm số giá trị phân biệt** | Quét trùng lặp từng phần tử | Đếm khi $A_i \ne A_{i-1}$ | $\mathcal{O}(N \log N)$ |
| **Tìm phần tử có tần suất cực đại** | Bảng đếm / Quét lặp $\mathcal{O}(N^2)$ | Đếm độ dài khối bằng nhau liên tiếp | $\mathcal{O}(N \log N)$ |
| **Gom cụm chênh lệch $\le K$** | Tìm kiếm nhánh cận | Duyệt tuyến tính gom đoạn kề nhau | $\mathcal{O}(N \log N)$ |

## 4. Hàm `sort` & nguyên lý Strict Weak Ordering

### 4.1. Cú pháp chuẩn trong C++
C++ cung cấp hai hàm sắp xếp có sẵn:

* `sort(first, last)`: Sử dụng thuật toán **IntroSort** (kết hợp giữa QuickSort, HeapSort và InsertionSort), đạt độ phức tạp thời gian $\mathcal{O}(N \log N)$ trong mọi trường hợp (trung bình và xấu nhất). Không bảo toàn thứ tự ban đầu của các phần tử bằng nhau.
* `stable_sort(first, last)`: Sử dụng thuật toán **MergeSort**, độ phức tạp $\mathcal{O}(N \log N)$, đảm bảo bảo toàn nguyên vẹn thứ tự xuất hiện ban đầu của các phần tử có giá trị bằng nhau.

### 4.2. Nguyên lý Strict Weak Ordering (toán tử so sánh nghiêm ngặt)
Một hàm so sánh `cmp(a, b)` truyền vào `sort` **bắt buộc** phải thỏa mãn 3 tiên đề toán học:

1. **Tính bất phản xạ (Irreflexivity):** `cmp(a, a)` luôn trả về `false`.
2. **Tính bất đối xứng (Asymmetry):** Nếu `cmp(a, b)` là `true` thì `cmp(b, a)` bắt buộc phải là `false`.
3. **Tính bắc cầu (Transitivity):** Nếu `cmp(a, b)` là `true` và `cmp(b, c)` là `true` thì `cmp(a, c)` phải là `true`.

### Cảnh báo quan trọng:
**Cảnh báo bẫy lỗi: BẪY DẤU `<= ` TRONG COMPARATOR**

> Nếu viết `return a <= b;`, khi `a == b` thì cả `cmp(a, b)` và `cmp(b, a)` đều trả về `true` $\implies$ Vi phạm tiên đề Bất phản xạ và Bất đối xứng $\implies$ `sort` sẽ tiếp tục truy cập vùng nhớ ngoài biên của mảng $\implies$ **RUNTIME ERROR / CRASH CHƯƠNG TRÌNH**.
> **Lưu ý quan trọng:** Luôn dùng toán tử so sánh nghiêm ngặt (`<` hoặc `>`). Khi hai phần tử bằng nhau (`a == b`), hàm so sánh bắt buộc phải trả về `false`!

## 5. Các kỹ thuật Custom Comparator nâng cao

### 5.1. Sắp xếp đa tiêu chí với vector lồng nhau (multi-criteria sorting)
Khi mỗi phần tử gồm nhiều thuộc tính số (ví dụ: điểm bắt đầu $L = a[0]$ và điểm kết thúc $R = a[1]$ của một đoạn thẳng), ta sử dụng **vector lồng nhau `vector<vector<int>>`** để tận dụng mảng sẵn có:

```cpp
// Ví dụ: Sắp xếp các đoạn thẳng theo điểm kết thúc a[1] tăng dần,
// nếu trùng điểm kết thúc thì theo điểm bắt đầu a[0] giảm dần
bool cmpInterval(const vector<int> &a, const vector<int> &b) {

    if (a[1] != b[1]) {
        return a[1] < b[1]; // Ưu tiên kết thúc sớm hơn đứng trước
    }
    return a[0] > b[0]; // Cùng điểm kết thúc: Bắt đầu muộn hơn đứng trước

}
```

#### Ví dụ minh họa 2: Sắp xếp danh sách 4 đoạn thẳng
Cho 4 đoạn thẳng: $\{ [1, 5], [2, 3], [3, 6], [1, 3] \}$

* **Trước khi sắp xếp:** $[1, 5], [2, 3], [3, 6], [1, 3]$
* **Tiêu chí 1 (Điểm kết thúc tăng dần):** Các đoạn kết thúc tại $3$ đứng trước, sau đó đến $5$, rồi đến $6$.
* **Tiêu chí 2 (Cùng điểm kết thúc $\implies$ bắt đầu giảm dần):** Giữa $[2, 3]$ và $[1, 3]$, đoạn $[2, 3]$ có điểm bắt đầu $2 > 1$ nên được xếp trước.

> **Kết quả sau sắp xếp:** $[[2, 3], [1, 3], [1, 5], [3, 6]]$

### 5.2. Sắp xếp lưu chỉ số ban đầu (index tracking)
Khi bài toán yêu cầu in ra vị trí gốc của các phần tử sau khi sắp xếp, sử dụng **vector 2 chiều `vector<vector<long long>>`** lưu cặp `{giá_trị, chỉ_số_gốc}`:

```cpp
// Khởi tạo vector 2 chiều n hàng, 2 cột: a[i][0] là giá trị, a[i][1] là chỉ số gốc
vector<vector<long long>> a(n, vector<long long>(2));

for (int i = 0; i < n; ++i) {
    cin >> a[i][0];   // Giá trị phần tử

    a[i][1] = i + 1;  // Chỉ số ban đầu (1-based)
}

// sort mặc định so sánh cột 0 (giá trị), nếu bằng nhau so sánh tiếp cột 1 (chỉ số gốc)
sort(a.begin(), a.end());
```

### 5.3. Comparator hàm mục tiêu (objective comparison)
Bài toán ghép $N$ chuỗi số để tạo thành số lớn nhất:

```cpp
bool cmpConcat(const string &a, const string &b) {
    // Sắp xếp sao cho chuỗi ghép a + b lớn hơn chuỗi ghép b + a
    return a + b > b + a;

}
```

## 6. Mẫu cài đặt chuẩn thi đấu (competitive template)

```cpp
# include <bits/stdc++.h>
using namespace std;

int main() {
    // Tối ưu hóa tốc độ I/O
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);

    for (int i = 0; i < n; ++i) {
        cin >> a[i];

    }

    // Bước 1: Sắp xếp mảng O(N log N)
    sort(a.begin(), a.end());

    // Bước 2: Khai thác trật tự tuyến tính O(N)
    long long min_diff = a[1] - a[0];
    for (int i = 1; i < n - 1; ++i) {
        min_diff = min(min_diff, a[i + 1] - a[i]);
    }

    cout << min_diff << "\n";
    return 0;
}
```

## 7. Ranh giới áp dụng: Khi nào được & không được sắp xếp?

* **ĐƯỢC PHÉP SẮP XẾP:** Khi bài toán khảo sát tính chất trên **toàn bộ tập hợp** mà không phụ thuộc vào vị trí ban đầu của phần tử (như tìm $\min/\max$, đếm giá trị phân biệt, tìm cặp thỏa mãn điều kiện đại số).
* **KHÔNG ĐƯỢC PHÉP SẮP XẾP:** Khi bài toán có ràng buộc gắn liền với **dòng thời gian hoặc vị trí liền kề nguyên thủy** (như tìm đoạn con liên tiếp, chuỗi con tăng dài nhất bảo toàn thứ tự ban đầu).

## Bài tập thực hành


### Bài 01 [CPPB-SX-01]: Xếp Hàng Điểm Danh

**Bối cảnh:** Trong buổi học thể dục đầu năm, thầy giáo muốn xếp hàng $N$ bạn học sinh theo thứ tự chiều cao từ thấp đến cao để chuẩn bị cho bài tập đồng diễn.

**Nhiệm vụ:** Cho danh sách chiều cao của $N$ bạn học sinh. Hãy in ra danh sách chiều cao sau khi đã xếp hàng theo thứ tự tăng dần.

**Đầu vào (Input):**

- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 1000$).
- Dòng 2: Chứa $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^6$).

**Đầu ra (Output):**

- In ra trên một dòng gồm $N$ số nguyên biểu diễn chiều cao sau khi sắp xếp tăng dần, cách nhau bởi khoảng trắng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 <br> 1550 1420 1680 1500 1600 | 1420 1500 1550 1600 1680 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 1000, 1 \le A_i \le 10^6$.



### Bài 02 [CPPB-SX-02]: Khoảng Cách Nhỏ Nhất

**Bối cảnh:** Cho tập hợp gồm $N$ số nguyên. Hãy tìm khoảng cách nhỏ nhất giữa hai số bất kỳ trong tập hợp đó.

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $N$ ($2 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

**Đầu ra (Output):**

- In ra khoảng cách nhỏ nhất giữa hai phần tử bất kỳ.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 <br> 8 3 14 6 10 | 2 |

**Ràng buộc & Giới hạn:**

- $40\%$ số test có $N \le 1000$.
- $60\%$ số test có $N \le 10^5$.



### Bài 03 [CPPB-SX-03]: Sắp Xếp Theo Trị Tuyệt Đối

**Bối cảnh:** Cho một dãy gồm $N$ số nguyên. Hãy sắp xếp các phần tử theo giá trị tuyệt đối tăng dần. Nếu hai phần tử có cùng giá trị tuyệt đối, số âm phải đứng trước số dương.

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

**Đầu ra (Output):**

- In ra dãy số sau khi sắp xếp, cách nhau bởi một khoảng trắng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 <br> 5 -8 2 -3 8 | 2 -3 5 -8 8 |

**Ràng buộc & Giới hạn:**

- $40\%$ số test có $N \le 1000$.
- $60\%$ số test có $N \le 10^5$.



### Bài 04 [CPPB-SX-04]: Đếm Giá Trị Phân Biệt

**Bối cảnh:** Cho dãy số nguyên gồm $N$ phần tử. Hãy đếm xem trong dãy có bao nhiêu giá trị phân biệt.

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 2 \cdot 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là số lượng giá trị phân biệt.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 6 <br> 2 3 2 1 3 5 | 4 |

**Ràng buộc & Giới hạn:**

- $40\%$ số test có $N \le 1000$.
- $60\%$ số test có $N \le 2 \cdot 10^5$.



### Bài 05 [CPPB-SX-05]: Hai Trạm Kiểm Soát Gần Nhau Nhất

**Bối cảnh:** Trên một tuyến quốc lộ thẳng tắp, có $N$ trạm kiểm soát tự động tại tọa độ $X_1, X_2, \dots, X_N$ ($0 \le X_i \le 10^{12}$). Hãy tìm khoảng cách ngắn nhất giữa hai trạm bất kỳ.

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $N$ ($2 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên không âm $X_1, X_2, \dots, X_N$ ($0 \le X_i \le 10^{12}$).

**Đầu ra (Output):**

- In ra khoảng cách ngắn nhất giữa hai trạm.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 6 <br> 1500 300 2800 800 1200 3150 | 300 |

**Ràng buộc & Giới hạn:**

- $40\%$ số test có $N \le 1000$.
- $60\%$ số test có $N \le 10^5, X_i \le 10^{12}$.



### Bài 06 [CPPB-SX-06]: Khoảng Trống Lớn Nhất Trên Trục Tọa Độ

**Bối cảnh:** Cho $N$ chướng ngại vật tại các vị trí $A_1, A_2, \dots, A_N$ ($-10^{18} \le A_i \le 10^{18}$). Hãy tìm khoảng cách lớn nhất giữa hai chướng ngại vật liên tiếp sau khi sắp xếp.

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $N$ ($2 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^{18} \le A_i \le 10^{18}$).

**Đầu ra (Output):**

- In ra khoảng cách lớn nhất giữa hai chướng ngại vật liên tiếp.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 <br> 10 3 25 8 12 | 13 |

**Ràng buộc & Giới hạn:**

- $40\%$ số test có $N \le 1000, \vert A_i \vert \le 10^9$.
- $60\%$ số test có $N \le 10^5, \vert A_i \vert \le 10^{18}$.



### Bài 07 [CPPB-SX-07]: Sắp Xếp Theo Tổng Chữ Số

**Bối cảnh:** Cho $N$ số nguyên dương. Hãy sắp xếp dãy số theo **tổng các chữ số tăng dần**. Nếu hai số có cùng tổng chữ số, số có giá trị nhỏ hơn sẽ đứng trước.

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

**Đầu ra (Output):**

- In ra dãy số sau khi sắp xếp, cách nhau bởi khoảng trắng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 <br> 13 20 4 103 11 | 11 20 4 13 103 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 10^5, 1 \le A_i \le 10^9$.



### Bài 08 [CPPB-SX-08]: Gom Cụm Chênh Lệch Không Quá K

**Bối cảnh:** Cho $N$ học sinh với điểm số $A_1, A_2, \dots, A_N$. Giáo viên muốn chia các bạn học sinh thành các nhóm sao cho trong mỗi nhóm, chênh lệch điểm số giữa bạn cao nhất và bạn thấp nhất không vượt quá $K$.

**Nhiệm vụ:** Hãy tìm số lượng nhóm ít nhất để phân chia toàn bộ $N$ học sinh.

**Đầu vào (Input):**

- Dòng 1: Chứa 2 số nguyên dương $N$ và $K$ ($1 \le N \le 2 \cdot 10^5, 0 \le K \le 10^9$).
- Dòng 2: $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

**Đầu ra (Output):**

- In ra số lượng nhóm ít nhất cần chia.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 6 3 <br> 1 10 3 4 12 15 | 3 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 2 \cdot 10^5, K \le 10^9, A_i \le 10^9$.



### Bài 09 [CPPB-SX-09]: Tìm Phần Tử Xuất Hiện Nhiều Nhất

**Bối cảnh:** Cho một dãy gồm $N$ số nguyên. Hãy tìm phần tử có số lần xuất hiện nhiều nhất trong dãy. Nếu có nhiều phần tử có cùng số lần xuất hiện cực đại, in ra phần tử có giá trị nhỏ nhất.

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 2 \cdot 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

**Đầu ra (Output):**

- In ra hai số nguyên: giá trị của phần tử xuất hiện nhiều nhất và số lần xuất hiện của nó.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 7 <br> 3 5 2 3 5 3 2 | 3 3 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 2 \cdot 10^5, \vert A_i \vert \le 10^9$.



### Bài 10 [CPPB-SX-10]: Sắp Xếp Lưu Vị Trí Ban Đầu

**Bối cảnh:** Cho một dãy gồm $N$ số nguyên $A_1, A_2, \dots, A_N$. Hãy sắp xếp các phần tử theo thứ tự tăng dần, đồng thời in ra vị trí ban đầu (chỉ số 1-indexed) của mỗi phần tử trong mảng gốc. Nếu hai phần tử có cùng giá trị, phần tử xuất hiện trước trong mảng gốc sẽ đứng trước.

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

**Đầu ra (Output):**

- In ra $N$ dòng, mỗi dòng gồm 2 số nguyên biểu diễn giá trị phần tử và chỉ số ban đầu của nó.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 <br> 40 10 20 10 30 | 10 2 <br> 10 4 <br> 20 3 <br> 30 5 <br> 40 1 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 10^5, \vert A_i \vert \le 10^9$.



### Bài 11 [CPPB-SX-11]: Ghép Chuỗi Tạo Số Lớn Nhất

**Bối cảnh:** Cho $N$ số nguyên không âm biểu diễn dưới dạng chuỗi ký tự. Hãy ghép toàn bộ $N$ số này lại với nhau theo thứ tự nào đó để tạo thành số có giá trị lớn nhất.

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^4$).
- Dòng 2: $N$ chuỗi số $S_1, S_2, \dots, S_N$ (độ dài mỗi chuỗi không quá 10 ký tự).

**Đầu ra (Output):**

- In ra chuỗi số lớn nhất tạo được. Nếu kết quả gồm toàn số 0, in ra `0`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 <br> 3 30 34 5 | 534330 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 10^4$.



### Bài 12 [CPPB-SX-12]: Bảng Điểm Học Sinh Đa Trường

**Bối cảnh:** Cho danh sách $N$ học sinh tham gia kỳ thi. Mỗi học sinh có mã số $ID$, điểm thi Toán và điểm thi Tin. Hãy sắp xếp danh sách học sinh theo các quy tắc sau:
1. Tổng điểm (Toán + Tin) giảm dần.
2. Nếu bằng tổng điểm, điểm Tin học cao hơn đứng trước.
3. Nếu vẫn bằng nhau, mã số $ID$ nhỏ hơn đứng trước.

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
- $N$ dòng tiếp theo: Mỗi dòng gồm 3 số nguyên $ID, Math, Info$ ($1 \le ID \le 10^9, 0 \le Math, Info \le 100$).

**Đầu ra (Output):**

- In ra danh sách học sinh sau khi sắp xếp, mỗi học sinh gồm 3 số $ID, Math, Info$ trên một dòng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 <br> 101 8 9 <br> 102 9 8 <br> 103 10 10 | 103 10 10 <br> 101 8 9 <br> 102 9 8 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 10^5$.



### Bài 13 [CPPB-SX-13]: Bảng Xếp Hạng Giải Đấu Thể Thao

**Bối cảnh:** Cho kết quả của $N$ đội bóng gồm: Mã đội $ID$, Điểm số $Points$, Hiệu số bàn thắng $GoalDiff$, Số bàn thắng ghi được $Goals$. Hãy xếp hạng các đội theo thứ tự:
1. Điểm số giảm dần.
2. Hiệu số bàn thắng giảm dần.
3. Số bàn thắng ghi được giảm dần.
4. Mã đội $ID$ tăng dần.

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
- $N$ dòng tiếp theo: Mỗi dòng gồm 4 số nguyên $ID, Points, GoalDiff, Goals$.

**Đầu ra (Output):**

- In ra danh sách mã đội $ID$ sau khi đã sắp xếp thứ hạng, cách nhau bởi khoảng trắng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 <br> 1 10 5 12 <br> 2 10 5 15 <br> 3 12 2 8 | 3 2 1 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 10^5$.



### Bài 14 [CPPB-SX-14]: Sắp Xếp Đoạn Thẳng Không Giao Lỗi

**Bối cảnh:** Cho $N$ đoạn thẳng $[L_i, R_i]$ trên trục số. Hãy sắp xếp các đoạn thẳng theo tiêu chí:
1. Tọa độ đầu mút $L_i$ tăng dần.
2. Nếu cùng $L_i$, tọa độ $R_i$ giảm dần.
3. Nếu trùng cả $L_i$ và $R_i$, giữ nguyên thứ tự ban đầu (sắp xếp ổn định).

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 2 \cdot 10^5$).
- $N$ dòng tiếp theo: Mỗi dòng gồm 2 số nguyên $L_i, R_i$ ($-10^9 \le L_i \le R_i \le 10^9$).

**Đầu ra (Output):**

- In ra $N$ dòng, mỗi dòng gồm 2 số $L_i, R_i$ sau khi sắp xếp.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 <br> 2 8 <br> 1 5 <br> 2 10 | 1 5 <br> 2 10 <br> 2 8 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 2 \cdot 10^5$.




# Bài 02: Kỹ thuật hai con trỏ


## 1. Khái niệm & nguyên lý hoạt động

**Kỹ thuật Hai con trỏ (Two Pointers Technique)** là phương pháp sử dụng hai biến chỉ số (thường ký hiệu là $L$ và $R$) duyệt trên cấu trúc dữ liệu tuyến tính (mảng hoặc chuỗi) nhằm thu hẹp không gian tìm kiếm từ $\mathcal{O}(N^2)$ xuống $\mathcal{O}(N)$.

Trong mô hình **Hai con trỏ đối đầu (Opposite-direction Two Pointers)**:

* Con trỏ trái $L$ khởi tạo tại đầu mảng ($L = 0$).
* Con trỏ phải $R$ khởi tạo tại cuối mảng ($R = N - 1$).
* Dãy số bắt buộc phải có **tính đơn điệu** (thường là mảng đã sắp xếp tăng dần $A_0 \le A_1 \le \dots \le A_{N-1}$).

Tại mỗi bước, thuật toán tính toán một hàm mục tiêu trên cặp phần tử $(A_L, A_R)$ (ví dụ: $\text{Sum} = A_L + A_R$) và so sánh với giá trị đích $S$:

* **Nếu $\text{Sum} == S$:** Tìm thấy nghiệm hợp lệ.
* **Nếu $\text{Sum} < S$:** Tổng hiện tại nhỏ hơn mục tiêu $\implies$ Tăng con trỏ trái (`++L`) để tìm kiếm tổng lớn hơn.
* **Nếu $\text{Sum} > S$:** Tổng hiện tại lớn hơn mục tiêu $\implies$ Giảm con trỏ phải (`--R`) để tìm kiếm tổng nhỏ hơn.

## 2. Chứng minh bất biến lặp (loop invariant) & tính đúng đắn

### 2.1. Phát biểu bất biến lặp

> **Bất biến lặp:** Tại bất kỳ thời điểm nào trong quá trình thực thi, nếu tồn tại một cặp nghiệm $(i, j)$ thỏa mãn $A_i + A_j = S$ ($i < j$), thì cặp nghiệm đó chắc chắn nằm trọn vẹn trong đoạn chỉ số đang xét: $L \le i < j \le R$.

### 2.2. Chứng minh quy nạp toán học

1. **Khởi tạo:** Ban đầu $L = 0, R = N - 1$, đoạn $[L, R]$ bao phủ toàn bộ mảng, bất biến lặp hiển nhiên đúng.
2. **Duy trì:** Giả sử bất biến lặp đúng tại bước hiện tại $[L, R]$.
* **Trường hợp 1: $A_L + A_R > S$ (Thao tác `--R`):**

Vì mảng tăng dần, với mọi chỉ số $k \in [L, R-1]$, ta luôn có $A_k \ge A_L \implies A_k + A_R \ge A_L + A_R > S$.

Do đó, phần tử $A_R$ không thể tạo thành tổng $S$ với bất kỳ phần tử nào trong đoạn $[L, R-1]$. Việc loại bỏ $R$ bằng cách giảm $R \to R - 1$ không làm mất bất kỳ nghiệm hợp lệ nào.

* **Trường hợp 2: $A_L + A_R < S$ (Thao tác `++L`):**
Vì mảng tăng dần, với mọi chỉ số $k \in [L+1, R]$, ta luôn có $A_k \le A_R \implies A_L + A_k \le A_L + A_R < S$.
Do đó, phần tử $A_L$ không thể tạo thành tổng $S$ với bất kỳ phần tử nào trong đoạn $[L+1, R]$. Việc loại bỏ $L$ bằng cách tăng $L \to L + 1$ là an toàn $100\%$.

3. **Kết thúc:** Vòng lặp dừng khi $L \ge R$. Nếu không tìm thấy nghiệm, chứng tỏ không tồn tại cặp $(i, j)$ nào thỏa mãn $A_i + A_j = S$.

## 3. Các mô hình bài toán đặc trưng

### 3.1. Mô hình 1: Tìm cặp số có tổng đúng bằng $S$ (two sum)

* **Mục tiêu:** Tìm $i < j$ sao cho $A_i + A_j = S$.
* **Quy tắc di chuyển:**
* Nếu $A_L + A_R < S \implies L \leftarrow L + 1$ (Tổng nhỏ hơn mục tiêu, tăng cận dưới).
* Nếu $A_L + A_R > S \implies R \leftarrow R - 1$ (Tổng lớn hơn mục tiêu, giảm cận trên).

* Nếu $A_L + A_R = S \implies$ Ghi nhận nghiệm và dừng thuật toán.

#### Ví dụ minh họa 1: Tìm cặp số có tổng $S = 14$
Cho mảng $N = 6$ phần tử đã sắp xếp: $A = [2, 3, 5, 8, 11, 15]$ (0-based indexing).

| Phần tử | $A[0]$ | $A[1]$ | $A[2]$ | $A[3]$ | $A[4]$ | $A[5]$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Giá trị** | $\mathbf{2}$ | $\mathbf{3}$ | $\mathbf{5}$ | $\mathbf{8}$ | $\mathbf{11}$ | $\mathbf{15}$ |

**Bảng mô phỏng từng bước lặp Hai con trỏ:**

| Bước | Con trỏ $(L, R)$ | Giá trị $(A_L, A_R)$ | Tổng $A_L + A_R$ | Đánh giá & Hành động |
| :---: | :---: | :---: | :---: | :--- |
| **1** | $(0, 5)$ | $(2, 15)$ | $2 + 15 = 17$ | $17 > 14 \implies$ Giảm con trỏ phải: $R \leftarrow 4$ |
| **2** | $(0, 4)$ | $(2, 11)$ | $2 + 11 = 13$ | $13 < 14 \implies$ Tăng con trỏ trái: $L \leftarrow 1$ |
| **3** | $(1, 4)$ | $(3, 11)$ | $3 + 11 = \mathbf{14}$ | $14 = 14 \implies$ **Khớp mục tiêu!** Cặp nghiệm $(A_1, A_4) = (3, 11)$ |

### 3.2. Mô hình 2: Đếm số cặp có tổng thỏa mãn bất đẳng thức $A_i + A_j \le S$

* **Mục tiêu:** Đếm số lượng cặp $(i, j)$ với $i < j$ thỏa mãn $A_i + A_j \le S$.
* **Khai thác tổ hợp:**
Nếu tại bước $(L, R)$ ta có $A_L + A_R \le S$, thì do mảng tăng dần, mọi phần tử $A_k$ với $L < k \le R$ khi ghép với $A_L$ đều thỏa mãn:
$$A_L + A_k \le A_L + A_R \le S$$
Do đó, có đúng **$R - L$ cặp hợp lệ** xuất phát từ $L$: $(L, L+1), (L, L+2), \dots, (L, R)$.

* **Thao tác:** Cộng $(R - L)$ vào kết quả đếm, sau đó tăng $L \leftarrow L + 1$. Ngược lại, nếu $A_L + A_R > S$, giảm $R \leftarrow R - 1$.

#### Ví dụ minh họa 2: Đếm số cặp có tổng $\le 10$ trên mảng $A = [1, 2, 4, 7, 9]$

| Bước | Con trỏ $(L, R)$ | Tổng $A_L + A_R$ | Điều kiện $\le 10$ | Số cặp đếm được ($R - L$) | Hành động kế tiếp |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **1** | $(0, 4) \to (1, 9)$ | $1 + 9 = 10$ | $\le 10$ (Hợp lệ) | $+ (4 - 0) = \mathbf{4}$ cặp: $(1,2), (1,4), (1,7), (1,9)$ | Tăng $L \leftarrow 1$ |
| **2** | $(1, 4) \to (2, 9)$ | $2 + 9 = 11$ | $> 10$ (Vi phạm) | $+ 0$ cặp | Giảm $R \leftarrow 3$ |
| **3** | $(1, 3) \to (2, 7)$ | $2 + 7 = 9$ | $\le 10$ (Hợp lệ) | $+ (3 - 1) = \mathbf{2}$ cặp: $(2,4), (2,7)$ | Tăng $L \leftarrow 2$ |
| **4** | $(2, 3) \to (4, 7)$ | $4 + 7 = 11$ | $> 10$ (Vi phạm) | $+ 0$ cặp | Giảm $R \leftarrow 2$ |
| **Dừng** | $(2, 2)$ | — | $L \ge R$ | **Tổng số cặp thỏa mãn = $4 + 2 = \mathbf{6}$ cặp** | Kết thúc thuật toán |

### 3.3. Mô hình 3: Ghép cặp cực trị tham lam (bài toán thuyền cứu hộ / xe chở hàng)

* **Bài toán:** Mỗi xe chở tối đa 2 kiện hàng có tổng trọng lượng $\le C$. Tìm số xe ít nhất để chở hết $N$ kiện hàng.
* **Chiến lược:** Sắp xếp mảng trọng lượng tăng dần. Đặt $L = 0, R = N - 1$.
* Thử ghép kiện nặng nhất $A_R$ với kiện nhẹ nhất $A_L$.
* Nếu $A_L + A_R \le C$: Cả hai kiện đi chung xe $\implies L \leftarrow L + 1, R \leftarrow R - 1$.
* Nếu $A_L + A_R > C$: Kiện $A_R$ buộc phải đi xe riêng $\implies R \leftarrow R - 1$.

* Mỗi lần lặp tốn 1 xe (`++ans`).

### 3.4. Mô hình 4: Khử chiều đa biến (bài toán 3-sum và 4-sum)

* **Bài toán 3-Sum:** Tìm bộ ba $(i, j, k)$ có tổng $A_i + A_j + A_k = S$.
* **Chiến lược:** Sắp xếp mảng. Cố định phần tử thứ nhất $i$ từ $0$ đến $N - 3$, chuyển bài toán về tìm 2 số trong đoạn $[i+1 \dots N-1]$ có tổng bằng $S - A_i$ bằng Two Pointers.
* **Độ phức tạp:** Giảm từ $\mathcal{O}(N^3)$ xuống $\mathcal{O}(N^2)$.

## 4. Phân tích độ phức tạp thời gian & không gian

* **Thời gian (Time Complexity):**
* Bước sắp xếp: $\mathcal{O}(N \log N)$.
* Bước duyệt Hai con trỏ: $\mathcal{O}(N)$ (do tại mỗi phép so sánh, ít nhất một trong hai con trỏ di chuyển 1 bước, tổng số bước di chuyển tối đa là $N$).
* Tổng thời gian: $\mathcal{O}(N \log N + N) = \mathcal{O}(N \log N)$.
* **Không gian bộ nhớ (Space Complexity):**
* $\mathcal{O}(1)$ bộ nhớ phụ trợ khi xử lý trực tiếp trên mảng (in-place).

## 5. Mẫu cài đặt chuẩn thi đấu (competitive template)

```cpp
# include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long s;
    if (!(cin >> n >> s)) return 0;

    vector<long long> a(n);

    for (int i = 0; i < n; ++i) {
        cin >> a[i];

    }

    // Bước 1: Sắp xếp mảng tạo tính đơn điệu O(N log N)
    sort(a.begin(), a.end());

    // Bước 2: Khởi tạo Hai con trỏ đối đầu O(N)
    int l = 0, r = n - 1;
    bool found = false;

    while (l < r) {
        long long current_sum = a[l] + a[r];
        if (current_sum == s) {
            cout << a[l] << " " << a[r] << "\n";
            found = true;
            break;
        } else if (current_sum < s) {
            ++l; // Tổng nhỏ hơn mục tiêu -> tăng giá trị cận dưới

        } else {
            --r; // Tổng lớn hơn mục tiêu -> giảm giá trị cận trên

        }
    }

    if (!found) {
        cout << -1 << "\n";
    }

    return 0;
}
```

## 6. Các bẫy lỗi kỹ thuật thường gặp (bug traps)

1. **Bẫy điều kiện dừng `l <= r` thay vì `l < r`:** Khi $L = R$, phần tử $A_L$ tự cộng với chính nó ($2 \cdot A_L$), vi phạm yêu cầu chọn hai vị trí phân biệt ($i < j$).
2. **Bẫy tràn số nguyên 32-bit:** Khi các phần tử $A_i \approx 10^9$, tổng $A_L + A_R$ có thể đạt $2 \cdot 10^9$, suýt soát giới hạn kiểu `int` ($2^{31}-1$). Bắt buộc sử dụng `long long` cho biến tính tổng.
3. **Bẫy mảng chưa sắp xếp:** Áp dụng Hai con trỏ trên mảng chưa có trật tự đơn điệu sẽ dẫn đến sai lệch logic hoàn toàn.

## Bài tập thực hành


### Bài 01 [CPPB-HCT-01]: Mô Phỏng Hai Con Trỏ Đối Đầu

**Bối cảnh:** Cho mảng $N$ số nguyên đã sắp xếp tăng dần và một số nguyên $S$. Hãy kiểm tra xem trong mảng có tồn tại cặp chỉ số $(i, j)$ với $i < j$ sao cho $A_i + A_j = S$ hay không. Nếu có, in ra `YES`, ngược lại in ra `NO`.

**Đầu vào (Input):**

- Dòng 1: Chứa 2 số nguyên $N$ và $S$ ($2 \le N \le 10^5, -10^{18} \le S \le 10^{18}$).
- Dòng 2: Chứa $N$ số nguyên đã sắp xếp tăng dần $A_1 \le A_2 \le \dots \le A_N$ ($-10^9 \le A_i \le 10^9$).

**Đầu ra (Output):**

- In ra `YES` nếu tồn tại cặp số có tổng bằng $S$, ngược lại in ra `NO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 20 <br> 2 5 8 12 19 | YES |

**Ràng buộc & Giới hạn:**

- $40\%$ số test có $N \le 1000$.
- $60\%$ số test có $N \le 10^5$.



### Bài 02 [CPPB-HCT-02]: Cặp Số Có Tổng Bằng S (Two Sum)

**Bối cảnh:** Cho một mảng gồm $N$ số nguyên và một số nguyên $S$. Hãy tìm hai phần tử ở hai vị trí khác nhau trong mảng có tổng đúng bằng $S$. Nếu có nhiều cặp thỏa mãn, in ra một cặp bất kỳ theo thứ tự tăng dần. Nếu không tồn tại, in ra `-1`.

**Đầu vào (Input):**

- Dòng 1: Chứa 2 số nguyên $N$ và $S$ ($2 \le N \le 10^5, -10^{18} \le S \le 10^{18}$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

**Đầu ra (Output):**

- In ra 2 số nguyên là giá trị của 2 phần tử tìm được theo thứ tự tăng dần, hoặc `-1` nếu không có nghiệm.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 20 <br> 19 2 8 12 5 | 8 12 |

**Ràng buộc & Giới hạn:**

- $40\%$ số test có $N \le 1000$.
- $60\%$ số test có $N \le 10^5$.



### Bài 03 [CPPB-HCT-03]: Đếm Cặp Có Tổng Không Quá S

**Bối cảnh:** Cho mảng gồm $N$ số nguyên và một số nguyên $S$. Hãy đếm số lượng cặp chỉ số $(i, j)$ với $1 \le i < j \le N$ thỏa mãn:
$$A_i + A_j \le S$$

**Đầu vào (Input):**

- Dòng 1: Chứa 2 số nguyên $N$ và $S$ ($2 \le N \le 2 \cdot 10^5, -10^{18} \le S \le 10^{18}$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là số lượng cặp thỏa mãn.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 8 <br> 2 5 1 4 3 | 9 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 2 \cdot 10^5$.



### Bài 04 [CPPB-HCT-04]: Đếm Cặp Có Tổng Lớn Hơn Hoặc Bằng S

**Bối cảnh:** Cho mảng gồm $N$ số nguyên và một số nguyên $S$. Hãy đếm số lượng cặp chỉ số $(i, j)$ với $1 \le i < j \le N$ thỏa mãn:
$$A_i + A_j \ge S$$

**Đầu vào (Input):**

- Dòng 1: Chứa 2 số nguyên $N$ và $S$ ($2 \le N \le 2 \cdot 10^5, -10^{18} \le S \le 10^{18}$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là số lượng cặp thỏa mãn.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 8 <br> 2 5 1 4 3 | 2 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 2 \cdot 10^5$.



### Bài 05 [CPPB-HCT-05]: Ghép Thuyền Cứu Hộ Tối Ưu

**Bối cảnh:** Có $N$ người cần qua sông bằng thuyền cứu hộ. Mỗi người thứ $i$ có cân nặng $W_i$. Mỗi chiếc thuyền chở tối đa **2 người** và tổng cân nặng không vượt quá $C$. Hãy tìm số thuyền ít nhất.

**Đầu vào (Input):**

- Dòng 1: 2 số nguyên $N$ và $C$ ($1 \le N \le 10^5, 1 \le C \le 10^9$).
- Dòng 2: $N$ số nguyên $W_1, W_2, \dots, W_N$ ($1 \le W_i \le C$).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là số thuyền ít nhất cần dùng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 50 <br> 30 20 40 50 | 3 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 10^5, C \le 10^9$.



### Bài 06 [CPPB-HCT-06]: Vận Chuyển Thùng Hàng Cực Đại

**Bối cảnh:** Một đội xe chuyên dụng cần chở $N$ kiện hàng $W_1, W_2, \dots, W_N$ ($W_i \le 10^{12}$) ra bến cảng. Mỗi xe chở tối đa **2 kiện hàng** và tổng khối lượng không vượt quá tải trọng $C$ ($C \le 10^{12}$). Hãy tính số chuyến xe tối thiểu.

**Đầu vào (Input):**

- Dòng 1: 2 số nguyên dương $N$ và $C$ ($1 \le N \le 10^5, 1 \le C \le 10^{12}$).
- Dòng 2: $N$ số nguyên dương $W_1, W_2, \dots, W_N$ ($1 \le W_i \le C$).

**Đầu ra (Output):**

- In ra số chuyến xe ít nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 10 <br> 3 5 8 2 7 | 3 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 10^5, C \le 10^{12}$.



### Bài 07 [CPPB-HCT-07]: Tìm Cặp Có Tổng Gần S Nhất

**Bối cảnh:** Cho mảng gồm $N$ số nguyên và một số nguyên $S$. Hãy tìm một cặp số $(A_i, A_j)$ với $i < j$ sao cho tổng $A_i + A_j$ có độ chênh lệch $|(A_i + A_j) - S|$ là nhỏ nhất có thể. Nếu có nhiều cặp, in ra cặp có tổng nhỏ hơn.

**Đầu vào (Input):**

- Dòng 1: Chứa 2 số nguyên $N$ và $S$ ($2 \le N \le 10^5, -10^{18} \le S \le 10^{18}$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

**Đầu ra (Output):**

- In ra 2 số nguyên biểu diễn cặp số tìm được theo thứ tự tăng dần.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 20 <br> 2 8 13 4 25 | 8 13 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 10^5$.



### Bài 08 [CPPB-HCT-08]: Tìm Cặp Có Hiệu Đúng Bằng K

**Bối cảnh:** Cho mảng gồm $N$ số nguyên và số nguyên không âm $K$. Hãy kiểm tra xem có tồn tại cặp chỉ số $(i, j)$ với $i \neq j$ sao cho $A_j - A_i = K$ hay không. Nếu có in ra `YES`, ngược lại in ra `NO`.

**Đầu vào (Input):**

- Dòng 1: Chứa 2 số nguyên $N$ và $K$ ($2 \le N \le 10^5, 0 \le K \le 10^{18}$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

**Đầu ra (Output):**

- In ra `YES` hoặc `NO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 3 <br> 1 8 5 3 2 | YES |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 10^5$.



### Bài 09 [CPPB-HCT-09]: Bộ Ba Số Có Tổng Bằng S (3-Sum)

**Bối cảnh:** Cho mảng gồm $N$ số nguyên và một số nguyên $S$. Hãy tìm 3 phần tử ở 3 vị trí phân biệt trong mảng có tổng đúng bằng $S$. Nếu có nhiều bộ, in ra một bộ bất kỳ theo thứ tự tăng dần. Nếu không tồn tại, in ra `-1`.

**Đầu vào (Input):**

- Dòng 1: Chứa 2 số nguyên $N$ và $S$ ($3 \le N \le 3000, -10^{18} \le S \le 10^{18}$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

**Đầu ra (Output):**

- In ra 3 số nguyên theo thứ tự tăng dần, hoặc `-1`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 6 15 <br> 2 7 5 1 8 4 | 2 5 8 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 3000$.



### Bài 10 [CPPB-HCT-10]: Đếm Số Tam Giác Có Thể Tạo Thành

**Bối cảnh:** Cho $N$ đoạn que với độ dài $A_1, A_2, \dots, A_N$. Hãy đếm số lượng bộ 3 que có thể ghép lại thành một tam giác không suy biến (tổng 2 cạnh bất kỳ lớn hơn cạnh còn lại).

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $N$ ($3 \le N \le 3000$).
- Dòng 2: $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là số lượng tam giác tạo được.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 <br> 4 6 3 7 | 3 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 3000, 1 \le A_i \le 10^9$.



### Bài 11 [CPPB-HCT-11]: Đếm Cặp Tổng S Trên Mảng Trùng Lặp

**Bối cảnh:** Cho mảng gồm $N$ số nguyên có thể chứa nhiều phần tử trùng lặp và số nguyên $S$. Hãy đếm số lượng cặp chỉ số $(i, j)$ với $1 \le i < j \le N$ sao cho $A_i + A_j = S$.

**Đầu vào (Input):**

- Dòng 1: 2 số nguyên $N$ và $S$ ($2 \le N \le 2 \cdot 10^5, -10^{18} \le S \le 10^{18}$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là số lượng cặp chỉ số thỏa mãn.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 6 6 <br> 3 3 3 3 3 3 | 15 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 2 \cdot 10^5$.



### Bài 12 [CPPB-HCT-12]: Ghép Cặp Trẻ Em Và Bánh Quy

**Bối cảnh:** Có $N$ đứa trẻ và $M$ chiếc bánh quy. Đứa trẻ thứ $i$ có mức độ thèm ăn $G_i$ (chỉ hài lòng nếu nhận được bánh có kích thước $\ge G_i$). Chiếc bánh thứ $j$ có kích thước $S_j$. Mỗi đứa trẻ nhận tối đa 1 bánh và mỗi bánh chỉ phát cho 1 trẻ. Hãy tính số lượng đứa trẻ tối đa có thể được thỏa mãn.

**Đầu vào (Input):**

- Dòng 1: 2 số nguyên $N$ và $M$ ($1 \le N, M \le 10^5$).
- Dòng 2: $N$ số nguyên $G_1, G_2, \dots, G_N$ ($1 \le G_i \le 10^9$).
- Dòng 3: $M$ số nguyên $S_1, S_2, \dots, S_M$ ($1 \le S_j \le 10^9$).

**Đầu ra (Output):**

- In ra số lượng đứa trẻ tối đa được thỏa mãn.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 2 <br> 1 2 3 <br> 1 1 | 1 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N, M \le 10^5$.



### Bài 13 [CPPB-HCT-13]: Bộ Bốn Số Có Tổng Bằng S (4-Sum)

**Bối cảnh:** Cho mảng gồm $N$ số nguyên và số nguyên $S$. Hãy tìm 4 phần tử ở 4 vị trí phân biệt có tổng đúng bằng $S$. Nếu có nhiều bộ, in ra một bộ theo thứ tự tăng dần. Nếu không tồn tại, in ra `-1`.

**Đầu vào (Input):**

- Dòng 1: 2 số nguyên $N$ và $S$ ($4 \le N \le 1000, -10^{18} \le S \le 10^{18}$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

**Đầu ra (Output):**

- In ra 4 số nguyên tăng dần hoặc `-1`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 6 20 <br> 2 7 5 1 8 4 | 1 4 7 8 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 1000$.



### Bài 14 [CPPB-HCT-14]: Cặp Số Tối Ưu Với Chênh Lệch Cực Hạn

**Bối cảnh:** Cho 2 dãy số nguyên $A$ gồm $N$ phần tử và $B$ gồm $M$ phần tử. Hãy tìm một phần tử $A_i$ và một phần tử $B_j$ sao cho độ chênh lệch $|A_i - B_j|$ là nhỏ nhất có thể.

**Đầu vào (Input):**

- Dòng 1: 2 số nguyên $N$ và $M$ ($1 \le N, M \le 2 \cdot 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^{18} \le A_i \le 10^{18}$).
- Dòng 3: $M$ số nguyên $B_1, B_2, \dots, B_M$ ($-10^{18} \le B_j \le 10^{18}$).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là giá trị chênh lệch nhỏ nhất $|A_i - B_j|$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 3 <br> 1 5 10 <br> 2 8 14 | 1 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N, M \le 2 \cdot 10^5$.




# Bài 03: Kỹ thuật cửa sổ trượt


## 1. Khái niệm & bản chất của kỹ thuật cửa sổ trượt

**Kỹ thuật Cửa sổ trượt (Sliding Window Technique)** là phương pháp tối ưu hóa trên cấu trúc dữ liệu mảng hoặc chuỗi nhằm giải quyết các bài toán liên quan đến **đoạn con liên tiếp (Contiguous Subarray / Substring)**.

Thay vì phải tính toán lại từ đầu hàm mục tiêu trên từng đoạn con $[i \dots j]$ với độ phức tạp $\mathcal{O}(K)$ hoặc $\mathcal{O}(N)$, kỹ thuật này duy trì một "khung cửa sổ" $[L \dots R]$ và cập nhật trạng thái mục tiêu trong **$\mathcal{O}(1)$ thời gian** bằng cách:
$$\text{State}_{\text{mới}} = \text{State}_{\text{cũ}} + \text{Phần tử nạp vào } A_R - \text{Phần tử nhả ra } A_{L-1}$$

## 2. Cơ chế chuyển dịch & phân tích độ phức tạp $\mathcal{O}(N)$

### 2.1. Cơ chế hai con trỏ cùng chiều ($L \longrightarrow R$)

* **Con trỏ phải $R$ (Right / Lead pointer):** Mở rộng biên phải để nạp thêm phần tử $A_R$ vào cửa sổ nhằm thỏa mãn điều kiện bài toán.
* **Con trỏ trái $L$ (Left / Trail pointer):** Co hẹp biên trái để loại bỏ phần tử $A_L$ ra khỏi cửa sổ nhằm tối ưu hóa kích thước hoặc khôi phục tính hợp lệ của cửa sổ.

### 2.2. Phân tích chi phí khấu hao (amortized complexity analysis)
Mặc dù thuật toán thường được cài đặt dưới dạng một vòng lặp `while` lồng bên trong một vòng lặp `for`:

* Con trỏ $R$ duyệt từ $0$ đến $N - 1$ (thực hiện đúng $N$ bước tăng).
* Con trỏ $L$ duyệt từ $0$ đến $N$ (thực hiện tối đa $N$ bước tăng).
* **Mỗi phần tử trong mảng chỉ đi vào cửa sổ đúng 1 lần và ra khỏi cửa sổ tối đa 1 lần**.

Do đó, tổng số thao tác thêm/bớt phần tử trong toàn bộ chương trình không bao giờ vượt quá $2N$. Độ phức tạp thời gian đạt **$\mathcal{O}(N)$ tuyến tính tuyệt đối**.

## 3. Phân loại hai dạng cửa sổ trượt chuẩn mực

### 3.1. Dạng 1: Cửa sổ cố định độ dài $K$ (fixed-size window)
Áp dụng cho các bài toán yêu cầu khảo sát mọi đoạn con liên tiếp có độ dài đúng bằng $K$.

* **Công thức trượt $\mathcal{O}(1)$:**
* Khởi tạo: $\text{Current\_Sum} = \sum_{i=0}^{K-1} A_i$.
* Trượt từ vị trí $i = K$ đến $N - 1$:
$$\text{Current\_Sum} \leftarrow \text{Current\_Sum} + A_i - A_{i-K}$$

* Cập nhật giá trị cực trị: $\text{Ans} = \max(\text{Ans}, \text{Current\_Sum})$.

#### Ví dụ minh họa 1: Tìm tổng đoạn con $K = 3$ lớn nhất trên dãy $A = [2, 1, 5, 1, 3, 2]$

| Phần tử | $A[0]$ | $A[1]$ | $A[2]$ | $A[3]$ | $A[4]$ | $A[5]$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Giá trị** | $\mathbf{2}$ | $\mathbf{1}$ | $\mathbf{5}$ | $\mathbf{1}$ | $\mathbf{3}$ | $\mathbf{2}$ |

**Bảng mô phỏng quá trình trượt cửa sổ:**

| Vị trí $i$ | Đoạn cửa sổ | Thao tác nạp / loại | Tổng mới ($\text{Sum}$) | $\text{Max\_Sum}$ |
| :---: | :---: | :---: | :---: | :---: |
| **Khởi tạo ($i=2$)** | $[2, 1, 5]$ (đoạn $0..2$) | Tính tổng $3$ phần tử đầu | $2 + 1 + 5 = \mathbf{8}$ | $\mathbf{8}$ |
| **$i = 3$** | $[1, 5, 1]$ (đoạn $1..3$) | $+ A_3(1) - A_0(2)$ | $8 + 1 - 2 = \mathbf{7}$ | $8$ |
| **$i = 4$** | $[5, 1, 3]$ (đoạn $2..4$) | $+ A_4(3) - A_1(1)$ | $7 + 3 - 1 = \mathbf{9}$ | $\mathbf{9}$ |
| **$i = 5$** | $[1, 3, 2]$ (đoạn $3..5$) | $+ A_5(2) - A_2(5)$ | $9 + 2 - 5 = \mathbf{6}$ | $9$ |

$$\implies \text{Kết quả: Tổng lớn nhất của đoạn dài 3 là } \mathbf{9} \text{ (đoạn } [5, 1, 3]\text{), trượt trong đúng } \mathcal{O}(1) \text{ mỗi bước!}$$

### 3.2. Dạng 2: Cửa sổ biến thiên (variable-size window)
Áp dụng cho các bài toán tìm đoạn con liên tiếp dài nhất/ngắn nhất hoặc đếm số lượng đoạn con thỏa mãn điều kiện $f([L \dots R])$.

| Dạng Bài Toán | Chiến Lược Điều Khiển Con Trỏ | Công Thức Cập Nhật Kết Quả |
|---|---|---|
| **Đoạn con ngắn nhất có tổng $\ge S$** | Mở $R$ cho đến khi $\text{Sum} \ge S$, sau đó co $L$ tối đa để tìm $\min(R - L + 1)$ | $\text{Min\_Len} = \min(\text{Min\_Len}, R - L + 1)$ |
| **Đoạn con dài nhất có tổng $\le S$** | Mở $R$, nếu $\text{Sum} > S$ thì co $L$ cho đến khi $\text{Sum} \le S$ | $\text{Max\_Len} = \max(\text{Max\_Len}, R - L + 1)$ |
| **Đếm số lượng đoạn con có tổng $\le S$** | Mở $R$, co $L$ cho đến khi $\text{Sum} \le S$. Mọi đoạn con kết thúc tại $R$ bắt đầu từ $[L \dots R]$ đều thỏa mãn | $\text{Total} \leftarrow \text{Total} + (R - L + 1)$ |

#### Ví dụ minh họa 2: Tìm đoạn con ngắn nhất có tổng $\ge S = 7$ trên $A = [2, 3, 1, 2, 4, 3]$

| Bước ($R$) | Nạp $A_R$ | Tổng cửa sổ | Đánh giá $\ge 7$ | Thao tác co $L$ & Độ dài tìm được | $\text{Min\_Len}$ |
| :---: | :---: | :---: | :---: | :--- | :---: |
| $R = 0$ | $A_0 = 2$ | $2$ | Chưa đủ | — | $\infty$ |
| $R = 1$ | $A_1 = 3$ | $5$ | Chưa đủ | — | $\infty$ |
| $R = 2$ | $A_2 = 1$ | $6$ | Chưa đủ | — | $\infty$ |
| $R = 3$ | $A_3 = 2$ | $8$ | $\ge 7$ (Thỏa mãn) | Co $L=0 \to 1$ (bỏ $A_0=2$, tổng còn $6 < 7$) $\implies$ Đoạn $[3, 1, 2]$ dài $3$ | **$3$** |
| $R = 4$ | $A_4 = 4$ | $10$ | $\ge 7$ (Thỏa mãn) | Co $L=1 \to 3$ (bỏ $A_1, A_2$, tổng còn $6 < 7$) $\implies$ Đoạn $[2, 4]$ dài $2$ | **$2$** |
| $R = 5$ | $A_5 = 3$ | $9$ | $\ge 7$ (Thỏa mãn) | Co $L=3 \to 5$ (bỏ $A_3, A_4$, tổng còn $3 < 7$) $\implies$ Đoạn $[4, 3]$ dài $2$ | **$2$** |

$$\implies \text{Kết quả: Độ dài ngắn nhất là } \mathbf{2} \text{ (đoạn } [2, 4] \text{ hoặc } [4, 3]\text{)!}$$

## 4. Điều kiện áp dụng & giới hạn thất bại khi mảng có số âm

### 4.1. Điều kiện tiên quyết: Tính đơn điệu của hàm trạng thái
Cửa sổ trượt biến thiên **bắt buộc yêu cầu hàm mục tiêu phải có tính đơn điệu**:

* Khi mở rộng $R$ ($R \to R + 1$): Trạng thái phải tăng dần (hoặc không giảm).
* Khi co hẹp $L$ ($L \to L + 1$): Trạng thái phải giảm dần (hoặc không tăng).

Đối với bài toán tổng đoạn con, điều này tương đương với điều kiện: **Tất cả các phần tử trong mảng phải là số không âm ($A_i \ge 0$)**.

### 4.2. Giới hạn: Vì sao Sliding Window thất bại khi có số âm?
Xét mảng $A = [2, -5, 10, -2, 8]$ với mục tiêu tìm đoạn con ngắn nhất có tổng $\ge 8$.

* Khi $R$ nạp thêm số âm $-5$, tổng cửa sổ bị giảm.
* Khi $L$ dịch qua số âm $-5$, tổng cửa sổ lại tăng lên.
* Tính chất đơn điệu bị phá vỡ $\implies$ Con trỏ $L$ không thể đưa ra quyết định di chuyển một chiều chắc chắn $\implies$ Bỏ sót nghiệm tối ưu.
* **Giải pháp chuẩn:** Chuyển sang sử dụng **Mảng cộng dồn (Prefix Sum)** kết hợp **Hàng đợi hai đầu (Deque) / Cây chỉ số Fenwick / Segment Tree**.

## 5. Mẫu cài đặt chuẩn thi đấu (competitive template)

### Mẫu: Đoạn con liên tiếp ngắn nhất có tổng $\ge S$ ($A_i \ge 0$)

```cpp
# include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long s;
    if (!(cin >> n >> s)) return 0;

    vector<long long> a(n);

    for (int i = 0; i < n; ++i) {
        cin >> a[i];

    }

    int l = 0;
    long long current_sum = 0;
    int min_len = n + 1; // Khởi tạo vô cực

    // Duyệt con trỏ R tuyến tính O(N)
    for (int r = 0; r < n; ++r) {
        current_sum += a[r]; // Nạp a[r] vào cửa sổ

        // Co hẹp con trỏ L khi cửa sổ đã thỏa mãn điều kiện
        while (current_sum >= s) {
            min_len = min(min_len, r - l + 1); // Cập nhật độ dài nhỏ nhất
            current_sum -= a[l];               // Nhả a[l] ra khỏi cửa sổ
            ++l;                               // Dịch chuyển biên trái
        }
    }

    if (min_len > n) {

        cout << 0 << "\n"; // Không tồn tại đoạn thỏa mãn
    } else {
        cout << min_len << "\n";
    }

    return 0;
}
```

## 6. Kỹ thuật cửa sổ trượt với bảng đếm ký tự / trạng thái

Khi xử lý bài toán chuỗi ký tự (như Đoạn con dài nhất chứa tối đa $K$ ký tự khác nhau):

* Sử dụng mảng đếm tần suất `int count[256]` hoặc `int count[26]` và biến `distinct_count` lưu số ký tự khác nhau hiện có trong cửa sổ.
* Khi nạp ký tự $S[R]$: nếu `count[S[R]] == 0`, tăng `distinct_count`. Tăng `count[S[R]]++`.
* Khi `distinct_count > K`: co con trỏ $L$, giảm `count[S[L]]--`; nếu `count[S[L]] == 0`, giảm `distinct_count`. Tăng `++L`.

## 7. Các bẫy lỗi thường gặp (bug traps)

1. **Bẫy tràn số nguyên khi tính tổng cửa sổ:** Tổng đoạn con của mảng $N = 10^5$ phần tử với $A_i = 10^9$ có thể lên tới $10^{14}$. Khai báo biến `current_sum` kiểu `long long`.
2. **Bẫy điều kiện khởi tạo kết quả cực trị:** Khi tìm $\min$, khởi tạo `ans = n + 1` (hoặc $\infty$); khi không tìm thấy nghiệm phải in ra `0` hoặc `-1` theo đúng quy cách đề bài.
3. **Bẫy chỉ số âm khi trượt cửa sổ cố định:** Luôn đảm bảo chỉ thực hiện phép trừ `a[i - k]` khi chỉ số $i \ge K$.

## Bài tập thực hành


### Bài 01 [CPPB-CST-01]: Tổng Cửa Sổ Cố Định K

**Bối cảnh:** Cho một dãy gồm $N$ số nguyên $A_1, A_2, \dots, A_N$ và một số nguyên dương $K$ ($K \le N$). Hãy tìm tổng lớn nhất của một đoạn con gồm đúng $K$ phần tử liên tiếp.

**Đầu vào (Input):**

- Dòng 1: Chứa 2 số nguyên $N$ và $K$ ($1 \le K \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là tổng lớn nhất của đoạn $K$ phần tử liên tiếp.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 6 3 <br> 2 1 5 1 3 2 | 9 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 10^5$.



### Bài 02 [CPPB-CST-02]: Giá Trị Trung Bình Lớn Nhất Của Đoạn K

**Bối cảnh:** Cho một dãy gồm $N$ số nguyên $A_1, A_2, \dots, A_N$ và số nguyên $K$ ($K \le N$). Hãy tìm giá trị trung bình cộng lớn nhất của một đoạn con gồm $K$ phần tử liên tiếp.

**Đầu vào (Input):**

- Dòng 1: Chứa 2 số nguyên $N$ và $K$ ($1 \le K \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

**Đầu ra (Output):**

- In ra một số thực duy nhất là giá trị trung bình lớn nhất, làm tròn đúng 3 chữ số thập phân sau dấu phẩy.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 2 <br> 1 12 -5 6 | 6.500 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 10^5$.



### Bài 03 [CPPB-CST-03]: Đoạn Con Ngắn Nhất Có Tổng Đạt S

**Bối cảnh:** Cho dãy gồm $N$ số nguyên **không âm** $A_1, A_2, \dots, A_N$ và một số nguyên dương $S$. Hãy tìm độ dài nhỏ nhất của một đoạn con liên tiếp có tổng các phần tử $\ge S$. Nếu không có đoạn con nào thỏa mãn, in ra `-1`.

**Đầu vào (Input):**

- Dòng 1: Chứa 2 số nguyên $N$ và $S$ ($1 \le N \le 10^5, 1 \le S \le 10^{14}$).
- Dòng 2: $N$ số nguyên không âm $A_1, A_2, \dots, A_N$ ($0 \le A_i \le 10^9$).

**Đầu ra (Output):**

- In ra độ dài ngắn nhất hoặc `-1`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 6 7 <br> 2 3 1 2 4 3 | 2 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 10^5$.



### Bài 04 [CPPB-CST-04]: Đoạn Con Dài Nhất Có Tổng Không Quá S

**Bối cảnh:** Cho dãy gồm $N$ số nguyên **không âm** $A_1, A_2, \dots, A_N$ và một số nguyên dương $S$. Hãy tìm độ dài lớn nhất của một đoạn con liên tiếp có tổng các phần tử $\le S$.

**Đầu vào (Input):**

- Dòng 1: Chứa 2 số nguyên $N$ và $S$ ($1 \le N \le 2 \cdot 10^5, 1 \le S \le 10^{14}$).
- Dòng 2: $N$ số nguyên không âm $A_1, A_2, \dots, A_N$ ($0 \le A_i \le 10^9$).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là độ dài lớn nhất của đoạn con thỏa mãn.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 7 <br> 3 1 2 1 4 | 4 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 2 \cdot 10^5$.



### Bài 05 [CPPB-CST-05]: Đoạn Con Chứa Tối Đa K Số 0 (Lật Bit)

**Bối cảnh:** Cho một mảng nhị phân $A$ gồm $N$ phần tử ($A_i \in \{0, 1\}$) và số nguyên không âm $K$. Bạn được phép đổi tối đa $K$ số 0 thành số 1. Hãy tìm độ dài lớn nhất của dãy số 1 liên tiếp có thể tạo được.

**Đầu vào (Input):**

- Dòng 1: Chứa 2 số nguyên $N$ và $K$ ($1 \le N \le 10^5, 0 \le K \le N$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($A_i \in \{0, 1\}$).

**Đầu ra (Output):**

- In ra độ dài lớn nhất tìm được.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 1 <br> 1 0 1 1 0 | 4 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 10^5, K \le N$.



### Bài 06 [CPPB-CST-06]: Giám Sát Camera Giao Thông Thông Minh

**Bối cảnh:** Trên tuyến đường cao tốc có $N$ vị trí gắn camera. Trạng thái camera thứ $i$ được ghi nhận bởi $A_i$ ($A_i = 1$ là hoạt động tốt, $A_i = 0$ là bị hỏng). Trung tâm muốn chọn một đoạn liên tiếp gồm $K$ camera để kiểm tra định kỳ. Hãy tìm số lượng camera bị hỏng ít nhất trong bất kỳ đoạn $K$ camera liên tiếp nào.

**Đầu vào (Input):**

- Dòng 1: Chứa 2 số nguyên $N$ và $K$ ($1 \le K \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($A_i \in \{0, 1\}$).

**Đầu ra (Output):**

- In ra số camera hỏng ít nhất trong mọi cửa sổ độ dài $K$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 7 3 <br> 1 0 1 1 0 0 1 | 1 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 10^5, K \le N$.



### Bài 07 [CPPB-CST-07]: Tìm Min Trong Mọi Cửa Sổ Độ Dài K

**Bối cảnh:** Cho mảng gồm $N$ số nguyên và số nguyên $K$. Với mỗi cửa sổ gồm $K$ phần tử liên tiếp từ trái sang phải, hãy tìm giá trị nhỏ nhất trong cửa sổ đó.

**Đầu vào (Input):**

- Dòng 1: Chứa 2 số nguyên $N$ và $K$ ($1 \le K \le N \le 10^4$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

**Đầu ra (Output):**

- In ra $N - K + 1$ số nguyên cách nhau bởi khoảng trắng là giá trị nhỏ nhất của các cửa sổ.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 6 3 <br> 4 2 12 3 5 1 | 2 2 3 1 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 10^4, K \le N$.



### Bài 08 [CPPB-CST-08]: Đếm Số Lượng Đoạn Con Có Tổng Không Quá S

**Bối cảnh:** Cho mảng gồm $N$ số nguyên **không âm** $A_1, A_2, \dots, A_N$ và số nguyên $S$. Hãy đếm số lượng đoạn con liên tiếp $[L, R]$ ($1 \le L \le R \le N$) có tổng các phần tử $\le S$.

**Đầu vào (Input):**

- Dòng 1: Chứa 2 số nguyên $N$ và $S$ ($1 \le N \le 2 \cdot 10^5, 0 \le S \le 10^{14}$).
- Dòng 2: $N$ số nguyên không âm $A_1, A_2, \dots, A_N$ ($0 \le A_i \le 10^9$).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là số lượng đoạn con thỏa mãn.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 5 <br> 1 3 2 1 | 7 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 2 \cdot 10^5$.



### Bài 09 [CPPB-CST-09]: Đếm Số Lượng Đoạn Con Có Tổng Đúng Bằng S

**Bối cảnh:** Cho mảng gồm $N$ số nguyên **dương** $A_1, A_2, \dots, A_N$ ($A_i > 0$) và số nguyên dương $S$. Hãy đếm số lượng đoạn con liên tiếp có tổng đúng bằng $S$.

**Đầu vào (Input):**

- Dòng 1: Chứa 2 số nguyên $N$ và $S$ ($1 \le N \le 2 \cdot 10^5, 1 \le S \le 10^{14}$).
- Dòng 2: $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là số lượng đoạn con có tổng bằng $S$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 7 <br> 2 4 1 2 7 | 3 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 2 \cdot 10^5, A_i > 0$.



### Bài 10 [CPPB-CST-10]: Đoạn Con Dài Nhất Chứa Tối Đa K Ký Tự Khác Nhau

**Bối cảnh:** Cho chuỗi ký tự $S$ gồm các chữ cái tiếng Anh in thường và số nguyên dương $K$. Hãy tìm độ dài của chuỗi con liên tiếp dài nhất chứa **không quá $K$ ký tự phân biệt**.

**Đầu vào (Input):**

- Dòng 1: Chứa 2 số nguyên $N$ và $K$ ($1 \le K \le 26, 1 \le N \le 10^5$).
- Dòng 2: Chuỗi ký tự $S$ có độ dài $N$.

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là độ dài lớn nhất tìm được.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 7 2 <br> ecebaaa | 4 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 10^5, K \le 26$.



### Bài 11 [CPPB-CST-11]: Đoạn Con Ngắn Nhất Chứa Đủ Mọi Ký Tự Của Tập Hợp

**Bối cảnh:** Cho chuỗi $S$ gồm các chữ cái in thường và chuỗi mẫu $T$ gồm $M$ ký tự phân biệt. Hãy tìm độ dài ngắn nhất của một chuỗi con liên tiếp trong $S$ chứa đầy đủ tất cả các ký tự có trong $T$. Nếu không tồn tại, in ra `-1`.

**Đầu vào (Input):**

- Dòng 1: Chứa 2 số nguyên $N$ và $M$ ($1 \le M \le 26, 1 \le N \le 10^5$).
- Dòng 2: Chuỗi $S$ có độ dài $N$.
- Dòng 3: Chuỗi $T$ có độ dài $M$ gồm các ký tự phân biệt.

**Đầu ra (Output):**

- In ra độ dài ngắn nhất tìm được hoặc `-1`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 8 3 <br> adobecod <br> abc | 6 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 10^5, M \le 26$.



### Bài 12 [CPPB-CST-12]: Phủ Sóng Trạm Phát Sóng Wifi Đô Thị

**Bối cảnh:** Dọc theo tuyến phố dài, có $N$ căn nhà tại tọa độ $X_1, X_2, \dots, X_N$ ($X_1 < X_2 < \dots < X_N$). Nhà mạng muốn lắp các bộ phát wifi, mỗi bộ có bán kính phủ sóng là $R$ (phủ được đoạn $[x - R, x + R]$, tức độ dài vùng phủ là $2R$). Hãy tìm số lượng bộ phát wifi ít nhất để phủ sóng toàn bộ $N$ căn nhà.

**Đầu vào (Input):**

- Dòng 1: Chứa 2 số nguyên $N$ và $R$ ($1 \le N \le 10^5, 0 \le R \le 10^9$).
- Dòng 2: $N$ số nguyên tăng dần $X_1, X_2, \dots, X_N$ ($0 \le X_i \le 10^{14}$).

**Đầu ra (Output):**

- In ra số bộ phát wifi ít nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 6 2 <br> 1 2 3 7 8 11 | 3 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 10^5$.



### Bài 13 [CPPB-CST-13]: Đoạn Con Có Độ Chênh Lệch Max - Min Không Quá K

**Bối cảnh:** Cho mảng gồm $N$ số nguyên và số nguyên không âm $K$. Hãy tìm độ dài của đoạn con liên tiếp dài nhất sao cho chênh lệch giữa phần tử lớn nhất và nhỏ nhất trong đoạn đó không vượt quá $K$ (tức $\max - \min \le K$).

**Đầu vào (Input):**

- Dòng 1: Chứa 2 số nguyên $N$ và $K$ ($1 \le N \le 5000, 0 \le K \le 10^9$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

**Đầu ra (Output):**

- In ra độ dài lớn nhất của đoạn con thỏa mãn.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 6 3 <br> 8 2 4 7 3 9 | 2 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 5000$.



### Bài 14 [CPPB-CST-14]: Tối Ưu Cửa Sổ Trượt Tuyến Tính Khi N = 2.10⁵

**Bối cảnh:** Cho mảng gồm $N$ số nguyên dương và số nguyên $S$. Hãy tìm số lượng đoạn con liên tiếp có tổng các phần tử **nằm trong đoạn $[A, B]$** (tức $A \le \text{tổng} \le B$).

**Đầu vào (Input):**

- Dòng 1: Chứa 3 số nguyên $N, A, B$ ($1 \le N \le 2 \cdot 10^5, 1 \le A \le B \le 10^{14}$).
- Dòng 2: $N$ số nguyên dương $X_1, X_2, \dots, X_N$ ($1 \le X_i \le 10^9$).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là số lượng đoạn con thỏa mãn.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 3 6 <br> 1 2 3 4 | 5 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 2 \cdot 10^5$.



# CHƯƠNG 02: MẢNG TIỀN TỐ & TÌM KIẾM NHỊ PHÂN


# Bài 04: Mảng tiền tố & mảng hiệu


## 1. Khái niệm & bản chất của mảng tiền tố (Prefix Sum 1D)

**Mảng tiền tố (Prefix Sum)** là một kỹ thuật tiền xử lý dữ liệu mảng ban đầu thành một mảng cộng dồn tích lũy, cho phép tính toán tổng của bất kỳ đoạn con liên tiếp $[L \dots R]$ nào chỉ trong **$\mathcal{O}(1)$ thời gian**, thay vì phải duyệt vòng lặp $\mathcal{O}(N)$.

### 1.1. Công thức xây dựng mảng tiền tố
Cho mảng số nguyên $A$ gồm $N$ phần tử. Quy ước đánh số chỉ số từ $1$ đến $N$ (**1-based indexing**):

* Khởi tạo: $P_0 = 0$.
* Công thức truy hồi với $i$ từ $1$ đến $N$:
$$P_i = P_{i-1} + A_i \quad \Longleftrightarrow \quad P_i = \sum_{k=1}^{i} A_k$$

### 1.2. Công thức truy vấn tổng đoạn con trong $\mathcal{O}(1)$
Tổng các phần tử trong đoạn từ chỉ số $L$ đến chỉ số $R$ ($1 \le L \le R \le N$) được tính bằng hiệu của hai giá trị tiền tố:
$$\text{Sum}(L, R) = \sum_{k=L}^{R} A_k = P_R - P_{L-1}$$

### 1.3. Chứng minh toán học
Theo định nghĩa:
$$P_R = A_1 + A_2 + \dots + A_{L-1} + A_L + \dots + A_R$$
$$P_{L-1} = A_1 + A_2 + \dots + A_{L-1}$$

Lấy hiệu hai vế:
$$P_R - P_{L-1} = (A_1 + \dots + A_{L-1} + A_L + \dots + A_R) - (A_1 + \dots + A_{L-1}) = A_L + A_{L+1} + \dots + A_R = \text{Sum}(L, R)$$

> **Bất biến toán học:** Phép trừ $P_R - P_{L-1}$ đã loại bỏ chính xác đoạn tiền tố thừa từ $1$ đến $L-1$, chỉ giữ lại trọn vẹn đoạn con $[L \dots R]$ cần tính.

#### Ví dụ minh họa 1: Xây dựng và truy vấn Prefix Sum 1D
Cho mảng $N = 6$ phần tử: $A = [3, 1, 4, 1, 5, 9]$ (1-based indexing).

| Chỉ số $i$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Mảng gốc $A[i]$** | — | $3$ | $1$ | $4$ | $1$ | $5$ | $9$ |
| **Tiền tố $P[i]$** | $\mathbf{0}$ | $\mathbf{3}$ | $\mathbf{4}$ | $\mathbf{8}$ | $\mathbf{9}$ | $\mathbf{14}$ | $\mathbf{23}$ |

*Quy tắc cộng dồn:* $P[0] = 0$, $P[i] = P[i-1] + A[i]$ (ví dụ: $P[3] = 4 + 4 = 8, P[6] = 14 + 9 = 23$).

* **Truy vấn 1:** Tính tổng đoạn từ $L = 2$ đến $R = 5$ (đoạn $[1, 4, 1, 5]$):
$$\text{Sum}(2, 5) = P[5] - P[2 - 1] = P[5] - P[1] = 14 - 3 = \mathbf{11}$$
(Kiểm tra trực tiếp: $1 + 4 + 1 + 5 = 11$ — Hoàn toàn chính xác trong $\mathcal{O}(1)$).

* **Truy vấn 2:** Tính tổng toàn bộ mảng từ $L = 1$ đến $R = 6$:
$$\text{Sum}(1, 6) = P[6] - P[0] = 23 - 0 = \mathbf{23}$$

## 2. Kỹ thuật mảng tiền tố hai chiều (Prefix Sum 2D)

### 2.1. Bản chất nguyên lý bao hàm - Loại trừ (inclusion-exclusion principle)
Trên ma trận 2 chiều kích thước $N \times M$, gọi $P[i][j]$ là tổng của tất cả các phần tử trong hình chữ nhật có góc trái trên tại $(1, 1)$ và góc phải dưới tại $(i, j)$:
$$P[i][j] = \sum_{r=1}^{i} \sum_{c=1}^{j} A[r][c]$$

### 2.2. Công thức xây dựng bảng tiền tố 2D trong $\mathcal{O}(N \times M)$
Tại mỗi ô $(i, j)$:
$$P[i][j] = P[i-1][j] + P[i][j-1] - P[i-1][j-1] + A[i][j]$$
(Giải thích: Cộng vùng phía trên và vùng bên trái, trừ đi phần giao nhau bị cộng lặp $P[i-1][j-1]$, rồi cộng thêm giá trị ô hiện tại $A[i][j]$).

### 2.3. Công thức truy vấn tổng hình chữ nhật $(x_1, y_1) \to (x_2, y_2)$ trong $\mathcal{O}(1)$
$$\text{Sum}((x_1, y_1), (x_2, y_2)) = P[x_2][y_2] - P[x_1-1][y_2] - P[x_2][y_1-1] + P[x_1-1][y_1-1]$$

#### Ví dụ minh họa 2: Truy vấn hình chữ nhật trên ma trận $3 \times 3$
Cho ma trận $A$:
$$\begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix} \quad \xrightarrow{\text{Xây dựng } P} \quad P = \begin{bmatrix} 0 & 0 & 0 & 0 \\ 0 & 1 & 3 & 6 \\ 0 & 5 & 12 & 21 \\ 0 & 12 & 27 & 45 \end{bmatrix}$$

Cần tính tổng hình chữ nhật từ $(x_1=2, y_1=2)$ đến $(x_2=3, y_2=3)$ (vùng các ô $\begin{bmatrix} 5 & 6 \\ 8 & 9 \end{bmatrix}$):
$$\begin{aligned}
\text{Sum} &= P[3][3] - P[1][3] - P[3][1] + P[1][1] \\
&= 45 - 6 - 12 + 1 = \mathbf{28}
\end{aligned}$$
(Kiểm tra trực tiếp: $5 + 6 + 8 + 9 = 28$ — Tính toán trong đúng 4 phép toán $\mathcal{O}(1)$).

## 3. Kỹ thuật mảng hiệu (Difference Array 1D)

### 3.1. Bài toán đặt ra
Cho mảng ban đầu gồm $N$ phần tử (toàn số 0 hoặc có giá trị sẵn). Thực hiện $Q$ thao tác, mỗi thao tác yêu cầu: **Cộng thêm một giá trị $V$ vào tất cả các phần tử từ chỉ số $L$ đến $R$**. Sau $Q$ thao tác, in ra mảng kết quả cuối cùng.

* **Cách tiếp cận ngây thơ:** Với mỗi thao tác, dùng vòng lặp chạy từ $L$ đến $R$ để cộng. Tổng thời gian: $\mathcal{O}(Q \times N) \approx 10^5 \times 10^5 = 10^{10}$ phép tính $\implies$ **Time Limit Exceeded (TLE)**.
* **Tối ưu bằng Mảng hiệu:** Thực hiện mỗi thao tác cộng đoạn trong **$\mathcal{O}(1)$ thời gian**.

### 3.2. Cơ chế hoạt động của mảng hiệu
Xây dựng mảng hiệu $D$ thỏa mãn: $A_i = \sum_{k=1}^{i} D_k$ (Mảng ban đầu chính là mảng tiền tố của mảng hiệu).
Để cộng giá trị $V$ vào mọi phần tử trong đoạn $[L \dots R]$, ta chỉ cần thực hiện 2 thao tác điểm:

* **Tại điểm bắt đầu đoạn $L$:** $D[L] \mathrel{+}= V$
* **Tại điểm sau kết thúc đoạn $R + 1$:** $D[R + 1] \mathrel{-}= V$

### 3.3. Khôi phục mảng kết quả sau $Q$ thao tác
Sau khi hoàn thành tất cả $Q$ thao tác cập nhật $\mathcal{O}(1)$, ta khôi phục lại mảng kết quả $A$ bằng một lần chạy tiền tố duy nhất trong **$\mathcal{O}(N)$ thời gian**:
$$A_i = A_{i-1} + D_i \quad (i = 1 \dots N)$$

#### Ví dụ minh họa 3: Mảng hiệu trên dãy $N = 5$ phần tử
Ban đầu dãy toàn số 0: $A = [0, 0, 0, 0, 0]$, mảng hiệu $D = [0, 0, 0, 0, 0, 0, 0]$ (kích thước $N+2$).

1. **Thao tác 1:** Cộng $V = 3$ vào đoạn $[1 \dots 3] \implies D[1] += 3, D[4] -= 3$.
$$D = [0, \mathbf{+3}, 0, 0, \mathbf{-3}, 0, 0]$$

2. **Thao tác 2:** Cộng $V = 2$ vào đoạn $[2 \dots 5] \implies D[2] += 2, D[6] -= 2$.
$$D = [0, +3, \mathbf{+2}, 0, -3, 0, \mathbf{-2}]$$

**Bước khôi phục mảng kết quả $A$ bằng Prefix Sum trên $D$:**

* $A_1 = D_1 = 3$
* $A_2 = A_1 + D_2 = 3 + 2 = 5$
* $A_3 = A_2 + D_3 = 5 + 0 = 5$
* $A_4 = A_3 + D_4 = 5 + (-3) = 2$
* $A_5 = A_4 + D_5 = 2 + 0 = 2$

> **Kết quả cuối cùng:** $A = [3, 5, 5, 2, 2]$

## 4. Kỹ thuật mảng hiệu hai chiều (Difference Array 2D)

Để cộng thêm giá trị $V$ vào tất cả các ô trong hình chữ nhật từ $(x_1, y_1)$ đến $(x_2, y_2)$ trên ma trận $N \times M$, ta chỉ cần tác động lên **4 điểm góc** của mảng hiệu $2D$ trong $\mathcal{O}(1)$:

| Điểm Góc Tác Động | Tọa Độ Ô Mảng Hiệu | Thao Tác Cập Nhật $\mathcal{O}(1)$ |
|---|:---:|:---:|
| **Góc trên - trái** | $(x_1, y_1)$ | `D[x1][y1] += V` |
| **Góc trên - phải** | $(x_1, y_2 + 1)$ | `D[x1][y2 + 1] -= V` |
| **Góc dưới - trái** | $(x_2 + 1, y_1)$ | `D[x2 + 1][y1] -= V` |
| **Góc dưới - phải** | $(x_2 + 1, y_2 + 1)$ | `D[x2 + 1][y2 + 1] += V` |

Sau khi thực hiện xong $Q$ thao tác, khôi phục ma trận gốc bằng công thức Prefix Sum 2D trong $\mathcal{O}(N \times M)$.

## 5. Mẫu cài đặt chuẩn thi đấu (competitive template)

### Mẫu 1: Prefix Sum 1D (truy vấn tổng đoạn)

```cpp
# include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<long long> a(n + 1);

    vector<long long> p(n + 1, 0);

    // Bước 1: Đọc dữ liệu và xây dựng mảng tiền tố O(N)
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];

        p[i] = p[i - 1] + a[i];
    }

    // Bước 2: Trả lời từng truy vấn trong O(1)
    while (q--) {
        int l, r;
        cin >> l >> r;

        cout << p[r] - p[l - 1] << "\n";
    }

    return 0;
}
```

### Mẫu 2: Difference Array 1D (cập nhật đoạn)

```cpp
# include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    // Khởi tạo mảng hiệu kích thước n + 2 để an toàn khi truy cập r + 1
    vector<long long> d(n + 2, 0);

    // Bước 1: Tiếp nhận Q thao tác cập nhật O(1)
    while (q--) {
        int l, r;
        long long v;
        cin >> l >> r >> v;

        d[l] += v;
        d[r + 1] -= v;
    }

    // Bước 2: Khôi phục mảng kết quả bằng tiền tố O(N)
    vector<long long> a(n + 1, 0);

    for (int i = 1; i <= n; ++i) {
        a[i] = a[i - 1] + d[i];
        cout << a[i] << (i == n ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```

## 6. Các bẫy lỗi lập trình thường gặp (bug traps)

1. **Bẫy chỉ số 0-based vs 1-based:** Khi dùng chỉ số 0-based, truy vấn đoạn bắt đầu từ $L=0$ sẽ phải tính $P[R] - P[-1]$ dẫn đến lỗi truy cập vùng nhớ ngoài biên. **Khuyến nghị chuẩn:** Luôn chuyển toàn bộ mảng tiền tố và mảng hiệu sang **1-based indexing** với $P[0] = 0$.
2. **Bẫy tràn số nguyên 32-bit khi cộng dồn:** Mảng $N = 2 \cdot 10^5$ phần tử với $A_i = 10^9$ sẽ có tổng tiền tố lên tới $2 \cdot 10^{14}$, vượt ngưỡng $2 \cdot 10^9$ của `int`. Khai báo toàn bộ mảng $P$ và $D$ kiểu `long long`.
3. **Bẫy tràn biên $R + 1$ trong mảng hiệu:** Khi đoạn cập nhật có $R = N$, thao tác $D[R+1] -= V$ sẽ ghi vào vị trí $N + 1$. Bắt buộc phải cấp phát mảng hiệu có kích thước tối thiểu là `N + 2`.

## 7. Ranh giới áp dụng: Khi nào nên & không nên dùng?

* **KHI NÀO ÁP DỤNG TỐI ƯU:**
* **Mảng tĩnh (Static Queries):** Toàn bộ dữ liệu mảng cố định, chỉ nhận các truy vấn tính tổng đoạn liên tiếp $\implies$ **Prefix Sum đạt $\mathcal{O}(1)$ tuyệt đối**.
* **Cập nhật Offline (Batch Updates):** Nhận toàn bộ $Q$ thao tác cộng đoạn $[L, R]$ trước, sau đó mới cần in kết quả một lần ở cuối $\implies$ **Difference Array đạt $\mathcal{O}(Q + N)$**.

* **KHI NÀO KHÔNG ÁP DỤNG ĐƯỢC (Bẫy Lỗi KỸ THUẬT):**
* **Cập nhật và truy vấn xen kẽ Online:** Nếu chương trình vừa yêu cầu cập nhật giá trị một phần tử/đoạn, vừa yêu cầu truy vấn tổng đoạn ngay lập tức lặp đi lặp lại $Q$ lần:
* Dùng Prefix Sum sẽ tốn $\mathcal{O}(N)$ để cập nhật lại mảng $P \implies$ Tổng thời gian $\mathcal{O}(Q \times N)$ (TLE).
* Dùng Difference Array sẽ tốn $\mathcal{O}(N)$ để khôi phục mỗi khi có truy vấn $\implies$ Tổng thời gian $\mathcal{O}(Q \times N)$ (TLE).
* **Giải pháp chuẩn thi đấu:** Khi có cập nhật và truy vấn xen kẽ liên tục, bắt buộc phải sử dụng các cấu trúc dữ liệu cây động như **Cây chỉ số nhị phân (Fenwick Tree)** hoặc **Cây phân đoạn (Segment Tree)** (thuộc Module 08).

## Bài tập thực hành


### Bài 01 [CPPB-PT-01]: Truy Vấn Tổng Đoạn Con 1D

**Bối cảnh:** Cho một dãy số nguyên gồm $N$ phần tử $A_1, A_2, \dots, A_N$. Bạn cần trả lời $Q$ câu hỏi, mỗi câu hỏi yêu cầu tính tổng các phần tử trong đoạn từ vị trí $L$ đến vị trí $R$.

**Nhiệm vụ:** Hãy sử dụng kỹ thuật mảng tiền tố (Prefix Sum) để trả lời tất cả $Q$ truy vấn trong thời gian tối ưu $\mathcal{O}(1)$ cho mỗi truy vấn.

**Đầu vào (Input):**

- Dòng 1: Gồm 2 số nguyên dương $N, Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: Gồm $N$ số nguyên $A_1, A_2, \dots, A_N$ ($|A_i| \le 10^9$).
- $Q$ dòng tiếp theo: Mỗi dòng gồm 2 số nguyên $L, R$ ($1 \le L \le R \le N$).

**Đầu ra (Output):**

- In ra $Q$ dòng, mỗi dòng là một số nguyên biểu diễn tổng đoạn $[L \dots R]$ tương ứng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 3 <br> 2 4 1 5 3 <br> 1 3 <br> 2 4 <br> 1 5 | 7 <br> 10 <br> 15 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N, Q \le 10^5, |A_i| \le 10^9$.



### Bài 02 [CPPB-PT-02]: Đếm Số Lượng Số Chẵn Trong Đoạn

**Bối cảnh:** Cho một dãy gồm $N$ số nguyên. Có $Q$ câu hỏi dạng $[L, R]$, yêu cầu đếm xem trong đoạn từ vị trí $L$ đến $R$ có bao nhiêu số chẵn.

**Đầu vào (Input):**

- Dòng 1: Gồm 2 số nguyên $N, Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: Gồm $N$ số nguyên $A_1, A_2, \dots, A_N$ ($|A_i| \le 10^9$).
- $Q$ dòng tiếp theo: Mỗi dòng gồm 2 số nguyên $L, R$ ($1 \le L \le R \le N$).

**Đầu ra (Output):**

- In ra $Q$ dòng, mỗi dòng là số lượng số chẵn trong đoạn $[L \dots R]$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 6 3 <br> 1 2 4 5 6 7 <br> 1 4 <br> 2 5 <br> 1 6 | 2 <br> 3 <br> 3 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N, Q \le 10^5, |A_i| \le 10^9$.



### Bài 03 [CPPB-PT-03]: Tìm Vị Trí Cân Bằng Của Mảng

**Bối cảnh:** Một vị trí $i$ ($1 \le i \le N$) trong dãy số $A$ được gọi là **vị trí cân bằng** nếu tổng các phần tử đứng trước nó bằng tổng các phần tử đứng sau nó:
$$\sum_{k=1}^{i-1} A_k = \sum_{k=i+1}^{N} A_k$$
(Quy ước nếu trước $i$ hoặc sau $i$ không có phần tử nào thì tổng tương ứng bằng $0$).

**Nhiệm vụ:** Tìm vị trí cân bằng đầu tiên (chỉ số nhỏ nhất). Nếu không có, in ra `-1`.

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 2 \cdot 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($|A_i| \le 10^9$).

**Đầu ra (Output):**

- In ra chỉ số cân bằng nhỏ nhất (1-based), hoặc `-1` nếu không tồn tại.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 7 <br> -7 1 5 2 -4 3 0 | 4 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 2 \cdot 10^5, |A_i| \le 10^9$.



### Bài 04 [CPPB-PT-04]: Đoạn Con Có Tổng Bằng 0

**Bối cảnh:** Cho mảng số nguyên gồm $N$ phần tử. Hãy kiểm tra xem có tồn tại ít nhất một đoạn con liên tiếp khác rỗng có tổng các phần tử bằng $0$ hay không.

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($|A_i| \le 10^9$).

**Đầu ra (Output):**

- In ra `YES` nếu tồn tại đoạn con có tổng bằng 0, ngược lại in ra `NO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 <br> 4 2 -3 1 6 | YES |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 10^5, |A_i| \le 10^9$.



### Bài 05 [CPPB-PT-05]: Cập Nhật Cộng Đoạn Tuyến Tính (Mảng Hiệu)

**Bối cảnh:** Cho một dãy gồm $N$ số nguyên ban đầu toàn số 0. Có $Q$ thao tác, mỗi thao tác gồm 3 số $L, R, V$ yêu cầu cộng thêm $V$ vào tất cả các phần tử từ chỉ số $L$ đến $R$.

**Nhiệm vụ:** Hãy in ra dãy số cuối cùng sau khi đã thực hiện xong toàn bộ $Q$ thao tác.

**Đầu vào (Input):**

- Dòng 1: Gồm 2 số nguyên $N, Q$ ($1 \le N, Q \le 2 \cdot 10^5$).
- $Q$ dòng tiếp theo: Mỗi dòng gồm 3 số nguyên $L, R, V$ ($1 \le L \le R \le N, |V| \le 10^9$).

**Đầu ra (Output):**

- In ra $N$ số nguyên trên một dòng biểu diễn mảng sau $Q$ thao tác, cách nhau bởi khoảng trắng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 3 <br> 1 3 2 <br> 2 5 3 <br> 3 4 -1 | 2 5 4 2 3 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N, Q \le 2 \cdot 10^5, |V| \le 10^9$.



### Bài 06 [CPPB-PT-06]: Trồng Cây Phủ Đoạn Tối Ưu

**Bối cảnh:** Dọc một con đường thẳng có $N$ vị trí trồng cây được đánh số từ $1$ đến $N$. Ban đầu, các vị trí đều chưa có cây (mức phủ bằng 0). Có $Q$ tình nguyện viên tham gia tưới nước, người thứ $i$ tưới cho đoạn từ vị trí $L_i$ đến $R_i$.

**Nhiệm vụ:** Hãy đếm xem sau khi tất cả $Q$ người tưới xong, có bao nhiêu vị trí được tưới **ít nhất $K$ lần**.

**Đầu vào (Input):**

- Dòng 1: Gồm 3 số nguyên $N, Q, K$ ($1 \le N, Q \le 10^5, 1 \le K \le Q$).
- $Q$ dòng tiếp theo: Mỗi dòng gồm 2 số nguyên $L_i, R_i$ ($1 \le L_i \le R_i \le N$).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là số lượng vị trí được tưới ít nhất $K$ lần.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 6 3 2 <br> 1 4 <br> 2 5 <br> 3 6 | 4 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N, Q \le 10^5$.



### Bài 07 [CPPB-PT-07]: Truy Vấn Tổng Hình Chữ Nhật 2D

**Bối cảnh:** Cho ma trận số nguyên $A$ kích thước $N \times M$. Hãy trả lời $Q$ truy vấn, mỗi truy vấn yêu cầu tính tổng các phần tử trong hình chữ nhật có góc trái trên tại $(x_1, y_1)$ và góc phải dưới tại $(x_2, y_2)$.

**Đầu vào (Input):**

- Dòng 1: Gồm 3 số nguyên $N, M, Q$ ($1 \le N, M \le 1000, 1 \le Q \le 10^5$).
- $N$ dòng tiếp theo: Mỗi dòng gồm $M$ số nguyên $A_{i, j}$ ($|A_{i, j}| \le 10^9$).
- $Q$ dòng tiếp theo: Mỗi dòng gồm 4 số nguyên $x_1, y_1, x_2, y_2$ ($1 \le x_1 \le x_2 \le N, 1 \le y_1 \le y_2 \le M$).

**Đầu ra (Output):**

- In ra $Q$ dòng, mỗi dòng là tổng hình chữ nhật tương ứng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 3 2 <br> 1 2 3 <br> 4 5 6 <br> 7 8 9 <br> 1 1 2 2 <br> 2 2 3 3 | 12 <br> 28 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N, M \le 1000, Q \le 10^5$.



### Bài 08 [CPPB-PT-08]: Tìm Hình Vuông K x K Có Tổng Lớn Nhất

**Bối cảnh:** Cho ma trận $A$ kích thước $N \times M$ và một số nguyên dương $K$ ($K \le \min(N, M)$). Hãy tìm hình vuông con kích thước $K \times K$ có tổng các phần tử lớn nhất.

**Đầu vào (Input):**

- Dòng 1: Gồm 3 số nguyên $N, M, K$ ($1 \le N, M \le 1000, 1 \le K \le \min(N, M)$).
- $N$ dòng tiếp theo: Mỗi dòng gồm $M$ số nguyên $A_{i, j}$ ($|A_{i, j}| \le 10^9$).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là tổng lớn nhất của hình vuông $K \times K$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 3 2 <br> 1 1 1 <br> 1 2 2 <br> 1 2 2 | 8 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N, M \le 1000, |A_{i,j}| \le 10^9$.



### Bài 09 [CPPB-PT-09]: Cập Nhật Cộng Hình Chữ Nhật (Mảng Hiệu 2D)

**Bối cảnh:** Cho ma trận kích thước $N \times M$ ban đầu toàn số 0. Có $Q$ thao tác, mỗi thao tác gồm 5 số nguyên $x_1, y_1, x_2, y_2, V$ yêu cầu cộng giá trị $V$ vào tất cả các ô trong hình chữ nhật từ $(x_1, y_1)$ đến $(x_2, y_2)$.

**Nhiệm vụ:** Hãy in ra ma trận kết quả sau khi hoàn thành $Q$ thao tác.

**Đầu vào (Input):**

- Dòng 1: Gồm 3 số nguyên $N, M, Q$ ($1 \le N, M \le 1000, 1 \le Q \le 10^5$).
- $Q$ dòng tiếp theo: Mỗi dòng gồm 5 số $x_1, y_1, x_2, y_2, V$ ($1 \le x_1 \le x_2 \le N, 1 \le y_1 \le y_2 \le M, |V| \le 10^9$).

**Đầu ra (Output):**

- In ra $N$ dòng, mỗi dòng gồm $M$ số nguyên biểu diễn ma trận cuối cùng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 3 2 <br> 1 1 2 2 3 <br> 2 2 3 3 2 | 3 3 0 <br> 3 5 2 <br> 0 2 2 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N, M \le 1000, Q \le 10^5$.



### Bài 10 [CPPB-PT-10]: Đoạn Con Có Tổng Chia Hết Cho K

**Bối cảnh:** Cho mảng số nguyên gồm $N$ phần tử và một số nguyên dương $K$. Hãy đếm số lượng đoạn con liên tiếp khác rỗng có tổng các phần tử chia hết cho $K$.

**Đầu vào (Input):**

- Dòng 1: Gồm 2 số nguyên $N, K$ ($1 \le N \le 2 \cdot 10^5, 1 \le K \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($|A_i| \le 10^9$).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là số lượng đoạn con có tổng chia hết cho $K$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 3 <br> 4 5 0 -2 -3 | 6 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 2 \cdot 10^5, K \le 10^5$.



### Bài 11 [CPPB-PT-11]: Mảng Tiền Tố XOR Đoạn Con

**Bối cảnh:** Cho dãy số nguyên gồm $N$ phần tử. Có $Q$ truy vấn, mỗi truy vấn yêu cầu tính tích XOR của các phần tử trong đoạn từ $L$ đến $R$:
$$\text{XOR}(L, R) = A_L \oplus A_{L+1} \oplus \dots \oplus A_R$$

**Đầu vào (Input):**

- Dòng 1: Gồm 2 số nguyên $N, Q$ ($1 \le N, Q \le 2 \cdot 10^5$).
- Dòng 2: $N$ số nguyên không âm $A_1, A_2, \dots, A_N$ ($0 \le A_i \le 10^9$).
- $Q$ dòng tiếp theo: Mỗi dòng gồm 2 số nguyên $L, R$ ($1 \le L \le R \le N$).

**Đầu ra (Output):**

- In ra $Q$ dòng kết quả tương ứng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 3 <br> 1 3 4 2 2 <br> 1 3 <br> 2 4 <br> 1 5 | 6 <br> 5 <br> 6 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N, Q \le 2 \cdot 10^5, 0 \le A_i \le 10^9$.



### Bài 12 [CPPB-PT-12]: Đoạn Con Cân Bằng Số Lượng 0 và 1

**Bối cảnh:** Cho một mảng nhị phân gồm $N$ phần tử chỉ chứa các số 0 và 1. Hãy tìm độ dài của đoạn con liên tiếp dài nhất chứa số lượng số 0 bằng đúng số lượng số 1.

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 2 \cdot 10^5$).
- Dòng 2: $N$ số nhị phân $A_1, A_2, \dots, A_N$ ($A_i \in \{0, 1\}$).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là độ dài lớn nhất tìm được. Nếu không có đoạn nào, in ra `0`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 6 <br> 0 1 0 0 1 1 | 6 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 2 \cdot 10^5$.



### Bài 13 [CPPB-PT-13]: Truy Vấn Ma Trận Đa Vùng Cực Đại

**Bối cảnh:** Cho một ma trận $N \times M$. Mỗi truy vấn cung cấp tọa độ hai hình chữ nhật rời nhau $R_1$ và $R_2$. Hãy tính tổng của tất cả các phần tử thuộc cả hai hình chữ nhật này.

**Đầu vào (Input):**

- Dòng 1: Gồm 3 số nguyên $N, M, Q$ ($1 \le N, M \le 1500, 1 \le Q \le 10^5$).
- $N$ dòng tiếp theo: Mỗi dòng gồm $M$ số nguyên $A_{i, j}$ ($|A_{i, j}| \le 10^9$).
- $Q$ dòng tiếp theo: Mỗi dòng gồm 8 số $x_1, y_1, x_2, y_2, u_1, v_1, u_2, v_2$ mô tả hình chữ nhật 1 và hình chữ nhật 2.

**Đầu ra (Output):**

- In ra $Q$ dòng kết quả.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 3 1 <br> 1 2 3 <br> 4 5 6 <br> 7 8 9 <br> 1 1 1 1 3 3 3 3 | 10 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N, M \le 1500, Q \le 10^5$.



### Bài 14 [CPPB-PT-14]: Phân Phối Tài Nguyên Không Gian Tuyến Tính

**Bối cảnh:** Cho dãy số $N$ phần tử ban đầu toàn số 0. Có $Q$ thao tác, mỗi thao tác cộng vào đoạn $[L \dots R]$ một cấp số cộng bắt đầu từ giá trị $S$ và tăng dần theo bước nhảy $D$ (tức vị trí $L$ cộng $S$, vị trí $L+1$ cộng $S+D$, ..., vị trí $R$ cộng $S + (R-L)D$).

**Nhiệm vụ:** Hãy in ra mảng kết quả cuối cùng sau khi hoàn thành $Q$ thao tác.

**Đầu vào (Input):**

- Dòng 1: Gồm 2 số nguyên $N, Q$ ($1 \le N, Q \le 2 \cdot 10^5$).
- $Q$ dòng tiếp theo: Mỗi dòng gồm 4 số nguyên $L, R, S, D$ ($1 \le L \le R \le N, |S|, |D| \le 10^4$).

**Đầu ra (Output):**

- In ra $N$ số nguyên trên một dòng biểu diễn mảng cuối cùng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 2 <br> 1 3 2 1 <br> 2 4 1 2 | 2 4 7 5 0 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N, Q \le 2 \cdot 10^5, |S|, |D| \le 10^4$.



### Bài 15 [CPPB-PT-15]: Tìm Ma Trận Con Có Tổng Lớn Nhất (Max Submatrix Sum)

**Bối cảnh:** Cho ma trận số nguyên $A$ kích thước $N \times M$. Hãy tìm một ma trận con chữ nhật bất kỳ có tổng các phần tử là **lớn nhất có thể**.

**Đầu vào (Input):**

- Dòng 1: Gồm 2 số nguyên $N, M$ ($1 \le N, M \le 400$).
- $N$ dòng tiếp theo: Mỗi dòng gồm $M$ số nguyên $A_{i, j}$ ($|A_{i, j}| \le 10^5$).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là tổng lớn nhất của ma trận con tìm được.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 3 <br> 1 2 -1 <br> -8 -2 5 <br> 4 7 -2 | 11 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N, M \le 400$.



### Bài 16 [CPPB-PT-16]: Cân Bằng Tiền Tố Đa Chiều

**Bối cảnh:** Cho một chuỗi gồm $N$ ký tự chỉ gồm các chữ cái `'A'`, `'B'`, `'C'`. Hãy tìm độ dài của đoạn con liên tiếp dài nhất chứa số lượng ký tự `'A'`, `'B'`, `'C'` bằng nhau từng đôi một.

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: Chuỗi $S$ gồm $N$ ký tự thuộc $\{'A', 'B', 'C'\}$.

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là độ dài lớn nhất của đoạn con cân bằng. Nếu không có, in `0`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 7 <br> ABACABA | 3 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 10^5$.




# Bài 05: Thuật toán tìm kiếm nhị phân


## 1. Khái niệm & bản chất của tìm kiếm nhị phân (Binary Search)

**Tìm kiếm nhị phân (Binary Search)** là thuật toán tìm kiếm dựa trên nguyên lý **chia để trị (Divide and Conquer)**. Bằng cách so sánh giá trị cần tìm với phần tử ở chính giữa không gian tìm kiếm, thuật toán loại bỏ chính xác **một nửa không gian tìm kiếm** sau mỗi bước lặp.

### 1.1. Điều kiện tiên quyết (prerequisite condition)
Thuật toán tìm kiếm nhị phân **CHỈ HOẠT ĐỘNG ĐƯỢC** khi không gian tìm kiếm hoặc mảng dữ liệu có **tính chất đơn điệu (Monotonicity)**:

* Mảng đã được sắp xếp tăng dần hoặc giảm dần.
* Hoặc một hàm mệnh đề logic $f(x) \in \{\text{True}, \text{False}\}$ thỏa mãn: nếu $f(x_0) = \text{True}$ thì $\forall x \ge x_0, f(x) = \text{True}$ (hoặc ngược lại).

### 1.2. Phân tích độ phức tạp thời gian $\mathcal{O}(\log N)$
Giả sử không gian tìm kiếm ban đầu có kích thước $N$:

* Bước 1: Thu hẹp còn $\frac{N}{2}$.
* Bước 2: Thu hẹp còn $\frac{N}{4} = \frac{N}{2^2}$.
* Bước $k$: Thu hẹp còn $\frac{N}{2^k}$.

Quá trình dừng lại khi kích thước không gian tìm kiếm bằng $1 \implies \frac{N}{2^k} = 1 \iff 2^k = N \iff k = \log_2 N$.

* Với $N = 10^5 \implies \log_2(10^5) \approx 17$ lần thu hẹp không gian.
* Với $N = 10^9 \implies \log_2(10^9) \approx 30$ lần thu hẹp không gian.
* Với $N = 10^{18} \implies \log_2(10^{18}) \approx 60$ lần thu hẹp không gian.

> **Bản chất hiệu năng:** Trên không gian nghiệm lên tới $10^{18}$, thuật toán chỉ cần khoảng **$60$ lần thu hẹp không gian**. Tổng thời gian thực tế của chương trình sẽ bằng:

> $\text{Total Time} = \mathcal{O}\Big(\log(\text{Range}) \times \text{Complexity}(\text{check})\Big)$
> Nếu hàm kiểm tra $\text{check}(mid)$ chạy trong $\mathcal{O}(N)$ với $N = 10^5$, chương trình chỉ mất khoảng $60 \times 10^5 = 6 \cdot 10^6$ phép tính (thực thi trong khoảng $0.02$ giây).

## 2. Tìm kiếm nhị phân trên mảng đã sắp xếp

### 2.1. Tìm chính xác giá trị $X$ (exact search)
Khởi tạo hai con trỏ biên: $low = 0, high = N - 1$.

* Tính trung điểm an toàn: $mid = low + \frac{high - low}{2}$.
* Nếu $A[mid] == X \implies$ Tìm thấy tại vị trí $mid$.
* Nếu $A[mid] < X \implies$ Giá trị $X$ chỉ có thể nằm ở nửa phải $\implies low = mid + 1$.
* Nếu $A[mid] > X \implies$ Giá trị $X$ chỉ có thể nằm ở nửa trái $\implies high = mid - 1$.

#### Ví dụ minh họa 1: Tìm kiếm giá trị $X = 23$
Cho mảng đã sắp xếp gồm 10 phần tử: $A = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]$

| Phần tử | $A[0]$ | $A[1]$ | $A[2]$ | $A[3]$ | $A[4]$ | $A[5]$ | $A[6]$ | $A[7]$ | $A[8]$ | $A[9]$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Giá trị** | $\mathbf{2}$ | $\mathbf{5}$ | $\mathbf{8}$ | $\mathbf{12}$ | $\mathbf{16}$ | $\mathbf{23}$ | $\mathbf{38}$ | $\mathbf{56}$ | $\mathbf{72}$ | $\mathbf{91}$ |

**Bảng mô phỏng từng bước thu hẹp không gian tìm kiếm:**

| Bước | Đoạn $[low, high]$ | Vị trí $mid$ | Giá trị $A[mid]$ | So sánh với $X = 23$ | Quyết định thu hẹp |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **1** | $[0, 9]$ | $mid = 4$ | $A[4] = 16$ | $16 < 23$ | $X$ nằm bên phải $\implies low \leftarrow 5$ |
| **2** | $[5, 9]$ | $mid = 7$ | $A[7] = 56$ | $56 > 23$ | $X$ nằm bên trái $\implies high \leftarrow 6$ |
| **3** | $[5, 6]$ | $mid = 5$ | $A[5] = 23$ | $23 = 23$ | **Khớp chính xác!** Tìm thấy tại chỉ số $index = 5$ |

### 2.2. Tìm kiếm phần tử biên: `lower_bound` và `upper_bound`

Trong lập trình thi đấu, dạng toán tìm vị trí biên quan trọng hơn nhiều so với tìm chính xác:

1. **`lower_bound` (Tìm phần tử nhỏ nhất $\ge X$):**
* Tìm vị trí đầu tiên mà giá trị tại đó $\ge X$.
* Nếu tất cả các phần tử đều $< X$, trả về vị trí sau phần tử cuối cùng ($N$).
2. **`upper_bound` (Tìm phần tử nhỏ nhất $> X$):**

* Tìm vị trí đầu tiên mà giá trị tại đó $> X$.

* Vị trí phần tử lớn nhất $\le X$ chính là `upper_bound - 1`.

#### Ví dụ minh họa 2: Mảng có phần tử lặp lại
Cho mảng: $A = [1, 3, 5, 5, 5, 8, 12]$, tìm các mốc biên với $X = 5$:

| Chỉ số (0-based) | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Giá trị mảng $A$** | $1$ | $3$ | $5$ | $5$ | $5$ | $8$ | $12$ |
| **Vị trí con trỏ STL** | — | — | **`lower_bound(5)`** (chỉ số 2) | — | — | **`upper_bound(5)`** (chỉ số 5) | — |

* `lower_bound(A.begin(), A.end(), 5) - A.begin()` $\implies$ Trả về **chỉ số 2** (số 5 đầu tiên).
* `upper_bound(A.begin(), A.end(), 5) - A.begin()` $\implies$ Trả về **chỉ số 5** (phần tử đầu tiên $> 5$).

* Số lần xuất hiện của số 5: $\text{Count}(5) = \text{upper} - \text{lower} = 5 - 2 = \mathbf{3}$ phần tử.
* Vị trí xuất hiện cuối cùng của số 5: $\text{upper} - 1 = 5 - 1 = \mathbf{4}$.

## 3. Kỹ thuật chặt nhị phân trên tập kết quả (Binary Search on answer)

Đây là kỹ thuật cốt lõi trong các kỳ thi học sinh giỏi và Olympic tin học.

### 3.1. Nhận diện tính chất đơn điệu & phân loại 2 hướng
Trước khi cài đặt, **bắt buộc phải xác định hướng biến thiên đơn điệu** của hàm kiểm tra `check(x)`:

* **Hướng 1: Dạng `True → False` (Tìm giá trị $X$ LỚN NHẤT thỏa mãn):**
* Đồ thị nghiệm: $[\text{True}, \text{True}, \dots, \text{True}, \mathbf{True_{\text{max}}}, \text{False}, \dots, \text{False}]$.
* Nếu `check(mid) == true` $\implies$ $mid$ thỏa mãn, ghi nhận `ans = mid` và tìm nghiệm lớn hơn ở bên phải: `low = mid + 1`.
* Nếu `check(mid) == false` $\implies$ $mid$ quá lớn, thu hẹp về bên trái: `high = mid - 1`.
* *Ví dụ điển hình:* Cắt gỗ lấy tối thiểu $M$ mét (độ cao cưa càng thấp càng nhiều gỗ $\implies$ tìm độ cao Max).

* **Hướng 2: Dạng `False → True` (Tìm giá trị $X$ NHỎ NHẤT thỏa mãn):**
* Đồ thị nghiệm: $[\text{False}, \text{False}, \dots, \text{False}, \mathbf{True_{\text{min}}}, \text{True}, \dots, \text{True}]$.
* Nếu `check(mid) == true` $\implies$ $mid$ thỏa mãn, ghi nhận `ans = mid` và tìm nghiệm nhỏ hơn ở bên trái: `high = mid - 1`.
* Nếu `check(mid) == false` $\implies$ $mid$ chưa đủ lớn, tăng giá trị lên: `low = mid + 1`.
* *Ví dụ điển hình:* Vận chuyển hàng trong $D$ ngày (tải trọng thuyền càng lớn càng dễ chở $\implies$ tìm tải trọng Min).

#### Ví dụ minh họa 3: Bài toán cắt gỗ lấy tối thiểu $M = 7$ mét gỗ
Cho $N = 4$ cây có chiều cao: $A = [20, 15, 10, 17]$. Cần tìm độ cao máy cưa $H$ **lớn nhất** sao cho tổng lượng gỗ thu được $\ge 7$.

* Không gian tìm kiếm: $low = 0, high = \max(A) = 20$.
* Hàm `check(H)`: Tính tổng $\sum \max(0, A_i - H)$. Nếu $\ge 7 \implies$ `True`, ngược lại `False`.

**Bảng mô phỏng từng bước chặt nhị phân:**

| Bước | Khoảng $[low, high]$ | Thử độ cao $H = mid$ | Tổng gỗ cắt được | Đánh giá $\ge 7\text{m}$ & Quyết định |
| :---: | :---: | :---: | :---: | :--- |
| **1** | $[0, 20]$ | $H = 10$ | $10 + 5 + 0 + 7 = \mathbf{22\text{m}}$ | $\ge 7 \implies$ Đủ gỗ! Lưu `ans = 10`, thử cưa cao hơn: $low \leftarrow 11$ |
| **2** | $[11, 20]$ | $H = 15$ | $5 + 0 + 0 + 2 = \mathbf{7\text{m}}$ | $\ge 7 \implies$ Đủ gỗ! Lưu `ans = 15`, thử cưa cao hơn: $low \leftarrow 16$ |
| **3** | $[16, 20]$ | $H = 18$ | $2 + 0 + 0 + 0 = \mathbf{2\text{m}}$ | $< 7 \implies$ Thiếu gỗ! Phải hạ cưa: $high \leftarrow 17$ |
| **4** | $[16, 17]$ | $H = 16$ | $4 + 0 + 0 + 1 = \mathbf{5\text{m}}$ | $< 7 \implies$ Thiếu gỗ! Phải hạ cưa: $high \leftarrow 15$ |
| **Dừng** | $[16, 15]$ | — | $low > high \implies$ Kết thúc | **Đáp án tối ưu: $H = 15$** |

## 4. Chặt nhị phân trên tập số thực (real-number Binary Search)

Khi đề bài yêu cầu tìm nghiệm thực với độ chính xác sai số tuyệt đối $\le 10^{-6}$:

* **Vấn đề của điều kiện `while (high - low > 1e-7)`:** Khi khoảng cách giữa $low$ và $high$ đạt tới giới hạn độ phân giải của kiểu `double` (bit mantissa), phép tính trung điểm `mid = (low + high) / 2.0` có thể bị làm tròn thành đúng $low$ hoặc $high$, khiến hiệu số $high - low$ không thể thu hẹp thêm, dẫn đến nguy cơ vòng lặp không tiến triển hoặc chạy vô hạn.

* **Giải pháp chuẩn thi đấu:** Sử dụng vòng lặp với **số lần lặp cố định** ($60 \dots 100$ lần):
$$\text{Độ thu hẹp} = \frac{\text{high} - \text{low}}{2^{100}} \approx \frac{10^9}{1.26 \times 10^{30}} \approx 10^{-21} \ll 10^{-6}$$
Đảm bảo thuật toán luôn dừng đúng số bước, an toàn tuyệt đối và đạt độ chính xác tối đa của phần cứng.

## 5. Mẫu cài đặt chuẩn thi đấu (competitive templates)

### Mẫu 1a: Tìm giá trị lớn nhất thỏa mãn (dạng `True -> False`)

```cpp
# include <bits/stdc++.h>
using namespace std;

// Hàm kiểm tra: Lượng gỗ thu được khi cưa ở độ cao mid có >= M hay không?
bool check(long long mid, const vector<long long>& a, long long m) {
    long long wood = 0;
    for (long long x : a) {
        if (x > mid) wood += (x - mid);

    }
    return wood >= m;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> a(n);

    long long max_val = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];

        max_val = max(max_val, a[i]);
    }

    long long low = 0, high = max_val;
    long long ans = 0;

    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (check(mid, a, m)) {
            ans = mid;        // Ghi nhận nghiệm hợp lệ
            low = mid + 1;    // Tìm giá trị lớn hơn ở bên phải
        } else {
            high = mid - 1;   // Không thỏa mãn, thu hẹp về bên trái
        }
    }

    cout << ans << "\n";
    return 0;
}
```

### Mẫu 1b: Tìm giá trị nhỏ nhất thỏa mãn (dạng `False -> True`)

```cpp
# include <bits/stdc++.h>
using namespace std;

// Hàm kiểm tra: Với tải trọng phà là mid, có chở hết hàng trong <= D ngày hay không?
bool check(long long mid, const vector<long long>& w, int d) {
    int days = 1;
    long long current_load = 0;
    for (long long x : w) {
        if (current_load + x > mid) {

            days++;
            current_load = x;
        } else {
            current_load += x;
        }
    }
    return days <= d;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, d;
    if (!(cin >> n >> d)) return 0;

    vector<long long> w(n);

    long long max_w = 0, sum_w = 0;
    for (int i = 0; i < n; ++i) {
        cin >> w[i];

        max_w = max(max_w, w[i]);
        sum_w += w[i];
    }

    // Không gian tìm kiếm: Tải trọng tối thiểu phải chở được kiện nặng nhất
    long long low = max_w, high = sum_w;
    long long ans = sum_w;

    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (check(mid, w, d)) {
            ans = mid;        // Ghi nhận nghiệm hợp lệ
            high = mid - 1;   // Tìm giá trị nhỏ hơn ở bên trái
        } else {
            low = mid + 1;    // Tải trọng chưa đủ, phải tăng lên
        }
    }

    cout << ans << "\n";
    return 0;
}
```

### Mẫu 2: Binary Search số thực (100 vòng lặp robust)

```cpp
# include <bits/stdc++.h>
using namespace std;

bool check_real(double mid) {
    return (mid * mid * mid + 2.0 * mid * mid + 10.0 * mid >= 100.0);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    double low = 0.0, high = 1e9;

    // Lặp cố định 100 lần để đạt sai số < 10^-15
    for (int iter = 0; iter < 100; ++iter) {
        double mid = low + (high - low) / 2.0;
        if (check_real(mid)) {
            high = mid;
        } else {
            low = mid;
        }
    }

    cout << fixed << setprecision(7) << low << "\n";
    return 0;
}
```

## 6. Các bẫy lỗi lập trình kinh điển (bug traps)

1. **Bẫy tràn số khi tính `mid`:** Biểu thức $mid = (low + high)/2$ sẽ bị tràn số kiểu `int` 32-bit nếu $low + high \ge 2 \cdot 10^9$. **Quy tắc bắt buộc:** Luôn viết $mid = low + (high - low)/2$.
2. **Bẫy vòng lặp vô tận (Infinite Loop):** Khi không gian tìm kiếm chỉ còn 2 phần tử ($low = high - 1$), nếu cập nhật `low = mid` trong khi `mid` bị làm tròn xuống sẽ khiến $low$ không bao giờ tăng, gây TLE. Cần cập nhật `low = mid + 1` hoặc `high = mid - 1`.
3. **Bẫy biên không gian tìm kiếm $[low, high]$:** Đặt $high$ quá nhỏ dẫn đến bỏ sót nghiệm đúng, hoặc đặt $low = 0$ dẫn đến lỗi chia cho 0 (`mid = 0`) trong hàm `check`.
4. **Bẫy phần tử trùng lặp trong mảng xoay vòng:** Nếu mảng xoay vòng có các phần tử trùng lặp thỏa mãn $A[low] == A[mid] == A[high]$, ta không thể xác định nửa nào được sắp xếp đơn điệu $\implies$ Trường hợp xấu nhất phải co cả hai đầu `low++` và `high--`, làm độ phức tạp suy biến về $\mathcal{O}(N)$.

## 7. Ranh giới áp dụng: Khi nào nên & không nên dùng?

* **KHI NÀO ÁP DỤNG:**
* Không gian tìm kiếm có tính chất **đơn điệu (Monotonic)**: Đồ thị hàm kiểm tra có dạng dải phân cách rõ ràng: $[\text{True}, \dots, \text{True}, \text{False}, \dots, \text{False}]$.
* Cần tối ưu nghiệm trên miền cực lớn ($1 \dots 10^{18}$) mà không thể duyệt tuần tự.
* **KHI NÀO THẤT BẠI:**
* Không gian tìm kiếm **không đơn điệu** (hàm dao động, có nhiều cực trị cục bộ). Lúc này chặt nhị phân sẽ bỏ sót nghiệm tối ưu toàn cục. Bắt buộc phải dùng **Ternary Search (Tìm kiếm Tam phân)** nếu hàm lồi/lõm, hoặc Quy hoạch động / Duyệt đồ thị.

## Bài tập thực hành


### Bài 01 [CPPB-BS-01]: Tìm Kiếm Phần Tử Trên Mảng Đã Sắp Xếp

**Bối cảnh:** Cho mảng số nguyên gồm $N$ phần tử đã được sắp xếp theo thứ tự tăng dần. Có $Q$ câu hỏi, mỗi câu hỏi cho một số nguyên $X$, yêu cầu kiểm tra xem số $X$ có xuất hiện trong mảng hay không.

**Nhiệm vụ:** Hãy sử dụng thuật toán Tìm kiếm nhị phân (Binary Search) để trả lời mỗi truy vấn trong thời gian $\mathcal{O}(\log N)$.

**Đầu vào (Input):**

- Dòng 1: Gồm 2 số nguyên $N, Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: $N$ số nguyên đã sắp xếp tăng dần $A_1, A_2, \dots, A_N$ ($|A_i| \le 10^9$).
- Dòng 3: $Q$ số nguyên $X_1, X_2, \dots, X_Q$ ($|X_i| \le 10^9$).

**Đầu ra (Output):**

- In ra $Q$ dòng, mỗi dòng in `YES` nếu phần tử tương ứng tồn tại trong mảng, ngược lại in `NO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 3 <br> 1 3 5 7 9 <br> 3 4 9 | YES <br> NO <br> YES |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N, Q \le 10^5, |A_i| \le 10^9$.



### Bài 02 [CPPB-BS-02]: Tìm Vị Trí Xuất Hiện Đầu Tiên & Cuối Cùng

**Bối cảnh:** Cho mảng $N$ phần tử đã được sắp xếp tăng dần. Có $Q$ truy vấn, mỗi truy vấn cho một số $X$. Hãy tìm vị trí xuất hiện đầu tiên và vị trí xuất hiện cuối cùng của $X$ trong mảng (đánh số từ 1 đến $N$). Nếu không tồn tại, in ra `-1 -1`.

**Đầu vào (Input):**

- Dòng 1: Gồm 2 số nguyên $N, Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: $N$ số nguyên đã sắp xếp $A_1, A_2, \dots, A_N$ ($|A_i| \le 10^9$).
- $Q$ dòng tiếp theo: Mỗi dòng gồm một số nguyên $X$ ($|X| \le 10^9$).

**Đầu ra (Output):**

- In ra $Q$ dòng, mỗi dòng gồm 2 số là vị trí đầu tiên và cuối cùng (1-based), hoặc `-1 -1`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 6 2 <br> 1 2 2 2 5 6 <br> 2 <br> 3 | 2 4 <br> -1 -1 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N, Q \le 10^5$.



### Bài 03 [CPPB-BS-03]: Đếm Số Phần Tử Trong Đoạn [L, R]

**Bối cảnh:** Cho mảng gồm $N$ số nguyên (chưa sắp xếp). Có $Q$ câu hỏi, mỗi câu hỏi gồm 2 số $L, R$ ($L \le R$), yêu cầu đếm xem trong mảng có bao nhiêu phần tử có giá trị nằm trong đoạn $[L \dots R]$ (tức $L \le A_i \le R$).

**Đầu vào (Input):**

- Dòng 1: Gồm 2 số nguyên $N, Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($|A_i| \le 10^9$).
- $Q$ dòng tiếp theo: Mỗi dòng gồm 2 số $L, R$ ($|L|, |R| \le 10^9, L \le R$).

**Đầu ra (Output):**

- In ra $Q$ dòng, mỗi dòng là số lượng phần tử thỏa mãn.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 2 <br> 5 1 9 3 7 <br> 2 8 <br> 10 20 | 3 <br> 0 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N, Q \le 10^5$.



### Bài 04 [CPPB-BS-04]: Tìm Căn Bậc Hai Số Nguyên Lớn

**Bối cảnh:** Cho một số nguyên dương $N$ ($1 \le N \le 10^{18}$). Hãy tìm số nguyên dương $X$ lớn nhất sao cho $X^2 \le N$ (phần nguyên của căn bậc hai $\lfloor \sqrt{N} \rfloor$).

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $T$ ($1 \le T \le 10^5$) là số lượng testcase.
- $T$ dòng tiếp theo: Mỗi dòng gồm một số nguyên dương $N$ ($1 \le N \le 10^{18}$).

**Đầu ra (Output):**

- In ra $T$ dòng kết quả tương ứng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 <br> 16 <br> 20 <br> 1000000000000000000 | 4 <br> 4 <br> 1000000000 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 10^{18}$.



### Bài 05 [CPPB-BS-05]: Tìm Phần Tử Nhỏ Nhất Lớn Hơn X

**Bối cảnh:** Cho một mảng gồm $N$ số nguyên đã được sắp xếp tăng dần. Có $Q$ truy vấn, mỗi truy vấn cho một số nguyên $X$. Hãy tìm giá trị của phần tử nhỏ nhất trong mảng có giá trị nghiêm ngặt lớn hơn $X$. Nếu không có phần tử nào lớn hơn $X$, in ra `-1`.

**Đầu vào (Input):**

- Dòng 1: Gồm 2 số nguyên $N, Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: $N$ số nguyên đã sắp xếp $A_1, A_2, \dots, A_N$ ($|A_i| \le 10^9$).
- $Q$ dòng tiếp theo: Mỗi dòng gồm một số nguyên $X$ ($|X| \le 10^9$).

**Đầu ra (Output):**

- In ra $Q$ dòng kết quả tương ứng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 3 <br> 2 4 6 8 10 <br> 5 <br> 8 <br> 11 | 6 <br> 10 <br> -1 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N, Q \le 10^5$.



### Bài 06 [CPPB-BS-06]: Chia Kẹo Cho Học Sinh Đạt Chuẩn

**Bối cảnh:** Có $N$ gói kẹo, gói thứ $i$ chứa $A_i$ chiếc kẹo. Thầy giáo muốn chia đều kẹo cho $K$ học sinh sao cho mỗi học sinh nhận được đúng $M$ chiếc kẹo từ một gói nào đó (mỗi gói có thể chia cho nhiều học sinh, nhưng kẹo thừa trong gói không được ghép với gói khác).

**Nhiệm vụ:** Hãy tìm số lượng kẹo $M$ lớn nhất mà mỗi học sinh có thể nhận được. Nếu không thể chia cho đủ $K$ học sinh (ngay cả khi mỗi bạn 1 chiếc), in ra `0`.

**Đầu vào (Input):**

- Dòng 1: Gồm 2 số nguyên $N, K$ ($1 \le N \le 10^5, 1 \le K \le 10^{14}$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là giá trị $M$ lớn nhất tìm được.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 6 <br> 10 15 20 25 | 10 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 10^5, K \le 10^{14}$.



### Bài 07 [CPPB-BS-07]: Cắt Gỗ Xây Dựng (Woodcutting / EKO)

**Bối cảnh:** Bác thợ mộc cần lấy ít nhất $M$ mét gỗ. Khu rừng có $N$ cái cây với chiều cao lần lượt là $A_1, A_2, \dots, A_N$. Bác sử dụng một máy cắt có thể điều chỉnh độ cao lưỡi cưa tại mức $H$. Máy sẽ cắt ngang tất cả các cây có chiều cao lớn hơn $H$, phần ngọn bị cắt rời (chiều cao $A_i - H$) sẽ được gom lại làm gỗ. Các cây có chiều cao $\le H$ sẽ giữ nguyên vẹn.

**Nhiệm vụ:** Hãy tìm độ cao $H$ nguyên lớn nhất để bác thợ mộc thu được ít nhất $M$ mét gỗ.

**Đầu vào (Input):**

- Dòng 1: Gồm 2 số nguyên $N, M$ ($1 \le N \le 10^5, 1 \le M \le 10^{14}$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là độ cao $H$ lớn nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 7 <br> 20 15 10 17 | 15 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 10^5, M \le 10^{14}$.



### Bài 08 [CPPB-BS-08]: Đặt Trạm Phát Sóng Cách Nhau Xa Nhất (Aggressive Cows)

**Bối cảnh:** Dọc theo một đường thẳng có $N$ vị trí có thể đặt trạm phát sóng tại các tọa độ $X_1, X_2, \dots, X_N$. Bạn cần chọn ra đúng $C$ vị trí để đặt trạm sao cho khoảng cách giữa hai trạm bất kỳ gần nhau nhất là **lớn nhất có thể** (nhằm giảm thiểu sự can nhiễu sóng).

**Đầu vào (Input):**

- Dòng 1: Gồm 2 số nguyên $N, C$ ($2 \le C \le N \le 10^5$).
- Dòng 2: $N$ số nguyên biểu diễn tọa độ các điểm $X_1, X_2, \dots, X_N$ ($0 \le X_i \le 10^9$).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là khoảng cách nhỏ nhất lớn nhất tìm được.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 3 <br> 1 2 8 4 9 | 3 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 10^5, X_i \le 10^9$.



### Bài 09 [CPPB-BS-09]: Chia Mảng Thành K Đoạn Có Tổng Max Nhỏ Nhất

**Bối cảnh:** Cho một dãy gồm $N$ số nguyên dương $A_1, A_2, \dots, A_N$. Hãy chia dãy số này thành đúng $K$ đoạn con liên tiếp sao cho **tổng lớn nhất của một đoạn con là nhỏ nhất có thể**.

**Đầu vào (Input):**

- Dòng 1: Gồm 2 số nguyên $N, K$ ($1 \le K \le N \le 10^5$).
- Dòng 2: $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là tổng đoạn con lớn nhất nhỏ nhất có thể đạt được.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 3 <br> 7 2 5 10 8 | 14 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 10^5, A_i \le 10^9$.



### Bài 10 [CPPB-BS-10]: Vận Chuyển Hàng Hóa Qua Phà Trong D Ngày

**Bối cảnh:** Có $N$ kiện hàng được xếp thành một hàng dọc với trọng lượng lần lượt là $W_1, W_2, \dots, W_N$. Một chiếc phà cần vận chuyển toàn bộ $N$ kiện hàng này theo đúng thứ tự ban đầu qua sông trong không quá $D$ ngày. Mỗi ngày phà chỉ chở được một khối lượng hàng có tổng trọng lượng không vượt quá tải trọng $C$ của phà.

**Nhiệm vụ:** Hãy tìm tải trọng $C$ nhỏ nhất của phà để hoàn thành công việc đúng hạn trong $D$ ngày.

**Đầu vào (Input):**

- Dòng 1: Gồm 2 số nguyên $N, D$ ($1 \le D \le N \le 10^5$).
- Dòng 2: $N$ số nguyên dương $W_1, W_2, \dots, W_N$ ($1 \le W_i \le 10^9$).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là tải trọng tối thiểu của phà.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 6 3 <br> 3 2 2 4 1 4 | 6 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 10^5, W_i \le 10^9$.



### Bài 11 [CPPB-BS-11]: Tìm Nghiệm Thực Của Phương Trình Đơn Điệu

**Bối cảnh:** Cho phương trình số thực:
$$f(x) = x^3 + 2x^2 + 10x - C = 0$$
với $C$ là một hằng số thực dương ($1 \le C \le 10^9$).

**Nhiệm vụ:** Hãy tìm nghiệm thực $x > 0$ của phương trình với độ chính xác sai số tuyệt đối không quá $10^{-6}$.

**Đầu vào (Input):**

- Dòng 1: Số thực $C$ ($1 \le C \le 10^9$).

**Đầu ra (Output):**

- In ra nghiệm thực $x$ lấy đúng 6 chữ số sau dấu phẩy thập phân.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 13 | 1.000000 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le C \le 10^9$.



### Bài 12 [CPPB-BS-12]: Phần Tử Thứ K Của Hai Mảng Đã Sắp Xếp

**Bối cảnh:** Cho hai mảng số nguyên $A$ và $B$ có kích thước lần lượt là $N$ và $M$, cả hai đều đã được sắp xếp theo thứ tự tăng dần. Hãy tìm phần tử nhỏ thứ $K$ ($1 \le K \le N + M$) khi gộp chung hai mảng lại với nhau.

**Đầu vào (Input):**

- Dòng 1: Gồm 3 số nguyên $N, M, K$ ($1 \le N, M \le 10^5, 1 \le K \le N + M$).
- Dòng 2: $N$ số nguyên đã sắp xếp $A_1, A_2, \dots, A_N$ ($|A_i| \le 10^9$).
- Dòng 3: $M$ số nguyên đã sắp xếp $B_1, B_2, \dots, B_M$ ($|B_i| \le 10^9$).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là giá trị của phần tử nhỏ thứ $K$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 4 5 <br> 2 3 6 7 9 <br> 1 4 8 10 | 6 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N, M \le 10^5, |A_i|, |B_i| \le 10^9$.



### Bài 13 [CPPB-BS-13]: Tìm Đoạn Con Có Trung Bình Lớn Nhất Độ Dài >= K

**Bối cảnh:** Cho một dãy số nguyên gồm $N$ phần tử $A_1, A_2, \dots, A_N$ và một số nguyên $K$ ($1 \le K \le N$). Hãy tìm một đoạn con liên tiếp có độ dài ít nhất là $K$ sao cho giá trị trung bình cộng của các phần tử trong đoạn là **lớn nhất có thể**.

**Đầu vào (Input):**

- Dòng 1: Gồm 2 số nguyên $N, K$ ($1 \le K \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($0 \le A_i \le 10^6$).

**Đầu ra (Output):**

- In ra giá trị trung bình lớn nhất lấy 4 chữ số thập phân.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 2 <br> 6 8 1 3 | 7.0000 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 10^5, A_i \le 10^6$.



### Bài 14 [CPPB-BS-14]: Tối Ưu Hóa Tuyến Đường Vận Tải Đa Điểm

**Bối cảnh:** Có $N$ thành phố xếp liên tiếp từ $1$ đến $N$. Tại thành phố thứ $i$ có $A_i$ tấn hàng cần vận chuyển. Có $M$ xe tải giống hệt nhau, mỗi xe có bình nhiên liệu cho phép chạy tối đa một quãng đường $D$ (tức chỉ có thể gom hàng trong một cụm các thành phố liên tiếp có độ dài không vượt quá $D$ thành phố). Mỗi xe tải có sức chứa tối đa là $C$ tấn hàng.

**Nhiệm vụ:** Biết trước danh sách hàng hóa tại $N$ thành phố và số lượng xe $M$. Hãy tìm sức chứa tối thiểu $C$ của mỗi xe tải sao cho toàn bộ hàng hóa được gom hết về kho mà không xe nào phải gom quá cự ly $D$ thành phố.

**Đầu vào (Input):**

- Dòng 1: Gồm 3 số nguyên $N, M, D$ ($1 \le N \le 2 \cdot 10^5, 1 \le M \le N, 1 \le D \le N$).
- Dòng 2: $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là sức chứa $C$ nhỏ nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 2 3 <br> 4 2 3 5 1 | 9 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 2 \cdot 10^5, A_i \le 10^9$.



### Bài 15 [CPPB-BS-15]: Tìm Kiếm Trên Mảng Sắp Xếp Bị Xoay Vòng (Rotated Array)

**Bối cảnh:** Cho một mảng $N$ số nguyên phân biệt ban đầu đã sắp xếp tăng dần, nhưng bị xoay vòng tại một điểm bất kỳ không rõ (ví dụ: $[0, 1, 2, 4, 5, 6, 7]$ xoay vòng thành $[4, 5, 6, 7, 0, 1, 2]$). Có $Q$ câu hỏi, mỗi câu hỏi cho một số $X$, yêu cầu tìm vị trí của $X$ trong mảng (đánh số từ 1 đến $N$). Nếu không tồn tại, in ra `-1`.

**Đầu vào (Input):**

- Dòng 1: Gồm 2 số nguyên $N, Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: $N$ số nguyên phân biệt của mảng xoay vòng $A_1, A_2, \dots, A_N$ ($|A_i| \le 10^9$).
- $Q$ dòng tiếp theo: Mỗi dòng gồm một số nguyên $X$ ($|X| \le 10^9$).

**Đầu ra (Output):**

- In ra $Q$ dòng, mỗi dòng là vị trí của $X$ (1-based) hoặc `-1`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 7 2 <br> 4 5 6 7 0 1 2 <br> 0 <br> 3 | 5 <br> -1 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N, Q \le 10^5$.



### Bài 16 [CPPB-BS-16]: Tìm Kiếm Trên Ma Trận 2D Đã Sắp Xếp (Matrix Search)

**Bối cảnh:** Cho ma trận $A$ kích thước $N \times M$ với các tính chất:
1. Các số trên mỗi hàng được sắp xếp theo thứ tự tăng dần từ trái sang phải.
2. Số đầu tiên của mỗi hàng luôn nghiêm ngặt lớn hơn số cuối cùng của hàng ngay trước nó.

Có $Q$ truy vấn, mỗi truy vấn cho một số nguyên $X$. Hãy kiểm tra xem $X$ có xuất hiện trong ma trận hay không.

**Đầu vào (Input):**

- Dòng 1: Gồm 3 số nguyên $N, M, Q$ ($1 \le N, M \le 1000, 1 \le Q \le 10^5$).
- $N$ dòng tiếp theo: Mỗi dòng gồm $M$ số nguyên $A_{i, j}$ ($|A_{i, j}| \le 10^9$).
- $Q$ dòng tiếp theo: Mỗi dòng gồm một số nguyên $X$ ($|X| \le 10^9$).

**Đầu ra (Output):**

- In ra $Q$ dòng, mỗi dòng in `YES` nếu tìm thấy, ngược lại in `NO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 4 2 <br> 1 3 5 7 <br> 10 11 16 20 <br> 23 30 34 60 <br> 3 <br> 13 | YES <br> NO |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N, M \le 1000, Q \le 10^5$.



### Bài 17 [CPPB-BS-17]: Tìm Đỉnh Của Dãy Núi (Peak in Mountain Array)

**Bối cảnh:** Một mảng $A$ gồm $N$ số nguyên ($N \ge 3$) được gọi là một **dãy núi** nếu tồn tại chỉ số đỉnh $P$ ($1 < P < N$) sao cho:
$$A_1 < A_2 < \dots < A_{P-1} < A_P > A_{P+1} > \dots > A_N$$

**Nhiệm vụ:** Hãy tìm chỉ số $P$ (1-based) của đỉnh núi trong thời gian $\mathcal{O}(\log N)$.

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $N$ ($3 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($0 \le A_i \le 10^9$).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là chỉ số của đỉnh núi (1-based).

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 <br> 1 3 5 4 2 | 3 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $3 \le N \le 10^5$. Dữ liệu đảm bảo mảng luôn có dạng dãy núi hợp lệ.



### Bài 18 [CPPB-BS-18]: Trung Vị Của Hai Mảng Đã Sắp Xếp (Median of Two Sorted)

**Bối cảnh:** Cho hai mảng số nguyên $A$ và $B$ đã được sắp xếp tăng dần với kích thước lần lượt là $N$ và $M$. Hãy tìm giá trị trung vị (Median) của mảng hợp nhất gồm $N + M$ phần tử trong thời gian tối ưu $\mathcal{O}(\log(\min(N, M)))$.

(Quy ước: Nếu tổng số phần tử $N + M$ là lẻ, trung vị là phần tử ở chính giữa. Nếu $N + M$ là chẵn, trung vị là trung bình cộng của 2 phần tử ở chính giữa lấy 1 chữ số thập phân).

**Đầu vào (Input):**

- Dòng 1: Gồm 2 số nguyên $N, M$ ($1 \le N, M \le 10^5$).
- Dòng 2: $N$ số nguyên đã sắp xếp $A_1, A_2, \dots, A_N$ ($|A_i| \le 10^9$).
- Dòng 3: $M$ số nguyên đã sắp xếp $B_1, B_2, \dots, B_M$ ($|B_i| \le 10^9$).

**Đầu ra (Output):**

- In ra giá trị trung vị lấy đúng 1 chữ số sau dấu phẩy thập phân.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 2 2 <br> 1 3 <br> 2 4 | 2.5 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N, M \le 10^5$.




# Bài 06: Phép toán BIT & biểu diễn trạng thái


## 1. Khái niệm & 6 phép toán BIT cơ bản

Máy tính biểu diễn tất cả dữ liệu dưới dạng chuỗi nhị phân (gồm các bit $0$ và $1$). **Phép toán bit (Bitwise Operations)** là các thao tác tác động trực tiếp lên từng bit của thanh ghi CPU, đạt tốc độ thực thi nhanh nhất trong mọi câu lệnh phần mềm.

### 1.1. Bảng chân trị của 6 phép toán BIT trong C++

| Toán Tử C++ | Tên Phép Toán | Ký Hiệu Toán | Quy Tắc Bit | Ví dụ ($a = 5 = 101_2, b = 3 = 011_2$) |
|:---:|---|:---:|---|---|
| `&` | **AND** (Và) | $\wedge$ | Ra $1$ khi và chỉ khi cả 2 bit đều là $1$ | $5 \ \& \ 3 = 101_2 \ \& \ 011_2 = 001_2 = 1$ |
| `\|` | **OR** (Hoặc) | $\vee$ | Ra $1$ khi có ít nhất một bit là $1$ | $5 \text{ OR } 3 = 101_2 \text{ OR } 011_2 = 111_2 = 7$ |
| `^` | **XOR** (Hoặc loại trừ) | $\oplus$ | Ra $1$ khi 2 bit khác nhau, ra $0$ khi 2 bit giống nhau | $5 \ \hat{} \ 3 = 101_2 \ \hat{} \ 011_2 = 110_2 = 6$ |
| `~` | **NOT** (Đảo bit) | $\neg$ | Đổi $0 \to 1$ và $1 \to 0$ | $\sim 5 = \sim(00\dots0101_2) = -6$ |
| `<<` | **Dịch trái** (Left Shift) | $\ll$ | Dịch các bit sang trái $k$ vị trí (nhân $2^k$) | $5 \ll 2 = 10100_2 = 20$ |
| `>>` | **Dịch phải** (Right Shift) | $\gg$ | Dịch các bit sang phải $k$ vị trí (chia nguyên $2^k$) | $5 \gg 1 = 10_2 = 2$ |

### 1.2. Các tính chất đại số quan trọng của phép XOR ($\oplus$)

* Tính tự triệt tiêu: $A \oplus A = 0$.
* Phần tử trung hòa: $A \oplus 0 = A$.
* Giao hoán & Kết hợp: $A \oplus B = B \oplus A$ và $(A \oplus B) \oplus C = A \oplus (B \oplus C)$.
* Đổi giá trị 2 biến không cần biến phụ: `a ^= b; b ^= a; a ^= b;`.

## 2. 4 thao tác thao tác BIT chuẩn thi đấu

Quy ước đánh số các bit từ phải sang trái, bắt đầu từ bit $0$ (bit có trọng số nhỏ nhất $2^0$).

### 2.1. Kiểm tra BIT thứ $k$ có đang bật (bằng 1) hay không:
```cpp
bool is_set = (mask >> k) & 1;

// Hoặc: bool is_set = (mask & (1LL << k)) != 0;
```

### 2.2. Bật BIT thứ $k$ (gán thành 1):
```cpp
mask = mask | (1LL << k);
// Viết gọn: mask |= (1LL << k);
```

### 2.3. Tắt BIT thứ $k$ (gán thành 0):
```cpp
mask = mask & ~(1LL << k);
// Viết gọn: mask &= ~(1LL << k);
```

### 2.4. Đảo BIT thứ $k$ ($0 \to 1, 1 \to 0$):
```cpp
mask = mask ^ (1LL << k);
// Viết gọn: mask ^= (1LL << k);
```

#### Ví dụ minh họa 1: Thao tác trên số $N = 13 = 1101_2$



![Trực quan hóa cấu trúc Bit & 4 Thao tác Bit trên N = 13](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-06-phep-toan-bit/assets/bit_operations_simulation_vi.png)



## 3. Các tuyệt kỹ BIT & hàm nội tại CPU (builtin functions)

### 3.1. Kiểm tra một số nguyên dương có phải là lũy thừa của 2
Một số $N > 0$ là lũy thừa của 2 ($2^k$) khi và chỉ khi trong biểu diễn nhị phân của nó có **đúng duy nhất một bit 1**:

```cpp
bool is_power_of_two = (n > 0) && ((n & (n - 1)) == 0);

```

### 3.2. Lấy BIT 1 nhỏ nhất (lowest set BIT / lowbit)
Dùng trong cấu trúc Fenwick Tree và giải thuật bit:
```cpp
long long lowbit = x & (-x);
```

### 3.3. Các hàm nội tại tối ưu hóa phần cứng trong gcc/clang:

* `__builtin_popcount(unsigned int x)` / `__builtin_popcountll(unsigned long long x)`: Đếm số lượng bit 1 trong $\mathcal{O}(1)$ chu kỳ CPU.
* `__builtin_clz(x)` / `__builtin_clzll(x)`: Đếm số lượng bit 0 liên tiếp ở đầu (Count Leading Zeros).
* `__builtin_ctz(x)` / `__builtin_ctzll(x)`: Đếm số lượng bit 0 liên tiếp ở cuối (Count Trailing Zeros).

## 4. Kỹ thuật mặt nạ BIT (bitmask & subset enumeration)

Mặt nạ bit (**Bitmask**) là kỹ thuật dùng một số nguyên $N$ bit để biểu diễn một tập hợp con gồm các phần tử được chọn từ tập $N$ phần tử:

* Bit thứ $i = 1 \implies$ Phần tử thứ $i$ được chọn.
* Bit thứ $i = 0 \implies$ Phần tử thứ $i$ không được chọn.

### 4.1. Duyệt toàn bộ $2^N$ tập con (vét cạn nhị phân):
```cpp
int n = 4;
for (int mask = 0; mask < (1 << n); ++mask) {
    for (int i = 0; i < n; ++i) {
        if ((mask >> i) & 1) {

            // Phần tử i thuộc tập con hiện tại
        }
    }
}
```

### 4.2. Duyệt tất cả tập con (submasks) của một mask trong $\mathcal{O}(3^N)$:
```cpp
for (int sub = mask; sub > 0; sub = (sub - 1) & mask) {

    // sub là một tập con hợp lệ của mask
}
```

#### Ví dụ minh họa 2: Biểu diễn tập con của tập 3 phần tử $S = \{A_0, A_1, A_2\}$
Với $N = 3$, có $2^3 = 8$ mặt nạ bit từ $0$ đến $7$:

| Giá Trị Mask (Thập phân) | Biểu Diễn Nhị Phân ($b_2 b_1 b_0$) | Bit $2$ ($A_2$) | Bit $1$ ($A_1$) | Bit $0$ ($A_0$) | Tập Con Tương Ứng |
|:---:|:---:|:---:|:---:|:---:|---|
| **0** | `000` | $0$ | $0$ | $0$ | $\emptyset$ (Tập rỗng) |
| **1** | `001` | $0$ | $0$ | $1$ | $\{A_0\}$ |
| **2** | `010` | $0$ | $1$ | $0$ | $\{A_1\}$ |
| **3** | `011` | $0$ | $1$ | $1$ | $\{A_0, A_1\}$ |
| **4** | `100` | $1$ | $0$ | $0$ | $\{A_2\}$ |
| **5** | `101` | $1$ | $0$ | $1$ | $\{A_0, A_2\}$ |
| **6** | `110` | $1$ | $1$ | $0$ | $\{A_1, A_2\}$ |
| **7** | `111` | $1$ | $1$ | $1$ | $\{A_0, A_1, A_2\}$ (Tập đầy đủ) |

## 5. Mẫu cài đặt chuẩn thi đấu (competitive template)

### Mẫu 1: Vét cạn tập con bằng mặt nạ BIT (subset sum)

```cpp
# include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long target_s;
    if (!(cin >> n >> target_s)) return 0;

    vector<long long> a(n);

    for (int i = 0; i < n; ++i) {
        cin >> a[i];

    }

    bool found = false;
    int total_masks = (1 << n);

    for (int mask = 0; mask < total_masks; ++mask) {
        long long current_sum = 0;
        for (int i = 0; i < n; ++i) {
            if ((mask >> i) & 1) {

                current_sum += a[i];
            }
        }
        if (current_sum == target_s) {
            found = true;
            break;
        }
    }

    cout << (found ? "YES\n" : "NO\n");
    return 0;
}
```

## 6. Các bẫy lỗi lập trình kinh điển (bug traps)

1. **Bẫy thứ tự ưu tiên toán tử (Operator Precedence Bug):** Trong C++, các phép toán bit `&`, `|`, `^` có độ ưu tiên **thấp hơn** các phép toán so sánh `==`, `!=`, `<`, `>`.
* **Lỗi sai:** `if (mask & (1 << k) != 0)` sẽ bị hiểu thành `if (mask & ((1 << k) != 0))` $\implies$ Sai kết quả!
* **Cú pháp chuẩn:** `if ((mask & (1 << k)) != 0)` hoặc `if ((mask >> k) & 1)`.

2. **Bẫy tràn số khi dịch bit quá 31:** Hằng số `1` mặc định là số nguyên 32-bit có dấu. Biểu thức `1 << 40` sẽ gây tràn số và lỗi hành vi không xác định (Undefined Behavior).
* **Quy tắc bắt buộc:** Luôn viết `1LL << k` khi $k \ge 31$.

## 7. Ranh giới áp dụng: Khi nào nên & không nên dùng?

* **KHI NÀO ÁP DỤNG:**
* Kích thước tập hợp nhỏ: $N \le 20$ ($2^{20} \approx 10^6$ phép tính) hoặc $N \le 24$ ($2^{24} \approx 1.6 \cdot 10^7$ phép tính).
* Cần tối ưu bộ nhớ trạng thái và tốc độ truy vấn tập hợp $\mathcal{O}(1)$.
* **KHI NÀO THẤT BẠI:**
* Khi $N \ge 30$ ($2^{30} \approx 10^9$ phép tính $\implies$ TLE). Lúc này bắt buộc phải dùng:
* **Chia đôi tập hợp (Meet-in-the-middle)** khi $N \le 40$ ($\mathcal{O}(2^{N/2}) = 2^{20} \approx 10^6$).
* Quy hoạch động hoặc Thuật toán Tham lam nếu bài toán có cấu trúc con tối ưu.

## Bài tập thực hành


### Bài 01 [CPPB-BIT-01]: Bật, Tắt Và Kiểm Tra Bit Thứ K

**Bối cảnh:** Cho một số nguyên không âm $N$ ($0 \le N \le 10^{18}$). Có $Q$ thao tác, mỗi thao tác thuộc một trong 3 loại:
1. `1 k`: Bật bit thứ $k$ của $N$ lên 1.
2. `2 k`: Tắt bit thứ $k$ của $N$ về 0.
3. `3 k`: Kiểm tra xem bit thứ $k$ của $N$ có đang bật hay không (in ra `1` nếu bật, `0` nếu tắt).

(Quy ước các bit được đánh số từ $0$ đến $60$, với bit 0 là bit có trọng số $2^0$).

**Đầu vào (Input):**

- Dòng 1: Gồm 2 số nguyên $N, Q$ ($0 \le N \le 10^{18}, 1 \le Q \le 10^5$).
- $Q$ dòng tiếp theo: Mỗi dòng gồm 2 số nguyên `type k` ($1 \le \text{type} \le 3, 0 \le k \le 60$).

**Đầu ra (Output):**

- Với mỗi thao tác loại 3, in ra kết quả trên một dòng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 4 <br> 3 0 <br> 3 1 <br> 1 1 <br> 3 1 | 1 <br> 0 <br> 1 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 10^{18}, Q \le 10^5, k \le 60$.



### Bài 02 [CPPB-BIT-02]: Đếm Số Lượng Bit 1 (Popcount)

**Bối cảnh:** Cho một số nguyên không âm $N$ ($0 \le N \le 10^{18}$). Hãy đếm số lượng bit có giá trị bằng $1$ trong biểu diễn nhị phân của số $N$.

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $T$ ($1 \le T \le 10^5$) là số lượng testcase.
- $T$ dòng tiếp theo: Mỗi dòng gồm một số nguyên $N$ ($0 \le N \le 10^{18}$).

**Đầu ra (Output):**

- In ra $T$ dòng, mỗi dòng là số lượng bit 1 của số $N$ tương ứng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 <br> 5 <br> 15 <br> 0 | 2 <br> 4 <br> 0 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 10^{18}, T \le 10^5$.



### Bài 03 [CPPB-BIT-03]: Kiểm Tra Số Có Phải Lũy Thừa Của 2

**Bối cảnh:** Cho một số nguyên dương $N$ ($1 \le N \le 10^{18}$). Hãy kiểm tra xem $N$ có phải là một lũy thừa của 2 hay không (tức tồn tại số nguyên không âm $k$ sao cho $N = 2^k$).

**Đầu vào (Input):**

- Dòng 1: Số nguyên $T$ ($1 \le T \le 10^5$) là số lượng testcase.
- $T$ dòng tiếp theo: Mỗi dòng gồm một số nguyên dương $N$ ($1 \le N \le 10^{18}$).

**Đầu ra (Output):**

- In ra $T$ dòng, mỗi dòng in `YES` nếu là lũy thừa của 2, ngược lại in `NO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 <br> 16 <br> 18 <br> 1 | YES <br> NO <br> YES |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 10^{18}$.



### Bài 04 [CPPB-BIT-04]: Tìm Phần Tử Xuất Hiện 1 Lần Duy Nhất

**Bối cảnh:** Cho một mảng gồm $2N + 1$ số nguyên. Trong đó, có đúng một phần tử xuất hiện đúng 1 lần duy nhất, còn tất cả các phần tử khác đều xuất hiện đúng 2 lần.

**Nhiệm vụ:** Hãy tìm giá trị của phần tử xuất hiện 1 lần duy nhất đó với độ phức tạp thời gian $\mathcal{O}(N)$ và bộ nhớ $\mathcal{O}(1)$.

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$, mảng có $2N+1$ phần tử).
- Dòng 2: $2N + 1$ số nguyên $A_1, A_2, \dots, A_{2N+1}$ ($0 \le A_i \le 10^9$).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là phần tử xuất hiện 1 lần.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 2 <br> 4 1 2 1 2 | 4 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 10^5$.



### Bài 05 [CPPB-BIT-05]: Tìm Hai Số Xuất Hiện 1 Lần Duy Nhất

**Bối cảnh:** Cho một mảng gồm $2N + 2$ số nguyên. Trong mảng có đúng hai số nguyên $X$ và $Y$ ($X < Y$) xuất hiện đúng 1 lần duy nhất, còn tất cả các số khác đều xuất hiện đúng 2 lần.

**Nhiệm vụ:** Hãy tìm hai số $X$ và $Y$.

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$, tổng số phần tử là $2N+2$).
- Dòng 2: $2N + 2$ số nguyên $A_1, A_2, \dots, A_{2N+2}$ ($0 \le A_i \le 10^9$).

**Đầu ra (Output):**

- In ra hai số $X$ và $Y$ ($X < Y$) cách nhau bởi khoảng trắng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 2 <br> 1 2 1 3 2 5 | 3 5 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 10^5$.



### Bài 06 [CPPB-BIT-06]: Đảo Bit Và Giá Trị Bù 1

**Bối cảnh:** Cho một số nguyên dương $N$. Biểu diễn $N$ dưới dạng nhị phân không có các số 0 vô nghĩa ở đầu. Hãy tìm số nguyên thu được sau khi đảo ngược tất cả các bit của $N$ (biến bit 0 thành 1, và bit 1 thành 0).

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^9$).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất sau khi đảo bit.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 | 2 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 10^9$.



### Bài 07 [CPPB-BIT-07]: Duyệt Toàn Bộ 2^N Tập Con Bằng Mặt Nạ Bit

**Bối cảnh:** Cho một tập hợp gồm $N$ số nguyên phân biệt. Hãy liệt kê tất cả $2^N$ tập con của tập hợp này theo thứ tự từ điển của mặt nạ bit (từ $0$ đến $2^N - 1$).

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 15$).
- Dòng 2: $N$ số nguyên $A_0, A_1, \dots, A_{N-1}$ ($|A_i| \le 10^9$).

**Đầu ra (Output):**

- In ra $2^N$ dòng. Mỗi dòng in ra các phần tử của tập con tương ứng, cách nhau bởi khoảng trắng (nếu là tập rỗng thì in dòng trống).

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 <br> 1 2 3 | 1 <br> 2 <br> 1 2 <br> 3 <br> 1 3 <br> 2 3 <br> 1 2 3 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 15$.



### Bài 08 [CPPB-BIT-08]: Bài Toán Tổng Tập Con Bằng S (Subset Sum)

**Bối cảnh:** Cho một dãy gồm $N$ số nguyên dương $A_1, A_2, \dots, A_N$ và một số nguyên dương $S$. Hãy kiểm tra xem có tồn tại một tập con các phần tử có tổng đúng bằng $S$ hay không.

**Đầu vào (Input):**

- Dòng 1: Gồm 2 số nguyên $N, S$ ($1 \le N \le 20, 1 \le S \le 10^9$).
- Dòng 2: $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^8$).

**Đầu ra (Output):**

- In ra `YES` nếu tồn tại, ngược lại in `NO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 12 <br> 3 34 4 12 5 | YES |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 20$.



### Bài 09 [CPPB-BIT-09]: Chia Tập Hợp Thành 2 Phần Có Tổng Chênh Lệch Nhỏ Nhất

**Bối cảnh:** Cho $N$ quả táo với khối lượng lần lượt là $P_1, P_2, \dots, P_N$. Bạn muốn chia $N$ quả táo này vào 2 giỏ sao cho độ chênh lệch khối lượng giữa 2 giỏ là **nhỏ nhất có thể**.

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 20$).
- Dòng 2: $N$ số nguyên dương $P_1, P_2, \dots, P_N$ ($1 \le P_i \le 10^9$).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là độ chênh lệch khối lượng nhỏ nhất tìm được.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 <br> 3 2 7 4 1 | 1 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 20, P_i \le 10^9$.



### Bài 10 [CPPB-BIT-10]: Đếm Cặp Có Tích Bit AND Bằng 0

**Bối cảnh:** Cho một dãy gồm $N$ số nguyên không âm $A_1, A_2, \dots, A_N$. Hãy đếm số lượng cặp chỉ số $(i, j)$ thỏa mãn $1 \le i < j \le N$ và $A_i \ \& \ A_j = 0$.

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên không âm $A_1, A_2, \dots, A_N$ ($0 \le A_i < 2^{12} = 4096$).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là số lượng cặp thỏa mãn.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 <br> 1 2 3 4 | 4 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 10^5, A_i < 4096$.



### Bài 11 [CPPB-BIT-11]: Tìm Cặp Có XOR Lớn Nhất Trong Mảng

**Bối cảnh:** Cho một mảng gồm $N$ số nguyên không âm $A_1, A_2, \dots, A_N$. Hãy tìm giá trị lớn nhất của biểu thức $A_i \oplus A_j$ với $1 \le i < j \le N$.

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $N$ ($2 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên không âm $A_1, A_2, \dots, A_N$ ($0 \le A_i \le 10^9$).

**Đầu ra (Output):**

- In ra giá trị XOR lớn nhất tìm được.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 <br> 3 10 5 25 | 28 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 10^5, A_i \le 10^9$.



### Bài 12 [CPPB-BIT-12]: Duyệt Tất Cả Các Tập Con Của Một Mặt Nạ Bit

**Bối cảnh:** Cho một số nguyên dương $N$ biểu diễn một mặt nạ bit. Hãy liệt kê tất cả các số nguyên $S > 0$ là tập con thực sự của $N$ (tức mọi bit 1 của $S$ đều là bit 1 của $N$) theo thứ tự giảm dần.

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^9$).

**Đầu ra (Output):**

- In ra tất cả các submask dương của $N$ trên một dòng, cách nhau bởi khoảng trắng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 11 | 11 10 9 8 3 2 1 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 10^9$.



### Bài 13 [CPPB-BIT-13]: Tìm Dãy Con Có Tổng XOR Bằng K

**Bối cảnh:** Cho một tập hợp gồm $N$ số nguyên dương $A_1, A_2, \dots, A_N$ và một số nguyên $K$. Hãy đếm số lượng tập con khác rỗng có tích XOR của tất cả các phần tử đúng bằng $K$.

**Đầu vào (Input):**

- Dòng 1: Gồm 2 số nguyên $N, K$ ($1 \le N \le 20, 0 \le K \le 10^9$).
- Dòng 2: $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là số lượng tập con thỏa mãn.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 3 <br> 1 2 3 | 2 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 20$.



### Bài 14 [CPPB-BIT-14]: Tối Ưu Hóa Gán Việc Cho N Người (N <= 20)

**Bối cảnh:** Có $N$ công việc và $N$ nhân viên ($N \le 16$). Ma trận $C_{i, j}$ biểu diễn chi phí nếu giao công việc $i$ cho nhân viên $j$. Mỗi nhân viên chỉ làm đúng 1 việc, và mỗi công việc chỉ giao cho đúng 1 nhân viên.

**Nhiệm vụ:** Hãy tìm phương án phân công công việc sao cho **tổng chi phí là nhỏ nhất có thể**.

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 16$).
- $N$ dòng tiếp theo: Mỗi dòng gồm $N$ số nguyên $C_{i, j}$ ($0 \le C_{i, j} \le 10^6$).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là tổng chi phí tối thiểu.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 <br> 3 2 7 <br> 5 1 3 <br> 2 7 2 | 6 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 16, C_{i,j} \le 10^6$.



### Bài 15 [CPPB-BIT-15]: Đếm Số Cặp Có Tổng Bằng Lũy Thừa Của 2

**Bối cảnh:** Cho một dãy gồm $N$ số nguyên dương $A_1, A_2, \dots, A_N$. Hãy đếm số lượng cặp chỉ số $(i, j)$ thỏa mãn $1 \le i < j \le N$ sao cho tổng $A_i + A_j$ là một lũy thừa của 2 (tức $A_i + A_j = 2^k$ với $k \ge 1$).

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là số lượng cặp thỏa mãn.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 <br> 1 3 7 15 | 3 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 10^5, A_i \le 10^9$.



### Bài 16 [CPPB-BIT-16]: Tập Hợp Độc Lập Về Bit Lớn Nhất

**Bối cảnh:** Cho một tập hợp gồm $N$ số nguyên dương $A_0, A_1, \dots, A_{N-1}$ ($N \le 22$). Hãy tìm kích thước của tập hợp con lớn nhất sao cho hai phần tử bất kỳ $A_i, A_j$ trong tập con đều **không có chung bất kỳ bit 1 nào** (tức $A_i \ \& \ A_j = 0$).

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 22$).
- Dòng 2: $N$ số nguyên dương $A_0, A_1, \dots, A_{N-1}$ ($1 \le A_i \le 10^9$).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là kích thước lớn nhất của tập con độc lập về bit.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 <br> 1 2 4 3 | 3 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 22, A_i \le 10^9$.



# CHƯƠNG 03: SỐ HỌC & ĐẠI SỐ MODULAR


# Bài 07: Lý thuyết số & số nguyên tố

## 1. Bản chất vấn đề & trực giác thuật toán (the core problem & intuition)

Trong khoa học máy tính và lập trình thi đấu, các bài toán xoay quanh **ước số, bội số và số nguyên tố** là nền tảng của mật mã học (như thuật toán mã hóa khóa công khai RSA), phân tích độ phức tạp thuật toán và tối ưu hóa tài nguyên.

### Vấn đề 1: Tìm ước chung lớn nhất (GCD)
Cho hai số nguyên dương $A$ và $B$. Ước chung lớn nhất $\gcd(A, B)$ là số nguyên dương lớn nhất đồng thời chia hết cả $A$ và $B$.

* **Cách ngây thơ:** Thử tất cả các số từ $\min(A, B)$ giảm dần về $1 \implies \mathcal{O}(\min(A, B))$. Khi $A, B \approx 10^{18}$, cách này hoàn toàn bất khả thi.
* **Định lý Euclid:** $\gcd(A, B) = \gcd(B, A \pmod B)$.
* Mỗi bước lấy dư $A \pmod B$, giá trị giảm ít nhất một nửa sau mỗi 2 bước lặp $\implies$ Thuật toán dừng lại sau tối đa $\mathcal{O}(\log(\min(A, B)))$ bước (khoảng $\le 60$ phép tính với số $10^{18}$).

### Vấn đề 2: Kiểm tra số nguyên tố & phân tích thừa số nguyên tố
Một số nguyên $N > 1$ là số nguyên tố nếu nó chỉ có đúng 2 ước là $1$ và chính nó.

* **Tính chất đối xứng của ước số:** Nếu $d$ là ước của $N$ thì $\frac{N}{d}$ cũng là ước của $N$.
* **Bất biến $\sqrt{N}$:** Nếu $N$ là hợp số, nó **bắt buộc phải có ít nhất một ước nguyên tố $p \le \sqrt{N}$**. Do đó, ta chỉ cần duyệt kiểm tra các số từ $2$ đến $\lfloor \sqrt{N} \rfloor$ trong $\mathcal{O}(\sqrt{N})$ thay vì $\mathcal{O}(N)$.

## 2. Mô phỏng từng bước (visual step-by-step simulation)

### Ví dụ 1: Mô phỏng thuật toán euclid tìm $\gcd(252, 105)$

| Bước lặp | $A$ | $B$ | Phép chia lấy dư $A \pmod B$ | Trạng thái tiếp theo $(A', B') = (B, A \pmod B)$ |
|:---:|:---:|:---:|:---:|:---:|
| **1** | $252$ | $105$ | $252 \pmod{105} = 42$ | $(105, 42)$ |
| **2** | $105$ | $42$ | $105 \pmod{42} = 21$ | $(42, 21)$ |
| **3** | $42$ | $21$ | $42 \pmod{21} = 0$ | $(21, 0)$ |
| **Kết thúc** | $21$ | $0$ | $B = 0 \implies \text{Dừng}$ | **$\gcd(252, 105) = 21$** |

### Ví dụ 2: Mô phỏng sàng Eratosthenes tìm các số nguyên tố $\le 20$

1. Khởi tạo mảng đánh dấu `isPrime` từ $2 \dots 20$ đều là `true`.
2. Xét $i = 2$ (nguyên tố) $\implies$ Gạch bỏ các bội $4, 6, 8, 10, 12, 14, 16, 18, 20$.
3. Xét $i = 3$ (nguyên tố) $\implies$ Gạch bỏ các bội $9, 12, 15, 18$ (bắt đầu gạch từ $i^2 = 9$).
4. Xét $i = 4$ (đã bị gạch) $\implies$ Bỏ qua.
5. Vì $i^2 = 5^2 = 25 > 20$, vòng lặp dừng lại.



![Mô phỏng sàng Eratosthenes tìm số nguyên tố từ 2 đến 20](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-07-uoc-boi-so-nguyen-to/assets/sieve_eratosthenes_simulation_vi.png)



> **Danh sách số nguyên tố $\le 20$:** $\{2, 3, 5, 7, 11, 13, 17, 19\}$ (gồm 8 số).

## 3. Lý thuyết cốt lõi & bất biến toán học (core invariants)

### 3.1. Mối quan hệ giữa GCD và LCM
$$\gcd(A, B) \times \text{lcm}(A, B) = A \times B \implies \text{lcm}(A, B) = \frac{A}{\gcd(A, B)} \times B$$

### Cảnh báo quan trọng:
**Bẫy Lỗi TRÀN SỐ KHI TÍNH BỘI CHUNG NHỎ NHẤT (LCM):**

> * Không viết `(A * B) / gcd(A, B)` vì tích $A \times B$ có thể lên tới $10^{36}$ gây tràn số `long long`.
> * Luôn viết: `long long lcm = (a / gcd(a, b)) * b;`

> * **Lưu ý chuyên sâu:** Việc chia trước giúp triệt tiêu nguy cơ tràn số ở bước trung gian; tuy nhiên, nếu bản thân giá trị $\text{lcm}(A, B)$ thực tế vượt quá $9 \cdot 10^{18}$ (giới hạn của `long long`), ta bắt buộc phải sử dụng `__int128` hoặc kiểu dữ liệu số lớn (Big Integer).

### 3.2. Định lý cơ bản của số học & công thức nhân tính
Mọi số nguyên $N > 1$ đều phân tích duy nhất thành tích các thừa số nguyên tố:

$$N = p_1^{a_1} \times p_2^{a_2} \times \dots \times p_k^{a_k}$$

* **Số lượng ước số của $N$ ($\sigma_0(N)$):**
$$\text{d}(N) = (a_1 + 1)(a_2 + 1)\dots(a_k + 1)$$

* **Tổng các ước số của $N$ ($\sigma_1(N)$):**
$$\sigma(N) = \frac{p_1^{a_1+1} - 1}{p_1 - 1} \times \frac{p_2^{a_2+1} - 1}{p_2 - 1} \times \dots \times \frac{p_k^{a_k+1} - 1}{p_k - 1}$$

### 3.3. Sàng ước nguyên tố nhỏ nhất (spf - Smallest prime factor)
Thay vì chỉ lưu mảng `bool`, ta lưu mảng `spf[x]` là **ước số nguyên tố nhỏ nhất của $x$**.

* Phân tích thừa số nguyên tố bằng SPF cần tối đa $\mathcal{O}(\log X)$ lần chia liên tiếp, giúp trả lời cực nhanh cho hàng trăm nghìn truy vấn độc lập.

### 3.4. Phi hàm Euler (Euler's totient function $\phi(N)$)
Phi hàm Euler $\phi(N)$ đếm số lượng số nguyên dương trong đoạn $[1, N]$ nguyên tố cùng nhau với $N$ ($\gcd(k, N) = 1$):
$$\phi(N) = N \times \left(1 - \frac{1}{p_1}\right) \times \left(1 - \frac{1}{p_2}\right) \dots \left(1 - \frac{1}{p_k}\right)$$

* **Tính chất bất biến:** $\sum_{d | N} \phi(d) = N$.
* **Sàng Phi hàm Euler trong $\mathcal{O}(N \log \log N)$:** Cho phép tính $\phi(1) \dots \phi(N)$ đồng thời trên mảng, dùng để đếm tổng số cặp số $(x, y) \le N$ thỏa mãn $\gcd(x, y) = 1$ qua công thức $2 \sum_{i=1}^N \phi(i) - 1$.

## 4. Các bẫy lỗi lập trình kinh điển (bug traps)

1. **Tràn số khi so sánh vòng lặp căn bậc hai:**
* Viết `for (int i = 2; i * i <= n; ++i)` sẽ bị tràn số số nguyên 32-bit nếu $i \approx 46341 \implies i^2 < 0$ dẫn đến vòng lặp vô tận (TLE).
* **Cách sửa:** Dùng `1LL * i * i <= n` hoặc `i <= n / i`.

2. **Quên xử lý phần dư cuối cùng sau khi phân tích $\mathcal{O}(\sqrt{N})$:**
* Sau khi chia triệt để cho các ước nguyên tố $p \le \sqrt{N}$, nếu $N > 1$ thì giá trị còn lại của $N$ **chắc chắn là một số nguyên tố lớn hơn $\sqrt{N}$**. Nếu bỏ qua bước này sẽ thiếu thừa số cuối cùng.

3. **Số $0$ và số $1$ không phải là số nguyên tố:**
* Hàm kiểm tra số nguyên tố bắt buộc phải kiểm tra `if (n < 2) return false;`.

## 5. Mẫu cài đặt chuẩn thi đấu (competitive templates)

### Mẫu 1: Ước chung lớn nhất & bội chung nhỏ nhất
```cpp
# include <bits/stdc++.h>
using namespace std;

// GCD bằng thuật toán Euclid lặp O(log(min(A, B)))
long long getGcd(long long a, long long b) {
    while (b != 0) {
        long long r = a % b;
        a = b;
        b = r;
    }
    return a;
}

// LCM an toàn chống tràn số
long long getLcm(long long a, long long b) {
    if (a == 0 || b == 0) return 0;
    return (a / getGcd(a, b)) * b;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, b;
    if (!(cin >> a >> b)) return 0;

    cout << getGcd(a, b) << " " << getLcm(a, b) << "\n";
    return 0;
}
```

### Mẫu 2: Sàng Eratosthenes & sàng spf (tối ưu phân tích thừa số)
```cpp
# include <bits/stdc++.h>
using namespace std;

const int MAXN = 1000000;
vector<int> spf(MAXN + 1);

// Tiền xử lý Sàng SPF trong O(N log log N)
void sieveSPF() {
    for (int i = 1; i <= MAXN; ++i) spf[i] = i;
    for (int i = 2; 1LL * i * i <= MAXN; ++i) {
        if (spf[i] == i) { // i là số nguyên tố
            for (int j = i * i; j <= MAXN; j += i) {
                if (spf[j] == j) {
                    spf[j] = i;
                }
            }
        }
    }
}

// Phân tích thừa số nguyên tố O(log N) cho mỗi truy vấn
vector<pair<int, int>> factorize(int n) {

    vector<pair<int, int>> factors;

    while (n > 1) {

        int p = spf[n];
        int count = 0;
        while (n % p == 0) {
            count++;
            n /= p;
        }
        factors.push_back({p, count});
    }
    return factors;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    sieveSPF();

    int q;
    if (!(cin >> q)) return 0;

    while (q--) {
        int n;
        cin >> n;

        auto factors = factorize(n);
        for (int i = 0; i < (int)factors.size(); ++i) {
            cout << factors[i].first << "^" << factors[i].second << (i + 1 == (int)factors.size() ? "" : " * ");
        }
        cout << "\n";
    }
    return 0;
}
```

## Bài tập thực hành


### Bài 01 [CPPB-NT-01]: Ước Chung Lớn Nhất & Bội Chung Nhỏ Nhất

**Bối cảnh:** Cho hai số nguyên dương $A$ và $B$. Hãy tìm ước chung lớn nhất $\gcd(A, B)$ và bội chung nhỏ nhất $\text{lcm}(A, B)$ của chúng.

**Đầu vào (Input):**

- Một dòng duy nhất chứa 2 số nguyên dương $A$ và $B$ ($1 \le A, B \le 10^{12}$).

**Đầu ra (Output):**

- In ra trên một dòng 2 số nguyên cách nhau bởi dấu cách lần lượt là $\gcd(A, B)$ và $\text{lcm}(A, B)$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 12 18 | 6 36 |



### Bài 02 [CPPB-NT-02]: Kiểm Tra Số Nguyên Tố Cơ Bản

**Bối cảnh:** Cho một số nguyên dương $N$. Hãy xác định xem $N$ có phải là số nguyên tố hay không.

**Đầu vào (Input):**

- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10^{12}$).

**Đầu ra (Output):**

- In ra `YES` nếu $N$ là số nguyên tố, ngược lại in ra `NO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 29 | YES |



### Bài 03 [CPPB-NT-03]: Phân Tích Thừa Số Nguyên Tố

**Bối cảnh:** Cho số nguyên dương $N$. Hãy phân tích $N$ thành tích các thừa số nguyên tố theo dạng $p_1^{a_1} \times p_2^{a_2} \dots$.

**Đầu vào (Input):**

- Một dòng duy nhất chứa số nguyên dương $N$ ($2 \le N \le 10^{12}$).

**Đầu ra (Output):**

- In ra phân tích thừa số nguyên tố của $N$ theo thứ tự tăng dần của các ước nguyên tố theo định dạng `p^a`. Nếu $a=1$ vẫn in `p^1`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 60 | 2^2 * 3^1 * 5^1 |



### Bài 04 [CPPB-NT-04]: Đếm Số Lượng & Tính Tổng Các Ước Số

**Bối cảnh:** Cho số nguyên dương $N$. Hãy tính số lượng ước số nguyên dương $d(N)$ và tổng tất cả các ước số $\sigma(N)$ của $N$.

**Đầu vào (Input):**

- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10^{12}$).

**Đầu ra (Output):**

- In ra trên một dòng 2 số nguyên là số lượng ước và tổng ước của $N$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 12 | 6 28 |



### Bài 05 [CPPB-NT-05]: Kiểm Tra Số Chính Phương

**Bối cảnh:** Cho số nguyên dương $N$. Hãy kiểm tra xem $N$ có phải là số chính phương ($N = k^2$) hay không.

**Đầu vào (Input):**

- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10^{18}$).

**Đầu ra (Output):**

- In ra `YES` nếu $N$ là số chính phương, ngược lại in ra `NO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 49 | YES |



### Bài 06 [CPPB-NT-06]: Sàng Nguyên Tố Eratosthenes

**Bối cảnh:** Cho số nguyên dương $N$. Hãy in ra tất cả các số nguyên tố không vượt quá $N$ theo thứ tự tăng dần.

**Đầu vào (Input):**

- Một dòng duy nhất chứa số nguyên dương $N$ ($2 \le N \le 10^7$).

**Đầu ra (Output):**

- In ra các số nguyên tố $\le N$ trên một dòng, cách nhau bởi dấu cách.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 20 | 2 3 5 7 11 13 17 19 |



### Bài 07 [CPPB-NT-07]: Đếm Số Nguyên Tố Trong Đoạn [L, R]

**Bối cảnh:** Cho $Q$ truy vấn, mỗi truy vấn gồm 2 số nguyên $L, R$. Hãy đếm số lượng số nguyên tố trong đoạn $[L, R]$.

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $Q$ ($1 \le Q \le 10^5$).\n- $Q$ dòng tiếp theo: Mỗi dòng chứa 2 số nguyên $L, R$ ($1 \le L \le R \le 10^6$).

**Đầu ra (Output):**

- In ra $Q$ dòng, mỗi dòng là số lượng số nguyên tố tương ứng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3\n1 10\n11 20\n1 20 | 4\n4\n8 |



### Bài 08 [CPPB-NT-08]: Sàng Ước Nguyên Tố Nhỏ Nhất (SPF)

**Bối cảnh:** Cho $Q$ truy vấn, mỗi truy vấn chứa một số nguyên $N$. Hãy in ra ước số nguyên tố nhỏ nhất của $N$.

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $Q$ ($1 \le Q \le 10^5$).\n- Dòng 2: $Q$ số nguyên $N_1, N_2, \dots, N_Q$ ($2 \le N_i \le 10^6$).

**Đầu ra (Output):**

- In ra $Q$ số nguyên là ước nguyên tố nhỏ nhất tương ứng trên một dòng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4\n15 49 13 100 | 3 7 13 2 |



### Bài 09 [CPPB-NT-09]: Sàng Phân Đoạn (Segmented Sieve)

**Bối cảnh:** Cho hai số nguyên $L, R$. Hãy đếm số lượng số nguyên tố trong đoạn $[L, R]$.

**Đầu vào (Input):**

- Một dòng duy nhất chứa 2 số nguyên $L, R$ ($1 \le L \le R \le 10^{12}, R - L \le 10^6$).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là số lượng số nguyên tố.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 100 120 | 5 |



### Bài 10 [CPPB-NT-10]: Cặp Số Nguyên Tố Sinh Đôi (Twin Primes)

**Bối cảnh:** Một cặp số $(p, p+2)$ được gọi là số nguyên tố sinh đôi nếu cả $p$ và $p+2$ đều là số nguyên tố. Cho số nguyên $N$, hãy đếm số lượng cặp nguyên tố sinh đôi mà $p+2 \le N$.

**Đầu vào (Input):**

- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10^7$).

**Đầu ra (Output):**

- In ra một số nguyên là số lượng cặp nguyên tố sinh đôi.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 20 | 4 |



### Bài 11 [CPPB-NT-11]: Kiểm Tra Số Hoàn Hảo

**Bối cảnh:** Một số nguyên dương $N$ được gọi là số hoàn hảo nếu tổng tất cả các ước số thực sự của nó (không kể chính nó) bằng $N$. Cho số $N$, hãy kiểm tra $N$ có phải số hoàn hảo.

**Đầu vào (Input):**

- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10^{18}$).

**Đầu ra (Output):**

- In ra `YES` nếu $N$ là số hoàn hảo, ngược lại in `NO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 28 | YES |



### Bài 12 [CPPB-NT-12]: Số Có Đúng 3 Ước Số

**Bối cảnh:** Cho số nguyên dương $N$. Hãy đếm số lượng số nguyên dương $\le N$ có đúng 3 ước số nguyên dương phân biệt.

**Đầu vào (Input):**

- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10^{12}$).

**Đầu ra (Output):**

- In ra một số nguyên là số lượng số có đúng 3 ước.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 50 | 4 |



### Bài 13 [CPPB-NT-13]: Số Gần Nguyên Tố (Almost Prime)

**Bối cảnh:** Một số nguyên dương được gọi là 'gần nguyên tố' nếu nó có đúng 2 ước nguyên tố phân biệt. Cho số $N$, hãy đếm số lượng số gần nguyên tố $\le N$.

**Đầu vào (Input):**

- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10^7$).

**Đầu ra (Output):**

- In ra số lượng số gần nguyên tố $\le N$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 10 | 2 |



### Bài 14 [CPPB-NT-14]: Phân Tích Giai Thừa Ra Thừa Số (Định Lý Legendre)

**Bối cảnh:** Cho số nguyên $N$ và số nguyên tố $P$. Hãy tìm số mũ lớn nhất $K$ sao cho $N!$ chia hết cho $P^K$.

**Đầu vào (Input):**

- Một dòng duy nhất chứa 2 số nguyên $N$ và $P$ ($1 \le N \le 10^{18}, 2 \le P \le 10^6$, $P$ là số nguyên tố).

**Đầu ra (Output):**

- In ra một số nguyên $K$ là số mũ tìm được.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 10 3 | 4 |



### Bài 15 [CPPB-NT-15]: Đếm Số Lượng Số Không Tận Cùng Của N!

**Bối cảnh:** Cho số nguyên dương $N$. Hãy đếm số lượng chữ số $0$ liên tiếp tận cùng trong biểu diễn thập phân của $N!$.

**Đầu vào (Input):**

- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10^{18}$).

**Đầu ra (Output):**

- In ra số lượng chữ số 0 tận cùng của $N!$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 100 | 24 |



### Bài 16 [CPPB-NT-16]: Số Học Cực Hạn: Cặp Nguyên Tố Cùng Nhau & Phi Hàm Euler

**Bối cảnh:** Cho số nguyên dương $N$. Hãy đếm số lượng cặp số nguyên $(x, y)$ thỏa mãn $1 \le x, y \le N$ và $\gcd(x, y) = 1$.

**Đầu vào (Input):**

- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10^6$).

**Đầu ra (Output):**

- In ra tổng số lượng cặp $(x, y)$ nguyên tố cùng nhau.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 | 7 |




# Bài 08: Đồng dư thức, lũy thừa nhị phân & nghịch đảo modulo

## 1. Bản chất vấn đề & trực giác thuật toán (the core problem & intuition)

Trong nhiều bài toán lập trình và thi đấu thuật toán, kết quả tính toán hoặc số cách đếm tổ hợp thường tăng rất nhanh và vượt quá giới hạn lưu trữ của kiểu số nguyên 64-bit (`long long`). Để tránh việc phải xử lý số lớn phức tạp, đề bài thường yêu cầu: **"In ra kết quả sau khi chia lấy dư cho $M$"** (thông thường $M = 10^9 + 7$ hoặc $998244353$ — là các số nguyên tố lớn).

Từ yêu cầu thực tế này, bộ ba kỹ thuật nền tảng được hình thành:
$\text{Đồng Dư Cơ Bản (+, -, *)} \longrightarrow \text{Lũy Thừa Nhị Phân } \mathcal{O}(\log B) \longrightarrow \text{Nghịch Đảo Modulo } (B^{-1})$

### Vấn đề 1: Phép tính lũy thừa $A^B \pmod M$

* **Cách ngây thơ:** Nhân $B$ lần liên tiếp: $A \times A \times \dots \times A \implies \mathcal{O}(B)$. Khi $B = 10^{18}$, cách này hoàn toàn bất khả thi.
* **Trực giác Chia để trị (Binary Exponentiation):**
* Nếu $B$ chẵn: $A^B = (A^2)^{B / 2} = (A^{B / 2})^2$.
* Nếu $B$ lẻ: $A^B = A \times A^{B - 1}$.
* Sau mỗi bước, số mũ $B$ giảm đi một nửa $\implies$ Số phép nhân chỉ còn $\mathcal{O}(\log_2 B)$ (chưa tới $60$ phép tính với $B = 10^{18}$).

### Vấn đề 2: Phép chia trên vành modulo $\left(\frac{A}{B} \pmod M\right)$

* Trong số học đồng dư, **không thể thực hiện phép chia bằng phép chia số nguyên thông thường** (tức $\frac{A}{B} \pmod M \not\equiv \frac{A \pmod M}{B \pmod M}$).
* **Nghịch đảo Modulo ($B^{-1}$):** Muốn tính $\frac{A}{B} \pmod M$, ta chuyển phép chia thành phép nhân với nghịch đảo modulo $B^{-1}$ (nếu nghịch đảo tồn tại):
$$\frac{A}{B} \pmod M \equiv (A \times B^{-1}) \pmod M$$
với $B^{-1}$ là số nguyên thỏa mãn: $(B \times B^{-1}) \equiv 1 \pmod M$.

## 2. Mô phỏng từng bước (visual step-by-step simulation)

### Ví dụ 1: Mô phỏng tính $3^{13} \pmod{1000}$ bằng lũy thừa nhị phân

Biểu diễn nhị phân của số mũ $13 = 1101_2 = 8 + 4 + 1$.
Do đó: $3^{13} = 3^8 \times 3^4 \times 3^1$.

| Bước lặp | Số mũ $B$ | Trạng thái ($B$ chẵn hay lẻ) | Cơ số $A$ ($A \gets A^2 \pmod M$) | Kết quả tích lũy $ans$ ($ans \gets ans \times A \pmod M$) |
|:---:|:---:|:---:|:---:|:---:|
| **Khởi tạo** | $13$ | Lẻ (bit $0 = 1$) | $A = 3$ | $ans = 1 \times 3 = 3$ |
| **1** | $6$ | Chẵn (bit $1 = 0$) | $A \gets 3^2 = 9$ | $ans = 3$ (không nhân) |
| **2** | $3$ | Lẻ (bit $2 = 1$) | $A \gets 9^2 = 81$ | $ans \gets (3 \times 81) = 243$ |
| **3** | $1$ | Lẻ (bit $3 = 1$) | $A \gets 81^2 = 6561 \equiv 561$ | $ans \gets (243 \times 561) \pmod{1000} = \mathbf{323}$ |
| **Kết thúc** | $0$ | Dừng | — | **Đáp án:** $3^{13} \pmod{1000} = \mathbf{323}$ (vì $3^{13} = 1594323$) |

### Ví dụ 2: Mô phỏng tìm nghịch đảo modulo của $3 \pmod 7$
Ta cần tìm số nguyên $X \in \{1, \dots, 6\}$ sao cho $(3 \times X) \pmod 7 = 1$.

| Thử giá trị $X$ | Phép nhân $3 \times X$ | Lấy dư $(3 \times X) \pmod 7$ | Kết luận |
|:---:|:---:|:---:|:---:|
| $X = 1$ | $3 \times 1 = 3$ | $3$ | Không thỏa mãn |
| $X = 2$ | $3 \times 2 = 6$ | $6$ | Không thỏa mãn |
| $X = 3$ | $3 \times 3 = 9$ | $2$ | Không thỏa mãn |
| $X = 4$ | $3 \times 4 = 12$ | $5$ | Không thỏa mãn |
| **$X = 5$** | $3 \times 5 = 15$ | **$1$** | **$3^{-1} \equiv 5 \pmod 7$ (Thỏa mãn)** |

> **Kiểm chứng bằng Định lý Fermat nhỏ:** $3^{7-2} = 3^5 = 243 \equiv 5 \pmod 7$.

## 3. Lý thuyết cốt lõi & bất biến toán học (core invariants)

### 3.1. Các quy tắc đồng dư cơ bản (+, -, \*)

1. **Phép Cộng:** $(A + B) \pmod M = ((A \pmod M) + (B \pmod M)) \pmod M$.
2. **Phép Trừ (Tránh số âm):** $(A - B) \pmod M = ((A \pmod M) - (B \pmod M) + M) \pmod M$.
3. **Phép Nhân:** $(A \times B) \pmod M = ((A \pmod M) \times (B \pmod M)) \pmod M$.

### Cảnh báo quan trọng:
**2 Bẫy Lỗi KHI THỰC HIỆN PHÉP TOÁN ĐỒNG DƯ:**

> 1. **Số dư âm trong C++:** Trong C++, phép toán `-7 % 5` trả về `-2` (không phải `3`). Để luôn nhận kết quả không âm, bắt buộc phải viết: `(a % m + m) % m`.
> 2. **Tràn số 32-bit khi nhân:** Nếu $A, B \approx 10^9$, tích $A \times B \approx 10^{18}$ vượt giới hạn kiểu `int`. Bắt buộc phải ép kiểu 64-bit trước khi nhân: `(1LL * a * b) % m`.

### 3.2. Định lý Fermat nhỏ & nghịch đảo modulo
Nếu $M$ là một **số nguyên tố** và $A$ không chia hết cho $M$ ($\gcd(A, M) = 1$), thì:
$$A^{M - 1} \equiv 1 \pmod M \implies A \times A^{M - 2} \equiv 1 \pmod M$$

$$\implies \mathbf{A^{-1} \equiv A^{M - 2} \pmod M}$$

Ta có thể tính $A^{-1} \pmod M$ chỉ bằng một hàm Lũy thừa nhị phân: `power(A, M - 2, M)` trong $\mathcal{O}(\log M)$.

### Chú ý:
**ĐIỀU KIỆN TIÊN QUYẾT CỦA ĐỊNH LÝ FERMAT NHỎ:**

> * Quy tắc $A^{M - 1} \equiv 1 \pmod M$ và việc rút gọn số mũ $B \gets B \pmod{(M - 1)}$ **CHỈ ĐÚNG KHI $M$ LÀ SỐ NGUYÊN TỐ VÀ $\gcd(A, M) = 1$**.
> * Tuyệt đối không tùy tiện áp dụng nếu $A$ chia hết cho $M$ hoặc $M$ là hợp số.

### 3.3. Thuật toán euclid mở rộng (extended euclidean algorithm)
Khi $M$ **không phải là số nguyên tố** (nhưng $\gcd(A, M) = 1$), định lý Fermat nhỏ không áp dụng được. Ta dùng thuật toán Euclid mở rộng để giải phương trình nghiệm nguyên:
$$A \times x + M \times y = \gcd(A, M) = 1$$
Khi đó, $x \pmod M$ chính là nghịch đảo modulo $A^{-1}$.

### 3.4. Tính tổ hợp $C(N, K) \pmod M$ trong $\mathcal{O}(1)$ mỗi truy vấn
Công thức số tổ hợp chập $K$ của $N$:
$$C(N, K) = \frac{N!}{K! \times (N - K)!} \equiv N! \times (K!)^{-1} \times ((N - K)!)^{-1} \pmod M$$

* **Tiền xử lý trong $\mathcal{O}(N)$:**
1. Tính mảng giai thừa: `fact[i] = (fact[i-1] * i) % M`.
2. Tính mảng nghịch đảo giai thừa: `invFact[N] = power(fact[N], M - 2, M)`, sau đó đi ngược về 0: `invFact[i - 1] = (invFact[i] * i) % M`.
* **Trả lời mỗi truy vấn trong $\mathcal{O}(1)$:**
$$C(N, K) = \text{fact}[N] \times \text{invFact}[K] \pmod M \times \text{invFact}[N - K] \pmod M$$

### 3.5. Tính tổng cấp số nhân modulo bằng chia để trị
Cần tính tổng:
$$S_N = 1 + A + A^2 + \dots + A^N \pmod M$$

* **Trường hợp cơ sở:** Nếu $N = 0 \implies S_0 = 1$.
* **Nếu $N$ lẻ (Tổng có $N + 1$ số hạng chẵn):**
$$S_N = (1 + A + \dots + A^{(N-1)/2}) + A^{(N+1)/2} (1 + A + \dots + A^{(N-1)/2})$$
$$S_N = S_{(N-1)/2} \times \left(1 + A^{(N+1)/2}\right) \pmod M$$

* **Nếu $N$ chẵn:** Tách riêng số hạng cuối cùng:
$$S_N = 1 + A \times S_{N-1} \pmod M$$

* **Độ phức tạp:** $\mathcal{O}(\log^2 N)$ hoặc $\mathcal{O}(\log N)$, mở đường cho kỹ thuật nhân lũy thừa ma trận và quy hoạch động cấu trúc đại số.

## 4. Các bẫy lỗi lập trình kinh điển (bug traps)

1. **Chia trực tiếp trên Modulo:**
* Viết `((A % M) / (B % M)) % M` là **HOÀN TOÀN SAI BẢN CHẤT TOÁN HỌC**. Phép chia bắt buộc phải chuyển thành nhân với nghịch đảo: `(A * inverse(B)) % M`.
2. **Quên xử lý trường hợp $K > N$ hoặc $K < 0$ khi tính tổ hợp:**

* $C(N, K) = 0$ khi $K < 0$ hoặc $K > N$. Nếu không kiểm tra sẽ bị truy cập ô nhớ âm hoặc rác.

3. **Trường hợp $M = 1$:**
* $A^B \pmod 1$ luôn bằng $0$. Hàm lũy thừa cần trả về `0` khi $M = 1$.

## 5. Mẫu cài đặt chuẩn thi đấu (competitive templates)

### Mẫu 1: Lũy thừa nhị phân & nghịch đảo modulo chuẩn
```cpp
# include <bits/stdc++.h>
using namespace std;

// Tính (a^b) % m trong O(log b)
long long powerMod(long long a, long long b, long long m) {
    if (m == 1) return 0;
    long long ans = 1 % m;
    a %= m;
    while (b > 0) {

        if (b & 1) ans = (ans * a) % m;
        a = (a * a) % m;
        b >>= 1;
    }
    return ans;
}

// Nghịch đảo Modulo bằng Định lý Fermat nhỏ (khi m là số nguyên tố)
long long modInversePrime(long long a, long long m) {
    return powerMod(a, m - 2, m);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, b, m;
    if (!(cin >> a >> b >> m)) return 0;

    cout << powerMod(a, b, m) << "\n";
    return 0;
}
```

### Mẫu 2: Tiền xử lý tổ hợp $C(N, K) \pmod M$ trong $\mathcal{O}(1)$ mỗi truy vấn
```cpp
# include <bits/stdc++.h>
using namespace std;

const int MAXN = 1000000;
const long long MOD = 1000000007;

vector<long long> fact(MAXN + 1);

vector<long long> invFact(MAXN + 1);

long long powerMod(long long a, long long b, long long m) {
    long long ans = 1;
    a %= m;
    while (b > 0) {

        if (b & 1) ans = (ans * a) % m;
        a = (a * a) % m;
        b >>= 1;
    }
    return ans;
}

void precomputeCombinatorics() {
    fact[0] = 1;
    for (int i = 1; i <= MAXN; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    invFact[MAXN] = powerMod(fact[MAXN], MOD - 2, MOD);
    for (int i = MAXN; i >= 1; --i) {
        invFact[i - 1] = (invFact[i] * i) % MOD;
    }
}

long long nCr(int n, int r) {
    if (r < 0 || r > n) return 0;

    return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    precomputeCombinatorics();

    int q;
    if (!(cin >> q)) return 0;

    while (q--) {
        int n, r;
        cin >> n >> r;

        cout << nCr(n, r) << "\n";
    }
    return 0;
}
```

## Bài tập thực hành


### Bài 01 [CPPB-MOD-01]: Phép Tính Đồng Dư Cơ Bản (+, -, *)

**Bối cảnh:** Cho 2 số nguyên $A, B$ và số nguyên dương $M = 10^9 + 7$. Hãy tính $(A + B) \pmod M$, $(A - B) \pmod M$ và $(A \times B) \pmod M$ sao cho kết quả luôn thuộc $[0, M - 1]$.

**Đầu vào (Input):**

- Một dòng duy nhất chứa 2 số nguyên $A, B$ ($0 \le A, B \le 10^{18}$).

**Đầu ra (Output):**

- In ra 3 số nguyên cách nhau bởi dấu cách lần lượt là $(A + B) \pmod M$, $(A - B) \pmod M$ và $(A \times B) \pmod M$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 1000000008 3 | 4 1000000005 3 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $A, B \le 10^{18}$.



### Bài 02 [CPPB-MOD-10]: Tính Số Chỉnh Hợp A(N, K) mod M

**Bối cảnh:** Cho $Q$ truy vấn, mỗi truy vấn chứa 2 số $N, K$. Hãy tính số chỉnh hợp $A(N, K) = \frac{N!}{(N - K)!} \pmod{10^9 + 7}$.

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $Q$ ($1 \le Q \le 10^5$).
- $Q$ dòng tiếp theo: Mỗi dòng chứa 2 số $N, K$ ($0 \le K \le N \le 10^6$).

**Đầu ra (Output):**

- In ra $Q$ dòng tương ứng là $A(N, K) \pmod{10^9 + 7}$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 2 <br> 4 2 <br> 5 3 | 12 <br> 60 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $Q \le 10^5, N \le 10^6$.



### Bài 03 [CPPB-MOD-01]: Phép Tính Đồng Dư Cơ Bản (+, -, *)

**Bối cảnh:** Cho 2 số nguyên $A, B$ và số nguyên dương $M = 10^9 + 7$. Hãy tính $(A + B) \pmod M$, $(A - B) \pmod M$ và $(A \times B) \pmod M$ sao cho kết quả luôn thuộc $[0, M - 1]$.

**Đầu vào (Input):**

- Một dòng duy nhất chứa 2 số nguyên $A, B$ ($0 \le A, B \le 10^{18}$).

**Đầu ra (Output):**

- In ra 3 số nguyên cách nhau bởi dấu cách lần lượt là $(A + B) \pmod M$, $(A - B) \pmod M$ và $(A \times B) \pmod M$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 1000000008 3 | 4 1000000005 3 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $A, B \le 10^{18}$.



### Bài 04 [CPPB-MOD-02]: Lũy Thừa Nhị Phân Cơ Bản

**Bối cảnh:** Cho 3 số nguyên $A, B, M$. Hãy tính $A^B \pmod M$ bằng thuật toán Lũy thừa nhị phân $\mathcal{O}(\log B)$.

**Đầu vào (Input):**

- Một dòng duy nhất chứa 3 số nguyên $A, B, M$ ($0 \le A \le 10^{18}, 0 \le B \le 10^{18}, 1 \le M \le 10^9 + 7$).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là kết quả $A^B \pmod M$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 13 1000 | 323 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $A, B \le 10^{18}, M \le 10^9 + 7$.



### Bài 05 [CPPB-MOD-03]: Lũy Thừa Chuỗi Số Lớn

**Bối cảnh:** Cho số nguyên $A$ và số nguyên $B$ rất lớn được biểu diễn dưới dạng chuỗi có thể lên tới $10^5$ chữ số. Cho $M = 10^9 + 7$. Hãy tính $A^B \pmod M$.

**Đầu vào (Input):**

- Dòng 1: Số nguyên $A$ ($0 \le A \le 10^9$).
- Dòng 2: Chuỗi ký tự số $B$ ($1 \le |B| \le 10^5$).

**Đầu ra (Output):**

- In ra một số nguyên là $A^B \pmod{10^9 + 7}$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 2 <br> 10 | 1024 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $A \le 10^9, |B| \le 10^5$.



### Bài 06 [CPPB-MOD-04]: Nhân Ấn Độ Chống Tràn Số 64-bit

**Bối cảnh:** Cho 3 số nguyên $A, B, M$ ($0 \le A, B, M \le 10^{18}, M > 0$). Hãy tính $(A \times B) \pmod M$ mà không bị tràn số.

**Đầu vào (Input):**

- Một dòng duy nhất chứa 3 số nguyên $A, B, M$.

**Đầu ra (Output):**

- In ra một số nguyên là kết quả $(A \times B) \pmod M$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 1000000000000000000 1000000000000000000 1000000000000000007 | 49 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $A, B, M \le 10^{18}$.



### Bài 07 [CPPB-MOD-05]: Tính Tổng Cấp Số Nhân Đồng Dư

**Bối cảnh:** Cho $A, N$ và $M = 10^9 + 7$. Hãy tính tổng $S = 1 + A + A^2 + \dots + A^N \pmod M$.

**Đầu vào (Input):**

- Một dòng duy nhất chứa 2 số nguyên $A, N$ ($0 \le A \le 10^9, 0 \le N \le 10^{18}$).

**Đầu ra (Output):**

- In ra tổng $S \pmod{10^9 + 7}$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 2 3 | 15 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $A \le 10^9, N \le 10^{18}$.



### Bài 08 [CPPB-MOD-06]: Nghịch Đảo Modulo Bằng Fermat Nhỏ

**Bối cảnh:** Cho số nguyên $A$ và số nguyên tố $M = 10^9 + 7$. Hãy tìm nghịch đảo modulo $A^{-1} \pmod M$ ($1 \le A < M$).

**Đầu vào (Input):**

- Một dòng duy nhất chứa số nguyên $A$ ($1 \le A < 10^9 + 7$).

**Đầu ra (Output):**

- In ra một số nguyên $X$ là nghịch đảo modulo thỏa $(A \times X) \pmod M = 1$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 | 333333336 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le A < 10^9 + 7$.



### Bài 09 [CPPB-MOD-07]: Nghịch Đảo Modulo Bằng Euclid Mở Rộng

**Bối cảnh:** Cho hai số nguyên dương $A, M$ với $\gcd(A, M) = 1$. Hãy tìm nghịch đảo modulo $A^{-1} \pmod M$ bằng thuật toán Euclid mở rộng.

**Đầu vào (Input):**

- Một dòng duy nhất chứa 2 số nguyên $A, M$ ($1 \le A, M \le 10^9, \gcd(A, M) = 1$).

**Đầu ra (Output):**

- In ra một số nguyên $X \in [0, M - 1]$ thỏa $(A \times X) \pmod M = 1$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 7 | 5 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $A, M \le 10^9, \gcd(A, M) = 1$.



### Bài 10 [CPPB-MOD-08]: Phép Chia Đồng Dư A / B mod M

**Bối cảnh:** Cho 2 số nguyên $A, B$ và số nguyên tố $M = 10^9 + 7$ ($B 
ot\equiv 0 \pmod M$). Hãy tính giá trị $\frac{A}{B} \pmod M$.

**Đầu vào (Input):**

- Một dòng duy nhất chứa 2 số nguyên $A, B$ ($0 \le A \le 10^{18}, 1 \le B \le 10^{18}$).

**Đầu ra (Output):**

- In ra giá trị $\frac{A}{B} \pmod{10^9 + 7}$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 10 2 | 5 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $A, B \le 10^{18}$.



### Bài 11 [CPPB-MOD-09]: Tính Số Tổ Hợp C(N, K) mod M

**Bối cảnh:** Cho $Q$ truy vấn, mỗi truy vấn chứa 2 số $N, K$. Hãy tính $C(N, K) \pmod{10^9 + 7}$.

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $Q$ ($1 \le Q \le 10^5$).
- $Q$ dòng tiếp theo: Mỗi dòng chứa 2 số $N, K$ ($0 \le K \le N \le 10^6$).

**Đầu ra (Output):**

- In ra $Q$ dòng tương ứng là kết quả $C(N, K) \pmod{10^9 + 7}$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 <br> 5 2 <br> 6 3 <br> 10 0 | 10 <br> 20 <br> 1 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $Q \le 10^5, N \le 10^6$.



### Bài 12 [CPPB-MOD-10]: Tính Số Chỉnh Hợp A(N, K) mod M

**Bối cảnh:** Cho $Q$ truy vấn, mỗi truy vấn chứa 2 số $N, K$. Hãy tính số chỉnh hợp $A(N, K) = \frac{N!}{(N - K)!} \pmod{10^9 + 7}$.

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $Q$ ($1 \le Q \le 10^5$).
- $Q$ dòng tiếp theo: Mỗi dòng chứa 2 số $N, K$ ($0 \le K \le N \le 10^6$).

**Đầu ra (Output):**

- In ra $Q$ dòng tương ứng là $A(N, K) \pmod{10^9 + 7}$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 2 <br> 4 2 <br> 5 3 | 12 <br> 60 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $Q \le 10^5, N \le 10^6$.



### Bài 13 [CPPB-MOD-11]: Dãy Fibonacci Đồng Dư Lớn

**Bối cảnh:** Cho số nguyên $N$. Hãy tìm số Fibonacci thứ $N$ ($F_N$) theo modulo $10^9 + 7$ (với $F_0 = 0, F_1 = 1, F_2 = 1, \dots$).

**Đầu vào (Input):**

- Một dòng duy nhất chứa số nguyên $N$ ($0 \le N \le 10^{18}$).

**Đầu ra (Output):**

- In ra $F_N \pmod{10^9 + 7}$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 10 | 55 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 10^{18}$.



### Bài 14 [CPPB-MOD-12]: Số Catalan Đồng Dư

**Bối cảnh:** Số Catalan $C_N = \frac{1}{N + 1} C(2N, N)$. Cho số nguyên $N$, hãy tính $C_N \pmod{10^9 + 7}$.

**Đầu vào (Input):**

- Một dòng duy nhất chứa số nguyên $N$ ($0 \le N \le 10^6$).

**Đầu ra (Output):**

- In ra $C_N \pmod{10^9 + 7}$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 | 5 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 10^6$.



### Bài 15 [CPPB-MOD-13]: Lũy Thừa Tầng (Tower of Powers)

**Bối cảnh:** Cho 3 số nguyên $A, B, C$. Hãy tính $A^{B^C} \pmod{10^9 + 7}$.

**Đầu vào (Input):**

- Một dòng duy nhất chứa 3 số nguyên $A, B, C$ ($0 \le A, B, C \le 10^9$).

**Đầu ra (Output):**

- In ra $A^{B^C} \pmod{10^9 + 7}$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 2 3 | 6561 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $A, B, C \le 10^9$.



### Bài 16 [CPPB-MOD-14]: Nghịch Đảo Tuyến Tính 1..N Trong O(N)

**Bối cảnh:** Cho số nguyên $N$ và $M = 10^9 + 7$. Hãy tính nghịch đảo modulo của tất cả các số từ $1$ đến $N$ trong thời gian $\mathcal{O}(N)$.

**Đầu vào (Input):**

- Một dòng duy nhất chứa số nguyên $N$ ($1 \le N \le 10^7$).

**Đầu ra (Output):**

- In ra tổng của tất cả các nghịch đảo modulo $\sum_{i=1}^N i^{-1} \pmod M$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 | 833333341 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 10^7$.



### Bài 17 [CPPB-MOD-15]: Giải Phương Trình Đồng Dư Tuyến Tính Ax = B mod M

**Bối cảnh:** Cho 3 số nguyên $A, B, M$. Hãy tìm nghiệm nguyên không âm nhỏ nhất $X$ của phương trình $A \times X \equiv B \pmod M$. Nếu vô nghiệm in `-1`.

**Đầu vào (Input):**

- Một dòng duy nhất chứa 3 số nguyên $A, B, M$ ($1 \le A, B, M \le 10^9$).

**Đầu ra (Output):**

- In ra nghiệm $X$ nhỏ nhất ($0 \le X < M$), hoặc `-1` nếu vô nghiệm.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 14 30 100 | 95 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $A, B, M \le 10^9$.



### Bài 18 [CPPB-MOD-16]: Đồng Dư Cực Hạn: Căn Bậc Hai Modulo

**Bối cảnh:** Cho số nguyên $A$ và số nguyên tố $P = 10^9 + 7$. Hãy tìm số nguyên $X$ ($0 \le X < P$) nhỏ nhất sao cho $X^2 \equiv A \pmod P$. Nếu không tồn tại $X$, in `-1`.

**Đầu vào (Input):**

- Một dòng duy nhất chứa số nguyên $A$ ($0 \le A < 10^9 + 7$).

**Đầu ra (Output):**

- In ra nghiệm $X$ nhỏ nhất, hoặc `-1` nếu vô nghiệm.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 | 2 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $A < 10^9 + 7$.




# Bài 09: Xử lý số nguyên lớn (BigInt)

## 1. Bản chất vấn đề & trực giác thuật toán (the core problem & intuition)

Trong ngôn ngữ lập trình C++, kiểu dữ liệu số nguyên có kích thước lớn nhất được hỗ trợ phần cứng là `unsigned long long` (64-bit, tối đa xấp xỉ $1.84 \times 10^{19}$) hoặc phần mở rộng GCC `__int128` (128-bit, tối đa xấp xỉ $3.4 \times 10^{38}$).

Tuy nhiên, trong các bài toán thực tế và đề thi học sinh giỏi (như tính $100!$, tính số Fibonacci thứ $1000$, hoặc tính $2^{10000}$ **mà không lấy dư modulo**), kết quả có thể dài hàng nghìn đến hàng chục nghìn chữ số. Vì C++ không có sẵn kiểu dữ liệu BigInteger như Python hay Java, lập trình viên thi đấu C++ bắt buộc phải **tự mô phỏng các phép tính số học đặt tính rồi tính như toán tiểu học** trên mảng ký tự (`string`) hoặc mảng số nguyên (`vector<int>`).

### Big integer hay modular arithmetic: Chọn vũ khí nào?



![Phân định lựa chọn giải thuật: Modulo vs Big Integer](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-09-so-nguyen-lon-bigint/assets/bigint_vs_modulo_vi.png)



| Đề bài yêu cầu | Quy mô kết quả | Vũ khí tối ưu | Kỹ thuật cốt lõi |
|---|:---:|:---:|---|
| Tính $A^B \pmod M$ ($B \le 10^{18}$) | $\le M$ | **Modulo** | Lũy thừa nhị phân $\mathcal{O}(\log B)$ |
| Tính $\frac{A}{B} \pmod M$ | $\le M$ | **Modulo** | Nghịch đảo Modulo $A \times B^{-1}$ |
| Tính $F_{10^6} \pmod M$ | $\le M$ | **Modulo** | Nhân ma trận nhị phân $\mathcal{O}(\log N)$ |
| Tính chính xác $2^{10000}$ | $\approx 3011$ chữ số | **Big Integer** | Lũy thừa nhị phân trên BigInt |
| Tính chính xác $1000!$ | $2568$ chữ số | **Big Integer** | Nhân BigInt $\times$ int liên tiếp |
| Tính chính xác số Fibonacci $F_{1000}$ | $209$ chữ số | **Big Integer** | Cộng BigInt + BigInt quy hoạch động |
| Số có $10^5$ chữ số nhưng chỉ cần $\% M$ | $\le M$ | **Modulo** | Vòng lặp Horner: `cur = (cur * 10 + d) % M` |

## 2. Mô phỏng từng bước (visual step-by-step simulation)

### Ví dụ 1: Mô phỏng phép cộng số lớn $A = 9876$ và $B = 543$

* **Quy tắc:** Đảo ngược chuỗi để chữ số hàng đơn vị nằm ở chỉ số `0`.
* $A' = [6, 7, 8, 9]$, $B' = [3, 4, 5]$.

| Vị trí hàng ($i$) | Cặp chữ số $(A'_i, B'_i)$ | Biến nhớ vào | Phép tính tổng | Ghi nhận & Nhớ mới |
| :---: | :---: | :---: | :---: | :--- |
| **0** (Hàng đơn vị) | $(6, 3)$ | $0$ | $6 + 3 + 0 = 9$ | Ghi **$9$**, nhớ $0$ |
| **1** (Hàng chục) | $(7, 4)$ | $0$ | $7 + 4 + 0 = 11$ | Ghi **$1$**, nhớ $1$ |
| **2** (Hàng trăm) | $(8, 5)$ | $1$ | $8 + 5 + 1 = 14$ | Ghi **$4$**, nhớ $1$ |
| **3** (Hàng nghìn) | $(9, 0)$ | $1$ | $9 + 0 + 1 = 10$ | Ghi **$0$**, nhớ $1$ |
| **Dư cuối** | — | $1$ | $\text{carry} = 1$ | Ghi **$1$**, nhớ $0$ |

* Kết quả đảo ngược: $[9, 1, 4, 0, 1] \implies \mathbf{10419}$.

### Ví dụ 2: Mô phỏng phép nhân số lớn $A = 48$ với số nhỏ $b = 7$

* $A' = [8, 4]$.
* **Bước 0 ($i = 0$):** $8 \times 7 + 0 = 56 \implies$ Ghi $6$, `carry` $= 5$.
* **Bước 1 ($i = 1$):** $4 \times 7 + 5 = 33 \implies$ Ghi $3$, `carry` $= 3$.
* **Dư cuối:** Ghi `carry` $= 3$.
* Kết quả đảo ngược: $[6, 3, 3] \implies \mathbf{336}$.

## 3. Lý thuyết cốt lõi & bất biến thuật toán (core invariants)

### 3.1. Mô hình biểu diễn số lớn & little-endian

* **Biểu diễn Little-Endian:** Lưu các chữ số theo thứ tự từ hàng thấp đến hàng cao (chữ số hàng đơn vị nằm ở chỉ số `0`).
* **Ưu điểm cốt lõi:** Hàng đơn vị nằm ở `index = 0`, nên khi cộng, trừ hoặc nhân ta có thể xử lý trực tiếp từ hàng thấp lên hàng cao và truyền biến nhớ `carry/borrow` sang phần tử kế tiếp ($a[0] \to a[1] \to a[2] \dots$). Ngoài ra, chữ số mới ở cuối có thể được thêm bằng `push_back()` với chi phí amortized $\mathcal{O}(1)$.
* **Biểu diễn Base 10 vs Base $10^9$:**
* **Base 10 (`string` / `vector<int>`):** Mỗi phần tử lưu 1 chữ số thập phân ($0 \dots 9$).
* **Base $10^9$ (`vector<int>` / `vector<long long>`):** Nhóm các cụm 9 chữ số từ phải sang trái.
* *Cấu trúc dữ liệu:* Mỗi chunk lưu kiểu `int` ($0 \dots 999,999,999$); phép nhân giữa 2 chunks lưu kiểu `long long` (vì $(10^9 - 1) \times (10^9 - 1) \approx 10^{18} < 2^{63}-1$).
* *Ví dụ:* Số $1234567890123456789$ được tách thành:
$$\text{chunks} = [23456789, 123456789, 1]$$
$$\text{Giá trị} = 23456789 + 123456789 \times 10^9 + 1 \times (10^9)^2$$

### 3.2. Bảng tổng hợp các phép toán số nguyên lớn ($\mathcal{O}(L^2)$)

| Phép toán | Bản chất thuật toán | Độ phức tạp thời gian | Lưu ý quan trọng |
|---|---|:---:|---|
| **So sánh ($A, B$)** | So sánh độ dài trước, sau đó so sánh từ điển | $\mathcal{O}(\max(L_A, L_B))$ | Xóa sạch số 0 ở đầu trước khi so sánh |
| **Cộng ($A + B$)** | Mô phỏng cộng từng hàng kèm biến nhớ `carry` | $\mathcal{O}(\max(L_A, L_B))$ | Xử lý `carry` còn dư sau khi hết chữ số |
| **Trừ ($A - B$)** | Mô phỏng trừ có mượn `borrow` ($A \ge B$) | $\mathcal{O}(L_A)$ | Xóa sạch số $0$ vô nghĩa ở đầu (`leading zeros`) |
| **Nhân nhỏ ($A \times b$)** | Nhân từng chữ số của $A$ với số nguyên $b$ | $\mathcal{O}(L_A)$ | Biến `carry` có thể vượt quá $10$, cần kiểu `long long` |
| **Nhân lớn ($A \times B$)** | Tích lũy $C[i + j] += A[i] \times B[j]$ rồi normalize | $\mathcal{O}(L_A \times L_B)$ | Khởi tạo mảng $L_A + L_B$ (áp dụng cho $L \le 5000$) |
| **Chia nhỏ ($A / b, A \% b$)** | Chia từ hàng cao nhất xuống hàng đơn vị | $\mathcal{O}(L_A)$ | Biến tích lũy `cur = cur * 10 + A[i]` |

### 3.3. Thuật toán chia số lớn cho số nhỏ & bất biến horner
Khi chia số lớn $A$ cho số nguyên $b$ ($1 \le b \le 10^9$), ta duyệt từ chữ số hàng cao nhất xuống hàng đơn vị:
```cpp
string divSmall(string a, long long b) {
    string res = "";
    long long cur = 0;
    for (char c : a) {
        cur = cur * 10 + (c - '0');
        int digit = cur / b;
        res.push_back(char('0' + digit));
        cur %= b; // cur luôn là số dư hiện tại
    }
    // Xóa số 0 vô nghĩa ở đầu
    int pos = 0;
    while (pos + 1 < (int)res.size() && res[pos] == '0') pos++;
    return res.substr(pos);
}
```

### Ghi chú:
**BẤT BIẾN TOÁN HỌC CỦA PHÉP CHIA TỪNG BƯỚC:**

> Vì trước mỗi bước lặp ta luôn duy trì số dư $0 \le cur < b$, nên sau khi nhận thêm một chữ số mới $cur = cur \times 10 + \text{digit}$, giá trị luôn thỏa mãn $cur < 10b$. Do đó thương tại mỗi bước `digit = cur / b` **chắc chắn luôn nằm trong khoảng $[0, 9]$** (là một chữ số thập phân hợp lệ duy nhất).

### 3.4. Tối ưu hóa base $10^9$ (chunking optimization)

* Thay vì thực hiện phép nhân trên từng chữ số đơn lẻ (Base 10 có $L$ chữ số), ta nén số lớn thành $\frac{L}{9}$ chunks trong Base $10^9$.
* **Đánh giá hiệu năng:** Số lượng cặp chunk cần nhân giảm xấp xỉ $\left(\frac{L}{9}\right) \times \left(\frac{L}{9}\right) = \frac{L^2}{81}$ (giảm khoảng 81 lần về số lượng phép nhân chunk). Tốc độ thực tế tăng vọt từ hàng chục lần giúp vượt qua các bài toán $N \le 10^5$.

## 4. Các bẫy lỗi lập trình kinh điển (bug traps)

1. **Quên xóa số 0 vô nghĩa ở đầu (Leading Zeros):**
* Sau phép trừ (ví dụ $1000 - 999 = 0001$), nếu không xóa số 0 thì chuỗi sẽ in ra `0001`.
* **Cách xử lý:** `while (res.size() > 1 && res.back() == '0') res.pop_back();`.

2. **Không xét trường hợp số $0$:**
* Phép nhân $A \times 0$ phải trả về `"0"`, không được trả về rỗng `""`.
3. **Biến `carry` trong phép nhân số nhỏ có thể rất lớn:**
* Trong phép nhân $A \times b$ với $b = 10^9$, `carry` sau mỗi bước có thể lên tới $10^9$, do đó kiểu dữ liệu của `carry` bắt buộc phải là `long long`.

## 5. Mẫu cài đặt chuẩn thi đấu (competitive templates)

```cpp
# include <bits/stdc++.h>
using namespace std;

// Hàm xóa số 0 vô nghĩa ở đầu chuỗi đảo ngược
void removeLeadingZeros(string &s) {
    while (s.size() > 1 && s.back() == '0') {

        s.pop_back();
    }
}

// Phép cộng 2 số nguyên lớn không âm (A + B)
string addBig(string a, string b) {
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());

    string res = "";
    int carry = 0;
    int n = max(a.size(), b.size());

    for (int i = 0; i < n || carry; ++i) {
        int sum = carry;
        if (i < (int)a.size()) sum += a[i] - '0';
        if (i < (int)b.size()) sum += b[i] - '0';
        res.push_back((sum % 10) + '0');
        carry = sum / 10;
    }

    reverse(res.begin(), res.end());
    return res;
}

// Phép trừ 2 số nguyên lớn không âm (A - B với A >= B)
string subBig(string a, string b) {
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());

    string res = "";
    int borrow = 0;

    for (int i = 0; i < (int)a.size(); ++i) {
        int diff = (a[i] - '0') - borrow;
        if (i < (int)b.size()) diff -= (b[i] - '0');
        if (diff < 0) {
            diff += 10;
            borrow = 1;
        } else {
            borrow = 0;
        }
        res.push_back(diff + '0');
    }

    removeLeadingZeros(res);
    reverse(res.begin(), res.end());
    return res;
}

// Phép nhân 2 số nguyên lớn chuẩn mực và an toàn (A * B)
string mulBig(string a, string b) {
    if (a == "0" || b == "0") return "0";

    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());

    int n = a.size(), m = b.size();
    vector<int> c(n + m, 0);

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            c[i + j] += (a[i] - '0') * (b[j] - '0');
        }
    }

    // Normalize: Đẩy biến nhớ carry sang các ô kế tiếp
    for (int i = 0; i + 1 < n + m; ++i) {
        c[i + 1] += c[i] / 10;
        c[i] %= 10;
    }

    while (c.size() > 1 && c.back() == 0) {

        c.pop_back();
    }

    string res = "";
    for (int i = (int)c.size() - 1; i >= 0; --i) {
        res.push_back(c[i] + '0');
    }

    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a, b;
    if (!(cin >> a >> b)) return 0;

    cout << "A + B = " << addBig(a, b) << "\n";
    cout << "A * B = " << mulBig(a, b) << "\n";
    return 0;
}
```

## Bài tập thực hành


### Bài 01 [CPPB-BIG-01]: So Sánh Hai Số Nguyên Lớn

**Bối cảnh:** Cho 2 số nguyên dương lớn $A$ và $B$. Hãy so sánh $A$ và $B$.

**Đầu vào (Input):**

- Dòng 1: Chuỗi ký tự số $A$ ($1 \le |A| \le 10^5$).
- Dòng 2: Chuỗi ký tự số $B$ ($1 \le |B| \le 10^5$).

**Đầu ra (Output):**

- In ra `>` nếu $A > B$, `<` nếu $A < B$, `=` nếu $A = B$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 123456789 <br> 98765432 | > |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $|A|, |B| \le 10^5$.



### Bài 02 [CPPB-BIG-13]: Chia Hai Số Nguyên Lớn (A / B)

**Bối cảnh:** Cho 2 số nguyên dương lớn $A$ và $B$. Hãy tìm thương nguyên $\lfloor A / B \rfloor$.

**Đầu vào (Input):**

- Dòng 1: Chuỗi ký tự số $A$ ($1 \le |A| \le 1000$).
- Dòng 2: Chuỗi ký tự số $B$ ($1 \le |B| \le 1000$).

**Đầu ra (Output):**

- In ra thương nguyên $\lfloor A / B \rfloor$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 1000 <br> 30 | 33 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $|A|, |B| \le 1000$.



### Bài 03 [CPPB-BIG-01]: So Sánh Hai Số Nguyên Lớn

**Bối cảnh:** Cho 2 số nguyên dương lớn $A$ và $B$. Hãy so sánh $A$ và $B$.

**Đầu vào (Input):**

- Dòng 1: Chuỗi ký tự số $A$ ($1 \le |A| \le 10^5$).
- Dòng 2: Chuỗi ký tự số $B$ ($1 \le |B| \le 10^5$).

**Đầu ra (Output):**

- In ra `>` nếu $A > B$, `<` nếu $A < B$, `=` nếu $A = B$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 123456789 <br> 98765432 | > |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $|A|, |B| \le 10^5$.



### Bài 04 [CPPB-BIG-02]: Cộng Hai Số Nguyên Lớn

**Bối cảnh:** Cho 2 số nguyên dương lớn $A$ và $B$. Hãy tính tổng $A + B$.

**Đầu vào (Input):**

- Dòng 1: Chuỗi ký tự số $A$ ($1 \le |A| \le 10^5$).
- Dòng 2: Chuỗi ký tự số $B$ ($1 \le |B| \le 10^5$).

**Đầu ra (Output):**

- In ra một chuỗi là tổng $A + B$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 9876 <br> 543 | 10419 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $|A|, |B| \le 10^5$.



### Bài 05 [CPPB-BIG-03]: Trừ Hai Số Nguyên Lớn (A >= B)

**Bối cảnh:** Cho 2 số nguyên dương lớn $A$ và $B$ ($A \ge B$). Hãy tính hiệu $A - B$.

**Đầu vào (Input):**

- Dòng 1: Chuỗi ký tự số $A$ ($1 \le |A| \le 10^5$).
- Dòng 2: Chuỗi ký tự số $B$ ($1 \le |B| \le 10^5, B \le A$).

**Đầu ra (Output):**

- In ra hiệu $A - B$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 1000 <br> 999 | 1 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $A \ge B, |A| \le 10^5$.



### Bài 06 [CPPB-BIG-04]: Trừ Hai Số Lớn Tổng Quát (Có Thể Âm)

**Bối cảnh:** Cho 2 số nguyên dương lớn $A$ và $B$. Hãy tính hiệu $A - B$ (nếu âm thì in dấu trừ ở đầu).

**Đầu vào (Input):**

- Dòng 1: Chuỗi ký tự số $A$ ($1 \le |A| \le 10^5$).
- Dòng 2: Chuỗi ký tự số $B$ ($1 \le |B| \le 10^5$).

**Đầu ra (Output):**

- In ra giá trị $A - B$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 543 <br> 9876 | -9333 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $|A|, |B| \le 10^5$.



### Bài 07 [CPPB-BIG-05]: Nhân Số Lớn Với Số Nhỏ

**Bối cảnh:** Cho số nguyên lớn $A$ và số nguyên nhỏ $b$ ($0 \le b \le 10^9$). Hãy tính tích $A \times b$.

**Đầu vào (Input):**

- Dòng 1: Chuỗi ký tự số $A$ ($1 \le |A| \le 10^5$).
- Dòng 2: Số nguyên $b$ ($0 \le b \le 10^9$).

**Đầu ra (Output):**

- In ra tích $A \times b$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 48 <br> 7 | 336 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $|A| \le 10^5, b \le 10^9$.



### Bài 08 [CPPB-BIG-06]: Nhân Hai Số Nguyên Lớn

**Bối cảnh:** Cho 2 số nguyên lớn $A$ và $B$. Hãy tính tích $A \times B$.

**Đầu vào (Input):**

- Dòng 1: Chuỗi ký tự số $A$ ($1 \le |A| \le 2000$).
- Dòng 2: Chuỗi ký tự số $B$ ($1 \le |B| \le 2000$).

**Đầu ra (Output):**

- In ra một chuỗi là tích $A \times B$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 123 <br> 45 | 5535 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $|A|, |B| \le 2000$.



### Bài 09 [CPPB-BIG-07]: Chia Số Lớn Cho Số Nhỏ (Lấy Thương)

**Bối cảnh:** Cho số nguyên lớn $A$ và số nguyên nhỏ $b$ ($1 \le b \le 10^9$). Hãy tìm phần thương nguyên của phép chia $A / b$.

**Đầu vào (Input):**

- Dòng 1: Chuỗi ký tự số $A$ ($1 \le |A| \le 10^5$).
- Dòng 2: Số nguyên dương $b$ ($1 \le b \le 10^9$).

**Đầu ra (Output):**

- In ra phần thương nguyên của phép chia $A / b$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 1000 <br> 8 | 125 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $|A| \le 10^5, b \le 10^9$.



### Bài 10 [CPPB-BIG-08]: Chia Lấy Dư Số Lớn Cho Số Nhỏ

**Bối cảnh:** Cho số nguyên lớn $A$ và số nguyên nhỏ $b$ ($1 \le b \le 10^{18}$). Hãy tính $A \pmod b$.

**Đầu vào (Input):**

- Dòng 1: Chuỗi ký tự số $A$ ($1 \le |A| \le 10^5$).
- Dòng 2: Số nguyên dương $b$ ($1 \le b \le 10^{18}$).

**Đầu ra (Output):**

- In ra số dư $A \pmod b$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 123456789 <br> 100 | 89 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $|A| \le 10^5, b \le 10^{18}$.



### Bài 11 [CPPB-BIG-09]: Tính Giai Thừa Số Lớn (N!)

**Bối cảnh:** Cho số nguyên dương $N$. Hãy in ra giá trị chính xác của $N! = 1 \times 2 \times \dots \times N$.

**Đầu vào (Input):**

- Một dòng duy nhất chứa số nguyên $N$ ($1 \le N \le 1000$).

**Đầu ra (Output):**

- In ra giá trị chính xác của $N!$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 10 | 3628800 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 1000$.



### Bài 12 [CPPB-BIG-10]: Lũy Thừa Số Lớn Chính Xác (A^B)

**Bối cảnh:** Cho 2 số nguyên $A, B$. Hãy in ra giá trị chính xác của $A^B$.

**Đầu vào (Input):**

- Một dòng duy nhất chứa 2 số nguyên $A, B$ ($1 \le A \le 100, 0 \le B \le 1000$).

**Đầu ra (Output):**

- In ra giá trị chính xác của $A^B$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 2 10 | 1024 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $A \le 100, B \le 1000$.



### Bài 13 [CPPB-BIG-11]: Số Fibonacci Lớn Thứ N

**Bối cảnh:** Cho số nguyên $N$. Hãy in ra giá trị chính xác của số Fibonacci thứ $N$ ($F_0 = 0, F_1 = 1, F_2 = 1, \dots$).

**Đầu vào (Input):**

- Một dòng duy nhất chứa số nguyên $N$ ($0 \le N \le 1000$).

**Đầu ra (Output):**

- In ra giá trị chính xác của $F_N$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 10 | 55 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 1000$.



### Bài 14 [CPPB-BIG-12]: Tổng Các Chữ Số Của N!

**Bối cảnh:** Cho số nguyên $N$. Hãy tính tổng tất cả các chữ số trong biểu diễn thập phân của $N!$.

**Đầu vào (Input):**

- Một dòng duy nhất chứa số nguyên $N$ ($1 \le N \le 1000$).

**Đầu ra (Output):**

- In ra một số nguyên là tổng các chữ số của $N!$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 10 | 27 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 1000$.



### Bài 15 [CPPB-BIG-13]: Chia Hai Số Nguyên Lớn (A / B)

**Bối cảnh:** Cho 2 số nguyên dương lớn $A$ và $B$. Hãy tìm thương nguyên $\lfloor A / B \rfloor$.

**Đầu vào (Input):**

- Dòng 1: Chuỗi ký tự số $A$ ($1 \le |A| \le 1000$).
- Dòng 2: Chuỗi ký tự số $B$ ($1 \le |B| \le 1000$).

**Đầu ra (Output):**

- In ra thương nguyên $\lfloor A / B \rfloor$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 1000 <br> 30 | 33 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $|A|, |B| \le 1000$.



### Bài 16 [CPPB-BIG-14]: Căn Bậc Hai Số Nguyên Lớn

**Bối cảnh:** Cho số nguyên dương lớn $A$. Hãy tìm phần nguyên căn bậc hai $\lfloor \sqrt{A} \rfloor$.

**Đầu vào (Input):**

- Một dòng duy nhất chứa chuỗi ký tự số $A$ ($1 \le |A| \le 1000$).

**Đầu ra (Output):**

- In ra giá trị $\lfloor \sqrt{A} \rfloor$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 100 | 10 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $|A| \le 1000$.



### Bài 17 [CPPB-BIG-15]: Ước Chung Lớn Nhất Số Lớn

**Bối cảnh:** Cho 2 số nguyên dương lớn $A$ và $B$. Hãy tìm $\gcd(A, B)$.

**Đầu vào (Input):**

- Dòng 1: Chuỗi ký tự số $A$ ($1 \le |A| \le 1000$).
- Dòng 2: Chuỗi ký tự số $B$ ($1 \le |B| \le 1000$).

**Đầu ra (Output):**

- In ra $\gcd(A, B)$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 120000000000000000000000 <br> 180000000000000000000000 | 60000000000000000000000 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $|A|, |B| \le 1000$.



### Bài 18 [CPPB-BIG-16]: Số Lớn Cực Hạn: Tổ Hợp C(N, K) Chính Xác

**Bối cảnh:** Cho 2 số nguyên $N, K$. Hãy tính giá trị chính xác của $C(N, K) = \frac{N!}{K!(N-K)!}$ mà không lấy dư.

**Đầu vào (Input):**

- Một dòng duy nhất chứa 2 số nguyên $N, K$ ($0 \le K \le N \le 100$).

**Đầu ra (Output):**

- In ra giá trị chính xác của $C(N, K)$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 10 5 | 252 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $N \le 100$.



# CHƯƠNG 04: ĐỆ QUY, CHIA ĐỂ TRỊ & QUAY LUI


# Bài 10: Thuật toán đệ quy & cây gọi hàm

## 1. Bản chất vấn đề & trực giác thuật toán (the core problem & intuition)

Trong các bài toán lập trình cơ bản, chúng ta quen thuộc với tư duy lặp tuần tự (`for`, `while`): xử lý từng phần tử lần lượt từ đầu đến cuối. Tuy nhiên, trong thế giới cấu trúc dữ liệu và giải thuật nâng cao, rất nhiều bài toán mang bản chất **tự đồng dạng (Self-Similarity)**: Để giải một bài toán quy mô $N$, ta có thể giải bài toán tương tự nhưng ở quy mô nhỏ hơn $N-1$ hoặc $N/2$, sau đó kết hợp kết quả lại.

### Khái niệm đệ quy (recursion):
Đệ quy là kỹ thuật lập trình trong đó **một hàm tự gọi lại chính nó** (trực tiếp hoặc gián tiếp) với các tham số đại diện cho bài toán con nhỏ hơn.

Mỗi hàm đệ quy chuẩn mực bắt buộc phải có đủ 2 thành phần cốt lõi:

1. **Điểm Dừng (Base Case / Anchor):** Trường hợp bài toán đơn giản nhất đã biết trước đáp án mà không cần gọi tiếp đệ quy. Điểm dừng có nhiệm vụ **ngắt chuỗi lời gọi vô tận**.
2. **Bước Đệ Quy (Recursive Case / Reduction Step):** Thu nhỏ quy mô bài toán bằng cách gọi lại chính hàm đó với tham số tiến dần về phía Base Case.



![Cấu trúc điều hướng của hàm đệ quy: Base Case vs Recursive Case](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-10-de-quy-co-ban/assets/recursion_structure_vi.png)



## 2. Mô phỏng từng bước hoạt động của Call Stack (visual step-by-step simulation)

Để hiểu đệ quy, lập trình viên không được nhìn code như một vòng lặp phẳng, mà bắt buộc phải hình dung hoạt động của **Ngăn xếp cuộc gọi (Call Stack)** qua hai pha riêng biệt:

* **Pha Xuôi (Winding Phase):** Các hàm được gọi liên tiếp và đẩy đè lên nhau trên đỉnh ngăn xếp (`Stack Frame Push`).
* **Pha Ngược (Unwinding Phase):** Khi chạm Base Case, các hàm lần lượt tính xong kết quả, trả về (`Return`) và được giải phóng khỏi ngăn xếp (`Stack Frame Pop`).

### Ví dụ 1: Mô phỏng hàm tính giai thừa `fact(4)`

```cpp
long long fact(int n) {
    if (n <= 1) return 1;          // Base Case
    return n * fact(n - 1);        // Recursive Step
}
```

#### Bảng mô phỏng từng bước ngăn xếp (Call Stack trace):

| Bước | Hành động | Trạng thái Call Stack (Đỉnh stack ở trên cùng) | Giá trị trả về tại bước đó |
|:---:|---|---|:---:|
| **1** | Gọi `fact(4)` | `[fact(4)]` | Đang đợi `fact(3)` |
| **2** | Gọi `fact(3)` | `[fact(3)] -> [fact(4)]` | Đang đợi `fact(2)` |

| **3** | Gọi `fact(2)` | `[fact(2)] -> [fact(3)] -> [fact(4)]` | Đang đợi `fact(1)` |

| **4** | Gọi `fact(1)` | `[fact(1)] -> [fact(2)] -> [fact(3)] -> [fact(4)]` | **Chạm Base Case: Trả về 1** |

| **5** | Unwind `fact(2)` | `[fact(2)] -> [fact(3)] -> [fact(4)]` | `fact(2) = 2 * 1 = 2` |

| **6** | Unwind `fact(3)` | `[fact(3)] -> [fact(4)]` | `fact(3) = 3 * 2 = 6` |

| **7** | Unwind `fact(4)` | `[fact(4)]` | `fact(4) = 4 * 6 = 24` |
| **8** | Kết thúc | Stack rỗng | **Đáp án: 24** |

### Ví dụ 2: So sánh vị trí lệnh in (winding vs unwinding)

Quan sát sự khác biệt khi đặt lệnh `cout` **trước** vs **sau** lời gọi đệ quy:

```cpp
// Dạng A: In trong Winding Phase (Trước khi gọi đệ quy)
void printBackward(int n) {
    if (n == 0) return;
    cout << n << " ";           // In ngay khi vào hàm
    printBackward(n - 1);
}
// Gọi printBackward(3) -> Output: 3 2 1

// Dạng B: In trong Unwinding Phase (Sau khi gọi đệ quy)
void printForward(int n) {
    if (n == 0) return;
    printForward(n - 1);
    cout << n << " ";           // In khi hàm quay lui trở về
}
// Gọi printForward(3) -> Output: 1 2 3

```

### Quy luật vàng (winding vs unwinding):

* Các thao tác viết **trước lời gọi đệ quy** sẽ thực thi theo thứ tự từ ngoài vào trong ($N \to 1$).
* Các thao tác viết **sau lời gọi đệ quy** sẽ thực thi theo thứ tự từ trong ra ngoài ($1 \to N$), khi stack bắt đầu rút lui (Unwind).

## 3. Lý thuyết cốt lõi & bất biến thuật toán (core invariants)

### 3.1. Khái niệm stack frame & phân tích an toàn bộ nhớ (stack safety)

* Khi một hàm được gọi, mô hình thực thi của chương trình tạo ra một **Stack Frame (Activation Record)** lưu trữ trạng thái thực thi riêng biệt: tham số truyền vào, các biến cục bộ và địa chỉ trả về (Return Address) theo quy ước gọi (Calling Convention / ABI).
* Vùng nhớ ngăn xếp (Stack Memory) có kích thước hữu hạn và giới hạn cụ thể phụ thuộc vào môi trường thực thi, hệ điều hành và cấu hình của từng Online Judge.
* **Độ sâu đệ quy (Recursion Depth) vs Kích thước Stack Frame:**
* Để đánh giá an toàn bộ nhớ của hàm đệ quy, ta phải xem xét đồng thời **Độ sâu đệ quy tối đa (Maximum Depth)** và **Dung lượng bộ nhớ tiêu thụ trên mỗi Frame**. Nếu mỗi frame chứa mảng cục bộ lớn hoặc đệ quy vượt quá giới hạn bộ nhớ stack, chương trình sẽ gặp lỗi tràn ngăn xếp (**Stack Overflow / Segmentation Fault**).

### Lưu ý kỹ thuật về tail recursion trong C++:
Trong lý thuyết ngôn ngữ, *Đệ quy đuôi (Tail Recursion)* là hàm đệ quy mà lời gọi hàm là câu lệnh cuối cùng. Tuy nhiên, **chuẩn ngôn ngữ C++ không bắt buộc trình biên dịch phải tối ưu hóa đệ quy đuôi (Tail-Call Optimization - TCO)** trong mọi cờ biên dịch thi đấu. Do đó, học sinh không được chủ quan giả định đệ quy đuôi sẽ luôn tự biến thành vòng lặp $\mathcal{O}(1)$ bộ nhớ. Luôn phân tích độ sâu stack cẩn trọng!

### 3.2. Hệ thống phân loại thuật ngữ đệ quy (recursion taxonomy)



![Hệ thống phân loại thuật toán đệ quy: Tuyến tính vs Phân nhánh](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-10-de-quy-co-ban/assets/recursion_taxonomy_vi.png)



1. **Đệ quy Tuyến tính (Linear Recursion - 1 nhánh gọi / Frame):**
* Trong mỗi Stack Frame chỉ thực hiện **đúng 1 lời gọi đệ quy con**. Cây gọi hàm là một đường thẳng đơn tuyến.
* *Ví dụ:*
* Giai thừa $N!$: Độ sâu $N$, thời gian $\Theta(N)$, Stack Space $\Theta(N)$.
* Thuật toán Euclid $\gcd(A, B)$: Độ sâu $\Theta(\log(\min(A, B)))$, thời gian $\Theta(\log(\min(A, B)))$.
Lũy thừa nhị phân `powerRec(A, B/2)` (khi lưu biến tạm `half`): Độ sâu $\Theta(\log B)$, thời gian $\Theta(\log B)$. Lưu ý:* Mặc dù quy mô bài toán giảm theo cấp số nhân ($B \to B/2$), cấu trúc cây gọi hàm vẫn là đường thẳng 1 nhánh đơn tuyến.

2. **Đệ quy Phân nhánh (Branching / Tree Recursion - $\ge 2$ nhánh gọi / Frame):**
* Trong mỗi Stack Frame xuất hiện **từ 2 lời gọi đệ quy con trở lên**, làm bùng nổ không gian trạng thái tạo thành cây nhị phân hoặc cây đa phân.
* *Ví dụ:*
* Tháp Hà Nội: $T(N) = 2T(N-1) + 1 \implies \Theta(2^N)$ bước, Độ sâu $N$.
* Cây chia đôi tìm Min/Max: $T(N) = 2T(N/2) + \mathcal{O}(1) \implies \Theta(N)$ thao tác, Độ sâu $\Theta(\log N)$.
* Fibonacci đệ quy thuần túy $F(N) = F(N-1) + F(N-2)$.

### 3.3. Độ phức tạp toán học của fibonacci đệ quy & cầu nối sang quy hoạch động

Xét cây gọi hàm khi tính $F(5)$ bằng đệ quy phân nhánh:



![Cây đệ quy phân nhánh Fibonacci F(5) và hiện tượng bài toán con trùng lặp](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-10-de-quy-co-ban/assets/fibonacci_recursion_tree_vi.png)



* **Phân tích độ phức tạp tiệm cận chính xác:**
Số lời gọi hàm thỏa mãn hệ thức truy hồi $T(N) = T(N-1) + T(N-2) + 1$. Bằng phương trình đặc trưng $r^2 - r - 1 = 0$, ta chứng minh được số phép tính thực tế tăng theo **cấp số nhân chính xác**:
$$\Theta(\varphi^N) \quad \text{với} \quad \varphi = \frac{1 + \sqrt{5}}{2} \approx 1.618 \text{ (Tỉ lệ vàng)}$$
Chặn trên $O(2^N)$ là một cận trên lỏng (Upper Bound).

* **Hiện tượng Overlapping Subproblems:**
Để tính $F(5)$, hàm $F(3)$ bị tính lại 2 lần, $F(2)$ bị tính lại 3 lần. Với $N = 40$, số lượng lời gọi đã lên tới hàng trăm triệu theo mô hình Fibonacci ($\Theta(\varphi^N)$), minh họa rõ hiện tượng bùng nổ thời gian.

* **Bài học sư phạm:** Đệ quy thuần túy rất đẹp nhưng sẽ bị tê liệt khi không gian trạng thái có các bài toán con trùng lặp. Việc **lưu lại kết quả đã tính vào bảng nhớ (Memoization)** sẽ được học bài bản ở **Module 05: Quy hoạch động (Dynamic Programming)**.

## 4. Các bẫy lỗi lập trình kinh điển (bug traps)

1. **Thiếu Base Case hoặc Base Case không bao giờ chạm tới (Infinite Recursion):**
* Viết `if (n == 0)` nhưng tham số truyền vào là số âm $\implies$ Gọi đệ quy vô tận cho tới khi sập ngăn xếp.
* **Cách phòng chống:** Luôn chặn cận bằng dấu `<=` (ví dụ `if (n <= 1) return 1;`).
2. **Khai báo mảng lớn cục bộ bên trong hàm đệ quy:**
* Viết `int temp[100000];` trong hàm đệ quy sẽ khiến mỗi Stack Frame tốn hàng trăm KB bộ nhớ $\implies$ Tràn stack chỉ sau vài chục lời gọi.
* **Cách phòng chống:** Dùng biến toàn cục hoặc truyền tham chiếu `const vector<int> &a`.

3. **Bẫy Gọi Lặp Lại Đệ Quy (Recursive Call Duplication):**
* Trong bài lũy thừa nhị phân, nếu viết `return power(a, b/2) * power(a, b/2);` thì từ đệ quy tuyến tính $\mathcal{O}(\log B)$ sẽ bị nổ thành cây đệ quy phân nhánh $\Theta(B)$ thao tác.
* **Quy tắc vàng:** *Không có Memoization, hai lời gọi hàm giống nhau là hai lần tính toán hoàn toàn độc lập.* Tính 1 lần vào biến tạm: `long long half = power(a, b/2, m); return (half * half) % m;`.

## 5. Mẫu cài đặt chuẩn thi đấu (competitive templates)

```cpp
# include <bits/stdc++.h>
using namespace std;

// 1. In dãy số 1..N và N..1 chuẩn Winding / Unwinding
void printForward(int n) {
    if (n <= 0) return;
    printForward(n - 1);
    cout << n << " ";
}

void printBackward(int n) {
    if (n <= 0) return;
    cout << n << " ";
    printBackward(n - 1);
}

// 2. Lũy thừa nhị phân đệ quy O(log B) an toàn với M <= 10^9
long long powerRec(long long a, long long b, long long m) {
    if (b == 0) return 1 % m;
    long long half = powerRec(a, b / 2, m);
    long long res = (1LL * (half % m) * (half % m)) % m;
    if (b % 2 == 1) res = (1LL * res * (a % m)) % m;
    return res;
}

// 3. Tháp Hà Nội chuẩn Theta(2^N)
void solveHanoi(int n, char from_rod, char to_rod, char aux_rod) {
    if (n == 0) return;
    solveHanoi(n - 1, from_rod, aux_rod, to_rod);
    cout << from_rod << " -> " << to_rod << "\n";

    solveHanoi(n - 1, aux_rod, to_rod, from_rod);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n = 4;
    cout << "Day so 1..N: ";
    printForward(n);
    cout << "\n";

    cout << "Day so N..1: ";
    printBackward(n);
    cout << "\n";

    cout << "2^10 mod 1000 = " << powerRec(2, 10, 1000) << "\n";
    return 0;
}
```

## Bài tập thực hành


### Bài 01 [CPPB-REC-01]: In Dãy Số Đệ Quy 1..N và N..1

**Bối cảnh:** Cho số nguyên dương $N$. Hãy in ra 2 dòng:
- Dòng 1: In các số từ $1$ đến $N$ cách nhau bởi dấu cách.
- Dòng 2: In các số từ $N$ về $1$ cách nhau bởi dấu cách.
Bắt buộc sử dụng 2 hàm đệ quy riêng biệt để rèn luyện tư duy Winding vs Unwinding.

**Đầu vào (Input):**

- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 1000$).

**Đầu ra (Output):**

- Dòng 1: $N$ số từ $1$ đến $N$.
- Dòng 2: $N$ số từ $N$ về $1$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 | 1 2 3 4 <br> 4 3 2 1 |

**Ràng buộc & Giới hạn:**

- 100% số test có $1 \le N \le 1000$.



### Bài 02 [CPPB-REC-13]: Tháp Hà Nội Có Ràng Buộc Nước Đi

**Bối cảnh:** Cho $N$ đĩa trên cọc $A$. Quy tắc: **Cấm tuyệt đối mọi nước đi trực tiếp giữa cọc A và cọc C** (mọi đĩa muốn đi từ $A \to C$ hoặc $C \to A$ bắt buộc phải đi qua cọc trung gian $B$). Hãy in ra số bước di chuyển tối thiểu $K = 3^N - 1$ và danh sách các bước di chuyển hợp lệ.

**Đầu vào (Input):**

- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10$).

**Đầu ra (Output):**

- Dòng 1: Số bước di chuyển tối thiểu $K = 3^N - 1$.
- $K$ dòng tiếp theo: Mỗi dòng in theo định dạng `X -> Y`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 2 | 8 <br> A -> B <br> B -> C <br> A -> B <br> C -> B <br> B -> A <br> B -> C <br> A -> B <br> B -> C |

**Ràng buộc & Giới hạn:**

- 100% số test có $1 \le N \le 10$.



### Bài 03 [CPPB-REC-01]: In Dãy Số Đệ Quy 1..N và N..1

**Bối cảnh:** Cho số nguyên dương $N$. Hãy in ra 2 dòng:
- Dòng 1: In các số từ $1$ đến $N$ cách nhau bởi dấu cách.
- Dòng 2: In các số từ $N$ về $1$ cách nhau bởi dấu cách.
Bắt buộc sử dụng 2 hàm đệ quy riêng biệt để rèn luyện tư duy Winding vs Unwinding.

**Đầu vào (Input):**

- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 1000$).

**Đầu ra (Output):**

- Dòng 1: $N$ số từ $1$ đến $N$.
- Dòng 2: $N$ số từ $N$ về $1$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 | 1 2 3 4 <br> 4 3 2 1 |

**Ràng buộc & Giới hạn:**

- 100% số test có $1 \le N \le 1000$.



### Bài 04 [CPPB-REC-02]: Tính Tổng Dãy Số & Giai Thừa Bằng Đệ Quy

**Bối cảnh:** Cho số nguyên dương $N$. Hãy tính tổng $S = 1 + 2 + \dots + N$ và tích giai thừa $P = N! = 1 \times 2 \times \dots \times N$ bằng các hàm đệ quy có giá trị trả về.

**Đầu vào (Input):**

- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 20$).

**Đầu ra (Output):**

- In ra 2 số nguyên $S$ và $P$ trên cùng một dòng, cách nhau bởi dấu cách.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 | 10 24 |

**Ràng buộc & Giới hạn:**

- 100% số test có $1 \le N \le 20$.



### Bài 05 [CPPB-REC-03]: Đếm & Tính Tổng Chữ Số Của N Bằng Đệ Quy

**Bối cảnh:** Cho số nguyên dương $N$. Hãy viết hàm đệ quy để đếm số lượng chữ số và tính tổng tất cả các chữ số của $N$.

**Đầu vào (Input):**

- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10^{18}$).

**Đầu ra (Output):**

- In ra 2 số nguyên là số lượng chữ số và tổng các chữ số của $N$, cách nhau bởi dấu cách.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 12345 | 5 15 |

**Ràng buộc & Giới hạn:**

- 100% số test có $1 \le N \le 10^{18}$.



### Bài 06 [CPPB-REC-04]: Đảo Ngược Mảng Bằng Đệ Quy Hai Con Trỏ

**Bối cảnh:** Cho mảng số nguyên $A$ gồm $N$ phần tử. Hãy sử dụng hàm đệ quy 2 con trỏ `reverseRec(l, r)` để đảo ngược mảng $A$ ngay trên mảng gốc mà không dùng vòng lặp.

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 1000$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($|A_i| \le 10^9$).

**Đầu ra (Output):**

- In ra $N$ phần tử của mảng sau khi đảo ngược, cách nhau bởi dấu cách.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 <br> 1 2 3 4 5 | 5 4 3 2 1 |

**Ràng buộc & Giới hạn:**

- 100% số test có $N \le 1000, |A_i| \le 10^9$.



### Bài 07 [CPPB-REC-05]: Kiểm Tra Chuỗi Palindrome Bằng Đệ Quy

**Bối cảnh:** Cho xâu ký tự $S$ gồm các chữ cái tiếng Anh in thường. Hãy viết hàm đệ quy `isPalindrome(l, r)` để kiểm tra xem xâu $S$ có phải là xâu đối xứng hay không. In `YES` nếu đúng, ngược lại in `NO`.

**Đầu vào (Input):**

- Một dòng duy nhất chứa xâu ký tự $S$ ($1 \le |S| \le 1000$).

**Đầu ra (Output):**

- In `YES` nếu $S$ là palindrome, ngược lại in `NO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| radar | YES |

**Ràng buộc & Giới hạn:**

- 100% số test có $1 \le |S| \le 1000$.



### Bài 08 [CPPB-REC-06]: So Sánh Đệ Quy Tuyến Tính & Chia Đôi Khi Tìm Min/Max

**Bối cảnh:** Cho mảng số nguyên $A$ gồm $N$ phần tử. Hãy cài đặt hàm đệ quy chia đôi (Binary Recursion) để tìm giá trị nhỏ nhất và lớn nhất trong mảng.

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 1000$).
- Dòng 2: $N$ số nguyên $A_1, \dots, A_N$ ($|A_i| \le 10^9$).

**Đầu ra (Output):**

- In ra 2 số nguyên là giá trị nhỏ nhất và lớn nhất trong mảng, cách nhau bởi dấu cách.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 6 <br> 3 1 7 9 2 8 | 1 9 |

**Ràng buộc & Giới hạn:**

- 100% số test có $N \le 1000, |A_i| \le 10^9$.



### Bài 09 [CPPB-REC-07]: Thuật Toán Euclid Tính GCD & LCM Bằng Đệ Quy

**Bối cảnh:** Cho 2 số nguyên dương $A, B$. Hãy tính ước chung lớn nhất $\gcd(A, B)$ và bội chung nhỏ nhất $\text{lcm}(A, B)$ bằng thuật toán Euclid đệ quy.

**Đầu vào (Input):**

- Một dòng duy nhất chứa 2 số nguyên dương $A, B$ ($1 \le A, B \le 10^{18}$).

**Đầu ra (Output):**

- In ra 2 số $\gcd(A, B)$ và $\text{lcm}(A, B)$ cách nhau bởi dấu cách. (Nếu LCM tràn số 64-bit, dùng `__int128`).

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 12 18 | 6 36 |

**Ràng buộc & Giới hạn:**

- 100% số test có $1 \le A, B \le 10^{18}$.



### Bài 10 [CPPB-REC-08]: Lũy Thừa Nhị Phân Đệ Quy A^B mod M

**Bối cảnh:** Cho 3 số nguyên $A, B, M$. Hãy tính $A^B \pmod M$ bằng thuật toán Lũy thừa nhị phân đệ quy $\mathcal{O}(\log B)$ (chú ý chỉ gọi đệ quy 1 lần vào biến tạm `half` để tránh nổ thời gian).

**Đầu vào (Input):**

- Một dòng duy nhất chứa 3 số nguyên $A, B, M$ ($0 \le A, B \le 10^{18}, 1 \le M \le 10^9 + 7$).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là kết quả $A^B \pmod M$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 13 1000 | 323 |

**Ràng buộc & Giới hạn:**

- 100% số test có $A, B \le 10^{18}, M \le 10^9 + 7$.



### Bài 11 [CPPB-REC-09]: Bài Toán Tháp Hà Nội (Tower of Hanoi)

**Bối cảnh:** Cho $N$ đĩa có kích thước từ $1$ đến $N$ đặt trên cọc $A$. Hãy in ra số bước di chuyển tối thiểu và các bước di chuyển từng đĩa từ cọc $A$ sang cọc $C$ dùng cọc $B$ làm trung gian theo quy tắc kinh điển.

**Đầu vào (Input):**

- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 15$).

**Đầu ra (Output):**

- Dòng 1: Số bước di chuyển $K = 2^N - 1$.
- $K$ dòng tiếp theo: Mỗi dòng in theo định dạng `A -> C` (chuyển đĩa từ cọc nguồn sang cọc đích).

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 | 7 <br> A -> C <br> A -> B <br> C -> B <br> A -> C <br> B -> A <br> B -> C <br> A -> C |

**Ràng buộc & Giới hạn:**

- 100% số test có $1 \le N \le 15$.



### Bài 12 [CPPB-REC-10]: Dãy Fibonacci Đệ Quy & Khảo Sát Cây Gọi Hàm

**Bối cảnh:** Cho số nguyên $N$. Hãy tính số Fibonacci $F_N$ ($F_0 = 0, F_1 = 1, F_N = F_{N-1} + F_{N-2}$) bằng hàm đệ quy thuần túy và đếm tổng số lần hàm `fib()` được gọi.

**Đầu vào (Input):**

- Một dòng duy nhất chứa số nguyên $N$ ($0 \le N \le 30$).

**Đầu ra (Output):**

- In ra 2 số nguyên là giá trị $F_N$ và tổng số lần gọi hàm `fib()`, cách nhau bởi dấu cách.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 | 3 9 |

**Ràng buộc & Giới hạn:**

- 100% số test có $0 \le N \le 30$.



### Bài 13 [CPPB-REC-11]: Chuyển Đổi Hệ Cơ Số 10 Sang Nhị Phân Bằng Đệ Quy

**Bối cảnh:** Cho số nguyên không âm $N$. Hãy in ra biểu diễn nhị phân của $N$ bằng đệ quy (tận dụng pha Unwinding để in đúng thứ tự mà không cần đảo chuỗi).

**Đầu vào (Input):**

- Một dòng duy nhất chứa số nguyên $N$ ($0 \le N \le 10^{18}$).

**Đầu ra (Output):**

- In ra chuỗi nhị phân của $N$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 13 | 1101 |

**Ràng buộc & Giới hạn:**

- 100% số test có $0 \le N \le 10^{18}$.



### Bài 14 [CPPB-REC-12]: Xây Dựng Hệ Thức Truy Hồi Cho Dãy Số Đan Dấu

**Bối cảnh:** Cho số nguyên dương $N$. Hãy tính giá trị của biểu thức $S(N) = 1 - 2 + 3 - 4 + \dots + (-1)^{N+1} N$ bằng hàm đệ quy truy hồi $S(N) = S(N-1) + (-1)^{N+1} N$.

**Đầu vào (Input):**

- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 1000$).

**Đầu ra (Output):**

- In ra giá trị của biểu thức $S(N)$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 | 3 |

**Ràng buộc & Giới hạn:**

- 100% số test có $1 \le N \le 1000$.



### Bài 15 [CPPB-REC-13]: Tháp Hà Nội Có Ràng Buộc Nước Đi

**Bối cảnh:** Cho $N$ đĩa trên cọc $A$. Quy tắc: **Cấm tuyệt đối mọi nước đi trực tiếp giữa cọc A và cọc C** (mọi đĩa muốn đi từ $A \to C$ hoặc $C \to A$ bắt buộc phải đi qua cọc trung gian $B$). Hãy in ra số bước di chuyển tối thiểu $K = 3^N - 1$ và danh sách các bước di chuyển hợp lệ.

**Đầu vào (Input):**

- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10$).

**Đầu ra (Output):**

- Dòng 1: Số bước di chuyển tối thiểu $K = 3^N - 1$.
- $K$ dòng tiếp theo: Mỗi dòng in theo định dạng `X -> Y`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 2 | 8 <br> A -> B <br> B -> C <br> A -> B <br> C -> B <br> B -> A <br> B -> C <br> A -> B <br> B -> C |

**Ràng buộc & Giới hạn:**

- 100% số test có $1 \le N \le 10$.



### Bài 16 [CPPB-REC-14]: Sinh Xâu Nhị Phân Không Chứa Hai Số 1 Liền Kề

**Bối cảnh:** Cho số nguyên dương $N$. Hãy sinh tất cả các xâu nhị phân độ dài $N$ theo thứ tự từ điển sao cho không có 2 ký tự `'1'` nào đứng cạnh nhau bằng hàm đệ quy phân nhánh trạng thái.

**Đầu vào (Input):**

- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 20$).

**Đầu ra (Output):**

- Dòng 1: Số lượng xâu thỏa mãn (bằng số Fibonacci $F_{N+2}$).
- Các dòng tiếp theo: Mỗi dòng in ra một xâu nhị phân thỏa mãn.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 | 5 <br> 000 <br> 001 <br> 010 <br> 100 <br> 101 |

**Ràng buộc & Giới hạn:**

- 100% số test có $1 \le N \le 20$.



### Bài 17 [CPPB-REC-15]: Đếm Số Cách Phân Tích Số N Thành Tổng Bằng Đệ Quy

**Bối cảnh:** Cho số nguyên dương $N$. Hãy đếm số cách phân tích $N$ thành tổng của các số nguyên dương $N = a_1 + a_2 + \dots + a_k$ ($a_1 \ge a_2 \ge \dots \ge a_k \ge 1$) bằng hàm đệ quy thuần túy.

**Đầu vào (Input):**

- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 30$).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là số cách phân tích số $N$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 | 5 |

**Ràng buộc & Giới hạn:**

- 100% số test có $1 \le N \le 30$.



### Bài 18 [CPPB-REC-16]: Đếm Cấu Hình Trạng Thái Phân Nhánh Không Trùng Lặp

**Bối cảnh:** Cho số nguyên dương $N$. Hãy đếm số lượng cây nhị phân tìm kiếm (BST) phân biệt có thể tạo thành từ $N$ khóa có giá trị từ $1$ đến $N$ bằng hàm đệ quy cấu trúc cây (hệ thức Catalan) mà không dùng `set/map` hay công thức đại số đóng.

**Đầu vào (Input):**

- Một dòng duy nhất chứa số nguyên $N$ ($0 \le N \le 15$).

**Đầu ra (Output):**

- In ra số lượng cây nhị phân phân biệt.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 | 5 |

**Ràng buộc & Giới hạn:**

- 100% số test có $0 \le N \le 15$.




# Bài 11: Kỹ thuật chia để trị

## 1. Cầu nối tư duy: Recurrence $\to$ recursion tree $\to$ complexity

Ở Bài 10, chúng ta đã làm chủ kỹ thuật Đệ quy: giải bài toán quy mô $N$ bằng cách thu nhỏ dần bài toán. Từ cấu trúc code đệ quy, ta có thể thiết lập **Hệ thức truy hồi (Recurrence)** và phân tích qua **Cây đệ quy (Recursion Tree)** để tìm ra độ phức tạp chính xác:

$\text{Code Đệ Quy} \longrightarrow \text{Hệ Thức Truy Hồi (Recurrence)} \longrightarrow \text{Cây Đệ Quy (Recursion Tree)} \longrightarrow \text{Độ Phức Tạp (Complexity)}$

* **Đệ quy tuyến tính (Bài 10):**
$$T(N) = T(N-1) + \mathcal{O}(1) \implies \text{Cây 1 nhánh thẳng, độ sâu } N \implies \Theta(N)$$

* **Đệ quy phân nhánh chia đôi (Bài 11):**
$$T(N) = 2T\left(\frac{N}{2}\right) + \mathcal{O}(N) \implies \text{Cây nhị phân đầy đủ, chiều cao } \log_2 N \implies \Theta(N \log N)$$

* **Đệ quy phân nhánh giảm 1 (Bài 10):**
$$T(N) = 2T(N-1) + \mathcal{O}(1) \implies \text{Cây nhị phân bùng nổ, } 2^N \text{ lá} \implies \Theta(2^N)$$

> **Quy luật cốt lõi:** "Đệ quy" chỉ là cơ chế cài đặt; cấu trúc cây lời gọi và khối lượng công việc ở mỗi tầng mới là yếu tố quyết định độ phức tạp.

## 2. Phân biệt cốt lõi: Đệ quy (Recursion) và chia để trị (Divide & Conquer)

Học sinh rất dễ nhầm lẫn giữa hai khái niệm này:

| Khái Niệm | Bản Chất | Ví dụ Điển Hình |
|---|---|---|
| **Đệ Quy (Recursion)** | **Cơ chế thực thi:** Kỹ thuật lập trình trong đó một hàm tự gọi lại chính nó thông qua Call Stack. | Tính $N!$, Fibonacci, Duyệt mảng tuần tự. |
| **Chia Để Trị (D&C)** | **Chiến lược thiết kế thuật toán:** Phân rã bài toán thành các bài toán con cùng bản chất nhưng nhỏ hơn, giải từng phần và gộp lại. | Merge Sort, Inversion Count, Closest Pair. |

* Tính $N! = N \times (N-1)!$ là **Đệ quy** nhưng **không phải D&C** (vì chỉ thu nhỏ 1 phần tử mà không có bước chia và gộp cấu trúc).
* Merge Sort là **D&C hoàn chỉnh** sử dụng cơ chế Đệ quy để điều khiển.

## 3. Bản chất vấn đề & hai kiểu phân rã: Divide vs partition

**Divide & Conquer** là chiến lược phân rã một bài toán thành các bài toán con có cùng bản chất nhưng kích thước nhỏ hơn, giải các bài toán con, rồi kết hợp kết quả lại để thu được lời giải cho bài toán ban đầu.

### Phân biệt hai kiểu phân rã dữ liệu:

1. **Divide (Phân chia theo vị trí chỉ số):**
* Chia cố định theo chỉ số mảng (thường là tại trung điểm `mid = l + (r - l) / 2`).
* *Ví dụ:* Merge Sort chia `[1 2 3 4 5 6 7 8]` thành `[1 2 3 4]` và `[5 6 7 8]`.
2. **Partition (Phân hoạch theo quan hệ với Pivot):**
* Chia động dựa trên việc so sánh các phần tử với một giá trị chốt (`pivot`), kích thước 2 nửa có thể không đều nhau.
* *Ví dụ:* QuickSelect phân hoạch `[7 2 9 1 5 3 8]` với `pivot = 5` thành `[2 1 3]` (nhỏ hơn 5), `[5]`, và `[7 9 8]` (lớn hơn 5).



![Mô hình Thuật toán Chia để trị (Divide & Conquer)](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-11-chia-de-tri/assets/dnc_model_vi.png)



## 4. Khung tư duy d&c (the d&c mental model)

Trước bất kỳ bài toán nào nghi ngờ sử dụng Chia Để Trị, hãy luôn trả lời **4 câu hỏi định hướng**:

1. **Tôi chia bài toán ở đâu?** (Tại điểm giữa $mid$, theo trục tọa độ $x$, hay qua $pivot$?)
2. **Bài toán con có kích thước bao nhiêu?** ($N/2, N_1, N_2$?)
3. **Tôi cần giải bao nhiêu bài toán con?** (Chỉ 1 nhánh như Binary Search/QuickSelect hay cả 2 nhánh như Merge Sort?)
4. **Tôi combine kết quả của các bài toán con như thế nào?** (Đây là bước quyết định độ phức tạp!)



![Cây quyết định lựa chọn thuật toán Chia để trị](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-11-chia-de-tri/assets/dnc_decision_tree_vi.png)



## 5. Mô phỏng từng bước thuật toán sắp xếp trộn (Merge Sort simulation)

Xét mảng ban đầu: `A = [38, 27, 43, 3, 9, 82, 10]`.

### Sơ đồ cây phân rã & gộp mảng (divide & merge tree):



![Mô phỏng Cây phân rã và gộp Merge Sort](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-11-chia-de-tri/assets/mergesort_tree_vi.png)



## 6. Combine step & loop invariant — Trái tim của Divide & Conquer

> **Chân lý sư phạm:** Sức mạnh và sự tinh tế của Chia Để Trị không nằm ở việc "bẻ nhỏ bài toán", mà nằm ở **cách ta xử lý và kết hợp (Combine) các kết quả ở pha Unwinding**.

### Bất biến vòng lặp (loop invariant) trong hàm `merge()`:
Khi gộp 2 mảng con đã sắp xếp $a[l..mid]$ và $a[mid+1..r]$ vào $temp$:

* **Bất biến:** Tại mỗi bước lặp, mảng đệm $temp[l..k-1]$ luôn chứa chính xác $(k - l)$ phần tử nhỏ nhất đã được chọn từ hai nửa $a[l..mid]$ và $a[mid+1..r]$ theo thứ tự không giảm.
* **Quy tắc chọn:**
* Nếu $a[i] \le a[j]$: Chọn $a[i]$ đưa vào `temp[k]`, tăng $i$ và $k$ (điều kiện $\le$ bảo toàn tính **Stable Sort**).
* Nếu $a[i] > a[j]$: Chọn $a[j]$ đưa vào `temp[k]`, tăng $j$ và $k$.

## 7. Bảng trực giác recurrence & định lý thợ (Master Theorem)

Trước khi dùng công thức tổng quát, hãy nắm vững **4 hệ thức truy hồi kinh điển**:

| Hệ Thức Truy Hồi | Cấu Trúc Nhánh | Chi Phí Từng Tầng | Độ Phức Tạp | Thuật Toán Tiêu Biểu |
|---|---|---|:---:|---|
| $T(N) = T(N/2) + \mathcal{O}(1)$ | 1 nhánh, giảm nửa | $\mathcal{O}(1)$ mỗi tầng | $\Theta(\log N)$ | Binary Search |
| $T(N) = T(N/2) + \mathcal{O}(N)$ | 1 nhánh, quét $N$ | $N + N/2 + N/4 + \dots$ | $\Theta(N)$ (Expected) | QuickSelect |
| $T(N) = 2T(N/2) + \mathcal{O}(1)$| 2 nhánh, gộp $\mathcal{O}(1)$ | Số lá $N$ thống trị | $\Theta(N)$ | Tìm Min/Max chia đôi |
| $T(N) = 2T(N/2) + \mathcal{O}(N)$| 2 nhánh, gộp $\mathcal{O}(N)$ | Mỗi tầng đều tốn $\mathcal{O}(N)$ | $\Theta(N \log N)$ | Merge Sort, Inversion |

### Công thức tổng quát (Master Theorem):
Với $T(N) = a \cdot T(N/b) + \Theta(N^d)$ ($a \ge 1, b > 1$):

1. **$a < b^d$ ($\log_b a < d$):** Chi phí ngoài đệ quy thống trị $\implies T(N) = \Theta(N^d)$.
2. **$a = b^d$ ($\log_b a = d$):** Chi phí phân bố đều trên $\log_b N$ tầng $\implies T(N) = \Theta(N^d \log N)$.
3. **$a > b^d$ ($\log_b a > d$):** Số nút lá bùng nổ thống trị $\implies T(N) = \Theta(N^{\log_b a})$ (ví dụ Karatsuba $a=3, b=2, d=1 \implies \Theta(N^{\log_2 3}) \approx \Theta(N^{1.585})$).

## 8. Bảng nhận diện dấu hiệu thuật toán (d&c pattern recognition)

| Dấu Hiệu Đặc Trưng | Mô Hình Thuật Toán D&C Phù Hợp |
|---|---|
| Mảng đã sắp xếp + cần tìm kiếm một giá trị | **Binary Search đệ quy** (D&C đơn nhánh) |
| Chia đôi mảng + cần sắp xếp cả 2 nửa | **Merge Sort** (D&C đa nhánh + Combine 2 con trỏ) |
| Cần đếm số cặp phần tử có quan hệ giữa 2 nửa | **Inversion Counting** (Đếm khi Merge) |
| Cần tìm phần tử nhỏ thứ $K$ trên mảng chưa sắp xếp | **QuickSelect** (Partition chọn 1 nhánh) |
| Tìm max / min trong mô hình cây thi đấu đấu loại | **Tournament Tree** (Lưu lịch sử đối đầu) |
| Tìm đoạn con liên tiếp có tính chất tối ưu | **Maximum Subarray D&C** (Xét đoạn vắt qua $mid$) |
| Tập điểm trong không gian 2D cần tìm khoảng cách min | **Closest Pair of Points** (Chia hoành độ + Quét Strip) |
| Tìm trung vị của 2 dãy đã sắp xếp | **Binary Partition D&C** ($\mathcal{O}(\log(\min)))$ |

## 9. Chuỗi chuyển giao tri thức: Merge $\to$ Merge Sort $\to$ inversion counting

Điểm đặc sắc nhất của chuyên đề là **chuỗi kế thừa thuật toán**:

$\text{Merge Step (2 con trỏ)} \longrightarrow \text{Merge Sort } \Theta(N \log N) \longrightarrow \text{Đếm Nghịch Thế (Inversion Count)}$

### Ứng dụng đỉnh cao: Đếm cặp nghịch thế (inversion counting) $\mathcal{O}(N \log N)$

* **Khái niệm:** Cặp nghịch thế là cặp chỉ số $(i, j)$ sao cho $i < j$ nhưng $A_i > A_j$.

* **Bất biến gộp kỳ diệu:** Khi chia mảng thành $\text{Left}[l..mid]$ và $\text{Right}[mid+1..r]$ đã sắp xếp:
* Khi duyệt con trỏ $i$ trên $Left$ và $j$ trên $Right$, nếu $L[i] > R[j]$, thì do $L$ đã sắp xếp tăng dần, **toàn bộ các phần tử từ $L[i]$ đến $L[mid]$ đều lớn hơn $R[j]$**!

* Ta cộng ngay một lượng bằng $(mid - i + 1)$ vào biến đếm nghịch thế trong **$\mathcal{O}(1)$ thao tác cộng dồn**.
* Bước $merge$ vẫn tốn $\mathcal{O}(N)$ thời gian, giúp tổng thời gian đếm toàn bộ mảng đạt $\Theta(N \log N)$ chuẩn thi đấu thay vì $\mathcal{O}(N^2)$ vét cạn.

## 10. Các bẫy lỗi lập trình kinh điển (bug traps)

1. **Bẫy cấp phát bộ nhớ đệm trong Merge Sort:**
* Việc tạo các `vector` mới bên trong mỗi lần gọi `mergeSort()` gây thêm nhiều lần cấp phát/giải phóng động và sao chép dữ liệu, làm tăng constant factor.
* **Cách phòng chống:** Khai báo một mảng đệm toàn cục duy nhất `vector<long long> temp(N);` và truyền tham chiếu vào hàm đệ quy để tái sử dụng cho mọi bước gộp, giữ Auxiliary Memory ở mức $\Theta(N)$.

2. **Tràn số nguyên 32-bit khi đếm số cặp nghịch thế:**
* Số lượng cặp nghịch thế tối đa của mảng $N = 10^5$ là $N(N-1)/2 \approx 5 \times 10^9$ (vượt giới hạn của `int` $2 \times 10^9$).
* **Cách phòng chống:** Biến đếm nghịch thế bắt buộc dùng kiểu `long long`.
3. **Bẫy tràn số khi tính Midpoint:**
* Viết `mid = (l + r) / 2;` có thể tràn `int` khi $l + r > 2 \cdot 10^9$. Luôn viết: `mid = l + (r - l) / 2;`.

4. **Bẫy bỏ sót đoạn crossing trong Maximum Subarray:**
* Đoạn con lớn nhất có thể nằm trọn bên trái, trọn bên phải, hoặc vắt ngang qua tâm $mid$. Bắt buộc phải tính $maxCrossingSum$ từ $mid$ lan sang 2 phía.

## 11. Mẫu cài đặt chuẩn thi đấu (competitive templates)

```cpp
# include <bits/stdc++.h>
using namespace std;

using ll = long long;

// 1. Thuật toán Merge Sort chuẩn O(N log N) dùng buffer tái sử dụng
void merge(vector<ll> &a, vector<ll> &temp, int l, int mid, int r) {

    int i = l, j = mid + 1, k = l;
    while (i <= mid && j <= r) {
        // <= giữ tính stable: phần tử bên trái thắng khi bằng nhau
        if (a[i] <= a[j]) temp[k++] = a[i++];
        else temp[k++] = a[j++];
    }
    while (i <= mid) temp[k++] = a[i++];
    while (j <= r) temp[k++] = a[j++];
    for (int idx = l; idx <= r; ++idx) a[idx] = temp[idx];
}

void mergeSort(vector<ll> &a, vector<ll> &temp, int l, int r) {

    if (l >= r) return;
    int mid = l + (r - l) / 2;
    mergeSort(a, temp, l, mid);
    mergeSort(a, temp, mid + 1, r);
    merge(a, temp, l, mid, r);
}

// 2. Thuật toán Đếm Số Cặp Nghịch Thế O(N log N)
ll countInversions(vector<ll> &a, vector<ll> &temp, int l, int r) {

    if (l >= r) return 0;
    int mid = l + (r - l) / 2;
    ll inv = 0;
    inv += countInversions(a, temp, l, mid);
    inv += countInversions(a, temp, mid + 1, r);

    int i = l, j = mid + 1, k = l;
    while (i <= mid && j <= r) {
        if (a[i] <= a[j]) {
            temp[k++] = a[i++];
        } else {
            temp[k++] = a[j++];
            inv += (mid - i + 1); // Đếm O(1) nhờ cấu trúc đã sắp xếp
        }
    }
    while (i <= mid) temp[k++] = a[i++];
    while (j <= r) temp[k++] = a[j++];
    for (int idx = l; idx <= r; ++idx) a[idx] = temp[idx];
    return inv;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<ll> a = {38, 27, 43, 3, 9, 82, 10};

    int n = a.size();
    vector<ll> temp(n);

    cout << "So cap nghich the: " << countInversions(a, temp, 0, n - 1) << "\n";
    return 0;
}
```

## Bài tập thực hành


### Bài 01 [CPPB-DAC-01]: Tìm Kiếm Nhị Phân Bằng Đệ Quy (Cầu Nối Sang D&C)

**Bối cảnh:** Cho mảng số nguyên $A$ gồm $N$ phần tử đã được sắp xếp tăng dần và số nguyên $X$. Hãy sử dụng hàm đệ quy Chia Để Trị `binarySearchDac(l, r, x)` để tìm vị trí xuất hiện đầu tiên của $X$ trong mảng (chỉ số 1-based). Nếu không tìm thấy, in ra `-1`.

**Đầu vào (Input):**

- Dòng 1: Hai số nguyên $N, X$ ($1 \le N \le 10^5, |X| \le 10^9$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ đã sắp xếp tăng dần ($|A_i| \le 10^9$).

**Đầu ra (Output):**

- In ra vị trí 1-based của $X$ trong mảng, hoặc `-1` nếu không tồn tại.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 7 <br> 1 3 5 7 9 | 4 |

**Ràng buộc & Giới hạn:**

- 100% số test có $N \le 10^5, |A_i| \le 10^9$.



### Bài 02 [CPPB-DAC-13]: Thuật Toán QuickSelect Tìm K-th Element

**Bối cảnh:** Cho mảng số nguyên $A$ gồm $N$ phần tử và số nguyên $K$ ($1 \le K \le N$). Hãy tìm phần tử nhỏ thứ $K$ trong mảng bằng thuật toán QuickSelect Chia Để Trị đạt thời gian trung bình $\mathcal{O}(N)$.

**Đầu vào (Input):**

- Dòng 1: Hai số nguyên $N, K$ ($1 \le K \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, \dots, A_N$ ($|A_i| \le 10^9$).

**Đầu ra (Output):**

- In ra giá trị của phần tử nhỏ thứ $K$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 6 3 <br> 7 10 4 3 20 15 | 7 |

**Ràng buộc & Giới hạn:**

- 100% số test có $N \le 10^5, |A_i| \le 10^9$.



### Bài 03 [CPPB-DAC-01]: Tìm Kiếm Nhị Phân Bằng Đệ Quy (Cầu Nối Sang D&C)

**Bối cảnh:** Cho mảng số nguyên $A$ gồm $N$ phần tử đã được sắp xếp tăng dần và số nguyên $X$. Hãy sử dụng hàm đệ quy Chia Để Trị `binarySearchDac(l, r, x)` để tìm vị trí xuất hiện đầu tiên của $X$ trong mảng (chỉ số 1-based). Nếu không tìm thấy, in ra `-1`.

**Đầu vào (Input):**

- Dòng 1: Hai số nguyên $N, X$ ($1 \le N \le 10^5, |X| \le 10^9$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ đã sắp xếp tăng dần ($|A_i| \le 10^9$).

**Đầu ra (Output):**

- In ra vị trí 1-based của $X$ trong mảng, hoặc `-1` nếu không tồn tại.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 7 <br> 1 3 5 7 9 | 4 |

**Ràng buộc & Giới hạn:**

- 100% số test có $N \le 10^5, |A_i| \le 10^9$.



### Bài 04 [CPPB-DAC-02]: Tìm Min Trên Đoạn Bằng Chia Để Trị (RMQ D&C Cơ Bản)

**Bối cảnh:** Cho mảng số nguyên $A$ gồm $N$ phần tử. Hãy cài đặt hàm đệ quy Chia để trị `queryMin(l, r)` để tìm giá trị nhỏ nhất trong mảng $A$.

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($|A_i| \le 10^9$).

**Đầu ra (Output):**

- In ra giá trị nhỏ nhất trong mảng $A$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 6 <br> 4 2 7 1 9 3 | 1 |

**Ràng buộc & Giới hạn:**

- 100% số test có $N \le 10^5, |A_i| \le 10^9$.



### Bài 05 [CPPB-DAC-03]: Tìm Phần Tử Lớn Thứ Hai (Tournament Tree)

**Bối cảnh:** Cho mảng số nguyên $A$ gồm $N$ phần tử đôi một phân biệt. Hãy sử dụng mô hình cây thi đấu Chia Để Trị (Tournament Tree) để tìm phần tử lớn thứ hai trong mảng với số phép so sánh tối ưu $N + \lceil \log_2 N \rceil - 2$.

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $N$ ($2 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên phân biệt $A_1, \dots, A_N$ ($|A_i| \le 10^9$).

**Đầu ra (Output):**

- In ra giá trị của phần tử lớn thứ hai trong mảng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 <br> 8 3 10 5 7 | 8 |

**Ràng buộc & Giới hạn:**

- 100% số test có $2 \le N \le 10^5, |A_i| \le 10^9$.



### Bài 06 [CPPB-DAC-04]: Gộp Hai Mảng Đã Sắp Xếp (Merge Step)

**Bối cảnh:** Cho 2 dãy số nguyên $A$ (gồm $N$ phần tử) và $B$ (gồm $M$ phần tử) đều đã được sắp xếp tăng dần. Hãy cài đặt bước gộp `merge()` bằng kỹ thuật 2 con trỏ trong $\mathcal{O}(N + M)$ để gộp $A$ và $B$ thành một dãy số tăng dần duy nhất.

**Đầu vào (Input):**

- Dòng 1: Hai số nguyên $N, M$ ($1 \le N, M \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, \dots, A_N$ đã sắp xếp tăng dần ($|A_i| \le 10^9$).
- Dòng 3: $M$ số nguyên $B_1, \dots, B_M$ đã sắp xếp tăng dần ($|B_j| \le 10^9$).

**Đầu ra (Output):**

- In ra $N + M$ số nguyên của mảng sau khi gộp, cách nhau bởi dấu cách.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 4 <br> 1 5 8 <br> 2 3 6 9 | 1 2 3 5 6 8 9 |

**Ràng buộc & Giới hạn:**

- 100% số test có $N, M \le 10^5, |A_i|, |B_j| \le 10^9$.



### Bài 07 [CPPB-DAC-05]: Thuật Toán Sắp Xếp Trộn (Merge Sort)

**Bối cảnh:** Cho mảng số nguyên $A$ gồm $N$ phần tử. Hãy tự cài đặt hoàn chỉnh thuật toán Sắp Xếp Trộn (Merge Sort) theo mô hình Chia Để Trị để sắp xếp mảng $A$ theo thứ tự tăng dần.

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($|A_i| \le 10^9$).

**Đầu ra (Output):**

- In ra $N$ phần tử của mảng sau khi sắp xếp tăng dần, cách nhau bởi dấu cách.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 7 <br> 38 27 43 3 9 82 10 | 3 9 10 27 38 43 82 |

**Ràng buộc & Giới hạn:**

- 100% số test có $1 \le N \le 10^5, |A_i| \le 10^9$.



### Bài 08 [CPPB-DAC-06]: Đếm Số Cặp Nghịch Thế (Inversion Count)

**Bối cảnh:** Cho mảng số nguyên $A$ gồm $N$ phần tử. Cặp chỉ số $(i, j)$ được gọi là một cặp nghịch thế nếu $1 \le i < j \le N$ và $A_i > A_j$. Hãy tính tổng số cặp nghịch thế trong mảng bằng thuật toán Merge Sort $\mathcal{O}(N \log N)$.

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($|A_i| \le 10^9$).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là tổng số cặp nghịch thế trong mảng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 <br> 2 4 1 3 5 | 3 |

**Ràng buộc & Giới hạn:**

- 100% số test có $1 \le N \le 10^5, |A_i| \le 10^9$.



### Bài 09 [CPPB-DAC-07]: Đoạn Con Tổng Lớn Nhất (Maximum Subarray D&C)

**Bối cảnh:** Cho mảng số nguyên $A$ gồm $N$ phần tử (có thể chứa số âm). Hãy tìm tổng lớn nhất của một đoạn con liên tiếp khác rỗng bằng thuật toán Chia Để Trị $\mathcal{O}(N \log N)$ (`max(Left, Right, Crossing)`).

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($|A_i| \le 10^9$).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là tổng lớn nhất của đoạn con liên tiếp.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 8 <br> -2 -3 4 -1 -2 1 5 -3 | 7 |

**Ràng buộc & Giới hạn:**

- 100% số test có $1 \le N \le 10^5, |A_i| \le 10^9$.



### Bài 10 [CPPB-DAC-08]: Tìm Phần Tử Đa Số (Majority Element) D&C

**Bối cảnh:** Cho mảng số nguyên $A$ gồm $N$ phần tử. Phần tử đa số là phần tử xuất hiện nhiều hơn $\lfloor N / 2 \rfloor$ lần. Hãy sử dụng thuật toán Chia Để Trị để tìm phần tử đa số. Nếu không tồn tại, in ra `-1`.

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, \dots, A_N$ ($|A_i| \le 10^9$).

**Đầu ra (Output):**

- In ra phần tử đa số, hoặc `-1` nếu không có.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 7 <br> 2 2 1 1 2 2 3 | 2 |

**Ràng buộc & Giới hạn:**

- 100% số test có $N \le 10^5, |A_i| \le 10^9$.



### Bài 11 [CPPB-DAC-09]: Lũy Thừa Ma Trận Chia Để Trị 2x2

**Bối cảnh:** Cho ma trận vuông $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ cấp $2 \times 2$ và số nguyên không âm $N$. Hãy tính ma trận $A^N \pmod M$ bằng thuật toán Lũy thừa nhị phân Chia Để Trị trong $\mathcal{O}(\log N)$.

**Đầu vào (Input):**

- Dòng 1: 4 số nguyên $a, b, c, d$ ($0 \le a, b, c, d \le 10^9$).
- Dòng 2: Hai số nguyên $N, M$ ($0 \le N \le 10^{18}, 1 \le M \le 10^9 + 7$).

**Đầu ra (Output):**

- In ra ma trận kết quả 2 dòng, mỗi dòng 2 phần tử cách nhau bởi dấu cách.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 1 1 <br> 1 0 <br> 4 1000 | 5 3 <br> 3 2 |

**Ràng buộc & Giới hạn:**

- 100% số test có $N \le 10^{18}, M \le 10^9 + 7$.



### Bài 12 [CPPB-DAC-10]: Tìm Điểm Cực Đại Mảng Unimodal (Peak Index)

**Bối cảnh:** Một mảng $A$ được gọi là Unimodal (mảng đỉnh núi) nếu nó tăng nghiêm ngặt đến một vị trí đỉnh $p$ rồi sau đó giảm nghiêm ngặt ($A_1 < A_2 < \dots < A_p > A_{p+1} > \dots > A_N$). Hãy tìm giá trị cực đại $A_p$ trong $\mathcal{O}(\log N)$ bằng Chia Để Trị.

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $N$ ($3 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên của mảng Unimodal $A_1, \dots, A_N$ ($|A_i| \le 10^9$).

**Đầu ra (Output):**

- In ra giá trị cực đại $A_p$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 7 <br> 1 3 8 12 9 4 2 | 12 |

**Ràng buộc & Giới hạn:**

- 100% số test có $3 \le N \le 10^5, |A_i| \le 10^9$.



### Bài 13 [CPPB-DAC-11]: Tính Tổng Cấp Số Nhân D&C

**Bối cảnh:** Cho 3 số nguyên $A, N, M$. Hãy tính tổng cấp số nhân $S(N) = A^0 + A^1 + A^2 + \dots + A^N \pmod M$ bằng kỹ thuật Chia Để Trị trong $\mathcal{O}(\log N)$ theo hệ thức $S(2k+1) = S(k) \times (1 + A^{k+1})$.

**Đầu vào (Input):**

- Một dòng duy nhất chứa 3 số nguyên $A, N, M$ ($0 \le A, N \le 10^9, 1 \le M \le 10^9 + 7$).

**Đầu ra (Output):**

- In ra giá trị $S(N) \pmod M$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 2 3 1000 | 15 |

**Ràng buộc & Giới hạn:**

- 100% số test có $N \le 10^9, M \le 10^9 + 7$.



### Bài 14 [CPPB-DAC-12]: Đếm Số Cặp A_i > 2 * A_j (Significant Inversions)

**Bối cảnh:** Cho mảng số nguyên $A$ gồm $N$ phần tử. Hãy đếm số cặp chỉ số $(i, j)$ thỏa mãn $1 \le i < j \le N$ và $A_i > 2 \times A_j$ bằng biến thể Merge Sort Chia Để Trị trong $\mathcal{O}(N \log N)$.

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, \dots, A_N$ ($|A_i| \le 10^9$).

**Đầu ra (Output):**

- In ra số lượng cặp thỏa mãn điều kiện.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 <br> 1 3 2 3 1 | 2 |

**Ràng buộc & Giới hạn:**

- 100% số test có $N \le 10^5, |A_i| \le 10^9$.



### Bài 15 [CPPB-DAC-13]: Thuật Toán QuickSelect Tìm K-th Element

**Bối cảnh:** Cho mảng số nguyên $A$ gồm $N$ phần tử và số nguyên $K$ ($1 \le K \le N$). Hãy tìm phần tử nhỏ thứ $K$ trong mảng bằng thuật toán QuickSelect Chia Để Trị đạt thời gian trung bình $\mathcal{O}(N)$.

**Đầu vào (Input):**

- Dòng 1: Hai số nguyên $N, K$ ($1 \le K \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, \dots, A_N$ ($|A_i| \le 10^9$).

**Đầu ra (Output):**

- In ra giá trị của phần tử nhỏ thứ $K$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 6 3 <br> 7 10 4 3 20 15 | 7 |

**Ràng buộc & Giới hạn:**

- 100% số test có $N \le 10^5, |A_i| \le 10^9$.



### Bài 16 [CPPB-DAC-14]: Đếm Số Đoạn Con Tổng Trong Đoạn [L, R]

**Bối cảnh:** Cho mảng số nguyên $A$ gồm $N$ phần tử và hai số nguyên $Lower, Upper$. Hãy đếm số lượng đoạn con liên tiếp khác rỗng $A[i..j]$ ($1 \le i \le j \le N$) có tổng $\sum_{k=i}^j A_k$ nằm trong đoạn $[Lower, Upper]$ bằng Chia Để Trị trên mảng tiền tố (Prefix Sum Merge Count) trong $\mathcal{O}(N \log N)$.

**Đầu vào (Input):**

- Dòng 1: 3 số nguyên $N, Lower, Upper$ ($1 \le N \le 10^5, -10^{14} \le Lower \le Upper \le 10^{14}$).
- Dòng 2: $N$ số nguyên $A_1, \dots, A_N$ ($|A_i| \le 10^9$).

**Đầu ra (Output):**

- In ra số lượng đoạn con thỏa mãn.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 -2 2 <br> 0 -3 1 | 3 |

**Ràng buộc & Giới hạn:**

- 100% số test có $N \le 10^5, |A_i| \le 10^9$.



### Bài 17 [CPPB-DAC-15]: Cặp Điểm Gần Nhất (Closest Pair of Points)

**Bối cảnh:** Cho $N$ điểm trên mặt phẳng tọa độ $2D$. Hãy tìm khoảng cách Euclidean nhỏ nhất giữa 2 điểm bất kỳ trong tập hợp bằng thuật toán Chia Để Trị $\mathcal{O}(N \log N)$ (chia đôi theo hoành độ và quét dải Strip $\le 7$ điểm).

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $N$ ($2 \le N \le 5 \cdot 10^4$).
- $N$ dòng tiếp theo: Mỗi dòng chứa 2 số nguyên $X_i, Y_i$ ($|X_i|, |Y_i| \le 10^9$).

**Đầu ra (Output):**

- In ra bình phương khoảng cách nhỏ nhất giữa 2 điểm (để tránh sai số số thực).

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 <br> 0 0 <br> 1 1 <br> 2 4 <br> 3 1 | 2 |

**Ràng buộc & Giới hạn:**

- 100% số test có $2 \le N \le 5 \cdot 10^4, |X_i|, |Y_i| \le 10^9$.



### Bài 18 [CPPB-DAC-16]: Median Của Hai Mảng Đã Sắp Xếp

**Bối cảnh:** Cho 2 mảng số nguyên $A$ (gồm $N$ phần tử) và $B$ (gồm $M$ phần tử) đều đã được sắp xếp tăng dần. Hãy tìm phần tử trung vị (Median) của tập hợp hợp nhất $A \cup B$ trong thời gian tối ưu $\mathcal{O}(\log(\min(N, M)))$ bằng kỹ thuật Chia đôi không gian phân hoạch.

**Đầu vào (Input):**

- Dòng 1: Hai số nguyên $N, M$ ($1 \le N, M \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, \dots, A_N$ ($|A_i| \le 10^9$).
- Dòng 3: $M$ số nguyên $B_1, \dots, B_M$ ($|B_j| \le 10^9$).

**Đầu ra (Output):**

- In ra giá trị trung vị (nếu tổng số phần tử $N + M$ chẵn, in phần tử thứ $(N+M)/2$ theo thứ tự 1-based làm tròn dưới).

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 2 2 <br> 1 3 <br> 2 4 | 2 |

**Ràng buộc & Giới hạn:**

- 100% số test có $N, M \le 10^5, |A_i|, |B_j| \le 10^9$.




# Bài 12: Thuật toán quay lui & nhánh cận

## 1. Cầu nối kiến trúc: Recursion $\to$ Divide & Conquer $\to$ state-space search $\to$ Dynamic Programming

Để có cái nhìn toàn cảnh về các phương pháp giải thuật lớn trong Lập trình thi đấu:



![Cầu nối kiến trúc các phương pháp thuật toán lớn: Đệ quy -> D&C / Quay lui / Nhánh cận -> Quy hoạch động](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-12-quay-lui-nhanh-can/assets/search_paradigms_bridge_vi.png)



* **Divide & Conquer:** $\text{Bài toán lớn} \longrightarrow \text{Các bài toán con riêng biệt}$.
* **Backtracking / State-Space Search:** $\text{Trạng thái hiện tại} \longrightarrow \text{Các nhánh quyết định thử nghiệm (Choices)}$.
* **Dynamic Programming:** $\text{Nhiều đường đi khác nhau} \longrightarrow \text{Cùng một State Identity (Overlapping States)} \implies \text{Memoization / Bảng DP}$.

## 2. Bản chất trạng thái (state definition & state identity)

### Khái niệm state (trạng thái) & state identity:

> **Định nghĩa:** **State (Trạng thái)** là tập thông tin tối thiểu cần thiết để xác định chính xác các lựa chọn tiếp theo và kết quả có thể đạt được từ trạng thái hiện tại.
>
> * **Không phải mọi biến xuất hiện trong hàm đệ quy đều là thành phần của State Identity; chỉ những thông tin có thể làm thay đổi các lựa chọn hoặc kết quả của phần còn lại mới cần thiết.**

> * **Trong cài đặt DFS / Quay lui:** State bao gồm cả dữ liệu cấu hình đang xây dựng và các đại lượng tích lũy (`current_value`, `current_cost`).
> * **Khi chuyển sang Quy Hoạch Động (DP):** Ta chắt lọc những biến thực sự tạo nên **"State Identity"** (ví dụ: `dp[index][remaining_weight]` hoặc `dp[city][mask]`), còn giá trị mục tiêu trở thành giá trị lưu trong bảng DP thay vì là tham số đệ quy.

| Bài Toán | State Trong Cài Đặt DFS | State Identity Khi Chuyển Sang DP (Nếu có Memoization/DP) |
|---|---|---|
| **Sinh Hoán Vị** | `(step, visited[], cur[])` | *Thường không dùng DP kiểu thông thường (trừ Bitmask DP về sau)* |
| **N-Queens** | `(row, col_used[], diag1[], diag2[])` | *Không tự động trở thành DP chỉ vì có State (thiếu cấu trúc con tối ưu)* |
| **Subset Sum** | `(index, current_sum, cur_set[])` | `dp[index][current_sum]` |
| **Cái Túi 0/1 (Knapsack)** | `(index, current_weight, current_value)` | `dp[index][remaining_weight]` |
| **Người Du Lịch (TSP)** | `(current_city, visited_mask, current_cost)` | `dp[current_city][visited_mask]` |
| **Sudoku 9x9** | `(board[9][9], empty_cells_list)` | *Không phải ví dụ DP điển hình (CSP Backtracking)* |

> **Quy luật cốt lõi:** Không phải cứ có State là có thể chuyển sang DP. Để chuyển sang DP, bài toán bắt buộc phải có **State Identity gọn gàng** + **Hiện tượng trùng lặp trạng thái (Overlapping Subproblems)** + **Cấu trúc con tối ưu (Optimal Substructure)**.

## 3. Khung phương pháp luận: Design-time framework vs runtime pattern

### 1. Khung thiết kế thuật toán (design-time framework):

1. **Define State:** Xác định các biến trạng thái tối thiểu cần thiết để mô tả bài toán.
2. **Generate Candidates:** Xác định danh sách các lựa chọn khả dĩ tại mỗi bước đi.
3. **Define Feasibility:** Thiết lập điều kiện ràng buộc hợp lệ (Feasibility Pruning).
4. **Define Bound:** Thiết lập hàm cận dưới $LB$ hoặc cận trên $UB$ nếu là bài toán tối ưu (Branch & Bound).
5. **Define Transition & Restoration:** Thiết lập quy tắc chuyển trạng thái (`Choose`), gọi đệ quy (`Explore`) và hoàn tác (`Unchoose`).

### 2. Khung thực thi mã nguồn (runtime pattern):
```cpp
void search(State state) {
    if (isGoal(state)) {
        processSolution(state);
        return;
    }
    for (const auto &candidate : getCandidates(state)) {
        if (!isFeasible(state, candidate)) continue; // Feasibility Pruning

        if (boundSaysImpossible(state, candidate)) continue; // Optimality Pruning (B&B)

        choose(state, candidate);  // 1. Chuyển sang State_new
        search(state);             // 2. Đi sâu vào nhánh con (Explore)
        unchoose(state, candidate);// 3. Hoàn tác về State_before (Restoration)
    }
}
```

## 4. Khung tư duy mental model: Hai sơ đồ cốt lõi của lesson 12



![Cây tìm kiếm không gian trạng thái: Quay lui và Nhánh cận](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-12-quay-lui-nhanh-can/assets/state_space_tree_vi.png)



### Quy trình 1: Luồng ra quyết định quay lui thuần túy (backtracking)

### Quy trình 2: Luồng ra quyết định nhánh cận (Branch & Bound)

## 5. Bất biến trung tâm: State restoration invariant

> **Quy luật cốt lõi:** `Choose-Explore-Unchoose` là một pattern cài đặt phổ biến. Bản chất kỹ thuật sâu sắc là **Bất biến Khôi phục Trạng Thái (State Restoration Invariant)**:

> $\text{State}_{\text{before}} \xrightarrow{\text{Choose}} \text{State}_{\text{new}} \xrightarrow{\text{Explore}} \text{Subtree} \xrightarrow{\text{Unchoose}} \text{State}_{\text{before}}$
> Sau khi khám phá xong một nhánh con và hàm con return, trạng thái phải được trả về **nguyên vẹn 100%** như trước khi bước vào nhánh đó, đảm bảo nhánh kế tiếp bắt đầu từ cùng một trạng thái cha.

## 6. Phân biệt cắt tỉa ràng buộc (feasibility) vs cắt tỉa tối ưu (Branch & Bound)

* **BACKTRACKING:** *"Xây dựng nghiệm từng bước + quay lui khi cần (có thể không cần pruning như sinh nhị phân)"*
* **FEASIBILITY PRUNING:** *"Cắt những trạng thái chắc chắn không thể dẫn tới nghiệm hợp lệ"*
* **BRANCH AND BOUND:** *"Framework tìm kiếm tối ưu trên không gian trạng thái, kết hợp hàm Cận (Bound) để cắt tỉa nhánh không thể tốt hơn best hiện tại"*

> **Lưu ý mở rộng:** Trong chuyên đề này, ta triển khai Branch & Bound trên nền DFS / Backtracking để nắm vững nguyên lý. Về tổng quát, Branch & Bound là một framework tìm kiếm tối ưu có thể triển khai bằng Best-First Search với hàng đợi ưu tiên `priority_queue` hoặc BFS.

### Định nghĩa chuẩn xác: $OPT(\text{state})$ vs $best$ hiện tại:

* **$OPT(\text{state})$:** Giá trị tốt nhất thực sự có thể đạt được khi hoàn thành nghiệm từ trạng thái hiện tại.
* **$best$ (hoặc $best\_so\_far$ / $incumbent$):** Nghiệm tốt nhất đã tìm thấy trên toàn bộ các nhánh đã khám phá tính đến thời điểm hiện tại (chưa chắc là nghiệm tối ưu toàn cục cho đến khi duyệt xong).

### Nguyên tắc thiết lập hàm bound chuẩn xác:

1. **Với bài toán Cực Tiểu Hóa (Minimization - ví dụ TSP, Đổi tiền ít xu nhất, Job Assignment):**
* Ta duy trì hàm Cận Dưới $LB(\text{state}) \le OPT(\text{state})$.
* **Điều kiện cắt tỉa:** Nếu $LB(\text{state}) \ge \text{best}$, thì $OPT(\text{state}) \ge LB(\text{state}) \ge \text{best} \implies$ **Cắt tỉa ngay!**
* *Ví dụ:* $best = 100$. Nếu tại một nhánh ta tính được $LB = 105 \implies$ Cắt tỉa ngay vì $OPT \ge 105 > 100$. Nếu $LB = 95 \implies$ **Không được cắt tỉa** vì $OPT$ có thể là $95, 98$ tốt hơn $100$.

2. **Với bài toán Cực Đại Hóa (Maximization - ví dụ Cái túi Knapsack $0/1$):**
* Ta duy trì hàm Cận Trên $UB(\text{state}) \ge OPT(\text{state})$.
* **Điều kiện cắt tỉa:** Nếu $UB(\text{state}) \le \text{best}$, thì $OPT(\text{state}) \le UB(\text{state}) \le \text{best} \implies$ **Cắt tỉa ngay!**

> **Mối liên hệ giữa Heuristic Ordering & Branch and Bound:** Heuristic ordering giúp tìm ra nghiệm tốt sớm hơn $\implies best$ được cải thiện nhanh hơn $\implies$ Hàm Bound cắt tỉa được nhiều nhánh hơn $\implies$ Thuật toán B&B chạy nhanh hơn vượt trội!

## 7. Phân loại 4 cấp độ kỹ thuật trong tìm kiếm toàn vẹn

| Kỹ Thuật | Ảnh Hưởng Đến Tính Đúng Đắn | Vai Trò Thuật Toán |
|---|:---:|---|
| **Feasibility Pruning Hợp Lệ** | Không mất nghiệm hợp lệ | Loại bỏ trạng thái chắc chắn vi phạm ràng buộc bài toán. |
| **Valid Lower / Upper Bound** | Không mất nghiệm tối ưu | Loại bỏ trạng thái đã chứng minh toán học không thể vượt qua `best`. |
| **Heuristic Ordering** | Không làm mất nghiệm | Sắp xếp thứ tự thử nhánh (như Warnsdorff) để tìm thấy nghiệm tốt sớm hơn; tính đầy đủ vẫn bảo toàn nếu duyệt hết. |
| **Heuristic Pruning không chứng minh** | Có nguy cơ mất nghiệm | Cắt nhánh theo cảm tính, có nguy cơ bỏ sót nghiệm tối ưu toàn cục. |

## 8. Cầu nối sâu sang DP: Từ cây tìm kiếm (search tree) đến đồ thị trạng thái (state DAG)



![Từ Cây tìm kiếm Search Tree đến Đồ thị trạng thái State DAG](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-12-quay-lui-nhanh-can/assets/state_dag_overlapping_vi.png)



* **Duyệt cây thuần túy (Tree Search):** Phải tính toán lại trạng thái `E` nhiều lần ở các nhánh con khác nhau.
* **Quan điểm Đồ thị (State DAG View):** `E` chỉ là một đỉnh duy nhất trong không gian trạng thái.
* **Quy Hoạch Động (Dynamic Programming / Memoization):** Trong những bài toán mà State Identity có số lượng trạng thái đa thức theo kích thước input, Memoization/DP có thể giảm một cây tìm kiếm hàm mũ xuống $\text{Số trạng thái} \times \text{Chi phí chuyển trạng thái}$; ví dụ Knapsack đạt $\mathcal{O}(N \cdot W)$ khi $W$ là tham số giới hạn. Với các bài như TSP, Bitmask DP đạt $\mathcal{O}(N^2 \cdot 2^N)$ nhanh hơn rất nhiều so với vét cạn $N!$.

## 9. Các bẫy lỗi lập trình kinh điển (bug traps)

1. **Quên hoàn tác trạng thái (Missing Unchoose Step):**
* Sau khi gọi đệ quy `backtrack(i + 1)`, quên viết `visited[val] = false;` hoặc `cur_sum -= val;` $\implies$ Trạng thái của nhánh trước bị rò rỉ sang nhánh sau, làm mất toàn bộ các nghiệm tiếp theo.
2. **Bẫy cắt tỉa `break` trong Subset Sum có số âm:**
* Lệnh `if (current_sum + A[i] > S) break;` chỉ an toàn khi **mọi phần tử $A_i > 0$** và mảng đã sort tăng dần. Tuyệt đối không áp dụng nguyên trạng cho mảng có phần tử âm!

3. **Đánh dấu sai mảng các họ đường chéo trong bài $N$-Queens:**
* Với chỉ số 1-based:
* Họ đường chéo xuôi `\`: $row - col \in [-(N-1), N-1] \implies row - col + N \in [1, 2N-1]$.
* Họ đường chéo ngược `/`: $row + col \in [2, 2N]$.
* Khai báo `diag1` và `diag2` tối thiểu kích thước $2N + 1$.
4. **Giả thiết về mệnh giá xu trong Coin Change:**
* Mọi mệnh giá xu $C_i \ge 1$ để đảm bảo độ sâu tối đa bị chặn trên bởi $\lfloor S / C_{\min} \rfloor$.

## 10. Mẫu cài đặt chuẩn thi đấu (competitive templates)

```cpp
# include <bits/stdc++.h>
using namespace std;

using ll = long long;

// 1. Sinh Hoán Vị 1..N chuẩn State Restoration Invariant
int n = 3;
vector<int> cur;

vector<bool> visited;

void genPermutations(int step) {
    if (step > n) {

        for (int i = 0; i < n; ++i) cout << cur[i] << (i + 1 == n ? "" : " ");
        cout << "\n";
        return;
    }
    for (int val = 1; val <= n; ++val) {
        if (!visited[val]) {
            visited[val] = true;       // 1. CHOOSE
            cur.push_back(val);
            genPermutations(step + 1); // 2. EXPLORE
            cur.pop_back();            // 3. UNCHOOSE (Khôi phục)
            visited[val] = false;
        }
    }
}

// 2. Bài Toán N-Queens (Đếm số cách đặt N quân hậu)
int n_queens = 4;
ll queen_ways = 0;
vector<bool> col_used, diag1_used, diag2_used;

void solveNQueens(int row) {
    if (row > n_queens) {

        queen_ways++;
        return;
    }
    for (int col = 1; col <= n_queens; ++col) {
        if (!col_used[col] && !diag1_used[row - col + n_queens] && !diag2_used[row + col]) {
            col_used[col] = diag1_used[row - col + n_queens] = diag2_used[row + col] = true; // CHOOSE
            solveNQueens(row + 1); // EXPLORE
            col_used[col] = diag1_used[row - col + n_queens] = diag2_used[row + col] = false; // UNCHOOSE
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    visited.assign(n + 1, false);
    genPermutations(1);

    col_used.assign(n_queens + 1, false);
    diag1_used.assign(2 * n_queens + 1, false);
    diag2_used.assign(2 * n_queens + 1, false);
    solveNQueens(1);
    cout << "So cach dat " << n_queens << " quan hau: " << queen_ways << "\n";
    return 0;
}
```

## Bài tập thực hành


### Bài 01 [CPPB-BKT-01]: Sinh Tất Cả Xâu Nhị Phân Độ Dài N

**Bối cảnh:** Cho số nguyên dương $N$. Hãy sinh tất cả các xâu nhị phân độ dài $N$ theo thứ tự từ điển bằng thuật toán Quay Lui chuẩn mực (`Choose` $\to$ `Explore` $\to$ `Unchoose`).

**Đầu vào (Input):**

- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 16$).

**Đầu ra (Output):**

- In ra tất cả các xâu nhị phân độ dài $N$, mỗi xâu trên một dòng theo thứ tự từ điển.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 | 000 <br> 001 <br> 010 <br> 011 <br> 100 <br> 101 <br> 110 <br> 111 |

**Ràng buộc & Giới hạn:**

- 100% số test có $1 \le N \le 16$.



### Bài 02 [CPPB-BKT-05]: Sinh Dãy Ngoặc Hợp Lệ Độ Dài 2N

**Bối cảnh:** Cho số nguyên dương $N$. Hãy sinh tất cả các dãy ngoặc đúng gồm $N$ cặp ngoặc tròn `()` theo thứ tự từ điển bằng thuật toán Quay Lui có cắt tỉa khả thi (`open < N`, `close < open`).

**Đầu vào (Input):**

- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10$).

**Đầu ra (Output):**

- In ra tất cả các dãy ngoặc đúng độ dài $2N$, mỗi dãy trên một dòng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 | ((())) <br> (()()) <br> (())() <br> ()(()) <br> ()()() |

**Ràng buộc & Giới hạn:**

- 100% số test có $1 \le N \le 10$.



### Bài 03 [CPPB-BKT-10]: Đổi Tiền Xu Ít Nhất (B&B Coin Change)

**Bối cảnh:** Cho $N$ mệnh giá tiền xu $C_1, C_2, \dots, C_N$ (số lượng mỗi loại không giới hạn) và số tiền cần đổi $S$. Hãy tìm số lượng đồng xu ít nhất để đổi đúng số tiền $S$ bằng thuật toán Nhánh Cận (Branch and Bound). Nếu không đổi được, in `-1`.

**Đầu vào (Input):**

- Dòng 1: Hai số nguyên $N, S$ ($1 \le N \le 15, 1 \le S \le 100$).
- Dòng 2: $N$ số nguyên dương $C_1, \dots, C_N$ ($1 \le C_i \le 100$).

**Đầu ra (Output):**

- In ra số đồng xu ít nhất, hoặc `-1`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 11 <br> 1 2 5 | 3 |

**Ràng buộc & Giới hạn:**

- 100% số test có $N \le 15, S \le 100$.



### Bài 04 [CPPB-BKT-11]: Mã Đi Tuần (Knight's Tour)

**Bối cảnh:** Cho bàn cờ $N \times N$. Quân mã xuất phát từ ô $(R, C)$ (1-based). Hãy tìm một hành trình di chuyển quân mã đi qua tất cả $N^2$ ô đúng 1 lần bằng thuật toán Quay Lui kết hợp quy tắc sắp xếp thứ tự nhánh Warnsdorff. In ra ma trận $N \times N$ ghi số thứ tự các bước đi từ $1$ đến $N^2$, hoặc `-1` nếu không có.

**Đầu vào (Input):**

- Một dòng duy nhất chứa 3 số nguyên $N, R, C$ ($1 \le N \le 6, 1 \le R, C \le N$).

**Đầu ra (Output):**

- In ra ma trận $N \times N$ các bước đi, hoặc `-1`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 1 1 | 1 16 11 6 25 <br> 10 5 24 15 20 <br> 17 2 19 22 7 <br> 4 9 14 21 12 <br> 3 18 23 8 13 |

**Ràng buộc & Giới hạn:**

- 100% số test có $N \le 6, 1 \le R, C \le N$.



### Bài 05 [CPPB-BKT-01]: Sinh Tất Cả Xâu Nhị Phân Độ Dài N

**Bối cảnh:** Cho số nguyên dương $N$. Hãy sinh tất cả các xâu nhị phân độ dài $N$ theo thứ tự từ điển bằng thuật toán Quay Lui chuẩn mực (`Choose` $\to$ `Explore` $\to$ `Unchoose`).

**Đầu vào (Input):**

- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 16$).

**Đầu ra (Output):**

- In ra tất cả các xâu nhị phân độ dài $N$, mỗi xâu trên một dòng theo thứ tự từ điển.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 | 000 <br> 001 <br> 010 <br> 011 <br> 100 <br> 101 <br> 110 <br> 111 |

**Ràng buộc & Giới hạn:**

- 100% số test có $1 \le N \le 16$.



### Bài 06 [CPPB-BKT-02]: Sinh Tất Cả Tập Con Của Tập N Phần Tử

**Bối cảnh:** Cho tập hợp $S = \{1, 2, \dots, N\}$. Hãy sinh tất cả các tập con của $S$ (kể cả tập rỗng) theo thứ tự từ điển bằng thuật toán Quay Lui dạng Chọn / Bỏ qua.

**Đầu vào (Input):**

- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 16$).

**Đầu ra (Output):**

- In ra các tập con, mỗi tập con trên một dòng (in các phần tử cách nhau bởi dấu cách, tập rỗng in dòng trống).

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 | 3 <br> 2 <br> 2 3 <br> 1 <br> 1 3 <br> 1 2 <br> 1 2 3 |

**Ràng buộc & Giới hạn:**

- 100% số test có $1 \le N \le 16$.



### Bài 07 [CPPB-BKT-03]: Sinh Tất Cả Hoán Vị 1..N

**Bối cảnh:** Cho số nguyên dương $N$. Hãy sinh tất cả các hoán vị của tập hợp $\{1, 2, \dots, N\}$ theo thứ tự từ điển bằng thuật toán Quay Lui có mảng đánh dấu `visited[]`.

**Đầu vào (Input):**

- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 8$).

**Đầu ra (Output):**

- In ra tất cả $N!$ hoán vị, mỗi hoán vị trên một dòng, các phần tử cách nhau bởi dấu cách.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 | 1 2 3 <br> 1 3 2 <br> 2 1 3 <br> 2 3 1 <br> 3 1 2 <br> 3 2 1 |

**Ràng buộc & Giới hạn:**

- 100% số test có $1 \le N \le 8$.



### Bài 08 [CPPB-BKT-04]: Sinh Tất Cả Tổ Hợp Chập K Của N

**Bối cảnh:** Cho 2 số nguyên $N, K$ ($1 \le K \le N \le 16$). Hãy sinh tất cả các tổ hợp chập $K$ của $\{1, 2, \dots, N\}$ theo thứ tự từ điển bằng thuật toán Quay Lui.

**Đầu vào (Input):**

- Một dòng duy nhất chứa 2 số nguyên $N, K$ ($1 \le K \le N \le 16$).

**Đầu ra (Output):**

- In ra tất cả các tổ hợp chập $K$, mỗi tổ hợp trên một dòng cách nhau bởi dấu cách.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 2 | 1 2 <br> 1 3 <br> 1 4 <br> 2 3 <br> 2 4 <br> 3 4 |

**Ràng buộc & Giới hạn:**

- 100% số test có $1 \le K \le N \le 16$.



### Bài 09 [CPPB-BKT-05]: Sinh Dãy Ngoặc Hợp Lệ Độ Dài 2N

**Bối cảnh:** Cho số nguyên dương $N$. Hãy sinh tất cả các dãy ngoặc đúng gồm $N$ cặp ngoặc tròn `()` theo thứ tự từ điển bằng thuật toán Quay Lui có cắt tỉa khả thi (`open < N`, `close < open`).

**Đầu vào (Input):**

- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10$).

**Đầu ra (Output):**

- In ra tất cả các dãy ngoặc đúng độ dài $2N$, mỗi dãy trên một dòng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 | ((())) <br> (()()) <br> (())() <br> ()(()) <br> ()()() |

**Ràng buộc & Giới hạn:**

- 100% số test có $1 \le N \le 10$.



### Bài 10 [CPPB-BKT-06]: Bài Toán N-Queens (Đếm Số Cách)

**Bối cảnh:** Cho số nguyên dương $N$. Hãy đếm số cách đặt $N$ quân hậu lên bàn cờ $N \times N$ sao cho không có 2 quân hậu nào khống chế lẫn nhau (không cùng hàng, không cùng cột, không cùng đường chéo).

**Đầu vào (Input):**

- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 12$).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là số cách đặt $N$ quân hậu.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 | 2 |

**Ràng buộc & Giới hạn:**

- 100% số test có $1 \le N \le 12$.



### Bài 11 [CPPB-BKT-07]: Mê Cung (Rat in a Maze): Tìm Mọi Đường Đi

**Bối cảnh:** Cho mê cung $N \times N$ gồm các ô `1` (đi được) và `0` (tường đá). Con chuột xuất phát từ ô $(0, 0)$ cần đi tới ô $(N-1, N-1)$. Mỗi bước chỉ được đi sang các ô kề cạnh (Down `D`, Left `L`, Right `R`, Up `U`). Hãy in ra tất cả các đường đi hợp lệ theo thứ tự từ điển (`D < L < R < U`). Nếu không có đường đi, in `-1`.

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $N$ ($2 \le N \le 8$).
- $N$ dòng tiếp theo: Mỗi dòng gồm $N$ số nguyên `0` hoặc `1`.

**Đầu ra (Output):**

- In ra các xâu ký tự đại diện cho các đường đi tìm được (mỗi đường trên một dòng), hoặc `-1`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 <br> 1 0 0 0 <br> 1 1 0 1 <br> 0 1 0 0 <br> 1 1 1 1 | DDRDRR <br> DRDDRR |

**Ràng buộc & Giới hạn:**

- 100% số test có $2 \le N \le 8$.



### Bài 12 [CPPB-BKT-08]: Tập Con Có Tổng Bằng S (Subset Sum)

**Bối cảnh:** Cho mảng số nguyên dương $A$ gồm $N$ phần tử và số nguyên dương $S$. Hãy in ra tất cả các tập con của $A$ có tổng đúng bằng $S$ theo thứ tự từ điển bằng thuật toán Quay Lui có cắt tỉa khả thi (`current_sum > S`). Nếu không có tập nào, in `-1`.

**Đầu vào (Input):**

- Dòng 1: Hai số nguyên $N, S$ ($1 \le N \le 20, 1 \le S \le 1000$).
- Dòng 2: $N$ số nguyên dương $A_1, \dots, A_N$ ($1 \le A_i \le 100$).

**Đầu ra (Output):**

- In ra các tập con thỏa mãn (mỗi tập trên một dòng, các phần tử cách nhau bởi dấu cách), hoặc `-1`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 6 <br> 1 2 3 5 | 1 2 3 <br> 1 5 |

**Ràng buộc & Giới hạn:**

- 100% số test có $N \le 20, S \le 1000$.



### Bài 13 [CPPB-BKT-09]: Chia Tập Thành 2 Phần Có Tổng Bằng Nhau

**Bối cảnh:** Cho mảng số nguyên dương $A$ gồm $N$ phần tử. Hãy kiểm tra xem có thể chia tập $A$ thành 2 tập con rời nhau sao cho tổng các phần tử của 2 tập con bằng nhau hay không. In `YES` nếu được, ngược lại in `NO`.

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 20$).
- Dòng 2: $N$ số nguyên dương $A_1, \dots, A_N$ ($1 \le A_i \le 100$).

**Đầu ra (Output):**

- In `YES` hoặc `NO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 <br> 1 5 11 5 | YES |

**Ràng buộc & Giới hạn:**

- 100% số test có $1 \le N \le 20, A_i \le 100$.



### Bài 14 [CPPB-BKT-10]: Đổi Tiền Xu Ít Nhất (B&B Coin Change)

**Bối cảnh:** Cho $N$ mệnh giá tiền xu $C_1, C_2, \dots, C_N$ (số lượng mỗi loại không giới hạn) và số tiền cần đổi $S$. Hãy tìm số lượng đồng xu ít nhất để đổi đúng số tiền $S$ bằng thuật toán Nhánh Cận (Branch and Bound). Nếu không đổi được, in `-1`.

**Đầu vào (Input):**

- Dòng 1: Hai số nguyên $N, S$ ($1 \le N \le 15, 1 \le S \le 100$).
- Dòng 2: $N$ số nguyên dương $C_1, \dots, C_N$ ($1 \le C_i \le 100$).

**Đầu ra (Output):**

- In ra số đồng xu ít nhất, hoặc `-1`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 11 <br> 1 2 5 | 3 |

**Ràng buộc & Giới hạn:**

- 100% số test có $N \le 15, S \le 100$.



### Bài 15 [CPPB-BKT-11]: Mã Đi Tuần (Knight's Tour)

**Bối cảnh:** Cho bàn cờ $N \times N$. Quân mã xuất phát từ ô $(R, C)$ (1-based). Hãy tìm một hành trình di chuyển quân mã đi qua tất cả $N^2$ ô đúng 1 lần bằng thuật toán Quay Lui kết hợp quy tắc sắp xếp thứ tự nhánh Warnsdorff. In ra ma trận $N \times N$ ghi số thứ tự các bước đi từ $1$ đến $N^2$, hoặc `-1` nếu không có.

**Đầu vào (Input):**

- Một dòng duy nhất chứa 3 số nguyên $N, R, C$ ($1 \le N \le 6, 1 \le R, C \le N$).

**Đầu ra (Output):**

- In ra ma trận $N \times N$ các bước đi, hoặc `-1`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 1 1 | 1 16 11 6 25 <br> 10 5 24 15 20 <br> 17 2 19 22 7 <br> 4 9 14 21 12 <br> 3 18 23 8 13 |

**Ràng buộc & Giới hạn:**

- 100% số test có $N \le 6, 1 \le R, C \le N$.



### Bài 16 [CPPB-BKT-12]: Trò Chơi Sudoku 9x9

**Bối cảnh:** Cho bảng Sudoku $9 \times 9$ với các ô trống mang giá trị `0`. Hãy điền các số từ $1$ đến $9$ vào các ô trống sao cho mỗi hàng, mỗi cột và mỗi khối vuông con $3 \times 3$ đều chứa đủ các chữ số từ $1$ đến $9$ không trùng lặp bằng thuật toán Quay Lui.

**Đầu vào (Input):**

- 9 dòng, mỗi dòng chứa 9 số nguyên từ $0$ đến $9$.

**Đầu ra (Output):**

- In ra bảng Sudoku hoàn chỉnh sau khi điền 9 dòng, mỗi dòng 9 số cách nhau bởi dấu cách.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 0 6 5 0 8 4 0 0 <br> 5 2 0 0 0 0 0 0 0 <br> 0 8 7 0 0 0 0 3 1 <br> 0 0 3 0 1 0 0 8 0 <br> 9 0 0 8 6 3 0 0 5 <br> 0 5 0 0 9 0 6 0 0 <br> 1 3 0 0 0 0 2 5 0 <br> 0 0 0 0 0 0 0 7 4 <br> 0 0 5 2 0 6 3 0 0 | 3 1 6 5 7 8 4 9 2 <br> 5 2 9 1 3 4 7 6 8 <br> 4 8 7 6 2 9 5 3 1 <br> 2 6 3 4 1 5 9 8 7 <br> 9 7 4 8 6 3 1 2 5 <br> 8 5 1 7 9 2 6 4 3 <br> 1 3 8 9 4 7 2 5 6 <br> 6 9 2 3 5 1 8 7 4 <br> 7 4 5 2 8 6 3 1 9 |

**Ràng buộc & Giới hạn:**

- Đảm bảo bảng đầu vào có lời giải duy nhất.



### Bài 17 [CPPB-BKT-13]: Bài Toán Cái Túi 0/1 Nhánh Cận (B&B Knapsack)

**Bối cảnh:** Cho $N$ đồ vật, mỗi đồ vật $i$ có trọng lượng $W_i$ và giá trị $V_i$. Một cái túi có sức chứa tối đa $M$. Hãy tìm tổng giá trị lớn nhất của các đồ vật chọn vào túi bằng thuật toán Nhánh Cận (Branch and Bound) sử dụng hàm cận trên Fractional Knapsack.

**Đầu vào (Input):**

- Dòng 1: Hai số nguyên $N, M$ ($1 \le N \le 25, 1 \le M \le 10^9$).
- $N$ dòng tiếp theo: Mỗi dòng gồm 2 số nguyên $W_i, V_i$ ($1 \le W_i, V_i \le 10^7$).

**Đầu ra (Output):**

- In ra giá trị lớn nhất có thể đạt được.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 10 <br> 3 40 <br> 4 50 <br> 5 60 <br> 6 70 | 120 |

**Ràng buộc & Giới hạn:**

- 100% số test có $N \le 25, M \le 10^9$.



### Bài 18 [CPPB-BKT-14]: Người Du Lịch (TSP) Nhánh Cận

**Bối cảnh:** Cho $N$ thành phố và ma trận khoảng cách $C$ cấp $N \times N$. Hãy tìm chi phí nhỏ nhất của một chu trình xuất phát từ thành phố $1$, đi qua tất cả các thành phố còn lại đúng 1 lần rồi quay về thành phố $1$ bằng thuật toán Nhánh Cận (Branch and Bound).

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $N$ ($2 \le N \le 13$).
- $N$ dòng tiếp theo: Ma trận $C_{N \times N}$ ($0 \le C_{i, j} \le 10^6$, $C_{i, i} = 0$).

**Đầu ra (Output):**

- In ra chi phí nhỏ nhất của chu trình Hamilton.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 <br> 0 10 15 20 <br> 10 0 35 25 <br> 15 35 0 30 <br> 20 25 30 0 | 80 |

**Ràng buộc & Giới hạn:**

- 100% số test có $2 \le N \le 13$.



### Bài 19 [CPPB-BKT-15]: Tô Màu Đồ Thị (Graph K-Coloring)

**Bối cảnh:** Cho đồ thị vô hướng $G = (V, E)$ gồm $V$ đỉnh và $E$ cạnh, cùng số màu $K$. Hãy kiểm tra xem có thể tô màu $V$ đỉnh bằng $K$ màu sao cho không có 2 đỉnh kề nhau có cùng màu hay không. In `YES` nếu tô được, ngược lại in `NO`.

**Đầu vào (Input):**

- Dòng 1: 3 số nguyên $V, E, K$ ($1 \le V \le 12, 0 \le E \le V(V-1)/2, 1 \le K \le 4$).
- $E$ dòng tiếp theo: Mỗi dòng gồm 2 số nguyên $u, v$ mô tả một cạnh ($1 \le u, v \le V$).

**Đầu ra (Output):**

- In `YES` hoặc `NO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 5 3 <br> 1 2 <br> 2 3 <br> 3 4 <br> 4 1 <br> 1 3 | YES |

**Ràng buộc & Giới hạn:**

- 100% số test có $V \le 12, K \le 4$.



### Bài 20 [CPPB-BKT-16]: Phân Công Công Việc Tối Ưu (Job Assignment B&B)

**Bối cảnh:** Cho $N$ công nhân và $N$ công việc. Ma trận $C_{N \times N}$ cho biết chi phí $C_{i, j}$ nếu giao công nhân $i$ làm việc $j$. Mỗi công nhân làm đúng 1 việc, mỗi việc do đúng 1 người làm. Hãy tìm tổng chi phí phân công nhỏ nhất bằng thuật toán Nhánh Cận (Branch and Bound).

**Đầu vào (Input):**

- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 12$).
- $N$ dòng tiếp theo: Ma trận chi phí $C_{N \times N}$ ($0 \le C_{i, j} \le 10^6$).

**Đầu ra (Output):**

- In ra tổng chi phí phân công nhỏ nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 <br> 9 2 7 8 <br> 6 4 3 7 <br> 5 8 1 8 <br> 7 6 9 4 | 13 |

**Ràng buộc & Giới hạn:**

- 100% số test có $1 \le N \le 12$.



# CHƯƠNG 05: QUY HOẠCH ĐỘNG (DYNAMIC PROGRAMMING)


# Bài 13: Quy hoạch động 1D & dãy con tăng dài nhất

## 1. Bản chất vấn đề & cầu nối từ đệ quy sang quy hoạch động

Trong Bài 10 và 12, ta đã chứng kiến hiện tượng **Bùng nổ Không gian Trạng thái (Combinatorial Explosion)** khi duyệt đệ quy phân nhánh:

* Khi tính số Fibonacci $F(N) = F(N-1) + F(N-2)$, trạng thái $F(3)$ bị tính lại $2$ lần, $F(2)$ bị tính lại $3$ lần. Độ phức tạp thời gian tăng vọt lên cấp số nhân $\Theta(\varphi^N) \approx \Theta(1.618^N)$.
* **Nguyên nhân gốc rễ:** Hàm đệ quy thuần túy không có cơ chế "ghi nhớ" (Memory). Mỗi lần bước vào một nhánh mới, nó xem bài toán con đó như một thực thể hoàn toàn xa lạ và tính toán lại từ đầu.

**Quy Hoạch Động (Dynamic Programming - DP)** giải quyết vấn đề này bằng nguyên lý cốt lõi:

> **DP loại bỏ việc tính toán lại các bài toán con trùng lặp bằng cách lưu trữ kết quả vào Bảng phương án (DP Table) và tái sử dụng ngay lập tức trong $\mathcal{O}(1)$.**



![Mô hình Đồ thị trạng thái DAG Quy hoạch động 1D](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-13-quy-hoach-dong-1d/assets/dp_1d_state_dag_vi.png)



## 2. Khung phương pháp luận: 7 bước DP state invariant

Để giải quyết chính xác bất kỳ bài toán Quy hoạch động nào, ta áp dụng khung 7 thành phần logic chuẩn mực:

1. **State Definition & Invariant (Định nghĩa Trạng thái & Bất biến):** $dp[i]$ đại diện chính xác $100\%$ cho đại lượng nào? (Là giá trị tối ưu, số cách thực hiện, hay trạng thái logic?).
2. **Base Cases (Trường hợp cơ sở):** Các trạng thái biên nhỏ nhất không thể phân rã thêm ($i = 0, 1$) có giá trị bằng bao nhiêu?
3. **State Transition (Hệ thức chuyển trạng thái):** Trạng thái $dp[i]$ phụ thuộc vào các trạng thái con `dp[j]` ($j < i$) nào trước đó qua công thức toán học nào?
4. **Evaluation Order (Thứ tự tính toán):** Chiều duyệt vòng lặp ($i = 1 \to N$ xuôi hay ngược) theo thứ tự Topo DAG để đảm bảo mọi bài toán con phụ thuộc đều đã được tính xong trước khi dùng.
5. **Answer Extraction (Trích xuất kết quả):** Đáp án của bài toán gốc nằm ở đâu? (Tại `dp[N]`, hay $\max_{i=1}^N dp[i]$?).
6. **Space & Time Optimization (Tối ưu hóa):** Phân tích độ phức tạp thời gian $\mathcal{O}(\text{Time})$, bộ nhớ $\mathcal{O}(\text{Space})$ và khả năng nén mảng.
7. **Reconstruction (Khôi phục nghiệm):** Dùng mảng truy vết `trace[i]` hoặc duyệt ngược trên bảng `dp` để tái tạo lại cấu hình nghiệm tối ưu (*Ghi `N/A` nếu bài toán chỉ yêu cầu giá trị*).

## 3. Các mô hình quy hoạch động 1D cốt lõi (core patterns)

### 3.1. Mô hình bậc thang & bước nhảy (staircase / frog jump)

* **Bối cảnh:** Một chú ếch đứng ở bậc $0$, muốn nhảy lên bậc $N$. Tại mỗi bậc, ếch có thể nhảy $1$ bước hoặc $2$ bước.
* **State Definition:** $dp[i]$ là số cách khác nhau để ếch nhảy từ bậc $0$ đến bậc $i$.
* **Base Cases:** `dp[0] = 1` (có đúng một cách để hoàn thành hành trình từ bậc 0 đến bậc 0 — không thực hiện bước nhảy nào), `dp[1] = 1`.
* **State Transition:** Để đến bậc $i$, bước nhảy cuối cùng bắt buộc phải xuất phát từ bậc $i-1$ (nhảy 1 bước) hoặc bậc $i-2$ (nhảy 2 bước):
$$dp[i] = dp[i-1] + dp[i-2] \pmod{10^9+7}$$

* **Evaluation Order:** Duyệt xuôi từ $i = 2 \to N$.

### 3.2. Mô hình đổi tiền ít xu nhất (coin change 1D)

* **Bối cảnh:** Cho hệ thống gồm $K$ đồng xu có mệnh giá $C = \{c_1, c_2, \dots, c_K\}$. Cần đổi số tiền $S$ sao cho tổng số đồng xu là ít nhất.
* **State Definition:** $dp[i]$ là số lượng đồng xu **ít nhất** để tạo ra đúng tổng giá trị $i$.
* **Base Cases:** `dp[0] = 0` (Tổng tiền bằng 0 cần đúng 0 đồng xu). Khởi tạo mọi `dp[i] = \infty` với $i \ge 1$.
* **State Transition:** Thử chọn đồng xu cuối cùng là mệnh giá $c \in C$:
$$dp[i] = 1 + \min_{\{c \in C \mid i \ge c\}} dp[i - c]$$

* **Evaluation Order:** Duyệt xuôi $i = 1 \to S$. Nếu $dp[S] = \infty \implies$ Không thể đổi được.

> **Lưu ý quan trọng:** Quy tắc thứ tự vòng lặp phân biệt Hoán vị / Tổ hợp dưới đây áp dụng cho **bài toán đếm số cách**. Với bài toán tối ưu số đồng xu ít nhất $dp[i] = 1 + \min(dp[i-c])$, do phép toán $\min$ có tính chất giao hoán và kết hợp nên ta luôn duyệt $i$ từ $1 \to S$ mà không làm thay đổi giá trị tối ưu.

* **Phân biệt Sư phạm Cốt lõi Trong Bài Toán Đếm Số Cách (Counting Coin Change):**
* **Bài toán Hoán vị (Permutation):** Thứ tự các đồng xu có phân biệt (ví dụ $1+2 \neq 2+1$ (khác $2+1$)). Vòng lặp ngoài duyệt Tiền $i = 1 \to S$, vòng lặp trong thử từng đồng xu $c \in C$.
* **Bài toán Tổ hợp (Combination):** Thứ tự các đồng xu không phân biệt (ví dụ $1+2$ và $2+1$ là một cách). Vòng lặp ngoài duyệt từng đồng xu $c \in C$, vòng lặp trong duyệt Tiền $i = c \to S$.



![Bài toán Đổi tiền Coin Change và DAG trạng thái](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-13-quy-hoach-dong-1d/assets/coin_change_dag_vi.png)



### 3.3. Dãy con tăng dài nhất (longest increasing subsequence — LIS $\mathcal{O}(N^2)$)

* **Bối cảnh:** Cho dãy số $A = [a_1, a_2, \dots, a_N]$. Tìm độ dài dãy con tăng nghiêm ngặt dài nhất.
* **State Definition (Tử huyệt định nghĩa):** $dp[i]$ là độ dài của dãy con tăng dài nhất **kết thúc bắt buộc tại phần tử $A[i]$**.
* **Base Cases:** `dp[i] = 1` với mọi $1 \le i \le N$ (bản thân mỗi phần tử đơn lẻ là dãy con độ dài 1).
* **State Transition:** Duyệt qua mọi phần tử $A[j]$ đứng trước $A[i]$ ($1 \le j < i$):
$$dp[i] = 1 + \max_{\{1 \le j < i \mid A[j] < A[i]\}} dp[j]$$

* **Answer Extraction:** Kết quả toàn cục là $\max_{i=1}^N dp[i]$.
* **Độ phức tạp:** $\mathcal{O}(N^2)$ thời gian, $\mathcal{O}(N)$ bộ nhớ. Thường phù hợp với $N$ cỡ vài nghìn, tùy thuộc vào time limit và hệ số hằng số.



![Mô hình Dãy con tăng dài nhất LIS O(N^2) và Truy vết](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-13-quy-hoach-dong-1d/assets/lis_quadratic_model_vi.png)



### 3.4. Kỹ thuật khôi phục vết nghiệm 1D (traceback / reconstruction)
Để in ra chính xác cấu hình dãy phần tử tạo nên nghiệm tối ưu:

1. Duy trì mảng `trace[i] = j` ghi nhận chỉ số phần tử đứng ngay trước $A[i]$ trong cấu hình tối ưu.
2. Tìm vị trí $best\_idx$ có $dp[best\_idx]$ đạt cực trị.
3. Lần ngược mảng `trace` từ $best\_idx$ về điểm xuất phát, lưu các phần tử vào một vector rồi đảo ngược (`reverse`).

### 3.5. Mở rộng nâng cao: LIS $\mathcal{O}(N \log N)$ bằng Binary Search
Khi $N \le 10^5$, thuật toán $\mathcal{O}(N^2)$ sẽ bị Quá thời gian (TLE).

* **Ý tưởng:** Duy trì mảng phụ `tails` trong C++ (chỉ số 0-based), trong đó phần tử $tails[len - 1]$ lưu **giá trị phần tử kết thúc nhỏ nhất** của một dãy con tăng có độ dài đúng bằng `len`.
* Mảng $tails$ luôn có tính chất **đơn điệu tăng dần** $\implies$ Dùng Tìm kiếm nhị phân (`lower_bound`) để tìm và cập nhật vị trí thích hợp cho mỗi $A[i]$ trong $\mathcal{O}(\log N)$.
* **Tổng thời gian:** $\mathcal{O}(N \log N)$. Đây là kỹ thuật mở rộng tối ưu hóa nâng cao (Challenge Extension).

## 4. Các biến thể thiết kế trạng thái từ mô hình 1D (state design variations)

Mục tiêu lớn nhất của Module 05 không phải là học thuộc các công thức, mà là rèn luyện khả năng **Thiết Kế Trạng Thái (State Design)** trước các biến thể bài toán mới:

### 4.1. Pattern a: Quyết định nhị phân (binary choice — Chọn / bỏ qua)

* **Bối cảnh (House Robber):** Không được chọn hai phần tử liền kề nhau.
* **State Invariant:** $dp[i]$ là tổng giá trị lớn nhất khi chỉ xét tiền tố từ $1 \dots i$.
* **Transition:** Tại vị trí $i$, có 2 lựa chọn loại trừ lẫn nhau:
$$dp[i] = \max(\underbrace{dp[i-1]}_{\text{Không chọn } i}, \underbrace{dp[i-2] + A[i]}_{\text{Chọn } i \implies \text{bỏ qua } i-1})$$

* **Chuyển đổi bài toán (Delete and Earn):** Khi chọn giá trị $v$, ta nhận toàn bộ tổng điểm $points[v] = v \times count(v)$ nhưng bị cấm chọn $v-1$ và $v+1$. Bằng cách gom nhóm dữ liệu theo trục giá trị $v$, bài toán được quy đổi hoàn toàn về mô hình House Robber trên mảng $points$.

### 4.2. Pattern b: Mở rộng trạng thái hữu hạn (state dimension expansion)

* **Bối cảnh (Alternating Subsequence):** Dãy con đan dấu (tăng $\to$ giảm $\to$ tăng $\to$ giảm).
* **Vấn đề:** Nếu chỉ dùng $dp[i]$, ta không biết phần tử $A[i]$ đang đóng vai trò là "đỉnh tăng" hay "đáy giảm".
* **Thiết kế Trạng thái:** Bổ sung thêm một chiều trạng thái hữu hạn $\text{state} \in \{0, 1\}$:
* `dp[i][0]`: Độ dài dãy đan dấu kết thúc tại $A[i]$ với bước nhảy cuối cùng là **GIẢM** ($A[j] > A[i]$).

* `dp[i][1]`: Độ dài dãy đan dấu kết thúc tại $A[i]$ với bước nhảy cuối cùng là **TĂNG** ($A[j] < A[i]$).
* *Lưu ý:* Chiều bắt đầu của dãy con có thể linh hoạt bắt đầu bằng tăng hoặc giảm tùy theo yêu cầu đề bài; kết quả toàn cục thường là $\max(\max_i dp[i][0], \max_i dp[i][1])$.
* > **Lưu ý:** Với dãy có độ dài 1, chưa tồn tại bước nhảy tăng/giảm; giá trị khởi tạo cụ thể của `dp[i][0]`, `dp[i][1]` phụ thuộc vào định nghĩa bài toán và cách triển khai. Phần này được xem như mô hình mở rộng, không phải template cài đặt đầy đủ trong chuyên đề này.

### 4.3. Pattern c: Thay đổi đại lượng tối ưu (maximum sum increasing subsequence — Msis)

* **Bối cảnh:** Thay vì tìm dãy con tăng có *độ dài lớn nhất*, bài toán yêu cầu tìm dãy con tăng có **tổng giá trị các phần tử lớn nhất**.
* **Điều chỉnh Invariant:**
* LIS: $dp[i]$ = độ dài LIS $\implies dp[i] = 1 + \max(dp[j])$.
* MSIS: $dp[i]$ = **Tổng lớn nhất** của dãy con tăng kết thúc tại $A[i]$:
$$dp[i] = A[i] + \max_{\{j < i \mid A[j] < A[i]\}} dp[j]$$

### 4.4. Pattern d: Phân hoạch đoạn tối ưu (pattern mở rộng / preview — Optimal array partitioning & rod cutting)

* **Bối cảnh:** Cắt một thanh gỗ độ dài $N$ (hoặc phân chia dãy số $A[1 \dots N]$ thành các đoạn con liên tiếp) sao cho tổng giá trị/chi phí là tối ưu.
* **State Invariant:** $dp[i]$ là chi phí/giá trị tối ưu khi phân hoạch tiền tố $A[1 \dots i]$.
* **Transition:** Thử mọi điểm cắt cuối cùng $j \in [0, i-1]$:
$$dp[i] = \min_{0 \le j < i, \text{valid}(j+1, i)} (dp[j] + \text{cost}(j+1, i))$$

* **Áp dụng cho bài Mastery `CPPB-DP1-15`:** Tìm cách phân chia dãy số thành các khối đoạn con thỏa mãn điều kiện ràng buộc với chi phí nhỏ nhất.

## 5. Các bẫy lỗi lập trình kinh điển (bug traps)

1. **Bẫy khởi tạo giá trị vô cùng (Infinity Overflow):**
* Khi tìm giá trị nhỏ nhất, nếu dùng `INT_MAX` cho kiểu `int`, phép tính `dp[i-c] + 1` sẽ gây tràn số thành số âm cực lớn.
* **Quy tắc an toàn:** Dùng hằng số `const long long INF = 1e18;` (hoặc `1LL << 60`) và luôn kiểm tra `if (dp[i - c] != INF)` trước khi chuyển trạng thái.
2. **Bẫy định nghĩa sai Trạng thái trong LIS:**
* Ngộ nhận: *"dp[i] là độ dài LIS trong đoạn từ 1 đến i"*. Nếu định nghĩa như vậy, ta không thể biết phần tử kết thúc là bao nhiêu để so sánh với $A[i+1]$.
* **Bất biến đúng:** Bắt buộc $dp[i]$ phải là độ dài LIS kết thúc tại chính $A[i]$.
3. **Bẫy nhầm lẫn thứ tự vòng lặp trong Coin Change Đếm Số Cách:**
* Duyệt Tiền trước, Coin sau $\implies$ Tạo ra bài toán Hoán vị (đếm lặp thứ tự).
* Duyệt Coin trước, Tiền sau $\implies$ Tạo ra bài toán Tổ hợp (đếm không trùng lặp).

## 6. Mẫu cài đặt chuẩn thi đấu (competitive templates)

### Mẫu 1: Dãy con tăng dài nhất LIS $\mathcal{O}(N^2)$ kèm truy vết nghiệm

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    if (n <= 0) return 0;

    vector<long long> a(n);

    for (int i = 0; i < n; ++i) {
        cin >> a[i];

    }

    vector<int> dp(n, 1);

    vector<int> trace(n, -1);

    int max_len = 1;
    int best_end = 0;

    // Quy hoạch động O(N^2)
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
            if (a[j] < a[i] && dp[j] + 1 > dp[i]) {

                dp[i] = dp[j] + 1;
                trace[i] = j;
            }
        }
        if (dp[i] > max_len) {

            max_len = dp[i];
            best_end = i;
        }
    }

    cout << max_len << "\n";

    // Khôi phục vết nghiệm
    vector<long long> lis_elements;

    int curr = best_end;
    while (curr != -1) {
        lis_elements.push_back(a[curr]);
        curr = trace[curr];
    }
    reverse(lis_elements.begin(), lis_elements.end());

    for (int i = 0; i < (int)lis_elements.size(); ++i) {
        cout << lis_elements[i] << (i + 1 == (int)lis_elements.size() ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```

### Mẫu 2: Đổi tiền ít xu nhất (coin change 1D)

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long INF = 1e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    long long s;
    if (!(cin >> k >> s)) return 0;

    vector<long long> c(k);

    for (int i = 0; i < k; ++i) {
        cin >> c[i];

    }

    vector<long long> dp(s + 1, INF);

    dp[0] = 0;

    for (int i = 1; i <= s; ++i) {
        for (long long coin : c) {
            if (i >= coin && dp[i - coin] != INF) {
                dp[i] = min(dp[i], dp[i - coin] + 1);
            }
        }
    }

    if (dp[s] == INF) {
        cout << -1 << "\n";
    } else {
        cout << dp[s] << "\n";
    }

    return 0;
}
```

## 8. Ma trận 15 bài tập thực hành theo mức độ (P0 → P5)

| Mã Bài Tập | Tên Bài Toán | Mức Độ | Trọng Tâm Kiến Thức & DP Invariant |
|---|---|:---:|---|
| $CPPB-DP1-01$ | Bước Nhảy Bậc Thang Cơ Bản | **P0** | Nhận diện Base Case $dp[0]=1, dp[1]=1$ & Công thức truy hồi $1D$. |
| $CPPB-DP1-02$ | Chú Ếch Nhảy Cóc Chi Phí Min | **P1** | $dp[i] = \min(dp[i-1] + \vert h_i - h_{i-1} \vert, dp[i-2] + \vert h_i - h_{i-2} \vert)$. |
| $CPPB-DP1-03$ | Trộm Nhà Không Liền Kề (House Robber) | **P1** | Quyết định nhị phân: $dp[i] = \max(dp[i-1], dp[i-2] + A[i])$. |
| $CPPB-DP1-04$ | Delete and Earn Tối Đa Điểm | **P2** | Quy đổi bài toán trên mảng giá trị về mô hình House Robber. |
| $CPPB-DP1-05$ | Đổi Tiền Ít Đồng Xu Nhất | **P2** | $dp[S] = 1 + \min(dp[S-c])$, xử lý khởi tạo giá trị vô cùng $\infty$. |
| $CPPB-DP1-06$ | Đếm Số Cách Đổi Tiền (Tổ Hợp) | **P2** | Vòng lặp Coin ngoài, Tiền trong để đếm không trùng lặp. |
| $CPPB-DP1-07$ | Dãy Con Tăng Dài Nhất Cơ Bản (LIS) | **P2** | Cài đặt chuẩn $\mathcal{O}(N^2)$ và trích xuất $\max(dp[i])$. |
| $CPPB-DP1-08$ | Dãy Con Tăng Có Tổng Lớn Nhất (MSIS) | **P3** | $dp[i] = A[i] + \max(dp[j])$, biến thể cực đại hóa tổng giá trị. |
| $CPPB-DP1-09$ | Mua Bán Cổ Phiếu Tối Ưu 1 Lần | **P3** | Duy trì giá trị nhỏ nhất tiền tố kết hợp DP $\mathcal{O}(N)$ thời gian, $\mathcal{O}(1)$ bộ nhớ. |
| $CPPB-DP1-10$ | Dãy Con Đan Dấu Dài Nhất | **P3** | Mở rộng trạng thái $dp[i][0]$ (bước giảm) và $dp[i][1]$ (bước tăng). |
| $CPPB-DP1-11$ | Cắt Thanh Gỗ Tối Ưu (Rod Cutting) | **P3** | Thử mọi nhát cắt $j \in [1..i]$, tối ưu hóa doanh thu. |
| $CPPB-DP1-12$ | Khôi Phục Dãy LIS Cụ Thể | **P4** | Cài đặt mảng `trace[i]` và lần ngược tái tạo dãy phần tử tối ưu. |
| $CPPB-DP1-13$ | Khôi Phục Danh Sách Đồng Xu Đổi Tiền | **P4** | Truy vết các mệnh giá xu đã được lựa chọn để tạo nên tổng $S$. |
| $CPPB-DP1-14$ | LIS Tối Ưu $N \log N$ (Challenge) | **P4** | Kỹ thuật mảng $tails$ kết hợp Tìm kiếm nhị phân `lower_bound`. |
| $CPPB-DP1-15$ | Phân Đoạn Dãy Số Tối Ưu (Mastery) | **P5** | $dp[i] = \min(dp[j] + \text{cost}(j+1, i))$, phân hoạch tiền tố tối ưu. |



# Bài 14: Quy hoạch động 2D & bài toán cái túi (Knapsack)

## 1. Bản chất không gian trạng thái 2D

Trong Bài 13, trạng thái $dp[i]$ chỉ phụ thuộc vào một tham số đơn lẻ (vị trí trên dãy số hoặc giá trị tổng tiền). Tuy nhiên, trong thực tế thi đấu, bài toán thường yêu cầu thỏa mãn đồng thời **hai điều kiện độc lập**:

1. **Quy hoạch động trên Lưới tọa độ (Grid DP):** Trạng thái được định vị bởi cặp tọa độ $(i, j)$ trên ma trận $N \times M$.
2. **Quy hoạch động Bài toán Cái túi (Knapsack DP):** Trạng thái cần theo dõi đồng thời **Chỉ số món đồ đang xét $i$** và **Sức chứa còn lại của cái túi $w$**.

> **Bản chất Không gian Trạng thái 2D:** Mỗi ô $dp[i][j]$ là một đỉnh trong Đồ thị trạng thái DAG 2 chiều. Thứ tự tính toán phải quét qua toàn bộ các hàng và cột theo chiều tăng dần (hoặc giảm dần có kiểm soát) để đảm bảo tính đúng đắn của mọi quan hệ phụ thuộc.



![Ma trận Quy hoạch động trên Lưới 2D](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-14-quy-hoach-dong-2d-knapsack/assets/grid_dp_matrix_vi.png)



## 2. Quy hoạch động trên lưới tọa độ (grid DP)

### 2.1. Đếm số đường đi trên lưới & xử lý vật cản

* **Bối cảnh:** Bắt đầu từ ô $(1, 1)$, cần đi đến ô $(N, M)$. Tại mỗi ô $(i, j)$, chỉ được phép di chuyển **Sang phải** $(i, j+1)$ hoặc **Xuống dưới** $(i+1, j)$. Trên lưới có một số ô là vật cản không thể đi vào.
* **State Definition:** $dp[i][j]$ là số đường đi hợp lệ từ $(1, 1)$ đến $(i, j)$.
* **Base Case:** `dp[1][1] = (grid[1][1] == 0 ? 1 : 0)`.
* **State Transition:** Nếu ô $(i, j)$ là vật cản $\implies dp[i][j] = 0$. Ngược lại:
$$dp[i][j] = (dp[i-1][j] + dp[i][j-1]) \pmod{10^9+7}$$

* **Evaluation Order:** Duyệt lồng 2 vòng lặp: Hàng $i = 1 \to N$, Cột $j = 1 \to M$.

### 2.2. Tìm đường đi có tổng giá trị lớn nhất / nhỏ nhất

* Mỗi ô $(i, j)$ chứa một số nguyên $A[i][j]$. Cần tìm đường đi từ $(1, 1)$ đến $(N, M)$ có tổng giá trị lớn nhất:
$$dp[i][j] = A[i][j] + \max(dp[i-1][j], dp[i][j-1])$$

## 3. Bài toán cái túi $0/1$ (0/1 Knapsack problem)

### 3.1. Bảng phương án 2D chuẩn mực ($DP[i][w]$)

* **Bối cảnh:** Cho $N$ món đồ, món thứ $i$ có khối lượng $wt_i$ và giá trị $val_i$. Cái túi có sức chứa tối đa $W$. Mỗi món đồ được chọn **tối đa 1 lần** ($0$ hoặc $1$).
* **State Definition:** $dp[i][w]$ là tổng giá trị lớn nhất có thể đạt được khi **chỉ xét trong $i$ món đồ đầu tiên** với tổng khối lượng không vượt quá $w$.
* **Base Cases:** `dp[0][w] = 0` với mọi $0 \le w \le W$ (Không có đồ thì giá trị bằng 0).
* **State Transition:** Tại món đồ thứ $i$, ta có 2 quyết định:
* Nếu $w < wt_i \implies dp[i][w] = dp[i-1][w]$ (Không đủ sức chứa để chọn món $i$).
* Nếu $w \ge wt_i \implies dp[i][w] = \max(dp[i-1][w], val_i + dp[i-1][w - wt_i])$.
* **Độ phức tạp:** Thời gian $\mathcal{O}(N \cdot W)$, Bộ nhớ $\mathcal{O}(N \cdot W)$.

### 3.2. Tuyệt kỹ nén mảng 1D (space optimization & backward traversal)
Nhận xét rằng dòng $dp[i][\dots]$ **chỉ phụ thuộc duy nhất vào dòng ngay trước nó** là $dp[i-1][\dots]$. Ta có thể nén bảng 2D thành một mảng 1D $dp[w]$ kích thước $W + 1$.

* **Tử huyệt bắt buộc:** Vòng lặp sức chứa $w$ bắt buộc phải **duyệt ngược từ $W$ giảm dần về $wt_i$**:
  ```cpp
  for (int w = W; w >= wt[i]; --w) {
      dp[w] = max(dp[w], val[i] + dp[w - wt[i]]);
  }
  ```
* **Tại sao phải duyệt ngược?** Khi tính $dp[w]$, ô `dp[w - wt[i]]` vẫn giữ nguyên giá trị của tầng $i-1$ (chưa bị đồ thứ $i$ ghi đè), đảm bảo mỗi món đồ chỉ được dùng tối đa 1 lần duy nhất!



![Kỹ thuật Nén mảng 1D trong 0/1 Knapsack](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-14-quy-hoach-dong-2d-knapsack/assets/knapsack_01_compression_vi.png)



## 4. Bài toán cái túi không giới hạn (unbounded Knapsack)

Khi mỗi món đồ được phép chọn **vô số lần** không giới hạn:

* **Hệ thức 2D:** $dp[i][w] = \max(dp[i-1][w], val_i + dp[i][w - wt_i])$.
* **Kỹ thuật mảng 1D:** Vòng lặp $w$ duyệt **XUÔI từ $wt_i$ tăng dần lên $W$**:
  ```cpp
  for (int w = wt[i]; w <= W; ++w) {
      dp[w] = max(dp[w], val[i] + dp[w - wt[i]]);
  }
  ```
* Duyệt xuôi cho phép trạng thái $dp[w]$ kế thừa ngay lập tức kết quả của chính món đồ $i$ vừa được thêm vào ở `dp[w - wt[i]]`.



![So sánh 0/1 Knapsack vs Unbounded Knapsack](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-14-quy-hoach-dong-2d-knapsack/assets/unbounded_vs_01_knapsack_vi.png)



## 5. Kỹ thuật đổi trục DP khi sức chứa $W$ quá lớn ($DP[v] = \text{Min Weight}$)

* **Bối cảnh:** $N \le 100$, nhưng sức chứa $W \le 10^9$ (không thể tạo mảng kích thước $10^9$), trong khi tổng giá trị tối đa $V_{\text{sum}} = \sum val_i \le 10^5$.
* **Đổi Trục Trạng Thái (State Redesign):**
* Đặt $dp[v]$ là **Khối lượng nhỏ nhất** để đạt được đúng tổng giá trị $v$.
* Base case: `dp[0] = 0`, mọi `dp[v] = INF` ($v \ge 1$).
* Chuyển trạng thái: Duyệt ngược $v$ từ $V_{\text{sum}}$ về $val_i$:
$$dp[v] = \min(dp[v], wt_i + dp[v - val_i])$$

* Đáp án: $\max \{v \mid dp[v] \le W\}$.
* **Độ phức tạp:** $\mathcal{O}(N \cdot V_{\text{sum}})$ — Chạy mượt mà dưới $0.05$ giây!

## 6. Các bẫy lỗi lập trình kinh điển (bug traps)

1. **Bẫy duyệt xuôi trong 0/1 Knapsack mảng 1D:**
* Viết `for (int w = wt[i]; w <= W; ++w)` cho bài $0/1$ Knapsack sẽ biến thuật toán thành Unbounded Knapsack $\implies$ Món đồ bị lấy nhiều lần, sai hoàn toàn kết quả!
2. **Bẫy tràn chỉ số biên âm trên Lưới 2D:**
* Tại hàng 1 và cột 1, $dp[i-1][j]$ hoặc $dp[i][j-1]$ sẽ truy cập vào chỉ số 0.
* **Quy tắc an toàn:** Khai báo mảng 1-based kích thước $(N+2) \times (M+2)$ và khởi tạo viền bằng 0 (cho bài đếm cách) hoặc $-\infty$ (cho bài tìm Max).
3. **Bẫy mảng 2D quá lớn gây tràn bộ nhớ (Memory Limit Exceeded - MLE):**
* Khai báo `long long dp[2000][2000]` tốn $2000 \times 2000 \times 8 \text{ bytes} \approx 32\text{ MB}$ (an toàn). Nhưng `long long dp[10000][10000]` tốn $800\text{ MB} \implies$ Sập bộ nhớ $256\text{MB}$. Bắt buộc phải nén thành mảng 1D.

## 7. Mẫu cài đặt chuẩn thi đấu (competitive templates)

### Mẫu 1: Bài toán cái túi $0/1$ nén mảng 1D

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long W;
    if (!(cin >> n >> W)) return 0;

    if (n <= 0 || W < 0) return 0;

    vector<long long> wt(n), val(n);

    for (int i = 0; i < n; ++i) {
        cin >> wt[i] >> val[i];

    }

    vector<long long> dp(W + 1, 0);

    for (int i = 0; i < n; ++i) {
        // Duyệt ngược w giảm dần từ W về wt[i]
        for (long long w = W; w >= wt[i]; --w) {
            dp[w] = max(dp[w], val[i] + dp[w - wt[i]]);
        }
    }

    cout << dp[W] << "\n";
    return 0;
}
```

### Mẫu 2: Đường đi có tổng lớn nhất trên lưới 2D

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    if (n <= 0 || m <= 0) return 0;

    vector<vector<long long>> a(n + 1, vector<long long>(m + 1));

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            cin >> a[i][j];

        }
    }

    vector<vector<long long>> dp(n + 1, vector<long long>(m + 1, 0));

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (i == 1 && j == 1) {
                dp[i][j] = a[1][1];
            } else if (i == 1) {
                dp[i][j] = dp[1][j - 1] + a[i][j];
            } else if (j == 1) {
                dp[i][j] = dp[i - 1][1] + a[i][j];
            } else {
                dp[i][j] = a[i][j] + max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }

    cout << dp[n][m] << "\n";
    return 0;
}
```

## 9. Ma trận 15 bài tập thực hành theo mức độ (P0 → P5)

| Mã Bài Tập | Tên Bài Toán | Mức Độ | Trọng Tâm Kiến Thức & DP Invariant |
|---|---|:---:|---|
| $CPPB-DP2-01$ | Đường Đi Trên Lưới Chi Phí Min | **P0** | $dp[i][j] = A[i][j] + \min(dp[i-1][j], dp[i][j-1])$ cơ bản. |
| $CPPB-DP2-02$ | Đếm Số Đường Đi Trên Lưới | **P1** | $dp[i][j] = (dp[i-1][j] + dp[i][j-1]) \pmod{10^9+7}$. |
| $CPPB-DP2-03$ | Đường Đi Lưới Có Vật Cản | **P1** | Xử lý ô cấm gán $dp[i][j] = 0$, xử lý Base Case xuất phát. |
| $CPPB-DP2-04$ | Tam Giác Số Tối Ưu (Triangle DP) | **P2** | Quy hoạch động từ đáy lên đỉnh hội tụ tại $dp[0][0]$. |
| $CPPB-DP2-05$ | Cái Túi $0/1$ Knapsack Cơ Bản | **P2** | Cài đặt chuẩn mảng nén 1D $dp[w]$ duyệt ngược $w$ giảm. |
| $CPPB-DP2-06$ | Kiểm Tra Tập Con Có Tổng Bằng S | **P2** | Subset Sum boolean $dp[w] = dp[w] \lor dp[w - A[i]]$. |
| $CPPB-DP2-07$ | Chia Mảng Thành 2 Phần Bằng Nhau | **P2** | Kiểm tra tổng chẵn và quy về Subset Sum với mục tiêu $S/2$. |
| $CPPB-DP2-08$ | Phân Chia Tập Hợp Chênh Lệch Min | **P3** | Tìm tổng tập con gần $S/2$ nhất, cực tiểu hóa $\vert S - 2 \cdot s_1 \vert$. |
| $CPPB-DP2-09$ | Unbounded Knapsack (Đồ Vô Hạn) | **P3** | Vòng lặp $w$ duyệt xuôi tăng dần từ $wt_i \to W$. |
| $CPPB-DP2-10$ | Đổi Tiền 2D Số Cách Tổ Hợp | **P3** | Đếm số cách đổi tiền không phân biệt thứ tự (Unbounded Ways). |
| $CPPB-DP2-11$ | Knapsack Theo Tổng Giá Trị (Value DP) | **P3** | Đổi trục $dp[v] = \text{Min Weight}$ khi $W \le 10^9, V \le 10^5$. |
| $CPPB-DP2-12$ | Khôi Phục Đường Đi Trên Lưới 2D | **P4** | Lần ngược từ $(N, M)$ về $(1, 1)$ in ra chuỗi bước đi $D$ và $R$. |
| $CPPB-DP2-13$ | Khôi Phục Danh Sách Món Đồ Cái Túi | **P4** | Lần ngược trên bảng $dp[i][w]$ tái tạo các món đồ được chọn. |
| $CPPB-DP2-14$ | Knapsack 2 Chiều Khối Lượng & Thể Tích | **P4** | Nén 2 chiều $dp[w][v]$ duyệt ngược 2 biến độc lập. |
| $CPPB-DP2-15$ | Quy Hoạch Động Lưới Thi Đấu (Mastery) | **P5** | Lưới ma trận với quy tắc di chuyển mở rộng chuẩn Olympic. |



# Bài 15: Quy hoạch động chuỗi: LCS & Edit Distance

## 1. Không gian trạng thái hai tiền tố (2-prefix state)

Trong xử lý chuỗi ký tự thi đấu, các bài toán so khớp, tìm chuỗi tương đồng hay biến đổi xâu thường thao tác trên hai chuỗi $A$ (độ dài $N$) và $B$ (độ dài $M$).

* **Nguyên lý Thiết kế Trạng thái:** Ta định nghĩa trạng thái dựa trên **Cặp tiền tố** của hai chuỗi:

> **$dp[i][j]$ đại diện cho kết quả tối ưu khi xét tiền tố $A[1 \dots i]$ (gồm $i$ ký tự đầu của $A$) và tiền tố $B[1 \dots j]$ (gồm $j$ ký tự đầu của $B$).**

* **Trường hợp cơ sở (Base Cases):** Khi một trong hai tiền tố có độ dài bằng 0 ($i = 0$ hoặc $j = 0$), tương đương với chuỗi rỗng $\varepsilon$.

## 2. Dãy con chung dài nhất (longest common subsequence — LCS)

### 2.1. Bản chất toán học & hệ thức truy hồi

* **Định nghĩa:** Dãy con là dãy thu được bằng cách xóa đi một số ký tự mà **không làm thay đổi thứ tự** của các ký tự còn lại.
* **State Definition:** $dp[i][j]$ là độ dài của dãy con chung dài nhất giữa $A[1 \dots i]$ và $B[1 \dots j]$.
* **Base Cases:** `dp[0][j] = 0` và `dp[i][0] = 0` với mọi $i, j$.
* **State Transition:** So sánh ký tự đuôi $A[i]$ và $B[j]$:
1. Nếu $A[i] == B[j]$: Ký tự này chắc chắn thuộc LCS chung:
$$dp[i][j] = 1 + dp[i-1][j-1]$$

2. Nếu `A[i] != B[j]`: Bỏ qua $A[i]$ hoặc bỏ qua $B[j]$ để lấy phương án tốt hơn:
$$dp[i][j] = \max(dp[i-1][j], dp[i][j-1])$$

* **Độ phức tạp:** Thời gian $\mathcal{O}(N \cdot M)$, Bộ nhớ $\mathcal{O}(N \cdot M)$.



![Bảng phương án LCS và Đường truy vết](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-15-quy-hoach-dong-chuoi-lcs/assets/lcs_table_traceback_vi.png)



### 2.2. Kỹ thuật khôi phục xâu LCS tối ưu (traceback)
Từ ô kết quả $(N, M)$ trên bảng phương án 2D:

1. Nếu $A[i] == B[j] \implies$ Thêm $A[i]$ vào xâu kết quả, lùi chéo về $(i-1, j-1)$.
2. Nếu $A[i] \ne B[j] \implies$ Đi về ô có giá trị lớn hơn: lên trên $(i-1, j)$ nếu $dp[i-1][j] \ge dp[i][j-1]$, ngược lại sang trái $(i, j-1)$.
3. Dừng lại khi $i = 0$ hoặc $j = 0$. Đảo ngược xâu kết quả thu được.

## 3. Khoảng cách biến đổi xâu (Edit Distance / Levenshtein Distance)

### 3.1. Bản chất 3 phép biến đổi
Cần tìm số phép biến đổi **ít nhất** để biến xâu $A$ thành xâu $B$. Các phép thao tác hợp lệ gồm:

1. **Chèn (Insert):** Thêm 1 ký tự vào xâu $A$.
2. **Xóa (Delete):** Xóa 1 ký tự khỏi xâu $A$.
3. **Thay thế (Replace):** Đổi 1 ký tự của $A$ thành ký tự khác.

### 3.2. Hệ thức chuyển trạng thái

* **State Definition:** $dp[i][j]$ là số thao tác ít nhất biến $A[1 \dots i]$ thành $B[1 \dots j]$.
* **Base Cases:**
* `dp[i][0] = i` (Biến xâu độ dài $i$ thành xâu rỗng cần $i$ phép xóa).
* `dp[0][j] = j` (Biến xâu rỗng thành xâu độ dài $j$ cần $j$ phép chèn).
* **State Transition:**
* Nếu $A[i] == B[j] \implies dp[i][j] = dp[i-1][j-1]$ (Không tốn chi phí).
* Nếu `A[i] != B[j]`:
$$dp[i][j] = 1 + \min(\underbrace{dp[i-1][j-1]}_{\text{Thay thế}}, \underbrace{dp[i-1][j]}_{\text{Xóa}}, \underbrace{dp[i][j-1]}_{\text{Chèn}})$$



![Khoảng cách biến đổi xâu Edit Distance](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-15-quy-hoach-dong-chuoi-lcs/assets/edit_distance_transitions_vi.png)



## 4. Phân biệt rạch ròi: Xâu con đối xứng (substring) vs dãy con đối xứng (subsequence)

Đây là tử huyệt thuật ngữ cực kỳ quan trọng trong lập trình thi đấu:



![Phân biệt Xâu con liên tiếp vs Dãy con đối xứng](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-15-quy-hoach-dong-chuoi-lcs/assets/palindrome_substring_vs_subsequence_vi.png)



### 4.1. Xâu con liên tiếp đối xứng dài nhất (longest palindromic substring)

* **Đặc tính:** Các ký tự phải **liên tiếp liền kề nhau**.
* **State Definition:** $dp[i][j]$ kiểu boolean, nhận giá trị `true` nếu đoạn con liên tiếp $S[i \dots j]$ là một xâu đối xứng.
* **Transition:** $dp[i][j] = (S[i] == S[j]) \land dp[i+1][j-1]$.
* **Duyệt:** Theo độ dài xâu con $len = 1 \to N$.

### 4.2. Dãy con không liên tiếp đối xứng dài nhất (longest palindromic subsequence)

* **Đặc tính:** Các ký tự **không cần liên tiếp**.
* **State Definition:** $dp[i][j]$ là độ dài lớn nhất của dãy con đối xứng trích xuất từ đoạn $S[i \dots j]$.
* **Transition:**
* Nếu $S[i] == S[j] \implies dp[i][j] = 2 + dp[i+1][j-1]$.
* Nếu $S[i] \ne S[j] \implies dp[i][j] = \max(dp[i+1][j], dp[i][j-1])$.
* *Cách giải tương đương:* Tính $LCS$ giữa xâu $S$ và xâu đảo ngược $S^R$!

## 5. Các bẫy lỗi lập trình kinh điển (bug traps)

1. **Bẫy lệch chỉ số 0-based của Xâu ký tự với 1-based của Bảng DP:**
* Trong C++, `string` có chỉ số từ `0` đến $N-1$. Khi truy cập ký tự thứ $i$ trong bảng DP 1-based, phải viết `A[i - 1]` thay vì `A[i]`.
2. **Bẫy thứ tự duyệt trong Quy hoạch động trên Đoạn con Palindrome:**
* Trạng thái $dp[i][j]$ phụ thuộc vào $dp[i+1][j-1]$ (đoạn ngắn hơn). Nếu duyệt $i$ từ $1 \to N$ xuôi thì ô $dp[i+1][\dots]$ chưa được tính $\implies$ Kết quả sai!
* **Quy tắc đúng:** Luôn duyệt theo độ dài $len = 1 \to N$, sau đó duyệt điểm đầu $i = 1 \to N - len + 1$ và $j = i + len - 1$.
3. **Bẫy khởi tạo Base Case của Edit Distance:**
* Quên khởi tạo cột $0$ (`dp[i][0] = i`) và hàng $0$ (`dp[0][j] = j`) sẽ dẫn đến toàn bộ bảng nhận giá trị rác.

## 6. Mẫu cài đặt chuẩn thi đấu (competitive templates)

### Mẫu 1: Dãy con chung dài nhất (LCS) kèm khôi phục xâu

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a, b;
    if (!(cin >> a >> b)) return 0;

    int n = a.size();
    int m = b.size();
    if (n == 0 || m == 0) {
        cout << 0 << "\n\n";
        return 0;
    }

    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (a[i - 1] == b[j - 1]) {
                dp[i][j] = 1 + dp[i - 1][j - 1];
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }

    cout << dp[n][m] << "\n";

    // Khôi phục xâu LCS
    string lcs_str = "";
    int i = n, j = m;
    while (i > 0 && j > 0) {

        if (a[i - 1] == b[j - 1]) {
            lcs_str.push_back(a[i - 1]);
            --i;
            --j;
        } else if (dp[i - 1][j] >= dp[i][j - 1]) {
            --i;
        } else {
            --j;
        }
    }
    reverse(lcs_str.begin(), lcs_str.end());
    cout << lcs_str << "\n";

    return 0;
}
```

### Mẫu 2: Khoảng cách biến đổi xâu (Edit Distance)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a, b;
    if (!(cin >> a >> b)) return 0;

    int n = a.size();
    int m = b.size();

    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));

    for (int i = 0; i <= n; ++i) dp[i][0] = i;
    for (int j = 0; j <= m; ++j) dp[0][j] = j;

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (a[i - 1] == b[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1];
            } else {
                dp[i][j] = 1 + min({dp[i - 1][j - 1], // Replace
                                    dp[i - 1][j],     // Delete
                                    dp[i][j - 1]});   // Insert
            }
        }
    }

    cout << dp[n][m] << "\n";
    return 0;
}
```

## 8. Ma trận 15 bài tập thực hành theo mức độ (P0 → P5)

| Mã Bài Tập | Tên Bài Toán | Mức Độ | Trọng Tâm Kiến Thức & DP Invariant |
|---|---|:---:|---|
| $CPPB-DPS-01$ | Dãy con chung dài nhất Cơ Bản (LCS) | **P0** | $dp[i][j]$ trên 2 tiền tố, so khớp $A[i]==B[j]$. |
| $CPPB-DPS-02$ | Độ Dài LCS Của 3 Xâu Ngắn | **P1** | Quy hoạch động 3 chiều $dp[i][j][k]$ kích thước nhỏ. |
| $CPPB-DPS-03$ | Xâu Con Chung Ngắn Nhất (SCS) | **P1** | Áp dụng công thức $N + M - \text{LCS}(A, B)$. |
| $CPPB-DPS-04$ | Chèn Ít Ký Tự Nhất Tạo Xâu Đối Xứng | **P1** | Quy đổi về bài toán $N - \text{LPS}(S)$. |
| $CPPB-DPS-05$ | Khoảng cách biến đổi xâu (Edit Distance) | **P2** | 3 thao tác Chèn, Xóa, Thay thế kèm khởi tạo biên $\mathcal{O}(N \cdot M)$. |
| $CPPB-DPS-06$ | Edit Distance Chi Phí Thao Tác Bất Đối Xứng | **P2** | Chi phí chèn $c_I$, xóa $c_D$, thay thế $c_R$ khác nhau. |
| $CPPB-DPS-07$ | Xâu Con Liên Tiếp Đối Xứng Dài Nhất | **P2** | Longest Palindromic Substring boolean $dp[i][j]$ duyệt theo độ dài $len$. |
| $CPPB-DPS-08$ | Dãy Con Không Liên Tiếp Đối Xứng Dài Nhất | **P2** | Longest Palindromic Subsequence $dp[i][j]$ trên 2 đầu mút. |
| $CPPB-DPS-09$ | Đếm Số Lần Xuất Hiện Dãy Con (Distinct Subseq) | **P3** | Đếm số lần xâu $T$ xuất hiện dưới dạng dãy con của $S$ modulo $10^9+7$. |
| $CPPB-DPS-10$ | Xâu Đan Xen (Interleaving String) | **P3** | Kiểm tra xâu $C$ có được tạo bởi việc đan xen 2 xâu $A$ và $B$. |
| $CPPB-DPS-11$ | Xóa Ít Ký Tự Nhất Để Hai Xâu Bằng Nhau | **P3** | Cực tiểu hóa chi phí xóa ký tự mã ASCII. |
| $CPPB-DPS-12$ | Khôi Phục Chuỗi LCS Cụ Thể | **P4** | Lần ngược từ $(N, M)$ tái tạo chính xác xâu ký tự con chung. |
| $CPPB-DPS-13$ | Khôi Phục Lộ Trình Biến Đổi Edit Distance | **P4** | In ra từng bước thao tác Insert, Delete, Replace cụ thể. |
| $CPPB-DPS-14$ | So Khớp Ký Tự Đại Diện (Wildcard Matching) | **P4** | Xử lý ký tự `?` (1 ký tự) và $*$ (chuỗi bất kỳ $\ge 0$). |
| $CPPB-DPS-15$ | Quy Hoạch Động Chuỗi Olympic (Mastery) | **P5** | Bài toán tối ưu hóa xâu kết hợp điều kiện từ vựng chuẩn thi đấu. |


# CHƯƠNG 06: CẤU TRÚC DỮ LIỆU NÂNG CAO


# Bài 16: Cấu trúc dữ liệu STL: Set, map & heap

## 1. Bản chất các cấu trúc dữ liệu nâng cao trong thư viện chuẩn STL

Trong lập trình thi đấu hiện đại, việc tự cài đặt lại cây nhị phân cân bằng hay bảng băm từ đầu cho mọi bài toán là không khả thi. C++ Standard Template Library (STL) cung cấp các cấu trúc dữ liệu tối ưu hóa cực mạnh:

* **`std::set` / `std::map`:** Cây đỏ-đen (Red-Black Tree) tự cân bằng, luôn duy trì các phần tử theo thứ tự tăng dần. Các thao tác tìm kiếm, chèn, xóa đều có độ phức tạp đảm bảo $\mathcal{O}(\log N)$.
* **`std::unordered_map` / `std::unordered_set`:** Bảng băm trực tiếp (Hash Table), đạt thời gian trung bình $\mathcal{O}(1)$ cho các truy vấn.
* **`std::priority_queue`:** Cấu trúc Heap nhị phân hoàn chỉnh, cho phép truy xuất phần tử lớn nhất (hoặc nhỏ nhất) trong $\mathcal{O}(1)$ và thêm/bớt trong $\mathcal{O}(\log N)$.



![So sánh Set Map vs Unordered Map](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-16-cau-truc-du-lieu-stl-set-map/assets/stl_set_map_rb_tree_vi.png)



## 2. Kỹ thuật nén tọa độ (Coordinate Compression)

### 2.1. Bản chất bài toán & khi nào cần nén tọa độ?

* **Vấn đề:** Các giá trị trong mảng $A$ có thể rất lớn ($A[i] \le 10^9$ hoặc $10^{18}$), ta không thể dùng giá trị này làm chỉ số mảng đếm tần suất hoặc dựng cây Segment Tree / Fenwick Tree. Tuy nhiên, số lượng phần tử $N$ lại rất nhỏ ($N \le 10^5$).
* **Nguyên lý Nén Tọa Độ:** Ánh xạ tập giá trị rời rạc ban đầu về tập số nguyên liên tiếp $\{0, 1, 2, \dots, K-1\}$ ($K \le N$) sao cho **giữ nguyên thứ tự tương quan lớn bé** giữa các phần tử:
$$A[i] < A[j] \iff \text{rank}(A[i]) < \text{rank}(A[j])$$



![Mô hình Nén Tọa Độ](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-16-cau-truc-du-lieu-stl-set-map/assets/coordinate_compression_model_vi.png)



### 2.2. Quy trình 4 bước chuẩn mực trong C++

1. **Sao chép mảng:** `vector<long long> vals = a;`

2. **Sắp xếp tăng dần:** `sort(vals.begin(), vals.end());`
3. **Lọc bỏ trùng lặp:** `vals.erase(unique(vals.begin(), vals.end()), vals.end());`
4. **Ánh xạ bằng Tìm kiếm nhị phân:**
   ```cpp
   int compressed_val = lower_bound(vals.begin(), vals.end(), a[i]) - vals.begin();
   ```

## 3. Hàng đợi ưu tiên (Priority Queue / heap)



![Hàng đợi ưu tiên Max-Heap vs Min-Heap](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-16-cau-truc-du-lieu-stl-set-map/assets/priority_queue_heap_vi.png)



* **Max-Heap (Mặc định):** `priority_queue<long long> max_pq;` $\implies$ `top()` trả về giá trị lớn nhất.

* **Min-Heap (Đảo thứ tự):** `priority_queue<long long, vector<long long>, greater<long long>> min_pq;` $\implies$ `top()` trả về giá trị nhỏ nhất.

* **Ứng dụng kinh điển:** Tìm $K$ phần tử lớn nhất/nhỏ nhất trong luồng dữ liệu online, thuật toán Dijkstra, thuật toán Prim, duy trì Trung vị động (Median) bằng 2 Heap.

## 4. Các bẫy lỗi lập trình kinh điển (bug traps)

1. **Bẫy Worst-case $\mathcal{O}(N)$ của `unordered_map` do Anti-Hash Test:**
* Trong các kỳ thi competitive, hàm băm mặc định `std::hash` của `unordered_map` rất dễ bị các test đối kháng (Anti-hash tests) làm tràn bucket $\implies$ Độ phức tạp tụt xuống $\mathcal{O}(N^2)$ và bị TLE.
* **Quy tắc an toàn:** Dùng `std::map` khi $N \le 2 \cdot 10^5$ (đảm bảo $\mathcal{O}(N \log N)$), hoặc dùng Custom Hash an toàn với hằng số thời gian ngẫu nhiên `chrono`.
2. **Bẫy xóa phần tử trong `std::multiset`:**
* Lệnh `ms.erase(x)` sẽ **xóa TOÀN BỘ** các phần tử có giá trị bằng $x$ trong multiset!
* **Cú pháp chuẩn khi chỉ muốn xóa 1 bản sao:** `ms.erase(ms.find(x));`.
3. **Bẫy truy cập `map[key]` tự động chèn phần tử mới:**
* Khi gọi `if (mp[x] > 0)`, nếu $x$ chưa tồn tại trong map, C++ sẽ tự động chèn cặp `(x, 0)` vào map làm tăng kích thước bộ nhớ.

* **Cú pháp an toàn:** Dùng `if (mp.count(x))` hoặc `if (mp.find(x) != mp.end())`.

## 5. Mẫu cài đặt chuẩn thi đấu (competitive templates)

### Mẫu 1: Kỹ thuật nén tọa độ chuẩn mực

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    if (n <= 0) return 0;

    vector<long long> a(n);

    for (int i = 0; i < n; ++i) {
        cin >> a[i];

    }

    // 1. Tạo mảng nén
    vector<long long> vals = a;

    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());

    // 2. Ánh xạ từng phần tử
    vector<int> compressed(n);

    for (int i = 0; i < n; ++i) {
        compressed[i] = lower_bound(vals.begin(), vals.end(), a[i]) - vals.begin();
    }

    for (int i = 0; i < n; ++i) {
        cout << compressed[i] << (i + 1 == n ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```

### Mẫu 2: Duy trì trung vị động bằng 2 heap (median of stream)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    if (n <= 0) return 0;

    priority_queue<long long> left_max; // Nửa nhỏ hơn (Max-Heap)

    priority_queue<long long, vector<long long>, greater<long long>> right_min; // Nửa lớn hơn (Min-Heap)

    for (int i = 0; i < n; ++i) {
        long long x;
        cin >> x;

        if (left_max.empty() || x <= left_max.top()) {
            left_max.push(x);
        } else {
            right_min.push(x);
        }

        // Tự cân bằng kích thước: left_max luôn có size == right_min hoặc size == right_min + 1
        if (left_max.size() > right_min.size() + 1) {

            right_min.push(left_max.top());
            left_max.pop();
        } else if (right_min.size() > left_max.size()) {

            left_max.push(right_min.top());
            right_min.pop();
        }

        // In trung vị hiện tại
        cout << left_max.top() << (i + 1 == n ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```

## Bài tập thực hành


### Bài 01 [CPPB-STL-01]: Đếm Số Phần Tử Phân Biệt

**Bối cảnh:** Cho mảng $A$ gồm $N$ số nguyên. Cần đếm xem trong mảng có bao nhiêu giá trị phân biệt.

**Nhiệm vụ:** In ra số lượng phần tử phân biệt.

**Đầu vào (Input):**

- Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

**Đầu ra (Output):**

- Số phần tử phân biệt.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 <br> 2 3 2 2 3 | 2 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 10^5, 1 \le A_i \le 10^9$.



### Bài 02 [CPPB-STL-02]: Bảng Tra Cứu Tần Suất Từ Khóa

**Bối cảnh:** Cho danh sách $N$ từ khóa. Cần in ra tần suất xuất hiện của từng từ khóa theo thứ tự từ điển tăng dần.

**Nhiệm vụ:** Mỗi dòng in ra từ khóa và số lần xuất hiện tương ứng cách nhau bởi khoảng trắng.

**Đầu vào (Input):**

- Dòng 1: Số nguyên $N$ ($1 \le N \le 50000$).
- $N$ dòng tiếp theo: Mỗi dòng chứa 1 từ khóa.

**Đầu ra (Output):**

- Bảng tần suất theo thứ tự từ điển.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 <br> apple <br> banana <br> apple <br> orange | apple 2 <br> banana 1 <br> orange 1 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 50000$.



### Bài 03 [CPPB-STL-03]: Nén Tọa Độ Mảng Số Lớn

**Bối cảnh:** Cho mảng $A$ gồm $N$ số nguyên lớn ($A_i \le 10^9$). Cần ánh xạ các giá trị về tập $\{0, 1, \dots, K-1\}$ ($K \le N$) giữ nguyên quan hệ thứ tự.

**Nhiệm vụ:** In ra mảng sau khi nén tọa độ (0-based ranking).

**Đầu vào (Input):**

- Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

**Đầu ra (Output):**

- Dãy số sau khi nén tọa độ.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 <br> 100 20000 50 20000 100 | 1 2 0 2 1 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 10^5, 1 \le A_i \le 10^9$.



### Bài 04 [CPPB-STL-04]: Tìm Phần Tử Nhỏ Nhất Lớn Hơn Hoặc Bằng X

**Bối cảnh:** Cho tập hợp $N$ số nguyên và $Q$ truy vấn. Mỗi truy vấn cho số $X$, cần tìm phần tử nhỏ nhất trong tập hợp mà $\ge X$.

**Nhiệm vụ:** Với mỗi truy vấn in ra phần tử tìm được hoặc -1 nếu không tồn tại.

**Đầu vào (Input):**

- Dòng 1: Hai số $N$ và $Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: $N$ số nguyên trong tập hợp ($1 \le A_i \le 10^9$).
- $Q$ dòng tiếp theo: Mỗi dòng chứa 1 số $X$.

**Đầu ra (Output):**

- Kết quả $Q$ truy vấn.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 3 <br> 10 20 30 40 50 <br> 25 <br> 50 <br> 60 | 30 <br> 50 <br> -1 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N, Q \le 10^5, 1 \le A_i, X \le 10^9$.



### Bài 05 [CPPB-STL-05]: Hàng Đợi Ưu Tiên K Phần Tử Lớn Nhất

**Bối cảnh:** Cho mảng $N$ phần tử. Cần tìm $K$ phần tử lớn nhất và in ra theo thứ tự giảm dần.

**Nhiệm vụ:** In ra $K$ phần tử lớn nhất.

**Đầu vào (Input):**

- Dòng 1: Hai số $N$ và $K$ ($1 \le K \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

**Đầu ra (Output):**

- $K$ số nguyên lớn nhất theo thứ tự giảm dần.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 6 3 <br> 10 50 30 20 60 40 | 60 50 40 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le K \le N \le 10^5, 1 \le A_i \le 10^9$.



### Bài 06 [CPPB-STL-06]: Quản Lý Tập Hợp Đa Trùng Lặp (Multiset)

**Bối cảnh:** Hỗ trợ 3 loại thao tác: 1 x (Thêm x), 2 x (Xóa đúng 1 phần tử có giá trị x), 3 x (Đếm số lần xuất hiện của x).

**Nhiệm vụ:** Với thao tác loại 3, in ra số lần xuất hiện.

**Đầu vào (Input):**

- Dòng 1: Số nguyên $Q$ ($1 \le Q \le 50000$).
- $Q$ dòng tiếp theo: `type` và $x$ ($1 \le x \le 10^9$).

**Đầu ra (Output):**

- Kết quả các thao tác loại 3.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 <br> 1 5 <br> 1 5 <br> 3 5 <br> 2 5 <br> 3 5 | 2 <br> 1 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le Q \le 50000, 1 \le x \le 10^9$.



### Bài 07 [CPPB-STL-07]: Hợp Nhất Các Đoạn Số (Merge Intervals)

**Bối cảnh:** Cho $N$ đoạn số $[L_i, R_i]$. Cần hợp nhất tất cả các đoạn có điểm chung lại với nhau.

**Nhiệm vụ:** Dòng 1: Số lượng đoạn sau hợp nhất. Các dòng tiếp theo in các đoạn tăng dần theo $L$.

**Đầu vào (Input):**

- Dòng 1: Số nguyên $N$ ($1 \le N \le 50000$).
- $N$ dòng tiếp theo: $L_i, R_i$ ($1 \le L_i \le R_i \le 10^9$).

**Đầu ra (Output):**

- Danh sách các đoạn sau khi hợp nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 <br> 1 3 <br> 2 6 <br> 8 10 <br> 15 18 | 3 <br> 1 6 <br> 8 10 <br> 15 18 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 50000, 1 \le L_i \le R_i \le 10^9$.



### Bài 08 [CPPB-STL-08]: Tìm Trung Vị Động Trong Luồng Dữ Liệu

**Bối cảnh:** Nhận lần lượt $N$ số nguyên. Sau mỗi số được thêm vào, hãy in ra trung vị dưới của dãy số hiện tại.

**Nhiệm vụ:** In ra $N$ số là trung vị sau từng bước.

**Đầu vào (Input):**

- Dòng 1: Số nguyên $N$ ($1 \le N \le 50000$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

**Đầu ra (Output):**

- $N$ giá trị trung vị cách nhau bởi dấu cách.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 <br> 5 15 1 3 | 5 5 5 3 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 50000, 1 \le A_i \le 10^9$.



### Bài 09 [CPPB-STL-09]: Đếm Số Phần Tử Phân Biệt Trong Cửa Sổ K

**Bối cảnh:** Cho mảng $A$ và số $K$. Tính số lượng phần tử phân biệt trong mỗi cửa sổ trượt độ dài $K$.

**Nhiệm vụ:** In ra số lượng phần tử phân biệt trong từng cửa sổ.

**Đầu vào (Input):**

- Dòng 1: Hai số $N$ và $K$ ($1 \le K \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

**Đầu ra (Output):**

- $N - K + 1$ số nguyên.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 7 4 <br> 1 2 1 3 4 2 3 | 3 4 4 3 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le K \le N \le 10^5, 1 \le A_i \le 10^9$.



### Bài 10 [CPPB-STL-10]: Nối Dây Chi Phí Nhỏ Nhất (Huffman Greedy)

**Bối cảnh:** Có $N$ sợi dây với chiều dài $A_i$. Chi phí nối hai sợi dây có chiều dài $X$ và $Y$ là $X + Y$. Cần nối tất cả các sợi dây thành 1 sợi duy nhất.

**Nhiệm vụ:** Tìm tổng chi phí nối dây nhỏ nhất.

**Đầu vào (Input):**

- Dòng 1: Số nguyên $N$ ($1 \le N \le 50000$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^5$).

**Đầu ra (Output):**

- Tổng chi phí nhỏ nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 <br> 4 3 2 6 | 29 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 50000, 1 \le A_i \le 10^5$.



### Bài 11 [CPPB-STL-11]: Lập Lịch Công Việc Số Máy Chủ Ít Nhất

**Bối cảnh:** Có $N$ công việc, công việc thứ $i$ bắt đầu tại thời điểm $S_i$ và kết thúc tại $E_i$. Một máy chủ chỉ thực hiện được 1 công việc tại một thời điểm.

**Nhiệm vụ:** Tìm số lượng máy chủ ít nhất cần thiết để thực hiện toàn bộ $N$ công việc.

**Đầu vào (Input):**

- Dòng 1: Số nguyên $N$ ($1 \le N \le 50000$).
- $N$ dòng tiếp theo: $S_i, E_i$ ($1 \le S_i < E_i \le 10^9$).

**Đầu ra (Output):**

- Số máy chủ ít nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 <br> 0 30 <br> 5 10 <br> 15 20 | 2 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 50000, 1 \le S_i < E_i \le 10^9$.



### Bài 12 [CPPB-STL-12]: Đếm Cặp Số Có Hiệu Bằng K

**Bối cảnh:** Cho mảng $A$ gồm $N$ số nguyên lớn. Cần đếm số cặp chỉ số $(i, j)$ với $i < j$ sao cho $|A_i - A_j| = K$.

**Nhiệm vụ:** In ra số lượng cặp thỏa mãn.

**Đầu vào (Input):**

- Dòng 1: Hai số $N$ và $K$ ($1 \le N \le 10^5, 0 \le K \le 10^9$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

**Đầu ra (Output):**

- Số cặp thỏa mãn.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 2 <br> 1 5 3 4 2 | 3 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 10^5, 0 \le K, A_i \le 10^9$.



### Bài 13 [CPPB-STL-13]: Phần Tử Xuất Hiện Nhiều Nhất (Mode)

**Bối cảnh:** Cho mảng $N$ phần tử. Tìm phần tử xuất hiện nhiều lần nhất trong mảng. Nếu có nhiều phần tử cùng tần suất lớn nhất, chọn phần tử có giá trị nhỏ nhất.

**Nhiệm vụ:** In ra giá trị và tần suất xuất hiện lớn nhất.

**Đầu vào (Input):**

- Dòng 1: Số nguyên $N$ ($1 \le N \le 50000$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

**Đầu ra (Output):**

- Giá trị và tần suất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 6 <br> 1 3 2 1 4 1 | 1 3 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 50000, 1 \le A_i \le 10^9$.



### Bài 14 [CPPB-STL-14]: Cặp Điểm Gần Nhất (Closest Pair Of Points)

**Bối cảnh:** Cho $N$ điểm trên mặt phẳng 2D. Tìm bình phương khoảng cách Euclid nhỏ nhất giữa hai điểm bất kỳ.

**Nhiệm vụ:** In ra bình phương khoảng cách nhỏ nhất.

**Đầu vào (Input):**

- Dòng 1: Số nguyên $N$ ($2 \le N \le 10000$).
- $N$ dòng tiếp theo: Mỗi dòng gồm tọa độ $X_i, Y_i$ ($0 \le X_i, Y_i \le 10^5$).

**Đầu ra (Output):**

- Bình phương khoảng cách nhỏ nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 <br> 0 0 <br> 1 2 <br> 3 1 <br> 4 0 | 5 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $2 \le N \le 10000, 0 \le X_i, Y_i \le 10^5$.



### Bài 15 [CPPB-STL-15]: Hệ Thống Xếp Hạng Thi Đấu Dynamic

**Bối cảnh:** Hệ thống thi đấu online hỗ trợ 2 loại truy vấn: `1 Name Score` (Cộng điểm cho thí sinh Name) và `2 Name` (Hỏi tổng điểm hiện tại của thí sinh Name).

**Nhiệm vụ:** Với mỗi truy vấn loại 2, in ra điểm số của thí sinh tương ứng.

**Đầu vào (Input):**

- Dòng 1: Số nguyên $Q$ ($1 \le Q \le 20000$).
- $Q$ dòng tiếp theo chứa các truy vấn.

**Đầu ra (Output):**

- Kết quả các truy vấn loại 2.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 <br> 1 Alice 100 <br> 1 Bob 150 <br> 2 Alice <br> 1 Alice 60 | 100 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le Q \le 20000$.




# Bài 17: Cấu trúc dữ liệu ngăn xếp (stack) & Monotonic Stack

## 1. Bản chất cấu trúc dữ liệu ngăn xếp (stack)

Ngăn xếp (Stack) là cấu trúc dữ liệu hoạt động theo nguyên lý **LIFO (Last In, First Out — Vào sau, Ra trước)**:

* Phần tử được thêm vào cuối cùng sẽ là phần tử đầu tiên được lấy ra.
* Các thao tác cơ bản trong C++ `std::stack`: `push(x)` (thêm vào đỉnh), `pop()` (xóa đỉnh), `top()` (truy cập đỉnh), `empty()`, `size()`. Toàn bộ thao tác đều đạt thời gian tối ưu tuyệt đối $\mathcal{O}(1)$.



![Cơ chế LIFO của Stack và Khớp Dấu Ngoặc](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-17-ngan-xep-stack-monotonic/assets/stack_lifo_operation_vi.png)



## 2. Kỹ thuật ngăn xếp đơn điệu (Monotonic Stack)

### 2.1. Bản chất bài toán & khi nào cần Monotonic Stack?

* **Vấn đề:** Cho mảng $A$ gồm $N$ phần tử. Với mỗi vị trí $i$, cần tìm vị trí phần tử **đầu tiên bên phải (hoặc bên trái)** có giá trị lớn hơn (hoặc nhỏ hơn) $A[i]$.
* **Cách ngây thơ:** Duyệt 2 vòng lặp lồng nhau $\implies \mathcal{O}(N^2)$ (bị TLE khi $N = 10^5$).
* **Nguyên lý Monotonic Stack:** Duy trì một ngăn xếp chứa các chỉ số mà giá trị tương ứng trong mảng luôn tuân theo tính chất **đơn điệu** (tăng dần hoặc giảm dần). Khi gặp phần tử mới vi phạm tính đơn điệu, ta liên tục `pop()` các phần tử ở đỉnh ngăn xếp và ghi nhận đáp án cho chúng.



![Mô hình Monotonic Stack NGE](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-17-ngan-xep-stack-monotonic/assets/monotonic_stack_nge_vi.png)



### 2.2. Phân tích độ phức tạp khấu hao (amortized analysis $\mathcal{O}(N)$)
Mỗi phần tử của mảng được `push()` vào ngăn xếp đúng $1$ lần và bị `pop()` ra khỏi ngăn xếp tối đa $1$ lần trong toàn bộ quá trình chạy.
$$\text{Tổng số thao tác trên Stack} \le 2N \implies \text{Thời gian trung bình } \mathcal{O}(N)!$$

## 3. Bài toán kinh điển: Hình chữ nhật lớn nhất trên biểu đồ cột (largest rectangle in histogram)



![Hình chữ nhật lớn nhất trên Histogram](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-17-ngan-xep-stack-monotonic/assets/histogram_max_rectangle_vi.png)



* **Bản chất:** Với mỗi cột $i$ có chiều cao $H[i]$, ta cần tìm:
1. $L[i]$: Vị trí cột đầu tiên bên trái có chiều cao $< H[i]$.
2. $R[i]$: Vị trí cột đầu tiên bên phải có chiều cao $< H[i]$.
* Khi đó, hình chữ nhật lớn nhất nhận $H[i]$ làm chiều cao tối đa sẽ có chiều rộng $W = R[i] - L[i] - 1$, diện tích là $S[i] = H[i] \times (R[i] - L[i] - 1)$.
* Sử dụng 2 lượt Monotonic Stack (hoặc 1 lượt thông minh), ta tính toàn bộ mảng $L$ và $R$ trong $\mathcal{O}(N)$.

## 4. Các bẫy lỗi lập trình kinh điển (bug traps)

1. **Bẫy gọi `st.top()` hoặc `st.pop()` khi Stack rỗng:**
* Truy cập đỉnh ngăn xếp khi `st.empty() == true` sẽ dẫn đến lỗi bộ nhớ nghiêm trọng (Segmentation Fault / Runtime Error).
* **Quy tắc an toàn:** Luôn kiểm tra `while (!st.empty() && ...)` trước khi gọi `st.top()` hay `st.pop()`.
2. **Bẫy quên kiểm tra `st.empty()` ở cuối bài toán Dãy ngoặc đúng:**
* Sau khi duyệt hết chuỗi, nếu không còn ngoặc đóng nào nhưng trong stack vẫn còn ngoặc mở dư thừa (ví dụ chuỗi `"((()"`), dãy ngoặc vẫn là **KHÔNG HỢP LỆ**.
* **Điều kiện đủ:** Dãy hợp lệ khi và chỉ khi không bị lỗi giữa chừng VÀ `st.empty() == true` ở cuối.
3. **Bẫy tràn số khi tính diện tích hình chữ nhật lớn nhất:**
* Chiều cao $H[i] \le 10^9$ và chiều rộng $W \le 10^5 \implies$ Diện tích có thể lên tới $10^{14}$, vượt quá giới hạn 32-bit `int`. Bắt buộc phải ép kiểu sang `long long`.

## 5. Mẫu cài đặt chuẩn thi đấu (competitive templates)

### Mẫu 1: Tìm phần tử lớn hơn tiếp theo (next greater element)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    if (n <= 0) return 0;

    vector<long long> a(n);

    for (int i = 0; i < n; ++i) {
        cin >> a[i];

    }

    vector<long long> nge(n, -1);

    stack<int> st; // Lưu chỉ số

    for (int i = 0; i < n; ++i) {
        while (!st.empty() && a[i] > a[st.top()]) {

            nge[st.top()] = a[i];
            st.pop();
        }
        st.push(i);
    }

    for (int i = 0; i < n; ++i) {
        cout << nge[i] << (i + 1 == n ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```

### Mẫu 2: Hình chữ nhật lớn nhất trên biểu đồ cột (histogram)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    if (n <= 0) return 0;

    vector<long long> h(n);

    for (int i = 0; i < n; ++i) {
        cin >> h[i];

    }

    // Thêm phần tử lính canh 0 ở cuối để đẩy toàn bộ stack ra
    h.push_back(0);
    stack<int> st;

    long long max_area = 0;

    for (int i = 0; i <= n; ++i) {
        while (!st.empty() && h[i] < h[st.top()]) {
            long long height = h[st.top()];
            st.pop();
            long long width = st.empty() ? i : (i - st.top() - 1);
            max_area = max(max_area, height * width);
        }
        st.push(i);
    }

    cout << max_area << "\n";
    return 0;
}
```

## Bài tập thực hành


### Bài 01 [CPPB-STK-01]: Kiểm Tra Dãy Ngoặc Đúng Đơn Loại

**Bối cảnh:** Cho một chuỗi chỉ gồm các ký tự ngoặc tròn `(` và `)`. Cần xác định xem chuỗi đó có phải là một dãy ngoặc đúng hay không.

**Nhiệm vụ:** In ra `YES` nếu chuỗi là dãy ngoặc đúng, ngược lại in `NO`.

**Đầu vào (Input):**

- Một dòng duy nhất chứa chuỗi $S$ ($1 \le |S| \le 10^5$).

**Đầu ra (Output):**

- `YES` hoặc `NO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| (()()) | YES |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le |S| \le 10^5$.



### Bài 02 [CPPB-STK-02]: Dãy Ngoặc Hỗn Hợp Nhiều Loại

**Bối cảnh:** Cho một chuỗi gồm 3 loại ngoặc: `()`, `[]`, `{}`. Kiểm tra xem các cặp ngoặc có đóng mở hợp lệ và lồng nhau đúng quy tắc hay không.

**Nhiệm vụ:** In `YES` nếu hợp lệ, ngược lại in `NO`.

**Đầu vào (Input):**

- Một dòng chứa chuỗi $S$ ($1 \le |S| \le 10^5$).

**Đầu ra (Output):**

- `YES` hoặc `NO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| {[()]} | YES |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le |S| \le 10^5$.



### Bài 03 [CPPB-STK-03]: Đánh Giá Biểu Thức Hậu Tố (Reverse Polish Notation)

**Bối cảnh:** Cho danh sách $N$ token biểu diễn một biểu thức toán học dưới dạng Hậu tố (RPN) gồm các số nguyên và 3 toán tử `+`, `-`, `*`.

**Nhiệm vụ:** Tính và in ra giá trị của biểu thức.

**Đầu vào (Input):**

- Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ token cách nhau bởi khoảng trắng.

**Đầu ra (Output):**

- Giá trị số nguyên của biểu thức.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 <br> 2 1 + 3 * | 9 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 10^5$.



### Bài 04 [CPPB-STK-04]: Xóa Ký Tự Trùng Lặp Liền Kề

**Bối cảnh:** Liên tục xóa hai ký tự liền kề giống nhau trong chuỗi $S$ cho đến khi không thể xóa được nữa.

**Nhiệm vụ:** In ra chuỗi kết quả cuối cùng hoặc in `EMPTY` nếu chuỗi rỗng.

**Đầu vào (Input):**

- Một dòng chứa chuỗi $S$ ($1 \le |S| \le 10^5$).

**Đầu ra (Output):**

- Chuỗi kết quả hoặc `EMPTY`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| abbaca | ca |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le |S| \le 10^5$.



### Bài 05 [CPPB-STK-05]: Phần Tử Lớn Hơn Tiếp Theo (Next Greater Element)

**Bối cảnh:** Cho mảng $A$ gồm $N$ số nguyên. Với mỗi vị trí $i$, cần tìm phần tử đầu tiên bên phải có giá trị lớn hơn $A[i]$.

**Nhiệm vụ:** In ra $N$ số nguyên biểu diễn phần tử lớn hơn tiếp theo (hoặc -1 nếu không có).

**Đầu vào (Input):**

- Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

**Đầu ra (Output):**

- $N$ số nguyên cách nhau bởi khoảng trắng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 <br> 4 5 2 25 | 5 25 25 -1 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 10^5, 1 \le A_i \le 10^9$.



### Bài 06 [CPPB-STK-06]: Phần Tử Nhỏ Hơn Gần Nhất Bên Trái (Previous Smaller Element)

**Bối cảnh:** Với mỗi vị trí $i$, tìm phần tử đầu tiên bên trái có giá trị nhỏ hơn $A[i]$.

**Nhiệm vụ:** In ra giá trị của phần tử nhỏ hơn gần nhất bên trái (hoặc -1 nếu không có).

**Đầu vào (Input):**

- Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

**Đầu ra (Output):**

- $N$ số nguyên.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 <br> 4 5 2 10 8 | -1 4 -1 2 2 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 10^5, 1 \le A_i \le 10^9$.



### Bài 07 [CPPB-STK-07]: Độ Dài Đoạn Ngoặc Đúng Liên Tiếp Dài Nhất

**Bối cảnh:** Cho chuỗi $S$ gồm các ký tự `(` và `)`. Cần tìm độ dài lớn nhất của một đoạn con LIÊN TIẾP là dãy ngoặc đúng.

**Nhiệm vụ:** In ra độ dài lớn nhất.

**Đầu vào (Input):**

- Một dòng chứa chuỗi $S$ ($1 \le |S| \le 10^5$).

**Đầu ra (Output):**

- Độ dài lớn nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| )()()) | 4 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le |S| \le 10^5$.



### Bài 08 [CPPB-STK-08]: Xóa K Chữ Số Để Được Số Nhỏ Nhất

**Bối cảnh:** Cho số nguyên dương $S$ biểu diễn dạng chuỗi và số nguyên $K$. Cần xóa đúng $K$ chữ số sao cho số nhận được là nhỏ nhất có thể.

**Nhiệm vụ:** In ra số nhỏ nhất sau khi xóa.

**Đầu vào (Input):**

- Một dòng gồm chuỗi số $S$ ($1 \le |S| \le 10^5$) và số $K$ ($0 \le K < |S|$).

**Đầu ra (Output):**

- Số nhỏ nhất tìm được.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 1432219 3 | 1219 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le |S| \le 10^5$.



### Bài 09 [CPPB-STK-09]: Hình Chữ Nhật Lớn Nhất Trên Histogram

**Bối cảnh:** Cho biểu đồ cột gồm $N$ cột liền kề có chiều rộng bằng 1 và chiều cao lần lượt là $H_i$.

**Nhiệm vụ:** Tìm diện tích hình chữ nhật lớn nhất có thể tạo thành từ các cột biểu đồ.

**Đầu vào (Input):**

- Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $H_1, H_2, \dots, H_N$ ($0 \le H_i \le 10^9$).

**Đầu ra (Output):**

- Diện tích lớn nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 6 <br> 2 1 5 6 2 3 | 10 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 10^5, 0 \le H_i \le 10^9$.



### Bài 10 [CPPB-STK-10]: Hứng Nước Mưa (Trapping Rain Water)

**Bối cảnh:** Cho bản đồ độ cao gồm $N$ cột có chiều rộng 1. Sau cơn mưa, nước sẽ bị đọng lại giữa các cột.

**Nhiệm vụ:** Tính tổng thể tích nước mưa đọng lại.

**Đầu vào (Input):**

- Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên không âm $H_1, H_2, \dots, H_N$ ($0 \le H_i \le 10^5$).

**Đầu ra (Output):**

- Tổng lượng nước mưa đọng lại.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 12 <br> 0 1 0 2 1 0 1 3 2 1 2 1 | 6 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 10^5, 0 \le H_i \le 10^5$.



### Bài 11 [CPPB-STK-11]: Hình Chữ Nhật Toàn 1 Lớn Nhất Trong Ma Trận

**Bối cảnh:** Cho ma trận $N \times M$ gồm các số `0` và `1`.

**Nhiệm vụ:** Tìm diện tích hình chữ nhật lớn nhất chỉ chứa toàn số 1.

**Đầu vào (Input):**

- Dòng 1: Hai số $N$ và $M$ ($1 \le N, M \le 1000$).
- $N$ dòng tiếp theo biểu diễn ma trận.

**Đầu ra (Output):**

- Diện tích lớn nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 5 <br> 10100 <br> 10111 <br> 11111 <br> 10010 | 6 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N, M \le 1000$.



### Bài 12 [CPPB-STK-12]: Tổng Giá Trị Nhỏ Nhất Của Mọi Đoạn Con

**Bối cảnh:** Cho mảng $A$ gồm $N$ phần tử. Với mỗi đoạn con $[i, j]$ ($1 \le i \le j \le N$), gọi $\min(A[i..j])$ là giá trị nhỏ nhất của đoạn đó.

**Nhiệm vụ:** Tính tổng giá trị nhỏ nhất của tất cả các đoạn con lấy dư cho $10^9+7$.

**Đầu vào (Input):**

- Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

**Đầu ra (Output):**

- Tổng theo modulo $10^9 + 7$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 <br> 3 1 2 4 | 17 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 10^5, 1 \le A_i \le 10^9$.



### Bài 13 [CPPB-STK-13]: Next Greater Element Trên Mảng Vòng Tròn

**Bối cảnh:** Mảng $A$ là mảng xoay vòng (sau phần tử cuối cùng $A_N$ là phần tử đầu tiên $A_1$).

**Nhiệm vụ:** Tìm phần tử lớn hơn tiếp theo theo thứ tự vòng tròn cho mỗi vị trí.

**Đầu vào (Input):**

- Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

**Đầu ra (Output):**

- $N$ số nguyên.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 <br> 1 2 1 | 2 -1 2 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 10^5, 1 \le A_i \le 10^9$.



### Bài 14 [CPPB-STK-14]: Tầm Nhìn Tòa Tháp (Stock Span)

**Bối cảnh:** Có $N$ tòa tháp xếp thành một hàng. Tầm nhìn sang trái của tòa tháp $i$ là số lượng tòa tháp liên tiếp về phía trước có chiều cao $\le H_i$ (tính cả chính nó).

**Nhiệm vụ:** In ra tầm nhìn của từng tòa tháp.

**Đầu vào (Input):**

- Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $H_1, H_2, \dots, H_N$ ($1 \le H_i \le 10^9$).

**Đầu ra (Output):**

- $N$ số nguyên.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 7 <br> 100 80 60 70 60 75 85 | 1 1 1 2 1 4 6 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 10^5, 1 \le H_i \le 10^9$.



### Bài 15 [CPPB-STK-15]: Đánh Giá Biểu Thức Trung Tố (Infix Expression)

**Bối cảnh:** Cho một biểu thức đại số gồm các số nguyên dương, dấu ngoặc `()` và 4 phép toán `+`, `-`, `*`, `/`.

**Nhiệm vụ:** Tính giá trị của biểu thức tuân theo đúng thứ tự ưu tiên toán học.

**Đầu vào (Input):**

- Một dòng chứa chuỗi biểu thức $S$ ($1 \le |S| \le 10^5$).

**Đầu ra (Output):**

- Giá trị số nguyên của biểu thức.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3+2*2 | 7 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le |S| \le 10^5$.




# Bài 18: Cấu trúc dữ liệu hàng đợi (queue, deque) & Monotonic Deque

## 1. Bản chất cấu trúc dữ liệu hàng đợi (queue & deque)

### 1.1. Hàng đợi chuẩn (queue — FIFO)
Hàng đợi hoạt động theo nguyên lý **FIFO (First In, First Out — Vào trước, Ra trước)**:

* Phần tử được thêm vào ở đuôi (`push`), và được lấy ra ở đầu (`pop`).
* Đây là cấu trúc dữ liệu nền tảng của thuật toán Tìm kiếm theo chiều rộng (BFS).



![Cơ chế FIFO của Queue và Lan tỏa BFS](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-18-hang-doi-queue-deque/assets/queue_fifo_operation_vi.png)



### 1.2. Hàng đợi hai đầu (double-ended queue — Deque)
`std::deque` cho phép thực hiện thêm và xóa phần tử ở **CẢ HAI ĐẦU** với độ phức tạp tối ưu $\mathcal{O}(1)$:

* `push_front()`, `pop_front()`: Thao tác ở đầu hàng đợi.
* `push_back()`, `pop_back()`: Thao tác ở đuôi hàng đợi.

## 2. Kỹ thuật deque cửa sổ trượt min/max $\mathcal{O}(N)$ (Sliding Window Monotonic Deque)

### 2.1. Bản chất bài toán

* Cho mảng $A$ gồm $N$ phần tử và số $K$. Cần tìm giá trị nhỏ nhất (hoặc lớn nhất) trong mọi cửa sổ trượt độ dài $K$: $[i-K+1 \dots i]$ ($K \le i \le N$).
* **Cách dùng Multiset / Priority Queue:** Mất $\mathcal{O}(N \log K)$.
* **Cách dùng Monotonic Deque:** Đạt thời gian tối ưu tuyệt đối **$\mathcal{O}(N)$ tuyến tính**!



![Monotonic Deque Cửa Sổ Trượt](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-18-hang-doi-queue-deque/assets/deque_sliding_window_minmax_vi.png)



### 2.2. Bất biến 3 bước duy trì min cửa sổ
Tại mỗi vị trí $i$ khi phần tử $A[i]$ bước vào:

1. **Loại bỏ phần tử hết hạn (Out of Window):** Nếu phần tử ở đầu `dq.front() < i - K + 1` $\implies$ `dq.pop_front()`.
2. **Duy trì tính đơn điệu tăng:** Trong khi `!dq.empty()` và $A[\text{dq.back()}] \ge A[i] \implies$ `dq.pop_back()` (vì $A[i]$ vừa nhỏ hơn vừa tồn tại lâu hơn các phần tử ở đuôi).
3. **Thêm phần tử mới và lấy đáp án:** `dq.push_back(i)`. Khi $i \ge K-1$, giá trị nhỏ nhất của cửa sổ hiện tại chính là $A[\text{dq.front()}]$.

## 3. Ứng dụng nền tảng: Tìm đường đi ngắn nhất bằng queue (BFS nhập môn)



![Đường đi ngắn nhất bằng BFS](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-18-hang-doi-queue-deque/assets/bfs_shortest_path_unweighted_vi.png)



* Trên đồ thị không có trọng số (hoặc đồ thị lưới di chuyển 4 hướng có chi phí mỗi bước bằng 1), thuật toán BFS sử dụng Queue luôn đảm bảo:

> **Lần đầu tiên một đỉnh $v$ được lấy ra khỏi Queue, khoảng cách $dist[v]$ chắc chắn là khoảng cách ngắn nhất từ đỉnh nguồn $S$.**

## 4. Các bẫy lỗi lập trình kinh điển (bug traps)

1. **Bẫy gọi `q.front()` khi Queue rỗng:**
* Tương tự Stack, gọi `q.front()` hoặc `q.pop()` khi `q.empty() == true` gây Segmentation Fault.
2. **Bẫy lưu giá trị thay vì lưu chỉ số trong Monotonic Deque:**
* Nếu chỉ lưu giá trị $A[i]$, ta không thể kiểm tra xem phần tử ở đầu `dq.front()` đã vượt ra khỏi phạm vi cửa sổ $i - K + 1$ hay chưa.
* **Quy tắc bắt buộc:** Luôn lưu chỉ số $i$ vào trong Deque!
3. **Bẫy quên đánh dấu `visited` ngay khi `push` vào Queue trong BFS:**
* Nếu chờ đến khi `pop` mới đánh dấu `visited[u] = true`, một đỉnh có thể bị đẩy vào Queue hàng chục lần từ các đỉnh lân cận $\implies$ Bùng nổ bộ nhớ và thời gian (TLE/MLE).
* **Quy tắc sống còn:** Bắt buộc gán `visited[v] = true` ngay tại thời điểm `q.push(v)`.

## 5. Mẫu cài đặt chuẩn thi đấu (competitive templates)

### Mẫu 1: Min trên mọi cửa sổ trượt độ dài k bằng Monotonic Deque $\mathcal{O}(N)$

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    if (n <= 0 || k <= 0 || k > n) return 0;

    vector<long long> a(n);

    for (int i = 0; i < n; ++i) {
        cin >> a[i];

    }

    deque<int> dq; // Lưu chỉ số, duy trì A[dq[i]] tăng dần

    vector<long long> result;

    for (int i = 0; i < n; ++i) {
        // 1. Xóa phần tử quá hạn cửa sổ
        while (!dq.empty() && dq.front() < i - k + 1) {
            dq.pop_front();
        }

        // 2. Duy trì tính đơn điệu tăng
        while (!dq.empty() && a[dq.back()] >= a[i]) {
            dq.pop_back();
        }

        // 3. Thêm phần tử hiện tại
        dq.push_back(i);

        // 4. Ghi nhận kết quả khi cửa sổ đủ kích thước k
        if (i >= k - 1) {
            result.push_back(a[dq.front()]);
        }
    }

    for (int i = 0; i < (int)result.size(); ++i) {
        cout << result[i] << (i + 1 == (int)result.size() ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```

### Mẫu 2: BFS tìm bước đi ngắn nhất từ 1 đến n

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    if (n <= 0) return 0;

    vector<vector<int>> adj(n + 1);

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;

        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> dist(n + 1, -1);

    queue<int> q;

    // Khởi tạo gốc 1
    dist[1] = 0;
    q.push(1);

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (int v : adj[u]) {
            if (dist[v] == -1) { // Chưa thăm
                dist[v] = dist[u] + 1;
                q.push(v); // Đánh dấu ngay khi push
            }
        }
    }

    cout << dist[n] << "\n";
    return 0;
}
```

## Bài tập thực hành


### Bài 01 [CPPB-QUE-01]: Cài Đặt Hàng Đợi Cơ Bản

**Bối cảnh:** Mô phỏng hàng đợi FIFO với 3 thao tác: `1 x` (Thêm x vào đuôi), `2` (Xóa đầu hàng đợi), `3` (In ra phần tử ở đầu hàng đợi hoặc `EMPTY`).

**Nhiệm vụ:** In ra kết quả của các thao tác loại 3.

**Đầu vào (Input):**

- Dòng 1: Số nguyên $Q$ ($1 \le Q \le 50000$).
- $Q$ dòng tiếp theo chứa các thao tác.

**Đầu ra (Output):**

- Kết quả các thao tác loại 3.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 <br> 1 10 <br> 1 20 <br> 3 <br> 2 <br> 3 | 10 <br> 20 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le Q \le 50000, 1 \le x \le 10^9$.



### Bài 02 [CPPB-QUE-02]: Sinh Chuỗi Số Nhị Phân Bằng Queue

**Bối cảnh:** Dùng hàng đợi để sinh danh sách $N$ số nhị phân đầu tiên (`1`, `10`, `11`, `100`...) theo thứ tự tăng dần.

**Nhiệm vụ:** In ra $N$ chuỗi số nhị phân cách nhau bởi khoảng trắng.

**Đầu vào (Input):**

- Một dòng chứa số nguyên $N$ ($1 \le N \le 10^5$).

**Đầu ra (Output):**

- $N$ chuỗi nhị phân.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 | 1 10 11 100 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 10^5$.



### Bài 03 [CPPB-QUE-03]: BFS Tìm Bước Đi Ngắn Nhất Đồ Thị

**Bối cảnh:** Cho đồ thị vô hướng $N$ đỉnh $M$ cạnh không có trọng số. Cần tìm số cạnh ít nhất trên đường đi từ đỉnh 1 đến đỉnh $N$.

**Nhiệm vụ:** In ra khoảng cách ngắn nhất hoặc -1 nếu không có đường đi.

**Đầu vào (Input):**

- Dòng 1: Hai số $N$ và $M$ ($1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$).
- $M$ dòng tiếp theo: Mỗi dòng gồm 2 đỉnh $u, v$.

**Đầu ra (Output):**

- Số cạnh ít nhất hoặc -1.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 4 <br> 1 2 <br> 2 3 <br> 3 4 <br> 1 3 | 2 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.



### Bài 04 [CPPB-QUE-04]: Truy Vết Lộ Trình Ngắn Nhất Bằng BFS

**Bối cảnh:** Tìm và in ra chính xác danh sách các đỉnh trên đường đi ngắn nhất từ đỉnh 1 đến đỉnh $N$.

**Nhiệm vụ:** Dòng 1: Số đỉnh trên lộ trình. Dòng 2: Danh sách các đỉnh theo thứ tự đi từ 1 đến $N$. (Nếu không có đường đi in -1).

**Đầu vào (Input):**

- Dòng 1: $N, M$ ($1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$).
- $M$ dòng tiếp theo: Các cạnh vô hướng.

**Đầu ra (Output):**

- Dòng 1: Số đỉnh.
- Dòng 2: Lộ trình các đỉnh.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 5 <br> 1 2 <br> 2 3 <br> 3 5 <br> 1 4 <br> 4 5 | 3 <br> 1 4 5 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.



### Bài 05 [CPPB-QUE-05]: Min Mọi Cửa Sổ Trượt Bằng Monotonic Deque O(N)

**Bối cảnh:** Cho mảng $A$ và số $K$. Tìm giá trị nhỏ nhất trong mỗi cửa sổ trượt độ dài $K$.

**Nhiệm vụ:** In ra $N - K + 1$ số nguyên biểu diễn min từng cửa sổ.

**Đầu vào (Input):**

- Dòng 1: Hai số $N$ và $K$ ($1 \le K \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

**Đầu ra (Output):**

- $N - K + 1$ số nguyên.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 8 3 <br> 1 3 -1 -3 5 3 6 7 | -1 -3 -3 -3 3 3 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le K \le N \le 10^5, -10^9 \le A_i \le 10^9$.



### Bài 06 [CPPB-QUE-06]: Max Mọi Cửa Sổ Trượt Bằng Monotonic Deque O(N)

**Bối cảnh:** Tìm giá trị lớn nhất trong mỗi cửa sổ trượt độ dài $K$ bằng Deque đơn điệu giảm dần $\mathcal{O}(N)$.

**Nhiệm vụ:** In ra $N - K + 1$ giá trị lớn nhất.

**Đầu vào (Input):**

- Dòng 1: Hai số $N$ và $K$ ($1 \le K \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

**Đầu ra (Output):**

- $N - K + 1$ số nguyên.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 8 3 <br> 1 3 -1 -3 5 3 6 7 | 3 3 5 5 6 7 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le K \le N \le 10^5, -10^9 \le A_i \le 10^9$.



### Bài 07 [CPPB-QUE-07]: Kiểm Tra Đồ Thị Hai Phía (Bipartite Graph)

**Bối cảnh:** Đồ thị hai phía là đồ thị có thể tô màu toàn bộ các đỉnh bằng 2 màu sao cho không có 2 đỉnh kề nhau nào cùng màu.

**Nhiệm vụ:** In `YES` nếu đồ thị là hai phía, ngược lại in `NO`.

**Đầu vào (Input):**

- Dòng 1: $N, M$ ($1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$).
- $M$ dòng tiếp theo: Các cạnh vô hướng.

**Đầu ra (Output):**

- `YES` hoặc `NO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 4 <br> 1 2 <br> 2 3 <br> 3 4 <br> 4 1 | YES |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.



### Bài 08 [CPPB-QUE-08]: Biến Đổi Số Bước Nhỏ Nhất Từ A Sang B

**Bối cảnh:** Từ số $A$, mỗi bước có thể nhân 2 ($A \times 2$) hoặc trừ 1 ($A - 1$).

**Nhiệm vụ:** Tìm số thao tác ít nhất để biến đổi $A$ thành $B$.

**Đầu vào (Input):**

- Một dòng chứa hai số nguyên $A$ và $B$ ($1 \le A, B \le 10^4$).

**Đầu ra (Output):**

- Số thao tác ít nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 6 | 2 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le A, B \le 10^4$.



### Bài 09 [CPPB-QUE-09]: 0-1 BFS Tìm Đường Đi Ngắn Nhất Trọng Số 0/1

**Bối cảnh:** Cho đồ thị có trọng số trên các cạnh chỉ nhận giá trị 0 hoặc 1. Cần tìm đường đi ngắn nhất từ đỉnh 1 đến $N$ trong $\mathcal{O}(V + E)$.

**Nhiệm vụ:** In ra tổng trọng số đường đi ngắn nhất hoặc -1 nếu không đến được.

**Đầu vào (Input):**

- Dòng 1: $N, M$ ($1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$).
- $M$ dòng tiếp theo: Mỗi dòng gồm $u, v, w$ ($w \in \{0, 1\}$).

**Đầu ra (Output):**

- Chi phí ngắn nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 4 <br> 1 2 1 <br> 2 3 0 <br> 3 4 1 <br> 1 4 1 | 1 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.



### Bài 10 [CPPB-QUE-10]: Đoạn Con Tổng Lớn Nhất Độ Dài Tối Đa K

**Bối cảnh:** Tìm đoạn con liên tiếp có độ dài từ 1 đến $K$ sao cho tổng các phần tử trong đoạn là lớn nhất.

**Nhiệm vụ:** In ra tổng lớn nhất tìm được.

**Đầu vào (Input):**

- Dòng 1: Hai số $N$ và $K$ ($1 \le K \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

**Đầu ra (Output):**

- Tổng lớn nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 3 <br> -1 2 4 -3 5 | 6 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le K \le N \le 10^5, -10^9 \le A_i \le 10^9$.



### Bài 11 [CPPB-QUE-11]: Trò Chơi Vòng Tròn Josephus

**Bối cảnh:** Có $N$ người xếp thành vòng tròn đánh số $1$ đến $N$. Bắt đầu đếm từ người 1, cứ người thứ $K$ sẽ bị loại bỏ khỏi vòng. Tiếp tục đếm cho đến khi chỉ còn lại 1 người duy nhất.

**Nhiệm vụ:** Tìm vị trí của người sống sót cuối cùng.

**Đầu vào (Input):**

- Một dòng chứa hai số nguyên $N$ và $K$ ($1 \le N, K \le 10^4$).

**Đầu ra (Output):**

- Vị trí người sống sót.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 7 3 | 4 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N, K \le 10^4$.



### Bài 12 [CPPB-QUE-12]: Khoảng Cách Đến Trạm Cứu Hỏa Gần Nhất (Multi-Source BFS)

**Bối cảnh:** Trong thành phố có $N$ ngôi nhà và $K$ trạm cứu hỏa. Cần tính khoảng cách ngắn nhất từ mỗi ngôi nhà đến trạm cứu hỏa gần nhất.

**Nhiệm vụ:** In ra khoảng cách của từng ngôi nhà từ 1 đến $N$.

**Đầu vào (Input):**

- Dòng 1: $N, M, K$ ($1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5, 1 \le K \le N$).
- Dòng 2: Danh sách $K$ trạm cứu hỏa.
- $M$ dòng tiếp theo: Các con đường nối giữa hai nhà.

**Đầu ra (Output):**

- $N$ số nguyên.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 3 2 <br> 1 4 <br> 1 2 <br> 2 3 <br> 3 4 | 0 1 1 0 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.



### Bài 13 [CPPB-QUE-13]: Đoạn Con Dài Nhất Có Độ Chênh Lệch Max-Min <= C

**Bối cảnh:** Tìm độ dài lớn nhất của một đoạn con liên tiếp sao cho chênh lệch giữa phần tử lớn nhất và nhỏ nhất trong đoạn $\le C$.

**Nhiệm vụ:** In ra độ dài lớn nhất.

**Đầu vào (Input):**

- Dòng 1: Hai số $N$ và $C$ ($1 \le N \le 10^5, 0 \le C \le 10^9$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

**Đầu ra (Output):**

- Độ dài lớn nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 6 2 <br> 4 2 2 2 4 4 | 6 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 10^5, 0 \le C, A_i \le 10^9$.



### Bài 14 [CPPB-QUE-14]: Chọn Đoạn Tối Đa Không Quá K Phần Tử Liền Kề

**Bối cảnh:** Cho mảng $A$ gồm $N$ số nguyên dương. Chọn một tập hợp các phần tử sao cho không có quá $K$ phần tử liên tiếp nào cùng được chọn.

**Nhiệm vụ:** Tìm tổng giá trị lớn nhất có thể thu được.

**Đầu vào (Input):**

- Dòng 1: Hai số $N$ và $K$ ($1 \le K \le N \le 10^5$).
- Dòng 2: $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

**Đầu ra (Output):**

- Tổng lớn nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 2 <br> 1 2 3 4 5 | 12 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le K \le N \le 10^5, 1 \le A_i \le 10^9$.



### Bài 15 [CPPB-QUE-15]: Đua Xe Mê Cung Đổi Hướng Ít Nhất (0-1 BFS State)

**Bối cảnh:** Xe đua di chuyển trong mê cung từ vị trí `S` đến `E`. Nếu tiếp tục đi thẳng cùng hướng thì không tốn chi phí (chi phí 0), nếu rẽ sang hướng khác tốn 1 lần bẻ lái (chi phí 1).

**Nhiệm vụ:** Tìm số lần đổi hướng ít nhất để đến đích.

**Đầu vào (Input):**

- Dòng 1: Hai số $N$ và $M$ ($1 \le N, M \le 500$).
- $N$ dòng tiếp theo biểu diễn mê cung.

**Đầu ra (Output):**

- Số lần đổi hướng ít nhất hoặc -1.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 3 <br> S.. <br> .#. <br> ..E | 1 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N, M \le 500$.



# CHƯƠNG 07: ĐỒ THỊ & CÂY TRUY VẤN ĐOẠN


# Bài 19: Lý thuyết đồ thị cơ bản: Duyệt BFS & DFS

## 1. Bản chất đồ thị & các phương pháp biểu diễn

Đồ thị $G = (V, E)$ là cấu trúc toán học biểu diễn tập hợp các đỉnh (Vertices — $V$) và các cạnh nối giữa chúng (Edges — $E$). Đồ thị có thể là vô hướng (Undirected) hoặc có hướng (Directed), có trọng số hoặc không có trọng số.



![Biểu diễn Đồ thị: Ma trận kề vs Danh sách kề](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-19-ly-thuyet-do-thi-bfs-dfs/assets/graph_representations_vi.png)



### 1.1. Ma trận kề (adjacency matrix)

* Mảng 2 chiều `int adj[N][N]`: `adj[u][v] = 1` nếu có cạnh nối giữa $u$ và $v$.
* **Ưu điểm:** Kiểm tra cạnh $(u, v)$ trong $\mathcal{O}(1)$.
* **Nhược điểm:** Tốn $\mathcal{O}(N^2)$ bộ nhớ. Khi $N = 10^5$, ma trận cần $40\text{GB}$ RAM $\implies$ Sập bộ nhớ ngay lập tức (MLE). Chỉ dùng khi $N \le 1000$.

### 1.2. Danh sách kề (adjacency list — Chuẩn mực thi đấu)

* Sử dụng mảng các vector `vector<int> adj[N + 1]`: `adj[u]` chứa toàn bộ các đỉnh kề trực tiếp với $u$.

* **Bộ nhớ:** Đúng $\mathcal{O}(V + E)$, cực kỳ tiết kiệm và tối ưu cho đồ thị thưa trong lập trình thi đấu ($N, M \le 2 \cdot 10^5$).
* **Duyệt đỉnh kề:** `for (int v : adj[u])` tốn thời gian tỷ lệ thuận với bậc của đỉnh $\mathcal{O}(\text{deg}(u))$.

## 2. Hai chiến lược duyệt đồ thị kinh điển: BFS vs DFS



![So sánh BFS vs DFS](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-19-ly-thuyet-do-thi-bfs-dfs/assets/bfs_vs_dfs_traversal_vi.png)



### 2.1. Tìm kiếm theo chiều rộng (breadth-first search — BFS)

* Sử dụng **Hàng đợi (Queue)**, lan tỏa theo từng tầng bán kính $d = 0, 1, 2, \dots$ tính từ đỉnh nguồn $S$.
* **Đặc tính vàng:** Tìm đường đi có ít cạnh nhất (ngắn nhất) trên đồ thị không trọng số.

### 2.2. Tìm kiếm theo chiều sâu (depth-first search — DFS)

* Sử dụng **Đệ quy (hoặc Stack)**, đi sâu hết mức có thể trên một nhánh cho đến khi gặp ngõ cụt thì quay lui (Backtracking).
* **Đặc tính vàng:** Cực kỳ hiệu quả để đếm thành phần liên thông, phát hiện chu trình, kiểm tra tính liên thông, định hướng cây DFS.

## 3. Ứng dụng: Đếm số thành phần liên thông & kiểm tra chu trình



![Đếm số thành phần liên thông](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-19-ly-thuyet-do-thi-bfs-dfs/assets/connected_components_vi.png)



* **Thuật toán đếm thành phần liên thông:** Duyệt qua mọi đỉnh $i \in [1, N]$. Nếu đỉnh $i$ chưa được thăm (`!visited[i]`), tăng biến đếm số thành phần liên thông `components++` và gọi `DFS(i)` để loang thăm toàn bộ các đỉnh thuộc cùng thành phần.
* **Phát hiện chu trình trên đồ thị vô hướng bằng DFS:** Khi duyệt từ $u$ sang đỉnh kề $v$, nếu $v$ đã được thăm (`visited[v] == true`) và `v != parent[u]`, ta khẳng định đồ thị **CÓ CHU TRÌNH**!

## 4. Các bẫy lỗi lập trình kinh điển (bug traps)

1. **Bẫy thêm cạnh đồ thị vô hướng chỉ thêm 1 chiều:**
* Với đồ thị vô hướng, cạnh giữa $u$ và $v$ phải thêm cả 2 chiều: `adj[u].push_back(v); adj[v].push_back(u);`. Quên thêm chiều thứ hai làm đồ thị biến thành đồ thị có hướng sai hoàn toàn.
2. **Bẫy tràn ngăn xếp đệ quy (Stack Overflow) khi DFS đồ thị sâu:**
* Nếu đồ thị là một đường thẳng $N = 2 \cdot 10^5$ đỉnh, hàm đệ quy `DFS` sẽ gọi sâu $2 \cdot 10^5$ tầng, vượt quá giới hạn ngăn xếp (Call Stack) của một số hệ điều hành và gây Runtime Error.
3. **Bẫy cạnh lặp và khuyên (Multiple Edges & Self-loops):**
* Đề bài có thể cho nhiều cạnh nối giữa cùng một cặp đỉnh $(u, v)$ hoặc cạnh tự nối $u \to u$. Cần kiểm tra hoặc xử lý cẩn thận nếu thuật toán yêu cầu tính toán bậc hoặc trọng số tối thiểu.

## 5. Mẫu cài đặt chuẩn thi đấu (competitive templates)

### Mẫu 1: DFS đếm số thành phần liên thông và tìm kích thước từng thành phần

> ⚠️ **Lưu ý về Stack Overflow:** Hàm DFS đệ quy dưới đây có thể gây tràn ngăn xếp hệ thống (Segmentation Fault) khi đồ thị có dạng đường thẳng $N = 2 \times 10^5$ đỉnh (độ sâu đệ quy lên tới $N$ tầng). Trong thi đấu thực tế, nên dùng **DFS bằng `std::stack` tường minh** hoặc thiết lập `ulimit -s unlimited` (Linux) trước khi chạy. Mẫu đệ quy được giữ lại ở đây vì tính trực quan sư phạm.

```cpp
#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<vector<int>> adj;

vector<bool> visited;

int dfs(int u) {
    visited[u] = true;
    int comp_size = 1;
    for (int v : adj[u]) {
        if (!visited[v]) {
            comp_size += dfs(v);
        }
    }
    return comp_size;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> m)) return 0;

    if (n <= 0) return 0;

    adj.assign(n + 1, vector<int>());
    visited.assign(n + 1, false);

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;

        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    int component_count = 0;
    vector<int> component_sizes;

    for (int i = 1; i <= n; ++i) {
        if (!visited[i]) {
            component_count++;
            int sz = dfs(i);
            component_sizes.push_back(sz);
        }
    }

    cout << component_count << "\n";
    for (int i = 0; i < (int)component_sizes.size(); ++i) {
        cout << component_sizes[i] << (i + 1 == (int)component_sizes.size() ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```

### Mẫu 2: Phát hiện chu trình trên đồ thị vô hướng bằng DFS

```cpp
#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<vector<int>> adj;

vector<bool> visited;

bool has_cycle = false;

void dfs_cycle(int u, int p) {
    visited[u] = true;
    for (int v : adj[u]) {
        if (!visited[v]) {
            dfs_cycle(v, u);
        } else if (v != p) {
            has_cycle = true; // Gặp lại đỉnh đã thăm khác cha -> Chu trình!

        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> m)) return 0;

    if (n <= 0) return 0;

    adj.assign(n + 1, vector<int>());
    visited.assign(n + 1, false);

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;

        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    for (int i = 1; i <= n; ++i) {
        if (!visited[i]) {
            dfs_cycle(i, 0);
        }
    }

    if (has_cycle) {
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }

    return 0;
}
```

## Bài tập thực hành


### Bài 01 [CPPB-GRA-01]: Chuyển Danh Sách Cạnh Sang Danh Sách Kề

**Bối cảnh:** Cho đồ thị vô hướng $N$ đỉnh $M$ cạnh. Cần chuyển đổi biểu diễn đồ thị sang danh sách kề.

**Nhiệm vụ:** In ra $N$ dòng: Mỗi dòng gồm bậc của đỉnh và danh sách các đỉnh kề tăng dần.

**Đầu vào (Input):**

- Dòng 1: $N, M$ ($1 \le N \le 10000, 0 \le M \le 20000$).
- $M$ dòng tiếp theo: Mỗi dòng gồm 2 đỉnh $u, v$.

**Đầu ra (Output):**

- $N$ dòng biểu diễn danh sách kề.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 2 <br> 1 2 <br> 1 3 | 2 2 3 <br> 1 1 <br> 1 1 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 10000, 0 \le M \le 20000$.



### Bài 02 [CPPB-GRA-02]: Duyệt Đồ Thị Theo Chiều Sâu (DFS Traversal)

**Bối cảnh:** Duyệt đồ thị vô hướng bắt đầu từ đỉnh $S$ bằng thuật toán DFS (ưu tiên thăm đỉnh có chỉ số nhỏ hơn trước).

**Nhiệm vụ:** In ra thứ tự các đỉnh được thăm.

**Đầu vào (Input):**

- Dòng 1: $N, M, S$ ($1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5, 1 \le S \le N$).
- $M$ dòng tiếp theo: Các cạnh vô hướng.

**Đầu ra (Output):**

- Thứ tự các đỉnh được thăm.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 3 1 <br> 1 2 <br> 2 3 <br> 1 4 | 1 2 3 4 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.



### Bài 03 [CPPB-GRA-03]: Duyệt Đồ Thị Theo Chiều Rộng (BFS Traversal)

**Bối cảnh:** Duyệt đồ thị vô hướng từ đỉnh $S$ bằng BFS (ưu tiên các đỉnh kề có số hiệu nhỏ hơn).

**Nhiệm vụ:** In ra thứ tự duyệt BFS.

**Đầu vào (Input):**

- Dòng 1: $N, M, S$ ($1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$).
- $M$ dòng tiếp theo: Các cạnh vô hướng.

**Đầu ra (Output):**

- Thứ tự các đỉnh được thăm.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 3 1 <br> 1 2 <br> 1 3 <br> 2 4 | 1 2 3 4 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.



### Bài 04 [CPPB-GRA-04]: Đếm Số Thành Phần Liên Thông

**Bối cảnh:** Cho đồ thị vô hướng $N$ đỉnh $M$ cạnh. Cần đếm số thành phần liên thông của đồ thị.

**Nhiệm vụ:** In ra số lượng thành phần liên thông.

**Đầu vào (Input):**

- Dòng 1: $N, M$ ($1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$).
- $M$ dòng tiếp theo: Các cạnh vô hướng.

**Đầu ra (Output):**

- Số lượng thành phần liên thông.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 3 <br> 1 2 <br> 2 3 <br> 4 5 | 2 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.



### Bài 05 [CPPB-GRA-05]: Kích Thước Thành Phần Liên Thông Lớn Nhất

**Bối cảnh:** Tìm số lượng đỉnh trong thành phần liên thông có kích thước lớn nhất.

**Nhiệm vụ:** In ra số đỉnh của thành phần liên thông lớn nhất.

**Đầu vào (Input):**

- Dòng 1: $N, M$ ($1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$).
- $M$ dòng tiếp theo: Các cạnh vô hướng.

**Đầu ra (Output):**

- Kích thước lớn nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 3 <br> 1 2 <br> 2 3 <br> 4 5 | 3 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.



### Bài 06 [CPPB-GRA-06]: Kiểm Tra Đường Đi Giữa Hai Đỉnh

**Bối cảnh:** Kiểm tra xem có tồn tại đường đi từ đỉnh $S$ đến đỉnh $T$ trên đồ thị vô hướng hay không.

**Nhiệm vụ:** In `YES` nếu có đường đi, ngược lại in `NO`.

**Đầu vào (Input):**

- Dòng 1: $N, M, S, T$ ($1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5, 1 \le S, T \le N$).
- $M$ dòng tiếp theo: Các cạnh vô hướng.

**Đầu ra (Output):**

- `YES` hoặc `NO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 2 1 4 <br> 1 2 <br> 2 3 | NO |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.



### Bài 07 [CPPB-GRA-07]: Phát Hiện Chu Trình Trên Đồ Thị Vô Hướng

**Bối cảnh:** Kiểm tra xem đồ thị vô hướng $N$ đỉnh $M$ cạnh có chứa chu trình hay không.

**Nhiệm vụ:** In `YES` nếu có chu trình, ngược lại in `NO`.

**Đầu vào (Input):**

- Dòng 1: $N, M$ ($1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$).
- $M$ dòng tiếp theo: Các cạnh vô hướng.

**Đầu ra (Output):**

- `YES` hoặc `NO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 3 <br> 1 2 <br> 2 3 <br> 3 1 | YES |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.



### Bài 08 [CPPB-GRA-08]: Đường Đi Ngắn Nhất Trên Đồ Thị Không Trọng Số

**Bối cảnh:** Tìm số cạnh ít nhất trên đường đi từ đỉnh $1$ đến đỉnh $N$ bằng BFS.

**Nhiệm vụ:** In ra số cạnh ít nhất hoặc -1 nếu không đến được.

**Đầu vào (Input):**

- Dòng 1: $N, M$ ($1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$).
- $M$ dòng tiếp theo: Các cạnh vô hướng.

**Đầu ra (Output):**

- Khoảng cách ngắn nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 4 <br> 1 2 <br> 2 3 <br> 3 4 <br> 1 3 | 2 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.



### Bài 09 [CPPB-GRA-09]: Kiểm Tra Đồ Thị Cây (Tree Verification)

**Bối cảnh:** Một đồ thị vô hướng là cây khi và chỉ khi nó liên thông và có đúng $N - 1$ cạnh.

**Nhiệm vụ:** In `YES` nếu đồ thị là cây, ngược lại in `NO`.

**Đầu vào (Input):**

- Dòng 1: $N, M$ ($1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$).
- $M$ dòng tiếp theo: Các cạnh vô hướng.

**Đầu ra (Output):**

- `YES` hoặc `NO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 3 <br> 1 2 <br> 2 3 <br> 3 4 | YES |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.



### Bài 10 [CPPB-GRA-10]: Sắp Xếp Tô-pô (Topological Sort)

**Bối cảnh:** Cho đồ thị có hướng $N$ đỉnh $M$ cạnh. Hãy tìm một thứ tự tô-pô của các đỉnh (nếu có cạnh $u \to v$ thì $u$ phải đứng trước $v$).

**Nhiệm vụ:** In ra thứ tự tô-pô hoặc -1 nếu đồ thị có chu trình.

**Đầu vào (Input):**

- Dòng 1: $N, M$ ($1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$).
- $M$ dòng tiếp theo: Mỗi dòng gồm cạnh có hướng $u \to v$.

**Đầu ra (Output):**

- Thứ tự tô-pô hoặc -1.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 3 <br> 1 2 <br> 2 3 <br> 1 3 | 1 4 2 3 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.



### Bài 11 [CPPB-GRA-11]: Chu Trình Ngắn Nhất Trên Đồ Thị (Girth)

**Bối cảnh:** Tìm độ dài của chu trình đơn có số cạnh ít nhất trên đồ thị vô hướng không trọng số.

**Nhiệm vụ:** In ra độ dài chu trình ngắn nhất hoặc -1 nếu đồ thị không có chu trình.

**Đầu vào (Input):**

- Dòng 1: $N, M$ ($1 \le N \le 1000, 0 \le M \le 2000$).
- $M$ dòng tiếp theo: Các cạnh vô hướng.

**Đầu ra (Output):**

- Độ dài chu trình ngắn nhất hoặc -1.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 6 <br> 1 2 <br> 2 3 <br> 3 1 <br> 3 4 <br> 4 5 <br> 5 3 | 3 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 1000, 0 \le M \le 2000$.



### Bài 12 [CPPB-GRA-12]: Đếm Cặp Đỉnh Không Thể Đi Tới Nhau

**Bối cảnh:** Đếm số lượng cặp đỉnh $(u, v)$ với $u < v$ sao cho không tồn tại đường đi giữa $u$ và $v$.

**Nhiệm vụ:** In ra số lượng cặp đỉnh không liên thông.

**Đầu vào (Input):**

- Dòng 1: $N, M$ ($1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$).
- $M$ dòng tiếp theo: Các cạnh vô hướng.

**Đầu ra (Output):**

- Số lượng cặp đỉnh.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 2 <br> 1 2 <br> 3 4 | 8 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.



### Bài 13 [CPPB-GRA-13]: Lan Tỏa Virus Trong Mạng Lưới (Multi-Source BFS)

**Bối cảnh:** Có $K$ máy tính ban đầu bị nhiễm virus. Mỗi giây, virus lan sang toàn bộ các máy kề nối trực tiếp.

**Nhiệm vụ:** Tính thời gian tối thiểu để toàn bộ các máy trong mạng bị lây nhiễm (hoặc -1 nếu có máy cô lập không bị nhiễm).

**Đầu vào (Input):**

- Dòng 1: $N, M, K$ ($1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5, 1 \le K \le N$).
- Dòng 2: $K$ máy tính nhiễm virus ban đầu.
- $M$ dòng tiếp theo: Các đường cáp kết nối mạng.

**Đầu ra (Output):**

- Thời gian tối đa để toàn mạng nhiễm virus.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 3 1 <br> 1 <br> 1 2 <br> 2 3 <br> 3 4 | 3 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.



### Bài 14 [CPPB-GRA-14]: Đếm Số Cạnh Cầu Trên Đồ Thị (Bridges)

**Bối cảnh:** Cạnh cầu là cạnh mà khi xóa bỏ nó, số thành phần liên thông của đồ thị sẽ tăng lên (thuật toán Tarjan cơ bản).

**Nhiệm vụ:** In ra số lượng cạnh cầu trên đồ thị.

**Đầu vào (Input):**

- Dòng 1: $N, M$ ($1 \le N \le 50000, 0 \le M \le 10^5$).
- $M$ dòng tiếp theo: Các cạnh vô hướng.

**Đầu ra (Output):**

- Số lượng cạnh cầu.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 5 <br> 1 2 <br> 2 3 <br> 3 1 <br> 3 4 <br> 4 5 | 2 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 50000, 0 \le M \le 10^5$.



### Bài 15 [CPPB-GRA-15]: Xây Dựng Thêm Đường Nối Toàn Mạng (Building Roads)

**Bối cảnh:** Cần xây thêm số con đường ít nhất để mọi thành phố trong cả nước đều có thể đi tới nhau.

**Nhiệm vụ:** Dòng 1: Số đường ít nhất cần xây $K$. $K$ dòng tiếp theo: Mỗi dòng gồm 2 thành phố cần xây đường nối.

**Đầu vào (Input):**

- Dòng 1: $N, M$ ($1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$).
- $M$ dòng tiếp theo: Các con đường hiện có.

**Đầu ra (Output):**

- Dòng 1: Số đường cần xây.
- Các dòng tiếp theo: Danh sách các đường nối.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 2 <br> 1 2 <br> 3 4 | 1 <br> 1 3 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.




# Bài 20: Đồ thị lưới 2D, kỹ thuật Flood Fill & tính chất cây

## 1. Bản chất mô hình hóa lưới 2D thành đồ thị

Trong lập trình thi đấu, ma trận bảng vuông $N \times M$ có thể được xem là một đồ thị đặc biệt:

* Mỗi ô $(r, c)$ là một **Đỉnh** của đồ thị ($1 \le r \le N, 1 \le c \le M$). Tổng số đỉnh $|V| = N \times M$.
* Mỗi bước di chuyển sang các ô kề cạnh (4 hướng: Trên, Dưới, Trái, Phải) tương đương với một **Cạnh** vô hướng có trọng số bằng 1. Tổng số cạnh $|E| \le 4NM$.
* **Ưu điểm vượt trội:** Không cần dựng danh sách kề `vector<int> adj[]`, ta duyệt trực tiếp trên ma trận bằng **Mảng Hướng Dịch Chuyển (`dr`, `dc`)**.



![Mô hình hóa Đồ thị Lưới 2D và Mảng Hướng](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-20-do-thi-luoi-2d-flood-fill/assets/grid_2d_graph_modeling_vi.png)



## 2. Thuật toán loang (Flood Fill)



![Thuật toán Loang Flood Fill](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-20-do-thi-luoi-2d-flood-fill/assets/flood_fill_maze_vi.png)



* **Bản chất:** Từ một ô xuất phát $(r_0, c_0)$, thuật toán lan tỏa (bằng DFS hoặc BFS) sang tất cả các ô lân cận có cùng tính chất (cùng màu, ô đất liền không phải nước biển, ô đường đi không có vật cản).
* **Điều kiện biên hợp lệ (Boundary Invariant):**
  ```cpp
  bool isValid(int r, int c) {
      return (r >= 1 && r <= n && c >= 1 && c <= m && grid[r][c] != '#' && !visited[r][c]);
  }
  ```
* **Ứng dụng kinh điển:** Đếm số lượng hòn đảo (Number of Islands), tính diện tích vùng lớn nhất, tô màu sơn vùng kín, tìm đường thoát khỏi mê cung.

## 3. Lý thuyết cây trên đồ thị (Tree Properties & invariants)



![Đặc tính Bất biến của Cây](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-20-do-thi-luoi-2d-flood-fill/assets/tree_properties_and_cycles_vi.png)



Cây (Tree) là một dạng đồ thị vô hướng đặc biệt có cấu trúc phân cấp chặt chẽ:

1. Đồ thị liên thông gồm $N$ đỉnh và có **đúng $N - 1$ cạnh**.
2. Giữa 2 đỉnh bất kỳ trong cây có **duy nhất một đường đi đơn**.
3. Không chứa bất kỳ chu trình nào.
4. **Duyệt cây bằng DFS:** Bắt đầu từ gốc `root`, khi duyệt từ $u$ sang $v$ chỉ cần điều kiện `if (v != parent)` mà không cần dùng mảng `visited`!

## 4. Các bẫy lỗi lập trình kinh điển (bug traps)

1. **Bẫy tràn chỉ số biên ma trận (Index Out of Bounds):**
* Truy cập `grid[r + dr[d]][c + dc[d]]` trước khi kiểm tra `1 <= r+dr[d] $\le N$` sẽ gây lỗi Segmentation Fault.
* **Quy tắc an toàn:** Luôn kiểm tra tọa độ trong phạm vi $[1, N] \times [1, M]$ trước tiên!
2. **Bẫy nhầm lẫn thứ tự tọa độ Hàng và Cột (`r` vs `c`, `x` vs `y`):**
* Trong toán học, trục $x$ là ngang, $y$ là dọc. Nhưng trong ma trận máy tính, chỉ số thứ nhất là **Hàng** (chiều dọc, $N$), chỉ số thứ hai là **Cột** (chiều ngang, $M$).
* **Chuẩn hóa đặt tên:** Dùng `r` (row) và `c` (col) hoặc $dr$ và $dc$ để triệt tiêu hoàn toàn sự nhầm lẫn.
3. **Bẫy kích thước ma trận hình chữ nhật (khi $N \ne M$):**
* Viết nhầm `c <= n` thay vì `c <= m` khi ma trận có số hàng khác số cột sẽ dẫn đến truy cập sai vùng nhớ hoặc đọc thiếu dữ liệu.

## 5. Mẫu cài đặt chuẩn thi đấu (competitive templates)

### Mẫu 1: Đếm số lượng hòn đảo và diện tích lớn nhất (Flood Fill DFS)

> ⚠️ **Lưu ý về Stack Overflow:** Hàm DFS đệ quy trên lưới 2D có thể gây tràn ngăn xếp hệ thống khi hòn đảo có kích thước lớn (ví dụ lưới $500 \times 500$ toàn ô đất tạo ra độ sâu đệ quy $250{,}000$ tầng). Trong thi đấu thực tế với lưới lớn ($N \times M \ge 10^5$), **nên dùng BFS bằng `std::queue` (xem Mẫu 2 bên dưới)** để tránh hoàn toàn rủi ro này. Mẫu DFS đệ quy được giữ lại vì tính trực quan sư phạm.

```cpp
#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<string> grid;

vector<vector<bool>> visited;

const int dr[] = {-1, 1, 0, 0};
const int dc[] = {0, 0, -1, 1};

bool isValid(int r, int c) {
    return (r >= 0 && r < n && c >= 0 && c < m && grid[r][c] == '1' && !visited[r][c]);
}

int dfs(int r, int c) {
    visited[r][c] = true;
    int area = 1;

    for (int d = 0; d < 4; ++d) {
        int nr = r + dr[d];
        int nc = c + dc[d];
        if (isValid(nr, nc)) {
            area += dfs(nr, nc);
        }
    }
    return area;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> m)) return 0;

    if (n <= 0 || m <= 0) return 0;

    grid.resize(n);
    for (int i = 0; i < n; ++i) {
        cin >> grid[i];

    }

    visited.assign(n, vector<bool>(m, false));
    int island_count = 0;
    int max_area = 0;

    for (int r = 0; r < n; ++r) {
        for (int c = 0; c < m; ++c) {
            if (grid[r][c] == '1' && !visited[r][c]) {
                island_count++;
                max_area = max(max_area, dfs(r, c));
            }
        }
    }

    cout << island_count << " " << max_area << "\n";
    return 0;
}
```

### Mẫu 2: Tìm đường đi ngắn nhất trong mê cung (grid BFS)

```cpp
#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<string> grid;

vector<vector<int>> dist;

const int dr[] = {-1, 1, 0, 0};
const int dc[] = {0, 0, -1, 1};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> m)) return 0;

    if (n <= 0 || m <= 0) return 0;

    grid.resize(n);
    int sr = -1, sc = -1, er = -1, ec = -1;

    for (int r = 0; r < n; ++r) {
        cin >> grid[r];

        for (int c = 0; c < m; ++c) {
            if (grid[r][c] == 'S') { sr = r; sc = c; }
            if (grid[r][c] == 'E') { er = r; ec = c; }
        }
    }

    dist.assign(n, vector<int>(m, -1));
    queue<pair<int, int>> q;

    dist[sr][sc] = 0;
    q.push({sr, sc});

    while (!q.empty()) {
        auto [r, c] = q.front();
        q.pop();

        if (r == er && c == ec) break;

        for (int d = 0; d < 4; ++d) {
            int nr = r + dr[d];
            int nc = c + dc[d];

            if (nr >= 0 && nr < n && nc >= 0 && nc < m && grid[nr][nc] != '#' && dist[nr][nc] == -1) {
                dist[nr][nc] = dist[r][c] + 1;
                q.push({nr, nc});
            }
        }
    }

    cout << dist[er][ec] << "\n";
    return 0;
}
```

## Bài tập thực hành


### Bài 01 [CPPB-GRD-01]: Đếm Số Ô Kề Cạnh Hợp Lệ (4 Hướng)

**Bối cảnh:** Cho ma trận $N \times M$ với các ô có chỉ số 0-based từ $(0, 0)$ đến $(N-1, M-1)$. Cho tọa độ $(r, c)$.

**Nhiệm vụ:** Đếm số ô kề cạnh (trên, dưới, trái, phải) của ô $(r, c)$ nằm hoàn toàn bên trong ma trận.

**Đầu vào (Input):**

- Một dòng chứa 4 số nguyên $N, M, r, c$ ($1 \le N, M \le 1000, 0 \le r < N, 0 \le c < M$).

**Đầu ra (Output):**

- Số lượng ô kề hợp lệ.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 3 0 0 | 2 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N, M \le 1000$.



### Bài 02 [CPPB-GRD-02]: Đếm Số Lượng Hòn Đảo (Count Islands)

**Bối cảnh:** Cho bản đồ ma trận $N \times M$ gồm các ký tự `'1'` (đất liền) và `'0'` (nước biển). Các ô đất liền kề nhau 4 hướng tạo thành một hòn đảo.

**Nhiệm vụ:** Đếm số lượng hòn đảo trên bản đồ.

**Đầu vào (Input):**

- Dòng 1: Hai số $N$ và $M$ ($1 \le N, M \le 1000$).
- $N$ dòng tiếp theo: Ma trận nhị phân.

**Đầu ra (Output):**

- Số hòn đảo.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 5 <br> 11000 <br> 11000 <br> 00100 <br> 00011 | 3 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N, M \le 1000$.



### Bài 03 [CPPB-GRD-03]: Diện Tích Hòn Đảo Lớn Nhất (Max Area of Island)

**Bối cảnh:** Tìm diện tích (số ô đất liền `'1'`) của hòn đảo lớn nhất trên ma trận bản đồ $N \times M$.

**Nhiệm vụ:** In ra diện tích lớn nhất (hoặc 0 nếu không có đất liền).

**Đầu vào (Input):**

- Dòng 1: $N, M$ ($1 \le N, M \le 1000$).
- $N$ dòng tiếp theo biểu diễn ma trận.

**Đầu ra (Output):**

- Diện tích lớn nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 5 <br> 11000 <br> 11000 <br> 00100 <br> 00011 | 4 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N, M \le 1000$.



### Bài 04 [CPPB-GRD-04]: Tìm Đường Thoát Khỏi Mê Cung BFS

**Bối cảnh:** Tìm số bước đi ngắn nhất từ vị trí xuất phát `S` đến lối thoát `E` trong mê cung.

**Nhiệm vụ:** In ra số bước ngắn nhất hoặc -1 nếu không thể thoát.

**Đầu vào (Input):**

- Dòng 1: $N, M$ ($1 \le N, M \le 1000$).
- $N$ dòng tiếp theo biểu diễn mê cung.

**Đầu ra (Output):**

- Số bước ngắn nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 8 <br> ######## <br> #.A#...# <br> #.##.#B# <br> #......# <br> ######## | 9 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N, M \le 1000$.



### Bài 05 [CPPB-GRD-05]: Truy Vết Đường Đi Mê Cung (L, R, U, D)

**Bối cảnh:** In ra lộ trình bước đi cụ thể gồm các ký tự `'L'`, `'R'`, `'U'`, `'D'` từ `A` đến `B`.

**Nhiệm vụ:** Dòng 1: `YES` và số bước (hoặc `NO`). Dòng 2: Chuỗi các hướng đi.

**Đầu vào (Input):**

- Dòng 1: $N, M$ ($1 \le N, M \le 1000$).
- $N$ dòng tiếp theo: Ma trận mê cung.

**Đầu ra (Output):**

- Lộ trình các bước đi.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 8 <br> ######## <br> #.A#...# <br> #.##.#B# <br> #......# <br> ######## | YES <br> 9 <br> LDDRRRRRU |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N, M \le 1000$.



### Bài 06 [CPPB-GRD-06]: Đếm Số Ô Vùng Kín Không Thông Ra Biên

**Bối cảnh:** Cho ma trận gồm các số `0` và `1`. Một ô `0` được gọi là vùng kín nếu nó không có đường thông qua các ô 0 khác để đi ra viền biên ngoài cùng của ma trận.

**Nhiệm vụ:** Đếm số lượng ô 0 thuộc vùng kín.

**Đầu vào (Input):**

- Dòng 1: $N, M$ ($1 \le N, M \le 1000$).
- $N$ dòng tiếp theo biểu diễn ma trận.

**Đầu ra (Output):**

- Số ô 0 vùng kín.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 4 <br> 1111 <br> 1001 <br> 1101 <br> 1111 | 3 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N, M \le 1000$.



### Bài 07 [CPPB-GRD-07]: Chu Vi Hòn Đảo (Island Perimeter)

**Bối cảnh:** Mỗi ô đất liền kích thước $1 \times 1$ có 4 cạnh. Cạnh nào tiếp xúc với nước hoặc tiếp xúc với biên ngoài ma trận sẽ đóng góp 1 đơn vị vào chu vi.

**Nhiệm vụ:** Tính tổng chu vi của các hòn đảo.

**Đầu vào (Input):**

- Dòng 1: $N, M$ ($1 \le N, M \le 1000$).
- $N$ dòng tiếp theo biểu diễn ma trận.

**Đầu ra (Output):**

- Tổng chu vi.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 4 <br> 0100 <br> 1110 <br> 0100 <br> 1100 | 16 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N, M \le 1000$.



### Bài 08 [CPPB-GRD-08]: Nước Tràn Mê Cung (Multi-Source BFS)

**Bối cảnh:** Nước biển tràn vào mê cung từ nhiều nguồn xuất phát cùng lúc. Mỗi giây, nước lan sang các ô lân cận 4 hướng.

**Nhiệm vụ:** Tính thời gian ít nhất để nước ngập đến vị trí đích (hoặc -1).

**Đầu vào (Input):**

- Dòng 1: $N, M$ ($1 \le N, M \le 1000$).
- $N$ dòng tiếp theo: Ma trận với `W` (nguồn nước), `E` (đích), `.` (đường), `#` (tường).

**Đầu ra (Output):**

- Thời gian ngập hoặc -1.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 3 <br> W.. <br> .## <br> ..E | 4 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N, M \le 1000$.



### Bài 09 [CPPB-GRD-09]: Bước Nhảy Quân Mã Ngắn Nhất (Knight Moves)

**Bối cảnh:** Quân mã di chuyển hình chữ L (8 hướng) trên bàn cờ $N \times M$.

**Nhiệm vụ:** Tìm số nước đi ít nhất để quân mã đi từ $(sr, sc)$ đến $(er, ec)$.

**Đầu vào (Input):**

- Một dòng gồm 6 số: $N, M, sr, sc, er, ec$ ($1 \le N, M \le 1000, 0 \le sr, er < N, 0 \le sc, ec < M$).

**Đầu ra (Output):**

- Số bước ít nhất hoặc -1.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 8 8 0 0 7 7 | 6 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N, M \le 1000$.



### Bài 10 [CPPB-GRD-10]: Đường Kính Của Cây (Tree Diameter)

**Bối cảnh:** Cho một cây gồm $N$ đỉnh. Đường kính của cây là khoảng cách lớn nhất giữa hai đỉnh bất kỳ trên cây.

**Nhiệm vụ:** In ra đường kính của cây.

**Đầu vào (Input):**

- Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
- $N - 1$ dòng tiếp theo: Các cạnh của cây.

**Đầu ra (Output):**

- Đường kính cây.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 <br> 1 2 <br> 1 3 <br> 3 4 <br> 3 5 | 3 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 10^5$.



### Bài 11 [CPPB-GRD-11]: Trọng Tâm Của Cây (Tree Centroid)

**Bối cảnh:** Trọng tâm của cây là đỉnh mà khi loại bỏ nó, mỗi thành phần liên thông còn lại có số đỉnh không vượt quá $N / 2$.

**Nhiệm vụ:** Tìm một trọng tâm của cây.

**Đầu vào (Input):**

- Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
- $N - 1$ dòng tiếp theo: Các cạnh của cây.

**Đầu ra (Output):**

- Số hiệu đỉnh trọng tâm.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 <br> 1 2 <br> 2 3 <br> 3 4 <br> 3 5 | 3 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 10^5$.



### Bài 12 [CPPB-GRD-12]: Cổng Dịch Chuyển Tức Thời (Teleport Maze)

**Bối cảnh:** Các ô có cùng chữ cái in hoa `A` đến `Z` là các cổng dịch chuyển tức thời (bước vào cổng này có thể nhảy sang cổng cùng chữ cái khác trong 0 bước).

**Nhiệm vụ:** Tìm số bước đi ngắn nhất từ ô $(0, 0)$ đến $(N-1, M-1)$.

**Đầu vào (Input):**

- Dòng 1: $N, M$ ($1 \le N, M \le 500$).
- $N$ dòng tiếp theo biểu diễn ma trận.

**Đầu ra (Output):**

- Số bước ngắn nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 3 <br> ..A <br> .## <br> A.. | 2 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N, M \le 500$.



### Bài 13 [CPPB-GRD-13]: Lây Lan Quả Cam Hỏng (Rotting Oranges)

**Bối cảnh:** Ma trận chứa `0` (ô trống), `1` (cam tươi), `2` (cam hỏng). Mỗi phút, cam hỏng lan sang 4 quả cam tươi kề cạnh.

**Nhiệm vụ:** Tính thời gian tối thiểu để toàn bộ cam tươi bị hỏng (hoặc -1 nếu không thể hỏng hết).

**Đầu vào (Input):**

- Dòng 1: $N, M$ ($1 \le N, M \le 500$).
- $N$ dòng tiếp theo: Ma trận số 0, 1, 2.

**Đầu ra (Output):**

- Thời gian tối thiểu hoặc -1.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 3 <br> 211 <br> 110 <br> 011 | 4 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N, M \le 500$.



### Bài 14 [CPPB-GRD-14]: Hòn Đảo Nhân Tạo Lớn Nhất (Making A Large Island)

**Bối cảnh:** Bạn được phép thay đổi đúng một ô nước `'0'` thành ô đất `'1'` để nối các hòn đảo lại với nhau.

**Nhiệm vụ:** Tìm diện tích lớn nhất của hòn đảo có thể thu được.

**Đầu vào (Input):**

- Dòng 1: $N, M$ ($1 \le N, M \le 500$).
- $N$ dòng tiếp theo biểu diễn ma trận.

**Đầu ra (Output):**

- Diện tích lớn nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 2 2 <br> 10 <br> 01 | 3 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N, M \le 500$.



### Bài 15 [CPPB-GRD-15]: Thoát Khỏi Mê Cung Quái Vật (Monsters Maze)

**Bối cảnh:** Bạn đứng ở `A`, có nhiều quái vật ở các vị trí `M`. Mỗi giây, bạn và quái vật cùng di chuyển 4 hướng. Bạn thoát thành công nếu đến được một ô biên của ma trận trước quái vật.

**Nhiệm vụ:** In `YES` nếu có thể thoát hiểm, ngược lại in `NO`.

**Đầu vào (Input):**

- Dòng 1: $N, M$ ($1 \le N, M \le 500$).
- $N$ dòng tiếp theo: Ma trận gồm `#`, `.`, `A`, `M`.

**Đầu ra (Output):**

- `YES` hoặc `NO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 8 <br> ######## <br> #M..A..# <br> #.#.M#.# <br> #M#..#..# <br> #.###### | YES |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N, M \le 500$.




# Bài 21: Cấu trúc cây phân đoạn (Segment Tree) & Fenwick Tree (BIT)

## 1. Bản chất bài toán truy vấn đoạn động (dynamic range queries)

Cho mảng $A$ gồm $N$ phần tử. Cần thực hiện liên tiếp $Q$ thao tác thuộc 2 loại:

1. **Cập nhật điểm (Point Update):** Thay đổi giá trị $A[i] \gets v$ (hoặc $A[i] \gets A[i] + v$).
2. **Truy vấn đoạn (Range Query):** Tính tổng $\sum_{k=L}^R A[k]$ hoặc tìm $\min_{k=L}^R A[k]$ / $\max_{k=L}^R A[k]$.

| Cấu Trúc | Khởi Tạo (Build) | Cập Nhật Điểm (Update) | Truy Vấn Đoạn (Query) | Bộ Nhớ |
|---|:---:|:---:|:---:|:---:|
| **Mảng Tiền Tố (Prefix Sum)** | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ *(Quá chậm khi có update)* | $\mathcal{O}(1)$ | $\mathcal{O}(N)$ |
| **Cây Fenwick (BIT)** | $\mathcal{O}(N)$ | $\mathcal{O}(\log N)$ *(Cực nhanh)* | $\mathcal{O}(\log N)$ | $\mathcal{O}(N)$ |
| **Cây Phân Đoạn (Segment Tree)** | $\mathcal{O}(N)$ | $\mathcal{O}(\log N)$ *(Cực nhanh)* | $\mathcal{O}(\log N)$ | $\mathcal{O}(4N)$ |



![So sánh các cấu trúc Range Query](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-21-cay-phan-doan-segment-tree-fenwick/assets/point_update_range_query_vi.png)



## 2. Cây fenwick (Binary Indexed Tree — BIT)



![Cây Fenwick và Phép toán Lowbit](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-21-cay-phan-doan-segment-tree-fenwick/assets/fenwick_tree_lowbit_vi.png)



### 2.1. Phép toán ma thuật: `lowbit(x) = x & (-x)`
Phép toán `x & (-x)` trích xuất bit $1$ thấp nhất (trọng số nhỏ nhất) của số nguyên $x$.

* Mỗi vị trí $x$ trong mảng `bit[x]` quản lý tổng của một đoạn con có độ dài đúng bằng `lowbit(x)` kết thúc tại $x$:
$$\text{Đoạn quản lý của } x = (x - \text{lowbit}(x), x]$$

### 2.2. Hai thao tác cốt lõi siêu tinh gọn (chỉ 5 dòng code)
```cpp
void update(int x, long long val) {
    for (; x <= n; x += x & -x) bit[x] += val;
}

long long query(int x) { // Tính tổng tiền tố A[1..x]
    long long sum = 0;
    for (; x > 0; x -= x & -x) sum += bit[x];

    return sum;
}

long long range_query(int L, int R) {
    return query(R) - query(L - 1);
}
```

## 3. Cây phân đoạn (Segment Tree)



![Cây Phân Đoạn Segment Tree](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-21-cay-phan-doan-segment-tree-fenwick/assets/segment_tree_binary_tree_vi.png)



### 3.1. Cấu trúc cây nhị phân hoàn hảo

* Cây phân đoạn biểu diễn mảng quản lý theo cây nhị phân: Nút gốc $id = 1$ quản lý toàn đoạn $[1, N]$.
* Nút con trái quản lý nửa trái $[L, mid]$ tại vị trí $2 \cdot id$.
* Nút con phải quản lý nửa phải $[mid + 1, R]$ tại vị trí $2 \cdot id + 1$.
* **Quy tắc bộ nhớ:** Mảng cây Segment Tree cần khai báo **$4N$ phần tử** để đảm bảo không bị tràn chỉ số khi $N$ không phải là lũy thừa của 2.

### 3.2. Ưu thế vượt trội của Segment Tree
Khác với Fenwick Tree chủ yếu hỗ trợ phép toán có tính nghịch đảo (như phép cộng tổng), Segment Tree hỗ trợ **MỌI PHÉP TOÁN KẾT HỢP (Associative Operations)**:

* Tìm giá trị nhỏ nhất / lớn nhất trên đoạn (Range Minimum / Maximum Query — RMQ).
* Tìm ước chung lớn nhất trên đoạn ($\text{GCD}(A[L \dots R])$).
* Đếm số lượng phần tử đạt cực đại trên đoạn.

## 4. Các bẫy lỗi lập trình kinh điển (bug traps)

1. **Bẫy quên khai báo mảng Segment Tree kích thước $4N$:**
* Khai báo `tree[2  N]` hoặc `tree[N]` sẽ bị tràn mảng (Out of Bounds) khi $N = 10^5$. Bắt buộc phải khai báo kích thước tối thiểu $4N$ (`vector<long long> tree(4  n + 5)`).

2. **Bẫy chỉ số 0-based của Fenwick Tree (Vòng lặp vô tận):**
* Trong Fenwick Tree, `lowbit(0) = 0 & -0 = 0`. Nếu gọi `update(0, val)` hoặc `query(0)`, vòng lặp $x \gets x + (x \ \& \ -x)$ sẽ biến thành `x += 0` và chạy vô tận $\implies$ Time Limit Exceeded!
* **Bất biến sống còn:** Fenwick Tree **BẮT BUỘC DÙNG CHỈ SỐ 1-BASED** ($x \ge 1$).
3. **Bẫy tràn số khi cộng dồn tổng trên cây:**
* Mảng $N = 10^5$ phần tử có giá trị $10^9 \implies$ Tổng đoạn có thể lên tới $10^{14}$. Mảng `tree` và `bit` bắt buộc phải dùng kiểu `long long`.

## 5. Mẫu cài đặt chuẩn thi đấu (competitive templates)

### Mẫu 1: Cây fenwick (BIT) point update & range sum query

```cpp
#include <bits/stdc++.h>
using namespace std;

struct FenwickTree {
    int n;
    vector<long long> bit;

    FenwickTree(int n) : n(n), bit(n + 1, 0) {}

    void update(int x, long long val) {
        for (; x <= n; x += x & -x) {
            bit[x] += val;
        }
    }

    long long query(int x) {
        long long sum = 0;
        for (; x > 0; x -= x & -x) {

            sum += bit[x];
        }
        return sum;
    }

    long long queryRange(int l, int r) {
        if (l > r) return 0;

        return query(r) - query(l - 1);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    if (n <= 0) return 0;

    FenwickTree ft(n);

    for (int i = 1; i <= n; ++i) {
        long long x;
        cin >> x;

        ft.update(i, x);
    }

    while (q--) {
        int type;
        cin >> type;

        if (type == 1) { // Update: A[pos] += val
            int pos;
            long long val;
            cin >> pos >> val;

            ft.update(pos, val);
        } else { // Query: Sum(L..R)
            int l, r;
            cin >> l >> r;

            cout << ft.queryRange(l, r) << "\n";
        }
    }

    return 0;
}
```

### Mẫu 2: Cây phân đoạn (Segment Tree) range minimum query (RMQ)

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long INF = 1e18;

struct SegmentTree {
    int n;
    vector<long long> tree;

    SegmentTree(int n) : n(n), tree(4 * n + 5, INF) {}

    void build(const vector<long long>& a, int id, int l, int r) {
        if (l == r) {
            tree[id] = a[l];
            return;
        }
        int mid = (l + r) / 2;
        build(a, 2 * id, l, mid);
        build(a, 2 * id + 1, mid + 1, r);
        tree[id] = min(tree[2 * id], tree[2 * id + 1]);
    }

    void update(int id, int l, int r, int pos, long long val) {
        if (l == r) {
            tree[id] = val;
            return;
        }
        int mid = (l + r) / 2;
        if (pos <= mid) {
            update(2 * id, l, mid, pos, val);
        } else {
            update(2 * id + 1, mid + 1, r, pos, val);
        }
        tree[id] = min(tree[2 * id], tree[2 * id + 1]);
    }

    long long query(int id, int l, int r, int u, int v) {
        if (v < l || r < u) return INF; // Ngoài đoạn
        if (u <= l && r <= v) return tree[id]; // Nằm trọn trong đoạn

        int mid = (l + r) / 2;
        return min(query(2 * id, l, mid, u, v),
                   query(2 * id + 1, mid + 1, r, u, v));
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    if (n <= 0) return 0;

    vector<long long> a(n + 1);

    for (int i = 1; i <= n; ++i) {
        cin >> a[i];

    }

    SegmentTree st(n);
    st.build(a, 1, 1, n);

    while (q--) {
        int type;
        cin >> type;

        if (type == 1) { // Gán A[pos] = val
            int pos;
            long long val;
            cin >> pos >> val;

            st.update(1, 1, n, pos, val);
        } else { // Tìm Min trong đoạn [L, R]
            int l, r;
            cin >> l >> r;

            cout << st.query(1, 1, n, l, r) << "\n";
        }
    }

    return 0;
}
```

## Bài tập thực hành


### Bài 01 [CPPB-RNG-01]: Cài Đặt Fenwick Tree Tính Tổng Đoạn (Range Sum)

**Bối cảnh:** Hỗ trợ $Q$ thao tác trên mảng $N$ phần tử: `1 pos val` (cộng thêm `val` vào $A[pos]$) và `2 L R` (tính tổng các phần tử từ $L$ đến $R$).

**Nhiệm vụ:** Với thao tác loại 2, in ra tổng của đoạn $[L, R]$.

**Đầu vào (Input):**

- Dòng 1: $N, Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: $N$ số nguyên ban đầu ($1 \le A_i \le 10^9$).
- $Q$ dòng tiếp theo: Các truy vấn loại 1 và 2.

**Đầu ra (Output):**

- Kết quả các truy vấn loại 2.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 3 <br> 1 2 3 4 5 <br> 2 1 3 <br> 1 2 10 <br> 2 1 3 | 6 <br> 16 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N, Q \le 10^5, 1 \le A_i, val \le 10^9$.



### Bài 02 [CPPB-RNG-02]: Cài Đặt Segment Tree Tìm Min Đoạn (RMQ)

**Bối cảnh:** Hỗ trợ 2 thao tác: `1 pos val` (Gán $A[pos] = val$) và `2 L R` (Tìm giá trị nhỏ nhất trong đoạn $[L, R]$).

**Nhiệm vụ:** In ra giá trị nhỏ nhất cho mỗi truy vấn loại 2.

**Đầu vào (Input):**

- Dòng 1: $N, Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: $N$ số nguyên ban đầu ($1 \le A_i \le 10^9$).
- $Q$ dòng tiếp theo: Các truy vấn.

**Đầu ra (Output):**

- Kết quả các truy vấn loại 2.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 3 <br> 5 2 4 1 3 <br> 2 1 3 <br> 1 4 10 <br> 2 3 5 | 2 <br> 3 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N, Q \le 10^5, 1 \le A_i, val \le 10^9$.



### Bài 03 [CPPB-RNG-03]: Cập Nhật Đoạn & Truy Vấn Điểm (Range Update Point Query)

**Bối cảnh:** Hỗ trợ thao tác `1 L R val` (cộng thêm `val` vào mọi phần tử trong đoạn $[L, R]$) và `2 pos` (in ra giá trị hiện tại của $A[pos]$).

**Nhiệm vụ:** In ra giá trị tại vị trí $pos$ cho các truy vấn loại 2.

**Đầu vào (Input):**

- Dòng 1: $N, Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: $N$ số nguyên ban đầu ($1 \le A_i \le 10^9$).
- $Q$ dòng tiếp theo: Các truy vấn.

**Đầu ra (Output):**

- Kết quả các truy vấn loại 2.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 3 <br> 1 2 3 4 5 <br> 1 2 4 5 <br> 2 3 <br> 2 1 | 8 <br> 1 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N, Q \le 10^5, 1 \le A_i, val \le 10^9$.



### Bài 04 [CPPB-RNG-04]: Tìm Max Đoạn & Đếm Số Lần Xuất Hiện

**Bối cảnh:** Với mỗi truy vấn `2 L R`, tìm giá trị lớn nhất trong đoạn $[L, R]$ và đếm xem giá trị đó xuất hiện bao nhiêu lần trong đoạn.

**Nhiệm vụ:** In ra giá trị lớn nhất và số lần xuất hiện.

**Đầu vào (Input):**

- Dòng 1: $N, Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: $N$ số nguyên ban đầu ($1 \le A_i \le 10^9$).
- $Q$ dòng tiếp theo: Các truy vấn.

**Đầu ra (Output):**

- Kết quả các truy vấn loại 2.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 3 <br> 2 5 3 5 1 <br> 2 1 5 <br> 1 3 5 <br> 2 1 5 | 5 2 <br> 5 3 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N, Q \le 10^5, 1 \le A_i, val \le 10^9$.



### Bài 05 [CPPB-RNG-05]: Đếm Số Cặp Nghịch Thế (Inversion Count)

**Bối cảnh:** Cặp số $(i, j)$ với $i < j$ được gọi là cặp nghịch thế nếu $A[i] > A[j]$.

**Nhiệm vụ:** Tính tổng số cặp nghịch thế trong mảng bằng Cây Fenwick kết hợp nén tọa độ.

**Đầu vào (Input):**

- Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

**Đầu ra (Output):**

- Số lượng cặp nghịch thế.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 <br> 2 4 1 3 5 | 3 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 10^5, 1 \le A_i \le 10^9$.



### Bài 06 [CPPB-RNG-06]: Truy Vấn Ước Chung Lớn Nhất Đoạn (Range GCD)

**Bối cảnh:** Hỗ trợ cập nhật điểm `1 pos val` và truy vấn `2 L R` tính $\text{GCD}(A[L \dots R])$.

**Nhiệm vụ:** In ra GCD của đoạn $[L, R]$.

**Đầu vào (Input):**

- Dòng 1: $N, Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: $N$ số nguyên ban đầu ($1 \le A_i \le 10^9$).
- $Q$ dòng tiếp theo: Các truy vấn.

**Đầu ra (Output):**

- Kết quả các truy vấn loại 2.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 3 <br> 2 4 6 8 10 <br> 2 1 3 <br> 1 2 12 <br> 2 1 3 | 2 <br> 2 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N, Q \le 10^5, 1 \le A_i, val \le 10^9$.



### Bài 07 [CPPB-RNG-07]: Tìm Phần Tử Thứ K Nhỏ Nhất (K-th Element on BIT)

**Bối cảnh:** Hỗ trợ thao tác `1 x` (thêm phần tử x vào tập đa trùng lặp) và `2 k` (tìm phần tử nhỏ thứ k trong tập).

**Nhiệm vụ:** In ra giá trị phần tử thứ k cho các truy vấn loại 2.

**Đầu vào (Input):**

- Dòng 1: Số nguyên $Q$ ($1 \le Q \le 50000$).
- $Q$ dòng tiếp theo: Các truy vấn ($1 \le x \le 2 \cdot 10^5$).

**Đầu ra (Output):**

- Kết quả các truy vấn loại 2.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 <br> 1 10 <br> 1 20 <br> 1 15 <br> 2 2 <br> 2 3 | 15 <br> 20 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le Q \le 50000, 1 \le x \le 2 \cdot 10^5$.



### Bài 08 [CPPB-RNG-08]: Tìm Vị Trí Đầu Tiên Có Giá Trị Lớn Hơn Hoặc Bằng X

**Bối cảnh:** Hỗ trợ truy vấn `2 L R X` tìm chỉ số vị trí nhỏ nhất trong đoạn $[L, R]$ có giá trị $\ge X$ (tìm kiếm nhị phân trên Segment Tree $\mathcal{O}(\log N)$).

**Nhiệm vụ:** In ra chỉ số vị trí tìm được hoặc -1 nếu không có.

**Đầu vào (Input):**

- Dòng 1: $N, Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: $N$ số nguyên ban đầu ($1 \le A_i \le 10^9$).
- $Q$ dòng tiếp theo: Các truy vấn.

**Đầu ra (Output):**

- Kết quả các truy vấn loại 2.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 3 <br> 1 3 2 4 5 <br> 2 1 5 3 <br> 1 2 1 <br> 2 1 5 3 | 2 <br> 4 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N, Q \le 10^5, 1 \le A_i, val, X \le 10^9$.



### Bài 09 [CPPB-RNG-09]: Dãy Con Tăng Dài Nhất LIS Bằng Fenwick Tree

**Bối cảnh:** Tính độ dài của dãy con tăng dài nhất bằng cách dùng Fenwick Tree làm bảng tra cứu max prefix trên mảng nén.

**Nhiệm vụ:** In ra độ dài LIS.

**Đầu vào (Input):**

- Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

**Đầu ra (Output):**

- Độ dài LIS.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 6 <br> 5 2 7 4 3 8 | 3 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 10^5, 1 \le A_i \le 10^9$.



### Bài 10 [CPPB-RNG-10]: Đoạn Con Có Tổng Lớn Nhất Trên Đoạn (Maximum Subarray Query)

**Bối cảnh:** Hỗ trợ cập nhật điểm và truy vấn `2 L R` tìm tổng lớn nhất của một đoạn con liên tiếp nằm trọn trong đoạn $[L, R]$.

**Nhiệm vụ:** In ra tổng đoạn con lớn nhất cho mỗi truy vấn loại 2.

**Đầu vào (Input):**

- Dòng 1: $N, Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: $N$ số nguyên ($-10^9 \le A_i \le 10^9$).
- $Q$ dòng tiếp theo: Các truy vấn.

**Đầu ra (Output):**

- Kết quả các truy vấn loại 2.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 3 <br> 1 2 -5 4 5 <br> 2 1 5 <br> 1 3 10 <br> 2 1 5 | 9 <br> 22 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N, Q \le 10^5, -10^9 \le A_i, val \le 10^9$.



### Bài 11 [CPPB-RNG-11]: Đếm Số Điểm Trong Hình Chữ Nhật (2D Range Query)

**Bối cảnh:** Cho $N$ điểm trên mặt phẳng 2D. Cho $Q$ truy vấn hình chữ nhật $[X_1, X_2] \times [Y_1, Y_2]$.

**Nhiệm vụ:** Đếm số lượng điểm nằm trong mỗi hình chữ nhật.

**Đầu vào (Input):**

- Dòng 1: $N, Q$ ($1 \le N, Q \le 10000$).
- $N$ dòng tiếp theo: Tọa độ $X_i, Y_i$.
- $Q$ dòng tiếp theo: Các truy vấn $X_1, Y_1, X_2, Y_2$.

**Đầu ra (Output):**

- Kết quả $Q$ truy vấn.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 2 <br> 1 1 <br> 2 2 <br> 3 3 <br> 1 1 2 2 <br> 2 2 4 4 | 2 <br> 2 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N, Q \le 10000, 1 \le X_i, Y_i \le 10^5$.



### Bài 12 [CPPB-RNG-12]: Cập Nhật Phân Đoạn Nâng Cao

**Bối cảnh:** Hỗ trợ cập nhật điểm và truy vấn tổng trên cây phân đoạn.

**Nhiệm vụ:** In ra tổng các phần tử trong đoạn.

**Đầu vào (Input):**

- Dòng 1: $N, Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: $N$ số nguyên ban đầu ($1 \le A_i \le 10^9$).
- $Q$ dòng tiếp theo: Các truy vấn.

**Đầu ra (Output):**

- Kết quả các truy vấn loại 2.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 3 <br> 1 2 3 4 5 <br> 2 1 3 <br> 1 2 10 <br> 2 1 3 | 6 <br> 16 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N, Q \le 10^5, 1 \le A_i, val \le 10^9$.



### Bài 13 [CPPB-RNG-13]: Cây Fenwick 2D Tính Tổng Hình Chữ Nhật (2D BIT)

**Bối cảnh:** Hỗ trợ `1 r c val` (cộng thêm `val` vào ô $(r, c)$) và `2 r1 c1 r2 c2` (tính tổng các phần tử trong hình chữ nhật con $[r_1, r_2] \times [c_1, c_2]$).

**Nhiệm vụ:** In ra tổng hình chữ nhật cho mỗi truy vấn loại 2.

**Đầu vào (Input):**

- Dòng 1: $N, M, Q$ ($1 \le N, M \le 1000, 1 \le Q \le 50000$).
- $Q$ dòng tiếp theo: Các truy vấn.

**Đầu ra (Output):**

- Kết quả các truy vấn loại 2.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 3 3 <br> 1 1 1 5 <br> 1 2 2 10 <br> 2 1 1 2 2 | 15 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N, M \le 1000, 1 \le Q \le 50000$.



### Bài 14 [CPPB-RNG-14]: Lazy Propagation — Cập Nhật & Truy Vấn Đoạn (Range Add Range Sum)

**Bối cảnh:** Hỗ trợ thao tác `1 L R val` (cộng `val` vào đoạn $[L, R]$) và `2 L R` (tính tổng các phần tử trong đoạn $[L, R]$) trong $\mathcal{O}(\log N)$ bằng Lazy Propagation.

**Nhiệm vụ:** In ra tổng đoạn cho mỗi truy vấn loại 2.

**Đầu vào (Input):**

- Dòng 1: $N, Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: $N$ số nguyên ban đầu ($1 \le A_i \le 10^9$).
- $Q$ dòng tiếp theo: Các truy vấn.

**Đầu ra (Output):**

- Kết quả các truy vấn loại 2.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 3 <br> 1 2 3 4 5 <br> 1 2 4 2 <br> 2 1 5 <br> 2 2 4 | 21 <br> 15 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N, Q \le 10^5, 1 \le A_i, val \le 10^9$.



### Bài 15 [CPPB-RNG-15]: Hệ Thống Quản Lý Dữ Liệu Olympic (Range Master)

**Bối cảnh:** Bài toán tổng hợp nâng cao quản lý truy vấn cập nhật đoạn và tính tổng đoạn chuẩn Olympic.

**Nhiệm vụ:** In ra kết quả của các truy vấn tính tổng.

**Đầu vào (Input):**

- Dòng 1: $N, Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: $N$ số nguyên ban đầu ($1 \le A_i \le 10^9$).
- $Q$ dòng tiếp theo: Các truy vấn.

**Đầu ra (Output):**

- Kết quả các truy vấn loại 2.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 3 <br> 1 2 3 4 5 <br> 1 2 4 2 <br> 2 1 5 <br> 2 2 4 | 21 <br> 15 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N, Q \le 10^5, 1 \le A_i, val \le 10^9$.




> **Thống kê:** 21 chuyên đề đã nối | 0 thiếu | 8,230 dòng | 448,022 bytes tổng cộng


\newpage

# Phụ lục A: Nền tảng C++

> Phần này ôn tập nhanh các kiến thức nền tảng C++ cần thiết trước khi học thuật toán.

## 1. KHUNG TƯ DUY CỦA MỌI BÀI LẬP TRÌNH

Mọi bài toán đều bắt đầu bằng chuỗi câu hỏi:

```text
Đề bài → Dữ liệu → Biến → Công thức/Điều kiện
       → Các bước xử lý → Code → Kiểm tra kết quả
```

### Mô hình Input – Process – Output

| Thành phần | Câu hỏi cần trả lời |
|---|---|
| **Input** | Chương trình nhận những dữ liệu nào? |
| **Process** | Cần tính toán, kiểm tra hoặc lặp lại việc gì? |
| **Output** | Cần in ra kết quả nào, theo định dạng nào? |

Trước khi viết code, hãy viết bằng lời hoặc pseudocode:

```text
1. Đọc dữ liệu.
2. Tính hoặc xử lý dữ liệu.
3. Kiểm tra điều kiện nếu có.
4. In kết quả.
```

### Công thức trước code

Không viết code trước khi biết mình đang tính gì.

```text
Bài toán → Công thức hoặc quy tắc → Code
```

Ví dụ tính diện tích hình chữ nhật:

```text
S = chiều_dài × chiều_rộng
```

```cpp
long long area = length * width;
```

Ví dụ tính trung bình (giữ phần thập phân):

```cpp
double average = 1.0 * sum / n;
```

### Chuỗi ghi nhớ nền tảng

> **BIẾN → TÍNH → ĐIỀU KIỆN → LẶP → TÍCH LŨY → MẢNG → HÀM → DEBUG**

| Từ khóa | Câu hỏi tự kiểm tra |
|---|---|
| **Biến** | Tôi cần lưu dữ liệu gì? |
| **Tính** | Tôi cần công thức nào? |
| **Điều kiện** | Tôi cần đưa ra quyết định nào? |
| **Lặp** | Tôi cần làm việc gì nhiều lần? |
| **Tích lũy** | Tôi cần cộng, đếm, tìm lớn nhất hay nhỏ nhất? |
| **Mảng** | Tôi có nhiều dữ liệu cùng loại không? |
| **Hàm** | Tôi có thể tách phần việc nào thành một nhiệm vụ riêng? |
| **Debug** | Nếu kết quả sai, tôi sẽ kiểm tra từ đâu? |

---

## 2. KHUNG CHƯƠNG TRÌNH C++ TỐI THIỂU

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // 1. Khai báo biến
    // 2. Đọc dữ liệu
    // 3. Xử lý
    // 4. In kết quả

    return 0;
}
```

| Thành phần | Ý nghĩa |
|---|---|
| `#include <bits/stdc++.h>` | Nạp các thư viện C++ thường dùng trong thi đấu |
| `using namespace std;` | Cho phép dùng `vector`, `string`, `cin`, `cout`… trực tiếp |
| `int main()` | Điểm bắt đầu thực hiện chương trình |
| `ios::sync_with_stdio(false);` | Tăng tốc nhập/xuất |
| `cin.tie(nullptr);` | Tối ưu liên kết giữa nhập và xuất |
| `return 0;` | Kết thúc chương trình thành công |

Giai đoạn đầu chỉ cần tập trung vào **dữ liệu – xử lý – kết quả**, chưa cần hiểu sâu cơ chế thư viện.

---

## 3. BIẾN VÀ KIỂU DỮ LIỆU

> **Biến là ô nhớ có tên để lưu dữ liệu.**

```cpp
int age = 15;
long long population = 9000000000LL;
double average = 8.5;
char grade = 'A';
string name = "An";
bool passed = true;
```

| Kiểu | Dùng để lưu | Ví dụ |
|---|---|---|
| `int` | Số nguyên thông thường | tuổi, số lượng nhỏ |
| `long long` | Số nguyên lớn hoặc tổng lớn | tổng tiền, tổng mảng |
| `double` | Số thực | trung bình, kết quả đo |
| `char` | Một ký tự | `'A'`, `'7'` |
| `string` | Một chuỗi ký tự | `"Hello"` |
| `bool` | Đúng hoặc sai | `true`, `false` |

### Quy tắc chọn kiểu dữ liệu

| Nếu giá trị… | Nên nghĩ đến… |
|---|---|
| Là số đếm nhỏ | `int` |
| Có thể vượt giới hạn `int`, hoặc là tổng nhiều số | `long long` |
| Có phần thập phân | `double` |
| Là một ký tự duy nhất | `char` |
| Là nhiều ký tự liên tiếp | `string` |
| Chỉ có hai trạng thái đúng/sai | `bool` |

> Khi chưa chắc tổng có lớn hay không, hãy cân nhắc dùng `long long`.

### Khởi tạo biến tích lũy

```cpp
long long sum = 0;
int count = 0;
int mx = -1000000000;
int mn = 1000000000;
```

Biến dùng để cộng hoặc đếm phải có giá trị ban đầu đúng. Không dùng biến chưa khởi tạo.

---

## 4. NHẬP VÀ XUẤT DỮ LIỆU

```cpp
int a, b;
cin >> a >> b;
cout << a + b << '\n';
```

```cpp
string s;
cin >> s;
cout << s << '\n';
```

| Lệnh | Ý nghĩa |
|---|---|
| `cin >> a` | Đọc một giá trị vào biến `a` |
| `cin >> a >> b` | Đọc nhiều giá trị liên tiếp |
| `cout << answer` | In kết quả |
| `<< '\n'` | Xuống dòng |

Nếu cần đọc cả một dòng có khoảng trắng, có thể dùng:

```cpp
getline(cin, s);
```

Trong phần lớn bài thi cơ bản, dữ liệu dạng số hoặc từ không có khoảng trắng có thể đọc bằng `cin >>`.

### Ba mẹo thi đấu thường gặp

```cpp
// 1. Đọc nhiều bộ test đến khi hết file
int n;
while (cin >> n) {
    // xử lý từng bộ test
}

// 2. Đọc dòng có khoảng trắng sau khi đã cin >> n
cin.ignore(numeric_limits<streamsize>::max(), '\n');
getline(cin, s);

// 3. Ép kiểu giữ phần thập phân khi sum là long long
double avg = 1.0 * sum / n;
```

> Cần `#include <bits/stdc++.h>` đã bao gồm `limits` cho `numeric_limits`.

---

## 5. TOÁN TỬ VÀ BIỂU THỨC

### Toán tử số học

| Toán tử | Ý nghĩa | Ví dụ |
|---|---|---|
| `+` | Cộng | `a + b` |
| `-` | Trừ | `a - b` |
| `*` | Nhân | `a * b` |
| `/` | Chia | `a / b` |
| `%` | Phần dư | `a % b` |

### Chia nguyên và phần dư

```cpp
15 / 4 == 3
15 % 4 == 3
```

Khi cả hai toán hạng là số nguyên, phép `/` cho phần nguyên. Toán tử `%` cho phần dư.

| Mẫu | Ý nghĩa |
|---|---|
| `x % 2 == 0` | `x` là số chẵn |
| `x % 2 != 0` | `x` là số lẻ |
| `x % 10` | Chữ số cuối của `x` |
| `x / 10` | Bỏ chữ số cuối của `x` |
| `a % b == 0` | `a` chia hết cho `b` |

### Toán tử so sánh

```cpp
>    <    >=    <=    ==    !=
```

| Toán tử | Ý nghĩa |
|---|---|
| `==` | Bằng nhau |
| `!=` | Khác nhau |
| `>` | Lớn hơn |
| `<` | Nhỏ hơn |
| `>=` | Lớn hơn hoặc bằng |
| `<=` | Nhỏ hơn hoặc bằng |

> **Lưu ý:** Đừng nhầm `=` (gán) với `==` (so sánh).

### Toán tử logic

| Toán tử | Ý nghĩa | Ví dụ |
|---|---|---|
| `&&` | Và | `age >= 10 && age <= 15` |
| `||` | Hoặc | `x == 0 || y == 0` |
| `!` | Phủ định | `!passed` |

---

## 6. ĐIỀU KIỆN — RẼ NHÁNH

### Mẫu cơ bản

```cpp
if (condition) {
    // việc A
} else {
    // việc B
}
```

Mô hình bằng lời:

```text
NẾU điều kiện đúng
    thực hiện A
NGƯỢC LẠI
    thực hiện B
```

### Nhiều trường hợp

```cpp
if (score >= 8) {
    cout << "Gioi";
} else if (score >= 6.5) {
    cout << "Kha";
} else {
    cout << "Can co gang";
}
```

### Điều kiện lồng nhau

Chỉ dùng khi quyết định thứ hai phụ thuộc vào quyết định thứ nhất. Hãy viết điều kiện bằng lời trước để tránh rối.

### Lỗi thường gặp

| Lỗi | Cách kiểm tra |
|---|---|
| Dùng `=` thay cho `==` | Đọc lại mọi điều kiện so sánh |
| Nhầm `>` với `>=` | Kiểm tra trường hợp bằng đúng ngưỡng |
| Thiếu trường hợp | Thử giá trị nhỏ nhất, lớn nhất và đúng biên |
| Điều kiện quá phức tạp | Tách thành các biến `bool` hoặc viết lại bằng lời |

---

## 7. VÒNG LẶP – LÀM MỘT VIỆC NHIỀU LẦN

Trước khi viết vòng lặp, trả lời ba câu hỏi:

1. Việc gì được lặp lại?
2. Biến nào thay đổi sau mỗi lần?
3. Khi nào vòng lặp dừng?

### `for`: biết trước số lần hoặc khoảng lặp

```cpp
for (int i = 0; i < n; i++) {
    // xử lý phần tử thứ i
}
```

Với mảng có `n` phần tử, chỉ số thường chạy từ `0` đến `n - 1`.

### `while`: lặp khi điều kiện còn đúng

```cpp
while (condition) {
    // xử lý
    // phải có cách làm condition thay đổi
}
```

Nếu điều kiện không bao giờ sai, chương trình có thể lặp vô hạn.

### `do..while`: thực hiện ít nhất một lần

```cpp
do {
    // xử lý
} while (condition);
```

Trong phần C++ cơ bản, `for` và `while` là hai dạng cần dùng thành thạo nhất.

### Vòng lặp lồng nhau

```cpp
for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
        // xử lý từng cặp (i, j)
    }
}
```

Nếu vòng ngoài chạy `N` lần và vòng trong chạy `M` lần, số thao tác thường là `O(NM)`.

---

## 8. BỐN MẪU TÍCH LŨY

### Tính tổng

```cpp
long long sum = 0;
for (int x : a) {
    sum += x;
}
```

### Đếm phần tử thỏa điều kiện

```cpp
int count = 0;
for (int x : a) {
    if (x % 2 == 0) count++;
}
```

### Tìm giá trị lớn nhất

```cpp
int mx = a[0];
for (int x : a) {
    mx = max(mx, x);
}
```

### Tìm giá trị nhỏ nhất

```cpp
int mn = a[0];
for (int x : a) {
    mn = min(mn, x);
}
```

> Nếu dữ liệu có thể rỗng, không được truy cập `a[0]` trước khi kiểm tra kích thước. Có thể khởi tạo `mx`, `mn` theo giới hạn bài toán.

---

## 9. MẢNG, `VECTOR` VÀ `STRING`

### Mảng và chỉ số

```text
a[0], a[1], a[2], .., a[n - 1]
```

> **Chỉ số bắt đầu từ 0.** Với `n` phần tử, chỉ số hợp lệ là `0 … n-1`.

### Đọc và duyệt mảng

```cpp
int n;
cin >> n;

vector<int> a(n);
for (int i = 0; i < n; i++) {
    cin >> a[i];
}

for (int i = 0; i < n; i++) {
    cout << a[i] << ' ';
}
```

### Duyệt bằng phần tử

```cpp
for (int x : a) {
    cout << x << ' ';
}
```

Dùng chỉ số `i` khi cần biết vị trí hoặc cập nhật `a[i]`. Dùng `x` khi chỉ cần đọc từng giá trị.

### Các thao tác `vector` cơ bản

| Lệnh | Ý nghĩa |
|---|---|
| `vector<int> a(n)` | Tạo vector có `n` phần tử |
| `a.size()` | Số phần tử |
| `a.push_back(x)` | Thêm `x` vào cuối |
| `a.pop_back()` | Xóa phần tử cuối |
| `a[i]` | Truy cập phần tử vị trí `i` |
| `a.empty()` | Kiểm tra có rỗng không |

### Xử lý `string`

```cpp
string s;
cin >> s;

for (int i = 0; i < (int)s.size(); i++) {
    if (s[i] == 'A') {
        // xử lý ký tự A
    }
}
```

| Biểu thức | Ý nghĩa |
|---|---|
| `s.size()` | Độ dài xâu |
| `s[i]` | Ký tự ở vị trí `i` |
| `s.front()` | Ký tự đầu |
| `s.back()` | Ký tự cuối |
|

---

## 10. HÀM — CHIA BÀI TOÁN THÀNH CÁC PHẦN

> **Hàm là một khối công việc riêng:** nhận dữ liệu vào, thực hiện một nhiệm vụ và có thể trả về kết quả.

```cpp
int square(int x) {
    return x * x;
}
```

```cpp
int result = square(5); // result = 25
```

### Mẫu hàm

```cpp
return_type function_name(parameters) {
    // xử lý
    return value;
}
```

Nếu hàm không trả về kết quả, dùng `void`:

```cpp
void printLine(int n) {
    for (int i = 0; i < n; i++) cout << '-';
    cout << '\n';
}
```

Hàm nên thực hiện **một nhiệm vụ rõ ràng**. Các tên hàm thường gặp trong bài thuật toán là `check()`, `isPrime()`, `gcd()`, `solve()` và `dfs()`.

---

## 11. GỠ LỖI VÀ KIỂM THỬ

Khi chương trình sai, không đoán bừa. Hãy kiểm tra theo thứ tự:

| Câu hỏi | Việc cần làm |
|---|---|
| Input có đúng không? | Đọc lại định dạng và số lượng dữ liệu |
| Kiểu dữ liệu có đủ lớn không? | Kiểm tra `int`, `long long`, phép nhân và tổng |
| Công thức có đúng không? | Tính thủ công bằng một ví dụ nhỏ |
| Điều kiện có đúng không? | Thử trường hợp bằng biên, nhỏ hơn và lớn hơn biên |
| Vòng lặp có chạy đủ không? | Theo dõi giá trị bắt đầu, kết thúc và bước nhảy |
| Chỉ số có hợp lệ không? | Kiểm tra `0 ≤ i < n` |
| Kết quả trung gian có đúng không? | In biến tạm tại vị trí cần kiểm tra |

### In giá trị trung gian

```cpp
cerr << "i = " << i << ", sum = " << sum << '\n';
```

Có thể dùng `cout` ở bài đơn giản, nhưng phải xóa các dòng debug trước khi nộp nếu output yêu cầu chính xác.

### Bộ test tối thiểu

Mỗi bài nên thử:

1. Ví dụ mẫu.
2. Dữ liệu nhỏ nhất.
3. Dữ liệu lớn nhất hoặc gần lớn nhất.
4. Trường hợp đúng bằng ngưỡng.
5. Trường hợp không có phần tử thỏa điều kiện.
6. Trường hợp tất cả phần tử đều thỏa điều kiện.
7. Trường hợp có nhiều phần tử bằng nhau.

---

## 12. ĐỘ PHỨC TẠP — CHƯƠNG TRÌNH CÓ ĐỦ NHANH?

| Độ phức tạp | Trực giác |
|---|---|
| `O(1)` | Số thao tác gần như không phụ thuộc kích thước dữ liệu |
| `O(log N)` | Mỗi bước thu nhỏ đáng kể phạm vi tìm kiếm |
| `O(N)` | Duyệt dữ liệu một lần |
| `O(N log N)` | Thường gặp khi sắp xếp |
| `O(N²)` | Xét mọi cặp hoặc hai vòng lặp theo `N` |
| `O(2^N)` | Thử mọi tập con; chỉ phù hợp với `N` nhỏ |

### Quy tắc đọc giới hạn

| Nếu `N` khoảng… | Có thể cân nhắc… |
|---:|---|
| `N ≤ 20` | Duyệt tập con, bitmask, quay lui |
| `N ≤ 10^3` | Một số lời giải `O(N²)` |
| `N ≤ 10^5` hoặc `2 × 10^5` | `O(N)`, `O(N log N)` |
| `N` rất lớn | Công thức, toán học hoặc tối ưu mạnh hơn |

Đây chỉ là quy tắc định hướng. Cần xét thêm số test, hằng số trong chương trình và giới hạn thời gian.

---

## TÓM TẮT MỘT TRANG

```text
BIẾN
  Tôi cần lưu dữ liệu gì?

TÍNH
  Tôi cần công thức nào?

ĐIỀU KIỆN
  Tôi cần quyết định điều gì?

LẶP
  Tôi cần làm việc gì nhiều lần?

TÍCH LŨY
  Tôi cần cộng, đếm, max hay min?

MẢNG
  Tôi có nhiều dữ liệu cùng loại không?

HÀM
  Tôi có thể tách nhiệm vụ nào thành một khối công việc riêng?

DEBUG
  Input, biến, công thức, điều kiện, vòng lặp và kết quả trung gian có đúng không?
```

> **Mục tiêu của C++ Cơ bản:** Không phải nhớ thật nhiều câu lệnh, mà là nhìn một bài toán đơn giản và biết biến nó thành các bước có thể lập trình được.



\newpage

# Phụ lục B: Bài giải

> Phần này chứa lời giải tham khảo (code C++) cho toàn bộ bài tập trong sách. Hãy tự cố gắng giải bài ít nhất 30 phút trước khi xem bài giải.

## Chương 01 — Bài 01: Sắp xếp

### `CPPB-SX-01` — Xep Hang Diem Danh

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end());

    for (int i = 0; i < n; ++i) {
        cout << a[i] << (i == n - 1 ? "" : " ");
    }
    cout << "\n";
    return 0;
}

```

### `CPPB-SX-02` — Khoang Cach Nho Nhat

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end());

    long long ans = a[1] - a[0];
    for (int i = 1; i < n - 1; ++i) {
        ans = min(ans, a[i + 1] - a[i]);
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB-SX-03` — Tri Tuyet Doi

```cpp
#include <bits/stdc++.h>
using namespace std;

bool cmp(long long u, long long v) {
    if (abs(u) != abs(v)) return abs(u) < abs(v);
    return u < v;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end(), cmp);

    for (int i = 0; i < n; ++i) {
        cout << a[i] << (i == n - 1 ? "" : " ");
    }
    cout << "\n";
    return 0;
}

```

### `CPPB-SX-04` — Dem Gia Tri Phan Biet

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end());

    int cnt = 1;
    for (int i = 1; i < n; ++i) {
        if (a[i] != a[i - 1]) ++cnt;
    }

    cout << cnt << "\n";
    return 0;
}

```

### `CPPB-SX-05` — Hai Tram Kiem Soat

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> x(n);
    for (int i = 0; i < n; ++i) cin >> x[i];

    sort(x.begin(), x.end());

    long long min_dist = x[1] - x[0];
    for (int i = 1; i < n - 1; ++i) {
        min_dist = min(min_dist, x[i + 1] - x[i]);
    }

    cout << min_dist << "\n";
    return 0;
}

```

### `CPPB-SX-06` — Khoang Trong Lon Nhat

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end());

    long long max_gap = 0;
    for (int i = 0; i < n - 1; ++i) {
        max_gap = max(max_gap, a[i + 1] - a[i]);
    }

    cout << max_gap << "\n";
    return 0;
}

```

### `CPPB-SX-07` — Sap Xep Tong Chu So

```cpp
#include <bits/stdc++.h>
using namespace std;

long long sum_digits(long long x) {
    long long s = 0;
    while (x > 0) {
        s += x % 10;
        x /= 10;
    }
    return s;
}

bool cmp(long long a, long long b) {
    long long sa = sum_digits(a);
    long long sb = sum_digits(b);
    if (sa != sb) return sa < sb;
    return a < b;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end(), cmp);

    for (int i = 0; i < n; ++i) {
        cout << a[i] << (i == n - 1 ? "" : " ");
    }
    cout << "\n";
    return 0;
}

```

### `CPPB-SX-08` — Gom Cum Chenh Lech K

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end());

    int groups = 1;
    long long min_val = a[0];

    for (int i = 1; i < n; ++i) {
        if (a[i] - min_val > k) {
            ++groups;
            min_val = a[i];
        }
    }

    cout << groups << "\n";
    return 0;
}

```

### `CPPB-SX-09` — Phan Tu Xuat Hien Nhieu Nhat

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end());

    long long best_val = a[0];
    int max_freq = 1;

    long long cur_val = a[0];
    int cur_freq = 1;

    for (int i = 1; i < n; ++i) {
        if (a[i] == cur_val) {
            ++cur_freq;
        } else {
            if (cur_freq > max_freq) {
                max_freq = cur_freq;
                best_val = cur_val;
            }
            cur_val = a[i];
            cur_freq = 1;
        }
    }
    if (cur_freq > max_freq) {
        max_freq = cur_freq;
        best_val = cur_val;
    }

    cout << best_val << " " << max_freq << "\n";
    return 0;
}

```

### `CPPB-SX-10` — Sap Xep Luu Vi Tri

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<long long>> a(n, vector<long long>(2));
    for (int i = 0; i < n; ++i) {
        cin >> a[i][0];
        a[i][1] = i + 1;
    }

    sort(a.begin(), a.end());

    for (int i = 0; i < n; ++i) {
        cout << a[i][0] << " " << a[i][1] << "\n";
    }
    return 0;
}

```

### `CPPB-SX-11` — Ghep So Lon Nhat

```cpp
#include <bits/stdc++.h>
using namespace std;

bool cmp(const string &a, const string &b) {
    return a + b > b + a;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<string> s(n);
    for (int i = 0; i < n; ++i) cin >> s[i];

    sort(s.begin(), s.end(), cmp);

    if (s[0] == "0") {
        cout << 0 << "\n";
        return 0;
    }

    for (int i = 0; i < n; ++i) {
        cout << s[i];
    }
    cout << "\n";
    return 0;
}

```

### `CPPB-SX-12` — Bang Diem Hoc Sinh

```cpp
#include <bits/stdc++.h>
using namespace std;

bool cmp(const vector<long long> &a, const vector<long long> &b) {
    long long total_a = a[1] + a[2];
    long long total_b = b[1] + b[2];
    if (total_a != total_b) return total_a > total_b;
    if (a[2] != b[2]) return a[2] > b[2];
    return a[0] < b[0];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<long long>> a(n, vector<long long>(3));
    for (int i = 0; i < n; ++i) {
        cin >> a[i][0] >> a[i][1] >> a[i][2];
    }

    sort(a.begin(), a.end(), cmp);

    for (int i = 0; i < n; ++i) {
        cout << a[i][0] << " " << a[i][1] << " " << a[i][2] << "\n";
    }
    return 0;
}

```

### `CPPB-SX-13` — Bang Xep Hang The Thao

```cpp
#include <bits/stdc++.h>
using namespace std;

bool cmp(const vector<long long> &a, const vector<long long> &b) {
    if (a[1] != b[1]) return a[1] > b[1];
    if (a[2] != b[2]) return a[2] > b[2];
    if (a[3] != b[3]) return a[3] > b[3];
    return a[0] < b[0];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<long long>> a(n, vector<long long>(4));
    for (int i = 0; i < n; ++i) {
        cin >> a[i][0] >> a[i][1] >> a[i][2] >> a[i][3];
    }

    sort(a.begin(), a.end(), cmp);

    for (int i = 0; i < n; ++i) {
        cout << a[i][0] << (i == n - 1 ? "" : " ");
    }
    cout << "\n";
    return 0;
}

```

### `CPPB-SX-14` — Khac Phuc Strict Weak Ordering

```cpp
#include <bits/stdc++.h>
using namespace std;

bool cmp(const vector<long long> &a, const vector<long long> &b) {
    if (a[0] != b[0]) return a[0] < b[0];
    return a[1] > b[1];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<long long>> a(n, vector<long long>(2));
    for (int i = 0; i < n; ++i) {
        cin >> a[i][0] >> a[i][1];
    }

    stable_sort(a.begin(), a.end(), cmp);

    for (int i = 0; i < n; ++i) {
        cout << a[i][0] << " " << a[i][1] << "\n";
    }
    return 0;
}

```

## Chương 01 — Bài 02: Hai con trỏ

### `CPPB-HCT-01` — Mo Phong Hai Con Tro

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long s;
    if (!(cin >> n >> s)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    int l = 0, r = n - 1;
    bool found = false;

    while (l < r) {
        long long sum = a[l] + a[r];
        if (sum == s) {
            found = true;
            break;
        } else if (sum < s) {
            ++l;
        } else {
            --r;
        }
    }

    if (found) cout << "YES\n";
    else cout << "NO\n";
    return 0;
}

```

### `CPPB-HCT-02` — Tong Hai So

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long s;
    if (!(cin >> n >> s)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end());

    int l = 0, r = n - 1;
    bool found = false;

    while (l < r) {
        long long sum = a[l] + a[r];
        if (sum == s) {
            cout << a[l] << " " << a[r] << "\n";
            found = true;
            break;
        } else if (sum < s) {
            ++l;
        } else {
            --r;
        }
    }

    if (!found) cout << -1 << "\n";
    return 0;
}

```

### `CPPB-HCT-03` — Dem Cap Tong Be Hon S

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long s;
    if (!(cin >> n >> s)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end());

    int l = 0, r = n - 1;
    long long count = 0;

    while (l < r) {
        if (a[l] + a[r] <= s) {
            count += (r - l);
            ++l;
        } else {
            --r;
        }
    }

    cout << count << "\n";
    return 0;
}

```

### `CPPB-HCT-04` — Dem Cap Tong Lon Hon S

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long s;
    if (!(cin >> n >> s)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end());

    int l = 0, r = n - 1;
    long long count = 0;

    while (l < r) {
        if (a[l] + a[r] >= s) {
            count += (r - l);
            --r;
        } else {
            ++l;
        }
    }

    cout << count << "\n";
    return 0;
}

```

### `CPPB-HCT-05` — Thuyen Cuu Ho

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long c;
    if (!(cin >> n >> c)) return 0;

    vector<long long> w(n);
    for (int i = 0; i < n; ++i) cin >> w[i];

    sort(w.begin(), w.end());

    int l = 0, r = n - 1;
    int boats = 0;

    while (l <= r) {
        if (l == r) {
            ++boats;
            break;
        }
        if (w[l] + w[r] <= c) {
            ++l;
            --r;
        } else {
            --r;
        }
        ++boats;
    }

    cout << boats << "\n";
    return 0;
}

```

### `CPPB-HCT-06` — Van Chuyen Hang Hoa

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long c;
    if (!(cin >> n >> c)) return 0;

    vector<long long> w(n);
    for (int i = 0; i < n; ++i) cin >> w[i];

    sort(w.begin(), w.end());

    int l = 0, r = n - 1;
    int trips = 0;

    while (l <= r) {
        if (l == r) {
            ++trips;
            break;
        }
        if (w[l] + w[r] <= c) {
            ++l;
            --r;
        } else {
            --r;
        }
        ++trips;
    }

    cout << trips << "\n";
    return 0;
}

```

### `CPPB-HCT-07` — Tong Gan S Nhat

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long s;
    if (!(cin >> n >> s)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end());

    int l = 0, r = n - 1;
    long long best_diff = -1;
    long long ans_l = a[0], ans_r = a[1];

    while (l < r) {
        long long cur_sum = a[l] + a[r];
        long long cur_diff = abs(cur_sum - s);

        if (best_diff == -1 || cur_diff < best_diff || (cur_diff == best_diff && cur_sum < ans_l + ans_r)) {
            best_diff = cur_diff;
            ans_l = a[l];
            ans_r = a[r];
        }

        if (cur_sum == s) break;
        else if (cur_sum < s) ++l;
        else --r;
    }

    cout << ans_l << " " << ans_r << "\n";
    return 0;
}

```

### `CPPB-HCT-08` — Hieu Hai So Bang K

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end());

    int l = 0, r = 1;
    bool found = false;

    while (r < n) {
        if (l == r) {
            ++r;
            continue;
        }
        long long diff = a[r] - a[l];
        if (diff == k) {
            found = true;
            break;
        } else if (diff < k) {
            ++r;
        } else {
            ++l;
        }
    }

    if (found) cout << "YES\n";
    else cout << "NO\n";
    return 0;
}

```

### `CPPB-HCT-09` — Bo Ba Tong Bang S

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long s;
    if (!(cin >> n >> s)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end());

    for (int i = 0; i < n - 2; ++i) {
        long long target = s - a[i];
        int l = i + 1, r = n - 1;
        while (l < r) {
            long long sum = a[l] + a[r];
            if (sum == target) {
                cout << a[i] << " " << a[l] << " " << a[r] << "\n";
                return 0;
            } else if (sum < target) {
                ++l;
            } else {
                --r;
            }
        }
    }

    cout << -1 << "\n";
    return 0;
}

```

### `CPPB-HCT-10` — Dem So Tam Giac

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end());

    long long count = 0;

    for (int k = n - 1; k >= 2; --k) {
        int l = 0, r = k - 1;
        while (l < r) {
            if (a[l] + a[r] > a[k]) {
                count += (r - l);
                --r;
            } else {
                ++l;
            }
        }
    }

    cout << count << "\n";
    return 0;
}

```

### `CPPB-HCT-11` — Dem Cap Trung Lap

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long s;
    if (!(cin >> n >> s)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end());

    int l = 0, r = n - 1;
    long long ans = 0;

    while (l < r) {
        long long sum = a[l] + a[r];
        if (sum == s) {
            if (a[l] == a[r]) {
                long long cnt = r - l + 1;
                ans += cnt * (cnt - 1) / 2;
                break;
            } else {
                long long c1 = 1, c2 = 1;
                while (l + 1 < r && a[l + 1] == a[l]) { ++c1; ++l; }
                while (r - 1 > l && a[r - 1] == a[r]) { ++c2; --r; }
                ans += c1 * c2;
                ++l;
                --r;
            }
        } else if (sum < s) {
            ++l;
        } else {
            --r;
        }
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB-HCT-12` — Ghep Tre Em Banh Quy

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> g(n), s(m);
    for (int i = 0; i < n; ++i) cin >> g[i];
    for (int i = 0; i < m; ++i) cin >> s[i];

    sort(g.begin(), g.end());
    sort(s.begin(), s.end());

    int i = 0, j = 0;
    int satisfied = 0;

    while (i < n && j < m) {
        if (s[j] >= g[i]) {
            ++satisfied;
            ++i;
            ++j;
        } else {
            ++j;
        }
    }

    cout << satisfied << "\n";
    return 0;
}

```

### `CPPB-HCT-13` — Bo Bon Tong Bang S

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long s;
    if (!(cin >> n >> s)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end());

    for (int i = 0; i < n - 3; ++i) {
        for (int j = i + 1; j < n - 2; ++j) {
            long long target = s - a[i] - a[j];
            int l = j + 1, r = n - 1;
            while (l < r) {
                long long sum = a[l] + a[r];
                if (sum == target) {
                    cout << a[i] << " " << a[j] << " " << a[l] << " " << a[r] << "\n";
                    return 0;
                } else if (sum < target) {
                    ++l;
                } else {
                    --r;
                }
            }
        }
    }

    cout << -1 << "\n";
    return 0;
}

```

### `CPPB-HCT-14` — Hai Con Tro Cuc Han

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> a(n), b(m);
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int i = 0; i < m; ++i) cin >> b[i];

    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    int i = 0, j = 0;
    long long min_diff = abs(a[0] - b[0]);

    while (i < n && j < m) {
        min_diff = min(min_diff, abs(a[i] - b[j]));
        if (a[i] == b[j]) break;
        else if (a[i] < b[j]) ++i;
        else ++j;
    }

    cout << min_diff << "\n";
    return 0;
}

```

## Chương 01 — Bài 03: Cửa sổ trượt

### `CPPB-CST-01` — Cua So K

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long cur_sum = 0;
    for (int i = 0; i < k; ++i) cur_sum += a[i];

    long long max_sum = cur_sum;
    for (int i = k; i < n; ++i) {
        cur_sum += a[i] - a[i - k];
        max_sum = max(max_sum, cur_sum);
    }

    cout << max_sum << "\n";
    return 0;
}

```

### `CPPB-CST-02` — Trung Binh K Lon Nhat

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long cur_sum = 0;
    for (int i = 0; i < k; ++i) cur_sum += a[i];

    long long max_sum = cur_sum;
    for (int i = k; i < n; ++i) {
        cur_sum += a[i] - a[i - k];
        max_sum = max(max_sum, cur_sum);
    }

    double ans = (double)max_sum / k;
    cout << fixed << setprecision(3) << ans << "\n";
    return 0;
}

```

### `CPPB-CST-03` — Doan Con Ngan Nhat Tong S

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long s;
    if (!(cin >> n >> s)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    int l = 0;
    long long cur_sum = 0;
    int min_len = n + 1;

    for (int r = 0; r < n; ++r) {
        cur_sum += a[r];
        while (cur_sum >= s) {
            min_len = min(min_len, r - l + 1);
            cur_sum -= a[l];
            ++l;
        }
    }

    if (min_len > n) cout << -1 << "\n";
    else cout << min_len << "\n";
    return 0;
}

```

### `CPPB-CST-04` — Doan Con Dai Nhat Tong S

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long s;
    if (!(cin >> n >> s)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    int l = 0;
    long long cur_sum = 0;
    int max_len = 0;

    for (int r = 0; r < n; ++r) {
        cur_sum += a[r];
        while (cur_sum > s) {
            cur_sum -= a[l];
            ++l;
        }
        max_len = max(max_len, r - l + 1);
    }

    cout << max_len << "\n";
    return 0;
}

```

### `CPPB-CST-05` — Lat Bit K So Khong

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    int l = 0;
    int zero_cnt = 0;
    int max_len = 0;

    for (int r = 0; r < n; ++r) {
        if (a[r] == 0) ++zero_cnt;

        while (zero_cnt > k) {
            if (a[l] == 0) --zero_cnt;
            ++l;
        }

        max_len = max(max_len, r - l + 1);
    }

    cout << max_len << "\n";
    return 0;
}

```

### `CPPB-CST-06` — Camera Giao Thong

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    int cur_broken = 0;
    for (int i = 0; i < k; ++i) {
        if (a[i] == 0) ++cur_broken;
    }

    int min_broken = cur_broken;
    for (int i = k; i < n; ++i) {
        if (a[i] == 0) ++cur_broken;
        if (a[i - k] == 0) --cur_broken;
        min_broken = min(min_broken, cur_broken);
    }

    cout << min_broken << "\n";
    return 0;
}

```

### `CPPB-CST-07` — Min Max Cua So K

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    for (int i = 0; i <= n - k; ++i) {
        long long cur_min = a[i];
        for (int j = i + 1; j < i + k; ++j) {
            cur_min = min(cur_min, a[j]);
        }
        cout << cur_min << (i == n - k ? "" : " ");
    }
    cout << "\n";
    return 0;
}

```

### `CPPB-CST-08` — Dem Doan Con Tong Be Hon S

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long s;
    if (!(cin >> n >> s)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    int l = 0;
    long long cur_sum = 0;
    long long count = 0;

    for (int r = 0; r < n; ++r) {
        cur_sum += a[r];
        while (cur_sum > s) {
            cur_sum -= a[l];
            ++l;
        }
        count += (r - l + 1);
    }

    cout << count << "\n";
    return 0;
}

```

### `CPPB-CST-09` — Dem Doan Con Tong Bang S

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long s;
    if (!(cin >> n >> s)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    int l = 0;
    long long cur_sum = 0;
    long long count = 0;

    for (int r = 0; r < n; ++r) {
        cur_sum += a[r];
        while (cur_sum > s) {
            cur_sum -= a[l];
            ++l;
        }
        if (cur_sum == s) {
            ++count;
        }
    }

    cout << count << "\n";
    return 0;
}

```

### `CPPB-CST-10` — Doan Con K Ky Tu Khac Nhau

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    string s;
    cin >> s;

    vector<int> freq(26, 0);
    int distinct = 0;
    int l = 0, max_len = 0;

    for (int r = 0; r < n; ++r) {
        int c = s[r] - 'a';
        if (freq[c] == 0) ++distinct;
        ++freq[c];

        while (distinct > k) {
            int lc = s[l] - 'a';
            --freq[lc];
            if (freq[lc] == 0) --distinct;
            ++l;
        }

        max_len = max(max_len, r - l + 1);
    }

    cout << max_len << "\n";
    return 0;
}

```

### `CPPB-CST-11` — Doan Con Ngan Nhat Chua Du Ky Tu

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    string s, t;
    cin >> s >> t;

    vector<int> need(26, 0);
    for (char c : t) need[c - 'a'] = 1;

    vector<int> have(26, 0);
    int matched = 0;
    int l = 0, min_len = n + 1;

    for (int r = 0; r < n; ++r) {
        int c = s[r] - 'a';
        if (need[c]) {
            if (have[c] == 0) ++matched;
            ++have[c];
        }

        while (matched == m) {
            min_len = min(min_len, r - l + 1);
            int lc = s[l] - 'a';
            if (need[lc]) {
                --have[lc];
                if (have[lc] == 0) --matched;
            }
            ++l;
        }
    }

    if (min_len > n) cout << -1 << "\n";
    else cout << min_len << "\n";
    return 0;
}

```

### `CPPB-CST-12` — Phu Song Wifi

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long r;
    if (!(cin >> n >> r)) return 0;

    vector<long long> x(n);
    for (int i = 0; i < n; ++i) cin >> x[i];

    int i = 0;
    int count = 0;

    while (i < n) {
        ++count;
        long long loc = x[i];
        while (i < n && x[i] - loc <= r) ++i;
        long long tower = x[i - 1];
        while (i < n && x[i] - tower <= r) ++i;
    }

    cout << count << "\n";
    return 0;
}

```

### `CPPB-CST-13` — Doan Con Chenh Lech K

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    int max_len = 0;

    for (int l = 0; l < n; ++l) {
        long long cur_min = a[l], cur_max = a[l];
        for (int r = l; r < n; ++r) {
            cur_min = min(cur_min, a[r]);
            cur_max = max(cur_max, a[r]);
            if (cur_max - cur_min <= k) {
                max_len = max(max_len, r - l + 1);
            } else {
                break;
            }
        }
    }

    cout << max_len << "\n";
    return 0;
}

```

### `CPPB-CST-14` — Cua So Truot Cuc Han

```cpp
#include <bits/stdc++.h>
using namespace std;

long long count_at_most(const vector<long long> &x, long long limit) {
    if (limit <= 0) return 0;
    int n = x.size();
    int l = 0;
    long long cur_sum = 0;
    long long count = 0;

    for (int r = 0; r < n; ++r) {
        cur_sum += x[r];
        while (cur_sum > limit) {
            cur_sum -= x[l];
            ++l;
        }
        count += (r - l + 1);
    }
    return count;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long a, b;
    if (!(cin >> n >> a >> b)) return 0;

    vector<long long> x(n);
    for (int i = 0; i < n; ++i) cin >> x[i];

    long long ans = count_at_most(x, b) - count_at_most(x, a - 1);
    cout << ans << "\n";
    return 0;
}

```

## Chương 02 — Bài 04: Mảng tiền tố

### `CPPB-PT-01` — Truy Van Tong Doan Con

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<long long> p(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        long long x;
        cin >> x;
        p[i] = p[i - 1] + x;
    }

    while (q--) {
        int l, r;
        cin >> l >> r;
        cout << p[r] - p[l - 1] << "\n";
    }

    return 0;
}

```

### `CPPB-PT-02` — Dem So Chan Trong Doan

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<int> p(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        long long x;
        cin >> x;
        p[i] = p[i - 1] + (abs(x) % 2 == 0 ? 1 : 0);
    }

    while (q--) {
        int l, r;
        cin >> l >> r;
        cout << p[r] - p[l - 1] << "\n";
    }

    return 0;
}

```

### `CPPB-PT-03` — Vi Tri Can Bang

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n + 1);
    vector<long long> p(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
        p[i] = p[i - 1] + a[i];
    }

    for (int i = 1; i <= n; ++i) {
        long long left_sum = p[i - 1];
        long long right_sum = p[n] - p[i];
        if (left_sum == right_sum) {
            cout << i << "\n";
            return 0;
        }
    }

    cout << -1 << "\n";
    return 0;
}

```

### `CPPB-PT-04` — Doan Con Tong Bang Khong

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> p(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        long long x;
        cin >> x;
        p[i] = p[i - 1] + x;
    }

    sort(p.begin(), p.end());

    for (int i = 1; i <= n; ++i) {
        if (p[i] == p[i - 1]) {
            cout << "YES\n";
            return 0;
        }
    }

    cout << "NO\n";
    return 0;
}

```

### `CPPB-PT-05` — Cap Nhat Cong Doan

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<long long> d(n + 2, 0);

    while (q--) {
        int l, r;
        long long v;
        cin >> l >> r >> v;
        d[l] += v;
        d[r + 1] -= v;
    }

    long long current = 0;
    for (int i = 1; i <= n; ++i) {
        current += d[i];
        cout << current << (i == n ? "" : " ");
    }
    cout << "\n";

    return 0;
}

```

### `CPPB-PT-06` — Trong Cay Phu Doan

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q, k;
    if (!(cin >> n >> q >> k)) return 0;

    vector<int> d(n + 2, 0);
    while (q--) {
        int l, r;
        cin >> l >> r;
        d[l]++;
        d[r + 1]--;
    }

    int count_ge_k = 0;
    int current = 0;
    for (int i = 1; i <= n; ++i) {
        current += d[i];
        if (current >= k) {
            count_ge_k++;
        }
    }

    cout << count_ge_k << "\n";
    return 0;
}

```

### `CPPB-PT-07` — Truy Van Hinh Chu Nhat 2d

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, q;
    if (!(cin >> n >> m >> q)) return 0;

    vector<vector<long long>> p(n + 1, vector<long long>(m + 1, 0));
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            long long val;
            cin >> val;
            p[i][j] = p[i - 1][j] + p[i][j - 1] - p[i - 1][j - 1] + val;
        }
    }

    while (q--) {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        long long ans = p[x2][y2] - p[x1 - 1][y2] - p[x2][y1 - 1] + p[x1 - 1][y1 - 1];
        cout << ans << "\n";
    }

    return 0;
}

```

### `CPPB-PT-08` — Hinh Vuong K Tong Lon Nhat

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, k;
    if (!(cin >> n >> m >> k)) return 0;

    vector<vector<long long>> p(n + 1, vector<long long>(m + 1, 0));
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            long long val;
            cin >> val;
            p[i][j] = p[i - 1][j] + p[i][j - 1] - p[i - 1][j - 1] + val;
        }
    }

    long long max_sum = -4e18; // Khởi tạo âm vô cùng
    for (int i = k; i <= n; ++i) {
        for (int j = k; j <= m; ++j) {
            long long current = p[i][j] - p[i - k][j] - p[i][j - k] + p[i - k][j - k];
            max_sum = max(max_sum, current);
        }
    }

    cout << max_sum << "\n";
    return 0;
}

```

### `CPPB-PT-09` — Mang Hieu 2d

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, q;
    if (!(cin >> n >> m >> q)) return 0;

    vector<vector<long long>> d(n + 2, vector<long long>(m + 2, 0));

    while (q--) {
        int x1, y1, x2, y2;
        long long v;
        cin >> x1 >> y1 >> x2 >> y2 >> v;
        d[x1][y1] += v;
        d[x1][y2 + 1] -= v;
        d[x2 + 1][y1] -= v;
        d[x2 + 1][y2 + 1] += v;
    }

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            d[i][j] = d[i - 1][j] + d[i][j - 1] - d[i - 1][j - 1] + d[i][j];
            cout << d[i][j] << (j == m ? "" : " ");
        }
        cout << "\n";
    }

    return 0;
}

```

### `CPPB-PT-10` — Tong Chia Het Cho K

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> cnt(k, 0);
    cnt[0] = 1; // P[0] = 0

    long long current_sum = 0;
    for (int i = 1; i <= n; ++i) {
        long long x;
        cin >> x;
        current_sum += x;
        long long rem = (current_sum % k + k) % k;
        cnt[rem]++;
    }

    long long total_pairs = 0;
    for (int r = 0; r < k; ++r) {
        total_pairs += cnt[r] * (cnt[r] - 1) / 2;
    }

    cout << total_pairs << "\n";
    return 0;
}

```

### `CPPB-PT-11` — Mang Tien To Xor

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<long long> p(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        long long x;
        cin >> x;
        p[i] = p[i - 1] ^ x;
    }

    while (q--) {
        int l, r;
        cin >> l >> r;
        cout << (p[r] ^ p[l - 1]) << "\n";
    }

    return 0;
}

```

### `CPPB-PT-12` — Can Bang Khong Va Mot

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    // Tiền tố có thể chạy từ -N đến +N, offset = n
    vector<int> first_pos(2 * n + 1, -2);
    first_pos[0 + n] = 0; // P[0] = 0 tại vị trí 0

    int current_sum = 0;
    int max_len = 0;

    for (int i = 1; i <= n; ++i) {
        int x;
        cin >> x;
        current_sum += (x == 1 ? 1 : -1);

        int idx = current_sum + n;
        if (first_pos[idx] != -2) {
            max_len = max(max_len, i - first_pos[idx]);
        } else {
            first_pos[idx] = i;
        }
    }

    cout << max_len << "\n";
    return 0;
}

```

### `CPPB-PT-13` — Ma Tran Da Vung

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, q;
    if (!(cin >> n >> m >> q)) return 0;

    vector<vector<long long>> p(n + 1, vector<long long>(m + 1, 0));
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            long long val;
            cin >> val;
            p[i][j] = p[i - 1][j] + p[i][j - 1] - p[i - 1][j - 1] + val;
        }
    }

    auto query = [&](int x1, int y1, int x2, int y2) -> long long {
        return p[x2][y2] - p[x1 - 1][y2] - p[x2][y1 - 1] + p[x1 - 1][y1 - 1];
    };

    while (q--) {
        int x1, y1, x2, y2, u1, v1, u2, v2;
        cin >> x1 >> y1 >> x2 >> y2 >> u1 >> v1 >> u2 >> v2;
        cout << query(x1, y1, x2, y2) + query(u1, v1, u2, v2) << "\n";
    }

    return 0;
}

```

### `CPPB-PT-14` — Phan Phoi Tai Nguyen

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<long long> d2(n + 3, 0);

    while (q--) {
        long long l, r, s, d;
        cin >> l >> r >> s >> d;
        d2[l] += s;
        d2[l + 1] += (d - s);
        d2[r + 1] -= (s + (r - l + 1) * d);
        d2[r + 2] += (s + (r - l) * d);
    }

    // Lần 1: Khôi phục mảng hiệu bậc 1
    vector<long long> d1(n + 2, 0);
    for (int i = 1; i <= n + 1; ++i) {
        d1[i] = d1[i - 1] + d2[i];
    }

    // Lần 2: Khôi phục mảng giá trị gốc
    vector<long long> a(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        a[i] = a[i - 1] + d1[i];
        cout << a[i] << (i == n ? "" : " ");
    }
    cout << "\n";

    return 0;
}

```

### `CPPB-PT-15` — Ma Tran Con Tong Lon Nhat

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<long long>> a(n + 1, vector<long long>(m + 1));
    vector<vector<long long>> p(n + 1, vector<long long>(m + 1, 0));

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            cin >> a[i][j];
            p[i][j] = p[i - 1][j] + a[i][j]; // Tiền tố theo cột
        }
    }

    long long max_sum = -4e18;

    for (int r1 = 1; r1 <= n; ++r1) {
        for (int r2 = r1; r2 <= n; ++r2) {
            long long current_kadane = 0;
            for (int c = 1; c <= m; ++c) {
                long long val = p[r2][c] - p[r1 - 1][c];
                current_kadane = max(val, current_kadane + val);
                max_sum = max(max_sum, current_kadane);
            }
        }
    }

    cout << max_sum << "\n";
    return 0;
}

```

### `CPPB-PT-16` — Can Bang Tien To Da Chieu

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    string s;
    if (!(cin >> n >> s)) return 0;

    int ca = 0, cb = 0, cc = 0;

    // Lưu: {diff1, diff2, index}
    vector<vector<int>> states;
    states.reserve(n + 1);
    states.push_back({0, 0, 0}); // Tại vị trí 0

    for (int i = 1; i <= n; ++i) {
        if (s[i - 1] == 'A') ca++;
        else if (s[i - 1] == 'B') cb++;
        else if (s[i - 1] == 'C') cc++;

        states.push_back({ca - cb, cb - cc, i});
    }

    sort(states.begin(), states.end(), [](const vector<int>& u, const vector<int>& v) {
        if (u[0] != v[0]) return u[0] < v[0];
        if (u[1] != v[1]) return u[1] < v[1];
        return u[2] < v[2];
    });

    int max_len = 0;
    int i = 0;
    while (i <= n) {
        int j = i;
        while (j <= n && states[j][0] == states[i][0] && states[j][1] == states[i][1]) {
            j++;
        }
        max_len = max(max_len, states[j - 1][2] - states[i][2]);
        i = j;
    }

    cout << max_len << "\n";
    return 0;
}

```

## Chương 02 — Bài 05: Tìm kiếm nhị phân

### `CPPB-BS-01` — Tim Kiem Tren Mang Sap Xep

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    while (q--) {
        long long x;
        cin >> x;
        if (binary_search(a.begin(), a.end(), x)) {
            cout << "YES\n";
        } else {
            cout << "NO\n";
        }
    }

    return 0;
}

```

### `CPPB-BS-02` — Vi Tri Dau Va Cuoi

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    while (q--) {
        long long x;
        cin >> x;
        auto it1 = lower_bound(a.begin(), a.end(), x);
        if (it1 == a.end() || *it1 != x) {
            cout << "-1 -1\n";
        } else {
            auto it2 = upper_bound(a.begin(), a.end(), x);
            int first_idx = it1 - a.begin() + 1;
            int last_idx = it2 - a.begin();
            cout << first_idx << " " << last_idx << "\n";
        }
    }

    return 0;
}

```

### `CPPB-BS-03` — Dem So Trong Khoang

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    sort(a.begin(), a.end());

    while (q--) {
        long long l, r;
        cin >> l >> r;
        auto it_l = lower_bound(a.begin(), a.end(), l);
        auto it_r = upper_bound(a.begin(), a.end(), r);
        cout << (it_r - it_l) << "\n";
    }

    return 0;
}

```

### `CPPB-BS-04` — Can Bac Hai So Lon

```cpp
#include <bits/stdc++.h>
using namespace std;

void solve() {
    long long n;
    cin >> n;
    long long low = 1, high = 1000000000LL, ans = 1;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (mid <= n / mid) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    cout << ans << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        solve();
    }
    return 0;
}

```

### `CPPB-BS-05` — Phan Tu Nho Nhat Lon Hon X

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    while (q--) {
        long long x;
        cin >> x;
        auto it = upper_bound(a.begin(), a.end(), x);
        if (it == a.end()) {
            cout << -1 << "\n";
        } else {
            cout << *it << "\n";
        }
    }

    return 0;
}

```

### `CPPB-BS-06` — Chia Keo Hoc Sinh

```cpp
#include <bits/stdc++.h>
using namespace std;

bool check(long long mid, const vector<long long>& a, long long k) {
    long long count = 0;
    for (long long x : a) {
        count += (x / mid);
    }
    return count >= k;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    long long max_val = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        max_val = max(max_val, a[i]);
    }

    long long low = 1, high = max_val, ans = 0;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (check(mid, a, k)) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB-BS-07` — Cat Go Xay Dung

```cpp
#include <bits/stdc++.h>
using namespace std;

bool check(long long h, const vector<long long>& a, long long m) {
    long long wood = 0;
    for (long long x : a) {
        if (x > h) {
            wood += (x - h);
        }
    }
    return wood >= m;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> a(n);
    long long max_val = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        max_val = max(max_val, a[i]);
    }

    long long low = 0, high = max_val, ans = 0;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (check(mid, a, m)) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB-BS-08` — Dat Tram Phat Song

```cpp
#include <bits/stdc++.h>
using namespace std;

bool check(long long d, const vector<long long>& x, int c) {
    int count = 1;
    long long last_pos = x[0];
    for (size_t i = 1; i < x.size(); ++i) {
        if (x[i] - last_pos >= d) {
            count++;
            last_pos = x[i];
        }
    }
    return count >= c;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, c;
    if (!(cin >> n >> c)) return 0;

    vector<long long> x(n);
    for (int i = 0; i < n; ++i) {
        cin >> x[i];
    }
    sort(x.begin(), x.end());

    long long low = 1, high = x[n - 1] - x[0], ans = 1;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (check(mid, x, c)) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB-BS-09` — Chia Mang Tong Max Nho Nhat

```cpp
#include <bits/stdc++.h>
using namespace std;

bool check(long long limit, const vector<long long>& a, int k) {
    int segments = 1;
    long long current_sum = 0;
    for (long long x : a) {
        if (current_sum + x > limit) {
            segments++;
            current_sum = x;
        } else {
            current_sum += x;
        }
    }
    return segments <= k;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    long long max_val = 0, total_sum = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        max_val = max(max_val, a[i]);
        total_sum += a[i];
    }

    long long low = max_val, high = total_sum, ans = total_sum;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (check(mid, a, k)) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB-BS-10` — Van Chuyen Hang Hoa

```cpp
#include <bits/stdc++.h>
using namespace std;

bool check(long long cap, const vector<long long>& w, int d) {
    int days = 1;
    long long current_weight = 0;
    for (long long x : w) {
        if (current_weight + x > cap) {
            days++;
            current_weight = x;
        } else {
            current_weight += x;
        }
    }
    return days <= d;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, d;
    if (!(cin >> n >> d)) return 0;

    vector<long long> w(n);
    long long max_w = 0, sum_w = 0;
    for (int i = 0; i < n; ++i) {
        cin >> w[i];
        max_w = max(max_w, w[i]);
        sum_w += w[i];
    }

    long long low = max_w, high = sum_w, ans = sum_w;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (check(mid, w, d)) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB-BS-11` — Nghiem Thuc Phuong Trinh

```cpp
#include <bits/stdc++.h>
using namespace std;

double f(double x) {
    return x * x * x + 2.0 * x * x + 10.0 * x;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    double c;
    if (!(cin >> c)) return 0;

    double low = 0.0, high = 1000.0;
    for (int iter = 0; iter < 100; ++iter) {
        double mid = low + (high - low) / 2.0;
        if (f(mid) >= c) {
            high = mid;
        } else {
            low = mid;
        }
    }

    cout << fixed << setprecision(6) << low << "\n";
    return 0;
}

```

### `CPPB-BS-12` — Phan Tu Thu K Hai Mang

```cpp
#include <bits/stdc++.h>
using namespace std;

long long count_le(long long x, const vector<long long>& a, const vector<long long>& b) {
    auto it1 = upper_bound(a.begin(), a.end(), x);
    auto it2 = upper_bound(b.begin(), b.end(), x);
    return (it1 - a.begin()) + (it2 - b.begin());
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    long long k;
    if (!(cin >> n >> m >> k)) return 0;

    vector<long long> a(n), b(m);
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int i = 0; i < m; ++i) cin >> b[i];

    long long low = -2e9, high = 2e9, ans = high;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (count_le(mid, a, b) >= k) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB-BS-13` — Trung Binh Lon Nhat Do Dai K

```cpp
#include <bits/stdc++.h>
using namespace std;

bool check(double mid, const vector<double>& a, int n, int k) {
    vector<double> p(n + 1, 0.0);
    for (int i = 1; i <= n; ++i) {
        p[i] = p[i - 1] + (a[i - 1] - mid);
    }

    double min_p = 0.0;
    for (int i = k; i <= n; ++i) {
        min_p = min(min_p, p[i - k]);
        if (p[i] - min_p >= -1e-9) {
            return true;
        }
    }
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<double> a(n);
    double max_val = 0.0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        max_val = max(max_val, a[i]);
    }

    double low = 0.0, high = max_val;
    for (int iter = 0; iter < 80; ++iter) {
        double mid = low + (high - low) / 2.0;
        if (check(mid, a, n, k)) {
            low = mid;
        } else {
            high = mid;
        }
    }

    cout << fixed << setprecision(4) << low << "\n";
    return 0;
}

```

### `CPPB-BS-14` — Tuyen Duong Van Tai

```cpp
#include <bits/stdc++.h>
using namespace std;

bool check(long long cap, const vector<long long>& a, int n, int m, int d) {
    int trucks = 0;
    int i = 0;
    while (i < n) {
        trucks++;
        if (trucks > m) return false;
        long long current_load = 0;
        int count_cities = 0;
        while (i < n && count_cities < d && current_load + a[i] <= cap) {
            current_load += a[i];
            count_cities++;
            i++;
        }
    }
    return trucks <= m;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, d;
    if (!(cin >> n >> m >> d)) return 0;

    vector<long long> a(n);
    long long max_val = 0, sum_val = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        max_val = max(max_val, a[i]);
        sum_val += a[i];
    }

    long long low = max_val, high = sum_val, ans = sum_val;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (check(mid, a, n, m, d)) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB-BS-15` — Tim Kiem Mang Xoay Vong

```cpp
#include <bits/stdc++.h>
using namespace std;

int search_rotated(const vector<long long>& a, long long target) {
    int low = 0, high = (int)a.size() - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (a[mid] == target) return mid + 1; // 1-based

        if (a[low] <= a[mid]) {
            // Nửa trái được sắp xếp
            if (a[low] <= target && target < a[mid]) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        } else {
            // Nửa phải được sắp xếp
            if (a[mid] < target && target <= a[high]) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
    }
    return -1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    while (q--) {
        long long x;
        cin >> x;
        cout << search_rotated(a, x) << "\n";
    }

    return 0;
}

```

### `CPPB-BS-16` — Tim Kiem Ma Tran 2d

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, q;
    if (!(cin >> n >> m >> q)) return 0;

    vector<vector<long long>> a(n, vector<long long>(m));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> a[i][j];
        }
    }

    while (q--) {
        long long target;
        cin >> target;

        int low = 0, high = n * m - 1;
        bool found = false;

        while (low <= high) {
            int mid = low + (high - low) / 2;
            int r = mid / m;
            int c = mid % m;

            if (a[r][c] == target) {
                found = true;
                break;
            } else if (a[r][c] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        cout << (found ? "YES\n" : "NO\n");
    }

    return 0;
}

```

### `CPPB-BS-17` — Tim Dinh Day Nui

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    int low = 0, high = n - 1;
    while (low < high) {
        int mid = low + (high - low) / 2;
        if (a[mid] < a[mid + 1]) {
            low = mid + 1;
        } else {
            high = mid;
        }
    }

    cout << (low + 1) << "\n"; // 1-based
    return 0;
}

```

### `CPPB-BS-18` — Trung Vi Hai Mang Sap Xep

```cpp
#include <bits/stdc++.h>
using namespace std;

double findMedianSortedArrays(vector<long long>& a, vector<long long>& b) {
    if (a.size() > b.size()) return findMedianSortedArrays(b, a);

    int n = (int)a.size();
    int m = (int)b.size();
    int low = 0, high = n;

    const long long INF = 2e18;

    while (low <= high) {
        int i = low + (high - low) / 2;
        int j = (n + m + 1) / 2 - i;

        long long maxLeftA = (i == 0) ? -INF : a[i - 1];
        long long minRightA = (i == n) ? INF : a[i];

        long long maxLeftB = (j == 0) ? -INF : b[j - 1];
        long long minRightB = (j == m) ? INF : b[j];

        if (maxLeftA <= minRightB && maxLeftB <= minRightA) {
            if ((n + m) % 2 == 1) {
                return (double)max(maxLeftA, maxLeftB);
            } else {
                return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2.0;
            }
        } else if (maxLeftA > minRightB) {
            high = i - 1;
        } else {
            low = i + 1;
        }
    }
    return 0.0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> a(n), b(m);
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int i = 0; i < m; ++i) cin >> b[i];

    double median = findMedianSortedArrays(a, b);
    cout << fixed << setprecision(1) << median << "\n";

    return 0;
}

```

## Chương 02 — Bài 06: Phép toán bit

### `CPPB-BIT-01` — Bat Tat Kiem Tra Bit

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    unsigned long long n;
    int q;
    if (!(cin >> n >> q)) return 0;

    while (q--) {
        int type, k;
        cin >> type >> k;
        if (type == 1) {
            n |= (1ULL << k);
        } else if (type == 2) {
            n &= ~(1ULL << k);
        } else if (type == 3) {
            cout << ((n >> k) & 1ULL) << "\n";
        }
    }

    return 0;
}

```

### `CPPB-BIT-02` — Dem So Bit Mot

```cpp
#include <bits/stdc++.h>
using namespace std;

void solve() {
    unsigned long long n;
    cin >> n;
    cout << __builtin_popcountll(n) << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        solve();
    }
    return 0;
}

```

### `CPPB-BIT-03` — Kiem Tra Luy Thua Cua Hai

```cpp
#include <bits/stdc++.h>
using namespace std;

void solve() {
    unsigned long long n;
    cin >> n;
    if (n > 0 && (n & (n - 1)) == 0) {
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        solve();
    }
    return 0;
}

```

### `CPPB-BIT-04` — Tim Phan Tu Don Le

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    int total_elements = 2 * n + 1;
    long long ans = 0;
    for (int i = 0; i < total_elements; ++i) {
        long long x;
        cin >> x;
        ans ^= x;
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB-BIT-05` — Tim Hai So Don Le

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    int total_elements = 2 * n + 2;
    vector<long long> a(total_elements);
    long long xor_sum = 0;
    for (int i = 0; i < total_elements; ++i) {
        cin >> a[i];
        xor_sum ^= a[i];
    }

    // Lấy bit 1 phân biệt
    long long diff_bit = xor_sum & (-xor_sum);

    long long num1 = 0, num2 = 0;
    for (long long val : a) {
        if (val & diff_bit) {
            num1 ^= val;
        } else {
            num2 ^= val;
        }
    }

    if (num1 > num2) swap(num1, num2);
    cout << num1 << " " << num2 << "\n";
    return 0;
}

```

### `CPPB-BIT-06` — Dao Bit Gia Tri Bu Mot

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    unsigned long long n;
    if (!(cin >> n)) return 0;

    int length = 64 - __builtin_clzll(n);
    unsigned long long mask = (1ULL << length) - 1;
    unsigned long long ans = n ^ mask;

    cout << ans << "\n";
    return 0;
}

```

### `CPPB-BIT-07` — Duyet Tap Con Bitmask

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    int total_masks = (1 << n);
    for (int mask = 0; mask < total_masks; ++mask) {
        bool first = true;
        for (int i = 0; i < n; ++i) {
            if ((mask >> i) & 1) {
                if (!first) cout << " ";
                cout << a[i];
                first = false;
            }
        }
        cout << "\n";
    }

    return 0;
}

```

### `CPPB-BIT-08` — Tong Tap Con Bang S

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long s;
    if (!(cin >> n >> s)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    int total_masks = (1 << n);
    for (int mask = 0; mask < total_masks; ++mask) {
        long long current_sum = 0;
        for (int i = 0; i < n; ++i) {
            if ((mask >> i) & 1) {
                current_sum += a[i];
            }
        }
        if (current_sum == s) {
            cout << "YES\n";
            return 0;
        }
    }

    cout << "NO\n";
    return 0;
}

```

### `CPPB-BIT-09` — Chia Tap Hop Chenh Lech Min

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> p(n);
    long long total_sum = 0;
    for (int i = 0; i < n; ++i) {
        cin >> p[i];
        total_sum += p[i];
    }

    long long min_diff = total_sum;
    int total_masks = (1 << n);

    for (int mask = 0; mask < total_masks; ++mask) {
        long long s1 = 0;
        for (int i = 0; i < n; ++i) {
            if ((mask >> i) & 1) {
                s1 += p[i];
            }
        }
        long long s2 = total_sum - s1;
        min_diff = min(min_diff, abs(s1 - s2));
    }

    cout << min_diff << "\n";
    return 0;
}

```

### `CPPB-BIT-10` — Dem Cap Tich And Bang Khong

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    const int MAX_VAL = 4096;
    vector<long long> cnt(MAX_VAL, 0);

    for (int i = 0; i < n; ++i) {
        int x;
        cin >> x;
        cnt[x]++;
    }

    long long total_pairs = 0;

    // Trường hợp u == 0
    total_pairs += cnt[0] * (cnt[0] - 1) / 2;
    for (int v = 1; v < MAX_VAL; ++v) {
        total_pairs += cnt[0] * cnt[v];
    }

    // Trường hợp 1 <= u < v
    for (int u = 1; u < MAX_VAL; ++u) {
        if (cnt[u] == 0) continue;
        for (int v = u + 1; v < MAX_VAL; ++v) {
            if ((u & v) == 0) {
                total_pairs += cnt[u] * cnt[v];
            }
        }
    }

    cout << total_pairs << "\n";
    return 0;
}

```

### `CPPB-BIT-11` — Cap Xor Lon Nhat

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    long long max_xor = 0;
    long long mask = 0;

    for (int bit = 30; bit >= 0; --bit) {
        mask |= (1LL << bit);
        vector<long long> prefixes;
        prefixes.reserve(n);
        for (long long x : a) {
            prefixes.push_back(x & mask);
        }
        sort(prefixes.begin(), prefixes.end());
        prefixes.erase(unique(prefixes.begin(), prefixes.end()), prefixes.end());

        long long candidate = max_xor | (1LL << bit);
        bool found = false;

        for (long long p : prefixes) {
            long long target = p ^ candidate;
            if (binary_search(prefixes.begin(), prefixes.end(), target)) {
                found = true;
                break;
            }
        }

        if (found) {
            max_xor = candidate;
        }
    }

    cout << max_xor << "\n";
    return 0;
}

```

### `CPPB-BIT-12` — Duyet Tat Ca Submask

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;

    bool first = true;
    for (long long sub = n; sub > 0; sub = (sub - 1) & n) {
        if (!first) cout << " ";
        cout << sub;
        first = false;
    }
    cout << "\n";

    return 0;
}

```

### `CPPB-BIT-13` — Day Con Tong Xor Bang K

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    int count_k = 0;
    int total_masks = (1 << n);

    for (int mask = 1; mask < total_masks; ++mask) {
        long long current_xor = 0;
        for (int i = 0; i < n; ++i) {
            if ((mask >> i) & 1) {
                current_xor ^= a[i];
            }
        }
        if (current_xor == k) {
            count_k++;
        }
    }

    cout << count_k << "\n";
    return 0;
}

```

### `CPPB-BIT-14` — Toi Uu Gan Viec N Nguoi

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<long long>> cost(n, vector<long long>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> cost[i][j];
        }
    }

    int total_masks = (1 << n);
    const long long INF = 1e18;
    vector<long long> dp(total_masks, INF);
    dp[0] = 0;

    for (int mask = 0; mask < total_masks; ++mask) {
        if (dp[mask] == INF) continue;
        int task_idx = __builtin_popcount(mask);
        if (task_idx >= n) continue;

        for (int j = 0; j < n; ++j) {
            if (!((mask >> j) & 1)) {
                int next_mask = mask | (1 << j);
                dp[next_mask] = min(dp[next_mask], dp[mask] + cost[task_idx][j]);
            }
        }
    }

    cout << dp[total_masks - 1] << "\n";
    return 0;
}

```

### `CPPB-BIT-15` — Cap Tong Luy Thua Hai

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    sort(a.begin(), a.end());

    long long total_pairs = 0;

    for (int i = 0; i < n; ++i) {
        for (int k = 1; k <= 30; ++k) {
            long long target = (1LL << k) - a[i];
            if (target <= 0) continue;

            auto it1 = lower_bound(a.begin() + i + 1, a.end(), target);
            auto it2 = upper_bound(a.begin() + i + 1, a.end(), target);
            total_pairs += (it2 - it1);
        }
    }

    cout << total_pairs << "\n";
    return 0;
}

```

### `CPPB-BIT-16` — Tap Doc Lap Bit Lon Nhat

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    int max_size = 0;
    int total_masks = (1 << n);

    for (int mask = 0; mask < total_masks; ++mask) {
        long long used_bits = 0;
        bool valid = true;
        int current_count = 0;

        for (int i = 0; i < n; ++i) {
            if ((mask >> i) & 1) {
                if (used_bits & a[i]) {
                    valid = false;
                    break;
                }
                used_bits |= a[i];
                current_count++;
            }
        }

        if (valid) {
            max_size = max(max_size, current_count);
        }
    }

    cout << max_size << "\n";
    return 0;
}

```

## Chương 03 — Bài 07: Ước, bội & số nguyên tố

### `CPPB-NT-01` — Uoc Chung Boi Chung

```cpp
#include <bits/stdc++.h>
using namespace std;

long long getGcd(long long a, long long b) {
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

    long long g = getGcd(a, b);
    long long l = (a / g) * b;

    cout << g << " " << l << "\n";
    return 0;
}
```

### `CPPB-NT-02` — Kiem Tra So Nguyen To

```cpp
#include <bits/stdc++.h>
using namespace std;

bool isPrime(long long n) {
    if (n < 2) return false;
    if (n == 2 || n == 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    for (long long i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) return false;
    }
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;

    cout << (isPrime(n) ? "YES" : "NO") << "\n";
    return 0;
}
```

### `CPPB-NT-03` — Phan Tich Thua So Nguyen To

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;

    vector<pair<long long, int>> factors;
    for (long long i = 2; i * i <= n; ++i) {
        if (n % i == 0) {
            int cnt = 0;
            while (n % i == 0) {
                cnt++;
                n /= i;
            }
            factors.push_back({i, cnt});
        }
    }
    if (n > 1) {
        factors.push_back({n, 1});
    }

    for (int i = 0; i < (int)factors.size(); ++i) {
        cout << factors[i].first << "^" << factors[i].second;
        if (i + 1 < (int)factors.size()) cout << " * ";
    }
    cout << "\n";
    return 0;
}
```

### `CPPB-NT-04` — Dem Uoc Va Tong Uoc

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;

    long long count_div = 1;
    long long sum_div = 1;

    for (long long i = 2; i * i <= n; ++i) {
        if (n % i == 0) {
            int a = 0;
            long long p_pow = 1;
            long long cur_sum = 1;
            while (n % i == 0) {
                a++;
                n /= i;
                p_pow *= i;
                cur_sum += p_pow;
            }
            count_div *= (a + 1);
            sum_div *= cur_sum;
        }
    }
    if (n > 1) {
        count_div *= 2;
        sum_div *= (1 + n);
    }

    cout << count_div << " " << sum_div << "\n";
    return 0;
}
```

### `CPPB-NT-05` — Kiem Tra So Chinh Phuong

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    unsigned long long n;
    if (!(cin >> n)) return 0;

    unsigned long long r = sqrt((double)n);
    while (r * r > n) r--;
    while ((r + 1) * (r + 1) <= n) r++;

    if (r * r == n) cout << "YES\n";
    else cout << "NO\n";
    return 0;
}
```

### `CPPB-NT-06` — Sang Nguyen To Eratosthenes

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<bool> is_prime(n + 1, true);
    is_prime[0] = is_prime[1] = false;

    for (int i = 2; 1LL * i * i <= n; ++i) {
        if (is_prime[i]) {
            for (int j = i * i; j <= n; j += i) {
                is_prime[j] = false;
            }
        }
    }

    bool first = true;
    for (int i = 2; i <= n; ++i) {
        if (is_prime[i]) {
            if (!first) cout << " ";
            cout << i;
            first = false;
        }
    }
    cout << "\n";
    return 0;
}
```

### `CPPB-NT-07` — Dem So Nguyen To Doan L R

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1000000;
vector<bool> is_prime(MAXN + 1, true);
vector<int> pref(MAXN + 1, 0);

void sieve() {
    is_prime[0] = is_prime[1] = false;
    for (int i = 2; 1LL * i * i <= MAXN; ++i) {
        if (is_prime[i]) {
            for (int j = i * i; j <= MAXN; j += i) {
                is_prime[j] = false;
            }
        }
    }
    for (int i = 1; i <= MAXN; ++i) {
        pref[i] = pref[i - 1] + (is_prime[i] ? 1 : 0);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    sieve();

    int q;
    if (!(cin >> q)) return 0;

    while (q--) {
        int l, r;
        cin >> l >> r;
        cout << pref[r] - pref[l - 1] << "\n";
    }
    return 0;
}
```

### `CPPB-NT-08` — Sang Uoc Nguyen To Nho Nhat Spf

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1000000;
vector<int> spf(MAXN + 1);

void sieveSPF() {
    for (int i = 1; i <= MAXN; ++i) spf[i] = i;
    for (int i = 2; 1LL * i * i <= MAXN; ++i) {
        if (spf[i] == i) {
            for (int j = i * i; j <= MAXN; j += i) {
                if (spf[j] == j) spf[j] = i;
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    sieveSPF();

    int q;
    if (!(cin >> q)) return 0;

    for (int i = 0; i < q; ++i) {
        int n;
        cin >> n;
        cout << spf[n] << (i + 1 == q ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```

### `CPPB-NT-09` — Sang Phan Doan Segmented Sieve

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long l, r;
    if (!(cin >> l >> r)) return 0;

    int lim = sqrt(r);
    vector<bool> is_prime(lim + 1, true);
    vector<int> primes;
    for (int i = 2; i <= lim; ++i) {
        if (is_prime[i]) {
            primes.push_back(i);
            for (int j = i * 2; j <= lim; j += i) is_prime[j] = false;
        }
    }

    vector<bool> is_prime_range(r - l + 1, true);
    for (int p : primes) {
        long long start = max(1LL * p * p, ((l + p - 1) / p) * p);
        for (long long j = start; j <= r; j += p) {
            is_prime_range[j - l] = false;
        }
    }

    if (l == 1) is_prime_range[0] = false;

    int count_primes = 0;
    for (int i = 0; i <= r - l; ++i) {
        if (is_prime_range[i]) count_primes++;
    }

    cout << count_primes << "\n";
    return 0;
}
```

### `CPPB-NT-10` — Cap So Nguyen To Sinh Doi

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    if (n < 5) {
        cout << 0 << "\n";
        return 0;
    }

    vector<bool> is_prime(n + 1, true);
    is_prime[0] = is_prime[1] = false;
    for (int i = 2; 1LL * i * i <= n; ++i) {
        if (is_prime[i]) {
            for (int j = i * i; j <= n; j += i) is_prime[j] = false;
        }
    }

    int count_twin = 0;
    for (int p = 3; p + 2 <= n; p += 2) {
        if (is_prime[p] && is_prime[p + 2]) count_twin++;
    }

    cout << count_twin << "\n";
    return 0;
}
```

### `CPPB-NT-11` — So Hoan Hao

```cpp
#include <bits/stdc++.h>
using namespace std;

bool isPrime(long long p) {
    if (p < 2) return false;
    for (long long i = 2; i * i <= p; ++i) {
        if (p % i == 0) return false;
    }
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    unsigned long long n;
    if (!(cin >> n)) return 0;

    // Theo Euclid-Euler, số hoàn hảo chẵn có dạng 2^(p-1) * (2^p - 1) với 2^p - 1 là số nguyên tố
    vector<unsigned long long> perfect_nums;
    int primes[] = {2, 3, 5, 7, 13, 17, 19, 31};
    for (int p : primes) {
        unsigned long long mersenne = (1ULL << p) - 1;
        if (isPrime(mersenne)) {
            unsigned long long perf = (1ULL << (p - 1)) * mersenne;
            perfect_nums.push_back(perf);
        }
    }

    for (auto v : perfect_nums) {
        if (v == n) {
            cout << "YES\n";
            return 0;
        }
    }
    cout << "NO\n";
    return 0;
}
```

### `CPPB-NT-12` — So Co Dung Ba Uoc

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;

    int lim = sqrt(n);
    vector<bool> is_prime(lim + 1, true);
    is_prime[0] = is_prime[1] = false;
    for (int i = 2; 1LL * i * i <= lim; ++i) {
        if (is_prime[i]) {
            for (int j = i * i; j <= lim; j += i) is_prime[j] = false;
        }
    }

    int count_3div = 0;
    for (int i = 2; i <= lim; ++i) {
        if (is_prime[i] && 1LL * i * i <= n) count_3div++;
    }

    cout << count_3div << "\n";
    return 0;
}
```

### `CPPB-NT-13` — So Gan Nguyen To Almost Prime

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> prime_count(n + 1, 0);
    for (int i = 2; i <= n; ++i) {
        if (prime_count[i] == 0) { // i là số nguyên tố
            for (int j = i; j <= n; j += i) {
                prime_count[j]++;
            }
        }
    }

    int ans = 0;
    for (int i = 1; i <= n; ++i) {
        if (prime_count[i] == 2) ans++;
    }

    cout << ans << "\n";
    return 0;
}
```

### `CPPB-NT-14` — Phan Tich Giai Thua Legendre

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, p;
    if (!(cin >> n >> p)) return 0;

    long long k = 0;
    while (n > 0) {
        k += (n / p);
        n /= p;
    }

    cout << k << "\n";
    return 0;
}
```

### `CPPB-NT-15` — Dem So Khong Tan Cung Giai Thua

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;

    long long count_zeros = 0;
    while (n > 0) {
        count_zeros += (n / 5);
        n /= 5;
    }

    cout << count_zeros << "\n";
    return 0;
}
```

### `CPPB-NT-16` — Cap Nguyen To Cung Nhau Phi Euler

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1000000;
vector<int> phi(MAXN + 1);

void sievePhi() {
    for (int i = 0; i <= MAXN; ++i) phi[i] = i;
    for (int i = 2; i <= MAXN; ++i) {
        if (phi[i] == i) { // i là số nguyên tố
            for (int j = i; j <= MAXN; j += i) {
                phi[j] -= phi[j] / i;
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    sievePhi();

    int n;
    if (!(cin >> n)) return 0;

    long long sum_phi = 0;
    for (int i = 1; i <= n; ++i) {
        sum_phi += phi[i];
    }

    // Số cặp (x, y) với gcd(x, y) = 1 là 2 * sum(phi(i)) - 1 (do (1,1) tính 1 lần)
    long long ans = 2 * sum_phi - 1;
    cout << ans << "\n";
    return 0;
}
```

## Chương 03 — Bài 08: Đồng dư & lũy thừa

### `CPPB-MOD-01` — Phep Tinh Dong Du Co Ban

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, b;
    if (!(cin >> a >> b)) return 0;

    a %= MOD;
    b %= MOD;

    long long add_res = (a + b) % MOD;
    long long sub_res = (a - b + MOD) % MOD;
    long long mul_res = (a * b) % MOD;

    cout << add_res << " " << sub_res << " " << mul_res << "\n";
    return 0;
}
```

### `CPPB-MOD-02` — Luy Thua Nhi Phan

```cpp
#include <bits/stdc++.h>
using namespace std;

long long powerMod(long long a, long long b, long long m) {
    if (m == 1) return 0;
    long long ans = 1 % m;
    a %= m;
    while (b > 0) {
        if (b & 1) ans = (ans * a) % m;
        a = (a * a) % m;
        b >>= 1;
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, b, m;
    if (!(cin >> a >> b >> m)) return 0;

    cout << powerMod(a, b, m) << "\n";
    return 0;
}
```

### `CPPB-MOD-03` — Luy Thua Chuoi So Lon

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

long long powerMod(long long a, long long b, long long m) {
    long long ans = 1;
    a %= m;
    while (b > 0) {
        if (b & 1) ans = (ans * a) % m;
        a = (a * a) % m;
        b >>= 1;
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a;
    string b_str;
    if (!(cin >> a >> b_str)) return 0;

    if (a % MOD == 0) {
        cout << 0 << "\n";
        return 0;
    }

    long long rem_b = 0;
    for (char c : b_str) {
        rem_b = (rem_b * 10 + (c - '0')) % (MOD - 1);
    }

    cout << powerMod(a, rem_b, MOD) << "\n";
    return 0;
}
```

### `CPPB-MOD-04` — Nhan An Do Chong Tran So

```cpp
#include <bits/stdc++.h>
using namespace std;

long long mulMod(long long a, long long b, long long m) {
    long long ans = 0;
    a %= m;
    while (b > 0) {
        if (b & 1) ans = (ans + a) % m;
        a = (a + a) % m;
        b >>= 1;
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, b, m;
    if (!(cin >> a >> b >> m)) return 0;

    cout << mulMod(a, b, m) << "\n";
    return 0;
}
```

### `CPPB-MOD-05` — Tong Cap So Nhan Dong Du

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

long long powerMod(long long a, long long b) {
    long long ans = 1;
    a %= MOD;
    while (b > 0) {
        if (b & 1) ans = (ans * a) % MOD;
        a = (a * a) % MOD;
        b >>= 1;
    }
    return ans;
}

long long sumGeo(long long a, long long k) {
    if (k == 0) return 0;
    if (k == 1) return 1;
    if (k % 2 == 0) {
        long long half = sumGeo(a, k / 2);
        return half * (1 + powerMod(a, k / 2)) % MOD;
    } else {
        return (1 + a * sumGeo(a, k - 1)) % MOD;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, n;
    if (!(cin >> a >> n)) return 0;

    cout << sumGeo(a, n + 1) << "\n";
    return 0;
}
```

### `CPPB-MOD-06` — Nghich Dao Fermat

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

long long powerMod(long long a, long long b) {
    long long ans = 1;
    a %= MOD;
    while (b > 0) {
        if (b & 1) ans = (ans * a) % MOD;
        a = (a * a) % MOD;
        b >>= 1;
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a;
    if (!(cin >> a)) return 0;

    cout << powerMod(a, MOD - 2) << "\n";
    return 0;
}
```

### `CPPB-MOD-07` — Nghich Dao Euclid Mo Rong

```cpp
#include <bits/stdc++.h>
using namespace std;

long long extGCD(long long a, long long b, long long &x, long long &y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    long long x1, y1;
    long long d = extGCD(b, a % b, x1, y1);
    x = y1;
    y = x1 - y1 * (a / b);
    return d;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, m;
    if (!(cin >> a >> m)) return 0;

    long long x, y;
    extGCD(a, m, x, y);
    x = (x % m + m) % m;

    cout << x << "\n";
    return 0;
}
```

### `CPPB-MOD-08` — Phep Chia Dong Du

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

long long powerMod(long long a, long long b) {
    long long ans = 1;
    a %= MOD;
    while (b > 0) {
        if (b & 1) ans = (ans * a) % MOD;
        a = (a * a) % MOD;
        b >>= 1;
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, b;
    if (!(cin >> a >> b)) return 0;

    a %= MOD;
    long long inv_b = powerMod(b, MOD - 2);
    long long ans = (a * inv_b) % MOD;

    cout << ans << "\n";
    return 0;
}
```

### `CPPB-MOD-09` — To Hop C N K Modulo

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1000000;
const long long MOD = 1000000007;

vector<long long> fact(MAXN + 1);
vector<long long> invFact(MAXN + 1);

long long powerMod(long long a, long long b) {
    long long ans = 1;
    a %= MOD;
    while (b > 0) {
        if (b & 1) ans = (ans * a) % MOD;
        a = (a * a) % MOD;
        b >>= 1;
    }
    return ans;
}

void precompute() {
    fact[0] = 1;
    for (int i = 1; i <= MAXN; ++i) fact[i] = (fact[i - 1] * i) % MOD;
    invFact[MAXN] = powerMod(fact[MAXN], MOD - 2);
    for (int i = MAXN; i >= 1; --i) invFact[i - 1] = (invFact[i] * i) % MOD;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    precompute();

    int q;
    if (!(cin >> q)) return 0;

    while (q--) {
        int n, k;
        cin >> n >> k;
        if (k < 0 || k > n) cout << 0 << "\n";
        else cout << fact[n] * invFact[k] % MOD * invFact[n - k] % MOD << "\n";
    }
    return 0;
}
```

### `CPPB-MOD-10` — Chinh Hop A N K Modulo

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1000000;
const long long MOD = 1000000007;

vector<long long> fact(MAXN + 1);
vector<long long> invFact(MAXN + 1);

long long powerMod(long long a, long long b) {
    long long ans = 1;
    a %= MOD;
    while (b > 0) {
        if (b & 1) ans = (ans * a) % MOD;
        a = (a * a) % MOD;
        b >>= 1;
    }
    return ans;
}

void precompute() {
    fact[0] = 1;
    for (int i = 1; i <= MAXN; ++i) fact[i] = (fact[i - 1] * i) % MOD;
    invFact[MAXN] = powerMod(fact[MAXN], MOD - 2);
    for (int i = MAXN; i >= 1; --i) invFact[i - 1] = (invFact[i] * i) % MOD;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    precompute();

    int q;
    if (!(cin >> q)) return 0;

    while (q--) {
        int n, k;
        cin >> n >> k;
        if (k < 0 || k > n) cout << 0 << "\n";
        else cout << fact[n] * invFact[n - k] % MOD << "\n";
    }
    return 0;
}
```

### `CPPB-MOD-11` — Fibonacci Dong Du Lon

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

void multiply(long long F[2][2], long long M[2][2]) {
    long long x = (F[0][0] * M[0][0] + F[0][1] * M[1][0]) % MOD;
    long long y = (F[0][0] * M[0][1] + F[0][1] * M[1][1]) % MOD;
    long long z = (F[1][0] * M[0][0] + F[1][0] * M[1][0]) % MOD;
    long long w = (F[1][0] * M[0][1] + F[1][1] * M[1][1]) % MOD;
    F[0][0] = x; F[0][1] = y;
    F[1][0] = z; F[1][1] = w;
}

void powerMat(long long F[2][2], long long n) {
    if (n == 0 || n == 1) return;
    long long M[2][2] = {{1, 1}, {1, 0}};
    powerMat(F, n / 2);
    multiply(F, F);
    if (n % 2 != 0) multiply(F, M);
}

long long fib(long long n) {
    if (n == 0) return 0;
    long long F[2][2] = {{1, 1}, {1, 0}};
    powerMat(F, n - 1);
    return F[0][0];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;

    cout << fib(n) << "\n";
    return 0;
}
```

### `CPPB-MOD-12` — So Catalan Dong Du

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 2000000;
const long long MOD = 1000000007;

vector<long long> fact(MAXN + 1);
vector<long long> invFact(MAXN + 1);

long long powerMod(long long a, long long b) {
    long long ans = 1;
    a %= MOD;
    while (b > 0) {
        if (b & 1) ans = (ans * a) % MOD;
        a = (a * a) % MOD;
        b >>= 1;
    }
    return ans;
}

void precompute() {
    fact[0] = 1;
    for (int i = 1; i <= MAXN; ++i) fact[i] = (fact[i - 1] * i) % MOD;
    invFact[MAXN] = powerMod(fact[MAXN], MOD - 2);
    for (int i = MAXN; i >= 1; --i) invFact[i - 1] = (invFact[i] * i) % MOD;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    precompute();

    int n;
    if (!(cin >> n)) return 0;

    long long c2n_n = fact[2 * n] * invFact[n] % MOD * invFact[n] % MOD;
    long long inv_n_plus_1 = powerMod(n + 1, MOD - 2);
    long long ans = (c2n_n * inv_n_plus_1) % MOD;

    cout << ans << "\n";
    return 0;
}
```

### `CPPB-MOD-13` — Luy Thua Tang Tower Of Powers

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

long long powerMod(long long a, long long b, long long m) {
    if (m == 1) return 0;
    long long ans = 1 % m;
    a %= m;
    while (b > 0) {
        if (b & 1) ans = (ans * a) % m;
        a = (a * a) % m;
        b >>= 1;
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, b, c;
    if (!(cin >> a >> b >> c)) return 0;

    long long exp = powerMod(b, c, MOD - 1);
    long long ans = powerMod(a, exp, MOD);

    cout << ans << "\n";
    return 0;
}
```

### `CPPB-MOD-14` — Nghich Dao Tuyen Tinh

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> inv(n + 1);
    inv[1] = 1;
    long long sum_inv = 1;

    for (int i = 2; i <= n; ++i) {
        inv[i] = (MOD - (MOD / i) * inv[MOD % i] % MOD) % MOD;
        sum_inv = (sum_inv + inv[i]) % MOD;
    }

    cout << sum_inv << "\n";
    return 0;
}
```

### `CPPB-MOD-15` — Phuong Trinh Dong Du Tuyen Tinh

```cpp
#include <bits/stdc++.h>
using namespace std;

long long extGCD(long long a, long long b, long long &x, long long &y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    long long x1, y1;
    long long d = extGCD(b, a % b, x1, y1);
    x = y1;
    y = x1 - y1 * (a / b);
    return d;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, b, m;
    if (!(cin >> a >> b >> m)) return 0;

    long long x, y;
    long long g = extGCD(a, m, x, y);

    if (b % g != 0) {
        cout << -1 << "\n";
        return 0;
    }

    x = (x % m + m) % m;
    long long m_prime = m / g;
    long long ans = (x * ((b / g) % m_prime)) % m_prime;
    ans = (ans % m_prime + m_prime) % m_prime;

    cout << ans << "\n";
    return 0;
}
```

### `CPPB-MOD-16` — Can Bac Hai Modulo

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long P = 1000000007;

long long powerMod(long long a, long long b, long long m) {
    long long ans = 1;
    a %= m;
    while (b > 0) {
        if (b & 1) ans = (ans * a) % m;
        a = (a * a) % m;
        b >>= 1;
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a;
    if (!(cin >> a)) return 0;

    a %= P;
    if (a == 0) {
        cout << 0 << "\n";
        return 0;
    }

    if (powerMod(a, (P - 1) / 2, P) != 1) {
        cout << -1 << "\n";
        return 0;
    }

    long long x = powerMod(a, (P + 1) / 4, P);
    long long x2 = P - x;

    long long min_x = min(x, x2);
    cout << min_x << "\n";
    return 0;
}
```

## Chương 03 — Bài 09: Số nguyên lớn

### `CPPB-BIG-01` — So Sanh Hai So Lon

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a, b;
    if (!(cin >> a >> b)) return 0;

    if (a.size() > b.size()) cout << ">\n";
    else if (a.size() < b.size()) cout << "<\n";
    else {
        if (a > b) cout << ">\n";
        else if (a < b) cout << "<\n";
        else cout << "=\n";
    }
    return 0;
}
```

### `CPPB-BIG-02` — Cong Hai So Lon

```cpp
#include <bits/stdc++.h>
using namespace std;

string addBig(string a, string b) {
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());

    string res = "";
    int carry = 0;
    int n = max(a.size(), b.size());

    for (int i = 0; i < n || carry; ++i) {
        int sum = carry;
        if (i < (int)a.size()) sum += a[i] - '0';
        if (i < (int)b.size()) sum += b[i] - '0';
        res.push_back((sum % 10) + '0');
        carry = sum / 10;
    }

    reverse(res.begin(), res.end());
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a, b;
    if (!(cin >> a >> b)) return 0;

    cout << addBig(a, b) << "\n";
    return 0;
}
```

### `CPPB-BIG-03` — Tru Hai So Lon Khong Am

```cpp
#include <bits/stdc++.h>
using namespace std;

string subBig(string a, string b) {
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());

    string res = "";
    int borrow = 0;

    for (int i = 0; i < (int)a.size(); ++i) {
        int diff = (a[i] - '0') - borrow;
        if (i < (int)b.size()) diff -= (b[i] - '0');
        if (diff < 0) {
            diff += 10;
            borrow = 1;
        } else {
            borrow = 0;
        }
        res.push_back(diff + '0');
    }

    while (res.size() > 1 && res.back() == '0') res.pop_back();
    reverse(res.begin(), res.end());
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a, b;
    if (!(cin >> a >> b)) return 0;

    cout << subBig(a, b) << "\n";
    return 0;
}
```

### `CPPB-BIG-04` — Tru Hai So Lon Tong Quat

```cpp
#include <bits/stdc++.h>
using namespace std;

bool isLess(const string &a, const string &b) {
    if (a.size() != b.size()) return a.size() < b.size();
    return a < b;
}

string subBig(string a, string b) {
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());

    string res = "";
    int borrow = 0;

    for (int i = 0; i < (int)a.size(); ++i) {
        int diff = (a[i] - '0') - borrow;
        if (i < (int)b.size()) diff -= (b[i] - '0');
        if (diff < 0) {
            diff += 10;
            borrow = 1;
        } else {
            borrow = 0;
        }
        res.push_back(diff + '0');
    }

    while (res.size() > 1 && res.back() == '0') res.pop_back();
    reverse(res.begin(), res.end());
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a, b;
    if (!(cin >> a >> b)) return 0;

    if (a == b) {
        cout << "0\n";
    } else if (isLess(a, b)) {
        cout << "-" << subBig(b, a) << "\n";
    } else {
        cout << subBig(a, b) << "\n";
    }
    return 0;
}
```

### `CPPB-BIG-05` — Nhan So Lon Voi So Nho

```cpp
#include <bits/stdc++.h>
using namespace std;

string mulSmall(string a, long long b) {
    if (a == "0" || b == 0) return "0";

    reverse(a.begin(), a.end());
    string res = "";
    long long carry = 0;

    for (int i = 0; i < (int)a.size() || carry; ++i) {
        long long prod = carry;
        if (i < (int)a.size()) prod += 1LL * (a[i] - '0') * b;
        res.push_back((prod % 10) + '0');
        carry = prod / 10;
    }

    while (res.size() > 1 && res.back() == '0') res.pop_back();
    reverse(res.begin(), res.end());
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a;
    long long b;
    if (!(cin >> a >> b)) return 0;

    cout << mulSmall(a, b) << "\n";
    return 0;
}
```

### `CPPB-BIG-06` — Nhan Hai So Lon

```cpp
#include <bits/stdc++.h>
using namespace std;

string mulBig(string a, string b) {
    if (a == "0" || b == "0") return "0";

    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());

    int n = a.size(), m = b.size();
    vector<int> c(n + m, 0);

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            c[i + j] += (a[i] - '0') * (b[j] - '0');
        }
    }

    int carry = 0;
    string res = "";
    for (int i = 0; i < n + m || carry; ++i) {
        if (i < (int)c.size()) carry += c[i];
        res.push_back((carry % 10) + '0');
        carry /= 10;
    }

    while (res.size() > 1 && res.back() == '0') res.pop_back();
    reverse(res.begin(), res.end());
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a, b;
    if (!(cin >> a >> b)) return 0;

    cout << mulBig(a, b) << "\n";
    return 0;
}
```

### `CPPB-BIG-07` — Chia So Lon Cho So Nho

```cpp
#include <bits/stdc++.h>
using namespace std;

string divSmall(string a, long long b) {
    string res = "";
    long long cur = 0;

    for (char c : a) {
        cur = cur * 10 + (c - '0');
        res.push_back((cur / b) + '0');
        cur %= b;
    }

    int pos = 0;
    while (pos + 1 < (int)res.size() && res[pos] == '0') pos++;
    return res.substr(pos);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a;
    long long b;
    if (!(cin >> a >> b)) return 0;

    cout << divSmall(a, b) << "\n";
    return 0;
}
```

### `CPPB-BIG-08` — Chia Lay Du So Lon Cho So Nho

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a;
    long long b;
    if (!(cin >> a >> b)) return 0;

    long long cur = 0;
    for (char c : a) {
        cur = (cur * 10 + (c - '0')) % b;
    }

    cout << cur << "\n";
    return 0;
}
```

### `CPPB-BIG-09` — Giai Thua So Lon

```cpp
#include <bits/stdc++.h>
using namespace std;

string mulSmall(string a, int b) {
    reverse(a.begin(), a.end());
    string res = "";
    int carry = 0;
    for (int i = 0; i < (int)a.size() || carry; ++i) {
        int prod = carry;
        if (i < (int)a.size()) prod += (a[i] - '0') * b;
        res.push_back((prod % 10) + '0');
        carry = prod / 10;
    }
    reverse(res.begin(), res.end());
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    string ans = "1";
    for (int i = 2; i <= n; ++i) {
        ans = mulSmall(ans, i);
    }

    cout << ans << "\n";
    return 0;
}
```

### `CPPB-BIG-10` — Luy Thua So Lon Chinh Xac

```cpp
#include <bits/stdc++.h>
using namespace std;

string mulBig(string a, string b) {
    if (a == "0" || b == "0") return "0";
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());
    int n = a.size(), m = b.size();
    vector<int> c(n + m, 0);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            c[i + j] += (a[i] - '0') * (b[j] - '0');
        }
    }
    int carry = 0;
    string res = "";
    for (int i = 0; i < n + m || carry; ++i) {
        if (i < (int)c.size()) carry += c[i];
        res.push_back((carry % 10) + '0');
        carry /= 10;
    }
    while (res.size() > 1 && res.back() == '0') res.pop_back();
    reverse(res.begin(), res.end());
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int a, b;
    if (!(cin >> a >> b)) return 0;

    string base = to_string(a);
    string ans = "1";

    while (b > 0) {
        if (b & 1) ans = mulBig(ans, base);
        base = mulBig(base, base);
        b >>= 1;
    }

    cout << ans << "\n";
    return 0;
}
```

### `CPPB-BIG-11` — Fibonacci So Lon

```cpp
#include <bits/stdc++.h>
using namespace std;

string addBig(string a, string b) {
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());
    string res = "";
    int carry = 0;
    int n = max(a.size(), b.size());
    for (int i = 0; i < n || carry; ++i) {
        int sum = carry;
        if (i < (int)a.size()) sum += a[i] - '0';
        if (i < (int)b.size()) sum += b[i] - '0';
        res.push_back((sum % 10) + '0');
        carry = sum / 10;
    }
    reverse(res.begin(), res.end());
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    if (n == 0) { cout << "0\n"; return 0; }
    if (n == 1) { cout << "1\n"; return 0; }

    string f0 = "0", f1 = "1", f2 = "";
    for (int i = 2; i <= n; ++i) {
        f2 = addBig(f0, f1);
        f0 = f1;
        f1 = f2;
    }

    cout << f1 << "\n";
    return 0;
}
```

### `CPPB-BIG-12` — Tong Chu So Giai Thua

```cpp
#include <bits/stdc++.h>
using namespace std;

string mulSmall(string a, int b) {
    reverse(a.begin(), a.end());
    string res = "";
    int carry = 0;
    for (int i = 0; i < (int)a.size() || carry; ++i) {
        int prod = carry;
        if (i < (int)a.size()) prod += (a[i] - '0') * b;
        res.push_back((prod % 10) + '0');
        carry = prod / 10;
    }
    reverse(res.begin(), res.end());
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    string fact = "1";
    for (int i = 2; i <= n; ++i) {
        fact = mulSmall(fact, i);
    }

    long long sum_digits = 0;
    for (char c : fact) {
        sum_digits += (c - '0');
    }

    cout << sum_digits << "\n";
    return 0;
}
```

### `CPPB-BIG-13` — Chia Hai So Nguyen Lon

```cpp
#include <bits/stdc++.h>
using namespace std;

bool isLess(const string &a, const string &b) {
    if (a.size() != b.size()) return a.size() < b.size();
    return a < b;
}

string subBig(string a, string b) {
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());
    string res = "";
    int borrow = 0;
    for (int i = 0; i < (int)a.size(); ++i) {
        int diff = (a[i] - '0') - borrow;
        if (i < (int)b.size()) diff -= (b[i] - '0');
        if (diff < 0) { diff += 10; borrow = 1; }
        else borrow = 0;
        res.push_back(diff + '0');
    }
    while (res.size() > 1 && res.back() == '0') res.pop_back();
    reverse(res.begin(), res.end());
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a, b;
    if (!(cin >> a >> b)) return 0;

    if (isLess(a, b)) {
        cout << "0\n";
        return 0;
    }

    string cur = "";
    string res = "";

    for (char c : a) {
        cur.push_back(c);
        while (cur.size() > 1 && cur[0] == '0') cur.erase(cur.begin());
        int digit = 0;
        while (!isLess(cur, b)) {
            cur = subBig(cur, b);
            digit++;
        }
        res.push_back(digit + '0');
    }

    int pos = 0;
    while (pos + 1 < (int)res.size() && res[pos] == '0') pos++;
    cout << res.substr(pos) << "\n";
    return 0;
}
```

### `CPPB-BIG-14` — Can Bac Hai So Lon

```cpp
#include <bits/stdc++.h>
using namespace std;

bool isLess(const string &a, const string &b) {
    if (a.size() != b.size()) return a.size() < b.size();
    return a < b;
}

string mulBig(string a, string b) {
    if (a == "0" || b == "0") return "0";
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());
    int n = a.size(), m = b.size();
    vector<int> c(n + m, 0);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            c[i + j] += (a[i] - '0') * (b[j] - '0');
        }
    }
    int carry = 0;
    string res = "";
    for (int i = 0; i < n + m || carry; ++i) {
        if (i < (int)c.size()) carry += c[i];
        res.push_back((carry % 10) + '0');
        carry /= 10;
    }
    while (res.size() > 1 && res.back() == '0') res.pop_back();
    reverse(res.begin(), res.end());
    return res;
}

string addBig(string a, string b) {
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());
    string res = "";
    int carry = 0;
    int n = max(a.size(), b.size());
    for (int i = 0; i < n || carry; ++i) {
        int sum = carry;
        if (i < (int)a.size()) sum += a[i] - '0';
        if (i < (int)b.size()) sum += b[i] - '0';
        res.push_back((sum % 10) + '0');
        carry = sum / 10;
    }
    reverse(res.begin(), res.end());
    return res;
}

string div2(string a) {
    string res = "";
    int cur = 0;
    for (char c : a) {
        cur = cur * 10 + (c - '0');
        res.push_back((cur / 2) + '0');
        cur %= 2;
    }
    int pos = 0;
    while (pos + 1 < (int)res.size() && res[pos] == '0') pos++;
    return res.substr(pos);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a;
    if (!(cin >> a)) return 0;

    int target_len = (a.size() + 1) / 2;
    string low = "1";
    string high = string(target_len + 1, '9');
    string ans = "1";

    while (!isLess(high, low)) {
        string mid = div2(addBig(low, high));
        string sq = mulBig(mid, mid);
        if (!isLess(a, sq)) {
            ans = mid;
            low = addBig(mid, "1");
        } else {
            // high = mid - 1
            // vi low, high chi dung cho binary search chuoi
            int borrow = 1;
            for (int i = (int)mid.size() - 1; i >= 0; --i) {
                if (mid[i] >= '1') { mid[i]--; break; }
                else mid[i] = '9';
            }
            while (mid.size() > 1 && mid[0] == '0') mid.erase(mid.begin());
            high = mid;
        }
    }

    cout << ans << "\n";
    return 0;
}
```

### `CPPB-BIG-15` — Uoc Chung Lon Nhat So Lon

```cpp
#include <bits/stdc++.h>
using namespace std;

bool isLess(const string &a, const string &b) {
    if (a.size() != b.size()) return a.size() < b.size();
    return a < b;
}

string subBig(string a, string b) {
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());
    string res = "";
    int borrow = 0;
    for (int i = 0; i < (int)a.size(); ++i) {
        int diff = (a[i] - '0') - borrow;
        if (i < (int)b.size()) diff -= (b[i] - '0');
        if (diff < 0) { diff += 10; borrow = 1; }
        else borrow = 0;
        res.push_back(diff + '0');
    }
    while (res.size() > 1 && res.back() == '0') res.pop_back();
    reverse(res.begin(), res.end());
    return res;
}

string div2(string a) {
    string res = "";
    int cur = 0;
    for (char c : a) {
        cur = cur * 10 + (c - '0');
        res.push_back((cur / 2) + '0');
        cur %= 2;
    }
    int pos = 0;
    while (pos + 1 < (int)res.size() && res[pos] == '0') pos++;
    return res.substr(pos);
}

string mul2(string a) {
    reverse(a.begin(), a.end());
    string res = "";
    int carry = 0;
    for (int i = 0; i < (int)a.size() || carry; ++i) {
        int prod = carry;
        if (i < (int)a.size()) prod += (a[i] - '0') * 2;
        res.push_back((prod % 10) + '0');
        carry = prod / 10;
    }
    reverse(res.begin(), res.end());
    return res;
}

bool isEven(const string &s) {
    return (s.back() - '0') % 2 == 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a, b;
    if (!(cin >> a >> b)) return 0;

    int shift = 0;
    while (a != "0" && b != "0") {
        if (isEven(a) && isEven(b)) {
            shift++;
            a = div2(a);
            b = div2(b);
        } else if (isEven(a)) {
            a = div2(a);
        } else if (isEven(b)) {
            b = div2(b);
        } else {
            if (isLess(a, b)) b = subBig(b, a);
            else a = subBig(a, b);
        }
    }

    string ans = (a == "0" ? b : a);
    while (shift--) ans = mul2(ans);

    cout << ans << "\n";
    return 0;
}
```

### `CPPB-BIG-16` — To Hop So Lon Chinh Xac

```cpp
#include <bits/stdc++.h>
using namespace std;

string addBig(string a, string b) {
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());
    string res = "";
    int carry = 0;
    int n = max(a.size(), b.size());
    for (int i = 0; i < n || carry; ++i) {
        int sum = carry;
        if (i < (int)a.size()) sum += a[i] - '0';
        if (i < (int)b.size()) sum += b[i] - '0';
        res.push_back((sum % 10) + '0');
        carry = sum / 10;
    }
    reverse(res.begin(), res.end());
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<vector<string>> c(n + 1, vector<string>(k + 1, "0"));
    for (int i = 0; i <= n; ++i) {
        c[i][0] = "1";
        for (int j = 1; j <= min(i, k); ++j) {
            if (j == i) c[i][j] = "1";
            else c[i][j] = addBig(c[i - 1][j - 1], c[i - 1][j]);
        }
    }

    cout << c[n][k] << "\n";
    return 0;
}
```

## Chương 04 — Bài 10: Đệ quy

### `CPPB-REC-01` — In Day So De Quy

```cpp
#include <bits/stdc++.h>
using namespace std;

void printForward(int n) {
    if (n <= 0) return;
    printForward(n - 1);
    cout << n << " ";
}

void printBackward(int n) {
    if (n <= 0) return;
    cout << n << " ";
    printBackward(n - 1);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    printForward(n);
    cout << "\n";
    printBackward(n);
    cout << "\n";
    return 0;
}

```

### `CPPB-REC-02` — Tong Day So Va Giai Thua

```cpp
#include <bits/stdc++.h>
using namespace std;

long long getSum(int n) {
    if (n <= 1) return n;
    return n + getSum(n - 1);
}

long long getFact(int n) {
    if (n <= 1) return 1;
    return 1LL * n * getFact(n - 1);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    cout << getSum(n) << " " << getFact(n) << "\n";
    return 0;
}

```

### `CPPB-REC-03` — Dem Va Tinh Tong Chu So

```cpp
#include <bits/stdc++.h>
using namespace std;

int countDigits(long long n) {
    if (n < 10) return 1;
    return 1 + countDigits(n / 10);
}

long long sumDigits(long long n) {
    if (n < 10) return n;
    return (n % 10) + sumDigits(n / 10);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long n;
    if (!(cin >> n)) return 0;
    cout << countDigits(n) << " " << sumDigits(n) << "\n";
    return 0;
}

```

### `CPPB-REC-04` — Dao Nguoc Mang De Quy

```cpp
#include <bits/stdc++.h>
using namespace std;

void reverseRec(vector<long long> &a, int l, int r) {
    if (l >= r) return;
    swap(a[l], a[r]);
    reverseRec(a, l + 1, r - 1);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    reverseRec(a, 0, n - 1);
    for (int i = 0; i < n; ++i) cout << a[i] << (i + 1 == n ? "" : " ");
    cout << "\n";
    return 0;
}

```

### `CPPB-REC-05` — Kiem Tra Palindrome De Quy

```cpp
#include <bits/stdc++.h>
using namespace std;

bool isPalindromeRec(const string &s, int l, int r) {
    if (l >= r) return true;
    if (s[l] != s[r]) return false;
    return isPalindromeRec(s, l + 1, r - 1);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s;
    if (!(cin >> s)) return 0;
    if (isPalindromeRec(s, 0, (int)s.size() - 1)) {
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }
    return 0;
}

```

### `CPPB-REC-06` — Tim Min Max De Quy

```cpp
#include <bits/stdc++.h>
using namespace std;

long long getMinRec(const vector<long long> &a, int l, int r) {
    if (l == r) return a[l];
    int mid = l + (r - l) / 2;
    return min(getMinRec(a, l, mid), getMinRec(a, mid + 1, r));
}

long long getMaxRec(const vector<long long> &a, int l, int r) {
    if (l == r) return a[l];
    int mid = l + (r - l) / 2;
    return max(getMaxRec(a, l, mid), getMaxRec(a, mid + 1, r));
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    cout << getMinRec(a, 0, n - 1) << " " << getMaxRec(a, 0, n - 1) << "\n";
    return 0;
}

```

### `CPPB-REC-07` — Uoc Chung Lon Nhat De Quy

```cpp
#include <bits/stdc++.h>
using namespace std;

long long gcdRec(long long a, long long b) {
    if (b == 0) return a;
    return gcdRec(b, a % b);
}

void print128(__int128 n) {
    if (n == 0) { cout << 0; return; }
    string s = "";
    while (n > 0) {
        s.push_back(char('0' + (n % 10)));
        n /= 10;
    }
    reverse(s.begin(), s.end());
    cout << s;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long a, b;
    if (!(cin >> a >> b)) return 0;
    long long g = gcdRec(a, b);
    __int128 lcm = ((__int128)a / g) * b;
    cout << g << " ";
    print128(lcm);
    cout << "\n";
    return 0;
}

```

### `CPPB-REC-08` — Luy Thua Nhi Phan De Quy

```cpp
#include <bits/stdc++.h>
using namespace std;

long long powerRec(long long a, long long b, long long m) {
    if (b == 0) return 1 % m;
    long long half = powerRec(a, b / 2, m);
    long long res = (1LL * (half % m) * (half % m)) % m;
    if (b % 2 == 1) res = (1LL * res * (a % m)) % m;
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long a, b, m;
    if (!(cin >> a >> b >> m)) return 0;
    cout << powerRec(a, b, m) << "\n";
    return 0;
}

```

### `CPPB-REC-09` — Thap Ha Noi Co Ban

```cpp
#include <bits/stdc++.h>
using namespace std;

void solveHanoi(int n, char from, char to, char aux) {
    if (n == 0) return;
    solveHanoi(n - 1, from, aux, to);
    cout << from << " -> " << to << "\n";
    solveHanoi(n - 1, aux, to, from);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    cout << (1 << n) - 1 << "\n";
    solveHanoi(n, 'A', 'C', 'B');
    return 0;
}

```

### `CPPB-REC-10` — Fibonacci Cay Nhi Phan

```cpp
#include <bits/stdc++.h>
using namespace std;

long long call_count = 0;

long long fibRec(int n) {
    call_count++;
    if (n <= 0) return 0;
    if (n == 1) return 1;
    return fibRec(n - 1) + fibRec(n - 2);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    long long val = fibRec(n);
    cout << val << " " << call_count << "\n";
    return 0;
}

```

### `CPPB-REC-11` — Chuyen Doi He Nhi Phan De Quy

```cpp
#include <bits/stdc++.h>
using namespace std;

void printBinaryRec(long long n) {
    if (n == 0) return;
    printBinaryRec(n / 2);
    cout << (n % 2);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long n;
    if (!(cin >> n)) return 0;
    if (n == 0) {
        cout << 0 << "\n";
    } else {
        printBinaryRec(n);
        cout << "\n";
    }
    return 0;
}

```

### `CPPB-REC-12` — Xay Dung Cong Thuc Truy Hoi Dan Dau

```cpp
#include <bits/stdc++.h>
using namespace std;

long long solveRec(int n) {
    if (n == 1) return 1;
    long long term = (n % 2 == 1) ? n : -n;
    return solveRec(n - 1) + term;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    cout << solveRec(n) << "\n";
    return 0;
}

```

### `CPPB-REC-13` — Thap Ha Noi Co Rang Buoc

```cpp
#include <bits/stdc++.h>
using namespace std;

void moveAtoB(int n, char a, char b, char c);
void moveBtoC(int n, char b, char c, char a);

void solveConstrainedHanoi(int n, char from, char to, char aux) {
    if (n == 0) return;
    // Chuyển n-1 đĩa from -> to
    solveConstrainedHanoi(n - 1, from, to, aux);
    // Chuyển đĩa n: from -> aux
    cout << from << " -> " << aux << "\n";
    // Chuyển n-1 đĩa to -> from
    solveConstrainedHanoi(n - 1, to, from, aux);
    // Chuyển đĩa n: aux -> to
    cout << aux << " -> " << to << "\n";
    // Chuyển n-1 đĩa from -> to
    solveConstrainedHanoi(n - 1, from, to, aux);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    long long total_steps = 1;
    for (int i = 0; i < n; ++i) total_steps *= 3;
    total_steps -= 1;
    cout << total_steps << "\n";
    solveConstrainedHanoi(n, 'A', 'C', 'B');
    return 0;
}

```

### `CPPB-REC-14` — Sinh Xau Nhi Phan Khong 2 So 1 Lien Ke

```cpp
#include <bits/stdc++.h>
using namespace std;

vector<string> results;

void genRec(int n, string &cur, char last_char) {
    if ((int)cur.size() == n) {
        results.push_back(cur);
        return;
    }
    // Luôn có thể thêm '0'
    cur.push_back('0');
    genRec(n, cur, '0');
    cur.pop_back();

    // Chỉ thêm '1' nếu ký tự trước không phải '1'
    if (last_char != '1') {
        cur.push_back('1');
        genRec(n, cur, '1');
        cur.pop_back();
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    string cur = "";
    genRec(n, cur, '0');
    cout << results.size() << "\n";
    for (const string &s : results) cout << s << "\n";
    return 0;
}

```

### `CPPB-REC-15` — Phan Tich So Thanh Tong De Quy

```cpp
#include <bits/stdc++.h>
using namespace std;

long long countPartitions(int remain, int max_val) {
    if (remain == 0) return 1;
    if (remain < 0 || max_val <= 0) return 0;
    // Chọn dùng max_val hoặc không dùng max_val
    return countPartitions(remain - max_val, max_val) + countPartitions(remain, max_val - 1);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    cout << countPartitions(n, n) << "\n";
    return 0;
}

```

### `CPPB-REC-16` — Dem Cau Hinh Cay Catalan De Quy

```cpp
#include <bits/stdc++.h>
using namespace std;

long long countBST(int n) {
    if (n <= 1) return 1;
    long long total = 0;
    for (int root = 1; root <= n; ++root) {
        int left_size = root - 1;
        int right_size = n - root;
        total += countBST(left_size) * countBST(right_size);
    }
    return total;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    cout << countBST(n) << "\n";
    return 0;
}

```

## Chương 04 — Bài 11: Chia để trị

### `CPPB-DAC-01` — Tim Kiem Nhi Phan Chia De Tri

```cpp
#include <bits/stdc++.h>
using namespace std;

int binarySearchDac(const vector<long long> &a, int l, int r, long long x) {
    if (l > r) return -1;
    int mid = l + (r - l) / 2;
    if (a[mid] == x) {
        int left_res = binarySearchDac(a, l, mid - 1, x);
        if (left_res != -1) return left_res;
        return mid;
    }
    if (a[mid] > x) return binarySearchDac(a, l, mid - 1, x);
    return binarySearchDac(a, mid + 1, r, x);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    long long x;
    if (!(cin >> n >> x)) return 0;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    int ans = binarySearchDac(a, 0, n - 1, x);
    if (ans != -1) ans += 1;
    cout << ans << "\n";
    return 0;
}

```

### `CPPB-DAC-02` — Range Minimum Query Chia De Tri

```cpp
#include <bits/stdc++.h>
using namespace std;

long long queryMin(const vector<long long> &a, int l, int r) {
    if (l == r) return a[l];
    int mid = l + (r - l) / 2;
    return min(queryMin(a, l, mid), queryMin(a, mid + 1, r));
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    cout << queryMin(a, 0, n - 1) << "\n";
    return 0;
}

```

### `CPPB-DAC-03` — Tim Phan Tu Lon Thu Hai Tournament

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Node {
    long long winner;
    vector<long long> losers;
};

Node tournament(const vector<long long> &a, int l, int r) {
    if (l == r) return {a[l], {}};
    int mid = l + (r - l) / 2;
    Node left_node = tournament(a, l, mid);
    Node right_node = tournament(a, mid + 1, r);
    if (left_node.winner > right_node.winner) {
        left_node.losers.push_back(right_node.winner);
        return left_node;
    } else {
        right_node.losers.push_back(left_node.winner);
        return right_node;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    Node res = tournament(a, 0, n - 1);
    long long second_max = res.losers[0];
    for (long long x : res.losers) second_max = max(second_max, x);
    cout << second_max << "\n";
    return 0;
}

```

### `CPPB-DAC-04` — Gop Hai Mang Da Sap Xep Merge Step

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<long long> a(n), b(m);
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int j = 0; j < m; ++j) cin >> b[j];

    int i = 0, j = 0;
    bool first = true;
    while (i < n && j < m) {
        if (!first) cout << " ";
        if (a[i] <= b[j]) {
            cout << a[i++];
        } else {
            cout << b[j++];
        }
        first = false;
    }
    while (i < n) {
        if (!first) cout << " ";
        cout << a[i++];
        first = false;
    }
    while (j < m) {
        if (!first) cout << " ";
        cout << b[j++];
        first = false;
    }
    cout << "\n";
    return 0;
}

```

### `CPPB-DAC-05` — Sap Xep Tron Merge Sort

```cpp
#include <bits/stdc++.h>
using namespace std;

void merge(vector<long long> &a, vector<long long> &temp, int l, int mid, int r) {
    int i = l, j = mid + 1, k = l;
    while (i <= mid && j <= r) {
        if (a[i] <= a[j]) temp[k++] = a[i++];
        else temp[k++] = a[j++];
    }
    while (i <= mid) temp[k++] = a[i++];
    while (j <= r) temp[k++] = a[j++];
    for (int idx = l; idx <= r; ++idx) a[idx] = temp[idx];
}

void mergeSort(vector<long long> &a, vector<long long> &temp, int l, int r) {
    if (l >= r) return;
    int mid = l + (r - l) / 2;
    mergeSort(a, temp, l, mid);
    mergeSort(a, temp, mid + 1, r);
    merge(a, temp, l, mid, r);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<long long> a(n), temp(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    mergeSort(a, temp, 0, n - 1);
    for (int i = 0; i < n; ++i) cout << a[i] << (i + 1 == n ? "" : " ");
    cout << "\n";
    return 0;
}

```

### `CPPB-DAC-06` — Dem So Cap Nghich The Inversion

```cpp
#include <bits/stdc++.h>
using namespace std;

long long countInversions(vector<long long> &a, vector<long long> &temp, int l, int r) {
    if (l >= r) return 0;
    int mid = l + (r - l) / 2;
    long long inv = 0;
    inv += countInversions(a, temp, l, mid);
    inv += countInversions(a, temp, mid + 1, r);

    int i = l, j = mid + 1, k = l;
    while (i <= mid && j <= r) {
        if (a[i] <= a[j]) {
            temp[k++] = a[i++];
        } else {
            temp[k++] = a[j++];
            inv += (mid - i + 1);
        }
    }
    while (i <= mid) temp[k++] = a[i++];
    while (j <= r) temp[k++] = a[j++];
    for (int idx = l; idx <= r; ++idx) a[idx] = temp[idx];
    return inv;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<long long> a(n), temp(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    cout << countInversions(a, temp, 0, n - 1) << "\n";
    return 0;
}

```

### `CPPB-DAC-07` — Doan Con Tong Lon Nhat Maximum Subarray

```cpp
#include <bits/stdc++.h>
using namespace std;

long long maxCrossingSum(const vector<long long> &a, int l, int mid, int r) {
    long long left_sum = -1e18, sum = 0;
    for (int i = mid; i >= l; --i) {
        sum += a[i];
        left_sum = max(left_sum, sum);
    }
    long long right_sum = -1e18;
    sum = 0;
    for (int i = mid + 1; i <= r; ++i) {
        sum += a[i];
        right_sum = max(right_sum, sum);
    }
    return left_sum + right_sum;
}

long long maxSubarrayDac(const vector<long long> &a, int l, int r) {
    if (l == r) return a[l];
    int mid = l + (r - l) / 2;
    long long left_max = maxSubarrayDac(a, l, mid);
    long long right_max = maxSubarrayDac(a, mid + 1, r);
    long long cross_max = maxCrossingSum(a, l, mid, r);
    return max({left_max, right_max, cross_max});
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    cout << maxSubarrayDac(a, 0, n - 1) << "\n";
    return 0;
}

```

### `CPPB-DAC-08` — Tim Phan Tu Da So Majority Element

```cpp
#include <bits/stdc++.h>
using namespace std;

int countInRange(const vector<long long> &a, long long target, int l, int r) {
    int cnt = 0;
    for (int i = l; i <= r; ++i) if (a[i] == target) cnt++;
    return cnt;
}

long long majorityDac(const vector<long long> &a, int l, int r) {
    if (l == r) return a[l];
    int mid = l + (r - l) / 2;
    long long left_maj = majorityDac(a, l, mid);
    long long right_maj = majorityDac(a, mid + 1, r);

    if (left_maj == right_maj) return left_maj;

    int left_count = countInRange(a, left_maj, l, r);
    int right_count = countInRange(a, right_maj, l, r);

    return (left_count > right_count) ? left_maj : right_maj;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    long long cand = majorityDac(a, 0, n - 1);
    int total_cnt = 0;
    for (long long x : a) if (x == cand) total_cnt++;
    if (total_cnt > n / 2) {
        cout << cand << "\n";
    } else {
        cout << -1 << "\n";
    }
    return 0;
}

```

### `CPPB-DAC-09` — Luy Thua Ma Tran Chia De Tri

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Matrix {
    long long mat[2][2];
};

Matrix multiply(const Matrix &A, const Matrix &B, long long m) {
    Matrix C;
    for (int i = 0; i < 2; ++i) {
        for (int j = 0; j < 2; ++j) {
            C.mat[i][j] = 0;
            for (int k = 0; k < 2; ++k) {
                C.mat[i][j] = (C.mat[i][j] + (A.mat[i][k] % m) * (B.mat[k][j] % m)) % m;
            }
        }
    }
    return C;
}

Matrix powerMatrix(Matrix A, long long n, long long m) {
    Matrix res = {{{1 % m, 0}, {0, 1 % m}}};
    while (n > 0) {
        if (n & 1) res = multiply(res, A, m);
        A = multiply(A, A, m);
        n >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    Matrix A;
    if (!(cin >> A.mat[0][0] >> A.mat[0][1] >> A.mat[1][0] >> A.mat[1][1])) return 0;
    long long n, m;
    if (!(cin >> n >> m)) return 0;
    Matrix ans = powerMatrix(A, n, m);
    cout << ans.mat[0][0] << " " << ans.mat[0][1] << "\n";
    cout << ans.mat[1][0] << " " << ans.mat[1][1] << "\n";
    return 0;
}

```

### `CPPB-DAC-10` — Tim Dinh Mang Unimodal Peak Index

```cpp
#include <bits/stdc++.h>
using namespace std;

long long findPeak(const vector<long long> &a, int l, int r) {
    if (l == r) return a[l];
    int mid = l + (r - l) / 2;
    if (a[mid] < a[mid + 1]) {
        return findPeak(a, mid + 1, r);
    } else {
        return findPeak(a, l, mid);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    cout << findPeak(a, 0, n - 1) << "\n";
    return 0;
}

```

### `CPPB-DAC-11` — Tinh Tong Cap So Nhan Chia De Tri

```cpp
#include <bits/stdc++.h>
using namespace std;

long long powerMod(long long a, long long b, long long m) {
    long long res = 1 % m;
    a %= m;
    while (b > 0) {
        if (b & 1) res = (res * a) % m;
        a = (a * a) % m;
        b >>= 1;
    }
    return res;
}

long long sumGeoDac(long long a, long long n, long long m) {
    if (n == 0) return 1 % m;
    if (n % 2 == 1) {
        long long k = n / 2;
        long long half_sum = sumGeoDac(a, k, m);
        long long mult = (1 + powerMod(a, k + 1, m)) % m;
        return (half_sum * mult) % m;
    } else {
        long long prev = sumGeoDac(a, n - 1, m);
        return (prev + powerMod(a, n, m)) % m;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long a, n, m;
    if (!(cin >> a >> n >> m)) return 0;
    cout << sumGeoDac(a, n, m) << "\n";
    return 0;
}

```

### `CPPB-DAC-12` — Dem So Cap A I Lon Hon 2 A J

```cpp
#include <bits/stdc++.h>
using namespace std;

long long countSignificant(vector<long long> &a, vector<long long> &temp, int l, int r) {
    if (l >= r) return 0;
    int mid = l + (r - l) / 2;
    long long cnt = 0;
    cnt += countSignificant(a, temp, l, mid);
    cnt += countSignificant(a, temp, mid + 1, r);

    // Bước đếm 2 con trỏ trước khi merge
    int j = mid + 1;
    for (int i = l; i <= mid; ++i) {
        while (j <= r && a[i] > 2LL * a[j]) j++;
        cnt += (j - (mid + 1));
    }

    // Merge bình thường
    int i = l, k = l;
    j = mid + 1;
    while (i <= mid && j <= r) {
        if (a[i] <= a[j]) temp[k++] = a[i++];
        else temp[k++] = a[j++];
    }
    while (i <= mid) temp[k++] = a[i++];
    while (j <= r) temp[k++] = a[j++];
    for (int idx = l; idx <= r; ++idx) a[idx] = temp[idx];

    return cnt;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<long long> a(n), temp(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    cout << countSignificant(a, temp, 0, n - 1) << "\n";
    return 0;
}

```

### `CPPB-DAC-13` — Quickselect Tim Phan Tu Kth

```cpp
#include <bits/stdc++.h>
using namespace std;

int partition(vector<long long> &a, int l, int r) {
    int pivot_idx = l + rand() % (r - l + 1);
    swap(a[pivot_idx], a[r]);
    long long pivot = a[r];
    int i = l;
    for (int j = l; j < r; ++j) {
        if (a[j] <= pivot) {
            swap(a[i], a[j]);
            i++;
        }
    }
    swap(a[i], a[r]);
    return i;
}

long long quickSelect(vector<long long> &a, int l, int r, int k) {
    if (l == r) return a[l];
    int p = partition(a, l, r);
    int rank = p - l + 1;
    if (rank == k) return a[p];
    if (k < rank) return quickSelect(a, l, p - 1, k);
    return quickSelect(a, p + 1, r, k - rank);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    srand(42);
    int n, k;
    if (!(cin >> n >> k)) return 0;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    cout << quickSelect(a, 0, n - 1, k) << "\n";
    return 0;
}

```

### `CPPB-DAC-14` — Dem So Doan Con Tong Trong Khoang L R

```cpp
#include <bits/stdc++.h>
using namespace std;

long long countSubarraysDac(vector<long long> &prefix, vector<long long> &temp, int l, int r, long long lower, long long upper) {
    if (l >= r) return 0;
    int mid = l + (r - l) / 2;
    long long cnt = 0;
    cnt += countSubarraysDac(prefix, temp, l, mid, lower, upper);
    cnt += countSubarraysDac(prefix, temp, mid + 1, r, lower, upper);

    int j1 = mid + 1, j2 = mid + 1;
    for (int i = l; i <= mid; ++i) {
        while (j1 <= r && prefix[j1] - prefix[i] < lower) j1++;
        while (j2 <= r && prefix[j2] - prefix[i] <= upper) j2++;
        cnt += (j2 - j1);
    }

    int i = l, j = mid + 1, k = l;
    while (i <= mid && j <= r) {
        if (prefix[i] <= prefix[j]) temp[k++] = prefix[i++];
        else temp[k++] = prefix[j++];
    }
    while (i <= mid) temp[k++] = prefix[i++];
    while (j <= r) temp[k++] = prefix[j++];
    for (int idx = l; idx <= r; ++idx) prefix[idx] = temp[idx];

    return cnt;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    long long lower, upper;
    if (!(cin >> n >> lower >> upper)) return 0;
    vector<long long> a(n);
    vector<long long> prefix(n + 1, 0), temp(n + 1, 0);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        prefix[i + 1] = prefix[i] + a[i];
    }
    cout << countSubarraysDac(prefix, temp, 0, n, lower, upper) << "\n";
    return 0;
}

```

### `CPPB-DAC-15` — Cap Diem Gan Nhat Closest Pair

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Point {
    long long x, y;
};

long long distSq(const Point &p1, const Point &p2) {
    return (p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y);
}

long long closestPairRec(vector<Point> &pts, int l, int r) {
    if (r - l <= 3) {
        long long min_d = 4e18;
        for (int i = l; i <= r; ++i) {
            for (int j = i + 1; j <= r; ++j) {
                min_d = min(min_d, distSq(pts[i], pts[j]));
            }
        }
        sort(pts.begin() + l, pts.begin() + r + 1, [](const Point &a, const Point &b) {
            return a.y < b.y;
        });
        return min_d;
    }

    int mid = l + (r - l) / 2;
    long long mid_x = pts[mid].x;
    long long dl = closestPairRec(pts, l, mid);
    long long dr = closestPairRec(pts, mid + 1, r);
    long long d = min(dl, dr);

    vector<Point> temp(r - l + 1);
    merge(pts.begin() + l, pts.begin() + mid + 1, pts.begin() + mid + 1, pts.begin() + r + 1, temp.begin(), [](const Point &a, const Point &b) {
        return a.y < b.y;
    });
    for (int i = 0; i < (int)temp.size(); ++i) pts[l + i] = temp[i];

    vector<Point> strip;
    for (int i = l; i <= r; ++i) {
        if ((pts[i].x - mid_x) * (pts[i].x - mid_x) < d) {
            strip.push_back(pts[i]);
        }
    }

    for (int i = 0; i < (int)strip.size(); ++i) {
        for (int j = i + 1; j < (int)strip.size() && (strip[j].y - strip[i].y) * (strip[j].y - strip[i].y) < d; ++j) {
            d = min(d, distSq(strip[i], strip[j]));
        }
    }
    return d;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<Point> pts(n);
    for (int i = 0; i < n; ++i) cin >> pts[i].x >> pts[i].y;
    sort(pts.begin(), pts.end(), [](const Point &a, const Point &b) {
        return a.x < b.x;
    });
    cout << closestPairRec(pts, 0, n - 1) << "\n";
    return 0;
}

```

### `CPPB-DAC-16` — Median Hai Mang Da Sap Xep

```cpp
#include <bits/stdc++.h>
using namespace std;

long long findKth(const vector<long long> &A, int a_l, const vector<long long> &B, int b_l, int k) {
    if (a_l >= (int)A.size()) return B[b_l + k - 1];
    if (b_l >= (int)B.size()) return A[a_l + k - 1];
    if (k == 1) return min(A[a_l], B[b_l]);

    int a_mid = a_l + k / 2 - 1;
    int b_mid = b_l + k / 2 - 1;

    long long a_val = (a_mid < (int)A.size()) ? A[a_mid] : 2e18;
    long long b_val = (b_mid < (int)B.size()) ? B[b_mid] : 2e18;

    if (a_val <= b_val) {
        return findKth(A, a_l + k / 2, B, b_l, k - k / 2);
    } else {
        return findKth(A, a_l, B, b_l + k / 2, k - k / 2);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<long long> a(n), b(m);
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int j = 0; j < m; ++j) cin >> b[j];
    int total = n + m;
    int k = (total % 2 == 1) ? (total / 2 + 1) : (total / 2);
    cout << findKth(a, 0, b, 0, k) << "\n";
    return 0;
}

```

## Chương 04 — Bài 12: Quay lui & nhánh cận

### `CPPB-BKT-01` — Sinh Xau Nhi Phan

```cpp
#include <bits/stdc++.h>
using namespace std;

int n;
string cur = "";

void backtrack(int step) {
    if (step > n) {
        cout << cur << "\n";
        return;
    }
    for (char c : {'0', '1'}) {
        cur.push_back(c);
        backtrack(step + 1);
        cur.pop_back();
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> n)) return 0;
    backtrack(1);
    return 0;
}

```

### `CPPB-BKT-02` — Sinh Tap Con

```cpp
#include <bits/stdc++.h>
using namespace std;

int n;
vector<int> cur;

void backtrack(int step) {
    if (step > n) {
        for (int i = 0; i < (int)cur.size(); ++i) cout << cur[i] << (i + 1 == (int)cur.size() ? "" : " ");
        cout << "\n";
        return;
    }
    // Không chọn step
    backtrack(step + 1);
    // Chọn step
    cur.push_back(step);
    backtrack(step + 1);
    cur.pop_back();
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> n)) return 0;
    backtrack(1);
    return 0;
}

```

### `CPPB-BKT-03` — Sinh Hoan Vi

```cpp
#include <bits/stdc++.h>
using namespace std;

int n;
vector<int> cur;
vector<bool> visited;

void backtrack(int step) {
    if (step > n) {
        for (int i = 0; i < n; ++i) cout << cur[i] << (i + 1 == n ? "" : " ");
        cout << "\n";
        return;
    }
    for (int val = 1; val <= n; ++val) {
        if (!visited[val]) {
            visited[val] = true;
            cur.push_back(val);
            backtrack(step + 1);
            cur.pop_back();
            visited[val] = false;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> n)) return 0;
    visited.assign(n + 1, false);
    backtrack(1);
    return 0;
}

```

### `CPPB-BKT-04` — Sinh To Hop Chap K

```cpp
#include <bits/stdc++.h>
using namespace std;

int n, k;
vector<int> cur;

void backtrack(int step, int start_val) {
    if (step > k) {
        for (int i = 0; i < k; ++i) cout << cur[i] << (i + 1 == k ? "" : " ");
        cout << "\n";
        return;
    }
    for (int val = start_val; val <= n - (k - step); ++val) {
        cur.push_back(val);
        backtrack(step + 1, val + 1);
        cur.pop_back();
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> n >> k)) return 0;
    backtrack(1, 1);
    return 0;
}

```

### `CPPB-BKT-05` — Sinh Day Ngoac Dung

```cpp
#include <bits/stdc++.h>
using namespace std;

int n;
string cur = "";

void backtrack(int open_cnt, int close_cnt) {
    if (open_cnt == n && close_cnt == n) {
        cout << cur << "\n";
        return;
    }
    if (open_cnt < n) {
        cur.push_back('(');
        backtrack(open_cnt + 1, close_cnt);
        cur.pop_back();
    }
    if (close_cnt < open_cnt) {
        cur.push_back(')');
        backtrack(open_cnt, close_cnt + 1);
        cur.pop_back();
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> n)) return 0;
    backtrack(0, 0);
    return 0;
}

```

### `CPPB-BKT-06` — Bai Toan N Queens

```cpp
#include <bits/stdc++.h>
using namespace std;

int n;
long long ans = 0;
vector<bool> col_used, diag1, diag2;

void backtrack(int row) {
    if (row > n) {
        ans++;
        return;
    }
    for (int col = 1; col <= n; ++col) {
        if (!col_used[col] && !diag1[row - col + n] && !diag2[row + col]) {
            col_used[col] = diag1[row - col + n] = diag2[row + col] = true;
            backtrack(row + 1);
            col_used[col] = diag1[row - col + n] = diag2[row + col] = false;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> n)) return 0;
    col_used.assign(n + 1, false);
    diag1.assign(2 * n + 1, false);
    diag2.assign(2 * n + 1, false);
    backtrack(1);
    cout << ans << "\n";
    return 0;
}

```

### `CPPB-BKT-07` — Me Cung Rat In A Maze

```cpp
#include <bits/stdc++.h>
using namespace std;

int n;
int a[10][10];
bool visited[10][10];
vector<string> paths;
string cur = "";

int dx[] = {1, 0, 0, -1};
int dy[] = {0, -1, 1, 0};
char step_char[] = {'D', 'L', 'R', 'U'};

void backtrack(int x, int y) {
    if (x == n - 1 && y == n - 1) {
        paths.push_back(cur);
        return;
    }
    for (int i = 0; i < 4; ++i) {
        int nx = x + dx[i], ny = y + dy[i];
        if (nx >= 0 && nx < n && ny >= 0 && ny < n && a[nx][ny] == 1 && !visited[nx][ny]) {
            visited[nx][ny] = true;
            cur.push_back(step_char[i]);
            backtrack(nx, ny);
            cur.pop_back();
            visited[nx][ny] = false;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> n)) return 0;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j) cin >> a[i][j];

    if (a[0][0] == 1) {
        visited[0][0] = true;
        backtrack(0, 0);
    }
    if (paths.empty()) {
        cout << -1 << "\n";
    } else {
        for (const string &s : paths) cout << s << "\n";
    }
    return 0;
}

```

### `CPPB-BKT-08` — Tap Con Tong Bang S Subset Sum

```cpp
#include <bits/stdc++.h>
using namespace std;

int n;
long long S;
vector<long long> a;
vector<long long> cur;
bool found = false;

void backtrack(int idx, long long current_sum) {
    if (current_sum == S) {
        found = true;
        for (int i = 0; i < (int)cur.size(); ++i) cout << cur[i] << (i + 1 == (int)cur.size() ? "" : " ");
        cout << "\n";
        return;
    }
    if (idx >= n || current_sum > S) return;

    for (int i = idx; i < n; ++i) {
        if (current_sum + a[i] <= S) {
            cur.push_back(a[i]);
            backtrack(i + 1, current_sum + a[i]);
            cur.pop_back();
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> n >> S)) return 0;
    a.resize(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    sort(a.begin(), a.end());
    backtrack(0, 0);
    if (!found) cout << -1 << "\n";
    return 0;
}

```

### `CPPB-BKT-09` — Chia Tap Hai Phan Bang Nhau

```cpp
#include <bits/stdc++.h>
using namespace std;

int n;
long long target;
vector<long long> a;
bool possible = false;

void backtrack(int idx, long long cur_sum) {
    if (possible) return;
    if (cur_sum == target) {
        possible = true;
        return;
    }
    if (idx >= n || cur_sum > target) return;

    for (int i = idx; i < n; ++i) {
        if (cur_sum + a[i] <= target) {
            backtrack(i + 1, cur_sum + a[i]);
            if (possible) return;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> n)) return 0;
    a.resize(n);
    long long total = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        total += a[i];
    }
    if (total % 2 != 0) {
        cout << "NO\n";
        return 0;
    }
    target = total / 2;
    sort(a.rbegin(), a.rend());
    backtrack(0, 0);
    cout << (possible ? "YES\n" : "NO\n");
    return 0;
}

```

### `CPPB-BKT-10` — Doi Tien Xu It Nhat Branch And Bound

```cpp
#include <bits/stdc++.h>
using namespace std;

int n;
long long S;
vector<long long> c;
long long best_coins = 1e9;

void branchAndBound(int idx, long long remain, long long count) {
    // Optimality Pruning
    if (count + (remain + c[0] - 1) / c[0] >= best_coins) return;

    if (remain == 0) {
        best_coins = min(best_coins, count);
        return;
    }
    if (idx >= n) return;

    long long max_use = remain / c[idx];
    for (long long k = max_use; k >= 0; --k) {
        if (count + k + (remain - k * c[idx] + c[0] - 1) / c[0] < best_coins) {
            branchAndBound(idx + 1, remain - k * c[idx], count + k);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> n >> S)) return 0;
    c.resize(n);
    for (int i = 0; i < n; ++i) cin >> c[i];
    sort(c.rbegin(), c.rend());
    branchAndBound(0, S, 0);
    if (best_coins > 1e8) cout << -1 << "\n";
    else cout << best_coins << "\n";
    return 0;
}

```

### `CPPB-BKT-11` — Ma Di Tuan Knights Tour

```cpp
#include <bits/stdc++.h>
using namespace std;

int n;
int board[10][10];
int dx[] = {-2, -2, -1, -1, 1, 1, 2, 2};
int dy[] = {-1, 1, -2, 2, -2, 2, -1, 1};
bool found = false;

int countDegree(int x, int y) {
    int deg = 0;
    for (int i = 0; i < 8; ++i) {
        int nx = x + dx[i], ny = y + dy[i];
        if (nx >= 1 && nx <= n && ny >= 1 && ny <= n && board[nx][ny] == 0) deg++;
    }
    return deg;
}

void solveKnight(int x, int y, int step) {
    if (step == n * n) {
        found = true;
        return;
    }

    vector<pair<int, int>> next_moves;
    for (int i = 0; i < 8; ++i) {
        int nx = x + dx[i], ny = y + dy[i];
        if (nx >= 1 && nx <= n && ny >= 1 && ny <= n && board[nx][ny] == 0) {
            next_moves.push_back({countDegree(nx, ny), i});
        }
    }
    sort(next_moves.begin(), next_moves.end());

    for (auto &p : next_moves) {
        int idx = p.second;
        int nx = x + dx[idx], ny = y + dy[idx];
        board[nx][ny] = step + 1;
        solveKnight(nx, ny, step + 1);
        if (found) return;
        board[nx][ny] = 0;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int r, c;
    if (!(cin >> n >> r >> c)) return 0;
    memset(board, 0, sizeof(board));
    board[r][c] = 1;
    solveKnight(r, c, 1);
    if (!found) {
        cout << -1 << "\n";
    } else {
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                cout << board[i][j] << (j == n ? "" : " ");
            }
            cout << "\n";
        }
    }
    return 0;
}

```

### `CPPB-BKT-12` — Tro Choi Sudoku 9x9

```cpp
#include <bits/stdc++.h>
using namespace std;

int board[9][9];
bool row_used[9][10], col_used[9][10], box_used[9][10];

bool solveSudoku(int r, int c) {
    if (r == 9) return true;
    if (c == 9) return solveSudoku(r + 1, 0);
    if (board[r][c] != 0) return solveSudoku(r, c + 1);

    int b = (r / 3) * 3 + (c / 3);
    for (int num = 1; num <= 9; ++num) {
        if (!row_used[r][num] && !col_used[c][num] && !box_used[b][num]) {
            board[r][c] = num;
            row_used[r][num] = col_used[c][num] = box_used[b][num] = true;
            if (solveSudoku(r, c + 1)) return true;
            row_used[r][num] = col_used[c][num] = box_used[b][num] = false;
            board[r][c] = 0;
        }
    }
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    for (int i = 0; i < 9; ++i) {
        for (int j = 0; j < 9; ++j) {
            if (!(cin >> board[i][j])) return 0;
            int num = board[i][j];
            if (num != 0) {
                row_used[i][num] = col_used[j][num] = box_used[(i / 3) * 3 + (j / 3)][num] = true;
            }
        }
    }
    solveSudoku(0, 0);
    for (int i = 0; i < 9; ++i) {
        for (int j = 0; j < 9; ++j) {
            cout << board[i][j] << (j == 8 ? "" : " ");
        }
        cout << "\n";
    }
    return 0;
}

```

### `CPPB-BKT-13` — Cai Tui 01 Nhanh Can Knapsack

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Item {
    long long w, v;
    double ratio;
};

int n;
long long max_w;
vector<Item> items;
long long best_val = 0;

double getUpperBound(int idx, long long cur_w, long long cur_v) {
    long long remain_w = max_w - cur_w;
    double bound = cur_v;
    for (int i = idx; i < n; ++i) {
        if (items[i].w <= remain_w) {
            remain_w -= items[i].w;
            bound += items[i].v;
        } else {
            bound += items[i].ratio * remain_w;
            break;
        }
    }
    return bound;
}

void branchAndBound(int idx, long long cur_w, long long cur_v) {
    if (cur_v > best_val) best_val = cur_v;
    if (idx >= n) return;

    if (getUpperBound(idx, cur_w, cur_v) <= best_val) return;

    // Nhánh 1: Chọn vật idx
    if (cur_w + items[idx].w <= max_w) {
        branchAndBound(idx + 1, cur_w + items[idx].w, cur_v + items[idx].v);
    }
    // Nhánh 2: Không chọn vật idx
    branchAndBound(idx + 1, cur_w, cur_v);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> n >> max_w)) return 0;
    items.resize(n);
    for (int i = 0; i < n; ++i) {
        cin >> items[i].w >> items[i].v;
        items[i].ratio = (double)items[i].v / items[i].w;
    }
    sort(items.begin(), items.end(), [](const Item &a, const Item &b) {
        return a.ratio > b.ratio;
    });
    branchAndBound(0, 0, 0);
    cout << best_val << "\n";
    return 0;
}

```

### `CPPB-BKT-14` — Nguoi Du Lich Tsp Nhanh Can

```cpp
#include <bits/stdc++.h>
using namespace std;

int n;
long long c[15][15];
bool visited[15];
long long min_edge = 1e9;
long long best_cost = 1e18;

void branchAndBound(int u, int count, long long current_cost) {
    // Optimality Pruning
    if (current_cost + (n - count + 1) * min_edge >= best_cost) return;

    if (count == n) {
        best_cost = min(best_cost, current_cost + c[u][1]);
        return;
    }

    for (int v = 2; v <= n; ++v) {
        if (!visited[v]) {
            visited[v] = true;
            branchAndBound(v, count + 1, current_cost + c[u][v]);
            visited[v] = false;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> n)) return 0;
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j) {
            cin >> c[i][j];
            if (i != j) min_edge = min(min_edge, c[i][j]);
        }
    }
    memset(visited, false, sizeof(visited));
    visited[1] = true;
    branchAndBound(1, 1, 0);
    cout << best_cost << "\n";
    return 0;
}

```

### `CPPB-BKT-15` — To Mau Do Thi Graph Coloring

```cpp
#include <bits/stdc++.h>
using namespace std;

int V, E, K;
vector<int> adj[15];
int color[15];
bool possible = false;

bool isSafe(int u, int c) {
    for (int v : adj[u]) {
        if (color[v] == c) return false;
    }
    return true;
}

void backtrack(int u) {
    if (possible) return;
    if (u > V) {
        possible = true;
        return;
    }
    for (int c = 1; c <= K; ++c) {
        if (isSafe(u, c)) {
            color[u] = c;
            backtrack(u + 1);
            color[u] = 0;
            if (possible) return;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> V >> E >> K)) return 0;
    for (int i = 0; i < E; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    memset(color, 0, sizeof(color));
    backtrack(1);
    cout << (possible ? "YES\n" : "NO\n");
    return 0;
}

```

### `CPPB-BKT-16` — Phan Cong Cong Viec Toi Uu Job Assignment

```cpp
#include <bits/stdc++.h>
using namespace std;

int n;
long long c[15][15];
bool job_assigned[15];
long long min_row[15];
long long best_cost = 1e18;

void branchAndBound(int worker, long long current_cost) {
    // Optimality Pruning
    long long bound = current_cost;
    for (int w = worker; w <= n; ++w) bound += min_row[w];
    if (bound >= best_cost) return;

    if (worker > n) {
        best_cost = min(best_cost, current_cost);
        return;
    }

    for (int job = 1; job <= n; ++job) {
        if (!job_assigned[job]) {
            job_assigned[job] = true;
            branchAndBound(worker + 1, current_cost + c[worker][job]);
            job_assigned[job] = false;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> n)) return 0;
    for (int i = 1; i <= n; ++i) {
        min_row[i] = 1e9;
        for (int j = 1; j <= n; ++j) {
            cin >> c[i][j];
            min_row[i] = min(min_row[i], c[i][j]);
        }
    }
    memset(job_assigned, false, sizeof(job_assigned));
    branchAndBound(1, 0);
    cout << best_cost << "\n";
    return 0;
}

```

## Chương 05 — Bài 13: QHĐ 1D & LIS

### `CPPB-DP1-01` — Bac Thang Co Ban

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MOD = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    if (n == 1) { cout << 1 << "\n"; return 0; }
    if (n == 2) { cout << 2 << "\n"; return 0; }

    int prev2 = 1, prev1 = 2, cur = 0;
    for (int i = 3; i <= n; ++i) {
        cur = (prev1 + prev2) % MOD;
        prev2 = prev1;
        prev1 = cur;
    }

    cout << cur << "\n";
    return 0;
}

```

### `CPPB-DP1-02` — Chu Ech Nhay Cost

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    vector<long long> h(n);
    for (int i = 0; i < n; ++i) cin >> h[i];

    if (n == 1) { cout << 0 << "\n"; return 0; }

    vector<long long> dp(n, 0);
    dp[0] = 0;
    dp[1] = abs(h[1] - h[0]);

    for (int i = 2; i < n; ++i) {
        dp[i] = min(dp[i - 1] + abs(h[i] - h[i - 1]),
                    dp[i - 2] + abs(h[i] - h[i - 2]));
    }

    cout << dp[n - 1] << "\n";
    return 0;
}

```

### `CPPB-DP1-03` — Chu Ech Nhay K Buoc

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long INF = 1e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;
    if (n <= 0) return 0;

    vector<long long> h(n);
    for (int i = 0; i < n; ++i) cin >> h[i];

    vector<long long> dp(n, INF);
    dp[0] = 0;

    for (int i = 0; i < n; ++i) {
        for (int j = 1; j <= k && i + j < n; ++j) {
            dp[i + j] = min(dp[i + j], dp[i] + abs(h[i] - h[i + j]));
        }
    }

    cout << dp[n - 1] << "\n";
    return 0;
}

```

### `CPPB-DP1-04` — Doi Tien Xu It Nhat

```cpp
#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, s;
    if (!(cin >> n >> s)) return 0;
    if (n <= 0 || s < 0) return 0;

    vector<int> c(n);
    for (int i = 0; i < n; ++i) cin >> c[i];

    vector<int> dp(s + 1, INF);
    dp[0] = 0;

    for (int i = 1; i <= s; ++i) {
        for (int coin : c) {
            if (i >= coin && dp[i - coin] != INF) {
                dp[i] = min(dp[i], dp[i - coin] + 1);
            }
        }
    }

    if (dp[s] == INF) cout << -1 << "\n";
    else cout << dp[s] << "\n";
    return 0;
}

```

### `CPPB-DP1-05` — Dem So Cach Doi Tien

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MOD = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, s;
    if (!(cin >> n >> s)) return 0;
    if (n <= 0 || s < 0) return 0;

    vector<int> c(n);
    for (int i = 0; i < n; ++i) cin >> c[i];

    vector<int> dp(s + 1, 0);
    dp[0] = 1;

    for (int coin : c) {
        for (int i = coin; i <= s; ++i) {
            dp[i] = (dp[i] + dp[i - coin]) % MOD;
        }
    }

    cout << dp[s] << "\n";
    return 0;
}

```

### `CPPB-DP1-06` — Tong Doan Con Khong Lien Ke

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    if (n == 1) { cout << a[0] << "\n"; return 0; }

    long long prev2 = a[0];
    long long prev1 = max(a[0], a[1]);
    long long cur = prev1;

    for (int i = 2; i < n; ++i) {
        cur = max(prev1, prev2 + a[i]);
        prev2 = prev1;
        prev1 = cur;
    }

    cout << cur << "\n";
    return 0;
}

```

### `CPPB-DP1-07` — Lat Gach 2xn

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MOD = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    if (n == 1) { cout << 1 << "\n"; return 0; }
    if (n == 2) { cout << 2 << "\n"; return 0; }

    int p2 = 1, p1 = 2, cur = 0;
    for (int i = 3; i <= n; ++i) {
        cur = (p1 + p2) % MOD;
        p2 = p1;
        p1 = cur;
    }

    cout << cur << "\n";
    return 0;
}

```

### `CPPB-DP1-08` — Lat Gach 3xn

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MOD = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    if (n % 2 != 0) {
        cout << 0 << "\n";
        return 0;
    }

    vector<long long> a(n + 1, 0), b(n + 1, 0);
    a[0] = 1;
    b[0] = 0;
    if (n >= 1) b[1] = 1;

    for (int i = 2; i <= n; ++i) {
        a[i] = (a[i - 2] + 2LL * b[i - 1]) % MOD;
        b[i] = (a[i - 1] + b[i - 2]) % MOD;
    }

    cout << a[n] << "\n";
    return 0;
}

```

### `CPPB-DP1-09` — Day Con Tang Dai Nhat Lis N2

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<int> dp(n, 1);
    int ans = 1;

    for (int i = 1; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
            if (a[j] < a[i]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
        ans = max(ans, dp[i]);
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB-DP1-10` — Day Con Tang Dai Nhat Lis Nlogn

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<long long> tails;
    for (int i = 0; i < n; ++i) {
        auto it = lower_bound(tails.begin(), tails.end(), a[i]);
        if (it == tails.end()) {
            tails.push_back(a[i]);
        } else {
            *it = a[i];
        }
    }

    cout << tails.size() << "\n";
    return 0;
}

```

### `CPPB-DP1-11` — Truy Vet Day Con Tang Dai Nhat

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<int> dp(n, 1);
    vector<int> parent(n, -1);
    int max_len = 1;
    int best_end = 0;

    for (int i = 1; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
            if (a[j] < a[i] && dp[j] + 1 > dp[i]) {
                dp[i] = dp[j] + 1;
                parent[i] = j;
            }
        }
        if (dp[i] > max_len) {
            max_len = dp[i];
            best_end = i;
        }
    }

    vector<long long> lis;
    int curr = best_end;
    while (curr != -1) {
        lis.push_back(a[curr]);
        curr = parent[curr];
    }
    reverse(lis.begin(), lis.end());

    cout << max_len << "\n";
    for (int i = 0; i < (int)lis.size(); ++i) {
        cout << lis[i] << (i + 1 == (int)lis.size() ? "" : " ");
    }
    cout << "\n";
    return 0;
}

```

### `CPPB-DP1-12` — Day Con Giam Dai Nhat

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        a[i] = -a[i]; // Đảo dấu để tìm LIS tương đương LDS
    }

    vector<long long> tails;
    for (int i = 0; i < n; ++i) {
        auto it = lower_bound(tails.begin(), tails.end(), a[i]);
        if (it == tails.end()) {
            tails.push_back(a[i]);
        } else {
            *it = a[i];
        }
    }

    cout << tails.size() << "\n";
    return 0;
}

```

### `CPPB-DP1-13` — Day Con Hinh Song Nui Bitonic

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    // LIS từ trái sang phải
    vector<int> inc(n, 1);
    for (int i = 1; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
            if (a[j] < a[i]) inc[i] = max(inc[i], inc[j] + 1);
        }
    }

    // LDS từ phải sang trái
    vector<int> dec(n, 1);
    for (int i = n - 2; i >= 0; --i) {
        for (int j = n - 1; j > i; --j) {
            if (a[j] < a[i]) dec[i] = max(dec[i], dec[j] + 1);
        }
    }

    int max_bitonic = 0;
    for (int i = 0; i < n; ++i) {
        max_bitonic = max(max_bitonic, inc[i] + dec[i] - 1);
    }

    cout << max_bitonic << "\n";
    return 0;
}

```

### `CPPB-DP1-14` — Tong Day Con Tang Lon Nhat

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<long long> dp(n);
    long long ans = 0;

    for (int i = 0; i < n; ++i) {
        dp[i] = a[i];
        for (int j = 0; j < i; ++j) {
            if (a[j] < a[i]) {
                dp[i] = max(dp[i], dp[j] + a[i]);
            }
        }
        ans = max(ans, dp[i]);
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB-DP1-15` — Quy Hoach Dong 1d Cuc Han

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Item {
    long long v, c;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    vector<Item> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i].v >> a[i].c;
    }

    // Sắp xếp theo v tăng dần
    sort(a.begin(), a.end(), [](const Item& x, const Item& y) {
        if (x.v != y.v) return x.v < y.v;
        return x.c > y.c;
    });

    vector<long long> dp(n);
    long long ans = 0;

    for (int i = 0; i < n; ++i) {
        dp[i] = a[i].c;
        for (int j = 0; j < i; ++j) {
            if (a[j].v < a[i].v) {
                dp[i] = max(dp[i], dp[j] + a[i].c);
            }
        }
        ans = max(ans, dp[i]);
    }

    cout << ans << "\n";
    return 0;
}

```

## Chương 05 — Bài 14: QHĐ 2D & Knapsack

### `CPPB-DP2-01` — Duong Di Tren Luoi So Cach

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MOD = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    if (n <= 0 || m <= 0) return 0;

    vector<int> dp(m, 1);
    for (int i = 1; i < n; ++i) {
        for (int j = 1; j < m; ++j) {
            dp[j] = (dp[j] + dp[j - 1]) % MOD;
        }
    }

    cout << dp[m - 1] << "\n";
    return 0;
}

```

### `CPPB-DP2-02` — Duong Di Tren Luoi Co Vat Can

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MOD = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    if (n <= 0 || m <= 0) return 0;

    vector<string> grid(n);
    for (int i = 0; i < n; ++i) cin >> grid[i];

    if (grid[0][0] == '#' || grid[n - 1][m - 1] == '#') {
        cout << 0 << "\n";
        return 0;
    }

    vector<int> dp(m, 0);
    dp[0] = 1;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (grid[i][j] == '#') {
                dp[j] = 0;
            } else if (j > 0) {
                dp[j] = (dp[j] + dp[j - 1]) % MOD;
            }
        }
    }

    cout << dp[m - 1] << "\n";
    return 0;
}

```

### `CPPB-DP2-03` — Duong Di Chi Phi Nho Nhat Grid

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long INF = 1e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    if (n <= 0 || m <= 0) return 0;

    vector<vector<long long>> a(n, vector<long long>(m));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) cin >> a[i][j];
    }

    vector<long long> dp(m, INF);
    dp[0] = a[0][0];

    for (int j = 1; j < m; ++j) dp[j] = dp[j - 1] + a[0][j];

    for (int i = 1; i < n; ++i) {
        dp[0] += a[i][0];
        for (int j = 1; j < m; ++j) {
            dp[j] = min(dp[j], dp[j - 1]) + a[i][j];
        }
    }

    cout << dp[m - 1] << "\n";
    return 0;
}

```

### `CPPB-DP2-04` — Duong Di Tong Lon Nhat Grid

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    if (n <= 0 || m <= 0) return 0;

    vector<vector<long long>> a(n, vector<long long>(m));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) cin >> a[i][j];
    }

    vector<long long> dp(m, 0);
    dp[0] = a[0][0];

    for (int j = 1; j < m; ++j) dp[j] = dp[j - 1] + a[0][j];

    for (int i = 1; i < n; ++i) {
        dp[0] += a[i][0];
        for (int j = 1; j < m; ++j) {
            dp[j] = max(dp[j], dp[j - 1]) + a[i][j];
        }
    }

    cout << dp[m - 1] << "\n";
    return 0;
}

```

### `CPPB-DP2-05` — Cai Tui 01 Knapsack Co Ban

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, w;
    if (!(cin >> n >> w)) return 0;
    if (n <= 0 || w <= 0) return 0;

    vector<long long> dp(w + 1, 0);

    for (int i = 0; i < n; ++i) {
        long long weight, val;
        cin >> weight >> val;
        for (int j = w; j >= weight; --j) {
            dp[j] = max(dp[j], dp[j - weight] + val);
        }
    }

    long long ans = 0;
    for (int j = 0; j <= w; ++j) ans = max(ans, dp[j]);
    cout << ans << "\n";
    return 0;
}

```

### `CPPB-DP2-06` — Cai Tui Khong Gioi Han Unbounded

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, w;
    if (!(cin >> n >> w)) return 0;
    if (n <= 0 || w <= 0) return 0;

    vector<long long> dp(w + 1, 0);

    for (int i = 0; i < n; ++i) {
        long long weight, val;
        cin >> weight >> val;
        for (int j = weight; j <= w; ++j) {
            dp[j] = max(dp[j], dp[j - weight] + val);
        }
    }

    cout << dp[w] << "\n";
    return 0;
}

```

### `CPPB-DP2-07` — Cai Tui Truy Vet Mon Do

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, w;
    if (!(cin >> n >> w)) return 0;
    if (n <= 0 || w <= 0) return 0;

    vector<long long> weight(n + 1), val(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> weight[i] >> val[i];
    }

    vector<vector<long long>> dp(n + 1, vector<long long>(w + 1, 0));

    for (int i = 1; i <= n; ++i) {
        for (int j = 0; j <= w; ++j) {
            dp[i][j] = dp[i - 1][j];
            if (j >= weight[i]) {
                dp[i][j] = max(dp[i][j], dp[i - 1][j - weight[i]] + val[i]);
            }
        }
    }

    // Truy vết các món đồ được chọn
    vector<int> chosen;
    int curr_w = w;
    for (int i = n; i >= 1; --i) {
        if (curr_w >= weight[i] && dp[i][curr_w] == dp[i - 1][curr_w - weight[i]] + val[i]) {
            chosen.push_back(i);
            curr_w -= weight[i];
        }
    }
    reverse(chosen.begin(), chosen.end());

    cout << dp[n][w] << "\n";
    cout << chosen.size() << "\n";
    for (int i = 0; i < (int)chosen.size(); ++i) {
        cout << chosen[i] << (i + 1 == (int)chosen.size() ? "" : " ");
    }
    cout << "\n";
    return 0;
}

```

### `CPPB-DP2-08` — Chia Tap Hai Phan Bang Nhau

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    vector<int> a(n);
    int total_sum = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        total_sum += a[i];
    }

    if (total_sum % 2 != 0) {
        cout << "NO\n";
        return 0;
    }

    int target = total_sum / 2;
    vector<bool> dp(target + 1, false);
    dp[0] = true;

    for (int x : a) {
        for (int j = target; j >= x; --j) {
            if (dp[j - x]) dp[j] = true;
        }
    }

    if (dp[target]) cout << "YES\n";
    else cout << "NO\n";
    return 0;
}

```

### `CPPB-DP2-09` — Chia Tap Chenh Lech Nho Nhat

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    vector<int> a(n);
    int total_sum = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        total_sum += a[i];
    }

    int half = total_sum / 2;
    vector<bool> dp(half + 1, false);
    dp[0] = true;

    for (int x : a) {
        for (int j = half; j >= x; --j) {
            if (dp[j - x]) dp[j] = true;
        }
    }

    int best_s1 = 0;
    for (int j = half; j >= 0; --j) {
        if (dp[j]) {
            best_s1 = j;
            break;
        }
    }

    int min_diff = total_sum - 2 * best_s1;
    cout << min_diff << "\n";
    return 0;
}

```

### `CPPB-DP2-10` — Tam Giac So Tong Lon Nhat

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    vector<vector<long long>> a(n, vector<long long>(n, 0));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j <= i; ++j) {
            cin >> a[i][j];
        }
    }

    // Quy hoạch động từ đáy tam giác lên đỉnh
    for (int i = n - 2; i >= 0; --i) {
        for (int j = 0; j <= i; ++j) {
            a[i][j] += max(a[i + 1][j], a[i + 1][j + 1]);
        }
    }

    cout << a[0][0] << "\n";
    return 0;
}

```

### `CPPB-DP2-11` — Dem So Tap Con Tong Bang S

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MOD = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, s;
    if (!(cin >> n >> s)) return 0;
    if (n <= 0 || s < 0) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<int> dp(s + 1, 0);
    dp[0] = 1;

    for (int x : a) {
        for (int j = s; j >= x; --j) {
            dp[j] = (dp[j] + dp[j - x]) % MOD;
        }
    }

    cout << dp[s] << "\n";
    return 0;
}

```

### `CPPB-DP2-12` — Cai Tui Gia Tri Lon Doi Truc Dp

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long INF = 1e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long w;
    if (!(cin >> n >> w)) return 0;
    if (n <= 0 || w <= 0) return 0;

    vector<long long> weight(n), val(n);
    int max_v = 0;
    for (int i = 0; i < n; ++i) {
        cin >> weight[i] >> val[i];
        max_v += val[i];
    }

    // Đổi trục: dp[v] = khối lượng nhỏ nhất để đạt được tổng giá trị v
    vector<long long> dp(max_v + 1, INF);
    dp[0] = 0;

    for (int i = 0; i < n; ++i) {
        for (int v = max_v; v >= val[i]; --v) {
            if (dp[v - val[i]] != INF) {
                dp[v] = min(dp[v], dp[v - val[i]] + weight[i]);
            }
        }
    }

    long long ans = 0;
    for (int v = max_v; v >= 0; --v) {
        if (dp[v] <= w) {
            ans = v;
            break;
        }
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB-DP2-13` — Hinh Vuong Toan Mot Lon Nhat

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    if (n <= 0 || m <= 0) return 0;

    vector<string> grid(n);
    for (int i = 0; i < n; ++i) cin >> grid[i];

    vector<vector<int>> dp(n, vector<int>(m, 0));
    int max_side = 0;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (grid[i][j] == '1') {
                if (i == 0 || j == 0) {
                    dp[i][j] = 1;
                } else {
                    dp[i][j] = min({dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]}) + 1;
                }
                max_side = max(max_side, dp[i][j]);
            }
        }
    }

    cout << max_side * max_side << "\n";
    return 0;
}

```

### `CPPB-DP2-14` — Dong Tien Xu Gioi Han So Luong

```cpp
#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, s;
    if (!(cin >> n >> s)) return 0;
    if (n <= 0 || s < 0) return 0;

    vector<int> dp(s + 1, INF);
    dp[0] = 0;

    for (int i = 0; i < n; ++i) {
        int v, c;
        cin >> v >> c;
        // Phân rã nhị phân số lượng c thành 1, 2, 4, ...
        int k = 1;
        while (c > 0) {
            int take = min(k, c);
            int weight = take * v;
            int coins = take;

            for (int j = s; j >= weight; --j) {
                if (dp[j - weight] != INF) {
                    dp[j] = min(dp[j], dp[j - weight] + coins);
                }
            }

            c -= take;
            k *= 2;
        }
    }

    if (dp[s] == INF) cout << -1 << "\n";
    else cout << dp[s] << "\n";
    return 0;
}

```

### `CPPB-DP2-15` — Quy Hoach Dong 2d Cuc Han

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, w;
    if (!(cin >> n >> w)) return 0;
    if (n <= 0 || w <= 0) return 0;

    vector<long long> dp(w + 1, 0);

    for (int i = 0; i < n; ++i) {
        int type;
        long long weight, val;
        cin >> type >> weight >> val;

        if (type == 1) { // 0/1 Knapsack: duyệt ngược
            for (int j = w; j >= weight; --j) {
                dp[j] = max(dp[j], dp[j - weight] + val);
            }
        } else { // Unbounded Knapsack: duyệt xuôi
            for (int j = weight; j <= w; ++j) {
                dp[j] = max(dp[j], dp[j - weight] + val);
            }
        }
    }

    long long ans = 0;
    for (int j = 0; j <= w; ++j) ans = max(ans, dp[j]);
    cout << ans << "\n";
    return 0;
}

```

## Chương 05 — Bài 15: QHĐ chuỗi & LCS

### `CPPB-DPS-01` — Xau Con Chung Dai Nhat Lcs Co Ban

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s, t;
    if (!(cin >> s >> t)) return 0;

    int n = s.size(), m = t.size();
    vector<int> prev_row(m + 1, 0), curr_row(m + 1, 0);

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (s[i - 1] == t[j - 1]) {
                curr_row[j] = prev_row[j - 1] + 1;
            } else {
                curr_row[j] = max(prev_row[j], curr_row[j - 1]);
            }
        }
        prev_row = curr_row;
    }

    cout << prev_row[m] << "\n";
    return 0;
}

```

### `CPPB-DPS-02` — Truy Vet Xau Con Chung Dai Nhat

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s, t;
    if (!(cin >> s >> t)) return 0;

    int n = s.size(), m = t.size();
    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (s[i - 1] == t[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }

    // Truy vết
    string lcs = "";
    int i = n, j = m;
    while (i > 0 && j > 0) {
        if (s[i - 1] == t[j - 1]) {
            lcs += s[i - 1];
            --i; --j;
        } else if (dp[i - 1][j] >= dp[i][j - 1]) {
            --i;
        } else {
            --j;
        }
    }
    reverse(lcs.begin(), lcs.end());

    cout << dp[n][m] << "\n";
    cout << lcs << "\n";
    return 0;
}

```

### `CPPB-DPS-03` — Khoang Cach Chinh Sua Edit Distance

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s, t;
    if (!(cin >> s >> t)) return 0;

    int n = s.size(), m = t.size();
    vector<int> prev_row(m + 1), curr_row(m + 1);

    for (int j = 0; j <= m; ++j) prev_row[j] = j;

    for (int i = 1; i <= n; ++i) {
        curr_row[0] = i;
        for (int j = 1; j <= m; ++j) {
            if (s[i - 1] == t[j - 1]) {
                curr_row[j] = prev_row[j - 1];
            } else {
                curr_row[j] = 1 + min({prev_row[j], curr_row[j - 1], prev_row[j - 1]});
            }
        }
        prev_row = curr_row;
    }

    cout << prev_row[m] << "\n";
    return 0;
}

```

### `CPPB-DPS-04` — Bien Doi Xau It Phep Toan Nhat

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s, t;
    if (!(cin >> s >> t)) return 0;

    int n = s.size(), m = t.size();
    vector<int> prev_row(m + 1, 0), curr_row(m + 1, 0);

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (s[i - 1] == t[j - 1]) {
                curr_row[j] = prev_row[j - 1] + 1;
            } else {
                curr_row[j] = max(prev_row[j], curr_row[j - 1]);
            }
        }
        prev_row = curr_row;
    }

    int lcs = prev_row[m];
    int min_deletions = (n - lcs) + (m - lcs);
    cout << min_deletions << "\n";
    return 0;
}

```

### `CPPB-DPS-05` — Xau Con Doi Xung Dai Nhat Lps

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    int n = s.size();
    string t = s;
    reverse(t.begin(), t.end());

    vector<int> prev_row(n + 1, 0), curr_row(n + 1, 0);

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j) {
            if (s[i - 1] == t[j - 1]) {
                curr_row[j] = prev_row[j - 1] + 1;
            } else {
                curr_row[j] = max(prev_row[j], curr_row[j - 1]);
            }
        }
        prev_row = curr_row;
    }

    cout << prev_row[n] << "\n";
    return 0;
}

```

### `CPPB-DPS-06` — Doan Con Doi Xung Dai Nhat Substring

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    int n = s.size();
    if (n == 0) return 0;

    vector<vector<bool>> dp(n, vector<bool>(n, false));
    int max_len = 1;
    int start_idx = 0;

    for (int i = 0; i < n; ++i) dp[i][i] = true;

    for (int i = 0; i < n - 1; ++i) {
        if (s[i] == s[i + 1]) {
            dp[i][i + 1] = true;
            if (max_len < 2) {
                max_len = 2;
                start_idx = i;
            }
        }
    }

    for (int len = 3; len <= n; ++len) {
        for (int i = 0; i <= n - len; ++i) {
            int j = i + len - 1;
            if (s[i] == s[j] && dp[i + 1][j - 1]) {
                dp[i][j] = true;
                if (len > max_len) {
                    max_len = len;
                    start_idx = i;
                }
            }
        }
    }

    cout << max_len << "\n";
    cout << s.substr(start_idx, max_len) << "\n";
    return 0;
}

```

### `CPPB-DPS-07` — Dem So Xau Con Doi Xung

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    int n = s.size();
    vector<vector<bool>> dp(n, vector<bool>(n, false));
    int count = 0;

    for (int i = 0; i < n; ++i) {
        dp[i][i] = true;
        count++;
    }

    for (int i = 0; i < n - 1; ++i) {
        if (s[i] == s[i + 1]) {
            dp[i][i + 1] = true;
            count++;
        }
    }

    for (int len = 3; len <= n; ++len) {
        for (int i = 0; i <= n - len; ++i) {
            int j = i + len - 1;
            if (s[i] == s[j] && dp[i + 1][j - 1]) {
                dp[i][j] = true;
                count++;
            }
        }
    }

    cout << count << "\n";
    return 0;
}

```

### `CPPB-DPS-08` — Chen It Nhat Thanh Palindrome

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    int n = s.size();
    string t = s;
    reverse(t.begin(), t.end());

    vector<int> prev_row(n + 1, 0), curr_row(n + 1, 0);

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j) {
            if (s[i - 1] == t[j - 1]) {
                curr_row[j] = prev_row[j - 1] + 1;
            } else {
                curr_row[j] = max(prev_row[j], curr_row[j - 1]);
            }
        }
        prev_row = curr_row;
    }

    int lps = prev_row[n];
    cout << n - lps << "\n";
    return 0;
}

```

### `CPPB-DPS-09` — Xau Me Chung Ngan Nhat Scs

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s, t;
    if (!(cin >> s >> t)) return 0;

    int n = s.size(), m = t.size();
    vector<int> prev_row(m + 1, 0), curr_row(m + 1, 0);

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (s[i - 1] == t[j - 1]) {
                curr_row[j] = prev_row[j - 1] + 1;
            } else {
                curr_row[j] = max(prev_row[j], curr_row[j - 1]);
            }
        }
        prev_row = curr_row;
    }

    int lcs = prev_row[m];
    int scs_len = n + m - lcs;
    cout << scs_len << "\n";
    return 0;
}

```

### `CPPB-DPS-10` — Dem So Lan Xuat Hien Xau Con

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MOD = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s, t;
    if (!(cin >> s >> t)) return 0;

    int n = s.size(), m = t.size();
    vector<int> dp(m + 1, 0);
    dp[0] = 1;

    for (int i = 1; i <= n; ++i) {
        for (int j = m; j >= 1; --j) {
            if (s[i - 1] == t[j - 1]) {
                dp[j] = (dp[j] + dp[j - 1]) % MOD;
            }
        }
    }

    cout << dp[m] << "\n";
    return 0;
}

```

### `CPPB-DPS-11` — Khop Chuoi Wildcard Matching

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s, p;
    if (!(cin >> s >> p)) return 0;

    int n = s.size(), m = p.size();
    vector<vector<bool>> dp(n + 1, vector<bool>(m + 1, false));

    dp[0][0] = true;
    for (int j = 1; j <= m; ++j) {
        if (p[j - 1] == '*') dp[0][j] = dp[0][j - 1];
    }

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (p[j - 1] == '?' || p[j - 1] == s[i - 1]) {
                dp[i][j] = dp[i - 1][j - 1];
            } else if (p[j - 1] == '*') {
                dp[i][j] = dp[i][j - 1] || dp[i - 1][j];
            }
        }
    }

    if (dp[n][m]) cout << "YES\n";
    else cout << "NO\n";
    return 0;
}

```

### `CPPB-DPS-12` — Xau Con Chung Ba Chuoi

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s1, s2, s3;
    if (!(cin >> s1 >> s2 >> s3)) return 0;

    int n1 = s1.size(), n2 = s2.size(), n3 = s3.size();
    vector<vector<vector<int>>> dp(n1 + 1, vector<vector<int>>(n2 + 1, vector<int>(n3 + 1, 0)));

    for (int i = 1; i <= n1; ++i) {
        for (int j = 1; j <= n2; ++j) {
            for (int k = 1; k <= n3; ++k) {
                if (s1[i - 1] == s2[j - 1] && s2[j - 1] == s3[k - 1]) {
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1;
                } else {
                    dp[i][j][k] = max({dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1]});
                }
            }
        }
    }

    cout << dp[n1][n2][n3] << "\n";
    return 0;
}

```

### `CPPB-DPS-13` — Xoa It Ky Tu Nhat Tao Chuoi Doi Xung

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    int n = s.size();
    string t = s;
    reverse(t.begin(), t.end());

    vector<int> prev_row(n + 1, 0), curr_row(n + 1, 0);

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j) {
            if (s[i - 1] == t[j - 1]) {
                curr_row[j] = prev_row[j - 1] + 1;
            } else {
                curr_row[j] = max(prev_row[j], curr_row[j - 1]);
            }
        }
        prev_row = curr_row;
    }

    int lps = prev_row[n];
    cout << n - lps << "\n";
    return 0;
}

```

### `CPPB-DPS-14` — Khoi Phuc Chuoi Tu Dien Nho Nhat Lcs

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s, t;
    if (!(cin >> s >> t)) return 0;

    int n = s.size(), m = t.size();
    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (s[i - 1] == t[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }

    int lcs_len = dp[n][m];
    cout << lcs_len << "\n";
    return 0;
}

```

### `CPPB-DPS-15` — Quy Hoach Dong Chuoi Cuc Han

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    int k;
    if (!(cin >> s >> k)) return 0;

    unordered_set<string> dict;
    for (int i = 0; i < k; ++i) {
        string word;
        cin >> word;
        dict.insert(word);
    }

    int n = s.size();
    vector<bool> dp(n + 1, false);
    dp[0] = true;

    for (int i = 1; i <= n; ++i) {
        for (int j = 0; j < i; ++j) {
            if (dp[j] && dict.count(s.substr(j, i - j))) {
                dp[i] = true;
                break;
            }
        }
    }

    if (dp[n]) cout << "YES\n";
    else cout << "NO\n";
    return 0;
}

```

## Chương 06 — Bài 16: STL nâng cao

### `CPPB-STL-01` — Dem So Phan Tu Phan Biet

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    set<long long> st;
    for (int i = 0; i < n; ++i) {
        long long x;
        cin >> x;
        st.insert(x);
    }

    cout << st.size() << "\n";
    return 0;
}

```

### `CPPB-STL-02` — Bang Tra Cuu Tan Suat Tu Khoa

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    map<string, int> freq;
    for (int i = 0; i < n; ++i) {
        string s;
        cin >> s;
        freq[s]++;
    }

    for (const auto& p : freq) {
        cout << p.first << " " << p.second << "\n";
    }
    return 0;
}

```

### `CPPB-STL-03` — Nen Toa Do Mang So Lon

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<long long> vals = a;
    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());

    for (int i = 0; i < n; ++i) {
        int rank = lower_bound(vals.begin(), vals.end(), a[i]) - vals.begin();
        cout << rank << (i + 1 == n ? "" : " ");
    }
    cout << "\n";
    return 0;
}

```

### `CPPB-STL-04` — Tim Phan Tu Nho Nhat Lon Hon X

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;
    if (n <= 0) return 0;

    set<long long> st;
    for (int i = 0; i < n; ++i) {
        long long x;
        cin >> x;
        st.insert(x);
    }

    while (q--) {
        long long x;
        cin >> x;
        auto it = st.lower_bound(x);
        if (it == st.end()) {
            cout << -1 << "\n";
        } else {
            cout << *it << "\n";
        }
    }
    return 0;
}

```

### `CPPB-STL-05` — Hang Doi Uu Tien K Phan Tu Lon Nhat

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;
    if (n <= 0 || k <= 0 || k > n) return 0;

    priority_queue<long long, vector<long long>, greater<long long>> min_heap;

    for (int i = 0; i < n; ++i) {
        long long x;
        cin >> x;
        min_heap.push(x);
        if ((int)min_heap.size() > k) {
            min_heap.pop();
        }
    }

    vector<long long> result;
    while (!min_heap.empty()) {
        result.push_back(min_heap.top());
        min_heap.pop();
    }
    sort(result.rbegin(), result.rend());

    for (int i = 0; i < k; ++i) {
        cout << result[i] << (i + 1 == k ? "" : " ");
    }
    cout << "\n";
    return 0;
}

```

### `CPPB-STL-06` — Quan Ly Tap Hop Da Trung Lap

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;

    multiset<long long> ms;

    while (q--) {
        int type;
        long long x;
        cin >> type >> x;

        if (type == 1) { // Thêm x
            ms.insert(x);
        } else if (type == 2) { // Xóa đúng 1 bản sao của x nếu có
            auto it = ms.find(x);
            if (it != ms.end()) ms.erase(it);
        } else { // Đếm số lượng x
            cout << ms.count(x) << "\n";
        }
    }
    return 0;
}

```

### `CPPB-STL-07` — Hop Nhat Cac Doan So

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Interval {
    long long l, r;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    vector<Interval> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i].l >> a[i].r;

    sort(a.begin(), a.end(), [](const Interval& x, const Interval& y) {
        if (x.l != y.l) return x.l < y.l;
        return x.r < y.r;
    });

    vector<Interval> merged;
    merged.push_back(a[0]);

    for (int i = 1; i < n; ++i) {
        if (a[i].l <= merged.back().r) {
            merged.back().r = max(merged.back().r, a[i].r);
        } else {
            merged.push_back(a[i]);
        }
    }

    cout << merged.size() << "\n";
    for (const auto& iv : merged) {
        cout << iv.l << " " << iv.r << "\n";
    }
    return 0;
}

```

### `CPPB-STL-08` — Tim Trung Vi Dong Trong Luong Du Lieu

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    priority_queue<long long> left_max;
    priority_queue<long long, vector<long long>, greater<long long>> right_min;

    for (int i = 0; i < n; ++i) {
        long long x;
        cin >> x;

        if (left_max.empty() || x <= left_max.top()) {
            left_max.push(x);
        } else {
            right_min.push(x);
        }

        if (left_max.size() > right_min.size() + 1) {
            right_min.push(left_max.top());
            left_max.pop();
        } else if (right_min.size() > left_max.size()) {
            left_max.push(right_min.top());
            right_min.pop();
        }

        cout << left_max.top() << (i + 1 == n ? "" : " ");
    }
    cout << "\n";
    return 0;
}

```

### `CPPB-STL-09` — Dem So Phan Tu Phan Biet Trong Cua So K

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;
    if (n <= 0 || k <= 0 || k > n) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    map<int, int> freq;
    for (int i = 0; i < k; ++i) freq[a[i]]++;

    cout << freq.size();

    for (int i = k; i < n; ++i) {
        // Xóa phần tử cũ
        freq[a[i - k]]--;
        if (freq[a[i - k]] == 0) freq.erase(a[i - k]);

        // Thêm phần tử mới
        freq[a[i]]++;

        cout << " " << freq.size();
    }
    cout << "\n";
    return 0;
}

```

### `CPPB-STL-10` — Noi Day Chi Phi Nho Nhat

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 1) { cout << 0 << "\n"; return 0; }

    priority_queue<long long, vector<long long>, greater<long long>> min_heap;
    for (int i = 0; i < n; ++i) {
        long long x;
        cin >> x;
        min_heap.push(x);
    }

    long long total_cost = 0;
    while (min_heap.size() > 1) {
        long long a = min_heap.top(); min_heap.pop();
        long long b = min_heap.top(); min_heap.pop();
        long long sum = a + b;
        total_cost += sum;
        min_heap.push(sum);
    }

    cout << total_cost << "\n";
    return 0;
}

```

### `CPPB-STL-11` — Lap Lich Cong Viec Toi Uu May Chu

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Job {
    long long s, e;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    vector<Job> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i].s >> a[i].e;

    sort(a.begin(), a.end(), [](const Job& x, const Job& y) {
        if (x.s != y.s) return x.s < y.s;
        return x.e < y.e;
    });

    priority_queue<long long, vector<long long>, greater<long long>> servers;

    for (int i = 0; i < n; ++i) {
        if (!servers.empty() && servers.top() <= a[i].s) {
            servers.pop();
        }
        servers.push(a[i].e);
    }

    cout << servers.size() << "\n";
    return 0;
}

```

### `CPPB-STL-12` — Dem Cap So Co Hieu Bang K So Lon

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;
    if (n <= 0) return 0;

    map<long long, int> freq;
    long long ans = 0;

    for (int i = 0; i < n; ++i) {
        long long x;
        cin >> x;
        if (freq.count(x - k)) ans += freq[x - k];
        if (k != 0 && freq.count(x + k)) ans += freq[x + k];
        freq[x]++;
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB-STL-13` — Truy Van Phan Tu Xuat Hien Nhieu Nhat

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    map<long long, int> freq;
    long long best_val = -1;
    int max_freq = 0;

    for (int i = 0; i < n; ++i) {
        long long x;
        cin >> x;
        freq[x]++;
        if (freq[x] > max_freq || (freq[x] == max_freq && x < best_val)) {
            max_freq = freq[x];
            best_val = x;
        }
    }

    cout << best_val << " " << max_freq << "\n";
    return 0;
}

```

### `CPPB-STL-14` — Tim Cap Diem Gan Nhat

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Point {
    long long x, y;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 1) { cout << 0 << "\n"; return 0; }

    vector<Point> pts(n);
    for (int i = 0; i < n; ++i) cin >> pts[i].x >> pts[i].y;

    sort(pts.begin(), pts.end(), [](const Point& a, const Point& b) {
        if (a.x != b.x) return a.x < b.x;
        return a.y < b.y;
    });

    long long min_dist_sq = LLONG_MAX;
    set<pair<long long, long long>> active_set; // Lưu (y, x)

    int left = 0;
    for (int i = 0; i < n; ++i) {
        long long d = ceil(sqrt(min_dist_sq));
        while (left < i && pts[i].x - pts[left].x >= d) {
            active_set.erase({pts[left].y, pts[left].x});
            left++;
        }

        auto it_low = active_set.lower_bound({pts[i].y - d, LLONG_MIN});
        auto it_high = active_set.upper_bound({pts[i].y + d, LLONG_MAX});

        for (auto it = it_low; it != it_high; ++it) {
            long long dy = pts[i].y - it->first;
            long long dx = pts[i].x - it->second;
            min_dist_sq = min(min_dist_sq, dx * dx + dy * dy);
        }

        active_set.insert({pts[i].y, pts[i].x});
    }

    cout << min_dist_sq << "\n";
    return 0;
}

```

### `CPPB-STL-15` — He Thong Xep Hang Thi Dau Dynamic

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;

    map<string, long long> scores;
    multiset<long long> all_scores;

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) { // Cộng điểm cho thí sinh
            string name;
            long long delta;
            cin >> name >> delta;

            if (scores.count(name)) {
                auto it = all_scores.find(scores[name]);
                if (it != all_scores.end()) all_scores.erase(it);
            }

            scores[name] += delta;
            all_scores.insert(scores[name]);
        } else { // Truy vấn điểm của thí sinh
            string name;
            cin >> name;
            cout << (scores.count(name) ? scores[name] : 0) << "\n";
        }
    }
    return 0;
}

```

## Chương 06 — Bài 17: Stack & Monotonic Stack

### `CPPB-STK-01` — Kiem Tra Day Ngoac Dung Co Ban

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    int open_cnt = 0;
    for (char c : s) {
        if (c == '(') {
            open_cnt++;
        } else {
            if (open_cnt == 0) {
                cout << "NO\n";
                return 0;
            }
            open_cnt--;
        }
    }

    if (open_cnt == 0) cout << "YES\n";
    else cout << "NO\n";
    return 0;
}

```

### `CPPB-STK-02` — Day Ngoac Hon Hop Nhieu Loai

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    stack<char> st;
    for (char c : s) {
        if (c == '(' || c == '[' || c == '{') {
            st.push(c);
        } else {
            if (st.empty()) {
                cout << "NO\n";
                return 0;
            }
            char top = st.top();
            if ((c == ')' && top == '(') || (c == ']' && top == '[') || (c == '}' && top == '{')) {
                st.pop();
            } else {
                cout << "NO\n";
                return 0;
            }
        }
    }

    if (st.empty()) cout << "YES\n";
    else cout << "NO\n";
    return 0;
}

```

### `CPPB-STK-03` — Danh Gia Bieu Thuc Hau To Rpn

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    stack<long long> st;
    for (int i = 0; i < n; ++i) {
        string token;
        cin >> token;
        if (token == "+" || token == "-" || token == "*") {
            long long b = st.top(); st.pop();
            long long a = st.top(); st.pop();
            if (token == "+") st.push(a + b);
            else if (token == "-") st.push(a - b);
            else if (token == "*") st.push(a * b);
        } else {
            st.push(stoll(token));
        }
    }

    cout << st.top() << "\n";
    return 0;
}

```

### `CPPB-STK-04` — Xoa Cac Ky Tu Trung Lap Lien Ke

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    string st = "";
    for (char c : s) {
        if (!st.empty() && st.back() == c) {
            st.pop_back();
        } else {
            st.push_back(c);
        }
    }

    if (st.empty()) cout << "EMPTY\n";
    else cout << st << "\n";
    return 0;
}

```

### `CPPB-STK-05` — Phan Tu Lon Hon Tiep Theo Nge

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<long long> nge(n, -1);
    stack<int> st;

    for (int i = 0; i < n; ++i) {
        while (!st.empty() && a[i] > a[st.top()]) {
            nge[st.top()] = a[i];
            st.pop();
        }
        st.push(i);
    }

    for (int i = 0; i < n; ++i) {
        cout << nge[i] << (i + 1 == n ? "" : " ");
    }
    cout << "\n";
    return 0;
}

```

### `CPPB-STK-06` — Phan Tu Nho Hon Gan Nhat Ben Trai

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<long long> pse(n, -1);
    stack<long long> st;

    for (int i = 0; i < n; ++i) {
        while (!st.empty() && st.top() >= a[i]) {
            st.pop();
        }
        if (!st.empty()) {
            pse[i] = st.top();
        }
        st.push(a[i]);
    }

    for (int i = 0; i < n; ++i) {
        cout << pse[i] << (i + 1 == n ? "" : " ");
    }
    cout << "\n";
    return 0;
}

```

### `CPPB-STK-07` — Do Dai Day Ngoac Dung Dai Nhat

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    stack<int> st;
    st.push(-1);
    int max_len = 0;

    for (int i = 0; i < (int)s.size(); ++i) {
        if (s[i] == '(') {
            st.push(i);
        } else {
            st.pop();
            if (st.empty()) {
                st.push(i);
            } else {
                max_len = max(max_len, i - st.top());
            }
        }
    }

    cout << max_len << "\n";
    return 0;
}

```

### `CPPB-STK-08` — Xoa K Chu So De Duoc So Nho Nhat

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string num;
    int k;
    if (!(cin >> num >> k)) return 0;

    string st = "";
    for (char c : num) {
        while (!st.empty() && k > 0 && st.back() > c) {
            st.pop_back();
            k--;
        }
        st.push_back(c);
    }

    while (k > 0 && !st.empty()) {
        st.pop_back();
        k--;
    }

    // Xóa các số 0 ở đầu
    int start = 0;
    while (start < (int)st.size() && st[start] == '0') start++;

    string ans = st.substr(start);
    if (ans.empty()) cout << "0\n";
    else cout << ans << "\n";
    return 0;
}

```

### `CPPB-STK-09` — Hinh Chu Nhat Lon Nhat Tren Histogram

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    vector<long long> h(n);
    for (int i = 0; i < n; ++i) cin >> h[i];

    h.push_back(0); // Cột lính canh
    stack<int> st;
    long long max_area = 0;

    for (int i = 0; i <= n; ++i) {
        while (!st.empty() && h[i] < h[st.top()]) {
            long long height = h[st.top()];
            st.pop();
            long long width = st.empty() ? i : (i - st.top() - 1);
            max_area = max(max_area, height * width);
        }
        st.push(i);
    }

    cout << max_area << "\n";
    return 0;
}

```

### `CPPB-STK-10` — Hung Nuoc Mua Trapping Rain Water

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    vector<long long> h(n);
    for (int i = 0; i < n; ++i) cin >> h[i];

    stack<int> st;
    long long total_water = 0;

    for (int i = 0; i < n; ++i) {
        while (!st.empty() && h[i] > h[st.top()]) {
            int top = st.top();
            st.pop();
            if (st.empty()) break;

            int dist = i - st.top() - 1;
            long long bounded_height = min(h[i], h[st.top()]) - h[top];
            total_water += dist * bounded_height;
        }
        st.push(i);
    }

    cout << total_water << "\n";
    return 0;
}

```

### `CPPB-STK-11` — Hinh Chu Nhat Toan Mot Lon Nhat Ma Tran

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    if (n <= 0 || m <= 0) return 0;

    vector<string> grid(n);
    for (int i = 0; i < n; ++i) cin >> grid[i];

    vector<int> h(m, 0);
    int max_area = 0;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (grid[i][j] == '1') h[j]++;
            else h[j] = 0;
        }

        // Monotonic stack on row histogram
        vector<int> cur_h = h;
        cur_h.push_back(0);
        stack<int> st;

        for (int j = 0; j <= m; ++j) {
            while (!st.empty() && cur_h[j] < cur_h[st.top()]) {
                int height = cur_h[st.top()];
                st.pop();
                int width = st.empty() ? j : (j - st.top() - 1);
                max_area = max(max_area, height * width);
            }
            st.push(j);
        }
    }

    cout << max_area << "\n";
    return 0;
}

```

### `CPPB-STK-12` — Tong Gia Tri Nho Nhat Moi Doan Con

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MOD = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<int> left_bound(n), right_bound(n);
    stack<int> st;

    // Tìm biên trái nghiêm ngặt nhỏ hơn
    for (int i = 0; i < n; ++i) {
        while (!st.empty() && a[st.top()] > a[i]) st.pop();
        left_bound[i] = st.empty() ? -1 : st.top();
        st.push(i);
    }

    while (!st.empty()) st.pop();

    // Tìm biên phải nhỏ hơn hoặc bằng
    for (int i = n - 1; i >= 0; --i) {
        while (!st.empty() && a[st.top()] >= a[i]) st.pop();
        right_bound[i] = st.empty() ? n : st.top();
        st.push(i);
    }

    long long total_sum = 0;
    for (int i = 0; i < n; ++i) {
        long long count = (1LL * (i - left_bound[i]) * (right_bound[i] - i)) % MOD;
        total_sum = (total_sum + a[i] * count) % MOD;
    }

    cout << total_sum << "\n";
    return 0;
}

```

### `CPPB-STK-13` — Nge Tren Mang Xoay Vong

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<long long> nge(n, -1);
    stack<int> st;

    // Duyệt vòng tròn 2 vòng (2N)
    for (int i = 0; i < 2 * n; ++i) {
        while (!st.empty() && a[i % n] > a[st.top()]) {
            nge[st.top()] = a[i % n];
            st.pop();
        }
        if (i < n) st.push(i);
    }

    for (int i = 0; i < n; ++i) {
        cout << nge[i] << (i + 1 == n ? "" : " ");
    }
    cout << "\n";
    return 0;
}

```

### `CPPB-STK-14` — Toa Thap Tam Nhin

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    vector<long long> h(n);
    for (int i = 0; i < n; ++i) cin >> h[i];

    vector<int> span(n);
    stack<int> st;

    for (int i = 0; i < n; ++i) {
        while (!st.empty() && h[st.top()] <= h[i]) {
            st.pop();
        }
        span[i] = st.empty() ? (i + 1) : (i - st.top());
        st.push(i);
    }

    for (int i = 0; i < n; ++i) {
        cout << span[i] << (i + 1 == n ? "" : " ");
    }
    cout << "\n";
    return 0;
}

```

### `CPPB-STK-15` — Danh Gia Bieu Thuc Dai So Day Du

```cpp
#include <bits/stdc++.h>
using namespace std;

int precedence(char op) {
    if (op == '+' || op == '-') return 1;
    if (op == '*' || op == '/') return 2;
    return 0;
}

long long applyOp(long long a, long long b, char op) {
    if (op == '+') return a + b;
    if (op == '-') return a - b;
    if (op == '*') return a * b;
    if (op == '/') return b != 0 ? a / b : 0;
    return 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    stack<long long> values;
    stack<char> ops;

    for (int i = 0; i < (int)s.size(); ++i) {
        if (isdigit(s[i])) {
            long long val = 0;
            while (i < (int)s.size() && isdigit(s[i])) {
                val = (val * 10) + (s[i] - '0');
                i++;
            }
            values.push(val);
            i--;
        } else if (s[i] == '(') {
            ops.push(s[i]);
        } else if (s[i] == ')') {
            while (!ops.empty() && ops.top() != '(') {
                long long val2 = values.top(); values.pop();
                long long val1 = values.top(); values.pop();
                char op = ops.top(); ops.pop();
                values.push(applyOp(val1, val2, op));
            }
            if (!ops.empty()) ops.pop(); // Bỏ '('
        } else if (s[i] == '+' || s[i] == '-' || s[i] == '*' || s[i] == '/') {
            while (!ops.empty() && precedence(ops.top()) >= precedence(s[i])) {
                long long val2 = values.top(); values.pop();
                long long val1 = values.top(); values.pop();
                char op = ops.top(); ops.pop();
                values.push(applyOp(val1, val2, op));
            }
            ops.push(s[i]);
        }
    }

    while (!ops.empty()) {
        long long val2 = values.top(); values.pop();
        long long val1 = values.top(); values.pop();
        char op = ops.top(); ops.pop();
        values.push(applyOp(val1, val2, op));
    }

    cout << values.top() << "\n";
    return 0;
}

```

## Chương 06 — Bài 18: Queue & Deque

### `CPPB-QUE-01` — Cai Dat Hang Doi Co Ban

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;

    queue<long long> qu;

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) { // Push x
            long long x;
            cin >> x;
            qu.push(x);
        } else if (type == 2) { // Pop
            if (!qu.empty()) qu.pop();
        } else if (type == 3) { // Front
            if (qu.empty()) cout << "EMPTY\n";
            else cout << qu.front() << "\n";
        }
    }
    return 0;
}

```

### `CPPB-QUE-02` — Sinh Chuoi So Nhi Phan Bang Queue

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    queue<string> q;
    q.push("1");

    for (int i = 1; i <= n; ++i) {
        string s = q.front();
        q.pop();

        cout << s << (i == n ? "" : " ");

        q.push(s + "0");
        q.push(s + "1");
    }
    cout << "\n";
    return 0;
}

```

### `CPPB-QUE-03` — Bfs Tim Duong Di Ngan Nhat Do Thi

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    if (n <= 0) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> dist(n + 1, -1);
    queue<int> q;

    dist[1] = 0;
    q.push(1);

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (int v : adj[u]) {
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }

    cout << dist[n] << "\n";
    return 0;
}

```

### `CPPB-QUE-04` — Truy Vet Lo Trinh Ngan Nhat Bfs

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    if (n <= 0) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> dist(n + 1, -1);
    vector<int> parent(n + 1, -1);
    queue<int> q;

    dist[1] = 0;
    q.push(1);

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (int v : adj[u]) {
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                parent[v] = u;
                q.push(v);
            }
        }
    }

    if (dist[n] == -1) {
        cout << -1 << "\n";
        return 0;
    }

    vector<int> path;
    int curr = n;
    while (curr != -1) {
        path.push_back(curr);
        curr = parent[curr];
    }
    reverse(path.begin(), path.end());

    cout << path.size() << "\n";
    for (int i = 0; i < (int)path.size(); ++i) {
        cout << path[i] << (i + 1 == (int)path.size() ? "" : " ");
    }
    cout << "\n";
    return 0;
}

```

### `CPPB-QUE-05` — Min Moi Cua So Truot Do Dai K

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;
    if (n <= 0 || k <= 0 || k > n) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    deque<int> dq;
    vector<long long> ans;

    for (int i = 0; i < n; ++i) {
        while (!dq.empty() && dq.front() < i - k + 1) dq.pop_front();
        while (!dq.empty() && a[dq.back()] >= a[i]) dq.pop_back();
        dq.push_back(i);

        if (i >= k - 1) ans.push_back(a[dq.front()]);
    }

    for (int i = 0; i < (int)ans.size(); ++i) {
        cout << ans[i] << (i + 1 == (int)ans.size() ? "" : " ");
    }
    cout << "\n";
    return 0;
}

```

### `CPPB-QUE-06` — Max Moi Cua So Truot Do Dai K

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;
    if (n <= 0 || k <= 0 || k > n) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    deque<int> dq;
    vector<long long> ans;

    for (int i = 0; i < n; ++i) {
        while (!dq.empty() && dq.front() < i - k + 1) dq.pop_front();
        while (!dq.empty() && a[dq.back()] <= a[i]) dq.pop_back();
        dq.push_back(i);

        if (i >= k - 1) ans.push_back(a[dq.front()]);
    }

    for (int i = 0; i < (int)ans.size(); ++i) {
        cout << ans[i] << (i + 1 == (int)ans.size() ? "" : " ");
    }
    cout << "\n";
    return 0;
}

```

### `CPPB-QUE-07` — Kiem Tra Do Thi Hai Phia 2 Coloring

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    if (n <= 0) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> color(n + 1, 0);
    bool is_bipartite = true;

    for (int i = 1; i <= n; ++i) {
        if (color[i] == 0) {
            queue<int> q;
            color[i] = 1;
            q.push(i);

            while (!q.empty()) {
                int u = q.front();
                q.pop();

                for (int v : adj[u]) {
                    if (color[v] == 0) {
                        color[v] = 3 - color[u];
                        q.push(v);
                    } else if (color[v] == color[u]) {
                        is_bipartite = false;
                        break;
                    }
                }
                if (!is_bipartite) break;
            }
        }
        if (!is_bipartite) break;
    }

    if (is_bipartite) cout << "YES\n";
    else cout << "NO\n";
    return 0;
}

```

### `CPPB-QUE-08` — Bien Doi So Buoc Nho Nhat A Sang B

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int a, b;
    if (!(cin >> a >> b)) return 0;

    if (a >= b) {
        cout << a - b << "\n";
        return 0;
    }

    vector<int> dist(20005, -1);
    queue<int> q;

    dist[a] = 0;
    q.push(a);

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        if (u == b) {
            cout << dist[b] << "\n";
            return 0;
        }

        // Thao tác 1: u * 2
        if (u * 2 <= 20000 && dist[u * 2] == -1) {
            dist[u * 2] = dist[u] + 1;
            q.push(u * 2);
        }

        // Thao tác 2: u - 1
        if (u - 1 > 0 && dist[u - 1] == -1) {
            dist[u - 1] = dist[u] + 1;
            q.push(u - 1);
        }
    }

    return 0;
}

```

### `CPPB-QUE-09` — 0 1 Bfs Tim Duong Ngan Nhat Trong So 0 1

```cpp
#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;

struct Edge {
    int to, weight;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    if (n <= 0) return 0;

    vector<vector<Edge>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }

    vector<int> dist(n + 1, INF);
    deque<int> dq;

    dist[1] = 0;
    dq.push_back(1);

    while (!dq.empty()) {
        int u = dq.front();
        dq.pop_front();

        for (const auto& edge : adj[u]) {
            int v = edge.to;
            int w = edge.weight;

            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                if (w == 0) {
                    dq.push_front(v);
                } else {
                    dq.push_back(v);
                }
            }
        }
    }

    if (dist[n] == INF) cout << -1 << "\n";
    else cout << dist[n] << "\n";
    return 0;
}

```

### `CPPB-QUE-10` — Doan Con Tong Lon Nhat Do Dai Toi Da K

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;
    if (n <= 0 || k <= 0) return 0;

    vector<long long> a(n + 1);
    vector<long long> pref(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
        pref[i] = pref[i - 1] + a[i];
    }

    deque<int> dq;
    dq.push_back(0);
    long long max_sum = LLONG_MIN;

    for (int i = 1; i <= n; ++i) {
        while (!dq.empty() && dq.front() < i - k) dq.pop_front();
        if (!dq.empty()) {
            max_sum = max(max_sum, pref[i] - pref[dq.front()]);
        }
        while (!dq.empty() && pref[dq.back()] >= pref[i]) dq.pop_back();
        dq.push_back(i);
    }

    cout << max_sum << "\n";
    return 0;
}

```

### `CPPB-QUE-11` — Tro Choi Vong Tron Josephus Bang Queue

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;
    if (n <= 0 || k <= 0) return 0;

    queue<int> q;
    for (int i = 1; i <= n; ++i) q.push(i);

    while (q.size() > 1) {
        for (int i = 1; i < k; ++i) {
            q.push(q.front());
            q.pop();
        }
        q.pop(); // Loại bỏ người thứ k
    }

    cout << q.front() << "\n";
    return 0;
}

```

### `CPPB-QUE-12` — Khoang Cach Den Tram Cuu Hoa Gan Nhat

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, k;
    if (!(cin >> n >> m >> k)) return 0;
    if (n <= 0) return 0;

    vector<int> dist(n + 1, -1);
    queue<int> q;

    for (int i = 0; i < k; ++i) {
        int st;
        cin >> st;
        dist[st] = 0;
        q.push(st);
    }

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (int v : adj[u]) {
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }

    for (int i = 1; i <= n; ++i) {
        cout << dist[i] << (i == n ? "" : " ");
    }
    cout << "\n";
    return 0;
}

```

### `CPPB-QUE-13` — Cua So Truot Chenh Lech Max Min Le C

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long c;
    if (!(cin >> n >> c)) return 0;
    if (n <= 0) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    deque<int> min_dq, max_dq;
    int left = 0;
    int max_len = 0;

    for (int right = 0; right < n; ++right) {
        while (!min_dq.empty() && a[min_dq.back()] >= a[right]) min_dq.pop_back();
        min_dq.push_back(right);

        while (!max_dq.empty() && a[max_dq.back()] <= a[right]) max_dq.pop_back();
        max_dq.push_back(right);

        while (a[max_dq.front()] - a[min_dq.front()] > c) {
            left++;
            if (min_dq.front() < left) min_dq.pop_front();
            if (max_dq.front() < left) max_dq.pop_front();
        }

        max_len = max(max_len, right - left + 1);
    }

    cout << max_len << "\n";
    return 0;
}

```

### `CPPB-QUE-14` — Cat Bang Ron Quang Cao Toi Uu

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;
    if (n <= 0) return 0;

    vector<long long> a(n + 1);
    long long total_sum = 0;
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
        total_sum += a[i];
    }

    // dp[i]: tổng nhỏ nhất các phần tử bị loại bỏ kết thúc tại i sao cho không có k+1 phần tử liền kề nào được chọn
    vector<long long> dp(n + 1, 0);
    deque<int> dq;
    dq.push_back(0);

    for (int i = 1; i <= n; ++i) {
        while (!dq.empty() && dq.front() < i - k - 1) dq.pop_front();
        dp[i] = dp[dq.front()] + a[i];
        while (!dq.empty() && dp[dq.back()] >= dp[i]) dq.pop_back();
        dq.push_back(i);
    }

    long long min_dropped = LLONG_MAX;
    for (int i = n - k; i <= n; ++i) {
        if (i >= 0) min_dropped = min(min_dropped, dp[i]);
    }

    cout << total_sum - min_dropped << "\n";
    return 0;
}

```

### `CPPB-QUE-15` — Dua Xe Me Cung Doi Huong

```cpp
#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;
const int dr[] = {-1, 1, 0, 0};
const int dc[] = {0, 0, -1, 1};

struct State {
    int r, c, dir;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    if (n <= 0 || m <= 0) return 0;

    vector<string> grid(n);
    int sr = -1, sc = -1, er = -1, ec = -1;

    for (int r = 0; r < n; ++r) {
        cin >> grid[r];
        for (int c = 0; c < m; ++c) {
            if (grid[r][c] == 'S') { sr = r; sc = c; }
            if (grid[r][c] == 'E') { er = r; ec = c; }
        }
    }

    vector<vector<vector<int>>> dist(n, vector<vector<int>>(m, vector<int>(4, INF)));
    deque<State> dq;

    for (int d = 0; d < 4; ++d) {
        dist[sr][sc][d] = 0;
        dq.push_back({sr, sc, d});
    }

    while (!dq.empty()) {
        auto [r, c, dir] = dq.front();
        dq.pop_front();

        for (int nd = 0; nd < 4; ++nd) {
            int nr = r + dr[nd];
            int nc = c + dc[nd];
            int cost = (nd == dir ? 0 : 1);

            if (nr >= 0 && nr < n && nc >= 0 && nc < m && grid[nr][nc] != '#') {
                if (dist[r][c][dir] + cost < dist[nr][nc][nd]) {
                    dist[nr][nc][nd] = dist[r][c][dir] + cost;
                    if (cost == 0) {
                        dq.push_front({nr, nc, nd});
                    } else {
                        dq.push_back({nr, nc, nd});
                    }
                }
            }
        }
    }

    int ans = INF;
    for (int d = 0; d < 4; ++d) ans = min(ans, dist[er][ec][d]);

    if (ans == INF) cout << -1 << "\n";
    else cout << ans << "\n";
    return 0;
}

```

## Chương 07 — Bài 19: Đồ thị BFS & DFS

### `CPPB-GRA-01` — Chuyen Doi Danh Sach Canh Sang Danh Sach Ke

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    if (n <= 0) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    for (int i = 1; i <= n; ++i) {
        sort(adj[i].begin(), adj[i].end());
        cout << adj[i].size();
        for (int v : adj[i]) {
            cout << " " << v;
        }
        cout << "\n";
    }
    return 0;
}

```

### `CPPB-GRA-02` — Duyet Do Thi Theo Chieu Sau Dfs

```cpp
#include <bits/stdc++.h>
using namespace std;

int n, m, s;
vector<vector<int>> adj;
vector<bool> visited;
vector<int> traversal;

void dfs(int u) {
    visited[u] = true;
    traversal.push_back(u);
    for (int v : adj[u]) {
        if (!visited[v]) {
            dfs(v);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> m >> s)) return 0;
    if (n <= 0) return 0;

    adj.assign(n + 1, vector<int>());
    visited.assign(n + 1, false);

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    for (int i = 1; i <= n; ++i) sort(adj[i].begin(), adj[i].end());

    dfs(s);

    for (int i = 0; i < (int)traversal.size(); ++i) {
        cout << traversal[i] << (i + 1 == (int)traversal.size() ? "" : " ");
    }
    cout << "\n";
    return 0;
}

```

### `CPPB-GRA-03` — Duyet Do Thi Theo Chieu Rong Bfs

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, s;
    if (!(cin >> n >> m >> s)) return 0;
    if (n <= 0) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    for (int i = 1; i <= n; ++i) sort(adj[i].begin(), adj[i].end());

    vector<bool> visited(n + 1, false);
    vector<int> traversal;
    queue<int> q;

    visited[s] = true;
    q.push(s);

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        traversal.push_back(u);

        for (int v : adj[u]) {
            if (!visited[v]) {
                visited[v] = true;
                q.push(v);
            }
        }
    }

    for (int i = 0; i < (int)traversal.size(); ++i) {
        cout << traversal[i] << (i + 1 == (int)traversal.size() ? "" : " ");
    }
    cout << "\n";
    return 0;
}

```

### `CPPB-GRA-04` — Dem So Thanh Phan Lien Thong

```cpp
#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<vector<int>> adj;
vector<bool> visited;

void dfs(int u) {
    visited[u] = true;
    for (int v : adj[u]) {
        if (!visited[v]) dfs(v);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> m)) return 0;
    if (n <= 0) return 0;

    adj.assign(n + 1, vector<int>());
    visited.assign(n + 1, false);

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    int components = 0;
    for (int i = 1; i <= n; ++i) {
        if (!visited[i]) {
            components++;
            dfs(i);
        }
    }

    cout << components << "\n";
    return 0;
}

```

### `CPPB-GRA-05` — Tim Kich Thuoc Thanh Phan Lien Thong Lon Nhat

```cpp
#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<vector<int>> adj;
vector<bool> visited;

int dfs(int u) {
    visited[u] = true;
    int sz = 1;
    for (int v : adj[u]) {
        if (!visited[v]) sz += dfs(v);
    }
    return sz;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> m)) return 0;
    if (n <= 0) return 0;

    adj.assign(n + 1, vector<int>());
    visited.assign(n + 1, false);

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    int max_sz = 0;
    for (int i = 1; i <= n; ++i) {
        if (!visited[i]) {
            max_sz = max(max_sz, dfs(i));
        }
    }

    cout << max_sz << "\n";
    return 0;
}

```

### `CPPB-GRA-06` — Kiem Tra Duong Di Giua Hai Dinh

```cpp
#include <bits/stdc++.h>
using namespace std;

int n, m, s, t;
vector<vector<int>> adj;
vector<bool> visited;

void dfs(int u) {
    visited[u] = true;
    for (int v : adj[u]) {
        if (!visited[v]) dfs(v);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> m >> s >> t)) return 0;
    if (n <= 0) return 0;

    adj.assign(n + 1, vector<int>());
    visited.assign(n + 1, false);

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    dfs(s);

    if (visited[t]) cout << "YES\n";
    else cout << "NO\n";
    return 0;
}

```

### `CPPB-GRA-07` — Phat Hien Chu Trinh Tren Do Thi Vo Huong

```cpp
#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<vector<int>> adj;
vector<bool> visited;
bool has_cycle = false;

void dfs(int u, int p) {
    visited[u] = true;
    for (int v : adj[u]) {
        if (!visited[v]) {
            dfs(v, u);
        } else if (v != p) {
            has_cycle = true;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> m)) return 0;
    if (n <= 0) return 0;

    adj.assign(n + 1, vector<int>());
    visited.assign(n + 1, false);

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    for (int i = 1; i <= n; ++i) {
        if (!visited[i]) dfs(i, 0);
    }

    if (has_cycle) cout << "YES\n";
    else cout << "NO\n";
    return 0;
}

```

### `CPPB-GRA-08` — Tim Duong Di Ngan Nhat Bang Bfs

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    if (n <= 0) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> dist(n + 1, -1);
    queue<int> q;

    dist[1] = 0;
    q.push(1);

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (int v : adj[u]) {
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }

    cout << dist[n] << "\n";
    return 0;
}

```

### `CPPB-GRA-09` — Kiem Tra Do Thi Cay

```cpp
#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<vector<int>> adj;
vector<bool> visited;

int dfs(int u) {
    visited[u] = true;
    int sz = 1;
    for (int v : adj[u]) {
        if (!visited[v]) sz += dfs(v);
    }
    return sz;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> m)) return 0;
    if (n <= 0) return 0;

    if (m != n - 1) {
        cout << "NO\n";
        return 0;
    }

    adj.assign(n + 1, vector<int>());
    visited.assign(n + 1, false);

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    int sz = dfs(1);

    if (sz == n) cout << "YES\n";
    else cout << "NO\n";
    return 0;
}

```

### `CPPB-GRA-10` — Sap Xep To Po Tren Dag

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    if (n <= 0) return 0;

    vector<vector<int>> adj(n + 1);
    vector<int> in_degree(n + 1, 0);

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        in_degree[v]++;
    }

    queue<int> q;
    for (int i = 1; i <= n; ++i) {
        if (in_degree[i] == 0) q.push(i);
    }

    vector<int> topo;
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        topo.push_back(u);

        for (int v : adj[u]) {
            in_degree[v]--;
            if (in_degree[v] == 0) q.push(v);
        }
    }

    if ((int)topo.size() < n) {
        cout << -1 << "\n";
    } else {
        for (int i = 0; i < n; ++i) {
            cout << topo[i] << (i + 1 == n ? "" : " ");
        }
        cout << "\n";
    }
    return 0;
}

```

### `CPPB-GRA-11` — Tim Chu Trinh Do Dai Nho Nhat

```cpp
#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    if (n <= 0) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    int min_cycle = INF;

    for (int s = 1; s <= n; ++s) {
        vector<int> dist(n + 1, INF);
        vector<int> parent(n + 1, -1);
        queue<int> q;

        dist[s] = 0;
        q.push(s);

        while (!q.empty()) {
            int u = q.front();
            q.pop();

            for (int v : adj[u]) {
                if (dist[v] == INF) {
                    dist[v] = dist[u] + 1;
                    parent[v] = u;
                    q.push(v);
                } else if (parent[u] != v) {
                    min_cycle = min(min_cycle, dist[u] + dist[v] + 1);
                }
            }
        }
    }

    if (min_cycle == INF) cout << -1 << "\n";
    else cout << min_cycle << "\n";
    return 0;
}

```

### `CPPB-GRA-12` — Dem Cap Dinh Khong The Di Toi Nhau

```cpp
#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<vector<int>> adj;
vector<bool> visited;

int dfs(int u) {
    visited[u] = true;
    int sz = 1;
    for (int v : adj[u]) {
        if (!visited[v]) sz += dfs(v);
    }
    return sz;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> m)) return 0;
    if (n <= 0) return 0;

    adj.assign(n + 1, vector<int>());
    visited.assign(n + 1, false);

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<long long> comp_sizes;
    for (int i = 1; i <= n; ++i) {
        if (!visited[i]) {
            comp_sizes.push_back(dfs(i));
        }
    }

    long long total_pairs = 1LL * n * (n - 1) / 2;
    long long connected_pairs = 0;

    for (long long sz : comp_sizes) {
        connected_pairs += sz * (sz - 1) / 2;
    }

    cout << total_pairs - connected_pairs << "\n";
    return 0;
}

```

### `CPPB-GRA-13` — Multi Source Bfs Lan Toa Virus

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, k;
    if (!(cin >> n >> m >> k)) return 0;
    if (n <= 0) return 0;

    vector<int> dist(n + 1, -1);
    queue<int> q;

    for (int i = 0; i < k; ++i) {
        int src;
        cin >> src;
        dist[src] = 0;
        q.push(src);
    }

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    int max_time = 0;
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        max_time = max(max_time, dist[u]);

        for (int v : adj[u]) {
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }

    for (int i = 1; i <= n; ++i) {
        if (dist[i] == -1) {
            cout << -1 << "\n";
            return 0;
        }
    }

    cout << max_time << "\n";
    return 0;
}

```

### `CPPB-GRA-14` — Tim Canh Cau Tren Do Thi

```cpp
#include <bits/stdc++.h>
using namespace std;

int n, m, timer = 0;
vector<vector<int>> adj;
vector<int> tin, low;
vector<bool> visited;
int bridge_count = 0;

void dfs(int u, int p = -1) {
    visited[u] = true;
    tin[u] = low[u] = ++timer;

    for (int v : adj[u]) {
        if (v == p) continue;
        if (visited[v]) {
            low[u] = min(low[u], tin[v]);
        } else {
            dfs(v, u);
            low[u] = min(low[u], low[v]);
            if (low[v] > tin[u]) {
                bridge_count++;
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> m)) return 0;
    if (n <= 0) return 0;

    adj.assign(n + 1, vector<int>());
    tin.assign(n + 1, -1);
    low.assign(n + 1, -1);
    visited.assign(n + 1, false);

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    for (int i = 1; i <= n; ++i) {
        if (!visited[i]) dfs(i);
    }

    cout << bridge_count << "\n";
    return 0;
}

```

### `CPPB-GRA-15` — Mang Luoi Giao Thong Toi Uu

```cpp
#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<vector<int>> adj;
vector<bool> visited;

void dfs(int u) {
    visited[u] = true;
    for (int v : adj[u]) {
        if (!visited[v]) dfs(v);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> m)) return 0;
    if (n <= 0) return 0;

    adj.assign(n + 1, vector<int>());
    visited.assign(n + 1, false);

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> leaders;
    for (int i = 1; i <= n; ++i) {
        if (!visited[i]) {
            leaders.push_back(i);
            dfs(i);
        }
    }

    int needed = leaders.size() - 1;
    cout << needed << "\n";
    for (int i = 0; i < needed; ++i) {
        cout << leaders[i] << " " << leaders[i + 1] << "\n";
    }
    return 0;
}

```

## Chương 07 — Bài 20: Đồ thị lưới 2D

### `CPPB-GRD-01` — Duyet 4 Huong Tren Ma Tran Co Ban

```cpp
#include <bits/stdc++.h>
using namespace std;

const int dr[] = {-1, 1, 0, 0};
const int dc[] = {0, 0, -1, 1};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, r, c;
    if (!(cin >> n >> m >> r >> c)) return 0;

    int valid_neighbors = 0;
    for (int d = 0; d < 4; ++d) {
        int nr = r + dr[d];
        int nc = c + dc[d];
        if (nr >= 0 && nr < n && nc >= 0 && nc < m) {
            valid_neighbors++;
        }
    }

    cout << valid_neighbors << "\n";
    return 0;
}

```

### `CPPB-GRD-02` — Dem So Luong Hon Dao

```cpp
#include <bits/stdc++.h>
using namespace std;

const int dr[] = {-1, 1, 0, 0};
const int dc[] = {0, 0, -1, 1};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    if (n <= 0 || m <= 0) return 0;

    vector<string> grid(n);
    for (int i = 0; i < n; ++i) cin >> grid[i];

    vector<vector<bool>> visited(n, vector<bool>(m, false));
    int islands = 0;

    for (int r = 0; r < n; ++r) {
        for (int c = 0; c < m; ++c) {
            if (grid[r][c] == '1' && !visited[r][c]) {
                islands++;
                visited[r][c] = true;
                queue<pair<int, int>> q;
                q.push({r, c});

                while (!q.empty()) {
                    auto [cr, cc] = q.front();
                    q.pop();

                    for (int d = 0; d < 4; ++d) {
                        int nr = cr + dr[d];
                        int nc = cc + dc[d];
                        if (nr >= 0 && nr < n && nc >= 0 && nc < m && grid[nr][nc] == '1' && !visited[nr][nc]) {
                            visited[nr][nc] = true;
                            q.push({nr, nc});
                        }
                    }
                }
            }
        }
    }

    cout << islands << "\n";
    return 0;
}

```

### `CPPB-GRD-03` — Dien Tich Hon Dao Lon Nhat

```cpp
#include <bits/stdc++.h>
using namespace std;

const int dr[] = {-1, 1, 0, 0};
const int dc[] = {0, 0, -1, 1};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    if (n <= 0 || m <= 0) return 0;

    vector<string> grid(n);
    for (int i = 0; i < n; ++i) cin >> grid[i];

    vector<vector<bool>> visited(n, vector<bool>(m, false));
    int max_area = 0;

    for (int r = 0; r < n; ++r) {
        for (int c = 0; c < m; ++c) {
            if (grid[r][c] == '1' && !visited[r][c]) {
                int area = 0;
                visited[r][c] = true;
                queue<pair<int, int>> q;
                q.push({r, c});

                while (!q.empty()) {
                    auto [cr, cc] = q.front();
                    q.pop();
                    area++;

                    for (int d = 0; d < 4; ++d) {
                        int nr = cr + dr[d];
                        int nc = cc + dc[d];
                        if (nr >= 0 && nr < n && nc >= 0 && nc < m && grid[nr][nc] == '1' && !visited[nr][nc]) {
                            visited[nr][nc] = true;
                            q.push({nr, nc});
                        }
                    }
                }
                max_area = max(max_area, area);
            }
        }
    }

    cout << max_area << "\n";
    return 0;
}

```

### `CPPB-GRD-04` — Tim Duong Thoat Khoi Me Cung Bfs

```cpp
#include <bits/stdc++.h>
using namespace std;

const int dr[] = {-1, 1, 0, 0};
const int dc[] = {0, 0, -1, 1};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<string> grid(n);
    int sr = -1, sc = -1, er = -1, ec = -1;

    for (int r = 0; r < n; ++r) {
        cin >> grid[r];
        for (int c = 0; c < m; ++c) {
            if (grid[r][c] == 'A' || grid[r][c] == 'S') { sr = r; sc = c; }
            if (grid[r][c] == 'B' || grid[r][c] == 'E') { er = r; ec = c; }
        }
    }

    vector<vector<int>> dist(n, vector<int>(m, -1));
    queue<pair<int, int>> q;

    dist[sr][sc] = 0;
    q.push({sr, sc});

    while (!q.empty()) {
        auto [r, c] = q.front();
        q.pop();

        if (r == er && c == ec) {
            cout << dist[r][c] << "\n";
            return 0;
        }

        for (int d = 0; d < 4; ++d) {
            int nr = r + dr[d];
            int nc = c + dc[d];
            if (nr >= 0 && nr < n && nc >= 0 && nc < m && grid[nr][nc] != '#' && dist[nr][nc] == -1) {
                dist[nr][nc] = dist[r][c] + 1;
                q.push({nr, nc});
            }
        }
    }

    cout << -1 << "\n";
    return 0;
}

```

### `CPPB-GRD-05` — Truy Vet Duong Di Me Cung

```cpp
#include <bits/stdc++.h>
using namespace std;

const int dr[] = {-1, 1, 0, 0};
const int dc[] = {0, 0, -1, 1};
const char dir_char[] = {'U', 'D', 'L', 'R'};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<string> grid(n);
    int sr = -1, sc = -1, er = -1, ec = -1;

    for (int r = 0; r < n; ++r) {
        cin >> grid[r];
        for (int c = 0; c < m; ++c) {
            if (grid[r][c] == 'A' || grid[r][c] == 'S') { sr = r; sc = c; }
            if (grid[r][c] == 'B' || grid[r][c] == 'E') { er = r; ec = c; }
        }
    }

    vector<vector<int>> dist(n, vector<int>(m, -1));
    vector<vector<int>> prev_dir(n, vector<int>(m, -1));
    queue<pair<int, int>> q;

    dist[sr][sc] = 0;
    q.push({sr, sc});

    while (!q.empty()) {
        auto [r, c] = q.front();
        q.pop();

        if (r == er && c == ec) break;

        for (int d = 0; d < 4; ++d) {
            int nr = r + dr[d];
            int nc = c + dc[d];
            if (nr >= 0 && nr < n && nc >= 0 && nc < m && grid[nr][nc] != '#' && dist[nr][nc] == -1) {
                dist[nr][nc] = dist[r][c] + 1;
                prev_dir[nr][nc] = d;
                q.push({nr, nc});
            }
        }
    }

    if (dist[er][ec] == -1) {
        cout << "NO\n";
        return 0;
    }

    cout << "YES\n" << dist[er][ec] << "\n";
    string path = "";
    int curr_r = er, curr_c = ec;

    while (curr_r != sr || curr_c != sc) {
        int d = prev_dir[curr_r][curr_c];
        path += dir_char[d];
        curr_r -= dr[d];
        curr_c -= dc[d];
    }
    reverse(path.begin(), path.end());
    cout << path << "\n";
    return 0;
}

```

### `CPPB-GRD-06` — Dem Vung Kin Khong Thong Ra Bien

```cpp
#include <bits/stdc++.h>
using namespace std;

const int dr[] = {-1, 1, 0, 0};
const int dc[] = {0, 0, -1, 1};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<string> grid(n);
    for (int i = 0; i < n; ++i) cin >> grid[i];

    queue<pair<int, int>> q;

    for (int r = 0; r < n; ++r) {
        if (grid[r][0] == '0') { grid[r][0] = '1'; q.push({r, 0}); }
        if (grid[r][m - 1] == '0') { grid[r][m - 1] = '1'; q.push({r, m - 1}); }
    }
    for (int c = 0; c < m; ++c) {
        if (grid[0][c] == '0') { grid[0][c] = '1'; q.push({0, c}); }
        if (grid[n - 1][c] == '0') { grid[n - 1][c] = '1'; q.push({n - 1, c}); }
    }

    while (!q.empty()) {
        auto [r, c] = q.front();
        q.pop();

        for (int d = 0; d < 4; ++d) {
            int nr = r + dr[d];
            int nc = c + dc[d];
            if (nr >= 0 && nr < n && nc >= 0 && nc < m && grid[nr][nc] == '0') {
                grid[nr][nc] = '1';
                q.push({nr, nc});
            }
        }
    }

    int closed_zeros = 0;
    for (int r = 0; r < n; ++r) {
        for (int c = 0; c < m; ++c) {
            if (grid[r][c] == '0') closed_zeros++;
        }
    }

    cout << closed_zeros << "\n";
    return 0;
}

```

### `CPPB-GRD-07` — Chu Vi Hon Dao

```cpp
#include <bits/stdc++.h>
using namespace std;

const int dr[] = {-1, 1, 0, 0};
const int dc[] = {0, 0, -1, 1};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<string> grid(n);
    for (int i = 0; i < n; ++i) cin >> grid[i];

    int perimeter = 0;

    for (int r = 0; r < n; ++r) {
        for (int c = 0; c < m; ++c) {
            if (grid[r][c] == '1') {
                for (int d = 0; d < 4; ++d) {
                    int nr = r + dr[d];
                    int nc = c + dc[d];
                    if (nr < 0 || nr >= n || nc < 0 || nc >= m || grid[nr][nc] == '0') {
                        perimeter++;
                    }
                }
            }
        }
    }

    cout << perimeter << "\n";
    return 0;
}

```

### `CPPB-GRD-08` — Nuoc Tran Me Cung Multi Source Bfs

```cpp
#include <bits/stdc++.h>
using namespace std;

const int dr[] = {-1, 1, 0, 0};
const int dc[] = {0, 0, -1, 1};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<string> grid(n);
    int er = -1, ec = -1;
    vector<vector<int>> dist(n, vector<int>(m, -1));
    queue<pair<int, int>> q;

    for (int r = 0; r < n; ++r) {
        cin >> grid[r];
        for (int c = 0; c < m; ++c) {
            if (grid[r][c] == 'W') {
                dist[r][c] = 0;
                q.push({r, c});
            }
            if (grid[r][c] == 'E') { er = r; ec = c; }
        }
    }

    while (!q.empty()) {
        auto [r, c] = q.front();
        q.pop();

        for (int d = 0; d < 4; ++d) {
            int nr = r + dr[d];
            int nc = c + dc[d];
            if (nr >= 0 && nr < n && nc >= 0 && nc < m && grid[nr][nc] != '#' && dist[nr][nc] == -1) {
                dist[nr][nc] = dist[r][c] + 1;
                q.push({nr, nc});
            }
        }
    }

    cout << dist[er][ec] << "\n";
    return 0;
}

```

### `CPPB-GRD-09` — Buoc Nhay Quan Ma Ngan Nhat

```cpp
#include <bits/stdc++.h>
using namespace std;

const int dr[] = {-2, -2, -1, -1, 1, 1, 2, 2};
const int dc[] = {-1, 1, -2, 2, -2, 2, -1, 1};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, sr, sc, er, ec;
    if (!(cin >> n >> m >> sr >> sc >> er >> ec)) return 0;

    vector<vector<int>> dist(n, vector<int>(m, -1));
    queue<pair<int, int>> q;

    dist[sr][sc] = 0;
    q.push({sr, sc});

    while (!q.empty()) {
        auto [r, c] = q.front();
        q.pop();

        if (r == er && c == ec) {
            cout << dist[r][c] << "\n";
            return 0;
        }

        for (int d = 0; d < 8; ++d) {
            int nr = r + dr[d];
            int nc = c + dc[d];
            if (nr >= 0 && nr < n && nc >= 0 && nc < m && dist[nr][nc] == -1) {
                dist[nr][nc] = dist[r][c] + 1;
                q.push({nr, nc});
            }
        }
    }

    cout << dist[er][ec] << "\n";
    return 0;
}

```

### `CPPB-GRD-10` — Duong Kinh Cua Cay

```cpp
#include <bits/stdc++.h>
using namespace std;

int n;
vector<vector<int>> adj;

pair<int, int> bfs(int start) {
    vector<int> dist(n + 1, -1);
    queue<int> q;
    dist[start] = 0;
    q.push(start);

    int furthest_node = start;
    int max_d = 0;

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        if (dist[u] > max_d) {
            max_d = dist[u];
            furthest_node = u;
        }

        for (int v : adj[u]) {
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }
    return {furthest_node, max_d};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;
    if (n <= 1) { cout << 0 << "\n"; return 0; }

    adj.assign(n + 1, vector<int>());
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    auto [u, d1] = bfs(1);
    auto [v, diameter] = bfs(u);

    cout << diameter << "\n";
    return 0;
}

```

### `CPPB-GRD-11` — Kich Thuoc Cay Con Va Trong Tam Cay

```cpp
#include <bits/stdc++.h>
using namespace std;

int n;
vector<vector<int>> adj;
vector<int> sz;
int centroid_node = -1;

void dfs(int u, int p) {
    sz[u] = 1;
    bool is_centroid = true;

    for (int v : adj[u]) {
        if (v != p) {
            dfs(v, u);
            sz[u] += sz[v];
            if (sz[v] > n / 2) is_centroid = false;
        }
    }

    if (n - sz[u] > n / 2) is_centroid = false;
    if (is_centroid && centroid_node == -1) centroid_node = u;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    adj.assign(n + 1, vector<int>());
    sz.assign(n + 1, 0);

    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    dfs(1, 0);
    cout << centroid_node << "\n";
    return 0;
}

```

### `CPPB-GRD-12` — Me Cung Co Cua Dich Chuyen Tuc Thoi

```cpp
#include <bits/stdc++.h>
using namespace std;

const int dr[] = {-1, 1, 0, 0};
const int dc[] = {0, 0, -1, 1};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<string> grid(n);
    vector<vector<pair<int, int>>> teleports(26);

    for (int r = 0; r < n; ++r) {
        cin >> grid[r];
        for (int c = 0; c < m; ++c) {
            if (isupper(grid[r][c])) {
                teleports[grid[r][c] - 'A'].push_back({r, c});
            }
        }
    }

    vector<vector<int>> dist(n, vector<int>(m, -1));
    vector<bool> teleport_used(26, false);
    queue<pair<int, int>> q;

    dist[0][0] = 0;
    q.push({0, 0});

    while (!q.empty()) {
        auto [r, c] = q.front();
        q.pop();

        if (r == n - 1 && c == m - 1) {
            cout << dist[r][c] << "\n";
            return 0;
        }

        // Dịch chuyển tức thời
        if (isupper(grid[r][c])) {
            int ch = grid[r][c] - 'A';
            if (!teleport_used[ch]) {
                teleport_used[ch] = true;
                for (auto [tr, tc] : teleports[ch]) {
                    if (dist[tr][tc] == -1) {
                        dist[tr][tc] = dist[r][c];
                        q.push({tr, tc});
                    }
                }
            }
        }

        for (int d = 0; d < 4; ++d) {
            int nr = r + dr[d];
            int nc = c + dc[d];
            if (nr >= 0 && nr < n && nc >= 0 && nc < m && grid[nr][nc] != '#' && dist[nr][nc] == -1) {
                dist[nr][nc] = dist[r][c] + 1;
                q.push({nr, nc});
            }
        }
    }

    cout << dist[n - 1][m - 1] << "\n";
    return 0;
}

```

### `CPPB-GRD-13` — Lam Day Ho Chua Nuoc Rotting Oranges

```cpp
#include <bits/stdc++.h>
using namespace std;

const int dr[] = {-1, 1, 0, 0};
const int dc[] = {0, 0, -1, 1};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<string> grid(n);
    queue<pair<int, int>> q;
    int fresh_count = 0;

    for (int r = 0; r < n; ++r) {
        cin >> grid[r];
        for (int c = 0; c < m; ++c) {
            if (grid[r][c] == '2') q.push({r, c});
            else if (grid[r][c] == '1') fresh_count++;
        }
    }

    int minutes = 0;
    while (!q.empty() && fresh_count > 0) {
        int sz = q.size();
        minutes++;
        while (sz--) {
            auto [r, c] = q.front();
            q.pop();

            for (int d = 0; d < 4; ++d) {
                int nr = r + dr[d];
                int nc = c + dc[d];
                if (nr >= 0 && nr < n && nc >= 0 && nc < m && grid[nr][nc] == '1') {
                    grid[nr][nc] = '2';
                    fresh_count--;
                    q.push({nr, nc});
                }
            }
        }
    }

    if (fresh_count > 0) cout << -1 << "\n";
    else cout << minutes << "\n";
    return 0;
}

```

### `CPPB-GRD-14` — Hon Dao Nhan Tao Lon Nhat

```cpp
#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<string> grid;
vector<vector<int>> island_id;
vector<int> island_size;

const int dr[] = {-1, 1, 0, 0};
const int dc[] = {0, 0, -1, 1};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> m)) return 0;
    grid.resize(n);
    for (int i = 0; i < n; ++i) cin >> grid[i];

    island_id.assign(n, vector<int>(m, 0));
    island_size.push_back(0); // id 0 unused
    int current_id = 1;
    int max_area = 0;

    for (int r = 0; r < n; ++r) {
        for (int c = 0; c < m; ++c) {
            if (grid[r][c] == '1' && island_id[r][c] == 0) {
                int sz = 0;
                island_id[r][c] = current_id;
                queue<pair<int, int>> q;
                q.push({r, c});

                while (!q.empty()) {
                    auto [cr, cc] = q.front();
                    q.pop();
                    sz++;

                    for (int d = 0; d < 4; ++d) {
                        int nr = cr + dr[d];
                        int nc = cc + dc[d];
                        if (nr >= 0 && nr < n && nc >= 0 && nc < m && grid[nr][nc] == '1' && island_id[nr][nc] == 0) {
                            island_id[nr][nc] = current_id;
                            q.push({nr, nc});
                        }
                    }
                }

                island_size.push_back(sz);
                max_area = max(max_area, sz);
                current_id++;
            }
        }
    }

    for (int r = 0; r < n; ++r) {
        for (int c = 0; c < m; ++c) {
            if (grid[r][c] == '0') {
                unordered_set<int> neighbor_ids;
                for (int d = 0; d < 4; ++d) {
                    int nr = r + dr[d];
                    int nc = c + dc[d];
                    if (nr >= 0 && nr < n && nc >= 0 && nc < m && island_id[nr][nc] > 0) {
                        neighbor_ids.insert(island_id[nr][nc]);
                    }
                }
                int combined_sz = 1;
                for (int id : neighbor_ids) combined_sz += island_size[id];
                max_area = max(max_area, combined_sz);
            }
        }
    }

    cout << max_area << "\n";
    return 0;
}

```

### `CPPB-GRD-15` — Thoat Khoi Me Cung Quai Vat

```cpp
#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;
const int dr[] = {-1, 1, 0, 0};
const int dc[] = {0, 0, -1, 1};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<string> grid(n);
    queue<pair<int, int>> mq;
    vector<vector<int>> monster_dist(n, vector<int>(m, INF));
    int ar = -1, ac = -1;

    for (int r = 0; r < n; ++r) {
        cin >> grid[r];
        for (int c = 0; c < m; ++c) {
            if (grid[r][c] == 'M') {
                monster_dist[r][c] = 0;
                mq.push({r, c});
            } else if (grid[r][c] == 'A') {
                ar = r; ac = c;
            }
        }
    }

    while (!mq.empty()) {
        auto [r, c] = mq.front();
        mq.pop();

        for (int d = 0; d < 4; ++d) {
            int nr = r + dr[d];
            int nc = c + dc[d];
            if (nr >= 0 && nr < n && nc >= 0 && nc < m && grid[nr][nc] != '#' && monster_dist[nr][nc] == INF) {
                monster_dist[nr][nc] = monster_dist[r][c] + 1;
                mq.push({nr, nc});
            }
        }
    }

    vector<vector<int>> player_dist(n, vector<int>(m, -1));
    queue<pair<int, int>> pq;

    player_dist[ar][ac] = 0;
    pq.push({ar, ac});

    while (!pq.empty()) {
        auto [r, c] = pq.front();
        pq.pop();

        if (r == 0 || r == n - 1 || c == 0 || c == m - 1) {
            cout << "YES\n";
            return 0;
        }

        for (int d = 0; d < 4; ++d) {
            int nr = r + dr[d];
            int nc = c + dc[d];
            if (nr >= 0 && nr < n && nc >= 0 && nc < m && grid[nr][nc] != '#' && player_dist[nr][nc] == -1) {
                if (player_dist[r][c] + 1 < monster_dist[nr][nc]) {
                    player_dist[nr][nc] = player_dist[r][c] + 1;
                    pq.push({nr, nc});
                }
            }
        }
    }

    cout << "NO\n";
    return 0;
}

```

## Chương 07 — Bài 21: Segment Tree & Fenwick Tree

### `CPPB-RNG-01` — Cai Dat Fenwick Tree Tinh Tong Doan

```cpp
#include <bits/stdc++.h>
using namespace std;

struct FenwickTree {
    int n;
    vector<long long> bit;
    FenwickTree(int n) : n(n), bit(n + 1, 0) {}

    void update(int x, long long val) {
        for (; x <= n; x += x & -x) bit[x] += val;
    }

    long long query(int x) {
        long long sum = 0;
        for (; x > 0; x -= x & -x) sum += bit[x];
        return sum;
    }

    long long queryRange(int l, int r) {
        if (l > r) return 0;
        return query(r) - query(l - 1);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;
    if (n <= 0) return 0;

    FenwickTree ft(n);
    for (int i = 1; i <= n; ++i) {
        long long x;
        cin >> x;
        ft.update(i, x);
    }

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int pos;
            long long val;
            cin >> pos >> val;
            ft.update(pos, val);
        } else {
            int l, r;
            cin >> l >> r;
            cout << ft.queryRange(l, r) << "\n";
        }
    }
    return 0;
}

```

### `CPPB-RNG-02` — Cai Dat Segment Tree Tim Min Doan

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long INF = 1e18;

struct SegmentTree {
    int n;
    vector<long long> tree;
    SegmentTree(int n) : n(n), tree(4 * n + 5, INF) {}

    void build(const vector<long long>& a, int id, int l, int r) {
        if (l == r) {
            tree[id] = a[l];
            return;
        }
        int mid = (l + r) / 2;
        build(a, 2 * id, l, mid);
        build(a, 2 * id + 1, mid + 1, r);
        tree[id] = min(tree[2 * id], tree[2 * id + 1]);
    }

    void update(int id, int l, int r, int pos, long long val) {
        if (l == r) {
            tree[id] = val;
            return;
        }
        int mid = (l + r) / 2;
        if (pos <= mid) update(2 * id, l, mid, pos, val);
        else update(2 * id + 1, mid + 1, r, pos, val);
        tree[id] = min(tree[2 * id], tree[2 * id + 1]);
    }

    long long query(int id, int l, int r, int u, int v) {
        if (v < l || r < u) return INF;
        if (u <= l && r <= v) return tree[id];
        int mid = (l + r) / 2;
        return min(query(2 * id, l, mid, u, v), query(2 * id + 1, mid + 1, r, u, v));
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;
    if (n <= 0) return 0;

    vector<long long> a(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    SegmentTree st(n);
    st.build(a, 1, 1, n);

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int pos;
            long long val;
            cin >> pos >> val;
            st.update(1, 1, n, pos, val);
        } else {
            int l, r;
            cin >> l >> r;
            cout << st.query(1, 1, n, l, r) << "\n";
        }
    }
    return 0;
}

```

### `CPPB-RNG-03` — Cap Nhat Doan Va Truy Van Diem Bit

```cpp
#include <bits/stdc++.h>
using namespace std;

struct FenwickTree {
    int n;
    vector<long long> bit;
    FenwickTree(int n) : n(n), bit(n + 2, 0) {}

    void update(int x, long long val) {
        for (; x <= n; x += x & -x) bit[x] += val;
    }

    long long query(int x) {
        long long sum = 0;
        for (; x > 0; x -= x & -x) sum += bit[x];
        return sum;
    }

    void updateRange(int l, int r, long long val) {
        update(l, val);
        update(r + 1, -val);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;
    if (n <= 0) return 0;

    FenwickTree ft(n);
    vector<long long> a(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
        ft.updateRange(i, i, a[i]);
    }

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) { // Cộng val vào [L, R]
            int l, r;
            long long val;
            cin >> l >> r >> val;
            ft.updateRange(l, r, val);
        } else { // Hỏi giá trị tại pos
            int pos;
            cin >> pos;
            cout << ft.query(pos) << "\n";
        }
    }
    return 0;
}

```

### `CPPB-RNG-04` — Tim Gia Tri Lon Nhat Va Dem So Lan Xuat Hien

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Node {
    long long max_val;
    int count;
};

Node mergeNodes(Node a, Node b) {
    if (a.max_val > b.max_val) return a;
    if (b.max_val > a.max_val) return b;
    return {a.max_val, a.count + b.count};
}

struct SegmentTree {
    int n;
    vector<Node> tree;
    SegmentTree(int n) : n(n), tree(4 * n + 5) {}

    void build(const vector<long long>& a, int id, int l, int r) {
        if (l == r) {
            tree[id] = {a[l], 1};
            return;
        }
        int mid = (l + r) / 2;
        build(a, 2 * id, l, mid);
        build(a, 2 * id + 1, mid + 1, r);
        tree[id] = mergeNodes(tree[2 * id], tree[2 * id + 1]);
    }

    void update(int id, int l, int r, int pos, long long val) {
        if (l == r) {
            tree[id] = {val, 1};
            return;
        }
        int mid = (l + r) / 2;
        if (pos <= mid) update(2 * id, l, mid, pos, val);
        else update(2 * id + 1, mid + 1, r, pos, val);
        tree[id] = mergeNodes(tree[2 * id], tree[2 * id + 1]);
    }

    Node query(int id, int l, int r, int u, int v) {
        if (v < l || r < u) return {LLONG_MIN, 0};
        if (u <= l && r <= v) return tree[id];
        int mid = (l + r) / 2;
        return mergeNodes(query(2 * id, l, mid, u, v), query(2 * id + 1, mid + 1, r, u, v));
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;
    if (n <= 0) return 0;

    vector<long long> a(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    SegmentTree st(n);
    st.build(a, 1, 1, n);

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int pos;
            long long val;
            cin >> pos >> val;
            st.update(1, 1, n, pos, val);
        } else {
            int l, r;
            cin >> l >> r;
            Node res = st.query(1, 1, n, l, r);
            cout << res.max_val << " " << res.count << "\n";
        }
    }
    return 0;
}

```

### `CPPB-RNG-05` — Dem So Cap Nghich The Inversion Count

```cpp
#include <bits/stdc++.h>
using namespace std;

struct FenwickTree {
    int n;
    vector<int> bit;
    FenwickTree(int n) : n(n), bit(n + 1, 0) {}

    void update(int x, int val) {
        for (; x <= n; x += x & -x) bit[x] += val;
    }

    int query(int x) {
        int sum = 0;
        for (; x > 0; x -= x & -x) sum += bit[x];
        return sum;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    // Nén tọa độ
    vector<long long> vals = a;
    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());

    int sz = vals.size();
    FenwickTree ft(sz);
    long long inv_count = 0;

    for (int i = n - 1; i >= 0; --i) {
        int rank = lower_bound(vals.begin(), vals.end(), a[i]) - vals.begin() + 1;
        inv_count += ft.query(rank - 1);
        ft.update(rank, 1);
    }

    cout << inv_count << "\n";
    return 0;
}

```

### `CPPB-RNG-06` — Truy Van Uoc Chung Lon Nhat Doan

```cpp
#include <bits/stdc++.h>
using namespace std;

struct SegmentTree {
    int n;
    vector<long long> tree;
    SegmentTree(int n) : n(n), tree(4 * n + 5, 0) {}

    void build(const vector<long long>& a, int id, int l, int r) {
        if (l == r) {
            tree[id] = a[l];
            return;
        }
        int mid = (l + r) / 2;
        build(a, 2 * id, l, mid);
        build(a, 2 * id + 1, mid + 1, r);
        tree[id] = std::gcd(tree[2 * id], tree[2 * id + 1]);
    }

    void update(int id, int l, int r, int pos, long long val) {
        if (l == r) {
            tree[id] = val;
            return;
        }
        int mid = (l + r) / 2;
        if (pos <= mid) update(2 * id, l, mid, pos, val);
        else update(2 * id + 1, mid + 1, r, pos, val);
        tree[id] = std::gcd(tree[2 * id], tree[2 * id + 1]);
    }

    long long query(int id, int l, int r, int u, int v) {
        if (v < l || r < u) return 0;
        if (u <= l && r <= v) return tree[id];
        int mid = (l + r) / 2;
        return std::gcd(query(2 * id, l, mid, u, v), query(2 * id + 1, mid + 1, r, u, v));
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;
    if (n <= 0) return 0;

    vector<long long> a(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    SegmentTree st(n);
    st.build(a, 1, 1, n);

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int pos;
            long long val;
            cin >> pos >> val;
            st.update(1, 1, n, pos, val);
        } else {
            int l, r;
            cin >> l >> r;
            cout << st.query(1, 1, n, l, r) << "\n";
        }
    }
    return 0;
}

```

### `CPPB-RNG-07` — Tim Phan Tu Thu K Nho Nhat

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAX_VAL = 200000;

struct FenwickTree {
    int bit[MAX_VAL + 5];
    FenwickTree() { memset(bit, 0, sizeof(bit)); }

    void update(int x, int val) {
        for (; x <= MAX_VAL; x += x & -x) bit[x] += val;
    }

    int findKth(int k) {
        int idx = 0;
        for (int i = 1 << 18; i > 0; i >>= 1) {
            if (idx + i <= MAX_VAL && bit[idx + i] < k) {
                idx += i;
                k -= bit[idx];
            }
        }
        return idx + 1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;

    FenwickTree ft;

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int x;
            cin >> x;
            ft.update(x, 1);
        } else {
            int k;
            cin >> k;
            cout << ft.findKth(k) << "\n";
        }
    }
    return 0;
}

```

### `CPPB-RNG-08` — Tim Vi Tri Dau Tien Co Gia Tri Ge X

```cpp
#include <bits/stdc++.h>
using namespace std;

struct SegmentTree {
    int n;
    vector<long long> tree;
    SegmentTree(int n) : n(n), tree(4 * n + 5, 0) {}

    void build(const vector<long long>& a, int id, int l, int r) {
        if (l == r) {
            tree[id] = a[l];
            return;
        }
        int mid = (l + r) / 2;
        build(a, 2 * id, l, mid);
        build(a, 2 * id + 1, mid + 1, r);
        tree[id] = max(tree[2 * id], tree[2 * id + 1]);
    }

    void update(int id, int l, int r, int pos, long long val) {
        if (l == r) {
            tree[id] = val;
            return;
        }
        int mid = (l + r) / 2;
        if (pos <= mid) update(2 * id, l, mid, pos, val);
        else update(2 * id + 1, mid + 1, r, pos, val);
        tree[id] = max(tree[2 * id], tree[2 * id + 1]);
    }

    int findFirst(int id, int l, int r, int u, int v, long long x) {
        if (v < l || r < u || tree[id] < x) return -1;
        if (l == r) return l;
        int mid = (l + r) / 2;
        int res = findFirst(2 * id, l, mid, u, v, x);
        if (res != -1) return res;
        return findFirst(2 * id + 1, mid + 1, r, u, v, x);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;
    if (n <= 0) return 0;

    vector<long long> a(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    SegmentTree st(n);
    st.build(a, 1, 1, n);

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int pos;
            long long val;
            cin >> pos >> val;
            st.update(1, 1, n, pos, val);
        } else {
            int l, r;
            long long x;
            cin >> l >> r >> x;
            cout << st.findFirst(1, 1, n, l, r, x) << "\n";
        }
    }
    return 0;
}

```

### `CPPB-RNG-09` — Lis O Nlogn Bang Bit

```cpp
#include <bits/stdc++.h>
using namespace std;

struct FenwickTree {
    int n;
    vector<int> bit;
    FenwickTree(int n) : n(n), bit(n + 1, 0) {}

    void update(int x, int val) {
        for (; x <= n; x += x & -x) bit[x] = max(bit[x], val);
    }

    int query(int x) {
        int max_val = 0;
        for (; x > 0; x -= x & -x) max_val = max(max_val, bit[x]);
        return max_val;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<long long> vals = a;
    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());

    int sz = vals.size();
    FenwickTree ft(sz);
    int ans = 0;

    for (int i = 0; i < n; ++i) {
        int rank = lower_bound(vals.begin(), vals.end(), a[i]) - vals.begin() + 1;
        int best_prev = ft.query(rank - 1);
        int cur_lis = best_prev + 1;
        ans = max(ans, cur_lis);
        ft.update(rank, cur_lis);
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB-RNG-10` — Doan Con Co Tong Lon Nhat Max Sub Sum

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Node {
    long long sum, pref, suff, ans;
};

Node makeNode(long long val) {
    long long p = max(0LL, val);
    return {val, p, p, p};
}

Node mergeNodes(Node l, Node r) {
    Node res;
    res.sum = l.sum + r.sum;
    res.pref = max(l.pref, l.sum + r.pref);
    res.suff = max(r.suff, r.sum + l.suff);
    res.ans = max({l.ans, r.ans, l.suff + r.pref});
    return res;
}

struct SegmentTree {
    int n;
    vector<Node> tree;
    SegmentTree(int n) : n(n), tree(4 * n + 5) {}

    void build(const vector<long long>& a, int id, int l, int r) {
        if (l == r) {
            tree[id] = makeNode(a[l]);
            return;
        }
        int mid = (l + r) / 2;
        build(a, 2 * id, l, mid);
        build(a, 2 * id + 1, mid + 1, r);
        tree[id] = mergeNodes(tree[2 * id], tree[2 * id + 1]);
    }

    void update(int id, int l, int r, int pos, long long val) {
        if (l == r) {
            tree[id] = makeNode(val);
            return;
        }
        int mid = (l + r) / 2;
        if (pos <= mid) update(2 * id, l, mid, pos, val);
        else update(2 * id + 1, mid + 1, r, pos, val);
        tree[id] = mergeNodes(tree[2 * id], tree[2 * id + 1]);
    }

    Node query(int id, int l, int r, int u, int v) {
        if (v < l || r < u) return {0, 0, 0, 0};
        if (u <= l && r <= v) return tree[id];
        int mid = (l + r) / 2;
        return mergeNodes(query(2 * id, l, mid, u, v), query(2 * id + 1, mid + 1, r, u, v));
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;
    if (n <= 0) return 0;

    vector<long long> a(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    SegmentTree st(n);
    st.build(a, 1, 1, n);

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int pos;
            long long val;
            cin >> pos >> val;
            st.update(1, 1, n, pos, val);
        } else {
            int l, r;
            cin >> l >> r;
            cout << st.query(1, 1, n, l, r).ans << "\n";
        }
    }
    return 0;
}

```

### `CPPB-RNG-11` — Dem So Diem Nam Trong Hinh Chu Nhat

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Point {
    int x, y;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<Point> pts(n);
    for (int i = 0; i < n; ++i) cin >> pts[i].x >> pts[i].y;

    while (q--) {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        int count = 0;
        for (int i = 0; i < n; ++i) {
            if (pts[i].x >= x1 && pts[i].x <= x2 && pts[i].y >= y1 && pts[i].y <= y2) {
                count++;
            }
        }
        cout << count << "\n";
    }
    return 0;
}

```

### `CPPB-RNG-12` — Doi Dau Doan Va Tim Tong Lon Nhat

```cpp
#include <bits/stdc++.h>
using namespace std;

struct FenwickTree {
    int n;
    vector<long long> bit;
    FenwickTree(int n) : n(n), bit(n + 1, 0) {}

    void update(int x, long long val) {
        for (; x <= n; x += x & -x) bit[x] += val;
    }

    long long query(int x) {
        long long sum = 0;
        for (; x > 0; x -= x & -x) sum += bit[x];
        return sum;
    }

    long long queryRange(int l, int r) {
        if (l > r) return 0;
        return query(r) - query(l - 1);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;
    if (n <= 0) return 0;

    FenwickTree ft(n);
    for (int i = 1; i <= n; ++i) {
        long long x;
        cin >> x;
        ft.update(i, x);
    }

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int pos;
            long long val;
            cin >> pos >> val;
            ft.update(pos, val);
        } else {
            int l, r;
            cin >> l >> r;
            cout << ft.queryRange(l, r) << "\n";
        }
    }
    return 0;
}

```

### `CPPB-RNG-13` — Cay Fenwick 2d Doc Lap

```cpp
#include <bits/stdc++.h>
using namespace std;

int n, m, q;
vector<vector<long long>> bit;

void update(int r, int c, long long val) {
    for (int i = r; i <= n; i += i & -i) {
        for (int j = c; j <= m; j += j & -j) {
            bit[i][j] += val;
        }
    }
}

long long query(int r, int c) {
    long long sum = 0;
    for (int i = r; i > 0; i -= i & -i) {
        for (int j = c; j > 0; j -= j & -j) {
            sum += bit[i][j];
        }
    }
    return sum;
}

long long queryRange(int r1, int c1, int r2, int c2) {
    return query(r2, c2) - query(r1 - 1, c2) - query(r2, c1 - 1) + query(r1 - 1, c1 - 1);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> m >> q)) return 0;

    bit.assign(n + 1, vector<long long>(m + 1, 0));

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int r, c;
            long long val;
            cin >> r >> c >> val;
            update(r, c, val);
        } else {
            int r1, c1, r2, c2;
            cin >> r1 >> c1 >> r2 >> c2;
            cout << queryRange(r1, c1, r2, c2) << "\n";
        }
    }
    return 0;
}

```

### `CPPB-RNG-14` — Gioi Thieu Lazy Propagation Cong Doan

```cpp
#include <bits/stdc++.h>
using namespace std;

struct SegmentTreeLazy {
    int n;
    vector<long long> tree, lazy;
    SegmentTreeLazy(int n) : n(n), tree(4 * n + 5, 0), lazy(4 * n + 5, 0) {}

    void push(int id, int l, int r) {
        if (lazy[id] != 0) {
            int mid = (l + r) / 2;
            tree[2 * id] += lazy[id] * (mid - l + 1);
            lazy[2 * id] += lazy[id];
            tree[2 * id + 1] += lazy[id] * (r - mid);
            lazy[2 * id + 1] += lazy[id];
            lazy[id] = 0;
        }
    }

    void build(const vector<long long>& a, int id, int l, int r) {
        if (l == r) {
            tree[id] = a[l];
            return;
        }
        int mid = (l + r) / 2;
        build(a, 2 * id, l, mid);
        build(a, 2 * id + 1, mid + 1, r);
        tree[id] = tree[2 * id] + tree[2 * id + 1];
    }

    void updateRange(int id, int l, int r, int u, int v, long long val) {
        if (v < l || r < u) return;
        if (u <= l && r <= v) {
            tree[id] += val * (r - l + 1);
            lazy[id] += val;
            return;
        }
        push(id, l, r);
        int mid = (l + r) / 2;
        updateRange(2 * id, l, mid, u, v, val);
        updateRange(2 * id + 1, mid + 1, r, u, v, val);
        tree[id] = tree[2 * id] + tree[2 * id + 1];
    }

    long long query(int id, int l, int r, int u, int v) {
        if (v < l || r < u) return 0;
        if (u <= l && r <= v) return tree[id];
        push(id, l, r);
        int mid = (l + r) / 2;
        return query(2 * id, l, mid, u, v) + query(2 * id + 1, mid + 1, r, u, v);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;
    if (n <= 0) return 0;

    vector<long long> a(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    SegmentTreeLazy st(n);
    st.build(a, 1, 1, n);

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int l, r;
            long long val;
            cin >> l >> r >> val;
            st.updateRange(1, 1, n, l, r, val);
        } else {
            int l, r;
            cin >> l >> r;
            cout << st.query(1, 1, n, l, r) << "\n";
        }
    }
    return 0;
}

```

### `CPPB-RNG-15` — He Thong Quan Ly Du Lieu Olympic

```cpp
#include <bits/stdc++.h>
using namespace std;

struct SegmentTreeLazy {
    int n;
    vector<long long> tree, lazy;
    SegmentTreeLazy(int n) : n(n), tree(4 * n + 5, 0), lazy(4 * n + 5, 0) {}

    void push(int id, int l, int r) {
        if (lazy[id] != 0) {
            int mid = (l + r) / 2;
            tree[2 * id] += lazy[id] * (mid - l + 1);
            lazy[2 * id] += lazy[id];
            tree[2 * id + 1] += lazy[id] * (r - mid);
            lazy[2 * id + 1] += lazy[id];
            lazy[id] = 0;
        }
    }

    void build(const vector<long long>& a, int id, int l, int r) {
        if (l == r) {
            tree[id] = a[l];
            return;
        }
        int mid = (l + r) / 2;
        build(a, 2 * id, l, mid);
        build(a, 2 * id + 1, mid + 1, r);
        tree[id] = tree[2 * id] + tree[2 * id + 1];
    }

    void updateRange(int id, int l, int r, int u, int v, long long val) {
        if (v < l || r < u) return;
        if (u <= l && r <= v) {
            tree[id] += val * (r - l + 1);
            lazy[id] += val;
            return;
        }
        push(id, l, r);
        int mid = (l + r) / 2;
        updateRange(2 * id, l, mid, u, v, val);
        updateRange(2 * id + 1, mid + 1, r, u, v, val);
        tree[id] = tree[2 * id] + tree[2 * id + 1];
    }

    long long query(int id, int l, int r, int u, int v) {
        if (v < l || r < u) return 0;
        if (u <= l && r <= v) return tree[id];
        push(id, l, r);
        int mid = (l + r) / 2;
        return query(2 * id, l, mid, u, v) + query(2 * id + 1, mid + 1, r, u, v);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;
    if (n <= 0) return 0;

    vector<long long> a(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    SegmentTreeLazy st(n);
    st.build(a, 1, 1, n);

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int l, r;
            long long val;
            cin >> l >> r >> val;
            st.updateRange(1, 1, n, l, r, val);
        } else {
            int l, r;
            cin >> l >> r;
            cout << st.query(1, 1, n, l, r) << "\n";
        }
    }
    return 0;
}

```




\newpage

# Mục lục


