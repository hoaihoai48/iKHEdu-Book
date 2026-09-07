# Hướng Dẫn Giảng Dạy: Kiểm Tra Số Hoàn Hảo
Chuyên đề: **Bài 07: Lý thuyết số & số nguyên tố**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho số nguyên dương N. Hãy kiểm tra xem N có phải là số hoàn hảo hay không. In YES nếu đúng, ngược lại in NO.

- **Phương pháp tiếp cận — Lý thuyết số & Số nguyên tố:**
  - Tận dụng sàng nguyên tố Eratosthenes cho các truy vấn tiền xử lý $\mathcal{O}(N \log \log N)$ hoặc kiểm tra căn bậc hai $\mathcal{O}(\sqrt{N})$.
  - Phân tích thừa số nguyên tố và tính chất ước số để tối ưu hóa bài toán.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 28)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `28` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Các ước số thực sự của 28 là {1, 2, 4, 7, 14}. Tổng của chúng là 1 + 2 + 4 + 7 + 14 = 28. Vì vậy 28 là số hoàn hảo -> in... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `YES` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Các ước số thực sự của 28 là {1, 2, 4, 7, 14}. Tổng của chúng là 1 + 2 + 4 + 7 + 14 = 28. Vì vậy 28 là số hoàn hảo -> in YES.

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

bool isPrime(long long p) {
    if (p < 2) return false;
    for (long long i = 2; i * i <= p; ++i) {
        if (p % i == 0) return false;
    }
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    unsigned long long n;
    if (!(cin >> n)) return 0;

    // Theo Euclid-Euler, số hoàn hảo chẵn có dạng 2^(p-1) * (2^p - 1) với 2^p - 1 là số nguyên tố
    vector<unsigned long long> perfect_nums;
    int primes[] = {2, 3, 5, 7, 13, 17, 19, 31};
    for (int p : primes) {
        unsigned long long mersenne = (1ULL << p) - 1;
        if (isPrime(mersenne)) {
            unsigned long long perf = (1ULL << (p - 1)) * mersenne;
            perfect_nums.push_back(perf);
        }
    }

    for (auto v : perfect_nums) {
        if (v == n) {
            cout << "YES\n";
            return 0;
        }
    }
    cout << "NO\n";
    return 0;
}
```
