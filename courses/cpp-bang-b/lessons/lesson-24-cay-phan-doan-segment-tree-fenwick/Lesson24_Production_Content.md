# Bài 24: Cấu trúc cây phân đoạn (Segment Tree) & Fenwick Tree (BIT)

## 1. Bản chất bài toán truy vấn đoạn động (dynamic range queries)

Cho mảng $A$ gồm $N$ phần tử. Cần thực hiện liên tiếp $Q$ thao tác thuộc 2 loại:
1. **Cập nhật điểm (Point Update):** Thay đổi giá trị $A[i] \gets v$ (hoặc $A[i] \gets A[i] + v$).
2. **Truy vấn đoạn (Range Query):** Tính tổng $\sum_{k=L}^R A[k]$ hoặc tìm $\min_{k=L}^R A[k]$ / $\max_{k=L}^R A[k]$.

| Cấu Trúc | Khởi Tạo (Build) | Cập Nhật Điểm (Update) | Truy Vấn Đoạn (Query) | Bộ Nhớ |
|---|:---:|:---:|:---:|:---:|
| **Mảng Tiền Tố (Prefix Sum)** | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ *(Quá chậm khi có update)* | $\mathcal{O}(1)$ | $\mathcal{O}(N)$ |
| **Cây Fenwick (BIT)** | $\mathcal{O}(N)$ | $\mathcal{O}(\log N)$ *(Cực nhanh)* | $\mathcal{O}(\log N)$ | $\mathcal{O}(N)$ |
| **Cây Phân Đoạn (Segment Tree)** | $\mathcal{O}(N)$ | $\mathcal{O}(\log N)$ *(Cực nhanh)* | $\mathcal{O}(\log N)$ | $\mathcal{O}(4N)$ |

![So sánh các cấu trúc Range Query](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-21-cay-phan-doan-segment-tree-fenwick/assets/point_update_range_query_vi.svg)

## 2. Cây fenwick (Binary Indexed Tree — BIT)

![Cây Fenwick và Phép toán Lowbit](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-21-cay-phan-doan-segment-tree-fenwick/assets/fenwick_tree_lowbit_vi.svg)

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

![Cây Phân Đoạn Segment Tree](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-21-cay-phan-doan-segment-tree-fenwick/assets/segment_tree_binary_tree_vi.svg)

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

## 4. Các bẫy lỗi lập trình kinh điển

1. **Bẫy quên khai báo mảng Segment Tree kích thước $4N$:**
* Khai báo `tree[2 N]` hoặc `tree[N]` sẽ bị tràn mảng (Out of Bounds) khi $N = 10^5$. Bắt buộc phải khai báo kích thước tối thiểu $4N$ (`vector<long long> tree(4 n + 5)`).

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

## Câu hỏi trắc nghiệm củng cố khái niệm

#### Câu 1 (Khi nào dùng Segment Tree thay vì Fenwick Tree):

Ưu điểm quan trọng nhất của Segment Tree so với Fenwick Tree (BIT) cơ bản là gì

- **A.** Segment Tree chạy nhanh hơn và tốn ít bộ nhớ hơn.

- **B.** **[Đáp án đúng]** Segment Tree hỗ trợ mọi phép toán kết hợp như Range Minimum/Maximum (RMQ), GCD, trong khi Fenwick Tree cơ bản chỉ hỗ trợ các phép toán có tính nghịch đảo (như phép cộng tổng).

- **C.** Segment Tree code ngắn hơn.

- **D.** Segment Tree không dùng đệ quy.

> *Giải thích:* Phép toán $\min(x, y)$ không thể làm ngược lại (không có phép trừ min), do đó RMQ cần dùng Segment Tree.

#### Câu 2 (Kích thước mảng Segment Tree):

Với mảng $N$ phần tử, tại sao mảng cây Segment Tree dạng mảng 1D phẳng cần khai báo kích thước tối thiểu là $4N$

- **A.** Vì mỗi nút có 4 nút con.

- **B.** **[Đáp án đúng]** Vì khi $N$ không phải là lũy thừa của 2, cây nhị phân mở rộng xuống tầng lá tiếp theo có thể đạt tới chỉ số $4N - 1$.

- **C.** Để tránh tràn số nguyên.

- **D.** Vì cây có 4 tầng đệ quy.

> *Giải thích:* Chỉ số lớn nhất của nút lá trong cây nhị phân phân đoạn có thể đạt tới xấp xỉ $4N$. Khai báo $4N$ đảm bảo an toàn tuyệt đối 100%.

#### Câu 3 (Phép toán bit lowbit trong Fenwick Tree):

Giá trị của $\text{lowbit}(12)$ (tức $12 \ \& \ -12$) bằng bao nhiêu

- **A.** 1

- **B.** 2

