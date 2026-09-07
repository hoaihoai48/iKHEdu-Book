# Hướng Dẫn Giảng Dạy: Tìm Đoạn Con Có Trung Bình Lớn Nhất Độ Dài >= K
Chuyên đề: **Bài 05: Thuật toán tìm kiếm nhị phân**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho dãy số nguyên gồm N phần tử và số nguyên K. Hãy tìm giá trị trung bình lớn nhất của một đoạn con có độ dài ít nhất K, làm tròn đến đúng 3 chữ số thập phân.

- **Phương pháp tiếp cận — Tìm kiếm nhị phân (Binary Search):**
  - Nhận diện tính đơn điệu của hàm mục tiêu hoặc không gian tìm kiếm.
  - Thu hẹp không gian nghiệm $[L, R]$ qua điểm giữa $mid = L + (R - L) / 2$. Độ phức tạp thời gian đạt $\mathcal{O}(\log N)$ hoặc $\mathcal{O}(N \log(\text{range}))$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 4 2 1 12 -5 -6)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `4 2 1 12 -5 -6` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Đoạn con [1, 12] có độ dài 2 >= K = 2 có tổng 13 và trung bình là 13/2 = 6.500. Đây là giá trị trung bình lớn nhất của c... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `6.500` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Đoạn con [1, 12] có độ dài 2 >= K = 2 có tổng 13 và trung bình là 13/2 = 6.500. Đây là giá trị trung bình lớn nhất của các đoạn con có độ dài >= 2.

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

bool check(double mid, const vector<double>& a, int n, int k) {
    vector<double> p(n + 1, 0.0);
    for (int i = 1; i <= n; ++i) {
        p[i] = p[i - 1] + (a[i - 1] - mid);
    }

    double min_p = 0.0;
    for (int i = k; i <= n; ++i) {
        min_p = min(min_p, p[i - k]);
        if (p[i] - min_p >= -1e-9) {
            return true;
        }
    }
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<double> a(n);
    double max_val = 0.0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        max_val = max(max_val, a[i]);
    }

    double low = 0.0, high = max_val;
    for (int iter = 0; iter < 80; ++iter) {
        double mid = low + (high - low) / 2.0;
        if (check(mid, a, n, k)) {
            low = mid;
        } else {
            high = mid;
        }
    }

    cout << fixed << setprecision(4) << low << "\n";
    return 0;
}
```
