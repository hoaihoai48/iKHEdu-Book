---
title: "Khoá học C++ cơ bản — Quyển 2"
subtitle: "Quy hoạch động, Cấu trúc dữ liệu & Thuật toán đồ thị"
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
  - \fancyhead[L]{\textit{Khoá học C++ cơ bản — Quyển 2}}
  - \fancyhead[R]{\textit{Trung tâm tin học iKH}}
---


# Lời nói đầu

Cuốn sách **Khoá học C++ cơ bản — QUYỂN 2: QUY HOẠCH ĐỘNG, CẤU TRÚC DỮ LIỆU & THUẬT TOÁN ĐỒ THỊ** được biên soạn bởi **Trung tâm tin học iKH** nhằm cung cấp cho các em học sinh một lộ trình học tập toàn diện, hệ thống và chuyên sâu về lập trình C++ — từ nền tảng cơ bản đến các thuật toán nâng cao trong lập trình thi đấu.

Sách được thiết kế tối ưu cho học sinh ôn luyện thi **Tin học trẻ Bảng B**, **Học sinh giỏi THCS/THPT** và các kỳ thi lập trình thuật toán. Cuốn sách này gồm **3 Chương chuyên sâu (Chương 05 đến Chương 07)** với **9 Bài học** và **143 bài toán thực hành**, đưa học sinh bước vào thế giới của các kỹ thuật thuật toán đỉnh cao: quy hoạch động 1D/2D/chuỗi, cấu trúc dữ liệu STL nâng cao, ngăn xếp đơn điệu (Monotonic Stack), hàng đợi hai đầu (Deque), lý thuyết đồ thị (BFS, DFS, Flood Fill) và cây truy vấn đoạn (Segment Tree, Fenwick Tree).

Mỗi bài học trong sách tuân theo một khung logic sư phạm nhất quán:

- **Khái niệm & bản chất toán học** — giúp học sinh hiểu sâu bản chất thay vì chỉ học vẹt cú pháp.
- **Chứng minh & bất biến thuật toán** — rèn tư duy phân tích toán học nghiêm ngặt.
- **Mẫu cài đặt chuẩn thi đấu** — code C++ sạch, tối ưu, an toàn, sẵn sàng nộp bài.
- **Bẫy lỗi lập trình kinh điển** — cảnh báo những sai lầm và ngộ nhận phổ biến nhất.
- **Bài tập thực hành chi tiết** — mỗi bài toán đều có đề bài chuẩn, ví dụ I/O và ràng buộc toán học rõ ràng.

Toàn bộ code C++ trong sách tuân theo chuẩn thi đấu iKHEDU: sử dụng `#include <bits/stdc++.h>`, Fast I/O và Safe Input, giúp học sinh rèn luyện phong cách lập trình chuyên nghiệp ngay từ đầu.

Chúc các em học tập hiệu quả và chinh phục những giải thưởng cao nhất!

**Trung tâm tin học iKH**

\newpage



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

## Bài tập thực hành


### Bài 01 [CPPB-DP1-01]: Bậc Thang Cơ Bản

**Bối cảnh:** Một cầu thang có $N$ bậc. Mỗi bước bạn có thể bước lên $1$ bậc hoặc $2$ bậc.

**Nhiệm vụ:** Hãy tính số cách khác nhau để leo lên đến đỉnh bậc thứ $N$, lấy dư cho $10^9 + 7$.

**Đầu vào (Input):**

- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10^5$).

**Đầu ra (Output):**

- In ra số cách leo lên bậc $N$ theo modulo $10^9 + 7$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 | 3 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 10^5$.



### Bài 02 [CPPB-DP1-02]: Chú Ếch Nhảy Chi Phí Nhỏ Nhất

**Bối cảnh:** Có $N$ phiến đá đánh số từ $1$ đến $N$, phiến đá $i$ có độ cao $H_i$. Chú ếch ở phiến đá $1$ muốn nhảy tới phiến đá $N$. Từ phiến đá $i$, ếch có thể nhảy tới $i+1$ hoặc $i+2$ với chi phí $|H_i - H_j|$.

**Nhiệm vụ:** Tìm tổng chi phí tối thiểu để ếch nhảy từ phiến đá $1$ tới $N$.

**Đầu vào (Input):**

