# Hướng Dẫn Giảng Dạy: Sàng Ước Nguyên Tố Nhỏ Nhất (SPF)
Chuyên đề: **Bài 07: Lý thuyết số & số nguyên tố**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho Q truy vấn, mỗi truy vấn chứa một số nguyên N (2 <= N <= 10^6). Hãy in ra ước số nguyên tố nhỏ nhất của N.

- **Phương pháp tiếp cận — Lý thuyết số & Số nguyên tố:**
  - Tận dụng sàng nguyên tố Eratosthenes cho các truy vấn tiền xử lý $\mathcal{O}(N \log \log N)$ hoặc kiểm tra căn bậc hai $\mathcal{O}(\sqrt{N})$.
  - Phân tích thừa số nguyên tố và tính chất ước số để tối ưu hóa bài toán.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 3 15 7 20)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `3 15 7 20` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | - SPF(15) = 3 (vì 15 chia hết cho số nguyên tố nhỏ nhất là 3). - SPF(7) = 7 (vì 7 là số nguyên tố). - SPF(20) = 2 (vì 20... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `3 7 2` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* - SPF(15) = 3 (vì 15 chia hết cho số nguyên tố nhỏ nhất là 3).
- SPF(7) = 7 (vì 7 là số nguyên tố).
- SPF(20) = 2 (vì 20 chia hết cho 2).

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

const int MAXN = 1000000;
vector<int> spf(MAXN + 1);

void sieveSPF() {
    for (int i = 1; i <= MAXN; ++i) spf[i] = i;
    for (int i = 2; 1LL * i * i <= MAXN; ++i) {
        if (spf[i] == i) {
            for (int j = i * i; j <= MAXN; j += i) {
                if (spf[j] == j) spf[j] = i;
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    sieveSPF();

    int q;
    if (!(cin >> q)) return 0;

    for (int i = 0; i < q; ++i) {
        int n;
        cin >> n;
        cout << spf[n] << (i + 1 == q ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```
