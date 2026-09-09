# TÀI LIỆU GỐC — CHƯƠNG 20: PHÉP TOÁN TRÊN BIT VÀ BITMASK (BIT MANIPULATION & BITMASK)

## Bản đồ chương

| Trường | Nội dung |
|---|---|
| Mục tiêu | Nắm vững 6 toán tử bit cấp độ phần cứng (`&`, `|`, `^`, `~`, `<<`, `>>`); ứng dụng Mặt nạ bit (Bitmask) để biểu diễn tập hợp con của $N$ phần tử; làm chủ quy hoạch động Bitmask (Bitmask DP) và thuật toán Người du lịch TSP |
| Kiến thức cần có | Biểu diễn nhị phân, kiểu `int` và `long long`, quy hoạch động cơ bản |
| Phạm vi | 6 toán tử bit, Bật/Tắt/Kiểm tra bit thứ $K$, Các hàm bit dựng sẵn (`__builtin_popcount`, `__builtin_ctz`), Biểu diễn tập con bằng Bitmask, Duyệt toàn bộ $2^N$ tập con, Bitmask DP cho bài toán TSP $\mathcal{O}(2^N \times N^2)$ |
| Số bài | 4 bài học lý thuyết & ví dụ mẫu + 1 bài luyện tập phân tầng |
| Tổng bài tập | 12 bài tập tự chứa (Tầng A: 4 bài, Tầng B: 4 bài, Tầng C: 4 bài) |

### Learning outcomes

Sau chương này, em có thể:
1. Thao tác thành thạo các toán tử bit: Bật bit `(x | (1 << k))`, Tắt bit `(x & ~(1 << k))`, Kiểm tra bit `((x >> k) & 1)`.
2. Sử dụng các hàm bit tối ưu phần cứng `__builtin_popcountll` đếm số bit 1 trong $\mathcal{O}(1)$.
3. Duyệt toàn bộ $2^N$ tập con của tập hợp $N$ phần tử bằng vòng lặp Bitmask từ $0$ đến $2^N - 1$.
4. Cài đặt Quy hoạch động Bitmask giải bài toán Người du lịch (TSP) trong $\mathcal{O}(2^N \times N^2)$.

### Câu hỏi trung tâm của chương

> **Làm thế nào để lưu trữ trạng thái của $20$ đối tượng chỉ trong một biến số nguyên duy nhất**

---

### Bài 20.1 — Các phép toán Bitwise cơ bản

#### 1. Khái niệm & 6 toán tử bit
- AND `&`, OR `|`, XOR `^`, NOT `~`, Dịch trái `<<`, Dịch phải `>>`.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 20.1: Bật Tắt Cảm Biến Giám Sát Nhà Thông Minh Smart Home** 
> **Bối cảnh:** Bộ điều khiển nhà thông minh quản lý trạng thái của 30 cảm biến bằng một số nguyên $X$ (mỗi bit $1$ đại diện cho cảm biến đang BẬT). Thực hiện $Q$ lệnh kiểm tra hoặc bật/tắt cảm biến thứ $K$. 
> **Input:** `0` \ `3` \ `1 2` (Bật cảm biến 2) \ `3 2` (Kiểm tra cảm biến 2) \ `2 2` (Tắt cảm biến 2) $\implies$ **Output:** `ON`.

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

int mask, q;
if (!(cin >> mask >> q)) return 0;

while (q--) {
int type, k;
cin >> type >> k;
if (type == 1) {
mask |= (1 << k);
} else if (type == 2) {
mask &= ~(1 << k);
} else {
if ((mask >> k) & 1) cout << "ON\n";
else cout << "OFF\n";
}
}

