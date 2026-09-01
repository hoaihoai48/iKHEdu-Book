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

// S(n) = 1 + a + a^2 + ... + a^n
long long sum_geom(long long a, long long n) {
    if (n == 0) return 1;
    if (n % 2 == 1) {
        long long half = sum_geom(a, n / 2);
        long long a_half = power_mod(a, n / 2 + 1);
        return (half * (1 + a_half)) % MOD;
    } else {
        return (sum_geom(a, n - 1) + power_mod(a, n)) % MOD;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        long long a, n;
        cin >> a >> n;
        cout << sum_geom(a, n) << "\n";
    }
    return 0;
}
