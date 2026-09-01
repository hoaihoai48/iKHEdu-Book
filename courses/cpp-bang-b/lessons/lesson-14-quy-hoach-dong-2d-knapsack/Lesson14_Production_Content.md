# Chuyên đề 14: Quy hoạch động 2D & bài toán cái túi (Knapsack)

## 1. Bản chất không gian trạng thái 2D

Trong Chuyên đề 13, trạng thái $dp[i]$ chỉ phụ thuộc vào một tham số đơn lẻ (vị trí trên dãy số hoặc giá trị tổng tiền). Tuy nhiên, trong thực tế thi đấu, bài toán thường yêu cầu thỏa mãn đồng thời **hai điều kiện độc lập**:
1. **Quy hoạch động trên Lưới tọa độ (Grid DP):** Trạng thái được định vị bởi cặp tọa độ $(i, j)$ trên ma trận $N \times M$.
2. **Quy hoạch động Bài toán Cái túi (Knapsack DP):** Trạng thái cần theo dõi đồng thời **Chỉ số món đồ đang xét $i$** và **Sức chứa còn lại của cái túi $w$**.

> **Bản chất Không gian Trạng thái 2D:** Mỗi ô $dp[i][j]$ là một đỉnh trong Đồ thị trạng thái DAG 2 chiều. Thứ tự tính toán phải quét qua toàn bộ các hàng và cột theo chiều tăng dần (hoặc giảm dần có kiểm soát) để đảm bảo tính đúng đắn của mọi quan hệ phụ thuộc.

![Ma trận Quy hoạch động trên Lưới 2D](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-14-quy-hoach-dong-2d-knapsack/assets/grid_dp_matrix_vi.svg)

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

![Kỹ thuật Nén mảng 1D trong 0/1 Knapsack](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-14-quy-hoach-dong-2d-knapsack/assets/knapsack_01_compression_vi.svg)

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

![So sánh 0/1 Knapsack vs Unbounded Knapsack](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-14-quy-hoach-dong-2d-knapsack/assets/unbounded_vs_01_knapsack_vi.svg)

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

## 8. Hệ thống câu hỏi kiểm tra khái niệm (Concept Quiz)

#### Câu 1 (Bản chất Không gian Trạng thái 2D):

Trong bài toán Cái túi $0/1$ Knapsack, tại sao cần đến hai tham số trạng thái $dp[i][w]$?

- **A.** Vì mỗi món đồ có hai thuộc tính là tên gọi và mã số.

- **B.** **[Đáp án đúng]** Vì cần theo dõi đồng thời tập món đồ đã xét ($1 \to i$) và lượng sức chứa đã tiêu tốn ($w$).

- **C.** Để tăng độ phức tạp thời gian thuật toán.

- **D.** Vì ma trận 2D luôn chạy nhanh hơn mảng 1D.

> *Giải thích:* Một chiều đại diện cho tiến trình duyệt các lựa chọn ($i$), chiều còn lại đại diện cho giới hạn tài nguyên bị ràng buộc ($w$).

#### Câu 2 (Chiều duyệt vòng lặp Nén mảng 0/1 Knapsack):

Khi nén bảng $DP[i][w]$ thành mảng 1D $DP[w]$ trong bài toán $0/1$ Knapsack, chiều duyệt của biến $w$ bắt buộc phải như thế nào?

- **A.** Duyệt xuôi từ $wt_i \to W$.

- **B.** **[Đáp án đúng]** Duyệt ngược từ $W \to wt_i$.

- **C.** Duyệt ngẫu nhiên không theo thứ tự.

- **D.** Duyệt nhảy cóc 2 bước.

> *Giải thích:* Duyệt ngược đảm bảo khi tính $dp[w]$, giá trị $dp[w - wt_i]$ chưa bị món đồ thứ $i$ cập nhật đè lên, giữ trọn vẹn bất biến mỗi đồ dùng tối đa 1 lần.

#### Câu 3 (Unbounded Knapsack vs 0/1 Knapsack):

Điểm khác biệt duy nhất trong mã nguồn C++ giữa $0/1$ Knapsack mảng 1D và Unbounded Knapsack mảng 1D là gì?

- **A.** Thay hàm `max` bằng hàm `min`.

- **B.** **[Đáp án đúng]** $0/1$ Knapsack duyệt ngược $w$ giảm dần, còn Unbounded Knapsack duyệt xuôi $w$ tăng dần.

- **C.** Khởi tạo mảng bằng $-1$.

- **D.** Dùng thêm một mảng phụ thứ hai.

> *Giải thích:* Duyệt xuôi cho phép trạng thái $dp[w]$ tận dụng ngay kết quả vừa cập nhật của chính món đồ $i$ tại $dp[w - wt_i]$, tương đương việc lấy thêm món đồ $i$ lần thứ 2, 3...

#### Câu 4 (Xử lý vật cản trên Lưới 2D):

Khi đếm số đường đi trên lưới $N \times M$, nếu ô $(i, j)$ có chứa vật cản, giá trị $dp[i][j]$ phải được xử lý như thế nào?

- **A.** $dp[i][j] = -1$