return 0;
}
```

---

#### 3. Bài tập thực hành Bài 20.1

##### Bài 20.1.1 — Đếm Số Bit 1 Bằng Hàm Tối Ưu Phần Cứng
- **Bối cảnh:** Đếm số lượng bit 1 trong biểu diễn nhị phân của số nguyên 64-bit $X$ ($0 \le X \le 10^{18}$).
- **Input:** `7` $\implies$ **Output:** `3` (vì 7 = 111 nhị phân).

##### Bài 20.1.2 — Tìm Vị Trí Bit 1 Đầu Tiên (ctz)
- **Bối cảnh:** Đếm số chữ số 0 tận cùng trong biểu diễn nhị phân bằng `__builtin_ctzll(x)`.
- **Input:** `8` $\implies$ **Output:** `3` (8 = 1000_2, có 3 số 0 ở đuôi)

---

### Bài 20.2 — 4 Thao tác chuẩn trên Bitmask

#### 1. Khái niệm & Kỹ thuật
1. Bật bit: `mask | (1 << k)`.
2. Tắt bit: `mask & ~(1 << k)`.
3. Đảo bit: `mask ^ (1 << k)`.
4. Kiểm tra bit: `(mask >> k) & 1`.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 20.2: Đảo Trạng Thái Đèn Giao Thông** 
> **Bối cảnh:** Đảo trạng thái (ON $\to$ OFF, OFF $\to$ ON) của bit thứ $K$ trên thanh ghi điều khiển.

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

int mask, k;
if (!(cin >> mask >> k)) return 0;

mask ^= (1 << k);
cout << mask << "\n";
return 0;
}
```

---

#### 3. Bài tập thực hành Bài 20.2

##### Bài 20.2.1 — Kiểm Tra Số Lũy Thừa Của 2
- **Bối cảnh:** Kiểm tra $X$ có phải là lũy thừa của 2 không bằng biểu thức bit `(x > 0) && ((x & (x - 1)) == 0)`.
- **Input:** `16` $\implies$ **Output:** `YES`

##### Bài 20.2.2 — Lấy Bit Thấp Nhất (Lowbit)
- **Bối cảnh:** In giá trị `x & (-x)` của số nguyên $X$.
- **Input:** `12` $\implies$ **Output:** `4`

---

### Bài 20.3 — Duyệt toàn bộ $2^N$ tập hợp con (Bitmask Brute-force)

#### 1. Khái niệm & Thuật toán
- Duyệt `mask` từ `0` đến `(1 << n) - 1`.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 20.3: Phân Bổ Ngân Sách Dự Án Khởi Nghiệp iKHEDU** 
> **Bối cảnh:** Có $N$ dự án khởi nghiệp ($N \le 20$), dự án thứ $i$ cần vốn $A_i$ triệu đồng. Tìm tổng số cách chọn một tập hợp các dự án sao cho tổng vốn đầu tư đúng bằng số tiền ngân sách $S$. 
> **Input:** `4 10` \ `2 3 5 7` $\implies$ **Output:** `2` (tập {3, 7} và {2, 3, 5}).

#### Cài đặt C++
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
for (int i = 0; i < n; i++) cin >> a[i];

int validSubsets = 0;
int totalMasks = 1 << n;

for (int mask = 0; mask < totalMasks; mask++) {
long long currentSum = 0;
for (int i = 0; i < n; i++) {
if ((mask >> i) & 1) {
currentSum += a[i];
}
}
if (currentSum == s) validSubsets++;
}

