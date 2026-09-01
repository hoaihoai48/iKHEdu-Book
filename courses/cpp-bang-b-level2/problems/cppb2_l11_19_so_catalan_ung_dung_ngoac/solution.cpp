#include <bits/stdc++.h>
using namespace std;

// Tính số Catalan thứ N modulo 10^9 + 7: C_n = (1 / (n + 1)) * C(2n, n)
const int MOD = 1000000007;

long long power(long long a, long long b) {
    long long res = 1;
    a %= MOD;
    while (b > 0) {
        if (b & 1) res = (res * a) % MOD;
        a = (a * a) % MOD;
        exp_shift: b >>= 1;
    }
    return res;
}

long long modInverse(long long n) {
    return power(n, MOD - 2);
}

long long nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    long long num = 1, den = 1;
    for (int i = 0; i < r; ++i) {
        num = (num * (n - i)) % MOD;
        den = (den * (i + 1)) % MOD;
    }
    return (num * modInverse(den)) % MOD;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    // Số Catalan C_n biểu diễn số cách đặt dãy n cặp ngoặc hợp lệ
    long long c_2n_n = nCr(2 * n, n);
    long long catalan = (c_2n_n * modInverse(n + 1)) % MOD;

    cout << catalan << "\n";
    return 0;
}
