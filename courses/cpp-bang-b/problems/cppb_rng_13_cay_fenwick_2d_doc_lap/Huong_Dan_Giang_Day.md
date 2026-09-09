# Hướng Dẫn Giảng Dạy: Cây Fenwick 2D Tính Tổng Hình Chữ Nhật (2D BIT)

Chuyên đề: **Cấu Trúc Dữ Liệu Cây Phân Đoạn (Segment Tree & Fenwick Tree / BIT)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho ma trận độ sáng ban đầu và $Q$ thao tác thuộc hai dạng: cập nhật điểm ảnh hoặc truy vấn tổng vùng hình chữ nhật. Hãy in ra kết quả của các thao tác truy vấn.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Fenwick Tree (Binary Indexed Tree):**
* Tận dụng phép toán bit `lowbit(i) = i & (-i)` để lưu tổng các đoạn luỹ thừa của 2.
* Cập nhật điểm trong $\mathcal{O}(\log N)$, truy vấn tổng tiền tố trong $\mathcal{O}(\log N)$ với dung lượng bộ nhớ đúng bằng $N$ phần tử.
- **Segment Tree (Cây phân đoạn):**
* Cấu trúc cây nhị phân đầy đủ quản lý các đoạn con liên tiếp, cần mảng kích thước $4N$.
* Hỗ trợ đa dạng phép toán gộp (tổng, $\min, \max$, GCD) trong $\mathcal{O}(\log N)$ và kỹ thuật Lazy Propagation cho các truy vấn cập nhật đoạn.
- **Độ phức tạp:** Xây dựng cây $\mathcal{O}(N)$, mỗi thao tác truy vấn / cập nhật chỉ tốn $\mathcal{O}(\log N)$.

---

## 2. Bảng chạy tay trên số liệu mẫuMẫu thử (Sample 1): Đầu vào: `3 3 3 1 1 1 5 1 2 2 10 2 1 1 2 2` $\implies$ Đầu ra kỳ vọng: `15`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `3 3 3 1 1 1 5 1 2 2 10 2 1 1 2 2` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với ma trận $3 × 3$ toàn số 1: Tổng độ sáng của hình chữ nhật con kích thước $2 × 2$ từ $(1, 1)$ đến $(2, 2)$ gồm 4 ô số 1, tổng bằng 4. | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `15` |

*Giải thích chi tiết:* Với ma trận $3 × 3$ toàn số 1: Tổng độ sáng của hình chữ nhật con kích thước $2 × 2$ từ $(1, 1)$ đến $(2, 2)$ gồm 4 ô số 1, tổng bằng 4.

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

int n, m, q;
vector<vector<long long>> bit;

void update(int r, int c, long long val) {
for (int i = r; i <= n; i += i & -i) {
for (int j = c; j <= m; j += j & -j) {
bit[i][j] += val;
}
}
}

long long query(int r, int c) {
long long sum = 0;
for (int i = r; i > 0; i -= i & -i) {
for (int j = c; j > 0; j -= j & -j) {
sum += bit[i][j];
}
}
return sum;
}

long long queryRange(int r1, int c1, int r2, int c2) {
return query(r2, c2) - query(r1 - 1, c2) - query(r2, c1 - 1) + query(r1 - 1, c1 - 1);
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

if (!(cin >> n >> m >> q)) return 0;

bit.assign(n + 1, vector<long long>(m + 1, 0));

while (q--) {
int type;
cin >> type;
if (type == 1) {
int r, c;
long long val;
cin >> r >> c >> val;
update(r, c, val);
} else {
int r1, c1, r2, c2;
cin >> r1 >> c1 >> r2 >> c2;
cout << queryRange(r1, c1, r2, c2) << "\n";
}
}
return 0;
}
```
