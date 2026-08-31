#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> inv(n + 1);
    inv[1] = 1;
    long long sum_inv = 1;

    for (int i = 2; i <= n; ++i) {
        inv[i] = (MOD - (MOD / i) * inv[MOD % i] % MOD) % MOD;
        sum_inv = (sum_inv + inv[i]) % MOD;
    }

    cout << sum_inv << "\n";
    return 0;
}