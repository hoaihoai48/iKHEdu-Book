#include <bits/stdc++.h>
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

long long power_mod(long long a, long long b, long long m) {
    long long res = 1; a %= m;
    while (b > 0) {
        if (b & 1) res = (__int128_t)res * a % m;
        a = (__int128_t)a * a % m;
        b >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, m;
    string b_str;
    if (!(cin >> a >> b_str >> m)) return 0;

    long long phi = get_phi(m);
    long long b = 0;
    bool overflow = false;

    for (char c : b_str) {
        b = b * 10 + (c - '0');
        if (b >= phi) {
            overflow = true;
            b %= phi;
        }
    }

    if (overflow) b += phi;
    cout << power_mod(a, b, m) << "\n";
    return 0;
}