cout << validSubsets << "\n";
return 0;
}
```

---

#### 3. Bài tập thực hành Bài 20.3

##### Bài 20.3.1 — Tìm Tập Hợp Có Tổng Gần S Nhất
- **Bối cảnh:** Cho $N$ phần tử ($N \le 20$). Tìm tổng tập con lớn nhất không vượt quá $S$.
- **Input:** `3 10` \ `4 5 7` $\implies$ **Output:** `9` (chọn {4, 5}).

##### Bài 20.3.2 — Đếm Số Tập Con Có Tổng Là Số Chẵn
- **Bối cảnh:** Đếm số lượng tập con có tổng các phần tử là số chẵn trong $N \le 15$ phần tử.
- **Input:** `2` \ `1 3` $\implies$ **Output:** `2` (tập rỗng {} và tập {1, 3})

---

### Bài 20.4 — Quy hoạch động Bitmask cơ bản (Bitmask DP)

#### 1. Khái niệm & Bài toán TSP $\mathcal{O}(2^N \times N^2)$
- `dp[mask][u]`: Chi phí nhỏ nhất đã thăm tập đỉnh `mask` và hiện đang đứng tại đỉnh `u`.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 20.4: Lộ Trình Giao Hàng Tiết Kiệm Tối Ưu (TSP)** 
> **Bối cảnh:** Shipper cần đi qua $N$ địa điểm giao hàng ($N \le 16$). Ma trận $C[i][j]$ cho biết chi phí di chuyển giữa 2 điểm. Tìm tổng chi phí nhỏ nhất để đi qua tất cả $N$ địa điểm và quay về điểm xuất phát. 
> **Input:** 
> `3` 
> `0 10 20` 
> `10 0 15` 
> `20 15 0` 
> **Output:** `45` ($0 \to 1 \to 2 \to 0$: $10 + 15 + 20 = 45$).

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

const long long INF = 1e18;

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

int n;
if (!(cin >> n)) return 0;

vector<vector<long long>> cost(n, vector<long long>(n));
for (int i = 0; i < n; i++) {
for (int j = 0; j < n; j++) cin >> cost[i][j];
}

int totalMasks = 1 << n;
vector<vector<long long>> dp(totalMasks, vector<long long>(n, INF));
dp[1][0] = 0;

for (int mask = 1; mask < totalMasks; mask++) {
for (int u = 0; u < n; u++) {
if (!(mask & (1 << u)) || dp[mask][u] == INF) continue;

for (int v = 0; v < n; v++) {
if (!(mask & (1 << v))) {
int nextMask = mask | (1 << v);
dp[nextMask][v] = min(dp[nextMask][v], dp[mask][u] + cost[u][v]);
}
}
}
}

long long minTour = INF;
int finalMask = totalMasks - 1;
for (int u = 0; u < n; u++) {
minTour = min(minTour, dp[finalMask][u] + cost[u][0]);
}

cout << minTour << "\n";
return 0;
}
```

---

#### 3. Bài tập thực hành Bài 20.4

##### Bài 20.4.1 — Gán Việc Cho Kỹ Sư Chi Phí Nhỏ Nhất
- **Bối cảnh:** Gán $N$ kỹ sư vào $N$ công việc ($N \le 16$) bằng Bitmask DP $\mathcal{O}(2^N \times N)$.
- **Input:** `2` \ `1 2` \ `3 4` $\implies$ **Output:** `5` (1+4=5 hoặc 2+3=5).

##### Bài 20.4.2 — Tìm Đường Đi Hamilton Trên Đồ Thị Nhỏ
- **Bối cảnh:** Kiểm tra xem có tồn tại đường đi qua tất cả $N$ đỉnh của đồ thị ($N \le 16$) mỗi đỉnh đúng 1 lần không bằng Bitmask DP.
- **Input:** `3 2` \ `0 1` \ `1 2` $\implies$ **Output:** `YES`

---

### Bài 20.5 — Luyện tập tổng hợp và đánh giá chương

### Đề bài 12 bài tập phân tầng tự chứa (iKHEDU Standard)

#### Tầng A — Củng cố nền tảng (Rating 1000 - 1200)

##### Bài 20.5.1 — Bật Tắt Bit Cảm Biến Giám Sát
- **Bối cảnh:** Thao tác bật/tắt/kiểm tra bit thứ $K$ của số nguyên $X$.

##### Bài 20.5.2 — Đếm Số Bit 1 Trong Mã Khóa
- **Bối cảnh:** Sử dụng `__builtin_popcount` đếm số bit 1 trong biểu diễn nhị phân.

##### Bài 20.5.3 — Kiểm Tra Lũy Thừa Của 2
- **Bối cảnh:** Kiểm tra $X$ có phải lũy thừa của 2 không bằng điều kiện `(x & (x - 1)) == 0`.

##### Bài 20.5.4 — Duyệt Tất Cả Tập Con N Phần Tử
- **Bối cảnh:** In toàn bộ $2^N$ tập hợp con theo thứ tự mã nhị phân tăng dần.

