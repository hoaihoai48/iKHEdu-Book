#include <bits/stdc++.h>
using namespace std;

const int MAXN = 2000000;
const long long MOD = 1000000007;

long long fact[MAXN + 1], invFact[MAXN + 1];

long long power_mod(long long a, long long b) {
    long long res = 1; a %= MOD;
    while (b > 0) {
        if (b & 1) res = (res * a) % MOD;
        a = (a * a) % MOD;
        b >>= 1;
    }
    return res;
}

void precompute() {
    fact[0] = 1;
    for (int i = 1; i <= MAXN; ++i) fact[i] = (fact[i - 1] * i) % MOD;
    invFact[MAXN] = power_mod(fact[MAXN], MOD - 2);
    for (int i = MAXN - 1; i >= 0; --i) {
        invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;
    }
}

long long catalan(int n) {
    long long c2n_n = fact[2 * n] * invFact[n] % MOD * invFact[n] % MOD;
    return c2n_n * power_mod(n + 1, MOD - 2) % MOD;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    precompute();

    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        int n;
        cin >> n;
        cout << catalan(n) << "\n";
    }
    return 0;
}
