#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long total_xor = 0;
    for (int b = 0; b < 60; ++b) {
        long long count1 = 0;
        for (int i = 0; i < n; ++i) {
            if ((a[i] >> b) & 1) count1++;
        }
        long long count0 = n - count1;
        long long pairs = (count1 * count0) % MOD;
        long long weight = (1LL << b) % MOD;
        total_xor = (total_xor + pairs * weight) % MOD;
    }

    cout << total_xor << "\n";
    return 0;
}
