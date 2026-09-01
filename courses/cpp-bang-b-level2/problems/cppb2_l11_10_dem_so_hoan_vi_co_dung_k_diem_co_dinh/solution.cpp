#include <bits/stdc++.h>
using namespace std;

long long nCr_small(long long n, long long r, long long p) {
    if (r < 0 || r > n) return 0;
    long long num = 1, den = 1;
    for (long long i = 0; i < r; ++i) {
        num = (num * (n - i)) % p;
        den = (den * (i + 1)) % p;
    }
    long long inv = 1, exp = p - 2;
    while (exp > 0) {
        if (exp & 1) inv = (inv * den) % p;
        den = (den * den) % p;
        exp >>= 1;
    }
    return (num * inv) % p;
}

long long lucas(long long n, long long r, long long p) {
    if (r == 0) return 1;
    return lucas(n / p, r / p, p) * nCr_small(n % p, r % p, p) % p;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        long long n, r, p;
        cin >> n >> r >> p;
        cout << lucas(n, r, p) << "\n";
    }
    return 0;
}
