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

long long geom_sum(long long a, long long n) {
    if (n == 0) return 1;
    if (n % 2 == 1) {
        long long half = geom_sum(a, n / 2);
        long long p = power_mod(a, n / 2 + 1);
        return (half * (1 + p)) % MOD;
    } else {
        return (geom_sum(a, n - 1) + power_mod(a, n)) % MOD;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, n;
    if (!(cin >> a >> n)) return 0;

    cout << geom_sum(a, n) << "\n";
    return 0;
}
