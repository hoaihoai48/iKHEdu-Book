# Chuyên đề 13: Quy hoạch động 1D & dãy con tăng dài nhất

## 1. Bản chất vấn đề & cầu nối từ đệ quy sang quy hoạch động

Trong Chuyên đề 10 và 12, ta đã chứng kiến hiện tượng **Bùng nổ Không gian Trạng thái (Combinatorial Explosion)** khi duyệt đệ quy phân nhánh:
* Khi tính số Fibonacci $F(N) = F(N-1) + F(N-2)$, trạng thái $F(3)$ bị tính lại $2$ lần, $F(2)$ bị tính lại $3$ lần. Độ phức tạp thời gian tăng vọt lên cấp số nhân $\Theta(\varphi^N) \approx \Theta(1.618^N)$.
* **Nguyên nhân gốc rễ:** Hàm đệ quy thuần túy không có cơ chế "ghi nhớ" (Memory). Mỗi lần bước vào một nhánh mới, nó xem bài toán con đó như một thực thể hoàn toàn xa lạ và tính toán lại từ đầu.

**Quy Hoạch Động (Dynamic Programming - DP)** giải quyết vấn đề này bằng nguyên lý cốt lõi:

> **DP loại bỏ việc tính toán lại các bài toán con trùng lặp bằng cách lưu trữ kết quả vào Bảng phương án (DP Table) và tái sử dụng ngay lập tức trong $\mathcal{O}(1)$.**

![Mô hình Đồ thị trạng thái DAG Quy hoạch động 1D](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-13-quy-hoach-dong-1d/assets/dp_1d_state_dag_vi.svg)

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

![Bài toán Đổi tiền Coin Change và DAG trạng thái](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-13-quy-hoach-dong-1d/assets/coin_change_dag_vi.svg)

### 3.3. Dãy con tăng dài nhất (longest increasing subsequence — LIS $\mathcal{O}(N^2)$)
* **Bối cảnh:** Cho dãy số $A = [a_1, a_2, \dots, a_N]$. Tìm độ dài dãy con tăng nghiêm ngặt dài nhất.
* **State Definition (Tử huyệt định nghĩa):** $dp[i]$ là độ dài của dãy con tăng dài nhất **kết thúc bắt buộc tại phần tử $A[i]$**.
* **Base Cases:** `dp[i] = 1` với mọi $1 \le i \le N$ (bản thân mỗi phần tử đơn lẻ là dãy con độ dài 1).
* **State Transition:** Duyệt qua mọi phần tử $A[j]$ đứng trước $A[i]$ ($1 \le j < i$):
$$dp[i] = 1 + \max_{\{1 \le j < i \mid A[j] < A[i]\}} dp[j]$$
* **Answer Extraction:** Kết quả toàn cục là $\max_{i=1}^N dp[i]$.
* **Độ phức tạp:** $\mathcal{O}(N^2)$ thời gian, $\mathcal{O}(N)$ bộ nhớ. Thường phù hợp với $N$ cỡ vài nghìn, tùy thuộc vào time limit và hệ số hằng số.

![Mô hình Dãy con tăng dài nhất LIS O(N^2) và Truy vết](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-13-quy-hoach-dong-1d/assets/lis_quadratic_model_vi.svg)

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

## 7. Hệ thống câu hỏi kiểm tra khái niệm (Concept Quiz)

#### Câu 1 (Bản chất Quy hoạch động):

Điểm khác biệt cốt lõi nhất giữa Thuật toán Đệ quy thuần túy và Quy hoạch động là gì?

- **A.** Đệ quy chạy nhanh hơn Quy hoạch động.

- **B.** **[Đáp án đúng]** Quy hoạch động loại bỏ việc tính lại bài toán con trùng lặp bằng cách ghi nhớ kết quả trong bảng phương án.

- **C.** Quy hoạch động không sử dụng mảng nhớ.

- **D.** Đệ quy không thể chuyển đổi thành Quy hoạch động.

> *Giải thích:* Quy hoạch động tận dụng tính chất bài toán con trùng lặp (Overlapping Subproblems) và cấu trúc con tối ưu (Optimal Substructure) để lưu kết quả vào bảng $dp$, giảm thời gian từ hàm mũ xuống đa thức.

#### Câu 2 (Bất biến Trạng thái LIS):

