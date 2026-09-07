# Hướng Dẫn Giảng Dạy: Tìm Phần Tử Thứ K Nhỏ Nhất (K-th Element on BIT)

Chuyên đề: **Cấu Trúc Dữ Liệu Cây Phân Đoạn (Segment Tree & Fenwick Tree / BIT)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho một tập hợp các số nguyên hỗ trợ hai thao tác: thêm một số vào tập hợp, và tìm phần tử nhỏ thứ $K$ trong tập hợp. Hãy lập trình in ra kết quả cho các thao tác tìm kiếm.

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
Mẫu thử (Sample 1): Đầu vào: `5 1 10 1 20 1 15 2 2 2 3` $\implies$ Đầu ra kỳ vọng: `15 20`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `5 1 10 1 20 1 15 2 2 2 3` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với tập hợp các số {10, 20, 30, 40, 50}: Phần tử nhỏ thứ 3 trong tập hợp là số 30. | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `15 20` |

*Giải thích chi tiết:* Với tập hợp các số {10, 20, 30, 40, 50}:
Phần tử nhỏ thứ 3 trong tập hợp là số 30.

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

const int MAX_VAL = 200000;

struct FenwickTree {
    int bit[MAX_VAL + 5];
    FenwickTree() { memset(bit, 0, sizeof(bit)); }

    void update(int x, int val) {
        for (; x <= MAX_VAL; x += x & -x) bit[x] += val;
    }

    int findKth(int k) {
        int idx = 0;
        for (int i = 1 << 18; i > 0; i >>= 1) {
            if (idx + i <= MAX_VAL && bit[idx + i] < k) {
                idx += i;
                k -= bit[idx];
            }
        }
        return idx + 1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;

    FenwickTree ft;

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int x;
            cin >> x;
            ft.update(x, 1);
        } else {
            int k;
            cin >> k;
            cout << ft.findKth(k) << "\n";
        }
    }
    return 0;
}
```
