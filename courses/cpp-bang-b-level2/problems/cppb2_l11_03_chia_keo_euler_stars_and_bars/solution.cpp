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

long long nCr(long long n, long long r) {
    if (r < 0 || r > n) return 0;
    long long num = 1, den = 1;
    for (long long i = 0; i < r; ++i) {
        num = (num * (n - i)) % MOD;
        den = (den * (i + 1)) % MOD;
    }
    return num * power_mod(den, MOD - 2) % MOD;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, k;
    if (!(cin >> n >> k)) return 0;

    // C(n + k - 1, k - 1)
    cout << nCr(n + k - 1, k - 1) << "\n";
    return 0;
}
