#include <bits/stdc++.h>
using namespace std;
const long long MOD = 1000000007;
long long modpow(long long a, long long e) {
    long long r = 1;
    while (e) { if (e & 1) r = r * a % MOD; a = a * a % MOD; e >>= 1; }
    return r;
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, K;
    if (!(cin >> N >> K)) return 0;
    vector<long long> f(N + 1), inv(N + 1), D(N + 1);
    f[0] = 1;
    for (int i = 1; i <= N; i++) f[i] = f[i - 1] * i % MOD;
    inv[N] = modpow(f[N], MOD - 2);
    for (int i = N; i > 0; i--) inv[i - 1] = inv[i] * i % MOD;
    D[0] = 1;
    if (N >= 1) D[1] = 0;
    for (int i = 2; i <= N; i++) D[i] = (long long)(i - 1) * (D[i - 1] + D[i - 2]) % MOD;
    long long c = f[N] * inv[K] % MOD * inv[N - K] % MOD;
    cout << c * D[N - K] % MOD << "\n";
    return 0;
}
