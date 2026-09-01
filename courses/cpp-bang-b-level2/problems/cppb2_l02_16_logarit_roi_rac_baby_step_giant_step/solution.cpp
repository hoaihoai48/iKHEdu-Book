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

long long baby_step_giant_step(long long a, long long b, long long m) {
    a %= m; b %= m;
    long long n = sqrt(m) + 1;

    unordered_map<long long, long long> table;
    long long cur = 1;
    for (long long q = 0; q <= n; ++q) {
        table[cur] = q;
        cur = (__int128_t)cur * a % m;
    }

    long long an = power_mod(a, n, m);
    long long an_inv = power_mod(an, m - 2, m); // khi m nguyên tố
    cur = b;

    for (long long p = 0; p <= n; ++p) {
        if (table.count(cur)) {
            long long ans = p * n + table[cur];
            return ans;
        }
        cur = (__int128_t)cur * an_inv % m;
    }
    return -1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, b, m;
    if (!(cin >> a >> b >> m)) return 0;

    cout << baby_step_giant_step(a, b, m) << "\n";
    return 0;
}