- **B.** **[Đáp án đúng]** $dp[i][j] = 0$ (Gán bằng 0 và không nhận luồng đi qua).

- **C.** $dp[i][j] = dp[i-1][j] + dp[i][j-1]$

- **D.** Bỏ qua không khởi tạo.

> *Giải thích:* Ô có vật cản không thể bước vào $\implies$ Số cách đi đến ô này bằng 0. Khi các ô phía sau cộng dồn sẽ không nhận thêm cách nào từ ô cản này.

#### Câu 5 (Kỹ thuật Đổi Trục DP theo Value):

Khi $N = 100$ và $W = 10^9$ nhưng $\sum val_i \le 10^5$, tại sao ta đổi trạng thái thành $dp[v]$ = Khối lượng nhỏ nhất để đạt giá trị $v$?

- **A.** Vì thuật toán cũ bị sai đáp án.

- **B.** **[Đáp án đúng]** Vì không thể tạo mảng kích thước $10^9$ ($\mathcal{O}(W)$ gây MLE/TLE), trong khi mảng kích thước $10^5$ chạy cực nhanh và tốn rất ít bộ nhớ.

- **C.** Để làm cho code ngắn hơn.

- **D.** Vì khối lượng luôn nhỏ hơn giá trị.

> *Giải thích:* Đây là bài học kinh điển về Thiết kế Trạng thái: Chọn trục DP dựa trên đại lượng có miền giá trị khả thi trong giới hạn tài nguyên.

#### Câu 6 (Bài toán Subset Sum):

Cho mảng $N$ số nguyên dương và số $S$. Bài toán kiểm tra tồn tại tập con có tổng bằng $S$ thực chất là trường hợp đặc biệt của bài toán nào?

- **A.** Dãy con tăng dài nhất (LIS).

- **B.** **[Đáp án đúng]** Bài toán Cái túi $0/1$ Knapsack với $wt_i = val_i = A[i]$ và kiểu dữ liệu boolean.

- **C.** Bài toán Hai con trỏ.

- **D.** Thuật toán Euclid.

> *Giải thích:* $dp[w] = true$ nếu có thể tạo ra tổng khối lượng đúng bằng $w$. Chuyển trạng thái: $dp[w] = dp[w] \lor dp[w - A[i]]$.

#### Câu 7 (Khôi phục danh sách đồ trong Cái túi 0/1):

Để in ra danh sách các món đồ được chọn trong bài toán Cái túi $0/1$, ta cần lưu trữ bảng phương án ở dạng nào?

- **A.** Mảng 1D $dp[w]$.

- **B.** **[Đáp án đúng]** Bảng phương án 2D đầy đủ $dp[i][w]$, sau đó lần ngược từ $(N, W)$.

- **C.** Không thể khôi phục được.

- **D.** Chỉ cần lưu mảng ban đầu.

> *Giải thích:* Truy vết 2D so sánh nếu $dp[i][w] \ne dp[i-1][w] \implies$ Món $i$ đã được chọn, ghi nhận món $i$ và lùi về $w \gets w - wt_i$, $i \gets i - 1$.

#### Câu 8 (Độ phức tạp Lưới Tam Giác Triangle DP):

Cho tam giác số gồm $N$ hàng, hàng thứ $i$ có $i$ số. Độ phức tạp thời gian để tìm đường đi từ đỉnh xuống đáy có tổng lớn nhất là bao nhiêu?

- **A.** $\mathcal{O}(2^N)$

- **B.** **[Đáp án đúng]** $\mathcal{O}(N^2)$

- **C.** $\mathcal{O}(N)$

- **D.** $\mathcal{O}(N \log N)$

> *Giải thích:* Tổng số ô trong tam giác là $1 + 2 + \cdots + N = N(N+1)/2 \approx N^2 / 2$. Mỗi ô tính trong $\mathcal{O}(1) \implies \mathcal{O}(N^2)$.

#### Câu 9 (Bẫy bộ nhớ 2D MLE):

Khai báo mảng `long long dp[5000][5000]` trong C++ sẽ tiêu tốn xấp xỉ bao nhiêu bộ nhớ RAM?

- **A.** $25\text{ MB}$

- **B.** **[Đáp án đúng]** $\approx 200\text{ MB}$ ($5000 \times 5000 \times 8 \text{ bytes} = 200,000,000\text{ bytes}$).

- **C.** $2\text{ GB}$

- **D.** $10\text{ MB}$

> *Giải thích:* Cần tính toán kích thước bộ nhớ trước khi khai báo: $200\text{MB}$ nằm sát giới hạn $256\text{MB}$ của nhiều kỳ thi, rất dễ bị MLE nếu có thêm các mảng phụ khác.

#### Câu 10 (Bài toán Phân chia Tập con Bằng nhau):

Để kiểm tra xem mảng $A$ có thể chia thành 2 tập con có tổng bằng nhau hay không, điều kiện cần đầu tiên là gì?

- **A.** Số phần tử $N$ phải là số chẵn.

- **B.** **[Đáp án đúng]** Tổng toàn bộ mảng $S = \sum A_i$ phải là số chẵn, sau đó quy về bài toán tìm tập con tổng $S / 2$.

