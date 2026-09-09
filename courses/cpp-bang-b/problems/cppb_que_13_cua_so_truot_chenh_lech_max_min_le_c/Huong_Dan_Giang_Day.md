# Hướng Dẫn Giảng Dạy: Đoạn Con Dài Nhất Có Độ Chênh Lệch Max-Min <= C

Chuyên đề: **Cấu Trúc Dữ Liệu Hàng Đợi (Queue, Deque) & Monotonic Deque**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho mảng $A$ gồm $N$ số nguyên và ngưỡng chênh lệch $C$. Hãy lập trình tìm độ dài lớn nhất của một đoạn con liên tiếp có $\max - \min \le C$.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Nguyên lý Hàng đợi chuẩn (Queue):** Vào trước Ra trước (FIFO), là cấu trúc nền tảng phục vụ duyệt đồ thị theo chiều rộng (BFS).
- **Hàng đợi hai đầu (Deque) & Monotonic Deque:**
* Hỗ trợ thêm/xoá ở cả hai đầu trong $\mathcal{O}(1)$.
* Khi trượt cửa sổ kích thước $K$, lưu chỉ số phần tử trong deque sao cho giá trị tương ứng luôn đơn điệu.
* Loại bỏ phần tử trượt ra khỏi cửa sổ ở đầu trước (`pop_front()`) và loại bỏ phần tử kém tối ưu ở đầu sau (`pop_back()`).
- **Độ phức tạp:** Thời gian $\mathcal{O}(N)$, không gian phụ trợ $\mathcal{O}(K)$.

---

## 2. Bảng chạy tay trên số liệu mẫuMẫu thử (Sample 1): Đầu vào: `6 2 4 2 2 2 4 4` $\implies$ Đầu ra kỳ vọng: `6`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `6 2 4 2 2 2 4 4` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với mảng $[8, 2, 4, 7]$ và ngưỡng $C = 4$: Đoạn con $[2, 4]$ có $\max = 4, \min = 2$, độ chênh lệch là $4 - 2 = 2 \le 4$ có độ dài 2. Đ... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `6` |

*Giải thích chi tiết:* Với mảng $[8, 2, 4, 7]$ và ngưỡng $C = 4$:
Đoạn con $[2, 4]$ có $\max = 4, \min = 2$, độ chênh lệch là $4 - 2 = 2 \le 4$ có độ dài 2.
Đoạn con $[4, 7]$ có $\max = 7, \min = 4$, độ chênh lệch là $7 - 4 = 3 \le 4$ có độ dài 2.
Độ dài lớn nhất đạt được là 2.

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

int n;
long long c;
if (!(cin >> n >> c)) return 0;
if (n <= 0) return 0;

vector<long long> a(n);
for (int i = 0; i < n; ++i) cin >> a[i];

deque<int> min_dq, max_dq;
int left = 0;
int max_len = 0;

for (int right = 0; right < n; ++right) {
while (!min_dq.empty() && a[min_dq.back()] >= a[right]) min_dq.pop_back();
min_dq.push_back(right);

while (!max_dq.empty() && a[max_dq.back()] <= a[right]) max_dq.pop_back();
max_dq.push_back(right);

while (a[max_dq.front()] - a[min_dq.front()] > c) {
left++;
if (min_dq.front() < left) min_dq.pop_front();
if (max_dq.front() < left) max_dq.pop_front();
}

max_len = max(max_len, right - left + 1);
}

cout << max_len << "\n";
return 0;
}
```
