#include <bits/stdc++.h>
using namespace std;
const long long MOD = 1000000007;
long long modpow(long long a, long long e) {
    long long r = 1; a %= MOD;
    while (e) { if (e & 1) r = r * a % MOD; a = a * a % MOD; e >>= 1; }
    return r;
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long N, K;
    if (!(cin >> N >> K)) return 0;
    int n = (int)N;
    vector<int> phi(n + 1);
    for (int i = 0; i <= n; i++) phi[i] = i;
    for (int i = 2; i <= n; i++) if (phi[i] == i)
        for (int j = i; j <= n; j += i) phi[j] -= phi[j] / i;
    long long sum = 0;
    for (long long d = 1; d * d <= N; d++) if (N % d == 0) {
        long long d1 = d, d2 = N / d;
        sum = (sum + (long long)phi[d1] * modpow(K, N / d1)) % MOD;
        if (d2 != d1) sum = (sum + (long long)phi[d2] * modpow(K, N / d2)) % MOD;
    }
    cout << sum * modpow(N % MOD, MOD - 2) % MOD << "\n";
    return 0;
}
