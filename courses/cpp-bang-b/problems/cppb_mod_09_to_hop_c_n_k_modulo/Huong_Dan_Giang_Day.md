# Hướng Dẫn Giảng Dạy: Tính Số Tổ Hợp C(N, K) mod M
Chuyên đề: **Đồng Dư Thức & Lũy Thừa Nhị Phân (Modular Arithmetic)**

**Phân loại chuyên đề:** `Core Foundation` (Kiến thức nền tảng bắt buộc)

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Nắm vững và làm chủ kỹ thuật giải quyết bài toán: Tính Số Tổ Hợp C(N, K) mod M.
* **Tư duy thuật toán:** Rèn luyện phản xạ phân tích tính chất đồng dư, áp dụng lũy thừa nhị phân $\mathcal{O}(\log N)$, nghịch đảo modulo và tránh tràn số.
* **Chuẩn code thi đấu:** Cài đặt code C++ chuẩn thi đấu (Fast I/O, Safe Input, không tiền tố thừa, quản lý số dư âm chặt chẽ).

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
* **Dữ liệu đầu vào:** - Dòng 1: Số nguyên dương $Q$ ($1 \le Q \le 10^5$).
- $Q$ dòng tiếp theo: Mỗi dòng chứa 2 số $N, K$ ($0 \le K \le N \le 10^6$).
* **Yêu cầu cốt lõi:** Cho $Q$ truy vấn, mỗi truy vấn chứa 2 số $N, K$. Hãy tính $C(N, K) \pmod{10^9 + 7}$.
* **Trường hợp biên (Edge Cases):**
  * Giá trị $A, B = 0$ hoặc $B = 1$.
  * Số dư âm trong phép trừ.
  * Phép nhân tràn số 32-bit (bắt buộc dùng `long long` hoặc ép kiểu).

---

## 3. Câu Hỏi Dẫn Dắt Tư Duy (Socratic Method)
1. Bài toán có thể chia để trị số mũ $B$ thành $\lfloor B / 2 \rfloor$ không?
2. Có xuất hiện phép chia trên vành Modulo không? Nếu có, modulo $M$ có phải số nguyên tố không?
3. Trong phép trừ, ta cần làm gì để số dư không bao giờ bị âm trong C++?

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)
### 4.1. Chiến lược thực thi:
- Triển khai Lũy thừa nhị phân lặp hoặc tiền xử lý mảng giai thừa / nghịch đảo.
- Áp dụng các định lý số học (Fermat nhỏ, Euclid mở rộng).

### 4.2. Bất biến toán học (Invariant):
> Mọi phép toán biến đổi đều bảo toàn tính chất đồng dư trên vành $\mathbb{Z}_M$.

---

## 5. Mô Phỏng Từng Bước Trên Sample (Dry Run)
### Dữ liệu Sample:
* **Input:**
```text
3
5 2
6 3
10 0
```
* **Output:**
```text
10
20
1
```
* **Phân tích quá trình thực thi:**
  C(5, 2) = 10, C(6, 3) = 20, C(10, 0) = 1.

---

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian
- **Thời gian (Time Complexity):** Thuật toán chạy trong $\mathcal{O}(\log B)$ hoặc $\mathcal{O}(1)$ mỗi truy vấn sau tiền xử lý.
- **Không gian (Space Complexity):** $\mathcal{O}(1)$ hoặc $\mathcal{O}(N)$ bộ nhớ phụ trợ.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)
1. Tràn số khi nhân hai số $\approx 10^9$ (bắt buộc dùng `(1LL * a * b) % M`).
2. Quên cộng $M$ trong phép trừ: `(a - b + M) % M`.
3. Chia trực tiếp `(A / B) % M` gây sai bản chất toán học.

---

## 8. Mã Nguồn Tham Chiếu C++ Chuẩn Thi Đấu
```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1000000;
const long long MOD = 1000000007;

vector<long long> fact(MAXN + 1);
vector<long long> invFact(MAXN + 1);

long long powerMod(long long a, long long b) {
    long long ans = 1;
    a %= MOD;
    while (b > 0) {
        if (b & 1) ans = (ans * a) % MOD;
        a = (a * a) % MOD;
        b >>= 1;
    }
    return ans;
}

void precompute() {
    fact[0] = 1;
    for (int i = 1; i <= MAXN; ++i) fact[i] = (fact[i - 1] * i) % MOD;
    invFact[MAXN] = powerMod(fact[MAXN], MOD - 2);
    for (int i = MAXN; i >= 1; --i) invFact[i - 1] = (invFact[i] * i) % MOD;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    precompute();

    int q;
    if (!(cin >> q)) return 0;

    while (q--) {
        int n, k;
        cin >> n >> k;
        if (k < 0 || k > n) cout << 0 << "
";
        else cout << fact[n] * invFact[k] % MOD * invFact[n - k] % MOD << "
";
    }
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* **Mở rộng 1:** Áp dụng vào các bài toán quy hoạch động đếm đường đi, đếm dãy ngoặc đúng (Catalan).
* **Mở rộng 2:** Tích hợp Lũy thừa nhị phân vào phép nhân ma trận trên đồ thị.
