# TÀI LIỆU GỐC — CHƯƠNG 13: QUY HOẠCH ĐỘNG CƠ BẢN (DYNAMIC PROGRAMMING)

## Bản đồ chương

| Trường | Nội dung |
|---|---|
| Mục tiêu | Nắm vững bản chất tư duy Quy hoạch động (Dynamic Programming - DP): từ Đệ quy có nhớ (Memoization) đến Bảng phương án (Tabulation); làm chủ 3 bài toán kinh điển: LIS, Cái túi 0/1 (Knapsack) và Grid DP |
| Kiến thức cần có | Đệ quy, mảng 1D/2D, tư duy bài toán con gối nhau và cấu trúc con tối ưu |
| Phạm vi | Bản chất DP, Dãy con tăng dài nhất (LIS $\mathcal{O}(N^2)$), Bài toán Cái túi 0/1 (Knapsack), Quy hoạch động trên lưới (Grid DP), Kỹ thuật tối ưu bộ nhớ 1D |
| Số bài | 4 bài học lý thuyết & ví dụ mẫu + 1 bài luyện tập phân tầng |
| Tổng bài tập | 12 bài tập tự chứa (Tầng A: 4 bài, Tầng B: 4 bài, Tầng C: 4 bài) |

### Learning outcomes

Sau chương này, em có thể:
1. Nhận diện 2 dấu hiệu của bài toán DP: Bài toán con gối nhau (Overlapping Subproblems) và Cấu trúc con tối ưu (Optimal Substructure).
2. Trình bày đầy đủ 3 bước thiết kế DP: Trạng thái (State), Công thức chuyển (Transition) và Điều kiện cơ sở (Base Case).
3. Cài đặt thành thạo thuật toán LIS $\mathcal{O}(N^2)$ và bài toán Cái túi 0/1 (Knapsack) kèm tối ưu mảng 1D.
4. Giải các bài toán tìm đường đi tối ưu và đếm số cách đi trên lưới ô vuông (Grid DP).

### Câu hỏi trung tâm của chương

> **Làm thế nào để không bao giờ phải tính lại một kết quả mà mình đã từng tính trước đó**

---

### Bài 13.1 — Bản chất của DP: Từ Đệ quy có nhớ đến Bảng phương án

#### 1. Khái niệm & 3 bước bắt buộc
- **State (Trạng thái):** `dp[i]` đại diện cho cái gì
- **Transition (Công thức chuyển):** Tính `dp[i]` từ các trạng thái nhỏ hơn.
- **Base Case (Điều kiện cơ sở):** `dp[0], dp[1]`.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 13.1: Leo Cầu Thang Tòa Tháp Landmark 81** 
> **Bối cảnh:** Vận động viên tham gia cuộc thi chạy bộ leo cầu thang tòa tháp Landmark 81 gồm $N$ bậc thang. Mỗi bước, vận động viên có thể bước lên $1$ bậc hoặc nhảy lên $2$ bậc. 
> **Nhiệm vụ:** Tính số cách khác nhau để vận động viên leo lên đến đúng bậc thứ $N$ Modulo $10^9+7$. 
> **Input:** `4` $\implies$ **Output:** `5` (các cách: 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2).

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

const int MOD = 1000000007;

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

int n;
if (!(cin >> n)) return 0;

vector<int> dp(n + 1);
dp[0] = 1;
dp[1] = 1;

for (int i = 2; i <= n; i++) {
dp[i] = (dp[i - 1] + dp[i - 2]) % MOD;
}

