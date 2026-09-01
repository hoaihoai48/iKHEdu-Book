#include <bits/stdc++.h>
using namespace std;

long long power_mod(long long a, long long b, long long m) {
    long long res = 1; a %= m;
    while (b > 0) {
        if (b & 1) res = (__int128_t)res * a % m;
        a = (__int128_t)a * a % m;
        b >>= 1;
    }
    return res;
}

long long tonelli_shanks(long long n, long long p) {
    n %= p;
    if (n == 0) return 0;
    if (p == 2) return n;
    if (power_mod(n, (p - 1) / 2, p) != 1) return -1; // Không có thặng dư bậc 2

    long long q = p - 1;
    long long s = 0;
    while (q % 2 == 0) {
        q /= 2;
        s++;
    }

    if (s == 1) {
        return power_mod(n, (p + 1) / 4, p);
    }

    long long z = 2;
    while (power_mod(z, (p - 1) / 2, p) == 1) z++;

    long long c = power_mod(z, q, p);
    long long r = power_mod(n, (q + 1) / 2, p);
    long long t = power_mod(n, q, p);
    long long m = s;

    while (t != 1) {
        long long temp = t;
        long long i = 0;
        for (; i < m; ++i) {
            if (temp == 1) break;
            temp = power_mod(temp, 2, p);
        }
        long long b = power_mod(c, 1LL << (m - i - 1), p);
        r = (__int128_t)r * b % p;
        c = (__int128_t)b * b % p;
        t = (__int128_t)t * c % p;
        m = i;
    }
    return r;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        long long n, p;
        cin >> n >> p;
        long long root = tonelli_shanks(n, p);
        if (root == -1) cout << "-1\n";
        else cout << min(root, p - root) << "\n";
    }
    return 0;
}
