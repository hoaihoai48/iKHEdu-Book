import os

base_problems_dir = "/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b-level2/problems"

solutions_l01 = {
    # 01: Ước Chung & Bội Chung Cơ Bản
    "cppb2_l01_01": """#include <bits/stdc++.h>
using namespace std;

long long gcd_val(long long a, long long b) {
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

long long lcm_val(long long a, long long b) {
    if (a == 0 || b == 0) return 0;
    return (a / gcd_val(a, b)) * b;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        long long a, b;
        cin >> a >> b;
        cout << gcd_val(a, b) << " " << lcm_val(a, b) << "\\n";
    }
    return 0;
}
""",

    # 02: Rút Gọn Mảng Phân Số Lớn
    "cppb2_l01_02": """#include <bits/stdc++.h>
using namespace std;

long long gcd_val(long long a, long long b) {
    a = abs(a); b = abs(b);
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    for (int i = 0; i < n; ++i) {
        long long num, den;
        cin >> num >> den;
        if (den < 0) {
            num = -num;
            den = -den;
        }
        long long g = gcd_val(num, den);
        cout << num / g << " " << den / g << "\\n";
    }
    return 0;
}
""",

    # 03: Sàng Ước Số Nguyên Tố Nhỏ Nhất (SPF)
    "cppb2_l01_03": """#include <bits/stdc++.h>
using namespace std;

const int MAXA = 1000000;
int spf[MAXA + 1];

void sieve_spf() {
    for (int i = 1; i <= MAXA; ++i) spf[i] = i;
    for (int i = 2; i * i <= MAXA; ++i) {
        if (spf[i] == i) {
            for (int j = i * i; j <= MAXA; j += i) {
                if (spf[j] == j) spf[j] = i;
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    sieve_spf();

    int q;
    if (!(cin >> q)) return 0;
    while (q--) {
        int x;
        cin >> x;
        cout << spf[x] << "\\n";
    }
    return 0;
}
""",

    # 04: Phân Tích Thừa Số Truy Vấn Nhanh
    "cppb2_l01_04": """#include <bits/stdc++.h>
using namespace std;

const int MAXA = 1000000;
int spf[MAXA + 1];

void sieve_spf() {
    for (int i = 1; i <= MAXA; ++i) spf[i] = i;
    for (int i = 2; i * i <= MAXA; ++i) {
        if (spf[i] == i) {
            for (int j = i * i; j <= MAXA; j += i) {
                if (spf[j] == j) spf[j] = i;
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    sieve_spf();

    int q;
    if (!(cin >> q)) return 0;
    while (q--) {
        int x;
        cin >> x;
        vector<pair<int, int>> factors;
        while (x > 1) {
            int p = spf[x];
            int cnt = 0;
            while (x % p == 0) {
                cnt++;
                x /= p;
            }
            factors.push_back({p, cnt});
        }
        for (int i = 0; i < (int)factors.size(); ++i) {
            cout << factors[i].first << "^" << factors[i].second << (i + 1 == (int)factors.size() ? "" : " * ");
        }
        cout << "\\n";
    }
    return 0;
}
""",

    # 05: Đếm Ước Số & Tổng Ước Số Nhanh
    "cppb2_l01_05": """#include <bits/stdc++.h>
using namespace std;

const int MAXA = 1000000;
int spf[MAXA + 1];

void sieve_spf() {
    for (int i = 1; i <= MAXA; ++i) spf[i] = i;
    for (int i = 2; i * i <= MAXA; ++i) {
        if (spf[i] == i) {
            for (int j = i * i; j <= MAXA; j += i) {
                if (spf[j] == j) spf[j] = i;
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    sieve_spf();

    int q;
    if (!(cin >> q)) return 0;
    while (q--) {
        int x;
        cin >> x;
        long long num_divisors = 1;
        long long sum_divisors = 1;

        while (x > 1) {
            int p = spf[x];
            int cnt = 0;
            long long p_pow = 1;
            long long cur_sum = 1;
            while (x % p == 0) {
                cnt++;
                p_pow *= p;
                cur_sum += p_pow;
                x /= p;
            }
            num_divisors *= (cnt + 1);
            sum_divisors *= cur_sum;
        }
        cout << num_divisors << " " << sum_divisors << "\\n";
    }
    return 0;
}
""",

    # 06: Sàng Nguyên Tố Đoạn [L, R]
    "cppb2_l01_06": """#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R;
    if (!(cin >> L >> R)) return 0;

    long long lim = sqrt(R);
    vector<bool> is_prime_small(lim + 1, true);
    vector<long long> primes;
    for (long long i = 2; i <= lim; ++i) {
        if (is_prime_small[i]) {
            primes.push_back(i);
            for (long long j = i * i; j <= lim; j += i) is_prime_small[j] = false;
        }
    }

    vector<bool> is_prime_range(R - L + 1, true);
    for (long long p : primes) {
        long long start = max(p * p, ((L + p - 1) / p) * p);
        for (long long j = start; j <= R; j += p) {
            is_prime_range[j - L] = false;
        }
    }

    if (L == 1) is_prime_range[0] = false;

    long long cnt = 0;
    for (long long i = 0; i <= R - L; ++i) {
        if (is_prime_range[i]) cnt++;
    }
    cout << cnt << "\\n";
    return 0;
}
""",

    # 07: Cặp Số Nguyên Tố Sinh Đôi Trong Đoạn
    "cppb2_l01_07": """#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R;
    if (!(cin >> L >> R)) return 0;

    long long lim = sqrt(R);
    vector<bool> is_prime_small(lim + 1, true);
    vector<long long> primes;
    for (long long i = 2; i <= lim; ++i) {
        if (is_prime_small[i]) {
            primes.push_back(i);
            for (long long j = i * i; j <= lim; j += i) is_prime_small[j] = false;
        }
    }

    vector<bool> is_prime_range(R - L + 1, true);
    for (long long p : primes) {
        long long start = max(p * p, ((L + p - 1) / p) * p);
        for (long long j = start; j <= R; j += p) {
            is_prime_range[j - L] = false;
        }
    }
    if (L == 1 && R >= 1) is_prime_range[0] = false;

    long long twin_count = 0;
    for (long long x = L; x + 2 <= R; ++x) {
        if (is_prime_range[x - L] && is_prime_range[x + 2 - L]) {
            twin_count++;
        }
    }
    cout << twin_count << "\\n";
    return 0;
}
""",

    # 08: Tìm Nghiệm Nguyên Phương Trình Diophantine
    "cppb2_l01_08": """#include <bits/stdc++.h>
using namespace std;

long long extgcd(long long a, long long b, long long &x, long long &y) {
    if (b == 0) {
        x = 1; y = 0;
        return a;
    }
    long long x1, y1;
    long long g = extgcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return g;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, b, c;
    if (!(cin >> a >> b >> c)) return 0;

    long long x0, y0;
    long long g = extgcd(abs(a), abs(b), x0, y0);

    if (c % g != 0) {
        cout << "-1\\n";
    } else {
        if (a < 0) x0 = -x0;
        if (b < 0) y0 = -y0;
        x0 *= (c / g);
        y0 *= (c / g);
        cout << x0 << " " << y0 << "\\n";
    }
    return 0;
}
""",

    # 09: Nghiệm Nguyên Dương Nhỏ Nhất
    "cppb2_l01_09": """#include <bits/stdc++.h>
using namespace std;

long long extgcd(long long a, long long b, long long &x, long long &y) {
    if (b == 0) {
        x = 1; y = 0;
        return a;
    }
    long long x1, y1;
    long long g = extgcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return g;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, b, c;
    if (!(cin >> a >> b >> c)) return 0;

    long long x0, y0;
    long long g = extgcd(a, b, x0, y0);

    if (c % g != 0) {
        cout << "-1\\n";
        return 0;
    }

    x0 *= (c / g);
    y0 *= (c / g);

    long long b_prime = b / g;
    long long a_prime = a / g;

    // x = x0 + k * b_prime > 0
    long long k = (-x0) / b_prime;
    while (x0 + k * b_prime <= 0) k++;
    while (x0 + (k - 1) * b_prime > 0) k--;

    long long x_min = x0 + k * b_prime;
    long long y_cor = (c - a * x_min) / b;

    cout << x_min << " " << y_cor << "\\n";
    return 0;
}
""",

    # 10: Hàm Phi Euler phi(N) Nhanh Với SPF
    "cppb2_l01_10": """#include <bits/stdc++.h>
using namespace std;

const int MAXA = 1000000;
int spf[MAXA + 1];

void sieve_spf() {
    for (int i = 1; i <= MAXA; ++i) spf[i] = i;
    for (int i = 2; i * i <= MAXA; ++i) {
        if (spf[i] == i) {
            for (int j = i * i; j <= MAXA; j += i) {
                if (spf[j] == j) spf[j] = i;
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    sieve_spf();

    int q;
    if (!(cin >> q)) return 0;
    while (q--) {
        int n;
        cin >> n;
        int ans = n;
        int temp = n;
        while (temp > 1) {
            int p = spf[temp];
            ans -= ans / p;
            while (temp % p == 0) temp /= p;
        }
        cout << ans << "\\n";
    }
    return 0;
}
""",

    # 11: Phân Tích Giai Thừa N! (Legendre)
    "cppb2_l01_11": """#include <bits/stdc++.h>
using namespace std;

long long legendre(long long n, long long p) {
    long long count = 0;
    while (n > 0) {
        count += n / p;
        n /= p;
    }
    return count;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, p;
    if (!(cin >> n >> p)) return 0;

    cout << legendre(n, p) << "\\n";
    return 0;
}
""",

    # 12: Số Ước Số Lẻ & Số Chính Phương
    "cppb2_l01_12": """#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long A, B;
    if (!(cin >> A >> B)) return 0;

    // Số có số lượng ước số lẻ chính là số chính phương
    long long r = sqrt(B);
    long long l = ceil(sqrt(A));

    long long ans = max(0LL, r - l + 1);
    cout << ans << "\\n";
    return 0;
}
""",

    # 13: Cặp Số Có GCD và LCM Cho Trước
    "cppb2_l01_13": """#include <bits/stdc++.h>
using namespace std;

long long gcd_val(long long a, long long b) {
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long G, L;
    if (!(cin >> G >> L)) return 0;

    if (L % G != 0) {
        cout << "0\\n";
        return 0;
    }

    long long prod = L / G;
    long long count = 0;

    for (long long x = 1; x * x <= prod; ++x) {
        if (prod % x == 0) {
            long long y = prod / x;
            if (gcd_val(x, y) == 1) {
                count++;
            }
        }
    }

    cout << count << "\\n";
    return 0;
}
""",

    # 14: Khoảng Cách Cực Đại Giữa Hai Số Nguyên Tố
    "cppb2_l01_14": """#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R;
    if (!(cin >> L >> R)) return 0;

    long long lim = sqrt(R);
    vector<bool> is_prime_small(lim + 1, true);
    vector<long long> primes;
    for (long long i = 2; i <= lim; ++i) {
        if (is_prime_small[i]) {
            primes.push_back(i);
            for (long long j = i * i; j <= lim; j += i) is_prime_small[j] = false;
        }
    }

    vector<bool> is_prime_range(R - L + 1, true);
    for (long long p : primes) {
        long long start = max(p * p, ((L + p - 1) / p) * p);
        for (long long j = start; j <= R; j += p) {
            is_prime_range[j - L] = false;
        }
    }
    if (L == 1 && R >= 1) is_prime_range[0] = false;

    vector<long long> seg_primes;
    for (long long i = 0; i <= R - L; ++i) {
        if (is_prime_range[i]) seg_primes.push_back(L + i);
    }

    if (seg_primes.size() < 2) {
        cout << "-1\\n";
        return 0;
    }

    long long max_gap = 0;
    for (size_t i = 1; i < seg_primes.size(); ++i) {
        max_gap = max(max_gap, seg_primes[i] - seg_primes[i - 1]);
    }
    cout << max_gap << "\\n";
    return 0;
}
""",

    # 15: Phương Trình Đổi Tiền Xu Diophantine
    "cppb2_l01_15": """#include <bits/stdc++.h>
using namespace std;

long long extgcd(long long a, long long b, long long &x, long long &y) {
    if (b == 0) {
        x = 1; y = 0;
        return a;
    }
    long long x1, y1;
    long long g = extgcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return g;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, b, S;
    if (!(cin >> a >> b >> S)) return 0;

    long long x0, y0;
    long long g = extgcd(a, b, x0, y0);

    if (S % g != 0) {
        cout << "-1\\n";
        return 0;
    }

    x0 *= (S / g);
    y0 *= (S / g);

    long long b_prime = b / g;
    long long a_prime = a / g;

    // x = x0 + k * b_prime >= 0, y = y0 - k * a_prime >= 0
    // k >= -x0 / b_prime, k <= y0 / a_prime
    long long k_min = ceil((double)(-x0) / b_prime);
    long long k_max = floor((double)(y0) / a_prime);

    if (k_min > k_max) {
        cout << "-1\\n";
        return 0;
    }

    // Tối thiểu hóa tổng số tờ: x + y = x0 + y0 + k*(b_prime - a_prime)
    long long min_coins = 2e18;
    for (long long k : {k_min, k_max}) {
        long long cur_x = x0 + k * b_prime;
        long long cur_y = y0 - k * a_prime;
        if (cur_x >= 0 && cur_y >= 0) {
            min_coins = min(min_coins, cur_x + cur_y);
        }
    }
    cout << min_coins << "\\n";
    return 0;
}
""",

    # 16: Tổng gcd(i, N) Với 1 <= i <= N
    "cppb2_l01_16": """#include <bits/stdc++.h>
using namespace std;

long long get_phi(long long n) {
    long long res = n;
    for (long long p = 2; p * p <= n; ++p) {
        if (n % p == 0) {
            while (n % p == 0) n /= p;
            res -= res / p;
        }
    }
    if (n > 1) res -= res / n;
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;

    long long total_sum = 0;
    for (long long d = 1; d * d <= n; ++d) {
        if (n % d == 0) {
            total_sum += d * get_phi(n / d);
            if (d * d != n) {
                long long other_d = n / d;
                total_sum += other_d * get_phi(n / other_d);
            }
        }
    }
    cout << total_sum << "\\n";
    return 0;
}
"""
}

# Ghi các solution cho Lesson 01
for prefix, code_content in solutions_l01.items():
    matching_dirs = glob.glob(os.path.join(base_problems_dir, f"{prefix}_*"))
    for d in matching_dirs:
        sol_path = os.path.join(d, "solution.cpp")
        with open(sol_path, "w", encoding="utf-8") as f:
            f.write(code_content)

print(f"✅ Đã ghi hoàn tất 16 mã giải chuẩn thuật toán cho Lesson 01!")
