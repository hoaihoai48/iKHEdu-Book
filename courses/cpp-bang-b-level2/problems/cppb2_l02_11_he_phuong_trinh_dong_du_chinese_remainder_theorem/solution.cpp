#include <bits/stdc++.h>
using namespace std;

long long extgcd(long long a, long long b, long long &x, long long &y) {
    if (b == 0) { x = 1; y = 0; return a; }
    long long x1, y1;
    long long g = extgcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return g;
}

long long mod_inverse(long long a, long long m) {
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
        long long invMi = mod_inverse(Mi, m[i]);
        ans = (ans + (__int128_t)r[i] * Mi % M * invMi) % M;
    }

    cout << (ans % M + M) % M << "\n";
    return 0;
}
