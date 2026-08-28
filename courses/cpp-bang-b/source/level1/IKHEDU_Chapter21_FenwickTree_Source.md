# TÀI LIỆU GỐC — CHƯƠNG 21: CÂY CHỈ SỐ NHỊ PHÂN (FENWICK TREE / BIT)

## Bản đồ chương

| Trường | Nội dung |
|---|---|
| Mục tiêu | Nắm vững cấu trúc Cây Fenwick (Binary Indexed Tree - BIT) với code cài đặt siêu ngắn gọn (chưa tới 10 dòng) dựa trên phép toán `lowbit(i) = i & (-i)`; cập nhật điểm và tính tổng tiền tố trong $\mathcal{O}(\log N)$; ứng dụng đếm số cặp nghịch thế và so sánh với Segment Tree |
| Kiến thức cần có | Phép toán bit, mảng 1-based, mảng tiền tố |
| Phạm vi | Phép toán `lowbit(i) = i & (-i)`, Cài đặt `update` và `getPrefixSum` $\mathcal{O}(\log N)$, Ứng dụng đếm số cặp nghịch thế trong $\mathcal{O}(N \log N)$, So sánh Fenwick Tree vs Segment Tree |
| Số bài | 4 bài học lý thuyết & ví dụ mẫu + 1 bài luyện tập phân tầng |
| Tổng bài tập | 12 bài tập tự chứa (Tầng A: 4 bài, Tầng B: 4 bài, Tầng C: 4 bài) |

### Learning outcomes

Sau chương này, em có thể:
1. Giải thích ý nghĩa của phép toán `lowbit(i) = i & (-i)` và cấu trúc lưu trữ của cây Fenwick.
2. Cài đặt 2 hàm cơ bản `update` và `getPrefixSum` trong chưa tới 10 dòng code C++.
3. Áp dụng cây Fenwick kết hợp nén tọa độ để đếm số cặp nghịch thế trong thời gian $\mathcal{O}(N \log N)$ và bộ nhớ $\mathcal{O}(N)$ cực kỳ tối ưu.
4. Phân biệt chính xác khi nào nên chọn Fenwick Tree (ngắn gọn, nhanh gấp 2–3 lần) và khi nào bắt buộc dùng Segment Tree (cần Lazy propagation, RMQ phức tạp).

### Câu hỏi trung tâm của chương

> **Làm thế nào để vừa sửa đổi một phần tử vừa tính tổng đoạn tiền tố với đoạn mã C++ ngắn nhất và tốc độ chạy nhanh nhất có thể?**

---

### Bài 21.1 — Phép toán Bit thấp nhất (Lowbit: `x & (-x)`)

#### 1. Khái niệm & Phép toán `lowbit`
- `lowbit(i) = i & (-i)` trả về giá trị của bit $1$ nhỏ nhất trong biểu diễn nhị phân của $i$.
- Nút $i$ trong cây `bit[i]` quản lý tổng của `lowbit(i)` phần tử kết thúc tại $i$.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 21.1: Quản Lý Tổng Tiền Tài Khoản Ngân Hàng Số MB Bank**  
> **Bối cảnh:** Ứng dụng ngân hàng MB Bank quản lý biến động số dư của $N$ tài khoản giao dịch. Thực hiện $Q$ truy vấn:  
> - `1 pos val`: Cộng thêm số tiền `val` vào tài khoản `pos`.  
> - `2 l r`: Tính tổng số dư của các tài khoản từ `l` đến `r`.  
> **Input:** `5 3` \ `1 2 3 4 5` \ `2 1 3` \ `1 2 5` \ `2 1 3` $\implies$ **Output:** `6` \ `11`.

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int n, q;
vector<long long> bitTree;

void update(int idx, long long val) {
    for (; idx <= n; idx += idx & (-idx)) {
        bitTree[idx] += val;
    }
}

long long getPrefixSum(int idx) {
    long long sum = 0;
    for (; idx > 0; idx -= idx & (-idx)) {
        sum += bitTree[idx];
    }
    return sum;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> q)) return 0;

    bitTree.assign(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        long long x;
        cin >> x;
        update(i, x);
    }

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int pos;
            long long val;
            cin >> pos >> val;
            update(pos, val);
        } else {
            int l, r;
            cin >> l >> r;
            cout << getPrefixSum(r) - getPrefixSum(l - 1) << "\n";
        }
    }

    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 21.1

