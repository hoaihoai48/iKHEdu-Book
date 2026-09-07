#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

long long modpow(long long a, long long e) {
    long long r = 1;
    while (e > 0) {
        if (e & 1) r = (r * a) % MOD;
        a = (a * a) % MOD;
        e >>= 1;
    }
    return r;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;
    vector<int> ns(q), ks(q);
    int mx = 0;
    for (int i = 0; i < q; ++i) {
        cin >> ns[i] >> ks[i];
        mx = max(mx, ns[i]);
    }

    vector<long long> fact(mx + 1), invfact(mx + 1);
    fact[0] = 1;
    for (int i = 1; i <= mx; ++i) fact[i] = (fact[i - 1] * i) % MOD;
    invfact[mx] = modpow(fact[mx], MOD - 2);
    for (int i = mx; i > 0; --i) invfact[i - 1] = (invfact[i] * i) % MOD;

    for (int i = 0; i < q; ++i) {
        int n = ns[i], k = ks[i];
        long long ans = 0;
        if (k >= 0 && k <= n) {
            ans = fact[n];
            ans = (ans * invfact[k]) % MOD;
            ans = (ans * invfact[n - k]) % MOD;
        }
        cout << ans << "\n";
    }
    return 0;
}