Trong thuật toán tìm Dãy con tăng dài nhất LIS $\mathcal{O}(N^2)$, $dp[i]$ đại diện chính xác cho điều gì?

- **A.** Độ dài LIS của đoạn con từ $A[1]$ đến $A[i]$.

- **B.** **[Đáp án đúng]** Độ dài LIS kết thúc bắt buộc tại phần tử $A[i]$.

- **C.** Số lượng dãy con tăng có trong mảng.

- **D.** Giá trị nhỏ nhất của dãy con tăng độ dài $i$.

> *Giải thích:* Bắt buộc $dp[i]$ phải kết thúc tại chính $A[i]$ để khi xét phần tử $A[k]$ đứng sau, ta chỉ cần so sánh điều kiện $A[i] < A[k]$ để quyết định nối dài dãy.

#### Câu 3 (Trường hợp cơ sở Bài toán Bậc thang):

Trong bài toán ếch nhảy bậc thang $dp[i] = dp[i-1] + dp[i-2]$, tại sao giá trị cơ sở $dp[0] = 1$?

- **A.** Vì ếch bắt buộc phải nhảy 1 bước đầu tiên.

- **B.** **[Đáp án đúng]** Vì có đúng một cách để hoàn thành hành trình từ bậc 0 đến bậc 0 — không thực hiện bước nhảy nào.

- **C.** Vì $dp[0]$ không có ý nghĩa toán học nên gán tạm bằng 1.

- **D.** Vì số bậc thang luôn lớn hơn 0.

> *Giải thích:* $dp[0] = 1$ là empty path hợp lệ, đảm bảo khi tính $dp[2] = dp[1] + dp[0] = 1 + 1 = 2$ (gồm bước $1+1$ và bước nhảy thẳng $2$).

#### Câu 4 (Thứ tự tính toán Evaluation Order):

Trong bài toán **Đổi tiền ít đồng xu nhất với hệ thức truy hồi $dp[i] = 1 + \min(dp[i-c])$**, tại sao vòng lặp tính $i$ phải duyệt xuôi từ $1 \to S$?

- **A.** Để in ra các đồng xu theo thứ tự tăng dần.

- **B.** **[Đáp án đúng]** Để đảm bảo mọi giá trị $dp[i - c]$ (với $i - c < i$) đều đã được tính toán tối ưu trước khi dùng.

- **C.** Để tránh tràn bộ nhớ mảng.

- **D.** Vì duyệt ngược sẽ làm tăng độ phức tạp thời gian.

> *Giải thích:* Cấu trúc đồ thị trạng thái DAG quy định trạng thái $i$ phụ thuộc vào các trạng thái nhỏ hơn $i - c$. Do đó các trạng thái nhỏ hơn phải được hoàn tất trước theo thứ tự Topo.

#### Câu 5 (Bẫy số nguyên vô cùng):

Khi khởi tạo mảng $dp$ tìm giá trị nhỏ nhất, giá trị nào sau đây an toàn nhất để tránh tràn số khi cộng thêm 1?

- **A.** `INT_MAX` (khoảng $2 \cdot 10^9$) với kiểu `int`.

- **B.** **[Đáp án đúng]** $1e18$ với kiểu `long long` kèm điều kiện kiểm tra khác vô cùng trước khi cộng.

- **C.** $-1$.

- **D.** $0$.

> *Giải thích:* $INT_MAX + 1$ sẽ bị tràn số nguyên thành số âm cực lớn. Dùng `const long long INF = 1e18;` và luôn kiểm tra `if (dp[v] != INF)` là chuẩn mực an toàn.

#### Câu 6 (Khôi phục vết nghiệm Traceback):

Để khôi phục lại các phần tử thuộc dãy con tăng dài nhất LIS, kỹ thuật nào sau đây là chuẩn mực nhất?

- **A.** Chạy lại thuật toán LIS lần thứ hai.

- **B.** **[Đáp án đúng]** Lưu chỉ số phần tử đứng trước vào mảng `trace[i]`, sau đó lần ngược từ phần tử kết thúc tối ưu về đầu và đảo ngược vector.

- **C.** In trực tiếp mảng $dp$.

- **D.** Dùng thuật toán quay lui vét cạn lại từ đầu.

> *Giải thích:* Mảng `trace[i] = j` lưu vết trực tiếp trong $\mathcal{O}(1)$ tại thời điểm cập nhật $dp[i]$, cho phép truy vết nghiệm trong $\mathcal{O}(N)$.

