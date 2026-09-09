# Hướng Dẫn Giảng Dạy: Lazy Propagation — Cập Nhật & Truy Vấn Đoạn (Range Add Range Sum)

Chuyên đề: **Cấu Trúc Dữ Liệu Cây Phân Đoạn (Segment Tree & Fenwick Tree / BIT)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho mảng $A$ và $Q$ thao tác: `1 L R V` (cộng $V$ vào tất cả các phần tử từ $L$ đến $R$) và `2 L R` (tính tổng các phần tử trong đoạn $[L, R]$). Hãy in ra kết quả cho các thao tác loại 2.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Fenwick Tree (Binary Indexed Tree):**
* Tận dụng phép toán bit `lowbit(i) = i & (-i)` để lưu tổng các đoạn luỹ thừa của 2.
* Cập nhật điểm trong $\mathcal{O}(\log N)$, truy vấn tổng tiền tố trong $\mathcal{O}(\log N)$ với dung lượng bộ nhớ đúng bằng $N$ phần tử.
- **Segment Tree (Cây phân đoạn):**
* Cấu trúc cây nhị phân đầy đủ quản lý các đoạn con liên tiếp, cần mảng kích thước $4N$.
* Hỗ trợ đa dạng phép toán gộp (tổng, $\min, \max$, GCD) trong $\mathcal{O}(\log N)$ và kỹ thuật Lazy Propagation cho các truy vấn cập nhật đoạn.
- **Độ phức tạp:** Xây dựng cây $\mathcal{O}(N)$, mỗi thao tác truy vấn / cập nhật chỉ tốn $\mathcal{O}(\log N)$.

---

## 2. Bảng chạy tay trên số liệu mẫuMẫu thử (Sample 1): Đầu vào: `5 3 1 2 3 4 5 1 2 4 2 2 1 5 2 2 4` $\implies$ Đầu ra kỳ vọng: `21 15`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `5 3 1 2 3 4 5 1 2 4 2 2 1 5 2 2 4` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với mảng ban đầu $[1, 2, 3, 4, 5]$: - Cộng thêm 2 vào đoạn từ vị trí 2 đến 4: mảng trở thành $[1, 4, 5, 6, 5]$. - Truy vấn tổng đoạn từ... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `21 15` |

*Giải thích chi tiết:* Với mảng ban đầu $[1, 2, 3, 4, 5]$:

- Cộng thêm 2 vào đoạn từ vị trí 2 đến 4: mảng trở thành $[1, 4, 5, 6, 5]$.
- Truy vấn tổng đoạn từ 1 đến 5: $1 + 4 + 5 + 6 + 5 = 21$.

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
