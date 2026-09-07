# Hướng Dẫn Giảng Dạy: Đếm Số Điểm Trong Hình Chữ Nhật (2D Range Query)

Chuyên đề: **Cấu Trúc Dữ Liệu Cây Phân Đoạn (Segment Tree & Fenwick Tree / BIT)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho danh sách tọa độ $N$ điểm và $Q$ truy vấn hình chữ nhật. Hãy lập trình đếm số lượng điểm nằm trong từng hình chữ nhật.

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
Mẫu thử (Sample 1): Đầu vào: `3 2 1 1 2 2 3 3 1 1 2 2 2 2 4 4` $\implies$ Đầu ra kỳ vọng: `2 2`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `3 2 1 1 2 2 3 3 1 1 2 2 2 2 4 4` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với 3 điểm $(1, 2), (2, 3), (4, 5)$ và vùng quan sát từ $(1, 1)$ đến $(3, 4)$: Hai điểm $(1, 2)$ và $(2, 3)$ nằm trọn vẹn bên trong vùn... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `2 2` |

*Giải thích chi tiết:* Với 3 điểm $(1, 2), (2, 3), (4, 5)$ và vùng quan sát từ $(1, 1)$ đến $(3, 4)$:
Hai điểm $(1, 2)$ và $(2, 3)$ nằm trọn vẹn bên trong vùng hình chữ nhật. Điểm $(4, 5)$ nằm ngoài. Số điểm đếm được là 2.

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

struct Point {
    int x, y;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<Point> pts(n);
    for (int i = 0; i < n; ++i) cin >> pts[i].x >> pts[i].y;

    while (q--) {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        int count = 0;
        for (int i = 0; i < n; ++i) {
            if (pts[i].x >= x1 && pts[i].x <= x2 && pts[i].y >= y1 && pts[i].y <= y2) {
                count++;
            }
        }
        cout << count << "\n";
    }
    return 0;
}
```
