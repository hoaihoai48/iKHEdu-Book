# Hướng Dẫn Giảng Dạy: Chia Mảng Thành K Đoạn Có Tổng Max Nhỏ Nhất
Chuyên đề: **Bài 05: Thuật toán tìm kiếm nhị phân**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho mảng N số nguyên dương và số nguyên K. Hãy chia mảng thành K đoạn con liên tiếp sao cho tổng lớn nhất trong các đoạn là nhỏ nhất có thể.

- **Phương pháp tiếp cận — Tìm kiếm nhị phân:**
- Nhận diện tính đơn điệu của hàm mục tiêu hoặc không gian tìm kiếm.
- Thu hẹp không gian nghiệm $[L, R]$ qua điểm giữa $mid = L + (R - L) / 2$. Độ phức tạp thời gian đạt $\mathcal{O}(\log N)$ hoặc $\mathcal{O}(N \log(\text{range}))$.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `5 2 7 2 5 10 8` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Chia thành 2 đoạn con: đoạn 1 là [7, 2, 5] có tổng 14; đoạn 2 là [10, 8] có tổng 18. Tổng lớn nhất giữa hai đoạn là 18. ... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `18` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Chia thành 2 đoạn con: đoạn 1 là [7, 2, 5] có tổng 14; đoạn 2 là [10, 8] có tổng 18. Tổng lớn nhất giữa hai đoạn là 18. Không thể chia cách nào khác để có tổng cực đại nhỏ hơn 18. Vì vậy kết quả là 18.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- **Bẫy 1 — Tràn số nguyên:** Khi tính toán tổng, tích hoặc lũy thừa lớn hơn $2 \cdot 10^9$, bắt buộc phải sử dụng kiểu dữ liệu `long long` (64-bit) để tránh tràn số âm.
- **Bẫy 2 — Chỉ số mảng & Giới hạn biên:** Chú ý giữa đánh chỉ số 0-based (`0 .. N-1`) và 1-based (`1 .. N`). Kiểm tra kỹ trường hợp $N = 1$ hoặc giá trị biên tối đa của đề bài.
- **Bẫy 3 — Tối ưu thời gian I/O:** Luôn sử dụng `ios::sync_with_stdio(false); cin.tie(nullptr);` ở đầu hàm `main()` để đọc ghi nhanh, tránh bị TLE khi số lượng testcase lớn.

---

## 4. Lời giải tham khảo
```cpp
#include <bits/stdc++.h>
using namespace std;

bool check(long long limit, const vector<long long>& a, int k) {
int segments = 1;
long long current_sum = 0;
for (long long x : a) {
if (current_sum + x > limit) {
segments++;
current_sum = x;
} else {
current_sum += x;
}
}
return segments <= k;
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

int n, k;
if (!(cin >> n >> k)) return 0;

vector<long long> a(n);
long long max_val = 0, total_sum = 0;
for (int i = 0; i < n; ++i) {
cin >> a[i];
max_val = max(max_val, a[i]);
total_sum += a[i];
}

long long low = max_val, high = total_sum, ans = total_sum;
while (low <= high) {
long long mid = low + (high - low) / 2;
if (check(mid, a, k)) {
ans = mid;
high = mid - 1;
} else {
low = mid + 1;
}
}

cout << ans << "\n";
return 0;
}
```