#### Câu 7 (Độ phức tạp Bài toán Đổi tiền):

Cho $K$ loại đồng xu và số tiền cần đổi $S$. Độ phức tạp thời gian và không gian của thuật toán DP 1D là bao nhiêu?

- **A.** **[Đáp án đúng]** Thời gian $\mathcal{O}(K \cdot S)$, Không gian $\mathcal{O}(S)$.

- **B.** Thời gian $\mathcal{O}(S^2)$, Không gian $\mathcal{O}(K)$.

- **C.** Thời gian $\mathcal{O}(2^K)$, Không gian $\mathcal{O}(S)$.

- **D.** Thời gian $\mathcal{O}(K \log S)$, Không gian $\mathcal{O}(1)$.

> *Giải thích:* Vòng lặp ngoài chạy $S$ bước, vòng lặp trong thử $K$ đồng xu $\implies$ Tổng số phép tính là $K \cdot S$, mảng $dp$ có kích thước $S + 1$.

#### Câu 8 (Bài toán House Robber 1D):

Một tên trộm không được trộm hai ngôi nhà liền kề. Gọi $A[i]$ là số tiền ở nhà $i$. Hệ thức chuyển trạng thái nào sau đây là chính xác cho $dp[i]$ (tiền nhiều nhất trộm được từ $1 \to i$)?

- **A.** $dp[i] = dp[i-1] + A[i]$

- **B.** **[Đáp án đúng]** $dp[i] = \max(dp[i-1], dp[i-2] + A[i])$

- **C.** $dp[i] = \max(dp[i-1], dp[i-2])$

- **D.** $dp[i] = dp[i-2] + A[i]$

> *Giải thích:* Tại nhà $i$, tên trộm có 2 lựa chọn: (1) Không trộm nhà $i \implies$ Nhận $dp[i-1]$; (2) Trộm nhà $i \implies$ Không được trộm nhà $i-1$, nhận $dp[i-2] + A[i]$.

#### Câu 9 (Mô hình Cắt Thanh Gỗ Rod Cutting):

Cho thanh gỗ độ dài $N$ và bảng giá $P[len]$ cho từng đoạn gỗ độ dài $len$. Công thức tính giá trị lớn nhất $dp[i]$ khi cắt thanh gỗ độ dài $i$ là:

- **A.** **[Đáp án đúng]** $dp[i] = \max(\{P[j] + dp[i-j] \mid 1 \le j \le i\})$

- **B.** $dp[i] = P[i]$

- **C.** $dp[i] = dp[i-1] + P[1]$

- **D.** $dp[i] = \sum P[j]$

> *Giải thích:* Thử nhát cắt đầu tiên có độ dài $j \in [1, i]$, giá trị thu được là giá trị đoạn $j$ ($P[j]$) cộng với giá trị tối ưu của phần còn lại độ dài $i-j$ ($dp[i-j]$).

#### Câu 10 (Ranh giới LIS O(N^2) Vs o(n log n)):

Khi $N = 10^5$, tại sao thuật toán LIS $\mathcal{O}(N^2)$ không thể vượt qua giới hạn thời gian 1.0 giây?

- **A.** **[Đáp án đúng]** Vì với $N = 10^5$, thuật toán $\mathcal{O}(N^2)$ phải xét khoảng $N^2/2 \approx 5 \times 10^9$ cặp, thường vượt xa giới hạn thời gian thông thường của CPU trong 1.0 giây. Trong khi $\mathcal{O}(N \log N)$ chỉ cần khoảng $N \log_2 N \approx 1.7 \times 10^6$ bước ở quy mô này.

- **B.** Vì mảng $dp$ chiếm quá nhiều bộ nhớ RAM.

- **C.** Vì hàm `max` trong C++ chạy chậm.

- **D.** Vì số nguyên 64-bit bị tràn.

> *Giải thích:* Thuật toán $\mathcal{O}(N^2)$ thường không phù hợp khi $N$ đạt cỡ $10^4$ trở lên trong các giới hạn thời gian thi đấu thông thường. Cần chuyển sang $\mathcal{O}(N \log N)$ bằng mảng đơn điệu và tìm kiếm nhị phân.

#### Câu 11 (State Transformation — LIS sang MSIS):

