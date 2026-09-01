#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

long long power_mod(long long a, long long b, long long m) {
    long long res = 1; a %= m;
    while (b > 0) {
        if (b & 1) res = (res * a) % m;
        a = (a * a) % m;
        b >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        long long a, b, c;
        cin >> a >> b >> c;
        long long exp = power_mod(b, c, MOD - 1);
        long long ans = power_mod(a, exp, MOD);
        cout << ans << "\n";
    }
    return 0;
}