- **C.** Mảng phải được sắp xếp tăng dần.

- **D.** Mọi phần tử phải dương.

> *Giải thích:* Nếu $S$ lẻ thì không thể chia đôi thành 2 số nguyên bằng nhau. Nếu $S$ chẵn, bài toán trở thành Subset Sum với mục tiêu $target = S / 2$.

#### Câu 11 (Quy hoạch động từ Dưới lên trên Triangle DP):

Tại sao khi giải bài toán Tam giác số, duyệt từ hàng đáy $N-1$ ngược lên đỉnh $0$ lại tiện lợi hơn duyệt từ đỉnh xuống?

- **A.** Vì chạy nhanh hơn gấp đôi.

- **B.** **[Đáp án đúng]** Vì đáp án cuối cùng gom lại đúng 1 ô duy nhất tại đỉnh $dp[0][0]$, không cần tìm max trên toàn bộ hàng đáy.

- **C.** Vì không cần dùng mảng.

- **D.** Vì tránh được tràn số.

> *Giải thích:* Chuyển trạng thái từ dưới lên: $dp[i][j] = A[i][j] + \max(dp[i+1][j], dp[i+1][j+1]) \implies$ Kết quả hội tụ về $dp[0][0]$.

#### Câu 12 (Knapsack 2 chiều ràng buộc):

Nếu cái túi vừa có giới hạn khối lượng $W$, vừa có giới hạn thể tích $V$, mảng phương án nén 1D cần mở rộng thành mảng mấy chiều?

- **A.** Vẫn là mảng 1D.

- **B.** **[Đáp án đúng]** Mảng 2D $dp[w][v]$ với 2 vòng lặp duyệt ngược $w$ từ $W \to wt_i$ và $v$ từ $V \to vol_i$.

- **C.** Mảng 4D.

- **D.** Không thể giải bằng DP.

> *Giải thích:* Nén chiều món đồ $i$, giữ lại 2 chiều tài nguyên ràng buộc $(w, v)$, cả 2 vòng lặp đều duyệt ngược để đảm bảo mỗi đồ dùng tối đa 1 lần.

#### Câu 13 (Tối ưu hóa bộ nhớ Lưới 2D bằng 2 dòng):

Khi tính $dp[i][j] = A[i][j] + \max(dp[i-1][j], dp[i][j-1])$ trên lưới $N \times M$, nếu $N, M \le 10^4$ nhưng bộ nhớ giới hạn $16\text{MB}$, ta có thể tối ưu không gian như thế nào?

- **A.** Dùng thuật toán đệ quy.

- **B.** **[Đáp án đúng]** Chỉ lưu 2 dòng phương án `prev_row` và `curr_row` kích thước $\mathcal{O}(M)$, giảm bộ nhớ từ $\mathcal{O}(N \times M)$ về $\mathcal{O}(M)$.

- **C.** Bỏ qua không dùng DP.

- **D.** Ép kiểu dữ liệu về `char`.

> *Giải thích:* Ô $(i, j)$ chỉ phụ thuộc ô cùng cột của hàng trên $(i-1, j)$ và ô bên trái $(i, j-1)$, do đó chỉ cần duy trì 2 dòng liên tiếp.

#### Câu 14 (Knapsack Phân chia chênh lệch nhỏ nhất):

Cho mảng $N$ phần tử tổng $S$. Để chia thành 2 nhóm có tổng $s_1, s_2$ sao cho $|s_1 - s_2|$ nhỏ nhất, ta tìm giá trị $s_1$ như thế nào?

- **A.** $s_1 = S / 2$.

- **B.** **[Đáp án đúng]** Chạy Subset Sum tìm tổng $s_1 \le S / 2$ lớn nhất có thể đạt được, sau đó độ chênh lệch là $S - 2 \cdot s_1$.

- **C.** Sắp xếp mảng rồi chia đôi.

- **D.** Lấy phần tử lớn nhất trừ phần tử nhỏ nhất.

> *Giải thích:* $s_1 + s_2 = S \implies |s_1 - s_2| = |S - 2s_1|$. Cực tiểu hóa đại lượng này tương đương tìm $s_1 \le \lfloor S/2 \rfloor$ lớn nhất có $dp[s_1] = true$.

#### Câu 15 (Truy vết đường đi trên Lưới 2D):

Khi lần ngược từ ô $(N, M)$ về ô $(1, 1)$ để in ra các bước đi $D$ (Down) và $R$ (Right), thứ tự các bước đi được ghi nhận như thế nào?

- **A.** In trực tiếp không cần đảo ngược.

- **B.** **[Đáp án đúng]** Lưu các ký tự vào chuỗi rồi đảo ngược lại chuỗi trước khi in ra.

- **C.** Chạy lại thuật toán từ đầu.

- **D.** Dùng đệ quy in xuôi.

> *Giải thích:* Vì lần ngược từ đích về xuất phát nên chuỗi thu được bị ngược chiều, cần `reverse` để có lộ trình chuẩn từ $(1, 1) \to (N, M)$.

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
