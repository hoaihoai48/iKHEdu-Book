#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

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

    vector<long long> fact(n + 1), invFact(n + 1), D(n + 1, 0);
    fact[0] = 1;
    for (int i = 1; i <= n; ++i) fact[i] = fact[i - 1] * i % MOD;
    invFact[n] = power_mod(fact[n], MOD - 2);
    for (int i = n - 1; i >= 0; --i) invFact[i] = invFact[i + 1] * (i + 1) % MOD;

    D[0] = 1; D[1] = 0;
    for (int i = 2; i <= n; ++i) D[i] = (i - 1) * (D[i - 1] + D[i - 2]) % MOD;

    auto nCr = [&](int n, int r) {
        if (r < 0 || r > n) return 0LL;
        return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
    };

    long long ans = nCr(n, k) * D[n - k] % MOD;
    cout << ans << "\n";
    return 0;
}
