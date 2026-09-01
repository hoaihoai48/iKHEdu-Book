#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

long long power_mod(long long a, long long b, long long m = MOD) {
    long long res = 1; a %= m;
    while (b > 0) {
        if (b & 1) res = (res * a) % m;
        a = (a * a) % m;
        b >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        long long p, q;
        cin >> p >> q;
        long long inv_q = power_mod(q, MOD - 2);
        long long ans = (p % MOD * inv_q) % MOD;
        cout << ans << "\n";
    }
    return 0;
}
