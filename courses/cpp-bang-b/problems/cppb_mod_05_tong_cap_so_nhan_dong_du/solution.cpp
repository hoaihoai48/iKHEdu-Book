#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

long long powerMod(long long a, long long b) {
    long long ans = 1;
    a %= MOD;
    while (b > 0) {
        if (b & 1) ans = (ans * a) % MOD;
        a = (a * a) % MOD;
        b >>= 1;
    }
    return ans;
}

long long sumGeo(long long a, long long k) {
    if (k == 0) return 0;
    if (k == 1) return 1;
    if (k % 2 == 0) {
        long long half = sumGeo(a, k / 2);
        return half * (1 + powerMod(a, k / 2)) % MOD;
    } else {
        return (1 + a * sumGeo(a, k - 1)) % MOD;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, n;
    if (!(cin >> a >> n)) return 0;

    cout << sumGeo(a, n + 1) << "\n";
    return 0;
}