# Hướng Dẫn Giảng Dạy: Chọn Đoạn Tối Đa Không Quá K Phần Tử Liền Kề

Chuyên đề: **Cấu Trúc Dữ Liệu Hàng Đợi (Queue, Deque) & Monotonic Deque**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho danh sách doanh thu của $N$ vị trí và giới hạn $K$. Hãy lập trình chọn các vị trí treo biển sao cho không có quá $K$ vị trí liền kề được chọn và tổng doanh thu thu về là lớn nhất.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Nguyên lý Hàng đợi chuẩn (Queue):** Vào trước Ra trước (FIFO), là cấu trúc nền tảng phục vụ duyệt đồ thị theo chiều rộng (BFS).
- **Hàng đợi hai đầu (Deque) & Monotonic Deque:**
* Hỗ trợ thêm/xoá ở cả hai đầu trong $\mathcal{O}(1)$.
* Khi trượt cửa sổ kích thước $K$, lưu chỉ số phần tử trong deque sao cho giá trị tương ứng luôn đơn điệu.
* Loại bỏ phần tử trượt ra khỏi cửa sổ ở đầu trước (`pop_front()`) và loại bỏ phần tử kém tối ưu ở đầu sau (`pop_back()`).
- **Độ phức tạp:** Thời gian $\mathcal{O}(N)$, không gian phụ trợ $\mathcal{O}(K)$.

---

## 2. Bảng chạy tay trên số liệu mẫuMẫu thử (Sample 1): Đầu vào: `5 2 1 2 3 4 5` $\implies$ Đầu ra kỳ vọng: `12`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `5 2 1 2 3 4 5` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với 5 vị trí có doanh thu $[1, 2, 3, 4, 5]$ và giới hạn $K = 2$ (không được chọn quá 2 vị trí liên tiếp): Phương án tối ưu là bỏ chọn v... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `12` |

*Giải thích chi tiết:* Với 5 vị trí có doanh thu $[1, 2, 3, 4, 5]$ và giới hạn $K = 2$ (không được chọn quá 2 vị trí liên tiếp):
Phương án tối ưu là bỏ chọn vị trí thứ 3 (doanh thu 3), giữ lại các vị trí 1, 2, 4, 5. Các cụm chọn gồm [1, 2] (độ dài 2) và [4, 5] (độ dài 2), mang lại tổng doanh thu tối đa là $1 + 2 + 4 + 5 = 12$.

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
if (n <= 0) return 0;

vector<long long> a(n + 1);
long long total_sum = 0;
for (int i = 1; i <= n; ++i) {
cin >> a[i];
total_sum += a[i];
}

// dp[i]: tổng nhỏ nhất các phần tử bị loại bỏ kết thúc tại i sao cho không có k+1 phần tử liền kề nào được chọn
vector<long long> dp(n + 1, 0);
deque<int> dq;
dq.push_back(0);

for (int i = 1; i <= n; ++i) {
while (!dq.empty() && dq.front() < i - k - 1) dq.pop_front();
dp[i] = dp[dq.front()] + a[i];
while (!dq.empty() && dp[dq.back()] >= dp[i]) dq.pop_back();
dq.push_back(i);
}

long long min_dropped = LLONG_MAX;
for (int i = n - k; i <= n; ++i) {
if (i >= 0) min_dropped = min(min_dropped, dp[i]);
}

cout << total_sum - min_dropped << "\n";
return 0;
}
```
