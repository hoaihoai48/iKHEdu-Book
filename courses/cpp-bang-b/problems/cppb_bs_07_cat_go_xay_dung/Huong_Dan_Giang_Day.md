# Hướng Dẫn Giảng Dạy: Cắt Gỗ Xây Dựng (Woodcutting / EKO)
Chuyên đề: **Bài 05: Thuật toán tìm kiếm nhị phân**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho chiều cao N cây gỗ và lượng gỗ tối thiểu cần lấy M. Hãy tìm độ cao cắt H lớn nhất của máy cưa.

- **Phương pháp tiếp cận — Tìm kiếm nhị phân:**
- Nhận diện tính đơn điệu của hàm mục tiêu hoặc không gian tìm kiếm.
- Thu hẹp không gian nghiệm $[L, R]$ qua điểm giữa $mid = L + (R - L) / 2$. Độ phức tạp thời gian đạt $\mathcal{O}(\log N)$ hoặc $\mathcal{O}(N \log(\text{range}))$.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `4 7 20 15 10 17` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Khi đặt độ cao cắt H = 15: - Cây 20m cắt được: 20 - 15 = 5m. - Cây 15m cắt được: 15 - 15 = 0m. - Cây 10m không bị cắt: 0... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `15` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Khi đặt độ cao cắt H = 15:

- Cây 20m cắt được: 20 - 15 = 5m.
- Cây 15m cắt được: 15 - 15 = 0m.
- Cây 10m không bị cắt: 0m.
- Cây 17m cắt được: 17 - 15 = 2m.
Tổng gỗ thu được là 5 + 0 + 0 + 2 = 7 mét đúng bằng M. Đây là độ cao H lớn nhất.

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

bool check(long long h, const vector<long long>& a, long long m) {
long long wood = 0;
for (long long x : a) {
if (x > h) {
wood += (x - h);
}
}
return wood >= m;
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

int n;
long long m;
if (!(cin >> n >> m)) return 0;

vector<long long> a(n);
long long max_val = 0;
for (int i = 0; i < n; ++i) {
cin >> a[i];
max_val = max(max_val, a[i]);
}

long long low = 0, high = max_val, ans = 0;
while (low <= high) {
long long mid = low + (high - low) / 2;
if (check(mid, a, m)) {
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