- **C.** **[Đáp án đúng]** 4 (Số 12 có dạng nhị phân là $1100$, bit 1 thấp nhất có trọng số là $2^2 = 4$).

- **D.** 8

> *Giải thích:* $12 = 8 + 4 = 1100_2 \implies$ Bit 1 tận cùng bên phải có giá trị là 4.

#### Câu 4 (Bẫy số 0 trong Fenwick Tree):

Điều gì sẽ xảy ra nếu ta gọi hàm `update(0, val)` trên cây Fenwick Tree chuẩn

- **A.** Hàm cập nhật thành công ô số 0.

- **B.** **[Đáp án đúng]** Vòng lặp vô tận (Infinite Loop) vì $\text{lowbit}(0) == 0$, lệnh $x \gets x + (x \ \& \ -x)$ giữ nguyên `x = 0` mãi mãi $\implies$ TLE.

- **C.** Báo lỗi biên dịch.

- **D.** Không có chuyện gì xảy ra.

> *Giải thích:* $0 \ \& \ -0 = 0$, biến lặp không bao giờ tăng $\implies$ Cây Fenwick bắt buộc phải 1-based indexing.

#### Câu 5 (Độ phức tạp khởi tạo Build Segment Tree):

Hàm $build$ dựng toàn bộ cây Segment Tree $N$ phần tử từ mảng ban đầu có độ phức tạp thời gian là:

- **A.** $\mathcal{O}(N \log N)$

- **B.** **[Đáp án đúng]** $\mathcal{O}(N)$ tuyến tính (cây có tổng cộng $2N-1$ nút, mỗi nút tính trong $\mathcal{O}(1)$).

- **C.** $\mathcal{O}(N^2)$

- **D.** $\mathcal{O}(\log N)$

> *Giải thích:* Tổng số nút trên cây phân đoạn là $2N - 1$. Duyệt qua mỗi nút 1 lần duy nhất tốn $\mathcal{O}(N)$.

#### Câu 6 (Đếm số cặp nghịch thế bằng Fenwick Tree):

Để đếm số lượng cặp số nghịch thế ($i < j$ và $A[i] > A[j]$) trong mảng $N$ phần tử, ta kết hợp Fenwick Tree với kỹ thuật nào

- **A.** Thuật toán hai con trỏ.

- **B.** **[Đáp án đúng]** Nén tọa độ về $[1, N]$, duyệt từ phải sang trái: cộng dồn `query(A[i] - 1)` vào đáp án rồi gọi `update(A[i], 1)` trong tổng thời gian $\mathcal{O}(N \log N)$.

- **C.** Tìm kiếm nhị phân.

- **D.** Quy hoạch động 2 chiều.

> *Giải thích:* Fenwick Tree đóng vai trò mảng đếm tần suất động, `query(A[i] - 1)` đếm số phần tử nhỏ hơn $A[i]$ đã xuất hiện phía sau.

#### Câu 7 (Độ phức tạp mỗi truy vấn Segment Tree):

Tại sao hàm `query(L, R)` trên Segment Tree chỉ mất tối đa $\mathcal{O}(\log N)$ dù phải rẽ nhánh đệ quy

- **A.** Vì cây chỉ có 2 nút lá.

- **B.** **[Đáp án đúng]** Vì tại mỗi tầng của cây, truy vấn chỉ ghé thăm tối đa 4 nút (các đoạn nằm trọn bên trong trả về kết quả ngay lập tức).

- **C.** Vì hàm query không dùng đệ quy.

- **D.** Vì mảng đã được sắp xếp.

> *Giải thích:* Bằng chứng minh toán học, số lượng nút được duyệt tại mỗi độ sâu của cây luôn $\le 4 \implies 4 \log_2 N = \mathcal{O}(\log N)$.

#### Câu 8 (Cập nhật đoạn Range Update & Điểm Point Query bằng Fenwick):

Để hỗ trợ thao tác "Cộng thêm $v$ vào toàn bộ đoạn $[L, R]$" và "Hỏi giá trị tại vị trí $i$", ta cài đặt Fenwick Tree trên mảng nào

- **A.** Trên mảng gốc $A$.

- **B.** **[Đáp án đúng]** Trên Mảng hiệu (Difference Array $D[i] = A[i] - A[i-1]$): Update đoạn bằng `update(L, v)` và `update(R + 1, -v)`; Query điểm bằng `query(i)`.

- **C.** Trên mảng tiền tố.

- **D.** Trên mảng đảo ngược.

> *Giải thích:* Sự kết hợp hoàn hảo giữa Mảng hiệu (Chuyên đề 04) và Cây Fenwick cho phép biến Range Update thành 2 phép Point Update.

#### Câu 9 (Tìm kiếm K-th phần tử trên Fenwick Tree):