---

#### Tầng B — Vận dụng thi đấu (Rating 1200 - 1500)

##### Bài 20.5.5 — Phân Bổ Kỹ Sư Vào Công Đoạn (Assignment Problem)
- **Bối cảnh:** Gán $N$ kỹ sư vào $N$ công việc với ma trận chi phí $C[i][j]$ sao cho tổng chi phí là nhỏ nhất bằng Bitmask DP $\mathcal{O}(2^N \times N)$.

##### Bài 20.5.6 — Phần Tử Xuất Hiện Đúng 1 Lần Trong Dãy Trùng Đôi
- **Bối cảnh:** Mảng gồm $2N + 1$ phần tử, mọi phần tử đều xuất hiện 2 lần trừ 1 phần tử. Tìm phần tử đó bằng phép XOR trong $\mathcal{O}(N)$ bộ nhớ $\mathcal{O}(1)$.

##### Bài 20.5.7 — Tập Hợp Có Tổng Trọng Số Bằng K
- **Bối cảnh:** Duyệt Bitmask kiểm tra sự tồn tại của tập con có tổng trọng lượng bằng $K$ với $N \le 20$.

##### Bài 20.5.8 — Ghép Cặp Thi Đấu Đôi (Matching DP)
- **Bối cảnh:** Cho $2N$ thí sinh ($N \le 10$). Ghép thành $N$ cặp đấu với mức độ tương thích $A[i][j]$ lớn nhất bằng Bitmask DP.

---

#### Tầng C — Chuyển giao & Nâng cao (Rating 1500 - 1800)

##### Bài 20.5.9 — Người Du Lịch TSP Đầy Đủ Chi Phí
- **Bối cảnh:** Cài đặt hoàn chỉnh thuật toán TSP trên đồ thị $N \le 16$ đỉnh.

##### Bài 20.5.10 — Duyệt Tập Con Của Tập Con (Submask Enumeration)
- **Bối cảnh:** Vòng lặp `for (int sub = mask; sub > 0; sub = (sub - 1) & mask)` duyệt toàn bộ các mặt nạ con trong tổng thời gian $\mathcal{O}(3^N)$.

##### Bài 20.5.11 — Gặp Gỡ Ở Giữa (Meet in the Middle Cho N = 40)
- **Bối cảnh:** Chia mảng thành 2 nửa kích thước 20, sinh $2^{20}$ tổng và kết hợp Binary Search tìm tập con có tổng gần $S$ nhất trong $\mathcal{O}(2^{N/2} \log(2^{N/2}))$.

##### Bài 20.5.12 — Tìm Cặp Có XOR Lớn Nhất Bằng Cây Trie Bit
- **Bối cảnh:** Cho $N$ số nguyên ($N \le 10^5$). Tìm cặp $(A_i, A_j)$ có $A_i \oplus A_j$ lớn nhất trong $\mathcal{O}(N \times 30)$ bằng cây Trie nhị phân.

---

### Bẫy lỗi thường gặp & Rubric đánh giá
| Lỗi thường gặp | Cách kiểm soát |
|---|---|
| Quên đóng mở ngoặc khi dùng toán tử bit (vì độ ưu tiên của toán tử bit thấp hơn toán tử so sánh) | **Luôn viết `((x >> k) & 1)` hoặc `(mask & (1 << k))` có đủ dấu ngoặc** |
| Dịch bit vượt quá 31 khi dùng `1 << k` với kiểu `int` | Viết `1LL << k` khi $k \ge 31$ |

### Rubric hoàn thành chương
| Mức độ | Tiêu chí đánh giá |
|---|---|
| **Cơ bản (Tầng A)** | Bật/tắt/kiểm tra bit và đếm số bit 1 chính xác. |
| **Vận dụng (Tầng B)** | Duyệt toàn bộ $2^N$ tập con và giải bài toán Assignment bằng Bitmask DP. |
| **Thành thạo (Tầng C)** | Cài đặt thành thạo TSP và kỹ thuật Meet in the Middle cho $N = 40$. |
