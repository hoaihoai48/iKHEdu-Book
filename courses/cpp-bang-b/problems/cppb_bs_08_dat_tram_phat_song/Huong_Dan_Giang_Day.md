# Hướng Dẫn Giảng Dạy: Đặt Trạm Phát Sóng Cách Nhau Xa Nhất (Aggressive Cows)
Chuyên đề: **Bài 05: Thuật toán tìm kiếm nhị phân**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho N vị trí khả dụng và số trạm cần đặt C. Hãy tìm khoảng cách nhỏ nhất lớn nhất giữa hai trạm bất kỳ.

- **Phương pháp tiếp cận — Tìm kiếm nhị phân:**
- Nhận diện tính đơn điệu của hàm mục tiêu hoặc không gian tìm kiếm.
- Thu hẹp không gian nghiệm $[L, R]$ qua điểm giữa $mid = L + (R - L) / 2$. Độ phức tạp thời gian đạt $\mathcal{O}(\log N)$ hoặc $\mathcal{O}(N \log(\text{range}))$.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `5 3 1 2 8 4 9` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Sắp xếp tọa độ các vị trí: [1, 2, 4, 8, 9]. Để đặt 3 trạm với khoảng cách tối thiểu giữa hai trạm kề nhau là 3: ta đặt t... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `3` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Sắp xếp tọa độ các vị trí: [1, 2, 4, 8, 9]. Để đặt 3 trạm với khoảng cách tối thiểu giữa hai trạm kề nhau là 3: ta đặt tại các tọa độ 1, 4 và 8 (hoặc 9). Khoảng cách giữa 1 và 4 là 3; giữa 4 và 8 là 4 (đều >= 3). Không thể đặt với khoảng cách tối thiểu >= 4. Vì vậy kết quả là 3.

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

bool check(long long d, const vector<long long>& x, int c) {
int count = 1;
long long last_pos = x[0];
for (size_t i = 1; i < x.size(); ++i) {
if (x[i] - last_pos >= d) {
count++;
last_pos = x[i];
}
}
return count >= c;
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

int n, c;
if (!(cin >> n >> c)) return 0;

vector<long long> x(n);
for (int i = 0; i < n; ++i) {
cin >> x[i];
}
sort(x.begin(), x.end());

long long low = 1, high = x[n - 1] - x[0], ans = 1;
while (low <= high) {
long long mid = low + (high - low) / 2;
if (check(mid, x, c)) {
ans = mid;
low = mid + 1;
} else {
high = mid - 1;
}
}

cout << ans << "\n";
return 0;
}
```
