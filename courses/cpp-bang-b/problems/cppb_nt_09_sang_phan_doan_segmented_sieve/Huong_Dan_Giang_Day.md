# Hướng Dẫn Giảng Dạy: Sàng Phân Đoạn (Segmented Sieve)
Chuyên đề: **Bài 07: Lý thuyết số & số nguyên tố**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho hai số nguyên L, R (1 <= L <= R <= 10^12, R - L <= 10^6). Hãy đếm số lượng số nguyên tố trong đoạn [L, R].

- **Phương pháp tiếp cận — Lý thuyết số & Số nguyên tố:**
  - Tận dụng sàng nguyên tố Eratosthenes cho các truy vấn tiền xử lý $\mathcal{O}(N \log \log N)$ hoặc kiểm tra căn bậc hai $\mathcal{O}(\sqrt{N})$.
  - Phân tích thừa số nguyên tố và tính chất ước số để tối ưu hóa bài toán.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 10 20)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `10 20` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Các số nguyên tố trong đoạn [10, 20] gồm {11, 13, 17, 19}, tổng cộng có 4 số.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `4` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Các số nguyên tố trong đoạn [10, 20] gồm {11, 13, 17, 19}, tổng cộng có 4 số.

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

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long l, r;
    if (!(cin >> l >> r)) return 0;

    int lim = sqrt(r);
    vector<bool> is_prime(lim + 1, true);
    vector<int> primes;
    for (int i = 2; i <= lim; ++i) {
        if (is_prime[i]) {
            primes.push_back(i);
            for (int j = i * 2; j <= lim; j += i) is_prime[j] = false;
        }
    }

    vector<bool> is_prime_range(r - l + 1, true);
    for (int p : primes) {
        long long start = max(1LL * p * p, ((l + p - 1) / p) * p);
        for (long long j = start; j <= r; j += p) {
            is_prime_range[j - l] = false;
        }
    }

    if (l == 1) is_prime_range[0] = false;

    int count_primes = 0;
    for (int i = 0; i <= r - l; ++i) {
        if (is_prime_range[i]) count_primes++;
    }

    cout << count_primes << "\n";
    return 0;
}
```
