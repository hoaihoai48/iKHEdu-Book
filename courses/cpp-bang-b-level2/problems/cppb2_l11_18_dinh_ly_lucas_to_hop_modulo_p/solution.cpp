#include <bits/stdc++.h>
using namespace std;

// Định lý Lucas tính C(n, k) % P với P là số nguyên tố nhỏ
long long C_small(long long n, long long k, long long p) {
    if (k < 0 || k > n) return 0;
    long long num = 1, den = 1;
    for (int i = 0; i < k; ++i) {
        num = (num * (n - i)) % p;
        den = (den * (i + 1)) % p;
    }
    // Nghịch đảo Fermat
    long long inv = 1, base = den, exp = p - 2;
    while (exp > 0) {
        if (exp & 1) inv = (inv * base) % p;
        base = (base * base) % p;
        exp >>= 1;
    }
    return (num * inv) % p;
}

long long lucas(long long n, long long k, long long p) {
    if (k == 0) return 1;
    return (lucas(n / p, k / p, p) * C_small(n % p, k % p, p)) % p;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (!(cin >> t)) return 0;

    while (t--) {
        long long n, k, p;
        cin >> n >> k >> p;
        cout << lucas(n, k, p) << "\n";
    }
    return 0;
}