##### Bài 21.1.1 — Tính Giá Trị Lowbit Của Số Nguyên X
- **Bối cảnh:** Nhập $Q$ số nguyên. Với mỗi số, in ra giá trị $X \ \& \ (-X)$.
- **Input:** `12` $\implies$ **Output:** `4` (vì $12 = 1100_2$, bit 1 thấp nhất là 4).

##### Bài 21.1.2 — Đếm Số Bước Nhảy Lowbit Để Về 0
- **Bối cảnh:** Lặp thao tác `x -= x & (-x)` cho đến khi $x = 0$. Đếm số bước lặp (chính bằng số bit 1).
- **Input:** `7` $\implies$ **Output:** `3`

---

### Bài 21.2 — Cấu trúc Fenwick Tree và 2 Thao tác cốt lõi

#### 1. Khái niệm & Thuật toán
- Cập nhật điểm: `idx += idx & (-idx)`.
- Tính tổng tiền tố: `idx -= idx & (-idx)`.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 21.2: Truy Vấn Tổng Đoạn Với Cây BIT**  
> **Bối cảnh:** Cho mảng $N$ phần tử. Thực hiện $Q$ truy vấn cập nhật điểm và tính tổng đoạn $[L, R]$.

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int n, q;
vector<long long> bitTree;

void add(int idx, long long val) {
    for (; idx <= n; idx += idx & (-idx)) bitTree[idx] += val;
}

long long sum(int idx) {
    long long ans = 0;
    for (; idx > 0; idx -= idx & (-idx)) ans += bitTree[idx];
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> q)) return 0;
    bitTree.assign(n + 1, 0);

    for (int i = 1; i <= n; i++) {
        long long x;
        cin >> x;
        add(i, x);
    }

    while (q--) {
        int l, r;
        cin >> l >> r;
        cout << sum(r) - sum(l - 1) << "\n";
    }

    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 21.2

##### Bài 21.2.1 — Cập Nhật Điểm Bằng Giá Trị Mới (Point Assignment)
- **Bối cảnh:** Thực hiện cập nhật $A[P] = V$ bằng cách tính độ chênh lệch `diff = V - A[P]` rồi gọi `add(P, diff)`.
- **Input:** `3 1` \ `1 2 3` \ `1 10` \ `1 3` $\implies$ **Output:** `15`

##### Bài 21.2.2 — Đếm Số Lượng Phần Tử Dương Trong Đoạn $[L, R]$
- **Bối cảnh:** Cập nhật mảng BIT lưu giá trị 1 tại vị trí $A[i] > 0$. Tính số số dương trong đoạn $[L, R]$.
- **Input:** `3 1` \ `1 -2 3` \ `1 3` $\implies$ **Output:** `2`

---

### Bài 21.3 — Ứng dụng kinh điển: Đếm số cặp nghịch thế (Inversions)

#### 1. Khái niệm & Thuật toán
- Nén tọa độ mảng về $1.N$.
- Duyệt từ $N$ về 1: `invCount += getPrefixSum(rank - 1)`, sau đó `update(rank, 1)`.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 21.3: Đếm Cặp Nghịch Thế Bằng Fenwick Tree Siêu Tốc**  
> **Bối cảnh:** Đếm số cặp nghịch thế $(i, j)$ có $i < j$ và $A_i > A_j$ trong dãy $N$ số nguyên lớn $|A_i| \le 10^9$.  
> **Input:** `5` \ `5 2 4 1 3` $\implies$ **Output:** `7`.

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int n;
vector<int> bitTree;

void update(int idx, int val) {
    for (; idx <= n; idx += idx & (-idx)) {
        bitTree[idx] += val;
    }
}

int getPrefixSum(int idx) {
    int sum = 0;
    for (; idx > 0; idx -= idx & (-idx)) {
        sum += bitTree[idx];
    }
    return sum;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;

    vector<int> a(n), vals;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        vals.push_back(a[i]);
    }

    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());

    bitTree.assign(n + 1, 0);
    long long invCount = 0;

    for (int i = n - 1; i >= 0; i--) {
        int rank = lower_bound(vals.begin(), vals.end(), a[i]) - vals.begin() + 1;
        invCount += getPrefixSum(rank - 1);
        update(rank, 1);
    }

    cout << invCount << "\n";
    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 21.3

