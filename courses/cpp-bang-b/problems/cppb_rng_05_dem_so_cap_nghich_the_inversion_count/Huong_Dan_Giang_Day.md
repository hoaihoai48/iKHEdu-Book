# Hướng Dẫn Giảng Dạy: Đếm Số Cặp Nghịch Thế (Inversion Count)

Chuyên đề: **Cấu Trúc Dữ Liệu Cây Phân Đoạn (Segment Tree & Fenwick Tree / BIT)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho mảng $A$ gồm $N$ số nguyên. Hãy lập trình đếm tổng số lượng cặp nghịch thế trong mảng.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Fenwick Tree (Binary Indexed Tree):**
  * Tận dụng phép toán bit `lowbit(i) = i & (-i)` để lưu tổng các đoạn luỹ thừa của 2.
  * Cập nhật điểm trong $\mathcal{O}(\log N)$, truy vấn tổng tiền tố trong $\mathcal{O}(\log N)$ với dung lượng bộ nhớ đúng bằng $N$ phần tử.
- **Segment Tree (Cây phân đoạn):**
  * Cấu trúc cây nhị phân đầy đủ quản lý các đoạn con liên tiếp, cần mảng kích thước $4N$.
  * Hỗ trợ đa dạng phép toán gộp (tổng, $\min, \max$, GCD) trong $\mathcal{O}(\log N)$ và kỹ thuật Lazy Propagation cho các truy vấn cập nhật đoạn.
- **Độ phức tạp:** Xây dựng cây $\mathcal{O}(N)$, mỗi thao tác truy vấn / cập nhật chỉ tốn $\mathcal{O}(\log N)$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table)
Mẫu thử (Sample 1): Đầu vào: `5 2 4 1 3 5` $\implies$ Đầu ra kỳ vọng: `3`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `5 2 4 1 3 5` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với mảng gồm 5 phần tử $[2, 4, 1, 3, 5]$: Các cặp nghịch thế gồm: - (2, 1) vì $2 > 1$. - (4, 1) vì $4 > 1$. - (4, 3) vì $4 > 3$. Có tất... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `3` |

*Giải thích chi tiết:* Với mảng gồm 5 phần tử $[2, 4, 1, 3, 5]$:
Các cặp nghịch thế gồm:
- (2, 1) vì $2 > 1$.
- (4, 1) vì $4 > 1$.
- (4, 3) vì $4 > 3$.
Có tất cả 3 cặp nghịch thế, kết quả in ra là 3.

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
