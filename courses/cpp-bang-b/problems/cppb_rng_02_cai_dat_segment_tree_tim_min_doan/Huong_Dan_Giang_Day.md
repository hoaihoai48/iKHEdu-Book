# Hướng Dẫn Giảng Dạy: Cài Đặt Segment Tree Tìm Min Đoạn (RMQ)

Chuyên đề: **Cấu Trúc Dữ Liệu Cây Phân Đoạn (Segment Tree & Fenwick Tree / BIT)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho mảng $A$ gồm $N$ số nguyên và $Q$ truy vấn thuộc hai dạng: `1 pos val` (gán $A[pos] = val$) và `2 L R` (tìm giá trị nhỏ nhất trong đoạn từ $L$ đến $R$). Hãy in ra kết quả của các truy vấn loại 2.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Fenwick Tree (Binary Indexed Tree):**
* Tận dụng phép toán bit `lowbit(i) = i & (-i)` để lưu tổng các đoạn luỹ thừa của 2.
* Cập nhật điểm trong $\mathcal{O}(\log N)$, truy vấn tổng tiền tố trong $\mathcal{O}(\log N)$ với dung lượng bộ nhớ đúng bằng $N$ phần tử.
- **Segment Tree (Cây phân đoạn):**
* Cấu trúc cây nhị phân đầy đủ quản lý các đoạn con liên tiếp, cần mảng kích thước $4N$.
* Hỗ trợ đa dạng phép toán gộp (tổng, $\min, \max$, GCD) trong $\mathcal{O}(\log N)$ và kỹ thuật Lazy Propagation cho các truy vấn cập nhật đoạn.
- **Độ phức tạp:** Xây dựng cây $\mathcal{O}(N)$, mỗi thao tác truy vấn / cập nhật chỉ tốn $\mathcal{O}(\log N)$.

---

## 2. Bảng chạy tay trên số liệu mẫuMẫu thử (Sample 1): Đầu vào: `5 3 5 2 4 1 3 2 1 3 1 4 10 2 3 5` $\implies$ Đầu ra kỳ vọng: `2 3`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `5 3 5 2 4 1 3 2 1 3 1 4 10 2 3 5` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với mảng $[5, 2, 8, 1, 9]$: - Truy vấn tìm min đoạn từ 1 đến 3: $\min(5, 2, 8) = 2$. - Cập nhật vị trí 2 thành 10: mảng thành $[5, 10, ... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `2 3` |

*Giải thích chi tiết:* Với mảng $[5, 2, 8, 1, 9]$:

- Truy vấn tìm min đoạn từ 1 đến 3: $\min(5, 2, 8) = 2$.
- Cập nhật vị trí 2 thành 10: mảng thành $[5, 10, 8, 1, 9]$.
- Truy vấn lại min đoạn từ 1 đến 3: $\min(5, 10, 8) = 5$.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
* Khai báo mảng Segment Tree quá nhỏ: Cần tối thiểu $4N$ phần tử (`vector<long long> tree(4 * N)`), khai báo $2N$ sẽ bị tràn chỉ số mảng khi cây bị lệch.
* Fenwick Tree bắt buộc phải dùng chỉ số bắt đầu từ $1$ (1-based index). Nếu gọi `lowbit(0)` thì `0 & (-0) = 0`, vòng lặp `while (i <= N)` sẽ bị lặp vô tận.
* Khi cây quản lý phép cộng dồn, giá trị các nút trên cây có thể vượt quá $2 \times 10^9$, bắt buộc phải khai báo kiểu `long long` cho toàn bộ các nút của cây.

---

## 4. Lời giải tham khảo
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
