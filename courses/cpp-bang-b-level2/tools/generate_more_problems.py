#!/usr/bin/env python3
import os
import glob
from pathlib import Path

BASE = Path("/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b-level2")
PROB_DIR = BASE / "problems"
PROB_DIR.mkdir(parents=True, exist_ok=True)

# Danh sách các bài tập bổ sung cho 15 bài học (từ bài 17 trở đi)
NEW_PROBLEMS = {
    # Lesson 01: Số học nâng cao (thêm 6 bài: 17 -> 22)
    "cppb2_l01": [
        ("cppb2_l01_17_dinh_ly_thang_du_trung_hoa_crt", "Định lý thặng dư Trung Hoa (CRT)",
         "Cho hệ đồng dư $x \\equiv r_i \\pmod{m_i}$ với $m_i$ đôi một nguyên tố cùng nhau. Tìm $x$ nhỏ nhất.",
         "Dòng đầu chứa số $K$. $K$ dòng sau, mỗi dòng chứa hai số $r_i, m_i$.",
         "In ra số nguyên dương $x$ nhỏ nhất thỏa mãn hệ phương trình đồng dư.",
         "2\n2 3\n3 5\n", "8\n",
         """#include <bits/stdc++.h>
using namespace std;

long long extgcd(long long a, long long b, long long &x, long long &y) {
    if (b == 0) { x = 1; y = 0; return a; }
    long long x1, y1;
    long long d = extgcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - y1 * (a / b);
    return d;
}

long long modInverse(long long a, long long m) {
    long long x, y;
    extgcd(a, m, x, y);
    return (x % m + m) % m;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    if (!(cin >> k)) return 0;
    vector<long long> r(k), m(k);
    long long M = 1;
    for (int i = 0; i < k; ++i) {
        cin >> r[i] >> m[i];
        M *= m[i];
    }

    long long ans = 0;
    for (int i = 0; i < k; ++i) {
        long long Mi = M / m[i];
        long long yi = modInverse(Mi, m[i]);
        ans = (ans + (__int128)r[i] * Mi % M * yi % M) % M;
    }
    cout << (ans % M + M) % M << "\\n";
    return 0;
}
"""),
        ("cppb2_l01_18_bac_cua_so_nguyen_order", "Bậc của số nguyên Modulo P",
         "Cho hai số nguyên dương $A$ và $P$ với $\\gcd(A, P) = 1$. Tìm số nguyên dương $k$ nhỏ nhất sao cho $A^k \\equiv 1 \\pmod P$.",
         "Gồm 2 số nguyên $A$ và $P$ ($P$ là số nguyên tố $\\le 10^9$).",
         "In ra bậc $k = \\text{ord}_P(A)$.",
         "2 7\n", "3\n",
         """#include <bits/stdc++.h>
using namespace std;

long long power(long long a, long long b, long long m) {
    long long res = 1;
    a %= m;
    while (b > 0) {
        if (b & 1) res = (__int128)res * a % m;
        a = (__int128)a * a % m;
        b >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, p;
    if (!(cin >> a >> p)) return 0;

    long long phi = p - 1;
    vector<long long> divs;
    for (long long i = 1; i * i <= phi; ++i) {
        if (phi % i == 0) {
            divs.push_back(i);
            if (i * i != phi) divs.push_back(phi / i);
        }
    }
    sort(divs.begin(), divs.end());

    for (long long d : divs) {
        if (power(a, d, p) == 1) {
            cout << d << "\\n";
            return 0;
        }
    }
    cout << phi << "\\n";
    return 0;
}
"""),
        ("cppb2_l01_19_can_nguyen_nguyen_thuy_primitive_root", "Tìm căn nguyên nguyên thủy nhỏ nhất",
         "Cho số nguyên tố lẻ $P$. Tìm căn nguyên nguyên thủy nhỏ nhất modulo $P$.",
         "Một số nguyên tố $P$ ($3 \\le P \\le 10^9$).",
         "In ra căn nguyên nguyên thủy nhỏ nhất của $P$.",
         "7\n", "3\n",
         """#include <bits/stdc++.h>
using namespace std;

long long power(long long a, long long b, long long m) {
    long long res = 1;
    a %= m;
    while (b > 0) {
        if (b & 1) res = (__int128)res * a % m;
        a = (__int128)a * a % m;
        b >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long p;
    if (!(cin >> p)) return 0;

    long long phi = p - 1;
    vector<long long> factors;
    long long temp = phi;
    for (long long i = 2; i * i <= temp; ++i) {
        if (temp % i == 0) {
            factors.push_back(i);
            while (temp % i == 0) temp /= i;
        }
    }
    if (temp > 1) factors.push_back(temp);

    for (long long g = 2; g < p; ++g) {
        bool ok = true;
        for (long long f : factors) {
            if (power(g, phi / f, p) == 1) {
                ok = false;
                break;
            }
        }
        if (ok) {
            cout << g << "\\n";
            return 0;
        }
    }
    return 0;
}
"""),
        ("cppb2_l01_20_tinh_uoc_nguyen_to_lon_nhat", "Ước nguyên tố lớn nhất của dãy số",
         "Cho mảng $A$ gồm $N$ phần tử. Tìm ước số nguyên tố lớn nhất trong tất cả các phần tử của mảng.",
         "Dòng đầu chứa số $N$. Dòng sau chứa $N$ số nguyên $A_i$ ($A_i \\le 10^{12}$).",
         "In ra ước nguyên tố lớn nhất tìm được.",
         "3\n12 35 22\n", "11\n",
         """#include <bits/stdc++.h>
using namespace std;

long long get_max_prime_factor(long long n) {
    long long max_p = -1;
    while (n % 2 == 0) { max_p = 2; n /= 2; }
    for (long long i = 3; i * i <= n; i += 2) {
        while (n % i == 0) {
            max_p = i;
            n /= i;
        }
    }
    if (n > 1) max_p = max(max_p, n);
    return max_p;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    long long ans = -1;
    for (int i = 0; i < n; ++i) {
        long long x;
        cin >> x;
        ans = max(ans, get_max_prime_factor(x));
    }
    cout << ans << "\\n";
    return 0;
}
"""),
        ("cppb2_l01_21_phuong_trinh_pell_co_ban", "Phương trình nghiệm nguyên Pell cơ bản",
         "Tìm nghiệm nguyên dương nhỏ nhất $(x, y)$ của phương trình Pell: $x^2 - d \\cdot y^2 = 1$ với $d$ không chính phương.",
         "Một số nguyên dương $d$ không phải là số chính phương ($d \\le 1000$).",
         "In ra cặp nghiệm $(x, y)$ nguyên dương nhỏ nhất.",
         "2\n", "3 2\n",
         """#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long d;
    if (!(cin >> d)) return 0;

    long long m = 0, d_val = 1, a0 = sqrt(d), a = a0;
    if (a0 * a0 == d) return 0;

    __int128 p0 = a0, p1 = 1, q0 = 1, q1 = 0;
    __int128 p = p0, q = q0;

    while (p * p - (__int128)d * q * q != 1) {
        m = d_val * a - m;
        d_val = (d - m * m) / d_val;
        a = (a0 + m) / d_val;
        p = a * p0 + p1;
        q = a * q0 + q1;
        p1 = p0; p0 = p;
        q1 = q0; q0 = q;
    }

    cout << (long long)p << " " << (long long)q << "\\n";
    return 0;
}
"""),
        ("cppb2_l01_22_phan_tich_legendre_nang_cao", "Bội số nguyên tố trong tích giai thừa lớn",
         "Tính số mũ cao nhất của số nguyên tố $P$ trong tích $N! \\times M!$.",
         "Ba số nguyên dương $N, M, P$ ($P$ là số nguyên tố, $N, M \\le 10^{18}$).",
         "In ra số mũ của $P$ trong biểu thức $N! \\times M!$.",
         "5 3 2\n", "4\n",
         """#include <bits/stdc++.h>
using namespace std;

long long legendre(long long n, long long p) {
    long long cnt = 0;
    while (n > 0) {
        cnt += n / p;
        n /= p;
    }
    return cnt;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, m, p;
    if (!(cin >> n >> m >> p)) return 0;
    cout << legendre(n, p) + legendre(m, p) << "\\n";
    return 0;
}
"""),
    ],

    # Lesson 02: Modulo & Lũy Thừa Nhanh (thêm 6 bài: 17 -> 22)
    "cppb2_l02": [
        ("cppb2_l02_17_luy_thua_ma_tran_dem_duong_di", "Lũy thừa ma trận đếm đường đi đồ thị",
         "Cho đồ thị vô hướng $N$ đỉnh. Đếm số đường đi có độ dài đúng $K$ giữa đỉnh $U$ và đỉnh $V$ modulo $10^9+7$.",
         "Dòng đầu chứa $N, M, K, U, V$. $M$ dòng sau mô tả các cạnh của đồ thị.",
         "In ra số đường đi modulo $10^9+7$.",
         "3 3 2 1 3\n1 2\n2 3\n1 3\n", "1\n",
         """#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1e9 + 7;
typedef vector<vector<long long>> Matrix;

Matrix multiply(const Matrix &A, const Matrix &B, int n) {
    Matrix C(n, vector<long long>(n, 0));
    for (int i = 0; i < n; ++i)
        for (int k = 0; k < n; ++k)
            for (int j = 0; j < n; ++j)
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD;
    return C;
}

Matrix matPow(Matrix A, long long k, int n) {
    Matrix res(n, vector<long long>(n, 0));
    for (int i = 0; i < n; ++i) res[i][i] = 1;
    while (k > 0) {
        if (k & 1) res = multiply(res, A, n);
        A = multiply(A, A, n);
        k >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, u, v;
    long long k;
    if (!(cin >> n >> m >> k >> u >> v)) return 0;
    --u; --v;
    Matrix adj(n, vector<long long>(n, 0));
    for (int i = 0; i < m; ++i) {
        int x, y;
        cin >> x >> y;
        --x; --y;
        adj[x][y] = (adj[x][y] + 1) % MOD;
        adj[y][x] = (adj[y][x] + 1) % MOD;
    }

    Matrix res = matPow(adj, k, n);
    cout << res[u][v] << "\\n";
    return 0;
}
"""),
        ("cppb2_l02_18_tinh_cap_so_nhan_modulo_hop_so", "Tổng cấp số nhân Modulo hợp số",
         "Tính tổng $S = 1 + A + A^2 + \\dots + A^N \\pmod M$ với $M$ là hợp số bất kỳ.",
         "Ba số nguyên $A, N, M$ ($A, M \\le 10^9, N \\le 10^{18}$).",
         "In ra giá trị của $S \\pmod M$.",
         "2 3 100\n", "15\n",
         """#include <bits/stdc++.h>
using namespace std;

typedef vector<vector<long long>> Matrix;

Matrix multiply(const Matrix &A, const Matrix &B, long long mod) {
    Matrix C(2, vector<long long>(2, 0));
    for (int i = 0; i < 2; ++i)
        for (int k = 0; k < 2; ++k)
            for (int j = 0; j < 2; ++j)
                C[i][j] = (C[i][j] + (__int128)A[i][k] * B[k][j]) % mod;
    return C;
}

Matrix matPow(Matrix A, long long k, long long mod) {
    Matrix res = {{1, 0}, {0, 1}};
    while (k > 0) {
        if (k & 1) res = multiply(res, A, mod);
        A = multiply(A, A, mod);
        k >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, n, m;
    if (!(cin >> a >> n >> m)) return 0;

    Matrix T = {{a % m, 1}, {0, 1}};
    Matrix Tn = matPow(T, n + 1, m);
    cout << (Tn[0][1] % m + m) % m << "\\n";
    return 0;
}
"""),
        ("cppb2_l02_19_luy_thua_tang_thap_power_tower", "Lũy thừa tháp tầng Euler Modulo",
         "Tính $A^{B^C} \\pmod M$ với $M$ là số nguyên tố.",
         "Bốn số nguyên $A, B, C, M$ ($M$ là số nguyên tố $10^9+7$).",
         "In ra kết quả của $A^{B^C} \\pmod M$.",
         "2 3 2 1000000007\n", "512\n",
         """#include <bits/stdc++.h>
using namespace std;

long long power(long long a, long long b, long long m) {
    long long res = 1;
    a %= m;
    while (b > 0) {
        if (b & 1) res = (__int128)res * a % m;
        a = (__int128)a * a % m;
        b >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, b, c, m;
    if (!(cin >> a >> b >> c >> m)) return 0;

    long long exp = power(b, c, m - 1);
    cout << power(a, exp, m) << "\\n";
    return 0;
}
"""),
        ("cppb2_l02_20_can_bac_hai_modulo_tonelli_shanks", "Căn bậc hai Modulo P (Tonelli-Shanks)",
         "Tìm số nguyên $X$ nhỏ nhất sao cho $X^2 \\equiv N \\pmod P$ với $P$ là số nguyên tố.",
         "Hai số nguyên $N$ và $P$ ($P \\le 10^9+7$).",
         "In ra nghiệm $X$ nhỏ nhất hoặc -1 nếu vô nghiệm.",
         "2 7\n", "3\n",
         """#include <bits/stdc++.h>
using namespace std;

long long power(long long a, long long b, long long m) {
    long long res = 1;
    a %= m;
    while (b > 0) {
        if (b & 1) res = (__int128)res * a % m;
        a = (__int128)a * a % m;
        b >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, p;
    if (!(cin >> n >> p)) return 0;
    n %= p;
    if (n == 0) { cout << 0 << "\\n"; return 0; }
    if (p == 2) { cout << n << "\\n"; return 0; }
    if (power(n, (p - 1) / 2, p) != 1) { cout << -1 << "\\n"; return 0; }

    long long q = p - 1, s = 0;
    while (q % 2 == 0) { q /= 2; s++; }

    long long z = 2;
    while (power(z, (p - 1) / 2, p) == 1) z++;

    long long c = power(z, q, p);
    long long r = power(n, (q + 1) / 2, p);
    long long t = power(n, q, p);
    long long m = s;

    while (t != 1) {
        long long temp = t;
        long long i = 0;
        for (i = 0; i < m; ++i) {
            if (temp == 1) break;
            temp = (__int128)temp * temp % p;
        }
        long long b = power(c, 1LL << (m - i - 1), p);
        r = (__int128)r * b % p;
        c = (__int128)b * b % p;
        t = (__int128)t * c % p;
        m = i;
    }
    long long ans = min(r, p - r);
    cout << ans << "\\n";
    return 0;
}
"""),
        ("cppb2_l02_21_ma_tran_fibonacci_tong_doan", "Tổng dãy Fibonacci từ L đến R",
         "Tính tổng $S(L, R) = F_L + F_{L+1} + \\dots + F_R \\pmod{10^9+7}$.",
         "Gồm 2 số nguyên $L, R$ ($1 \\le L \\le R \\le 10^{18}$).",
         "In ra tổng modulo $10^9+7$.",
         "1 3\n", "4\n",
         """#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1e9 + 7;
typedef vector<vector<long long>> Matrix;

Matrix multiply(const Matrix &A, const Matrix &B) {
    Matrix C = {{0, 0}, {0, 0}};
    for (int i = 0; i < 2; ++i)
        for (int k = 0; k < 2; ++k)
            for (int j = 0; j < 2; ++j)
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD;
    return C;
}

Matrix matPow(Matrix A, long long k) {
    Matrix res = {{1, 0}, {0, 1}};
    while (k > 0) {
        if (k & 1) res = multiply(res, A);
        A = multiply(A, A);
        k >>= 1;
    }
    return res;
}

long long getFib(long long n) {
    if (n <= 0) return 0;
    if (n == 1) return 1;
    Matrix T = {{1, 1}, {1, 0}};
    Matrix Tn = matPow(T, n - 1);
    return Tn[0][0];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long l, r;
    if (!(cin >> l >> r)) return 0;
    long long sumR = (getFib(r + 2) - 1 + MOD) % MOD;
    long long sumL = (getFib(l + 1) - 1 + MOD) % MOD;
    cout << (sumR - sumL + MOD) % MOD << "\\n";
    return 0;
}
"""),
        ("cppb2_l02_22_day_so_bac_ba_tribonacci", "Số Tribonacci thứ N bằng ma trận 3x3",
         "Dãy Tribonacci: $T_0=0, T_1=1, T_2=1$ và $T_n = T_{n-1} + T_{n-2} + T_{n-3}$. Tính $T_N \\pmod{10^9+7}$.",
         "Một số nguyên $N$ ($N \\le 10^{18}$).",
         "In ra $T_N \\pmod{10^9+7}$.",
         "4\n", "4\n",
         """#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1e9 + 7;
typedef vector<vector<long long>> Matrix;

Matrix multiply(const Matrix &A, const Matrix &B) {
    Matrix C(3, vector<long long>(3, 0));
    for (int i = 0; i < 3; ++i)
        for (int k = 0; k < 3; ++k)
            for (int j = 0; j < 3; ++j)
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD;
    return C;
}

Matrix matPow(Matrix A, long long k) {
    Matrix res(3, vector<long long>(3, 0));
    for (int i = 0; i < 3; ++i) res[i][i] = 1;
    while (k > 0) {
        if (k & 1) res = multiply(res, A);
        A = multiply(A, A);
        k >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    if (n == 0) { cout << 0 << "\\n"; return 0; }
    if (n == 1 || n == 2) { cout << 1 << "\\n"; return 0; }

    Matrix T = {
        {1, 1, 1},
        {1, 0, 0},
        {0, 1, 0}
    };
    Matrix Tn = matPow(T, n - 2);
    long long ans = (Tn[0][0] * 1 + Tn[0][1] * 1 + Tn[0][2] * 0) % MOD;
    cout << ans << "\\n";
    return 0;
}
"""),
    ],
}