- Dòng 1: Số nguyên $N$ ($2 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $H_1, H_2, \dots, H_N$ ($1 \le H_i \le 10^4$).

**Đầu ra (Output):**

- In ra tổng chi phí nhỏ nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 <br> 10 30 40 20 | 30 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $2 \le N \le 10^5, 1 \le H_i \le 10^4$.



### Bài 03 [CPPB-DP1-03]: Chú Ếch Nhảy K Bước

**Bối cảnh:** Tương tự bài toán chú ếch, nhưng từ phiến đá $i$, ếch có thể nhảy xa tối đa $K$ bước tới các phiến đá $i+1, i+2, \dots, i+K$.

**Nhiệm vụ:** Tìm tổng chi phí tối thiểu để ếch nhảy từ phiến đá $1$ tới $N$.

**Đầu vào (Input):**

- Dòng 1: Hai số nguyên $N$ và $K$ ($2 \le N \le 10^5, 1 \le K \le 100$).
- Dòng 2: $N$ số nguyên $H_1, H_2, \dots, H_N$ ($1 \le H_i \le 10^4$).

**Đầu ra (Output):**

- In ra chi phí tối thiểu.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 3 <br> 10 30 40 50 20 | 30 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $2 \le N \le 10^5, 1 \le K \le 100$.



### Bài 04 [CPPB-DP1-04]: Đổi Tiền Số Xu Ít Nhất

**Bối cảnh:** Cho $N$ mệnh giá đồng xu và số tiền mục tiêu $S$. Mỗi mệnh giá có số lượng không giới hạn.

**Nhiệm vụ:** Tìm số lượng đồng xu ít nhất để đổi được đúng số tiền $S$. Nếu không đổi được in -1.

**Đầu vào (Input):**

- Dòng 1: Hai số nguyên $N$ và $S$ ($1 \le N \le 100, 1 \le S \le 10^5$).
- Dòng 2: $N$ số nguyên dương biểu diễn các mệnh giá xu ($1 \le c_i \le 10^4$).

**Đầu ra (Output):**

- Số lượng đồng xu ít nhất hoặc -1 nếu không thể đổi.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 11 <br> 1 5 6 | 2 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 100, 1 \le S \le 10^5$.



### Bài 05 [CPPB-DP1-05]: Đếm Số Cách Đổi Tiền

**Bối cảnh:** Cho $N$ loại đồng xu và số tiền $S$. Mỗi loại xu có số lượng không giới hạn.

**Nhiệm vụ:** Đếm số tổ hợp khác nhau để tạo thành số tiền $S$ lấy dư theo modulo $10^9+7$ (hai cách chỉ khác nhau về thứ tự xu được tính là 1 cách).

**Đầu vào (Input):**

- Dòng 1: $N$ và $S$ ($1 \le N \le 100, 1 \le S \le 10^5$).
- Dòng 2: $N$ số nguyên dương $c_i$ ($1 \le c_i \le 10^4$).

**Đầu ra (Output):**

- Số cách đổi tiền theo modulo $10^9 + 7$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 9 <br> 2 3 5 | 3 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 100, 1 \le S \le 10^5$.



### Bài 06 [CPPB-DP1-06]: Tổng Đoạn Con Không Liền Kề Lớn Nhất

**Bối cảnh:** Cho mảng $A$ gồm $N$ số nguyên không âm. Cần chọn một tập hợp các phần tử sao cho không có 2 phần tử nào đứng cạnh nhau trong mảng.

**Nhiệm vụ:** Tìm tổng lớn nhất của các phần tử được chọn.

**Đầu vào (Input):**

- Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên không âm $A_1, A_2, \dots, A_N$ ($0 \le A_i \le 10^9$).

**Đầu ra (Output):**

- In ra tổng lớn nhất tìm được.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 <br> 1 2 3 1 | 4 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 10^5, 0 \le A_i \le 10^9$.



### Bài 07 [CPPB-DP1-07]: Lát Gạch Bảng 2xN

**Bối cảnh:** Cần lát kín một sàn nhà kích thước $2 \times N$ bằng các viên gạch kích thước $2 \times 1$ và $1 \times 2$.

**Nhiệm vụ:** Tính số cách lát kín sàn nhà modulo $10^9 + 7$.

**Đầu vào (Input):**

- Một dòng chứa số nguyên dương $N$ ($1 \le N \le 10^5$).

**Đầu ra (Output):**

- Số cách lát theo modulo $10^9 + 7$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 | 5 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 10^5$.



### Bài 08 [CPPB-DP1-08]: Lát Gạch Bảng 3xN

**Bối cảnh:** Cần lát kín một bảng kích thước $3 \times N$ bằng các viên gạch domino $2 \times 1$.

**Nhiệm vụ:** Tính số cách lát kín bảng modulo $10^9+7$. Nếu không thể lát kín in 0.

**Đầu vào (Input):**

- Một dòng chứa số nguyên dương $N$ ($1 \le N \le 10^5$).

**Đầu ra (Output):**

- Số cách lát theo modulo $10^9 + 7$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 2 | 3 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 10^5$.



### Bài 09 [CPPB-DP1-09]: Dãy Con Tăng Dài Nhất LIS O(N^2)

**Bối cảnh:** Cho mảng $A$ gồm $N$ số nguyên. Cần tìm độ dài dãy con tăng nghiêm ngặt dài nhất.

**Nhiệm vụ:** In ra độ dài của dãy con tăng dài nhất.

**Đầu vào (Input):**

- Dòng 1: Số nguyên $N$ ($1 \le N \le 2000$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

**Đầu ra (Output):**

- Độ dài LIS.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 6 <br> 10 20 10 30 20 50 | 4 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 2000, 1 \le A_i \le 10^9$.



### Bài 10 [CPPB-DP1-10]: Dãy Con Tăng Dài Nhất LIS O(N log N)

**Bối cảnh:** Cho dãy số $A$ có kích thước lên tới $10^5$. Thuật toán $\mathcal{O}(N^2)$ sẽ bị quá thời gian.

**Nhiệm vụ:** Tìm độ dài của dãy con tăng nghiêm ngặt dài nhất bằng kỹ thuật tìm kiếm nhị phân trên mảng tails $\mathcal{O}(N \log N)$.

**Đầu vào (Input):**

- Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

**Đầu ra (Output):**

- In ra độ dài lớn nhất của dãy con tăng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 6 <br> 5 2 7 4 3 8 | 3 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 10^5, 1 \le A_i \le 10^9$.



### Bài 11 [CPPB-DP1-11]: Truy Vết Dãy Con Tăng Dài Nhất

**Bối cảnh:** Không chỉ tìm độ dài, ta cần in ra chính xác các giá trị của một dãy con tăng dài nhất.

**Nhiệm vụ:** Dòng 1 in độ dài LIS. Dòng 2 in các phần tử của dãy con tăng dài nhất tìm được.

**Đầu vào (Input):**

- Dòng 1: Số nguyên $N$ ($1 \le N \le 2000$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

**Đầu ra (Output):**

- Dòng 1: Độ dài LIS.
- Dòng 2: Các phần tử của dãy con tăng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 <br> 2 1 4 3 5 | 3 <br> 2 4 5 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 2000, 1 \le A_i \le 10^9$.



### Bài 12 [CPPB-DP1-12]: Dãy Con Giảm Dài Nhất (LDS)

**Bối cảnh:** Cho mảng $A$ gồm $N$ số nguyên. Cần tìm độ dài của dãy con giảm nghiêm ngặt dài nhất ($A_{i_1} > A_{i_2} > \dots > A_{i_k}$).

**Nhiệm vụ:** In ra độ dài của dãy con giảm dài nhất.

**Đầu vào (Input):**

- Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

**Đầu ra (Output):**

- Độ dài lớn nhất của dãy con giảm.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 <br> 10 9 2 5 3 7 101 18 | 4 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 10^5, 1 \le A_i \le 10^9$.



### Bài 13 [CPPB-DP1-13]: Dãy Con Hình Sóng Núi (Longest Bitonic Subsequence)

**Bối cảnh:** Một dãy con được gọi là có dạng hình sóng núi (Bitonic) nếu ban đầu tăng dần nghiêm ngặt rồi sau đó giảm dần nghiêm ngặt.

**Nhiệm vụ:** Tìm độ dài lớn nhất của một dãy con hình sóng núi từ mảng ban đầu.

**Đầu vào (Input):**

- Dòng 1: Số nguyên $N$ ($1 \le N \le 2000$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

**Đầu ra (Output):**

- Độ dài lớn nhất của dãy con hình sóng núi.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 8 <br> 1 11 2 10 4 5 2 1 | 6 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 2000, 1 \le A_i \le 10^9$.



### Bài 14 [CPPB-DP1-14]: Tổng Dãy Con Tăng Lớn Nhất (MSIS)

**Bối cảnh:** Cho mảng $A$ gồm $N$ số nguyên dương. Cần tìm một dãy con tăng nghiêm ngặt sao cho tổng giá trị các phần tử trong dãy là lớn nhất.

**Nhiệm vụ:** In ra tổng lớn nhất của dãy con tăng.

**Đầu vào (Input):**

- Dòng 1: Số nguyên $N$ ($1 \le N \le 2000$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

**Đầu ra (Output):**

- Tổng lớn nhất tìm được.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 7 <br> 1 101 2 3 100 4 5 | 106 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 2000, 1 \le A_i \le 10^9$.



### Bài 15 [CPPB-DP1-15]: Tối Ưu Hóa Chuỗi Dự Án Năng Lượng

**Bối cảnh:** Có $N$ dự án năng lượng, mỗi dự án có ngưỡng sản lượng yêu cầu $V_i$ và lợi nhuận $C_i$. Một chuỗi đầu tư hợp lệ chỉ được chọn các dự án có $V$ tăng nghiêm ngặt.

**Nhiệm vụ:** Tìm tổng lợi nhuận lớn nhất có thể đạt được từ một chuỗi đầu tư hợp lệ.

**Đầu vào (Input):**

- Dòng 1: Số nguyên $N$ ($1 \le N \le 2000$).
- $N$ dòng tiếp theo, mỗi dòng gồm 2 số nguyên $V_i, C_i$ ($1 \le V_i, C_i \le 10^9$).

**Đầu ra (Output):**

- Tổng lợi nhuận lớn nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 <br> 10 100 <br> 5 50 <br> 20 200 | 350 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 2000, 1 \le V_i, C_i \le 10^9$.




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

## Bài tập thực hành


### Bài 01 [CPPB-DP2-01]: Đếm Số Cách Đi Trên Lưới

**Bối cảnh:** Trên lưới ô vuông kích thước $N \times M$, một robot xuất phát từ ô $(1, 1)$ và cần di chuyển đến ô $(N, M)$. Mỗi bước robot chỉ có thể di chuyển sang phải $1$ ô hoặc xuống dưới $1$ ô.

**Nhiệm vụ:** Tính số cách đi khác nhau của robot từ ô $(1, 1)$ đến ô $(N, M)$ lấy dư cho $10^9+7$.

**Đầu vào (Input):**

- Một dòng chứa hai số nguyên $N$ và $M$ ($1 \le N, M \le 1000$).

**Đầu ra (Output):**

- Số cách đi theo modulo $10^9 + 7$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 3 | 6 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N, M \le 1000$.



### Bài 02 [CPPB-DP2-02]: Đường Đi Trên Lưới Có Vật Cản

**Bối cảnh:** Ma trận kích thước $N \times M$ có một số ô là vật cản ký hiệu là `#`, các ô đi được ký hiệu là `.`. Robot bắt đầu từ $(1, 1)$ muốn đến $(N, M)$ và chỉ đi sang phải hoặc xuống dưới.

**Nhiệm vụ:** Tính số cách đi không đi qua bất kỳ vật cản nào modulo $10^9+7$.

**Đầu vào (Input):**

- Dòng 1: Hai số nguyên $N$ và $M$ ($1 \le N, M \le 1000$).
- $N$ dòng tiếp theo biểu diễn ma trận.

**Đầu ra (Output):**

- Số cách đi hợp lệ modulo $10^9 + 7$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 3 <br> ... <br> .#. <br> ... | 2 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N, M \le 1000$.



### Bài 03 [CPPB-DP2-03]: Đường Đi Chi Phí Nhỏ Nhất Trên Lưới

**Bối cảnh:** Mỗi ô $(i, j)$ trên ma trận $N \times M$ có chi phí đi qua là $A_{i, j}$. Đi từ $(1, 1)$ đến $(N, M)$ chỉ sang phải hoặc xuống dưới.

**Nhiệm vụ:** Tìm tổng chi phí nhỏ nhất của một đường đi.

**Đầu vào (Input):**

- Dòng 1: Hai số nguyên $N, M$ ($1 \le N, M \le 1000$).
- $N$ dòng tiếp theo: Ma trận chi phí ($0 \le A_{i, j} \le 10^6$).

**Đầu ra (Output):**

- Chi phí nhỏ nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 3 <br> 1 3 1 <br> 1 5 1 <br> 4 2 1 | 7 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N, M \le 1000, 0 \le A_{i, j} \le 10^6$.



### Bài 04 [CPPB-DP2-04]: Nhặt Vàng Trên Lưới

**Bối cảnh:** Mỗi ô $(i, j)$ chứa $A_{i, j}$ lượng vàng. Đi từ $(1, 1)$ đến $(N, M)$ chỉ sang phải hoặc xuống dưới.

**Nhiệm vụ:** Tìm tổng lượng vàng lớn nhất có thể thu thập được.

**Đầu vào (Input):**

- Dòng 1: Hai số $N, M$ ($1 \le N, M \le 1000$).
- $N$ dòng tiếp theo: Ma trận lượng vàng ($0 \le A_{i, j} \le 10^6$).

**Đầu ra (Output):**

- Lượng vàng lớn nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 3 <br> 1 2 3 <br> 0 5 0 <br> 4 1 2 | 13 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N, M \le 1000, 0 \le A_{i, j} \le 10^6$.



### Bài 05 [CPPB-DP2-05]: Cái Túi 0/1 Cơ Bản (0/1 Knapsack)

**Bối cảnh:** Có $N$ món đồ, món thứ $i$ có khối lượng $W_i$ và giá trị $V_i$. Chiếc túi có sức chứa tối đa $W$. Mỗi món chỉ được chọn tối đa 1 lần.

**Nhiệm vụ:** Tìm tổng giá trị lớn nhất của các món đồ được chọn sao cho tổng khối lượng không vượt quá $W$.

**Đầu vào (Input):**

- Dòng 1: Hai số nguyên $N$ và $W$ ($1 \le N \le 1000, 1 \le W \le 10^4$).
- $N$ dòng tiếp theo: Mỗi dòng chứa 2 số $W_i, V_i$ ($1 \le W_i \le W, 1 \le V_i \le 10^6$).

**Đầu ra (Output):**

- Giá trị lớn nhất tìm được.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 7 <br> 1 1 <br> 3 4 <br> 4 5 <br> 5 7 | 9 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 1000, 1 \le W \le 10^4$.



### Bài 06 [CPPB-DP2-06]: Cái Túi Không Giới Hạn (Unbounded Knapsack)

**Bối cảnh:** Có $N$ loại đồ vật với khối lượng $W_i$ và giá trị $V_i$. Mỗi loại đồ vật có thể chọn số lượng không giới hạn.

**Nhiệm vụ:** Tìm tổng giá trị lớn nhất sao cho tổng khối lượng không vượt quá $W$.

**Đầu vào (Input):**

- Dòng 1: Hai số $N$ và $W$ ($1 \le N \le 1000, 1 \le W \le 10^4$).
- $N$ dòng tiếp theo: $W_i, V_i$ ($1 \le W_i \le W, 1 \le V_i \le 10^6$).

**Đầu ra (Output):**

- Tổng giá trị lớn nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 8 <br> 2 10 <br> 3 15 <br> 4 40 | 80 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 1000, 1 \le W \le 10^4$.



### Bài 07 [CPPB-DP2-07]: Truy Vết Món Đồ Cái Túi 0/1

**Bối cảnh:** Cần in ra chính xác các chỉ số của những món đồ được chọn để đạt giá trị lớn nhất trong bài toán cái túi 0/1.

**Nhiệm vụ:** Dòng 1: Giá trị lớn nhất. Dòng 2: Số món đồ được chọn. Dòng 3: Danh sách chỉ số các món đồ theo thứ tự tăng dần.

**Đầu vào (Input):**

- Dòng 1: $N, W$ ($1 \le N \le 500, 1 \le W \le 2000$).
- $N$ dòng tiếp theo: $W_i, V_i$ ($1 \le W_i \le W, 1 \le V_i \le 10^6$).

**Đầu ra (Output):**

- Dòng 1: Max value.
- Dòng 2: Số lượng đồ.
- Dòng 3: Các chỉ số 1-based.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 4 <br> 1 15 <br> 3 20 <br> 4 30 | 35 <br> 2 <br> 1 2 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 500, 1 \le W \le 2000$.



### Bài 08 [CPPB-DP2-08]: Chia Tập Thành Hai Phần Bằng Nhau (Partition Equal Subset Sum)

**Bối cảnh:** Cho mảng gồm $N$ số nguyên dương. Kiểm tra xem có thể chia mảng thành 2 tập hợp con rời nhau sao cho tổng các phần tử ở mỗi tập bằng nhau hay không.

**Nhiệm vụ:** In ra `YES` nếu có thể chia được, ngược lại in `NO`.

**Đầu vào (Input):**

- Dòng 1: Số nguyên $N$ ($1 \le N \le 500$).
- Dòng 2: $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 100$).

**Đầu ra (Output):**

- `YES` hoặc `NO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 <br> 1 5 11 5 | YES |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 500, 1 \le A_i \le 100$.



### Bài 09 [CPPB-DP2-09]: Chia Tập Chênh Lệch Nhỏ Nhất (Minimum Subset Sum Difference)

**Bối cảnh:** Cho $N$ đồ vật có khối lượng $A_i$. Cần chia các món đồ này cho hai người sao cho độ chênh lệch tổng khối lượng giữa hai người là nhỏ nhất có thể.

**Nhiệm vụ:** Tìm độ chênh lệch nhỏ nhất $|S_1 - S_2|$.

**Đầu vào (Input):**

- Dòng 1: Số nguyên $N$ ($1 \le N \le 500$).
- Dòng 2: $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 100$).

**Đầu ra (Output):**

- Độ chênh lệch nhỏ nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 <br> 1 6 11 5 | 1 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 500, 1 \le A_i \le 100$.



### Bài 10 [CPPB-DP2-10]: Tam Giác Số Tổng Lớn Nhất (Triangle DP)

**Bối cảnh:** Cho tam giác số gồm $N$ hàng. Từ vị trí $(i, j)$, ta chỉ có thể di chuyển xuống ô $(i+1, j)$ hoặc $(i+1, j+1)$.

**Nhiệm vụ:** Tìm tổng các số lớn nhất trên đường đi từ đỉnh tam giác $(0, 0)$ xuống hàng đáy.

**Đầu vào (Input):**

- Dòng 1: Số nguyên $N$ ($1 \le N \le 1000$).
- $N$ dòng tiếp theo biểu diễn tam giác số ($0 \le A_{i, j} \le 10^4$).

**Đầu ra (Output):**

- Tổng lớn nhất tìm được.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 <br> 2 <br> 3 4 <br> 6 5 7 <br> 4 1 8 3 | 21 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 1000, 0 \le A_{i, j} \le 10^4$.



### Bài 11 [CPPB-DP2-11]: Đếm Số Tập Con Có Tổng Bằng S

**Bối cảnh:** Cho mảng $A$ gồm $N$ số nguyên dương và số $S$.

**Nhiệm vụ:** Đếm số tập con khác nhau có tổng đúng bằng $S$ lấy dư cho $10^9+7$.

**Đầu vào (Input):**

- Dòng 1: Hai số nguyên $N$ và $S$ ($1 \le N \le 500, 1 \le S \le 5000$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 100$).

**Đầu ra (Output):**

- Số tập con theo modulo $10^9 + 7$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 5 <br> 1 2 3 4 | 2 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 500, 1 \le S \le 5000$.



### Bài 12 [CPPB-DP2-12]: Cái Túi Khối Lượng Cực Đại W <= 10^9 (Đổi Trục DP)

**Bối cảnh:** Trong bài toán cái túi 0/1, khối lượng $W$ có thể lên tới $10^9$ nhưng số lượng đồ vật $N \le 100$ và mỗi giá trị $V_i \le 1000$ (tổng giá trị $\le 10^5$).

**Nhiệm vụ:** Tìm tổng giá trị lớn nhất sao cho tổng khối lượng không vượt quá $W$.

**Đầu vào (Input):**

- Dòng 1: Hai số $N$ và $W$ ($1 \le N \le 100, 1 \le W \le 10^9$).
- $N$ dòng tiếp theo: $W_i, V_i$ ($1 \le W_i \le 10^9, 1 \le V_i \le 1000$).

**Đầu ra (Output):**

- Tổng giá trị lớn nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 8 <br> 3 30 <br> 4 50 <br> 5 60 | 90 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 100, 1 \le W \le 10^9, 1 \le V_i \le 1000$.



### Bài 13 [CPPB-DP2-13]: Hình Vuông Toàn 1 Lớn Nhất (Maximal Square)

**Bối cảnh:** Cho ma trận nhị phân $N \times M$ chỉ gồm các ký tự `'0'` và `'1'`.

**Nhiệm vụ:** Tìm diện tích của hình vuông lớn nhất chỉ chứa toàn các số 1.

**Đầu vào (Input):**

- Dòng 1: Hai số $N$ và $M$ ($1 \le N, M \le 1000$).
- $N$ dòng tiếp theo biểu diễn ma trận.

**Đầu ra (Output):**

- Diện tích hình vuông toàn 1 lớn nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 5 <br> 10100 <br> 10111 <br> 11111 <br> 10010 | 4 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N, M \le 1000$.



### Bài 14 [CPPB-DP2-14]: Đổi Tiền Giới Hạn Số Lượng (Bounded Knapsack)

**Bối cảnh:** Có $N$ loại đồng xu, loại thứ $i$ có mệnh giá $V_i$ và số lượng giới hạn $C_i$.

**Nhiệm vụ:** Tìm số lượng đồng xu ít nhất để tạo thành đúng số tiền $S$. Nếu không thể đổi in -1.

**Đầu vào (Input):**

- Dòng 1: Hai số $N$ và $S$ ($1 \le N \le 100, 1 \le S \le 20000$).
- $N$ dòng tiếp theo: $V_i, C_i$ ($1 \le V_i \le 1000, 1 \le C_i \le 100$).

**Đầu ra (Output):**

- Số đồng xu ít nhất hoặc -1.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 11 <br> 1 2 <br> 5 2 <br> 6 1 | 2 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 100, 1 \le S \le 20000$.



### Bài 15 [CPPB-DP2-15]: Tối Ưu Hóa Túi Đồ Hỗn Hợp (Hybrid Knapsack)

**Bối cảnh:** Có $N$ món đồ thuộc 2 loại: Loại 1 (chỉ được dùng 1 lần) và Loại 2 (được dùng không giới hạn số lần). Chiếc túi có sức chứa tối đa $W$.

**Nhiệm vụ:** Tìm tổng giá trị lớn nhất có thể thu được.

**Đầu vào (Input):**

- Dòng 1: Hai số $N$ và $W$ ($1 \le N \le 100, 1 \le W \le 5000$).
- $N$ dòng tiếp theo: Mỗi dòng gồm 3 số `type`, `weight`, `val` ($type \in \{1, 2\}, 1 \le weight \le W, 1 \le val \le 10^6$).

**Đầu ra (Output):**

- Tổng giá trị lớn nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 10 <br> 1 4 20 <br> 2 3 15 <br> 1 5 30 | 50 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le N \le 100, 1 \le W \le 5000$.




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

## Bài tập thực hành


### Bài 01 [CPPB-DPS-01]: Xâu Con Chung Dài Nhất Cơ Bản (LCS)

**Bối cảnh:** Cho hai chuỗi ký tự $S$ và $T$. Một xâu con chung là một chuỗi xuất hiện trong cả hai chuỗi theo đúng thứ tự tương đối nhưng không nhất thiết phải liền kề.

**Nhiệm vụ:** Tìm độ dài của xâu con chung dài nhất giữa $S$ và $T$.

**Đầu vào (Input):**

- Dòng 1: Chuỗi ký tự $S$ ($1 \le |S| \le 2000$).
- Dòng 2: Chuỗi ký tự $T$ ($1 \le |T| \le 2000$).

**Đầu ra (Output):**

- Độ dài LCS.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| AGGTAB <br> GXTXAYB | 4 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le |S|, |T| \le 2000$.



### Bài 02 [CPPB-DPS-02]: Truy Vết Xâu Con Chung Dài Nhất

**Bối cảnh:** Cần in ra chính xác nội dung của một xâu con chung dài nhất giữa hai chuỗi $S$ và $T$.

**Nhiệm vụ:** Dòng 1: In độ dài LCS. Dòng 2: In chuỗi LCS tìm được.

**Đầu vào (Input):**

- Dòng 1: Chuỗi $S$ ($1 \le |S| \le 2000$).
- Dòng 2: Chuỗi $T$ ($1 \le |T| \le 2000$).

**Đầu ra (Output):**

- Dòng 1: Độ dài LCS.
- Dòng 2: Chuỗi ký tự LCS.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ABCBDAB <br> BDCAB | 4 <br> BDAB |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le |S|, |T| \le 2000$.



### Bài 03 [CPPB-DPS-03]: Khoảng Cách Chỉnh Sửa (Edit Distance / Levenshtein)

**Bối cảnh:** Cho hai chuỗi $S$ và $T$. Bạn có thể thực hiện 3 phép biến đổi: Chèn 1 ký tự, Xóa 1 ký tự, hoặc Thay thế 1 ký tự.

**Nhiệm vụ:** Tìm số phép biến đổi ít nhất để biến chuỗi $S$ thành chuỗi $T$.

**Đầu vào (Input):**

- Dòng 1: Chuỗi $S$ ($1 \le |S| \le 2000$).
- Dòng 2: Chuỗi $T$ ($1 \le |T| \le 2000$).

**Đầu ra (Output):**

- Số phép biến đổi ít nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| horse <br> ros | 3 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le |S|, |T| \le 2000$.



### Bài 04 [CPPB-DPS-04]: Chỉ Dùng Phép Xóa Biến Đổi Hai Xâu

**Bối cảnh:** Cho hai chuỗi $S$ và $T$. Bạn chỉ được phép thực hiện thao tác XÓA ký tự trên chuỗi $S$ hoặc $T$.

**Nhiệm vụ:** Tìm tổng số ký tự ít nhất cần xóa trên cả hai chuỗi để hai chuỗi trở nên giống nhau.

**Đầu vào (Input):**

- Dòng 1: Chuỗi $S$ ($1 \le |S| \le 2000$).
- Dòng 2: Chuỗi $T$ ($1 \le |T| \le 2000$).

**Đầu ra (Output):**

- Tổng số ký tự xóa ít nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| sea <br> eat | 2 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le |S|, |T| \le 2000$.



### Bài 05 [CPPB-DPS-05]: Xâu Con Đối Xứng Dài Nhất (Longest Palindromic Subsequence)

**Bối cảnh:** Một chuỗi đối xứng (Palindrome) đọc xuôi hay đọc ngược đều như nhau. Xâu con không nhất thiết phải liền kề.

**Nhiệm vụ:** Tìm độ dài của dãy con đối xứng dài nhất trong chuỗi $S$.

**Đầu vào (Input):**

- Một dòng chứa chuỗi $S$ ($1 \le |S| \le 2000$).

**Đầu ra (Output):**

- Độ dài lớn nhất của xâu con đối xứng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| bbbab | 4 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le |S| \le 2000$.



### Bài 06 [CPPB-DPS-06]: Đoạn Con Đối Xứng Liên Tiếp Dài Nhất

**Bối cảnh:** Tìm đoạn con LIÊN TIẾP (Substring) đối xứng dài nhất trong chuỗi $S$.

**Nhiệm vụ:** Dòng 1: Độ dài đoạn con đối xứng dài nhất. Dòng 2: Chuỗi đối xứng đó.

**Đầu vào (Input):**

- Một dòng chứa chuỗi $S$ ($1 \le |S| \le 2000$).

**Đầu ra (Output):**

- Dòng 1: Độ dài.
- Dòng 2: Nội dung đoạn con đối xứng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| babad | 3 <br> bab |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le |S| \le 2000$.



### Bài 07 [CPPB-DPS-07]: Đếm Số Đoạn Con Đối Xứng Liên Tiếp

**Bối cảnh:** Cho chuỗi $S$. Cần đếm số lượng các đoạn con liên tiếp khác nhau là chuỗi đối xứng.

**Nhiệm vụ:** In ra tổng số đoạn con đối xứng.

**Đầu vào (Input):**

- Một dòng chứa chuỗi $S$ ($1 \le |S| \le 2000$).

**Đầu ra (Output):**

- Số đoạn con đối xứng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| aaa | 6 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le |S| \le 2000$.



### Bài 08 [CPPB-DPS-08]: Chèn Ít Ký Tự Nhất Tạo Chuỗi Đối Xứng

**Bối cảnh:** Cho chuỗi $S$. Mỗi bước bạn có thể chèn 1 ký tự vào vị trí bất kỳ trong chuỗi.

**Nhiệm vụ:** Tìm số ký tự ít nhất cần chèn để chuỗi $S$ trở thành chuỗi đối xứng.

**Đầu vào (Input):**

- Một dòng chứa chuỗi $S$ ($1 \le |S| \le 2000$).

**Đầu ra (Output):**

- Số ký tự chèn ít nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| zzazz | 0 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le |S| \le 2000$.



### Bài 09 [CPPB-DPS-09]: Xâu Mẹ Chung Ngắn Nhất (Shortest Common Supersequence)

**Bối cảnh:** Một xâu mẹ chung của hai chuỗi $S$ và $T$ là một chuỗi chứa cả $S$ và $T$ như những dãy con.

**Nhiệm vụ:** Tìm độ dài ngắn nhất của xâu mẹ chung.

**Đầu vào (Input):**

- Dòng 1: Chuỗi $S$ ($1 \le |S| \le 2000$).
- Dòng 2: Chuỗi $T$ ($1 \le |T| \le 2000$).

**Đầu ra (Output):**

- Độ dài ngắn nhất của Supersequence.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| abac <br> cab | 5 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le |S|, |T| \le 2000$.



### Bài 10 [CPPB-DPS-10]: Đếm Số Lần Xuất Hiện Xâu Con Rời Rạc (Distinct Subsequences)

**Bối cảnh:** Cho chuỗi $S$ và $T$. Cần đếm số dãy con khác nhau của $S$ bằng đúng chuỗi $T$.

**Nhiệm vụ:** Tính số cách chọn dãy con modulo $10^9+7$.

**Đầu vào (Input):**

- Dòng 1: Chuỗi $S$ ($1 \le |S| \le 2000$).
- Dòng 2: Chuỗi $T$ ($1 \le |T| \le 500$).

**Đầu ra (Output):**

- Số cách chọn theo modulo $10^9 + 7$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| rabbbit <br> rabbit | 3 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le |S| \le 2000, 1 \le |T| \le 500$.



### Bài 11 [CPPB-DPS-11]: Khớp Chuỗi Ký Tự Đại Diện (Wildcard Matching)

**Bối cảnh:** Cho chuỗi $S$ và mẫu $P$. Mẫu $P$ chứa ký tự `?` (khớp với 1 ký tự bất kỳ) và `*` (khớp với dãy ký tự bất kỳ có độ dài $\ge 0$).

**Nhiệm vụ:** In `YES` nếu mẫu $P$ khớp toàn bộ chuỗi $S$, ngược lại in `NO`.

**Đầu vào (Input):**

- Dòng 1: Chuỗi $S$ ($1 \le |S| \le 1000$).
- Dòng 2: Mẫu $P$ ($1 \le |P| \le 1000$).

**Đầu ra (Output):**

- `YES` hoặc `NO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| adceb <br> *a*b | YES |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le |S|, |P| \le 1000$.



### Bài 12 [CPPB-DPS-12]: Xâu Con Chung Của Ba Chuỗi (LCS 3 Strings)

**Bối cảnh:** Cho 3 chuỗi ký tự $S_1, S_2, S_3$. Cần tìm độ dài xâu con chung dài nhất của cả 3 chuỗi.

**Nhiệm vụ:** In ra độ dài LCS của 3 chuỗi.

**Đầu vào (Input):**

- 3 dòng, mỗi dòng chứa một chuỗi ký tự ($1 \le |S_i| \le 100$).

**Đầu ra (Output):**

- Độ dài xâu con chung dài nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| geeks <br> geek <br> geekfor | 4 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le |S_i| \le 100$.



### Bài 13 [CPPB-DPS-13]: Xóa Ít Ký Tự Nhất Để Chuỗi Đối Xứng

**Bối cảnh:** Cho chuỗi $S$. Mỗi bước bạn có thể xóa 1 ký tự bất kỳ.

**Nhiệm vụ:** Tìm số ký tự ít nhất cần xóa để chuỗi còn lại là chuỗi đối xứng.

**Đầu vào (Input):**

- Một dòng chứa chuỗi $S$ ($1 \le |S| \le 2000$).

**Đầu ra (Output):**

- Số ký tự xóa ít nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| aebcbda | 2 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le |S| \le 2000$.



### Bài 14 [CPPB-DPS-14]: Độ Dài LCS Giữa Hai Chuỗi Gen

**Bối cảnh:** Trong phân tích sinh học tính toán, hai chuỗi DNA được so sánh mức độ tương đồng thông qua xâu con chung dài nhất.

**Nhiệm vụ:** In ra độ dài LCS giữa hai chuỗi DNA.

**Đầu vào (Input):**

- Dòng 1: Chuỗi $S$ ($1 \le |S| \le 500$).
- Dòng 2: Chuỗi $T$ ($1 \le |T| \le 500$).

**Đầu ra (Output):**

- Độ dài LCS.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ACCGGTCGAGTGCGCGGAAGCCGGCCGAA <br> GTCGTTCGGAATGCCGTTGCTCTGTAAA | 20 |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le |S|, |T| \le 500$.



### Bài 15 [CPPB-DPS-15]: Tách Từ Trong Chuỗi (Word Break)

**Bối cảnh:** Cho một chuỗi ký tự $S$ và một từ điển gồm $K$ từ. Bạn cần xác định xem chuỗi $S$ có thể được phân tách thành một dãy các từ hợp lệ trong từ điển hay không.

**Nhiệm vụ:** In `YES` nếu có thể phân tách được, ngược lại in `NO`.

**Đầu vào (Input):**

- Dòng 1: Chuỗi $S$ ($1 \le |S| \le 300$).
- Dòng 2: Số nguyên $K$ ($1 \le K \le 100$).
- $K$ dòng tiếp theo chứa các từ trong từ điển.

**Đầu ra (Output):**

- `YES` hoặc `NO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| leetcode <br> 2 <br> leet <br> code | YES |

**Ràng buộc & Giới hạn:**

- $100\%$ số test có $1 \le |S| \le 300, 1 \le K \le 100$.



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


