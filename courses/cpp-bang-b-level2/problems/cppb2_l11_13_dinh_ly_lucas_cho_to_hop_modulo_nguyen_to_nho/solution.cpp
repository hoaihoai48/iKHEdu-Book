#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

long long gcd_val(long long a, long long b) {
    while (b) { a %= b; swap(a, b); }
    return a;
}

long long power_mod(long long a, long long b) {
    long long res = 1; a %= MOD;
    while (b > 0) {
        if (b & 1) res = (res * a) % MOD;
        a = (a * a) % MOD;
        b >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    long long total = 0;
    for (int i = 0; i < n; ++i) {
        total = (total + power_mod(k, gcd_val(i, n))) % MOD;
    }

    long long ans = total * power_mod(n, MOD - 2) % MOD;
    cout << ans << "\n";
    return 0;
}