##### Bài 21.3.1 — Đếm Số Cặp Nghịch Thế Cho Hoán Vị $1.N$
- **Bối cảnh:** Cho hoán vị $1.N$ ($N \le 10^5$). Đếm số cặp nghịch thế trong $\mathcal{O}(N \log N)$ (không cần nén tọa độ).
- **Input:** `3` \ `3 1 2` $\implies$ **Output:** `2` (cặp (3,1) và (3,2)).

##### Bài 21.3.2 — Đếm Số Phần Tử Lớn Hơn Đứng Trước Mỗi Vị Trí
- **Bối cảnh:** Với mỗi $i$, in ra số lượng phần tử $j < i$ có $A_j > A_i$.
- **Input:** `3` \ `2 1 3` $\implies$ **Output:** `0 1 0`

---

### Bài 21.4 — Mở rộng: Cập nhật đoạn, Truy vấn điểm và Fenwick 2D

#### 1. Bảng so sánh toàn diện
| Tiêu chí | Fenwick Tree (BIT) | Segment Tree |
|---|---|---|
| **Độ dài code** | Cực ngắn (5–10 dòng) | Dài (30–60 dòng) |
| **Hằng số thời gian** | Nhanh gấp 2–3 lần | Chậm hơn do đệ quy |
| **Bộ nhớ** | $\mathcal{O}(N)$ mảng | $\mathcal{O}(4N)$ mảng |
| **Phạm vi áp dụng** | Tổng tiền tố, phép toán nghịch đảo | Mọi phép toán (Min, Max, GCD, Gán đoạn..) |

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 21.4: Cập Nhật Đoạn Truy Vấn Điểm Bằng BIT Hiệu**  
> **Bối cảnh:** Thao tác 1: Cộng $V$ vào đoạn $[L, R]$. Thao tác 2: Tra cứu giá trị tại điểm $P$.  
> **Input:** `3 2` \ `0 0 0` \ `1 1 2 5` \ `2 2` $\implies$ **Output:** `5`.

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int n, q;
vector<long long> bitDiff;

void update(int idx, long long val) {
    for (; idx <= n; idx += idx & (-idx)) bitDiff[idx] += val;
}

long long queryPoint(int idx) {
    long long sum = 0;
    for (; idx > 0; idx -= idx & (-idx)) sum += bitDiff[idx];
    return sum;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> q)) return 0;
    bitDiff.assign(n + 1, 0);

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int l, r;
            long long val;
            cin >> l >> r >> val;
            update(l, val);
            update(r + 1, -val);
        } else {
            int p;
            cin >> p;
            cout << queryPoint(p) << "\n";
        }
    }

    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 21.4

##### Bài 21.4.1 — Fenwick 2D Tính Tổng Ma Trận Con
- **Bối cảnh:** Cập nhật điểm trên ô $(x, y)$ và tính tổng hình chữ nhật con từ $(1, 1)$ đến $(x, y)$ bằng 2D BIT.
- **Input:** `2 2 1` \ `1 1 5` \ `2 2 2` $\implies$ **Output:** `5`

##### Bài 21.4.2 — Tìm Phần Tử Nhỏ Nhất Bằng Cây Fenwick Tiền Tố
- **Bối cảnh:** Cài đặt Fenwick Tree lưu giá trị nhỏ nhất tiền tố `prefMin[i]` khi mảng chỉ có thao tác cập nhật giảm giá trị.
- **Input:** `3 1` \ `5 3 8` \ `1 3` $\implies$ **Output:** `3`

---

### Bài 21.5 — Luyện tập tổng hợp và đánh giá chương

### Đề bài 12 bài tập phân tầng tự chứa (iKHEDU Standard)

#### Tầng A — Củng cố nền tảng (Rating 1000 - 1200)

##### Bài 21.5.1 — Cây Fenwick Cộng Điểm Thưởng Cơ Bản
- **Bối cảnh:** $Q$ truy vấn cộng điểm cho học sinh tại vị trí $P$ và tính tổng điểm đoạn $[L, R]$.

##### Bài 21.5.2 — Đếm Cặp Nghịch Thế Bằng BIT Cho Hoán Vị
- **Bối cảnh:** Đếm số cặp nghịch thế trong hoán vị $1.N$ bằng cây Fenwick.