Để tìm phần tử thứ $K$ nhỏ nhất còn tồn tại trong tập hợp bằng Fenwick Tree, ta áp dụng kỹ thuật nào trong $\mathcal{O}(\log N)$

- **A.** Tìm kiếm nhị phân thông thường $\mathcal{O}(\log^2 N)$.

- **B.** **[Đáp án đúng]** Nhảy nhị phân trực tiếp trên cây Fenwick (Binary Lifting on BIT / BIT Walking) trong $\mathcal{O}(\log N)$.

- **C.** Duyệt tuần tự $\mathcal{O}(N)$.

- **D.** Sắp xếp lại cây.

> *Giải thích:* Tương tự tìm kiếm nhị phân các lũy thừa của 2, tận dụng cấu trúc các bước nhảy $2^p$ của Fenwick Tree.

#### Câu 10 (Nút cha và nút con trong Segment Tree dạng mảng):

Nút hiện tại có chỉ số $id$. Chỉ số của nút con trái và nút con phải lần lượt là:

- **A.** $id + 1$ và $id + 2$

- **B.** **[Đáp án đúng]** $2 \cdot id$ (hoặc `id << 1`) và $2 \cdot id + 1$ (hoặc `(id << 1) | 1`).

- **C.** $id/2$ và $id/2 + 1$

- **D.** $id \cdot 4$ và $id \cdot 4 + 1$

> *Giải thích:* Đây là cách định vị nút chuẩn mực trong biểu diễn cây nhị phân hoàn hảo trên mảng 1 chiều.

#### Câu 11 (Truy vấn ước chung lớn nhất Range GCD):

Khi dùng Segment Tree để tính $\text{GCD}(A[L \dots R])$, công thức kết hợp tại mỗi nút cha là:

- **A.** $tree[id] = tree[2 \cdot id] + tree[2 \cdot id + 1]$

- **B.** **[Đáp án đúng]** $tree[id] = \gcd(tree[2 \cdot id], tree[2 \cdot id + 1])$

- **C.** $tree[id] = \min(tree[2 \cdot id], tree[2 \cdot id + 1])$

- **D.** $tree[id] = tree[2 \cdot id] \times tree[2 \cdot id + 1]$

> *Giải thích:* Phép tính GCD có tính kết hợp: $\text{GCD}(a, b, c) = \text{GCD}(\text{GCD}(a, b), c)$, áp dụng tự nhiên trên Segment Tree.

#### Câu 12 (Điều kiện dừng đệ quy trong Query Segment Tree):

Trong hàm `query(id, l, r, u, v)`, khi đoạn hiện tại $[l, r]$ nằm hoàn toàn bên ngoài đoạn truy vấn $[u, v]$ ($r < u$ hoặc $v < l$), ta trả về giá trị gì cho bài toán Range Sum

- **A.** Trả về $1$.

- **B.** **[Đáp án đúng]** Trả về $0$ (Phần tử trung hòa của phép cộng).

- **C.** Trả về vô cùng $\infty$.

- **D.** Báo lỗi và dừng chương trình.

> *Giải thích:* Giá trị trung hòa của phép cộng là 0 (đối với phép tìm Min là $+\infty$, phép tìm Max là $-\infty$, phép nhân là $1$).

#### Câu 13 (Segment Tree không đệ quy — Iterative Segment Tree):

Ưu điểm lớn nhất của Cây phân đoạn không đệ quy (Iterative / Bottom-Up Segment Tree) là:

- **A.** Hỗ trợ nhiều phép toán hơn.

- **B.** **[Đáp án đúng]** Tốc độ chạy nhanh hơn gấp 2–3 lần do loại bỏ hoàn toàn chi phí gọi hàm đệ quy và chỉ tốn đúng $2N$ bộ nhớ.

- **C.** Tự động nén tọa độ.

- **D.** Không cần truyền chỉ số.

> *Giải thích:* Cây phân đoạn duyệt từ lá lên gốc (Bottom-Up) có hằng số thời gian cực nhỏ và code rất ngắn gọn.

#### Câu 14 (Đếm số lượng số 0 trong đoạn):

Để đếm số lượng số 0 trong đoạn $[L, R]$ hỗ trợ cập nhật điểm, cấu hình Segment Tree lưu trữ gì

- **A.** Lưu tổng các số.

- **B.** **[Đáp án đúng]** Mỗi lá lưu $1$ nếu $A[i] == 0$ (ngược lại lưu $0$), các nút cha lưu tổng số lượng số 0 của hai con: $tree[id] = tree[2 \cdot id] + tree[2 \cdot id + 1]$.

- **C.** Lưu giá trị nhỏ nhất.

- **D.** Dùng mảng hiệu.

