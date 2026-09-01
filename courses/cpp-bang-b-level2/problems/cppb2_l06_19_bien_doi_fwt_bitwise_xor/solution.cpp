#include <bits/stdc++.h>
using namespace std;

// Fast Walsh-Hadamard Transform (FWT) tính tích chập XOR O(N log N)
const int MOD = 1000000007;
const int INV2 = 500000004; // 2^(MOD-2) % MOD

void FWT(vector<long long>& a, bool invert) {
    int n = a.size();
    for (int len = 1; 2 * len <= n; len <<= 1) {
        for (int i = 0; i < n; i += 2 * len) {
            for (int j = 0; j < len; ++j) {
                long long u = a[i + j];
                long long v = a[i + len + j];
                if (!invert) {
                    a[i + j] = (u + v) % MOD;
                    a[i + len + j] = (u - v + MOD) % MOD;
                } else {
                    a[i + j] = (u + v) % MOD * INV2 % MOD;
                    a[i + len + j] = (u - v + MOD) % MOD * INV2 % MOD;
                }
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    int sz = 1 << n;
    vector<long long> a(sz), b(sz);
    for (int i = 0; i < sz; ++i) cin >> a[i];
    for (int i = 0; i < sz; ++i) cin >> b[i];

    FWT(a, false);
    FWT(b, false);
    for (int i = 0; i < sz; ++i) a[i] = (a[i] * b[i]) % MOD;
    FWT(a, true);

    for (int i = 0; i < sz; ++i) cout << a[i] << " ";
    cout << "\n";
    return 0;
}