##### Bài 21.5.3 — Cập Nhật Đoạn Truy Vấn Điểm Bằng BIT Hiệu
- **Bối cảnh:** Range Update Point Query bằng mảng hiệu trên Fenwick Tree.

##### Bài 21.5.4 — Tìm Vị Trí Có Tổng Tiền Tố Đạt K Bằng Binary Lifting
- **Bối cảnh:** Tìm chỉ số $i$ nhỏ nhất có `getPrefixSum(i) >= K` trong $\mathcal{O}(\log N)$ bằng bước nhảy nhị phân trên BIT.

---

#### Tầng B — Vận dụng thi đấu (Rating 1200 - 1500)

##### Bài 21.5.5 — Đếm Số Cặp Nghịch Thế Cho Mảng Số Lớn $10^9$
- **Bối cảnh:** Kết hợp Nén tọa độ và Fenwick Tree tính số nghịch thế.

##### Bài 21.5.6 — Đếm Số Bộ Ba Nghịch Thế $A_i > A_j > A_k$
- **Bối cảnh:** Dùng 2 cây BIT đếm số phần tử lớn hơn bên trái và số phần tử nhỏ hơn bên phải của từng vị trí $j$.

##### Bài 21.5.7 — Fenwick Tree 2 Chiều Trên Ma Trận $N \times M$
- **Bối cảnh:** Cập nhật điểm ô $(x, y)$ và tính tổng hình chữ nhật con trên ma trận 2D bằng 2D BIT.

##### Bài 21.5.8 — Cập Nhật Đoạn Và Truy Vấn Đoạn Bằng 2 Cây BIT
- **Bối cảnh:** Range Update Range Query trên Fenwick Tree bằng 2 cây BIT `bit1` và `bit2`.

---

#### Tầng C — Chuyển giao & Nâng cao (Rating 1500 - 1800)

##### Bài 21.5.9 — Đếm Số Đoạn Con Có Tổng Nằm Trong $[L, R]$
- **Bối cảnh:** Kết hợp Prefix Sum, Nén tọa độ và Fenwick Tree đếm số cặp $(i, j)$ có $L \le P[j] - P[i-1] \le R$.

##### Bài 21.5.10 — Truy Vấn Offline Đếm Số Giá Trị Phân Biệt Trong Đoạn
- **Bối cảnh:** Sắp xếp $Q$ truy vấn theo đầu mút phải $R$ và dùng Fenwick Tree duy trì vị trí xuất hiện cuối cùng của từng số.

##### Bài 21.5.11 — Fenwick Tree Trên Cây (Flatten Tree Bằng Euler Tour)
- **Bối cảnh:** Biến đổi cây thành mảng 1D bằng thứ tự DFS Euler Tour và cập nhật/truy vấn tổng cây con bằng BIT.

##### Bài 21.5.12 — LIS Siêu Tốc Bằng Fenwick Tree
- **Bối cảnh:** Tìm độ dài dãy con tăng dài nhất trong $\mathcal{O}(N \log N)$ bằng cây Fenwick quản lý giá trị Max tiền tố.

---

### Bẫy lỗi thường gặp & Rubric đánh giá
| Lỗi thường gặp | Cách kiểm soát |
|---|---|
| Dùng chỉ số 0 trong cây BIT gây lặp vô hạn (vì `0 + (0 & -0) == 0`) | **Fenwick Tree BẮT BUỘC dùng chỉ số 1-based** ($1 \le \text{idx} \le N$) |
| Quên ép kiểu `long long` cho biến đếm nghịch thế khi $N = 2 \times 10^5$ | Biến đếm cặp nghịch thế phải là kiểu `long long` |

### Rubric hoàn thành chương
| Mức độ | Tiêu chí đánh giá |
|---|---|
| **Cơ bản (Tầng A)** | Cài đặt chính xác hàm Update và GetPrefixSum của Fenwick Tree. |
| **Vận dụng (Tầng B)** | Đếm số cặp nghịch thế kết hợp nén tọa độ và cài đặt 2D BIT. |
| **Thành thạo (Tầng C)** | Áp dụng BIT cho truy vấn offline đếm số phần tử phân biệt và Flatten Tree. |
