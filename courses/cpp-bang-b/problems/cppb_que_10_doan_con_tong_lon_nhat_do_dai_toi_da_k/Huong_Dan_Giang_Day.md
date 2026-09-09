# Hướng Dẫn Giảng Dạy: Đoạn Con Tổng Lớn Nhất Độ Dài Tối Đa K

Chuyên đề: **Cấu Trúc Dữ Liệu Hàng Đợi (Queue, Deque) & Monotonic Deque**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho mảng $A$ gồm $N$ số nguyên và số nguyên $K$. Hãy lập trình tìm tổng lớn nhất của một đoạn con liên tiếp có độ dài tối đa là $K$.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Nguyên lý Hàng đợi chuẩn (Queue):** Vào trước Ra trước (FIFO), là cấu trúc nền tảng phục vụ duyệt đồ thị theo chiều rộng (BFS).
- **Hàng đợi hai đầu (Deque) & Monotonic Deque:**
* Hỗ trợ thêm/xoá ở cả hai đầu trong $\mathcal{O}(1)$.
* Khi trượt cửa sổ kích thước $K$, lưu chỉ số phần tử trong deque sao cho giá trị tương ứng luôn đơn điệu.
* Loại bỏ phần tử trượt ra khỏi cửa sổ ở đầu trước (`pop_front()`) và loại bỏ phần tử kém tối ưu ở đầu sau (`pop_back()`).
- **Độ phức tạp:** Thời gian $\mathcal{O}(N)$, không gian phụ trợ $\mathcal{O}(K)$.

---

## 2. Bảng chạy tay trên số liệu mẫuMẫu thử (Sample 1): Đầu vào: `5 3 -1 2 4 -3 5` $\implies$ Đầu ra kỳ vọng: `6`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `5 3 -1 2 4 -3 5` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với mảng $[-1, 2, 3, -2, 4]$ và độ dài tối đa $K = 2$: Đoạn con liên tiếp có độ dài không quá 2 có tổng lớn nhất là đoạn $[2, 3]$ (độ d... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `6` |

*Giải thích chi tiết:* Với mảng $[-1, 2, 3, -2, 4]$ và độ dài tối đa $K = 2$:
Đoạn con liên tiếp có độ dài không quá 2 có tổng lớn nhất là đoạn $[2, 3]$ (độ dài 2) cho tổng là $2 + 3 = 5$ (hoặc đoạn [4] có tổng 4).

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
if (n <= 0 || k <= 0) return 0;

vector<long long> a(n + 1);
vector<long long> pref(n + 1, 0);
for (int i = 1; i <= n; ++i) {
cin >> a[i];
pref[i] = pref[i - 1] + a[i];
}

deque<int> dq;
dq.push_back(0);
long long max_sum = LLONG_MIN;

for (int i = 1; i <= n; ++i) {
while (!dq.empty() && dq.front() < i - k) dq.pop_front();
if (!dq.empty()) {
max_sum = max(max_sum, pref[i] - pref[dq.front()]);
}
while (!dq.empty() && pref[dq.back()] >= pref[i]) dq.pop_back();
dq.push_back(i);
}

cout << max_sum << "\n";
return 0;
}
```
