#include <bits/stdc++.h>
using namespace std;
long long modpow(long long a, long long e, long long m) {
    long long r = 1 % m;
    a %= m;
    while (e) { if (e & 1) r = r * a % m; a = a * a % m; e >>= 1; }
    return r;
}
long long smallC(long long n, long long k, int p) {
    if (k < 0 || k > n) return 0;
    if (k > n - k) k = n - k;
    long long num = 1, den = 1;
    for (long long i = 1; i <= k; i++) { num = num * (n - k + i) % p; den = den * i % p; }
    return num * modpow(den, p - 2, p) % p;
}
long long lucas(long long n, long long k, int p) {
    if (k < 0 || k > n) return 0;
    long long r = 1;
    while (n > 0 || k > 0) {
        long long ni = n % p, ki = k % p;
        if (ki > ni) return 0;
        r = r * smallC(ni, ki, p) % p;
        n /= p; k /= p;
    }
    return r;
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    if (!(cin >> T)) return 0;
    while (T--) {
        long long N, K;
        int p;
        cin >> N >> K >> p;
        cout << lucas(N, K, p) % p << "\n";
    }
    return 0;
}
