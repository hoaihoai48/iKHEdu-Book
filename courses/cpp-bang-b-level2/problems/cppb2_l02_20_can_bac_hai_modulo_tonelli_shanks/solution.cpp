#include <bits/stdc++.h>
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
    if (n == 0) { cout << 0 << "\n"; return 0; }
    if (p == 2) { cout << n << "\n"; return 0; }
    if (power(n, (p - 1) / 2, p) != 1) { cout << -1 << "\n"; return 0; }

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
    cout << ans << "\n";
    return 0;
}