def create_problem_package(code, title, desc, inp, out, s_in, s_out, sol):
    pdir = PROB_DIR / code
    pdir.mkdir(parents=True, exist_ok=True)
    
    de_bai_content = f"""# {title}
## Mã bài toán: {code.upper().replace('_', '-')}

## Bối cảnh & Nhiệm vụ
{desc}

## Đầu vào (Input)
{inp}

## Đầu ra (Output)
{out}

## Ví dụ mẫu
### Sample 1
Input:
```text
{s_in}```
Output:
```text
{s_out}```

## Ràng buộc dữ liệu
- Thời gian chạy: $\\le 1.0\\text{{s}}$
- Bộ nhớ: $\\le 256\\text{{MB}}$
"""
    with open(pdir / "De_Bai.md", "w", encoding="utf-8") as fp:
        fp.write(de_bai_content)
    with open(pdir / "solution.cpp", "w", encoding="utf-8") as fp:
        fp.write(sol)
    print(f"  ✅ Đã tạo Problem Package: {code}")

def main():
    print("🚀 Đang khởi tạo các bài tập bổ sung cho Level 2...")
    total_added = 0
    for lesson, probs in NEW_PROBLEMS.items():
        for code, title, desc, inp, out, s_in, s_out, sol in probs:
            create_problem_package(code, title, desc, inp, out, s_in, s_out, sol)
            total_added += 1
    print(f"🎉 Đã tạo thành công {total_added} bài tập mới chất lượng cao!")

if __name__ == "__main__":
    main()
