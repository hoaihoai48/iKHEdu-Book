# Hướng Dẫn Giảng Dạy: Min Mọi Cửa Sổ Trượt Bằng Monotonic Deque O(N)

Chuyên đề: **Cấu Trúc Dữ Liệu Hàng Đợi (Queue, Deque) & Monotonic Deque**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho mảng $A$ gồm $N$ số nguyên và kích thước cửa sổ $K$. Hãy lập trình tìm giá trị nhỏ nhất trong mỗi cửa sổ trượt kích thước $K$ khi di chuyển từ trái sang phải.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Nguyên lý Hàng đợi chuẩn (Queue):** Vào trước Ra trước (FIFO), là cấu trúc nền tảng phục vụ duyệt đồ thị theo chiều rộng (BFS).
- **Hàng đợi hai đầu (Deque) & Monotonic Deque:**
  * Hỗ trợ thêm/xoá ở cả hai đầu trong $\mathcal{O}(1)$.
  * Khi trượt cửa sổ kích thước $K$, lưu chỉ số phần tử trong deque sao cho giá trị tương ứng luôn đơn điệu.
  * Loại bỏ phần tử trượt ra khỏi cửa sổ ở đầu trước (`pop_front()`) và loại bỏ phần tử kém tối ưu ở đầu sau (`pop_back()`).
- **Độ phức tạp:** Thời gian $\mathcal{O}(N)$, không gian phụ trợ $\mathcal{O}(K)$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table)
Mẫu thử (Sample 1): Đầu vào: `8 3 1 3 -1 -3 5 3 6 7` $\implies$ Đầu ra kỳ vọng: `-1 -3 -3 -3 3 3`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `8 3 1 3 -1 -3 5 3 6 7` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với mảng $[1, 3, -1, -3, 5, 3, 6, 7]$ và cửa sổ $K = 3$: - Cửa sổ 1 [1, 3, -1] -> min = -1. - Cửa sổ 2 [3, -1, -3] -> min = -3. - Cửa s... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `-1 -3 -3 -3 3 3` |

*Giải thích chi tiết:* Với mảng $[1, 3, -1, -3, 5, 3, 6, 7]$ và cửa sổ $K = 3$:
- Cửa sổ 1 [1, 3, -1] -> min = -1.
- Cửa sổ 2 [3, -1, -3] -> min = -3.
- Cửa sổ 3 [-1, -3, 5] -> min = -3.
- Cửa sổ 4 [-3, 5, 3] -> min = -3.
- Cửa sổ 5 [5, 3, 6] -> min = 3.
- Cửa sổ 6 [3, 6, 7] -> min = 3.
Kết quả in ra: -1 -3 -3 -3 3 3.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
* Lưu giá trị thay vì lưu chỉ số vị trí (index) trong Deque: Phải lưu index để kiểm tra điều kiện phần tử đã trượt ra khỏi cửa sổ $i - K$ hay chưa (`dq.front() <= i - K`).
* Quên kiểm tra `!dq.empty()` trước khi truy xuất `dq.front()` hoặc `dq.back()` gây crash chương trình.
* Không khởi tạo kết quả cho $K-1$ vị trí đầu tiên trước khi bắt đầu ghi nhận đáp án từ vị trí thứ $K$.

---

## 4. Lời giải tham khảo
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;
    if (n <= 0 || k <= 0 || k > n) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    deque<int> dq;
    vector<long long> ans;

    for (int i = 0; i < n; ++i) {
        while (!dq.empty() && dq.front() < i - k + 1) dq.pop_front();
        while (!dq.empty() && a[dq.back()] >= a[i]) dq.pop_back();
        dq.push_back(i);

        if (i >= k - 1) ans.push_back(a[dq.front()]);
    }

    for (int i = 0; i < (int)ans.size(); ++i) {
        cout << ans[i] << (i + 1 == (int)ans.size() ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```
