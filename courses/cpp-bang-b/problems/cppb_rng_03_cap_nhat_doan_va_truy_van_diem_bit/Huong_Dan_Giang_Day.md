# Hướng Dẫn Giảng Dạy: Cập Nhật Đoạn & Truy Vấn Điểm (Range Update Point Query)

Chuyên đề: **Cấu Trúc Dữ Liệu Cây Phân Đoạn (Segment Tree & Fenwick Tree / BIT)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho mảng $A$ và $Q$ thao tác thuộc hai dạng: `1 L R V` (cộng thêm $V$ vào tất cả các phần tử từ $L$ đến $R$) và `2 pos` (in ra giá trị hiện tại của phần tử tại vị trí $pos$). Hãy in ra kết quả của các thao tác loại 2.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Fenwick Tree (Binary Indexed Tree):**
* Tận dụng phép toán bit `lowbit(i) = i & (-i)` để lưu tổng các đoạn luỹ thừa của 2.
* Cập nhật điểm trong $\mathcal{O}(\log N)$, truy vấn tổng tiền tố trong $\mathcal{O}(\log N)$ với dung lượng bộ nhớ đúng bằng $N$ phần tử.
- **Segment Tree (Cây phân đoạn):**
* Cấu trúc cây nhị phân đầy đủ quản lý các đoạn con liên tiếp, cần mảng kích thước $4N$.
* Hỗ trợ đa dạng phép toán gộp (tổng, $\min, \max$, GCD) trong $\mathcal{O}(\log N)$ và kỹ thuật Lazy Propagation cho các truy vấn cập nhật đoạn.
- **Độ phức tạp:** Xây dựng cây $\mathcal{O}(N)$, mỗi thao tác truy vấn / cập nhật chỉ tốn $\mathcal{O}(\log N)$.

---

## 2. Bảng chạy tay trên số liệu mẫuMẫu thử (Sample 1): Đầu vào: `5 3 1 2 3 4 5 1 2 4 5 2 3 2 1` $\implies$ Đầu ra kỳ vọng: `8 1`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `5 3 1 2 3 4 5 1 2 4 5 2 3 2 1` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với mảng ban đầu toàn số 0: $[0, 0, 0, 0, 0]$: - Cộng thêm 5 vào đoạn từ vị trí 2 đến 4: mảng thành $[0, 5, 5, 5, 0]$. - Truy vấn giá t... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `8 1` |

*Giải thích chi tiết:* Với mảng ban đầu toàn số 0: $[0, 0, 0, 0, 0]$:

- Cộng thêm 5 vào đoạn từ vị trí 2 đến 4: mảng thành $[0, 5, 5, 5, 0]$.
- Truy vấn giá trị tại vị trí 3: in ra 5.

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