> *Giải thích:* Quy đổi bài toán đếm sang tính tổng các cờ boolean trên cây phân đoạn.

#### Câu 15 (Kỹ thuật Lazy Propagation — Giới thiệu mở rộng):

Khi cần thực hiện **Cập nhật cả đoạn (Range Update)** và **Truy vấn cả đoạn (Range Query)** trên Segment Tree trong $\mathcal{O}(\log N)$, kỹ thuật nào được áp dụng

- **A.** Dùng đệ quy quay lui.

- **B.** **[Đáp án đúng]** Kỹ thuật Lan truyền lười (Lazy Propagation): Chỉ cập nhật nút hiện tại và lưu giá trị chờ (lazy tag), chỉ đẩy xuống con khi có truy vấn cần thiết.

- **C.** Dùng 2 cây Fenwick.

- **D.** Chia mảng thành $\sqrt{N}$ khối (Mo's Algorithm).

> *Giải thích:* Lazy Propagation là kỹ thuật đỉnh cao trì hoãn cập nhật giúp thực hiện Range Update trong $\mathcal{O}(\log N)$.

## Ma trận bài tập thực hành (P0 → P5)

| Mã Bài Tập | Tên Bài Toán | Mức Độ | Trọng Tâm Kiến Thức & Kỹ Năng Range Query |
|---|---|:---:|---|
| `CPPB-RNG-01` | Cài Đặt Fenwick Tree Tính Tổng Đoạn | **P0** | Cài đặt chuẩn `update` và `query` trên cây BIT 1-based. |
| `CPPB-RNG-02` | Cài Đặt Segment Tree Tìm Min Đoạn (RMQ) | **P1** | Hàm `build`, `update` điểm và `query` trên cây nhị phân $4N$. |
| `CPPB-RNG-03` | Cập Nhật Đoạn & Truy Vấn Điểm Bằng BIT | **P1** | Fenwick Tree trên Mảng hiệu $D[i]$ hỗ trợ Range Add. |
| `CPPB-RNG-04` | Tìm Giá Trị Lớn Nhất & Đếm Số Lần Xuất Hiện | **P2** | Segment Tree lưu cặp `(max_val, count)` kết hợp tại nút cha. |
| `CPPB-RNG-05` | Đếm Số Cặp Nghịch Thế (Inversion Count) | **P2** | Nén tọa độ kết hợp Fenwick Tree đếm số phần tử nhỏ hơn phía sau. |
| `CPPB-RNG-06` | Truy Vấn Ước Chung Lớn Nhất Đoạn (Range GCD) | **P2** | Segment Tree với hàm kết hợp `std::gcd` $\mathcal{O}(\log N)$. |
| `CPPB-RNG-07` | Tìm Phần Tử Thứ K Nhỏ Nhất (K-th Element) | **P2** | Nhảy nhị phân trên Fenwick Tree (Binary Lifting on BIT). |
| `CPPB-RNG-08` | Tìm Vị Trí Đầu Tiên Có Giá Trị >= X | **P3** | Tìm kiếm nhị phân trực tiếp trên Segment Tree trong $\mathcal{O}(\log N)$. |
| `CPPB-RNG-09` | Dãy Con Tăng Dài Nhất LIS O(N log N) Bằng BIT | **P3** | Nén tọa độ, dùng BIT lưu $\max(dp)$ theo tiền tố giá trị. |
| `CPPB-RNG-10` | Đoạn Con Có Tổng Lớn Nhất (Maximum Subarray Sum) | **P3** | Segment Tree lưu 4 giá trị: `sum`, `pref_max`, `suff_max`, `max_sub`. |
| `CPPB-RNG-11` | Đếm Số Điểm Nằm Trong Hình Chữ Nhật | **P3** | Đường quét (Sweep-line) theo trục $X$ kết hợp Fenwick Tree trên trục $Y$. |
| `CPPB-RNG-12` | Đổi Dấu Đoạn & Tìm Tổng Lớn Nhất | **P4** | Segment Tree lưu trạng thái đa trường hỗ trợ truy vấn phức tạp. |
| `CPPB-RNG-13` | Cây Phân Đoạn 2D Độc Lập (2D Fenwick Tree) | **P4** | BIT lồng nhau 2 chiều `bit[x][y]` tính tổng hình chữ nhật con. |
| `CPPB-RNG-14` | Giới Thiệu Lazy Propagation Cộng Đoạn | **P4** | Kỹ thuật gắn nhãn `lazy` hỗ trợ Range Add & Range Sum $\mathcal{O}(\log N)$. |
| `CPPB-RNG-15` | Hệ Thống Quản Lý Dữ Liệu Olympic (Mastery) | **P5** | Bài toán cấu trúc dữ liệu tổng hợp kết hợp Segment Tree và hình học/đồ thị. |