Khi chuyển từ bài toán LIS (Độ dài lớn nhất) sang MSIS (Tổng giá trị lớn nhất), thành phần nào trong hệ thức quy hoạch động thay đổi?

- **A.** Điều kiện $A[j] < A[i]$ bị bỏ đi.

- **B.** **[Đáp án đúng]** Giá trị khởi tạo và phép cộng dồn chuyển từ $+1$ (đếm số lượng) sang $+A[i]$ (cộng dồn giá trị phần tử).

- **C.** Mảng $dp$ phải tăng lên 2 chiều.

- **D.** Thứ tự duyệt $i$ phải đảo ngược.

> *Giải thích:* Bất biến chuyển từ đếm độ dài sang cực đại hóa tổng: $dp[i] = A[i] + \max(dp[j])$ với $j < i$ và $A[j] < A[i]$.

#### Câu 12 (State Dimension — Alternating Subsequence):

Tại sao trong bài toán Dãy con đan dấu, ta cần mở rộng trạng thái thành $dp[i][2]$ thay vì chỉ dùng $dp[i]$?

- **A.** Để lưu thêm vị trí của phần tử đứng trước.

- **B.** **[Đáp án đúng]** Vì cần phân biệt trạng thái bước nhảy cuối cùng đang là TĂNG hay GIẢM để so sánh điều kiện kế tiếp.

- **C.** Để giảm độ phức tạp bộ nhớ.

- **D.** Vì mảng có 2 nửa chẵn và lẻ.

> *Giải thích:* Chiều thứ hai mang thông tin ngữ nghĩa: $0$ nghĩa là bước cuối đi xuống, $1$ nghĩa là bước cuối đi lên.

#### Câu 13 (Segmentation DP — Phân hoạch đoạn):

Trong bài toán Phân đoạn dãy số tối ưu $A[1 \dots N]$, hệ thức chuyển trạng thái tổng quát để tính $dp[i]$ (chi phí tối ưu cho tiền tố $1 \dots i$) là gì?

- **A.** $dp[i] = dp[i-1] + \text{cost}(i, i)$

- **B.** **[Đáp án đúng]** $dp[i] = \min(\{dp[j] + \text{cost}(j + 1, i) \mid 0 \le j < i\})$

- **C.** $dp[i] = dp[i/2]$

- **D.** $dp[i] = \min(dp[i-1], dp[i-2])$

> *Giải thích:* Thử mọi điểm cắt $j$ để tách tiền tố $1 \dots i$ thành phần đã tối ưu $1 \dots j$ và đoạn con mới nhất $j+1 \dots i$.

#### Câu 14 (Coin Change — Phân biệt Thứ tự duyệt):

Để đếm số cách đổi tiền không phân biệt thứ tự (tổ hợp: $1+2$ và $2+1$ là một cách), thứ tự duyệt 2 vòng lặp phải như thế nào?

- **A.** Vòng ngoài duyệt Tiền $1 \to S$, vòng trong duyệt từng Đồng xu.

- **B.** **[Đáp án đúng]** Vòng ngoài duyệt từng Đồng xu, vòng trong duyệt Tiền từ mệnh giá xu đến $S$.

- **C.** Duyệt ngẫu nhiên.

- **D.** Duyệt tiền giảm dần.

> *Giải thích:* Duyệt từng đồng xu ở vòng ngoài đảm bảo các đồng xu mệnh giá nhỏ được đưa vào trước, đồng xu lớn đưa vào sau $\implies$ Không bao giờ sinh ra hoán vị lặp lại.

#### Câu 15 (Ý nghĩa mảng tails trong LIS O(N log N)):

Trong thuật toán LIS $\mathcal{O}(N \log N)$ (chỉ số 0-based), phần tử $tails[len - 1]$ lưu trữ giá trị gì?

- **A.** Độ dài lớn nhất của dãy con tăng.

- **B.** **[Đáp án đúng]** Giá trị phần tử kết thúc nhỏ nhất của một dãy con tăng có độ dài đúng bằng $len$.

- **C.** Tổng giá trị của dãy con tăng độ dài $len$.

- **D.** Vị trí ban đầu của phần tử trong mảng gốc.

> *Giải thích:* Lưu phần tử kết thúc nhỏ nhất tạo điều kiện thuận lợi nhất để các phần tử đứng sau ghép nối vào tạo thành dãy con dài hơn.

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