cout << dp[n] << "\n";
return 0;
}
```

---

#### 3. Bài tập thực hành Bài 13.1

##### Bài 13.1.1 — Bước Cầu Thang Nhảy Tối Đa 3 Bậc
- **Bối cảnh:** Mỗi bước có thể nhảy 1, 2 hoặc 3 bậc thang. Đếm số cách leo lên bậc $N$ modulo $10^9+7$.
- **Input:** `4` $\implies$ **Output:** `7`

##### Bài 13.1.2 — Lát Gạch Đường Đi $2 \times N$ Bằng Gạch $1 \times 2$
- **Bối cảnh:** Có một lối đi kích thước $2 \times N$. Đếm số cách lát kín bằng các viên gạch $1 \times 2$ và $2 \times 1$.
- **Input:** `3` $\implies$ **Output:** `3`

---

### Bài 13.2 — Dãy con tăng dài nhất (LIS $\mathcal{O}(N^2)$)

#### 1. Khái niệm & Thuật toán
- `dp[i]` là độ dài LIS kết thúc tại $A[i]$. $dp[i] = 1 + \max(dp[j] \mid j < i, A[j] < A[i])$.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 13.2: Tăng Trưởng Khách Du Lịch Quốc Tế Đến Đà Nẵng** 
> **Bối cảnh:** Thống kê lượng khách du lịch quốc tế $N$ tháng liên tiếp $A_1, A_2, \dots, A_N$. Tìm độ dài chuỗi tháng tăng trưởng liên tục dài nhất (không nhất thiết kề nhau). 
> **Input:** `6` \ `1 4 2 5 3 6` $\implies$ **Output:** `4` (dãy tăng: $[1, 2, 3, 6]$).

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

int n;
if (!(cin >> n)) return 0;

vector<int> a(n);
for (int i = 0; i < n; i++) cin >> a[i];

vector<int> dp(n, 1);
int ans = 0;

for (int i = 0; i < n; i++) {
for (int j = 0; j < i; j++) {
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

---

#### 3. Bài tập thực hành Bài 13.2

##### Bài 13.2.1 — Dãy Con Giảm Dài Nhất (LDS)
- **Bối cảnh:** Tìm độ dài của dãy con giảm thực sự dài nhất trong mảng $N$ phần tử ($N \le 2000$).
- **Input:** `5` \ `5 4 3 2 1` $\implies$ **Output:** `5`

##### Bài 13.2.2 — Dãy Con Tăng Có Tổng Lớn Nhất (MSIS)
- **Bối cảnh:** Tìm tổng lớn nhất của một dãy con tăng trong mảng $N$ số nguyên dương.
- **Input:** `4` \ `1 101 2 3` $\implies$ **Output:** `102` (dãy $[1, 101]$).

---

### Bài 13.3 — Bài toán Cái túi 0/1 (0/1 Knapsack)

#### 1. Khái niệm & Kỹ thuật tối ưu mảng 1D
- Duyệt ngược từ $S$ về $W_i$: `dp[w] = max(dp[w], dp[w - weight[i]] + val[i])`.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 13.3: Lựa Chọn Thiết Bị Lắp Đặt Trạm Phát 5G Viettel** 
> **Bối cảnh:** Xe kỹ thuật có tải trọng tối đa $S$ kg. Có $N$ thiết bị viễn thông, thiết bị thứ $i$ có trọng lượng $W_i$ và giá trị phủ sóng $V_i$. 
> **Nhiệm vụ:** Tìm giá trị phủ sóng lớn nhất có thể mang lên trạm phát. 
> **Input:** `3 4` \ `1 1500` \ `3 2000` \ `4 3000` $\implies$ **Output:** `3500`.

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

int n, s;
if (!(cin >> n >> s)) return 0;

vector<int> weight(n), val(n);
for (int i = 0; i < n; i++) cin >> weight[i] >> val[i];

vector<long long> dp(s + 1, 0);
for (int i = 0; i < n; i++) {
for (int w = s; w >= weight[i]; w--) {
dp[w] = max(dp[w], dp[w - weight[i]] + val[i]);
}
}

cout << dp[s] << "\n";
return 0;
}
```

---

#### 3. Bài tập thực hành Bài 13.3

##### Bài 13.3.1 — Chia Đôi Tài Sản Cân Bằng Nhất
- **Bối cảnh:** Cho $N$ món đồ với giá trị $A_1.A_N$. Chia thành 2 phần sao cho chênh lệch tổng giá trị giữa 2 phần là nhỏ nhất có thể.
- **Input:** `4` \ `1 2 3 4` $\implies$ **Output:** `0` (chia {1, 4} và {2, 3}).

##### Bài 13.3.2 — Cái Túi Chọn Đúng K Món Đồ
- **Bối cảnh:** Chọn đúng $K$ món đồ sao cho tổng trọng lượng $\le S$ và tổng giá trị lớn nhất.
- **Input:** `3 2 10` \ `4 10` \ `5 20` \ `6 30` $\implies$ **Output:** `50`

---

### Bài 13.4 — Quy hoạch động trên lưới (Grid DP)

#### 1. Khái niệm & Thuật toán
- `dp[i][j] = A[i][j] + max(dp[i-1][j], dp[i][j-1])`.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 13.4: Thu Thập Mẫu Vật Khoáng Sản Trên Lưới** 
> **Bối cảnh:** Xe tự hành trên bản đồ $N \times M$ ô, xuất phát từ $(1, 1)$ đến $(N, M)$, mỗi bước chỉ đi sang phải hoặc xuống dưới. Ô $(i, j)$ có $A[i][j]$ gam khoáng sản. Tìm lượng khoáng sản lớn nhất thu được. 
> **Input:** `3 3` \ `1 3 1` \ `1 5 1` \ `4 2 1` $\implies$ **Output:** `12`.

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

int n, m;
if (!(cin >> n >> m)) return 0;

vector<vector<long long>> a(n + 1, vector<long long>(m + 1));
vector<vector<long long>> dp(n + 1, vector<long long>(m + 1, 0));

for (int i = 1; i <= n; i++) {
for (int j = 1; j <= m; j++) cin >> a[i][j];
}

for (int i = 1; i <= n; i++) {
for (int j = 1; j <= m; j++) {
dp[i][j] = a[i][j] + max(dp[i - 1][j], dp[i][j - 1]);
}
}

cout << dp[n][m] << "\n";
return 0;
}
```

---

#### 3. Bài tập thực hành Bài 13.4

##### Bài 13.4.1 — Đường Đi Chi Phí Nhỏ Nhất Trên Mê Cung
- **Bối cảnh:** Tìm đường đi từ $(1, 1)$ đến $(N, M)$ có tổng chi phí nhỏ nhất trên ma trận chi phí dương.
- **Input:** `2 2` \ `1 2` \ `3 4` $\implies$ **Output:** `7` ($1 \to 2 \to 4$).

##### Bài 13.4.2 — Đếm Số Đường Đi Tránh Ô Vật Cản Trên Lưới
- **Bối cảnh:** Đếm số đường đi từ $(1, 1)$ đến $(N, M)$ trên lưới có các ô cấm `#` modulo $10^9+7$.
- **Input:** `3 3` \ `..` \ `.#.` \ `..` $\implies$ **Output:** `2`

---

### Bài 13.5 — Luyện tập tổng hợp và đánh giá chương

### Đề bài 12 bài tập phân tầng tự chứa (iKHEDU Standard)

#### Tầng A — Củng cố nền tảng (Rating 1000 - 1200)

##### Bài 13.5.1 — Bước Cầu Thang Nhảy 1, 2, 3 Bậc
- **Bối cảnh:** Đếm số cách bước lên bậc $N$ khi mỗi bước có thể nhảy 1, 2 hoặc 3 bậc.

##### Bài 13.5.2 — Đổi Tiền Xu Số Lượng Ít Nhất
- **Bối cảnh:** Cho các mệnh giá tiền xu. Tìm số lượng đồng xu ít nhất để tạo thành số tiền $S$.

##### Bài 13.5.3 — LIS Cơ Bản Trên Dãy Số
- **Bối cảnh:** Tìm độ dài dãy con tăng dài nhất với $N \le 2000$.

##### Bài 13.5.4 — Đường Đi Trên Lưới Tránh Ô Vật Cản
- **Bối cảnh:** Đếm số cách đi từ $(1, 1)$ đến $(N, M)$ trên lưới có các ô cấm `#`.

---

#### Tầng B — Vận dụng thi đấu (Rating 1200 - 1500)

##### Bài 13.5.5 — Chia Tập Hợp Cân Bằng Trọng Lượng (Subset Sum)
- **Bối cảnh:** Kiểm tra xem có thể chọn một tập con có tổng trọng lượng đúng bằng $S$ hay không.

##### Bài 13.5.6 — Phân Chia Lô Hàng Chênh Lệch Nhỏ Nhất
- **Bối cảnh:** Chia $N$ gói hàng cho 2 xe sao cho độ chênh lệch tải trọng giữa 2 xe là nhỏ nhất.

##### Bài 13.5.7 — So Sánh Hai Chuỗi Gen (Longest Common Subsequence)
- **Bối cảnh:** Tìm độ dài xâu con chung dài nhất của 2 xâu ADN $S$ và $T$ trong $\mathcal{O}(|S| \times |T|)$.

##### Bài 13.5.8 — Đổi Tiền Không Giới Hạn Số Lượng (Unbounded Knapsack)
- **Bối cảnh:** Bài toán Cái túi khi mỗi món đồ được sử dụng không giới hạn số lần (duyệt xuôi mảng 1D).

---

#### Tầng C — Chuyển giao & Nâng cao (Rating 1500 - 1800)

##### Bài 13.5.9 — Truy Vết Danh Sách Cổ Phiếu Tăng Trưởng LIS
- **Bối cảnh:** In toàn bộ dãy các giá trị thuộc dãy con tăng dài nhất.

##### Bài 13.5.10 — LIS Siêu Tốc $\mathcal{O}(N \log N)$ Bằng Binary Search
- **Bối cảnh:** Tìm LIS với $N = 2 \times 10^5$ bằng mảng đuôi `tail` và `lower_bound`.

##### Bài 13.5.11 — Khoảng Cách Biến Đổi Văn Bản (Edit Distance)
- **Bối cảnh:** Số thao tác thêm, xóa, sửa ký tự ít nhất để biến xâu $S$ thành xâu $T$.

##### Bài 13.5.12 — Tập Độc Lập Trọng Số Lớn Nhất Trên Cây (Tree DP)
- **Bối cảnh:** Quy hoạch động trên cây chọn tập đỉnh không kề nhau có tổng trọng số lớn nhất.

---

### Bẫy lỗi thường gặp & Rubric đánh giá
| Lỗi thường gặp | Cách kiểm soát |
|---|---|
| Duyệt xuôi trong bài toán Cái túi 0/1 làm đồ vật bị dùng nhiều lần | Bài toán 0/1 bắt buộc duyệt ngược từ $S$ về $W_i$ |
| Khởi tạo `dp` bằng 0 trong bài toán tìm MIN | Khởi tạo mảng `dp` bằng vô cùng lớn ($10^{18}$) |

### Rubric hoàn thành chương
| Mức độ | Tiêu chí đánh giá |
|---|---|
| **Cơ bản (Tầng A)** | Nắm vững State, Transition và Base case cho các bài toán quy hoạch động 1D/2D cơ bản. |
| **Vận dụng (Tầng B)** | Cài đặt thành thạo Cái túi 0/1 tối ưu mảng 1D và bài toán LCS. |
| **Thành thạo (Tầng C)** | Cài đặt LIS $\mathcal{O}(N \log N)$ và truy vết phương án tối ưu. |
